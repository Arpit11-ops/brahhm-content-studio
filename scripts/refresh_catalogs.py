"""
Refresh public product catalogs for Brahhm brands.

Fetches /products.json from each Shopify storefront, paginating 250 at a time,
normalizes the payload, and writes one JSON per brand into research/catalogs/.
Also writes a summary INDEX.json with counts + last-fetched timestamps.

Run one-shot:  python scripts/refresh_catalogs.py
Cron-friendly: exit code non-zero if any brand fails; partial writes still land.

Caveman.co.in is intentionally skipped: it force-redirects /products.json to a
lander page, so no public catalog is exposed. Revisit if that changes.
"""

from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

BRANDS = {
    "biomart": "biomart.in",
    "healthfields": "healthfields.in",
    "pusht": "pusht.in",
}

OUT_DIR = Path(__file__).resolve().parent.parent / "research" / "catalogs"
PAGE_SIZE = 250
MAX_PAGES = 20
UA = "Mozilla/5.0 (BrahhmCatalogRefresh/1.0)"


def fetch_page(domain: str, page: int) -> list[dict]:
    url = f"https://{domain}/products.json?limit={PAGE_SIZE}&page={page}"
    req = Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urlopen(req, timeout=30) as r:
        body = r.read().decode("utf-8", errors="replace")
    data = json.loads(body)
    return data.get("products", [])


def normalize(brand: str, domain: str, product: dict) -> dict:
    variants = product.get("variants") or []
    any_in_stock = any(v.get("available") for v in variants)
    prices = [float(v["price"]) for v in variants if v.get("price")]
    return {
        "brand": brand,
        "handle": product.get("handle"),
        "title": product.get("title"),
        "url": f"https://{domain}/products/{product.get('handle')}",
        "product_type": product.get("product_type") or "",
        "tags": product.get("tags") or [],
        "in_stock": any_in_stock,
        "price_min": min(prices) if prices else None,
        "price_max": max(prices) if prices else None,
        "variant_count": len(variants),
        "images": [img.get("src") for img in (product.get("images") or []) if img.get("src")],
        "published_at": product.get("published_at"),
        "updated_at": product.get("updated_at"),
    }


def pull_brand(brand: str, domain: str) -> tuple[list[dict], str | None]:
    all_products: list[dict] = []
    for page in range(1, MAX_PAGES + 1):
        try:
            raw = fetch_page(domain, page)
        except (URLError, HTTPError, TimeoutError) as e:
            return all_products, f"page {page} fetch failed: {e}"
        except json.JSONDecodeError as e:
            return all_products, f"page {page} bad JSON: {e}"
        if not raw:
            break
        all_products.extend(normalize(brand, domain, p) for p in raw)
        if len(raw) < PAGE_SIZE:
            break
        time.sleep(0.3)
    return all_products, None


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    index = {"generated_at": ts, "brands": {}, "skipped": {"caveman": "products.json redirects to /lander"}}
    errors: list[str] = []

    for brand, domain in BRANDS.items():
        print(f"[{brand}] pulling https://{domain}/products.json ...", flush=True)
        products, err = pull_brand(brand, domain)
        in_stock = sum(1 for p in products if p["in_stock"])
        payload = {
            "brand": brand,
            "domain": domain,
            "generated_at": ts,
            "product_count": len(products),
            "in_stock_count": in_stock,
            "error": err,
            "products": products,
        }
        out = OUT_DIR / f"{brand}_catalog.json"
        out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        index["brands"][brand] = {
            "domain": domain,
            "file": out.name,
            "product_count": len(products),
            "in_stock_count": in_stock,
            "error": err,
        }
        print(f"[{brand}] wrote {len(products)} products ({in_stock} in stock) -> {out.name}"
              + (f"  [WARN: {err}]" if err else ""), flush=True)
        if err:
            errors.append(f"{brand}: {err}")

    (OUT_DIR / "INDEX.json").write_text(json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nINDEX.json written. Errors: {len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

import os
import sqlite3
import urllib.request
import urllib.parse
import urllib.error
import re
import json
import time
from html.parser import HTMLParser
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP Server
mcp = FastMCP("Brahhm Content Studio Helper")

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
DB_PATH = os.path.join(BASE_DIR, "studio_intelligence.db")
REFERENCE_LIB_DIR = os.path.join(BASE_DIR, "reference_library")
REFERENCE_INDEX_PATH = os.path.join(REFERENCE_LIB_DIR, "INDEX.json")

# Load .env from project root (no extra dependency)
def _load_dotenv():
    env_path = os.path.join(PROJECT_ROOT, ".env")
    if not os.path.exists(env_path):
        return
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            os.environ.setdefault(k.strip(), v.strip())

_load_dotenv()

# Text Extractor for HTML Scraping
class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_content = []
        self.ignored_tag_depth = 0
        self.ignored_tags = {"script", "style", "nav", "footer", "header", "head"}

    def handle_starttag(self, tag, attrs):
        if tag in self.ignored_tags:
            self.ignored_tag_depth += 1

    def handle_endtag(self, tag):
        if tag in self.ignored_tags:
            self.ignored_tag_depth = max(0, self.ignored_tag_depth - 1)

    def handle_data(self, data):
        if self.ignored_tag_depth == 0:
            clean_data = data.strip()
            if clean_data:
                self.text_content.append(clean_data)

    def get_text(self):
        return "\n".join(self.text_content)

@mcp.tool()
def query_studio_db(sql_query: str) -> str:
    """Execute a read-only SQL query on the competitor benchmark database (studio_intelligence.db).
    Use this to fetch viral posts, metrics, captions, and hashtags.
    """
    clean_sql = sql_query.strip()
    if not clean_sql.upper().startswith("SELECT"):
        return "Error: Only SELECT queries are permitted for database safety."
        
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(clean_sql)
        rows = cursor.fetchall()
        
        # Get column names
        cols = [desc[0] for desc in cursor.description]
        conn.close()
        
        # Format as table
        result = [" | ".join(cols)]
        result.append("-+-".join("-" * len(col) for col in cols))
        for r in rows:
            result.append(" | ".join(str(cell) for cell in r))
            
        return "\n".join(result)
    except Exception as e:
        return f"Error executing query: {e}"

@mcp.tool()
def fetch_product_page(url: str) -> str:
    """Fetch raw text descriptions and ingredients list from a live brand product URL.
    Use this to bypass the description gate when a product is not in cache.
    """
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')
            
        parser = TextExtractor()
        parser.feed(html)
        raw_text = parser.get_text()
        
        # Clean and limit content size to avoid context bloat
        lines = [line.strip() for line in raw_text.split('\n') if len(line.strip()) > 15]
        return "\n".join(lines[:40])
    except Exception as e:
        return f"Error fetching product URL: {e}"

@mcp.tool()
def search_duckduckgo(query: str) -> str:
    """Search DuckDuckGo for trending food guidelines, campaigns, and news in India.
    """
    try:
        url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')
            
        def strip_tags(text):
            return re.sub('<[^<]+?>', '', text).strip()
            
        # 1. Broad regex to match any <a> tag whose class contains "snippet"
        matches = re.findall(r'<a[^>]*class="[^"]*snippet[^"]*"[^>]*>(.*?)</a>', html, re.DOTALL | re.IGNORECASE)
        
        # 2. Fallback to any element containing "snippet" in class
        if not matches:
            matches = re.findall(r'<[a-z0-9]+[^>]*class="[^"]*snippet[^"]*"[^>]*>(.*?)<\/[a-z0-9]+>', html, re.DOTALL | re.IGNORECASE)
            
        results = []
        for match in matches:
            cleaned = strip_tags(match)
            cleaned = re.sub(r'\s+', ' ', cleaned)
            if len(cleaned) > 20:  # Only count meaningful snippets
                results.append(cleaned)
                if len(results) >= 5:
                    break
                    
        formatted_results = []
        for idx, res in enumerate(results):
            formatted_results.append(f"{idx+1}. {res}")
            
        if not formatted_results:
            if "ddg-lms" in html or "Oops, that's an error" in html or "rate limit" in html.lower():
                return "Error: DuckDuckGo search was rate limited or blocked by protection."
            elif len(html.strip()) > 500:
                return "Warning: DuckDuckGo search returned page HTML, but the scraper could not extract results. The page structure may have changed."
            else:
                return "No search results found."
                
        return "\n".join(formatted_results)
    except Exception as e:
        return f"Error executing DuckDuckGo search: {e}"

# ---------------------------------------------------------------------------
# Pinterest reference scraper (Apify-backed)
# ---------------------------------------------------------------------------

APIFY_ACTOR = "memo23~pinterest-scraper"
APIFY_RUN_SYNC_URL = (
    f"https://api.apify.com/v2/acts/{APIFY_ACTOR}/run-sync-get-dataset-items"
)
PIN_FIELDS = [
    "id",
    "title",
    "description",
    "auto_alt_text",
    "images.736x.url",
    "url",
    "repin_count",
    "aggregated_pin_data.aggregated_stats.saves",
    "domain",
    "is_video",
    "dominant_color",
]

def _slugify(text: str) -> str:
    text = re.sub(r"[^A-Za-z0-9]+", "-", text.lower()).strip("-")
    return text[:60] or "ref"

def _pin_saves(pin: dict) -> int:
    saves = pin.get("aggregated_pin_data.aggregated_stats.saves")
    if saves is None:
        # non-flattened response fallback
        agg = (pin.get("aggregated_pin_data") or {}).get("aggregated_stats") or {}
        saves = agg.get("saves")
    return saves or 0

def _normalize_pin(pin: dict) -> dict:
    image_url = pin.get("images.736x.url")
    if not image_url:
        images = pin.get("images") or {}
        image_url = (images.get("736x") or {}).get("url")
    return {
        "id": pin.get("id"),
        "title": (pin.get("title") or "").strip(),
        "description": (pin.get("description") or "").strip()[:280],
        "alt": (pin.get("auto_alt_text") or "").strip(),
        "image_url": image_url,
        "pin_url": pin.get("url"),
        "saves": _pin_saves(pin),
        "domain": pin.get("domain"),
        "dominant_color": pin.get("dominant_color"),
        "is_video": bool(pin.get("is_video")),
    }

def _apify_run_sync(input_payload: dict, timeout_secs: int = 110) -> list:
    token = os.environ.get("APIFY_API_TOKEN")
    if not token:
        raise RuntimeError("APIFY_API_TOKEN missing from environment (.env)")
    url = f"{APIFY_RUN_SYNC_URL}?token={token}&clean=true"
    body = json.dumps(input_payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout_secs) as resp:
        raw = resp.read().decode("utf-8", errors="ignore")
    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Apify returned non-JSON response: {e}")

def _load_index() -> dict:
    if not os.path.exists(REFERENCE_INDEX_PATH):
        return {"entries": []}
    try:
        with open(REFERENCE_INDEX_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"entries": []}

def _save_index(index: dict) -> None:
    os.makedirs(REFERENCE_LIB_DIR, exist_ok=True)
    with open(REFERENCE_INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

@mcp.tool()
def search_pinterest_references(
    queries: list[str],
    max_items_per_query: int = 8,
    tag: str = "",
    save_to_library: bool = True,
) -> str:
    """Search Pinterest for design reference pins via the memo23 Apify scraper.

    Use this when you need visual reference designs for a post — carousel templates,
    editorial flatlays, brand identity boards, product photography styles, etc.

    Each query string is sent verbatim to Pinterest's search. Use Pinterest user
    phrasing (e.g. "instagram carousel design", "grocery haul instagram") rather
    than marketer jargon ("template grocery", "post design system") — the latter
    returns zero hits.

    Returns a compact ranked list grouped by query, sorted by save count.

    Cost: ~$0.012 per query (8 items @ $0.00145 + $0.0086 actor start). Hard cap
    of 20 items per query and 5 queries per call enforced to keep spend bounded.

    Args:
        queries: List of Pinterest search strings (max 5).
        max_items_per_query: Pins per query, max 20.
        tag: Short label saved with the run (e.g. "biomart-pantry-restock-carousel").
        save_to_library: Persist results to research/reference_library/ + update INDEX.json.

    Returns:
        Human-readable ranked list per query plus a library file path if saved.
    """
    queries = [q.strip() for q in (queries or []) if q and q.strip()]
    if not queries:
        return "Error: provide at least one search query."
    if len(queries) > 5:
        return "Error: max 5 queries per call (cost cap)."
    max_items_per_query = max(1, min(int(max_items_per_query or 8), 20))

    total_items = max_items_per_query * len(queries)
    payload = {
        "searchQueries": queries,
        "searchScope": "pins",
        "maxItems": total_items,
        "maxSearchPages": 1,
        "flattenedOutput": True,
    }

    started = time.time()
    try:
        raw_items = _apify_run_sync(payload, timeout_secs=180)
    except urllib.error.HTTPError as e:
        return f"Apify HTTP {e.code}: {e.reason}"
    except urllib.error.URLError as e:
        return f"Apify network error: {e.reason}"
    except Exception as e:
        return f"Apify call failed: {e}"
    elapsed = round(time.time() - started, 1)

    # Apify returns one flat list across queries — group by source query if possible.
    # The scraper doesn't tag pins with the originating query, so we keep them in
    # one ranked pool but record which queries seeded it.
    normalized = [_normalize_pin(p) for p in raw_items if isinstance(p, dict)]
    normalized = [p for p in normalized if p.get("image_url")]
    normalized.sort(key=lambda p: p["saves"], reverse=True)

    # Save to library
    saved_path = None
    if save_to_library and normalized:
        os.makedirs(REFERENCE_LIB_DIR, exist_ok=True)
        ts = time.strftime("%Y%m%d-%H%M%S")
        slug = _slugify(tag or queries[0])
        fname = f"{ts}_{slug}.json"
        saved_path = os.path.join(REFERENCE_LIB_DIR, fname)
        record = {
            "timestamp": ts,
            "tag": tag,
            "queries": queries,
            "max_items_per_query": max_items_per_query,
            "elapsed_secs": elapsed,
            "pin_count": len(normalized),
            "pins": normalized,
        }
        with open(saved_path, "w", encoding="utf-8") as f:
            json.dump(record, f, indent=2, ensure_ascii=False)
        index = _load_index()
        index["entries"].insert(0, {
            "timestamp": ts,
            "tag": tag,
            "queries": queries,
            "pin_count": len(normalized),
            "file": fname,
        })
        index["entries"] = index["entries"][:200]
        _save_index(index)

    # Format response
    lines = []
    lines.append(f"Pinterest references — {len(normalized)} pins in {elapsed}s")
    lines.append(f"Queries: {', '.join(queries)}")
    if saved_path:
        rel = os.path.relpath(saved_path, PROJECT_ROOT).replace(os.sep, "/")
        lines.append(f"Saved: {rel}")
    lines.append("")
    lines.append("Top picks (sorted by saves):")
    for i, pin in enumerate(normalized[:max(10, max_items_per_query)], 1):
        title = pin["title"] or pin["alt"][:80] or "(untitled)"
        lines.append(
            f"{i}. [{pin['saves']:>6} saves] {title[:80]}\n"
            f"   img: {pin['image_url']}\n"
            f"   pin: {pin['pin_url']}\n"
            f"   src: {pin['domain']}  color: {pin['dominant_color']}"
        )
    return "\n".join(lines)


@mcp.tool()
def list_reference_library(limit: int = 20, tag_contains: str = "") -> str:
    """List saved Pinterest reference runs from the local library.

    Args:
        limit: Max entries to return (default 20).
        tag_contains: Filter to entries whose tag contains this substring.

    Returns:
        Newest-first list of stored reference runs with tag, queries, and file path.
    """
    index = _load_index()
    entries = index.get("entries", [])
    if tag_contains:
        needle = tag_contains.lower()
        entries = [e for e in entries if needle in (e.get("tag") or "").lower()]
    entries = entries[: max(1, min(int(limit or 20), 100))]
    if not entries:
        return "Reference library is empty (or no match for filter)."
    out = [f"Reference library — {len(entries)} entries"]
    for e in entries:
        out.append(
            f"- {e['timestamp']}  pins={e['pin_count']}  tag={e.get('tag','-')}\n"
            f"   queries: {', '.join(e.get('queries', []))}\n"
            f"   file: research/reference_library/{e['file']}"
        )
    return "\n".join(out)


if __name__ == "__main__":
    mcp.run()

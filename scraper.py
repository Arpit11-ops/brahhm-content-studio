import os
import time
import json
import requests
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_ID = os.getenv("CLOUDFLARE_ACCOUNT_ID")
API_TOKEN = os.getenv("CLOUDFLARE_API_TOKEN")
BASE_URL = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/browser-rendering"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
}


def start_crawl(url, max_pages=20, response_format="markdown"):
    payload = {
        "url": url,
        "formats": [response_format],
        "limit": max_pages,
        "crawlPurposes": ["search", "ai-input"],
    }
    r = requests.post(f"{BASE_URL}/crawl", headers=HEADERS, json=payload)
    if not r.ok:
        print(f"API error {r.status_code}: {r.text}")
        r.raise_for_status()
    data = r.json()
    result = data.get("result")
    # API returns result as a plain job ID string
    job_id = result if isinstance(result, str) else result.get("id")
    print(f"Crawl started — job ID: {job_id}")
    return job_id


def poll_crawl(job_id, poll_interval=5, timeout=300):
    deadline = time.time() + timeout
    while time.time() < deadline:
        r = requests.get(f"{BASE_URL}/crawl/{job_id}", headers=HEADERS)
        r.raise_for_status()
        data = r.json().get("result", {})
        status = data.get("status")
        finished = data.get("finished", 0)
        total = data.get("total", "?")
        print(f"Status: {status} ({finished}/{total} pages)")
        if status == "completed":
            return data.get("records", [])
        if status in ("failed", "error"):
            raise RuntimeError(f"Crawl failed: {data}")
        time.sleep(poll_interval)
    raise TimeoutError("Crawl timed out")


def save_results(pages, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for page in pages:
            url = page.get("url", "")
            # API returns content under 'markdown', 'html', or 'content'
            content = page.get("markdown") or page.get("content") or page.get("html") or ""
            f.write(f"\n\n---\nURL: {url}\n---\n\n{content}\n")
    print(f"Saved {len(pages)} pages to {output_file}")


def crawl(url, max_pages=20, output_file=None):
    if not output_file:
        safe_name = url.replace("https://", "").replace("/", "_").rstrip("_")
        output_file = f"crawl_{safe_name}.md"
    job_id = start_crawl(url, max_pages=max_pages)
    pages = poll_crawl(job_id)
    save_results(pages, output_file)
    return output_file


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python scraper.py <url> [max_pages]")
        print("Example: python scraper.py https://mamaearth.in 15")
        sys.exit(1)
    target_url = sys.argv[1]
    max_p = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    crawl(target_url, max_pages=max_p)

import os
import sqlite3
import urllib.request
import urllib.parse
import re
from html.parser import HTMLParser
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP Server
mcp = FastMCP("Brahhm Content Studio Helper")

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "studio_intelligence.db")

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

if __name__ == "__main__":
    mcp.run()

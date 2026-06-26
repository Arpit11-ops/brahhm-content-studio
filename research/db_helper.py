import os
import sqlite3
import sys

# Define database file path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, "studio_intelligence.db")

def get_connection():
    return sqlite3.connect(DB_FILE)

def get_competitor_summary():
    """Returns a list of all competitors with their metrics and post counts."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.username, c.full_name, c.followers_count, c.follows_count, c.is_verified, COUNT(p.id)
        FROM competitors c
        LEFT JOIN posts p ON c.username = p.owner_username
        GROUP BY c.id
        ORDER BY c.followers_count DESC
    """)
    rows = cursor.fetchall()
    conn.close()
    return [{
        "username": r[0],
        "full_name": r[1],
        "followers_count": r[2],
        "follows_count": r[3],
        "is_verified": bool(r[4]),
        "post_count": r[5]
    } for r in rows]

def get_viral_posts(limit=5, media_type=None):
    """Returns top performing posts ranked by likes count."""
    conn = get_connection()
    cursor = conn.cursor()
    
    query = """
        SELECT owner_username, shortcode, type, likes_count, comments_count, views_count, timestamp, caption
        FROM posts
    """
    params = []
    
    if media_type:
        query += " WHERE type = ?"
        params.append(media_type)
        
    query += " ORDER BY likes_count DESC LIMIT ?"
    params.append(limit)
    
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return [{
        "username": r[0],
        "shortcode": r[1],
        "type": r[2],
        "likes": r[3],
        "comments": r[4],
        "views": r[5],
        "timestamp": r[6],
        "caption": r[7]
    } for r in rows]

def get_top_hashtags(limit=10):
    """Returns the most frequently used hashtags with their count."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT hashtag, COUNT(post_id) as count
        FROM post_hashtags
        GROUP BY hashtag
        ORDER BY count DESC
        LIMIT ?
    """, (limit,))
    rows = cursor.fetchall()
    conn.close()
    return [{"hashtag": r[0], "count": r[1]} for r in rows]

def search_posts_by_keyword(keyword, limit=5):
    """Searches captions for matching keywords."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT owner_username, shortcode, type, likes_count, comments_count, timestamp, caption
        FROM posts
        WHERE caption LIKE ?
        ORDER BY likes_count DESC
        LIMIT ?
    """, (f"%{keyword}%", limit))
    rows = cursor.fetchall()
    conn.close()
    return [{
        "username": r[0],
        "shortcode": r[1],
        "type": r[2],
        "likes": r[3],
        "comments": r[4],
        "timestamp": r[5],
        "caption": r[6]
    } for r in rows]

def search_by_hashtag(hashtag, limit=5):
    """Returns posts containing a specific hashtag, ranked by likes."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.owner_username, p.shortcode, p.type, p.likes_count, p.comments_count, p.timestamp, p.caption
        FROM posts p
        JOIN post_hashtags ph ON p.id = ph.post_id
        WHERE ph.hashtag = ?
        ORDER BY p.likes_count DESC
        LIMIT ?
    """, (hashtag.strip().lower(), limit))
    rows = cursor.fetchall()
    conn.close()
    return [{
        "username": r[0],
        "shortcode": r[1],
        "type": r[2],
        "likes": r[3],
        "comments": r[4],
        "timestamp": r[5],
        "caption": r[6]
    } for r in rows]

def print_table(headers, rows):
    """Print clean tabular format in terminal."""
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

    # Clean smart quotes and common unicode characters that crash CP1252 consoles
    cleaned_rows = []
    for row in rows:
        cleaned_row = []
        for cell in row:
            val = str(cell)
            val = val.replace('\u2019', "'").replace('\u2018', "'")
            val = val.replace('\u201c', '"').replace('\u201d', '"')
            val = val.replace('\u2013', '-').replace('\u2014', '-')
            cleaned_row.append(val)
        cleaned_rows.append(cleaned_row)

    # Find max widths
    widths = [len(h) for h in headers]
    for row in cleaned_rows:
        for idx, cell in enumerate(row):
            widths[idx] = max(widths[idx], len(cell))
            
    # Format line
    format_str = " | ".join([f"{{:<{w}}}" for w in widths])
    divider = "-+-".join(["-"*w for w in widths])
    
    print("\n" + format_str.format(*headers))
    print(divider)
    for row in cleaned_rows:
        try:
            print(format_str.format(*row))
        except UnicodeEncodeError:
            # Safe fallback print
            fallback_row = [c.encode('ascii', errors='replace').decode('ascii') for c in row]
            print(format_str.format(*fallback_row))
    print()

def main():
    if not os.path.exists(DB_FILE):
        print(f"Error: Database file not found at {DB_FILE}. Please run migrate_to_sqlite.py first.")
        sys.exit(1)
        
    if len(sys.argv) < 2:
        print("Brahhm Content Studio - SQL Intelligence CLI Helper")
        print("="*55)
        print("Usage:")
        print("  python research/db_helper.py competitors          - List all competitors")
        print("  python research/db_helper.py viral [limit]       - List top performing viral posts")
        print("  python research/db_helper.py hashtags [limit]    - Show top trending hashtags")
        print("  python research/db_helper.py search <keyword>    - Search captions for keywords")
        print("  python research/db_helper.py tag <hashtag>      - Find posts featuring a specific hashtag")
        sys.exit(0)
        
    cmd = sys.argv[1].lower()
    
    if cmd == "competitors":
        data = get_competitor_summary()
        headers = ["USERNAME", "FULL NAME", "FOLLOWERS", "FOLLOWING", "VERIFIED", "POSTS"]
        rows = [[d["username"], d["full_name"], f"{d['followers_count']:,}", f"{d['follows_count']:,}", "YES" if d["is_verified"] else "NO", d["post_count"]] for d in data]
        print_table(headers, rows)
        
    elif cmd == "viral":
        limit = int(sys.argv[2]) if len(sys.argv) > 2 else 5
        data = get_viral_posts(limit)
        headers = ["USERNAME", "SHORTCODE", "TYPE", "LIKES", "COMMENTS", "VIEWS", "CAPTION (SNIPPET)"]
        rows = []
        for d in data:
            cap = (d["caption"] or "").replace("\n", " ")
            cap_snip = cap[:40] + "..." if len(cap) > 40 else cap
            rows.append([d["username"], d["shortcode"], d["type"], f"{d['likes']:,}", f"{d['comments']:,}", f"{d['views']:,}", cap_snip])
        print_table(headers, rows)
        
    elif cmd == "hashtags":
        limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        data = get_top_hashtags(limit)
        headers = ["HASHTAG", "FREQUENCY COUNT"]
        rows = [[f"#{d['hashtag']}", d["count"]] for d in data]
        print_table(headers, rows)
        
    elif cmd == "search":
        if len(sys.argv) < 3:
            print("Error: Missing search keyword. Example: python research/db_helper.py search millet")
            sys.exit(1)
        keyword = sys.argv[2]
        data = search_posts_by_keyword(keyword)
        headers = ["USERNAME", "SHORTCODE", "TYPE", "LIKES", "COMMENTS", "CAPTION (SNIPPET)"]
        rows = []
        for d in data:
            cap = (d["caption"] or "").replace("\n", " ")
            cap_snip = cap[:40] + "..." if len(cap) > 40 else cap
            rows.append([d["username"], d["shortcode"], d["type"], f"{d['likes']:,}", f"{d['comments']:,}", cap_snip])
        print(f"Search results for keyword: '{keyword}'")
        print_table(headers, rows)
        
    elif cmd == "tag":
        if len(sys.argv) < 3:
            print("Error: Missing hashtag. Example: python research/db_helper.py tag organic")
            sys.exit(1)
        hashtag = sys.argv[2].replace("#", "")
        data = search_by_hashtag(hashtag)
        headers = ["USERNAME", "SHORTCODE", "TYPE", "LIKES", "COMMENTS", "CAPTION (SNIPPET)"]
        rows = []
        for d in data:
            cap = (d["caption"] or "").replace("\n", " ")
            cap_snip = cap[:40] + "..." if len(cap) > 40 else cap
            rows.append([d["username"], d["shortcode"], d["type"], f"{d['likes']:,}", f"{d['comments']:,}", cap_snip])
        print(f"Posts matching hashtag: '#{hashtag}'")
        print_table(headers, rows)
        
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()

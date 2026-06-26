import os
import json
import sqlite3
from datetime import datetime

# Define file paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COMPETITORS_JSON = os.path.join(BASE_DIR, "competitor_profiles_raw.json")
HASHTAG_JSON = os.path.join(BASE_DIR, "hashtag_raw.json")
DB_FILE = os.path.join(BASE_DIR, "studio_intelligence.db")

def parse_timestamp(ts_str):
    if not ts_str:
        return None
    try:
        # Standard iso format conversion
        return datetime.fromisoformat(ts_str.replace("Z", "+00:00")).isoformat()
    except Exception:
        return ts_str

def migrate():
    print("Starting SQLite Database Migration...")
    
    # Connect to SQLite database
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # 1. Create tables
    print("Creating tables...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS competitors (
            id TEXT PRIMARY KEY,
            username TEXT UNIQUE,
            full_name TEXT,
            url TEXT,
            biography TEXT,
            followers_count INTEGER,
            follows_count INTEGER,
            is_verified INTEGER
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id TEXT PRIMARY KEY,
            owner_username TEXT,
            shortcode TEXT,
            type TEXT,
            url TEXT,
            caption TEXT,
            likes_count INTEGER,
            comments_count INTEGER,
            views_count INTEGER,
            timestamp TEXT,
            source_file TEXT
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS post_hashtags (
            post_id TEXT,
            hashtag TEXT,
            PRIMARY KEY (post_id, hashtag),
            FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE
        )
    """)
    
    # Commit table creation
    conn.commit()
    
    # 2. Parse and migrate competitors profiles
    competitor_count = 0
    post_count = 0
    hashtag_relations = 0
    
    if os.path.exists(COMPETITORS_JSON):
        print(f"Parsing {COMPETITORS_JSON}...")
        with open(COMPETITORS_JSON, "r", encoding="utf-8") as f:
            try:
                competitors_data = json.load(f)
            except Exception as e:
                print(f"Error parsing competitors JSON: {e}")
                competitors_data = []
                
        for account in competitors_data:
            account_id = account.get("id") or account.get("username")
            if not account_id:
                continue
                
            username = account.get("username")
            full_name = account.get("fullName")
            url = account.get("url")
            biography = account.get("biography")
            followers_count = account.get("followersCount") or 0
            follows_count = account.get("followsCount") or 0
            is_verified = 1 if account.get("verified") else 0
            
            # Insert or replace competitor
            cursor.execute("""
                INSERT OR REPLACE INTO competitors 
                (id, username, full_name, url, biography, followers_count, follows_count, is_verified)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (account_id, username, full_name, url, biography, followers_count, follows_count, is_verified))
            competitor_count += 1
            
            # Detect any post lists in the account object
            # Instagram scrapers store posts in keys like 'latestPosts', 'latestIgtvVideos', 'posts', etc.
            posts_lists = []
            for key, val in account.items():
                if isinstance(val, list) and len(val) > 0 and isinstance(val[0], dict):
                    # Check if items look like posts (have id/shortCode and caption/likesCount)
                    if any(k in val[0] for k in ["shortCode", "caption", "likesCount"]):
                        posts_lists.append(val)
            
            # Flatten lists of posts
            all_posts = []
            for plist in posts_lists:
                all_posts.extend(plist)
                
            for post in all_posts:
                post_id = post.get("id") or post.get("shortCode")
                if not post_id:
                    continue
                
                shortcode = post.get("shortCode")
                post_type = post.get("type") or "Image"
                post_url = post.get("url")
                caption = post.get("caption")
                likes = post.get("likesCount") or 0
                comments = post.get("commentsCount") or 0
                views = post.get("videoViewCount") or 0
                ts = parse_timestamp(post.get("timestamp"))
                
                cursor.execute("""
                    INSERT OR REPLACE INTO posts 
                    (id, owner_username, shortcode, type, url, caption, likes_count, comments_count, views_count, timestamp, source_file)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (post_id, username, shortcode, post_type, post_url, caption, likes, comments, views, ts, "competitor_profiles_raw.json"))
                post_count += 1
                
                # Ingest hashtags
                hashtags = post.get("hashtags") or []
                for tag in hashtags:
                    if tag:
                        tag_clean = tag.strip().lower()
                        try:
                            cursor.execute("""
                                INSERT OR IGNORE INTO post_hashtags (post_id, hashtag)
                                VALUES (?, ?)
                            """, (post_id, tag_clean))
                            hashtag_relations += 1
                        except sqlite3.Error:
                            pass
        conn.commit()
    else:
        print(f"Warning: {COMPETITORS_JSON} not found!")

    # 3. Parse and migrate hashtag explores
    hashtag_post_count = 0
    if os.path.exists(HASHTAG_JSON):
        print(f"Parsing {HASHTAG_JSON}...")
        with open(HASHTAG_JSON, "r", encoding="utf-8") as f:
            try:
                hashtag_data = json.load(f)
            except Exception as e:
                print(f"Error parsing hashtag JSON: {e}")
                hashtag_data = []
                
        for post in hashtag_data:
            post_id = post.get("id") or post.get("shortCode")
            if not post_id:
                continue
                
            owner_username = post.get("ownerUsername") or post.get("ownerId")
            shortcode = post.get("shortCode")
            post_type = post.get("type") or "Image"
            post_url = post.get("url")
            caption = post.get("caption")
            likes = post.get("likesCount") or 0
            comments = post.get("commentsCount") or 0
            views = post.get("videoViewCount") or 0
            ts = parse_timestamp(post.get("timestamp"))
            
            # Insert or replace post
            cursor.execute("""
                INSERT OR REPLACE INTO posts 
                (id, owner_username, shortcode, type, url, caption, likes_count, comments_count, views_count, timestamp, source_file)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (post_id, owner_username, shortcode, post_type, post_url, caption, likes, comments, views, ts, "hashtag_raw.json"))
            hashtag_post_count += 1
            
            # Ingest hashtags
            hashtags = post.get("hashtags") or []
            for tag in hashtags:
                if tag:
                    tag_clean = tag.strip().lower()
                    try:
                        cursor.execute("""
                            INSERT OR IGNORE INTO post_hashtags (post_id, hashtag)
                            VALUES (?, ?)
                        """, (post_id, tag_clean))
                        hashtag_relations += 1
                    except sqlite3.Error:
                        pass
        conn.commit()
    else:
        print(f"Warning: {HASHTAG_JSON} not found!")

    # 4. Create Indexes for speed optimization
    print("Creating database indexes for query acceleration...")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_posts_owner ON posts(owner_username)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_posts_likes ON posts(likes_count DESC)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_posts_comments ON posts(comments_count DESC)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_hashtags_tag ON post_hashtags(hashtag)")
    conn.commit()
    
    # 5. Output Verification Counts
    cursor.execute("SELECT COUNT(*) FROM competitors")
    total_competitors = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM posts")
    total_posts = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM post_hashtags")
    total_hashtags = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(DISTINCT hashtag) FROM post_hashtags")
    unique_hashtags = cursor.fetchone()[0]
    
    conn.close()
    
    print("\n" + "="*40)
    print("SQLite Database Migration Completed Successfully!")
    print("="*40)
    print(f"Database File:       {DB_FILE}")
    print(f"Total Competitors:   {total_competitors}")
    print(f"Total Unique Posts:  {total_posts}")
    print(f"Unique Hashtags:    {unique_hashtags}")
    print(f"Hashtag Relations:   {total_hashtags}")
    print("="*40 + "\n")

if __name__ == "__main__":
    migrate()

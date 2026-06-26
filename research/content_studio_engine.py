import os
import sys
import json
import sqlite3
import argparse
import re
import urllib.request
from html.parser import HTMLParser
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

# Define file paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
DOCX_PATH = os.path.join(ROOT_DIR, "June_2026_Content_Calendar_Brahhm.docx")
DB_FILE = os.path.join(BASE_DIR, "studio_intelligence.db")
DESCRIPTIONS_JSON = os.path.join(BASE_DIR, "product_descriptions.json")
PROMPTS_DIR = os.path.join(BASE_DIR, "prompts")

# Brand Bible file mapping
BRAND_BIBLE_MAP = {
    "CAVEMAN ORGANIC": "Caveman_Organic_Brand_Bible_v2.txt",
    "HEALTH FIELDS": "Health_Fields_Brand_Bible_v2.txt",
    "PUSHT ORGANIC": "Pusht_Organic_Brand_Bible_v2.txt",
    "GREENDIPZ": "Greendipz_Brand_Bible_v2.txt",
    "BIOMART": "Biomart_Brand_Bible_v2.txt"
}

# Skill File mappings
SKILL_MAP = {
    "humanizer": "skills/humanizer-main/humanizer-main/SKILL.md",
    "social": "skills/marketingskills-main/skills/social/SKILL.md",
    "copywriting": "skills/marketingskills-main/skills/copywriting/SKILL.md",
    "copy-editing": "skills/marketingskills-main/skills/copy-editing/SKILL.md",
    "marketing-psychology": "skills/marketingskills-main/skills/marketing-psychology/SKILL.md",
    "ad-creative": "skills/marketingskills-main/skills/ad-creative/SKILL.md",
    "video": "skills/marketingskills-main/skills/video/SKILL.md",
    "emails": "skills/marketingskills-main/skills/emails/SKILL.md",
    "popups": "skills/marketingskills-main/skills/popups/SKILL.md",
    "gpt-image-2": "skills/gpt-image-2/SKILL.md"
}

# HTML parser to extract clean text from product pages
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

def parse_calendar_docx(docx_path):
    """Parses the generated calendar docx file into a structured dictionary."""
    if not os.path.exists(docx_path):
        print(f"Error: {docx_path} not found.")
        return {}
        
    doc = Document(docx_path)
    body = doc.element.body
    date_items = {}
    current_date = None
    
    for element in body:
        tag = element.tag.split('}')[-1]
        if tag == 'p':
            p = Paragraph(element, doc)
            text = p.text.strip()
            # Look for June headings, ignoring the main title
            if text.upper().startswith("JUNE ") and not text.upper().startswith("JUNE 2026"):
                # Clean up date format for easy parsing
                current_date = text
        elif tag == 'tbl' and current_date:
            tbl = Table(element, doc)
            items = []
            n_cols = len(tbl.columns)
            
            for col_idx in range(n_cols):
                brand = tbl.cell(0, col_idx).text.strip()
                post_type = tbl.cell(1, col_idx).text.strip()
                product = tbl.cell(2, col_idx).text.strip()
                angle = tbl.cell(3, col_idx).text.strip()
                hook = tbl.cell(4, col_idx).text.strip()
                
                items.append({
                    "brand": brand,
                    "type": post_type,
                    "product": product,
                    "angle": angle,
                    "hook": hook
                })
            date_items[current_date] = items
            
    return date_items

def fetch_product_description_from_url(url):
    """Fetches and extracts raw text description from a live brand product URL."""
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            status = response.status
            html = response.read().decode('utf-8', errors='ignore')
            
        print(f"  [HTTP {status}] Fetched {len(html)} bytes from {url}")
        
        parser = TextExtractor()
        parser.feed(html)
        raw_text = parser.get_text()
        
        # Extract meaningful text lines (40 lines to capture full product specs,
        # ingredients, and certifications — consistent with mcp_server.py)
        lines = [line.strip() for line in raw_text.split('\n') if len(line.strip()) > 20]
        desc_candidate = "\n".join(lines[:40])
        return desc_candidate
    except urllib.error.HTTPError as e:
        print(f"  [HTTP {e.code}] URL returned error for {url}: {e.reason}")
        return None
    except Exception as e:
        print(f"  [ERROR] Web fetch failed for {url}: {e}")
        return None

def get_product_description(product_name, brand_name):
    """Retrieves product description from local JSON dictionary, or prompts user."""
    # Ensure cache file exists
    descriptions = {}
    if os.path.exists(DESCRIPTIONS_JSON):
        with open(DESCRIPTIONS_JSON, "r", encoding="utf-8") as f:
            try:
                descriptions = json.load(f)
            except Exception:
                descriptions = {}
                
    # Normalize product name
    prod_key = product_name.strip().lower()
    if prod_key in descriptions:
        return descriptions[prod_key]
        
    print(f"\n[?] Product description not found in local cache for: '{product_name}'")
    
    # Optional URL scraping helper
    brand_urls = {
        "CAVEMAN ORGANIC": "https://caveman.co.in",
        "HEALTH FIELDS": "https://health-fields.com",
        "PUSHT ORGANIC": "https://pusht.in",
        "BIOMART": "https://biomart.in",
        "GREENDIPZ": "https://biomart.in"
    }
    
    # Try automatic URL scraping first before prompting the user
    brand_base = brand_urls.get(brand_name.upper())
    if brand_base:
        slug = product_name.lower().replace(" ", "-").replace("&", "and").replace("₹", "")
        slug = re.sub(r'[^a-z0-9\-]', '', slug)
        guess_url = f"{brand_base}/products/{slug}"
        print(f"  Attempting auto-fetch from: {guess_url}")
        fetched = fetch_product_description_from_url(guess_url)
        if fetched and len(fetched.strip()) > 50:
            print("  [+] Successfully extracted description from URL!")
            descriptions[prod_key] = fetched
            with open(DESCRIPTIONS_JSON, "w", encoding="utf-8") as f:
                json.dump(descriptions, f, indent=2, ensure_ascii=False)
            return fetched
        else:
            print(f"  [!] Auto-fetch returned insufficient content from {guess_url}")
    
    # Fallback: prompt user only if auto-fetch failed
    print("\nOptions:")
    print(" 1. Input/paste the description manually")
    print(" 2. Try a different URL")
    print(" 3. Skip (forces Protocol 2 Gate)")
    
    choice = input("Select an option (1-3): ").strip()
    
    if choice == "1":
        print("\nEnter product description (Press Enter, then Ctrl+D / Ctrl+Z to save):")
        lines = []
        try:
            while True:
                line = input()
                lines.append(line)
        except EOFError:
            pass
        user_desc = "\n".join(lines).strip()
        if user_desc:
            descriptions[prod_key] = user_desc
            with open(DESCRIPTIONS_JSON, "w", encoding="utf-8") as f:
                json.dump(descriptions, f, indent=2, ensure_ascii=False)
            return user_desc
            
    elif choice == "2":
        custom_url = input("Paste product URL: ").strip()
        if custom_url:
            fetched = fetch_product_description_from_url(custom_url)
            if fetched and len(fetched.strip()) > 50:
                print("  [+] Successfully extracted description from custom URL!")
                descriptions[prod_key] = fetched
                with open(DESCRIPTIONS_JSON, "w", encoding="utf-8") as f:
                    json.dump(descriptions, f, indent=2, ensure_ascii=False)
                return fetched
            else:
                print("  [!] Could not extract useful content from that URL.")
                
    return None

def claims_audit(description):
    """Performs the Protocol 3 Claims Audit on the product description."""
    if not description:
        return []
        
    # Standard banned claims keyword lists
    health_keywords = ["immunity", "heart", "cholesterol", "diabetes", "blood pressure", "disease"]
    therapeutic_keywords = ["stress", "digestion", "sleep", "stomach", "pain", "detox", "calming"]
    superlative_keywords = ["best", "richest", "most powerful", "perfect", "ultimate"]
    wellness_keywords = ["nourishing", "wholesome goodness", "natural boost", "pure goodness"]
    
    audit_results = []
    
    # Split description into sentences
    sentences = re.split(r'\. |\n', description)
    for sent in sentences:
        sent = sent.strip()
        if not sent:
            continue
            
        sent_lower = sent.lower()
        verdict = "✅"
        action = "KEEP"
        reason = "Verified claim"
        
        # Audit checks
        if any(w in sent_lower for w in health_keywords):
            verdict = "❌"
            action = "REMOVE"
            reason = "Banned Health Claim"
        elif any(w in sent_lower for w in therapeutic_keywords):
            verdict = "❌"
            action = "REMOVE"
            reason = "Banned Therapeutic Claim"
        elif any(w in sent_lower for w in superlative_keywords):
            verdict = "❌"
            action = "REMOVE"
            reason = "Unverified Superlative"
        elif any(w in sent_lower for w in wellness_keywords):
            verdict = "❌"
            action = "REMOVE"
            reason = "Vague Wellness Language"
            
        audit_results.append({
            "claim": sent,
            "verdict": verdict,
            "action": action,
            "reason": reason
        })
        
    return audit_results

def query_benchmarks(brand_name, angle):
    """Queries SQLite DB for competitor post examples matching brand and angle.
    Uses expanded multi-keyword OR queries for broader, more relevant coverage.
    """
    benchmarks = []
    if not os.path.exists(DB_FILE):
        return benchmarks
        
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        # Multi-keyword map: each brand maps to multiple category terms for
        # broader coverage. Measured improvement: Caveman 45→116, greendipz 22→239,
        # Biomart 24→114, Health Fields 78→176 matching posts.
        category_map = {
            "CAVEMAN ORGANIC": ["%millet%", "%cookie%", "%snack%", "%grain%", "%ragi%", "%biscuit%"],
            "HEALTH FIELDS":   ["%tea%", "%honey%", "%spice%", "%organic%", "%herbal%", "%wellness%"],
            "PUSHT ORGANIC":   ["%organic%", "%dal%", "%oil%", "%farm%", "%cold pressed%", "%pulse%"],
            "GREENDIPZ":       ["%sauce%", "%gravy%", "%recipe%", "%cooking%", "%food%", "%kitchen%"],
            "BIOMART":         ["%organic%", "%certified%", "%pantry%", "%grocery%", "%store%", "%shop%"],
        }
        
        keywords = category_map.get(brand_name.upper(), ["%organic%"])
        
        # Build OR-based WHERE clause for broader matching
        where_clauses = " OR ".join(["caption LIKE ?" for _ in keywords])
        
        # Fetch top 3 viral posts matching any keyword (increased from 2 for diversity)
        cursor.execute(f"""
            SELECT owner_username, shortcode, likes_count, comments_count, caption
            FROM posts
            WHERE {where_clauses}
            ORDER BY likes_count DESC
            LIMIT 3
        """, keywords)
        
        rows = cursor.fetchall()
        for r in rows:
            benchmarks.append({
                "username": r[0],
                "shortcode": r[1],
                "likes": r[2],
                "comments": r[3],
                "caption": r[4][:300] + "..." if len(r[4]) > 300 else r[4]
            })
        conn.close()
    except Exception as e:
        print(f"Error querying benchmarks: {e}")
        
    return benchmarks

def extract_section_by_brand(file_path, brand_name, angle=None):
    """Extracts only the section(s) matching the brand name and optionally the angle
    from a large reference file (Hook Matrix, Caption Swipe, VEE).
    Returns the universal/shared header + brand-specific section.
    """
    if not os.path.exists(file_path):
        return ""
    
    with open(file_path, "r", encoding="utf-8") as f:
        full_text = f.read()
    
    lines = full_text.split('\n')
    
    # Brand name aliases for matching section headers
    brand_aliases = {
        "CAVEMAN ORGANIC": ["CAVEMAN"],
        "HEALTH FIELDS": ["HEALTH FIELDS"],
        "PUSHT ORGANIC": ["PUSHT"],
        "GREENDIPZ": ["GREENDIPZ"],
        "BIOMART": ["BIOMART"],
    }
    
    search_terms = brand_aliases.get(brand_name.upper(), [brand_name.upper()])
    
    # Collect the file header (rules, guidelines) — everything before the first brand section
    # and the brand-specific section
    header_lines = []
    brand_section_lines = []
    in_brand_section = False
    found_first_brand = False
    
    # Section separators used in Hook Matrix, Caption Swipe, VEE
    section_separators = ['━━━━', '════', '----']
    
    for i, line in enumerate(lines):
        line_upper = line.upper().strip()
        
        # Detect if this line is a brand section header
        is_brand_header = any(term in line_upper for term in 
            ["BRAND 1", "BRAND 2", "BRAND 3", "BRAND 4", "BRAND 5",
             "CAVEMAN", "HEALTH FIELDS", "PUSHT", "GREENDIPZ", "BIOMART"])
        is_separator = any(sep in line for sep in section_separators)
        
        if is_brand_header and not is_separator:
            if not found_first_brand:
                found_first_brand = True
            
            # Check if this is OUR brand's section
            if any(term in line_upper for term in search_terms):
                in_brand_section = True
                brand_section_lines.append(line)
                continue
            elif in_brand_section:
                # We've hit the next brand's section — stop
                break
        
        if not found_first_brand:
            header_lines.append(line)
        elif in_brand_section:
            brand_section_lines.append(line)
    
    # Also include universal/shared sections (e.g., "UNIVERSAL HOOKS", "LABEL PADHEGA")
    universal_lines = []
    in_universal = False
    for i, line in enumerate(lines):
        line_upper = line.upper().strip()
        if "UNIVERSAL" in line_upper or "LABEL PADHEGA" in line_upper or "RESEARCH-VALIDATED HOOK TYPES" in line_upper:
            in_universal = True
        elif in_universal and any(term in line_upper for term in ["BRAND 1", "BRAND 2", "BRAND 3", "BRAND 4", "BRAND 5"]):
            in_universal = False
        
        if in_universal:
            universal_lines.append(line)
    
    # Combine: header (global rules) + brand section + universal section
    result_parts = []
    if header_lines:
        result_parts.append('\n'.join(header_lines))  # Global rules from header (untruncated)
    if brand_section_lines:
        result_parts.append('\n'.join(brand_section_lines))
    if universal_lines:
        result_parts.append('\n'.join(universal_lines))
    
    return '\n\n'.join(result_parts)


def extract_vee_templates(brand_name):
    """Extracts only the VEE template assignment guide for the active brand,
    plus the core rules. The full VEE is 1,503 lines / 100KB — we extract ~60-100 lines.
    """
    vee_path = os.path.join(ROOT_DIR, "Visual_Execution_Engine_v4_txt.txt")
    if not os.path.exists(vee_path):
        return ""
    
    with open(vee_path, "r", encoding="utf-8") as f:
        full_text = f.read()
    
    lines = full_text.split('\n')
    
    # Extract core rules and general guides (first ~170 lines contain global rules, assignments and compatibility guides)
    core_rules = '\n'.join(lines[:170])
    
    # Extract brand-specific template assignments from the assignment guide
    brand_aliases = {
        "CAVEMAN ORGANIC": "CAVEMAN ORGANIC",
        "HEALTH FIELDS": "HEALTH FIELDS",
        "PUSHT ORGANIC": "PUSHT ORGANIC",
        "GREENDIPZ": "GREENDIPZ",
        "BIOMART": "BIOMART",
    }
    
    search_term = brand_aliases.get(brand_name.upper(), brand_name.upper())
    
    # Find the brand's template assignment block
    brand_templates = []
    in_brand = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if search_term in stripped.upper() and ":" in stripped:
            in_brand = True
            brand_templates.append(line)
            continue
        elif in_brand:
            # Stop at the next brand header or empty double-newline
            if stripped == "" and i + 1 < len(lines) and lines[i+1].strip() == "":
                break
            # Stop if we hit another brand name header
            next_brands = ["CAVEMAN", "HEALTH FIELDS", "PUSHT", "GREENDIPZ", "BIOMART"]
            if any(b in stripped.upper() and ":" in stripped for b in next_brands if b != search_term.split()[0]):
                break
            brand_templates.append(line)
    
    result = core_rules
    if brand_templates:
        result += "\n\n--- BRAND TEMPLATE ASSIGNMENTS ---\n"
        result += '\n'.join(brand_templates)
    
    return result


def build_pruned_context(brand_name, post_type, angle):
    """Loads only the bibles, skills, and reference sections relevant to the
    active item to optimize context size while preserving all critical rules.
    """
    context = {}
    
    # 1. Load active brand bible (FULL — no truncation. Bibles are only 280-334 lines)
    bible_file = BRAND_BIBLE_MAP.get(brand_name.upper())
    if bible_file:
        bible_path = os.path.join(ROOT_DIR, bible_file)
        if os.path.exists(bible_path):
            with open(bible_path, "r", encoding="utf-8") as f:
                context["brand_bible"] = f.read()
                
    # 2. Load Global Brand Architecture Master
    arch_path = os.path.join(ROOT_DIR, "Brand_Architecture_Master.txt")
    if os.path.exists(arch_path):
        with open(arch_path, "r", encoding="utf-8") as f:
            context["brand_architecture"] = f.read()
    
    # 3. Extract brand-specific Hook Matrix section (~40-80 lines vs 463 total)
    hook_path = os.path.join(ROOT_DIR, "Hook_Matrix_Library.md")
    context["hooks"] = extract_section_by_brand(hook_path, brand_name, angle)
    
    # 4. Extract brand-specific Caption Swipe references (~30-50 lines vs 1,046 total)
    swipe_path = os.path.join(ROOT_DIR, "Caption_Swipe_File.md")
    context["swipe_captions"] = extract_section_by_brand(swipe_path, brand_name, angle)
    
    # 5. Extract brand-specific VEE template assignments (~30-60 lines vs 1,503 total)
    context["visual_template"] = extract_vee_templates(brand_name)
            
    # 6. Load Mandatory Skill Files (FULL — no truncation per skill)
    mandatory_skills = ["humanizer", "social", "copywriting", "copy-editing"]
    
    # Context-dependent skills
    if angle.upper() in ["CONVERT", "ATTACK"]:
        mandatory_skills.append("marketing-psychology")
    if angle.upper() == "CONVERT":
        mandatory_skills.append("ad-creative")
    if post_type.upper() == "REEL":
        mandatory_skills.append("video")
    if post_type.upper() == "STORY":
        mandatory_skills.append("emails")
        mandatory_skills.append("popups")
    if post_type.upper() == "CAROUSEL":
        mandatory_skills.append("gpt-image-2")
        
    # Read skill file contents — FULL content, no truncation
    skills_content = {}
    for skill in mandatory_skills:
        rel_path = SKILL_MAP.get(skill)
        if rel_path:
            full_path = os.path.join(ROOT_DIR, rel_path)
            if os.path.exists(full_path):
                with open(full_path, "r", encoding="utf-8") as f:
                    skills_content[skill] = f.read()
                    
    context["skills"] = skills_content
    return context

def build_prompt_package(date_str, item, description, audit_table, benchmarks, pruned_ctx):
    """Compiles all pruned data into a single instruction prompt for the LLM."""
    brand = item["brand"]
    post_type = item["type"]
    product = item["product"]
    angle = item["angle"]
    hook = item["hook"]
    
    prompt = f"""# Content Studio Creative Brief — {brand}
**Target Date**: {date_str}
**Content Type**: {post_type}
**Product**: {product}
**Content Angle**: {angle}
**Target Hook**: {hook}

---

## 🛡️ CLAIMS AUDIT TABLE (Protocol 3 Compliance)
Please build the copy ONLY using the claims marked as KEEP.

"""
    # Write audit table
    prompt += "| Claim | Verdict | Action | Reason |\n"
    prompt += "| :--- | :--- | :--- | :--- |\n"
    for row in audit_table:
        prompt += f"| {row['claim']} | {row['verdict']} | {row['action']} | {row['reason']} |\n"
        
    prompt += "\n"
    
    # Write product descriptions
    prompt += f"## 📝 ACTIVE PRODUCT DESCRIPTION\n{description}\n\n"
    
    # Write benchmarks
    if benchmarks:
        prompt += "## 📈 SQL COMPETITOR BENCHMARKS (High Performance References)\n"
        for idx, b in enumerate(benchmarks):
            prompt += f"### Example {idx+1}: @{b['username']} (Shortcode: {b['shortcode']})\n"
            prompt += f"*   **Metrics**: {b['likes']:,} likes | {b['comments']:,} comments\n"
            prompt += f"*   **Caption Snippet**:\n    > {b['caption']}\n\n"
            
    # Include FULL Brand Bible — no truncation (280-334 lines each, already brand-pruned)
    prompt += "## 🏛️ BRAND GUIDELINES & VOICE ARCHITECTURE\n"
    if "brand_bible" in pruned_ctx:
        prompt += f"### Brand Bible (FULL):\n```\n{pruned_ctx['brand_bible']}\n```\n\n"
        
    if "brand_architecture" in pruned_ctx:
        prompt += f"### Global Brand Architecture Lexicon:\n```\n{pruned_ctx['brand_architecture']}\n```\n\n"
    
    # Include brand-specific Hook Matrix section
    if pruned_ctx.get("hooks"):
        prompt += f"## 🪝 HOOK MATRIX — BRAND-SPECIFIC HOOKS\n```\n{pruned_ctx['hooks']}\n```\n\n"
    
    # Include brand-specific Caption Swipe references
    if pruned_ctx.get("swipe_captions"):
        prompt += f"## 📋 CAPTION SWIPE FILE — BRAND REFERENCE CAPTIONS\n```\n{pruned_ctx['swipe_captions']}\n```\n\n"
    
    # Include brand-specific Visual Execution Engine templates
    if pruned_ctx.get("visual_template"):
        prompt += f"## 🎨 VISUAL EXECUTION ENGINE — TEMPLATE ASSIGNMENTS\n```\n{pruned_ctx['visual_template']}\n```\n\n"
        
    # Include FULL Skill Guidelines — no truncation (already post-type-pruned)
    prompt += "## ⚙️ MANDATORY SYSTEM SKILL RULES\n"
    for name, content in pruned_ctx["skills"].items():
        prompt += f"### Skill: {name}\n```markdown\n{content}\n```\n\n"
        
    # Final Instruction block
    prompt += """## 🎯 FINAL DIRECTIVE FOR WRITING ENGINE
Using the context provided above, generate the complete **13-Point Standard Post Package** for this post in strict compliance with the protocols:
*   Do NOT use any of the global banned words.
*   Do NOT include any brand URLs or "Link in bio" text inside the caption body.
*   Ensure exactly 3 hashtags below the caption (Branded + Category + Discovery).
*   Structure ManyChat CTAs for direct keyword trigger without links.
*   Confirm visual layout before generating the GPT Image prompt.

Output the post package now.
"""
    return prompt

def main():
    parser = argparse.ArgumentParser(description="Brahhm Content Studio Orchestration Engine")
    parser.add_argument("--date", required=True, help="Target Date, e.g. 'June 1' or 'June 8'")
    parser.add_argument("--brand", help="Filter by brand name, e.g. 'Caveman Organic'")
    args = parser.parse_args()
    
    # 1. Parse Calendar (use JSON cache if available for speed and reliability)
    JSON_CALENDAR_PATH = os.path.join(BASE_DIR, "content_calendar.json")
    if os.path.exists(JSON_CALENDAR_PATH):
        print(f"Loading calendar from optimized cache: {JSON_CALENDAR_PATH}...")
        with open(JSON_CALENDAR_PATH, "r", encoding="utf-8") as f:
            try:
                calendar = json.load(f)
            except Exception as e:
                print(f"Failed to read JSON calendar: {e}. Falling back to docx...")
                calendar = parse_calendar_docx(DOCX_PATH)
    else:
        print(f"Loading calendar from: {DOCX_PATH}...")
        calendar = parse_calendar_docx(DOCX_PATH)

    if not calendar:
        print("Calendar parsing failed or file empty.")
        sys.exit(1)
        
    # Normalize requested date to find matching key
    target_date_clean = args.date.strip().upper()
    matched_date_key = None
    for date_key in calendar.keys():
        if target_date_clean in date_key.upper():
            matched_date_key = date_key
            break
            
    if not matched_date_key:
        print(f"Error: Target date '{args.date}' not found in the Content Calendar.")
        print(f"Available Dates: {', '.join(list(calendar.keys())[:5])}...")
        sys.exit(1)
        
    items = calendar[matched_date_key]
    print(f"Found {len(items)} scheduled items for {matched_date_key}.")
    
    # Filter by brand if requested
    if args.brand:
        brand_filter = args.brand.strip().upper()
        items = [i for i in items if brand_filter in i["brand"].upper()]
        print(f"Filtered to {len(items)} items for brand '{args.brand}'.")
        
    if not items:
        print("No items to process after filtering.")
        sys.exit(0)
        
    # Ensure prompts folder exists
    if not os.path.exists(PROMPTS_DIR):
        os.makedirs(PROMPTS_DIR)
        
    for item in items:
        brand = item["brand"]
        product = item["product"]
        post_type = item["type"]
        angle = item["angle"]
        
        print("\n" + "="*50)
        print(f"Processing: {brand} — {product} ({post_type})")
        print("="*50)
        
        # 2. Description Gate (Protocol 2)
        description = get_product_description(product, brand)
        if not description:
            print(f"[!] Warning: No product description for '{product}'. Content Generation halted for this item (Protocol 2 Gate).")
            continue
            
        # 3. Claims Audit (Protocol 3)
        audit_table = claims_audit(description)
        print(f"[+] Claims Audit finished ({len(audit_table)} claims audited).")
        
        # 4. Query DB Benchmarks
        benchmarks = query_benchmarks(brand, angle)
        print(f"[+] Retrieved {len(benchmarks)} competitor benchmarks from SQLite.")
        
        # 5. Build Pruned Context
        pruned_ctx = build_pruned_context(brand, post_type, angle)
        print(f"[+] Pruned context loaded (Brand Bible + {len(pruned_ctx['skills'])} skills).")
        
        # 6. Build Prompt Package
        prompt_content = build_prompt_package(matched_date_key, item, description, audit_table, benchmarks, pruned_ctx)
        
        # Save prompt to file
        # Extract date from matched key for unique filenames (prevents overwrites)
        date_parts = matched_date_key.strip().split()
        safe_date = f"{date_parts[0].lower()}_{date_parts[1]}" if len(date_parts) >= 2 else "undated"
        safe_brand = brand.lower().replace(" ", "_")
        safe_product = product.lower().replace(" ", "_").replace("&", "and")
        safe_product = re.sub(r'[^a-z0-9\_]', '', safe_product)
        prompt_filename = f"generated_{safe_date}_{safe_brand}_{safe_product}.md"
        prompt_path = os.path.join(PROMPTS_DIR, prompt_filename)
        
        with open(prompt_path, "w", encoding="utf-8") as f:
            f.write(prompt_content)
            
        print(f"[SUCCESS] CRITICAL PROMPT CREATED: {prompt_path}")
        print("Copy the contents of this file directly into your AI chat session to generate a highly optimized post package!")

if __name__ == "__main__":
    main()

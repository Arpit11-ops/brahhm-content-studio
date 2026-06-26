from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

OUTPUT = r"C:\NITRO 4 BACKUP\IMPORTANT WORK\brahhm-content-studio\Brahhm_Content_Studio_Explainer.pdf"

# ── Palette ─────────────────────────────────────────────────────────────────
DARK       = colors.HexColor("#1A1A1A")
TEAL       = colors.HexColor("#007878")
TEAL_LIGHT = colors.HexColor("#E6F4F4")
GOLD       = colors.HexColor("#B49664")
CREAM      = colors.HexColor("#F5F2E8")
WHITE      = colors.white
GREY       = colors.HexColor("#666666")
RULE       = colors.HexColor("#DDDDDD")

# ── Styles ───────────────────────────────────────────────────────────────────
base = getSampleStyleSheet()

def style(name, parent="Normal", **kw):
    s = ParagraphStyle(name, parent=base[parent], **kw)
    return s

H1 = style("H1", "Heading1",
    fontSize=22, leading=28, textColor=DARK,
    fontName="Helvetica-Bold", spaceAfter=4)

H2 = style("H2", "Heading2",
    fontSize=13, leading=17, textColor=TEAL,
    fontName="Helvetica-Bold", spaceBefore=14, spaceAfter=4)

H3 = style("H3", "Heading3",
    fontSize=10, leading=14, textColor=DARK,
    fontName="Helvetica-Bold", spaceBefore=8, spaceAfter=2)

BODY = style("BODY",
    fontSize=9.5, leading=14.5, textColor=DARK,
    fontName="Helvetica", spaceAfter=6)

SMALL = style("SMALL",
    fontSize=8.5, leading=12, textColor=GREY,
    fontName="Helvetica", spaceAfter=4)

SUBTITLE = style("SUBTITLE",
    fontSize=11, leading=16, textColor=TEAL,
    fontName="Helvetica-Oblique", spaceAfter=16)

LABEL = style("LABEL",
    fontSize=8, leading=11, textColor=WHITE,
    fontName="Helvetica-Bold")

CODE = style("CODE",
    fontSize=8.5, leading=13, textColor=DARK,
    fontName="Courier", backColor=colors.HexColor("#F0F0F0"),
    leftIndent=8, rightIndent=8, spaceBefore=4, spaceAfter=6,
    borderPad=4)

def hr():
    return HRFlowable(width="100%", thickness=0.5, color=RULE, spaceAfter=6, spaceBefore=6)

def section(title):
    return [Spacer(1, 6), Paragraph(title, H2), hr()]

def body(text):
    return Paragraph(text, BODY)

def small(text):
    return Paragraph(text, SMALL)

def tbl(data, col_widths, header=True):
    """Generic table builder."""
    t = Table(data, colWidths=col_widths, repeatRows=1 if header else 0)
    ts = [
        ("BACKGROUND",   (0, 0), (-1,  0), TEAL),
        ("TEXTCOLOR",    (0, 0), (-1,  0), WHITE),
        ("FONTNAME",     (0, 0), (-1,  0), "Helvetica-Bold"),
        ("FONTSIZE",     (0, 0), (-1, -1), 8.5),
        ("LEADING",      (0, 0), (-1, -1), 12),
        ("ROWBACKGROUNDS",(0,1),(-1,-1), [WHITE, TEAL_LIGHT]),
        ("GRID",         (0, 0), (-1, -1), 0.4, RULE),
        ("TOPPADDING",   (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 5),
        ("LEFTPADDING",  (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
    ]
    if not header:
        ts.pop(0); ts.pop(0); ts.pop(0)  # remove header styles
    t.setStyle(TableStyle(ts))
    return t

# ── Document ─────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    leftMargin=20*mm, rightMargin=20*mm,
    topMargin=18*mm, bottomMargin=18*mm,
)

W = A4[0] - 40*mm   # usable width

story = []

# ── Cover Block ──────────────────────────────────────────────────────────────
cover_data = [[
    Paragraph("BRAHHM CONTENT STUDIO 3.2", style("CT", fontSize=20, leading=24,
        textColor=WHITE, fontName="Helvetica-Bold", alignment=TA_CENTER)),
    ],[
    Paragraph("System Overview — Brahhm Arpan Organic Pvt. Ltd.", style("CS", fontSize=10,
        leading=14, textColor=colors.HexColor("#CCE8E8"), fontName="Helvetica-Oblique",
        alignment=TA_CENTER)),
    ],[
    Paragraph("Version 3.2 &nbsp;|&nbsp; June 2026 &nbsp;|&nbsp; Confidential",
        style("CL", fontSize=8, leading=12, textColor=colors.HexColor("#99CCCC"),
        fontName="Helvetica", alignment=TA_CENTER)),
]]
cover_tbl = Table(cover_data, colWidths=[W])
cover_tbl.setStyle(TableStyle([
    ("BACKGROUND",   (0,0), (-1,-1), TEAL),
    ("TOPPADDING",   (0,0), (-1,-1), 10),
    ("BOTTOMPADDING",(0,0), (-1,-1), 10),
    ("LEFTPADDING",  (0,0), (-1,-1), 12),
    ("RIGHTPADDING", (0,0), (-1,-1), 12),
    ("LINEBELOW",    (0,-1),(-1,-1), 3, GOLD),
]))
story.append(cover_tbl)
story.append(Spacer(1, 10))

# ── What Is It ───────────────────────────────────────────────────────────────
story += section("What Is It?")
story.append(body(
    "A fully automated content production system built inside Claude Code for Brahhm Arpan "
    "Organic Pvt. Ltd. — a D2C organic food company running <b>5 brands simultaneously</b>. "
    "Instead of briefing a social media agency or a freelancer each time, the founder (Puran) "
    "types a single command and the system generates a complete, execution-ready post package "
    "— captions, image prompts, reel scripts, ManyChat flows — in minutes."
))

# ── The 5 Brands ─────────────────────────────────────────────────────────────
story += section("The 5 Brands")

brands = [
    ["Brand", "Aesthetic / Vibe", "Website"],
    ["Caveman Organic",  "Bold, Gen Z, millet-forward — Cave Red world",            "caveman.co.in"],
    ["Health Fields",    "Luxury wellness, clinical, Aesop-level premium",          "health-fields.com"],
    ["Pusht Organic",    "Farm-honest, golden hour, soil and seed",                 "pusht.in"],
    ["greendipz",        "Flavour-first, cuisine-led, street food bold",            "biomart.in"],
    ["Biomart",          "Organic megastore, clean abundant, Whole Foods feel",     "biomart.in"],
]
story.append(tbl(
    [[Paragraph(c, style("TH", fontSize=8.5, fontName="Helvetica-Bold" if r==0 else "Helvetica",
                         leading=12, textColor=WHITE if r==0 else DARK)) for c in row]
     for r, row in enumerate(brands)],
    [W*0.22, W*0.55, W*0.23]
))
story.append(Spacer(1, 6))
story.append(small(
    "Each brand has its own Brand Bible — tone rules, banned styles, visual language, and hero angles. "
    "The system never mixes them up."
))

# ── 13-Point Post Package ────────────────────────────────────────────────────
story += section("What Gets Generated Per Post — The 13-Point Package")

points = [
    ("1",  "Content Angle",       "ATTACK / EDUCATE / RELATE / CONVERT"),
    ("2",  "Idea Title",          "Descriptive title for the post concept"),
    ("3",  "Hook",                "Under 8 words — forces the 'Read More' click"),
    ("4",  "Execution Concept",   "Step-by-step breakdown of the post idea"),
    ("5",  "Visual Direction",    "Template number, composition, styling notes"),
    ("6",  "In-Image Text",       "Review table — confirmed by Puran before prompt is written"),
    ("7",  "GPT Image 2.0 Prompt","Full structured prompt in code block, paste-ready"),
    ("8",  "Caption",             "Plain text, humanized, brand-correct, with hashtags"),
    ("10", "ManyChat Flow",       "3-step DM automation tied to keyword trigger"),
    ("11", "Caption Variation",   "Alternative caption with a meaningfully different angle"),
    ("12", "Why It Will Perform", "Psychology and algorithm justification"),
    ("13", "Bundling Suggestion", "One complementary product for AOV cross-sell"),
]

pt_data = [["#", "Deliverable", "Notes"]] + points
story.append(tbl(
    [[Paragraph(c, style(f"PT{i}{j}", fontSize=8.5,
                         fontName="Helvetica-Bold" if i==0 else "Helvetica",
                         leading=12, textColor=WHITE if i==0 else DARK))
      for j, c in enumerate(row)]
     for i, row in enumerate(pt_data)],
    [W*0.06, W*0.28, W*0.66]
))

# ── Pipeline ─────────────────────────────────────────────────────────────────
story += section("The Production Pipeline")

story.append(Paragraph("Static Posts", H3))
flow_static = [
    ["Command", "→", "Claims Audit", "→", "Skills Read", "→", "Caption + GPT Prompt + ManyChat"]
]
t = Table(flow_static, colWidths=[W*0.14, W*0.04, W*0.14, W*0.04, W*0.14, W*0.04, W*0.46])
t.setStyle(TableStyle([
    ("BACKGROUND",   (0,0),(0,0), TEAL), ("BACKGROUND",(2,0),(2,0), GOLD),
    ("BACKGROUND",   (4,0),(4,0), colors.HexColor("#143C28")),
    ("BACKGROUND",   (6,0),(6,0), DARK),
    ("TEXTCOLOR",    (0,0),(-1,-1), WHITE),
    ("FONTNAME",     (0,0),(-1,-1), "Helvetica-Bold"),
    ("FONTSIZE",     (0,0),(-1,-1), 8), ("LEADING",(0,0),(-1,-1),11),
    ("ALIGN",        (0,0),(-1,-1), "CENTER"),
    ("TOPPADDING",   (0,0),(-1,-1), 6), ("BOTTOMPADDING",(0,0),(-1,-1),6),
    ("TEXTCOLOR",    (1,0),(1,0), DARK), ("TEXTCOLOR",(3,0),(3,0),DARK),
    ("TEXTCOLOR",    (5,0),(5,0), DARK),
    ("FONTNAME",     (1,0),(1,0),"Helvetica"), ("FONTNAME",(3,0),(3,0),"Helvetica"),
    ("FONTNAME",     (5,0),(5,0),"Helvetica"),
    ("BACKGROUND",   (1,0),(1,0), WHITE), ("BACKGROUND",(3,0),(3,0),WHITE),
    ("BACKGROUND",   (5,0),(5,0), WHITE),
]))
story.append(t)
story.append(Spacer(1, 10))

story.append(Paragraph("Reel Production — 3-Stage Workflow", H3))

stages = [
    ["Stage", "Action", "Tool"],
    ["Stage 1", "Build GPT Image 2.0 still frames", "GPT Image 2.0"],
    ["↓",       "Puran generates stills and uploads them", "—"],
    ["Stage 2", "Analyse stills — composition check, approve frames", "Claude Code"],
    ["↓",       "Only proceed after stills confirmed", "—"],
    ["Stage 3", "Build animation prompts from approved stills", "Kling 3.0"],
    ["Post",    "Assemble clips, voiceover, SFX, captions", "CapCut"],
    ["Final",   "Logo overlay, price callouts (Puran manually)", "Canva"],
]
story.append(tbl(
    [[Paragraph(c, style(f"S{i}{j}", fontSize=8.5,
                         fontName="Helvetica-Bold" if i==0 else "Helvetica",
                         leading=12, textColor=WHITE if i==0 else DARK))
      for j, c in enumerate(row)]
     for i, row in enumerate(stages)],
    [W*0.12, W*0.62, W*0.26]
))

# ── Safety Protocols ──────────────────────────────────────────────────────────
story += section("The Safety Protocols")

protocols = [
    ["Protocol", "Rule"],
    ["2 — Description Gate",    "No product description = no content. The system stops and asks. Never invents claims."],
    ["3 — Claims Audit",        "Every claim extracted and checked. Health claims, therapeutic claims, vague language — only verified facts proceed."],
    ["3A — Dynamic Bundling",   "Silently scans for one complementary product. Weaves into ManyChat Step 3 cross-sell only."],
    ["4 — Brand DNA Lock",      "Reads Brand Architecture Master + active Brand Bible before any copy. Brand voices never bleed into each other."],
    ["5 — Offers & Pricing",    "Never includes codes, prices, or offers unless Puran explicitly instructs in that session."],
    ["6 — Visual Execution",    "20-line GPT prompt structure. In-image text confirmed before prompt is written. No dots on headlines."],
    ["7 — Reverse Engineer",    "7-layer analysis of reference images → STEP 0 compositing detection → new template in creative brief language."],
    ["8 — Reel Production",     "3 hard stages. GPT stills first → Puran uploads → Kling prompts. Never animate baked text. Never skip stages."],
    ["9 — Caption 3.0",         "Hook under 8 words. 3-pass sweep: Humanizer → Copy-edit → Brand DNA check."],
    ["10 — ManyChat Engine",    "Every caption ends with keyword trigger. 3-step DM flow (public reply → immediate DM → 24hr cross-sell)."],
    ["11 — Hashtag Strategy",   "Max 3 hashtags. 1 branded + 1 category + 1 discovery. Test 0 hashtags on reels."],
]
story.append(tbl(
    [[Paragraph(c, style(f"P{i}{j}", fontSize=8.5,
                         fontName="Helvetica-Bold" if i==0 else ("Helvetica-Bold" if j==0 else "Helvetica"),
                         leading=12, textColor=WHITE if i==0 else DARK))
      for j, c in enumerate(row)]
     for i, row in enumerate(protocols)],
    [W*0.28, W*0.72]
))

# ── Skill System ──────────────────────────────────────────────────────────────
story += section("The Skill System — Mandatory Blocking Gates")

story.append(body(
    "Before writing any caption or image prompt, the system reads specialized skill files. "
    "These are <b>hard blocking gates</b> — no output is produced until the relevant skills are read. "
    "Every post triggers the core 4 reads, plus additional skills by post type."
))

skills = [
    ["Skill", "Fires When", "Purpose"],
    ["Humanizer",            "Every caption",                "Strips 29 AI-writing patterns so copy sounds human-written"],
    ["Social",               "Every caption + every hook",   "Instagram-native tone, hook formula, engagement logic"],
    ["Copywriting",          "All caption body copy",        "Conversion copy principles, CTA framing"],
    ["Copy-editing",         "Every caption (after humanizer)", "Banned words, emoji limit (max 3), voice check"],
    ["Video",                "Every reel brief",             "Short-form scripting, hook structure, 9:16 specs"],
    ["Marketing Psychology", "All ATTACK + CONVERT posts",   "Loss aversion, identity triggers, social proof, anchoring"],
    ["Ad Creative",          "All CONVERT + boost candidates","Min 2 variants with meaningfully different angles"],
    ["Emails / ManyChat",    "Every 3-step DM flow",         "Drip logic: trigger → value DM → 24hr cross-sell"],
    ["Launch",               "New SKUs + festival campaigns", "Teaser → reveal → proof → urgency → close arc"],
    ["CRO",                  "Any CTA landing on brand sites","Caption CTA matches landing page promise"],
]
story.append(tbl(
    [[Paragraph(c, style(f"SK{i}{j}", fontSize=8.5,
                         fontName="Helvetica-Bold" if i==0 else "Helvetica",
                         leading=12, textColor=WHITE if i==0 else DARK))
      for j, c in enumerate(row)]
     for i, row in enumerate(skills)],
    [W*0.22, W*0.30, W*0.48]
))

# ── ManyChat ──────────────────────────────────────────────────────────────────
story += section("The ManyChat Conversion Layer")

story.append(body(
    "Every caption ends with a keyword trigger in the format: "
    "<b>\"Comment KEYWORD for [benefit]\"</b>. "
    "The system generates the full 3-step DM automation alongside every caption."
))

mc_data = [
    ["Step", "Trigger", "Action"],
    ["Step 1 — Public Reply",   "User comments keyword",   "Account replies publicly: 'Comment received! Check your DMs ✓'"],
    ["Step 2 — Immediate DM",   "Immediately after Step 1","Value message with link or resource delivered to inbox"],
    ["Step 3 — Cross-sell DM",  "24 hours after Step 2",   "Pairing suggestion: complementary product recommendation"],
]
story.append(tbl(
    [[Paragraph(c, style(f"MC{i}{j}", fontSize=8.5,
                         fontName="Helvetica-Bold" if i==0 else "Helvetica",
                         leading=12, textColor=WHITE if i==0 else DARK))
      for j, c in enumerate(row)]
     for i, row in enumerate(mc_data)],
    [W*0.24, W*0.26, W*0.50]
))

# ── Command Reference ──────────────────────────────────────────────────────────
story += section("How Puran Uses It — Command Reference")

cmds = [
    ["Command", "Output"],
    ["Full post for Health Fields — Tulsi Green Tea",   "Complete 13-point post package"],
    ["Reel script for Caveman — Millet Cookies",        "3-stage reel production workflow"],
    ["This week's plan for all brands",                 "Full 7-day calendar across all 5 brands"],
    ["GPT prompt for greendipz — Kung Pao Sauce",       "Image prompt after in-image text confirmation"],
    ["Batch this week — Biomart",                       "All posts for the week in one output"],
    ["[Festival] campaign for [Brand]",                 "Campaign arc: teaser → reveal → proof → urgency → close"],
    ["[Brand] carousel — [Type] — [Product]",           "Slide-by-slide carousel + caption + CTA"],
]
story.append(tbl(
    [[Paragraph(c, style(f"CMD{i}{j}", fontSize=8.5,
                         fontName="Courier-Bold" if (i>0 and j==0) else ("Helvetica-Bold" if i==0 else "Helvetica"),
                         leading=12, textColor=WHITE if i==0 else (TEAL if j==0 and i>0 else DARK)))
      for j, c in enumerate(row)]
     for i, row in enumerate(cmds)],
    [W*0.52, W*0.48]
))

# ── Posting Times ──────────────────────────────────────────────────────────────
story += section("Optimal Posting Times (IST)")

times = [
    ["Slot",             "Time",           "Priority"],
    ["Morning",          "7:30 – 8:30 AM", "Standard"],
    ["Afternoon",        "12:00 – 1:00 PM","Standard"],
    ["Peak Evening",     "6:30 – 8:00 PM", "Priority — Reels"],
    ["Stories",          "8:00 AM + 8:00 PM daily", "Daily both slots"],
]
story.append(tbl(
    [[Paragraph(c, style(f"T{i}{j}", fontSize=8.5,
                         fontName="Helvetica-Bold" if i==0 else "Helvetica",
                         leading=12, textColor=WHITE if i==0 else DARK))
      for j, c in enumerate(row)]
     for i, row in enumerate(times)],
    [W*0.28, W*0.36, W*0.36]
))

# ── Footer ────────────────────────────────────────────────────────────────────
story.append(Spacer(1, 16))
story.append(hr())

footer_data = [[
    Paragraph("Brahhm Arpan Organic Pvt. Ltd.", style("FL", fontSize=8, fontName="Helvetica-Bold",
        textColor=TEAL, leading=11)),
    Paragraph("M-13, IIIrd Floor, South Ex. Part-II, New Delhi – 110049<br/>"
              "online@health-fields.com &nbsp;|&nbsp; +91 9599804397",
        style("FR", fontSize=7.5, fontName="Helvetica", textColor=GREY, leading=11, alignment=TA_CENTER)),
    Paragraph("FOODCERT (APEDA) · India Organic<br/>PGS-India · Jaivik Bharat",
        style("FC", fontSize=7.5, fontName="Helvetica", textColor=GREY, leading=11,
        alignment=TA_LEFT)),
]]
ft = Table(footer_data, colWidths=[W*0.33, W*0.40, W*0.27])
ft.setStyle(TableStyle([
    ("VALIGN", (0,0),(-1,-1), "TOP"),
    ("TOPPADDING",(0,0),(-1,-1),4),
]))
story.append(ft)

# ── Build ─────────────────────────────────────────────────────────────────────
doc.build(story)
print(f"PDF saved: {OUTPUT}")

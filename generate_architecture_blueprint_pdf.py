from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.lib.enums import TA_CENTER

OUTPUT = r"C:\NITRO 4 BACKUP\IMPORTANT WORK\brahhm-content-studio\Content_Studio_Generalized_Architecture_Blueprint.pdf"

# ── Palette (neutral — not brand-tied, since this doc is domain-agnostic) ───
DARK   = colors.HexColor("#1A1A1A")
INK    = colors.HexColor("#2B3A55")
ACCENT = colors.HexColor("#3D6E66")
GOLD   = colors.HexColor("#B49664")
LIGHT  = colors.HexColor("#EEF2F0")
WHITE  = colors.white
GREY   = colors.HexColor("#666666")
RULE   = colors.HexColor("#DDDDDD")

base = getSampleStyleSheet()

def style(name, parent="Normal", **kw):
    return ParagraphStyle(name, parent=base[parent], **kw)

H1 = style("H1", "Heading1", fontSize=21, leading=26, textColor=DARK,
           fontName="Helvetica-Bold", spaceAfter=4)
H2 = style("H2", "Heading2", fontSize=13, leading=17, textColor=ACCENT,
           fontName="Helvetica-Bold", spaceBefore=14, spaceAfter=4)
H3 = style("H3", "Heading3", fontSize=10, leading=14, textColor=DARK,
           fontName="Helvetica-Bold", spaceBefore=8, spaceAfter=2)
BODY = style("BODY", fontSize=9.5, leading=14.5, textColor=DARK,
             fontName="Helvetica", spaceAfter=6)
SMALL = style("SMALL", fontSize=8.5, leading=12, textColor=GREY,
              fontName="Helvetica", spaceAfter=4)
SUBTITLE = style("SUBTITLE", fontSize=11, leading=16, textColor=ACCENT,
                  fontName="Helvetica-Oblique", spaceAfter=16)

def hr():
    return HRFlowable(width="100%", thickness=0.5, color=RULE, spaceAfter=6, spaceBefore=6)

def section(title):
    return [Spacer(1, 6), Paragraph(title, H2), hr()]

def body(text):
    return Paragraph(text, BODY)

def small(text):
    return Paragraph(text, SMALL)

def tbl(data, col_widths, header=True):
    t = Table(data, colWidths=col_widths, repeatRows=1 if header else 0)
    ts = [
        ("BACKGROUND",   (0, 0), (-1,  0), ACCENT),
        ("TEXTCOLOR",    (0, 0), (-1,  0), WHITE),
        ("FONTNAME",     (0, 0), (-1,  0), "Helvetica-Bold"),
        ("FONTSIZE",     (0, 0), (-1, -1), 8.5),
        ("LEADING",      (0, 0), (-1, -1), 12),
        ("ROWBACKGROUNDS",(0,1),(-1,-1), [WHITE, LIGHT]),
        ("GRID",         (0, 0), (-1, -1), 0.4, RULE),
        ("TOPPADDING",   (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 5),
        ("LEFTPADDING",  (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
    ]
    if not header:
        ts.pop(0); ts.pop(0); ts.pop(0)
    t.setStyle(TableStyle(ts))
    return t

def cell_table(rows, col_widths, bold_first_col=False):
    out = []
    for i, row in enumerate(rows):
        out.append([
            Paragraph(c, style(f"C{i}{j}", fontSize=8.5,
                       fontName="Helvetica-Bold" if (i == 0 or (bold_first_col and j == 0)) else "Helvetica",
                       leading=12, textColor=WHITE if i == 0 else DARK))
            for j, c in enumerate(row)
        ])
    return tbl(out, col_widths)

doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=20*mm, rightMargin=20*mm, topMargin=18*mm, bottomMargin=18*mm,
)
W = A4[0] - 40*mm
story = []

# ── Cover ─────────────────────────────────────────────────────────────────
cover_data = [[
    Paragraph("CONTENT STUDIO — GENERALIZED ARCHITECTURE BLUEPRINT",
        style("CT", fontSize=18, leading=23, textColor=WHITE,
              fontName="Helvetica-Bold", alignment=TA_CENTER)),
], [
    Paragraph("Extracting the reusable system pattern behind Brahhm Content Studio 3.2 "
              "so it can be rebuilt for any domain",
        style("CS", fontSize=10, leading=14, textColor=colors.HexColor("#D8E8E4"),
              fontName="Helvetica-Oblique", alignment=TA_CENTER)),
], [
    Paragraph("Draft v1 &nbsp;|&nbsp; June 2026 &nbsp;|&nbsp; Internal Planning Document",
        style("CL", fontSize=8, leading=12, textColor=colors.HexColor("#B7CFC9"),
              fontName="Helvetica", alignment=TA_CENTER)),
]]
cover_tbl = Table(cover_data, colWidths=[W])
cover_tbl.setStyle(TableStyle([
    ("BACKGROUND",   (0,0), (-1,-1), ACCENT),
    ("TOPPADDING",   (0,0), (-1,-1), 12),
    ("BOTTOMPADDING",(0,0), (-1,-1), 12),
    ("LEFTPADDING",  (0,0), (-1,-1), 12),
    ("RIGHTPADDING", (0,0), (-1,-1), 12),
    ("LINEBELOW",    (0,-1),(-1,-1), 3, GOLD),
]))
story.append(cover_tbl)
story.append(Spacer(1, 10))

# ── Why this document exists ────────────────────────────────────────────
story += section("Why This Document Exists")
story.append(body(
    "Brahhm Content Studio 3.2 was built to solve one problem: produce on-brand, claims-safe, "
    "execution-ready marketing content for 5 organic food brands without a human re-explaining "
    "context every time. But the thing that actually makes it work has nothing to do with food, "
    "Instagram, or organic certification — it is a <b>general-purpose pattern for turning an LLM "
    "into a reliable, repeatable production system</b> for any output that has to be correct, "
    "on-voice, and non-repetitive at scale. This document strips the marketing specifics out and "
    "names the underlying architecture, so it can be re-skinned for a completely different domain "
    "&mdash; legal drafting, customer support, curriculum design, internal reporting, product "
    "documentation, anything with repeatable structure and real stakes for getting it wrong."
))

# ── The core insight ─────────────────────────────────────────────────────
story += section("The Core Insight")
story.append(body(
    "A generic LLM prompt drifts: tone slips between runs, facts get invented, the same idea "
    "repeats, and nothing is checked before it ships. Content Studio doesn't fix this by writing "
    "a better prompt &mdash; it fixes it by wrapping the model in a <b>system</b> made of five "
    "kinds of constraint, each addressing one specific failure mode. The system is the product, "
    "not the prompt."
))
story.append(cell_table([
    ["Failure Mode", "System Component That Fixes It"],
    ["Model invents facts / claims it can't verify",      "Source-of-Truth Gate (Protocol 2 + 3)"],
    ["Voice bleeds between contexts / brands / clients",  "Identity Lock (Protocol 4)"],
    ["Model skips steps or improvises structure",          "Capability Modules — mandatory blocking reads"],
    ["Output format is inconsistent run to run",            "Fixed Output Contract (the N-point package)"],
    ["Expensive or irreversible steps happen too early",    "Staged Pipeline with human checkpoints"],
    ["Same idea/asset/template repeats and gets stale",      "State Tracking Ledger"],
    ["User has to re-explain the task every session",        "Command Interface mapped to fixed outputs"],
], [W*0.46, W*0.54]))

# ── Layer 1 ──────────────────────────────────────────────────────────────
story += section("Layer 1 — Knowledge Base (read, never inferred)")
story.append(body(
    "A set of plain files the agent is instructed to <b>read directly</b> rather than rely on "
    "training-data guesses. In Content Studio this is the calendar JSON, product description "
    "JSON, brand bibles, and the visual template library. Generalized: any domain has an "
    "equivalent &mdash; a knowledge base, a style guide, a policy document, a price list, a case "
    "history. The rule that matters is not which files exist, but the standing instruction: "
    "<i>if the fact isn't in a file, it doesn't go in the output.</i>"
))

# ── Layer 2 ──────────────────────────────────────────────────────────────
story += section("Layer 2 — Capability Modules (mandatory blocking gates)")
story.append(body(
    "Content Studio calls these \"skills\" &mdash; small, single-purpose instruction files "
    "(humanizer, copywriting, video, psychology, etc.) that the agent is <b>required to read "
    "before producing output</b>, not just allowed to. The blocking part is what makes it work: "
    "the system never lets the model freelance a caption from general knowledge when a dedicated "
    "module exists. Generalized, a capability module is any narrow \"how we do X here\" file: how "
    "we write a contract clause, how we triage a support ticket, how we grade an essay. The "
    "trigger map (which module fires for which task type) is the routing logic of the whole system."
))

# ── Layer 3 ──────────────────────────────────────────────────────────────
story += section("Layer 3 — Safety & Quality Gates (hard stops, sequencing rules)")
story.append(body(
    "These are the numbered Protocols: description-gate, claims-audit, brand-DNA-lock, "
    "offer/pricing restriction, reel-stage sequencing. Each is a rule of the form "
    "<b>\"do not proceed past point X until condition Y is satisfied\"</b> &mdash; not a style "
    "preference, an actual stop condition the agent must obey even under pressure to just "
    "produce something. This is the part of the system that prevents confident-sounding garbage."
))
story.append(cell_table([
    ["Gate Type", "Example in Content Studio", "Generalized Form"],
    ["Source verification gate", "No product description → stop and ask",
     "No verified input → stop and ask, never assume"],
    ["Claims/fact audit",         "Extract every claim, flag against banned list, keep only verified",
     "Extract every assertion, check against source-of-truth, flag unverifiable"],
    ["Identity lock",             "Never write Brand A in Brand B's tone",
     "Never let voice/context/client bleed across boundaries"],
    ["Scope restriction",          "No pricing/offers unless explicitly instructed this session",
     "No high-stakes commitments unless explicitly authorized this session"],
    ["Sequencing lock",            "Never write Stage 3 prompts before Stage 1 stills are approved",
     "Never skip a human checkpoint to reach the next irreversible step"],
], [W*0.22, W*0.40, W*0.38]))

# ── Layer 4 ──────────────────────────────────────────────────────────────
story += section("Layer 4 — Fixed Output Contract")
story.append(body(
    "Every post produces the same numbered structure (the 13-point package) regardless of "
    "brand, product, or angle. This is what makes outputs comparable, reviewable at a glance, "
    "and pluggable into downstream tools (Canva, ManyChat, CapCut). The generalized rule: "
    "<b>decide the shape of the output once, as a numbered contract, and never let the model "
    "improvise the shape per-request.</b> The content changes; the schema doesn't."
))

# ── Layer 5 ──────────────────────────────────────────────────────────────
story += section("Layer 5 — Staged Pipeline With Human Checkpoints")
story.append(body(
    "Reel production is the clearest example: Stage 1 (stills) must be generated and "
    "<b>approved by a human</b> before Stage 2 (analysis) runs, and Stage 2 must complete before "
    "Stage 3 (animation prompts) is even attempted. The system refuses to imagine what an "
    "unapproved asset looks like. Generalized: any workflow with an expensive, hard-to-reverse, "
    "or reputationally risky step should have a forced pause for human sign-off immediately "
    "before that step &mdash; not after."
))

# ── Layer 6 ──────────────────────────────────────────────────────────────
story += section("Layer 6 — State Tracking Ledger (anti-repetition memory)")
story.append(body(
    "The \"Known Used Reel Products\" list and the VEE template counter exist purely so the "
    "system doesn't repeat itself across sessions where the model has no native memory of what "
    "it already produced. Generalized: any system generating recurring output (weekly reports, "
    "support replies, lesson plans) needs a small persisted ledger of what was already used, "
    "checked before each new generation."
))

# ── Layer 7 ──────────────────────────────────────────────────────────────
story += section("Layer 7 — Command Interface")
story.append(body(
    "A small fixed vocabulary of commands (\"Full post for X\", \"Reel script for Y\", "
    "\"Batch this week\") each map to one exact output contract. The user never has to "
    "re-explain the task structure &mdash; they just name the brand/product/type and the system "
    "knows the shape of what comes back. Generalized: define your domain's 5–10 recurring "
    "task types as named commands up front, each bound to a fixed output contract from Layer 4."
))

story.append(PageBreak())

# ── Adaptation template ─────────────────────────────────────────────────
story += section("Adaptation Template — Building a \"[Domain] Studio\"")
story.append(body(
    "To port this architecture to a new domain, fill in each layer before writing a single "
    "line of output-generating instructions. Skipping a layer is what causes drift later."
))
story.append(cell_table([
    ["Layer", "Questions to Answer For The New Domain"],
    ["1. Knowledge Base",      "What source-of-truth files must be read, never guessed from? Where do they live?"],
    ["2. Capability Modules",  "What are the 5–15 narrow \"how we do X\" skills? What task type triggers each?"],
    ["3. Safety/Quality Gates","What facts must be verified before output? What identity/voice boundaries must never cross? What must never be included without explicit one-time authorization?"],
    ["4. Output Contract",     "What is the fixed numbered structure every output must follow, regardless of input?"],
    ["5. Pipeline Stages",     "Which steps are expensive/irreversible enough to need a forced human checkpoint before proceeding?"],
    ["6. State Ledger",        "What needs to never repeat? Where is that list persisted across sessions?"],
    ["7. Command Interface",   "What are the recurring task types, and what short command names them?"],
], [W*0.26, W*0.74]))

story.append(Spacer(1, 6))
story.append(Paragraph("Illustrative — Not Prescriptive", H3))
story.append(small(
    "These are only examples of how the same seven layers re-skin onto non-marketing work. "
    "The point is the pattern, not these specific domains."
))
story.append(cell_table([
    ["Domain", "Knowledge Base", "Output Contract"],
    ["Client services / agency ops", "Client SOWs, past deliverables, brand/style guides per client",
     "Fixed deliverable package: scope recap, draft, QA checklist, sign-off request"],
    ["Internal reporting",  "Source dashboards, prior reports, terminology glossary",
     "Fixed report shape: headline, metrics table, callouts, risks, next actions"],
    ["Curriculum / training design", "Syllabus, learning objectives, prior lesson archive",
     "Fixed lesson package: objective, hook, content, exercise, assessment, next-lesson link"],
], [W*0.30, W*0.36, W*0.34]))

# ── What NOT to skip ─────────────────────────────────────────────────────
story += section("What Breaks If You Skip a Layer")
story.append(cell_table([
    ["Skip This Layer", "What Goes Wrong"],
    ["Knowledge Base",        "Model fills gaps with plausible-sounding invention"],
    ["Capability Modules",    "Quality reverts to generic LLM default voice, inconsistent across runs"],
    ["Safety/Quality Gates",  "Unverifiable claims or cross-context bleed ship to production"],
    ["Output Contract",       "Every output has a different shape; nothing is comparable or reviewable at a glance"],
    ["Pipeline Checkpoints",  "Expensive/irreversible work happens on unapproved assumptions"],
    ["State Ledger",          "Repetition becomes visible to the audience within weeks"],
    ["Command Interface",     "User re-explains task structure every single session"],
], [W*0.32, W*0.68]))

# ── Footer ───────────────────────────────────────────────────────────────
story.append(Spacer(1, 16))
story.append(hr())
story.append(small(
    "This blueprint is derived from the live Brahhm Content Studio 3.2 system "
    "(CLAUDE.md, June 2026 revision). It intentionally omits brand names, product lists, and "
    "marketing-specific rules so the pattern can be reused outside Brahhm Arpan Organic Pvt. Ltd."
))

doc.build(story)
print(f"PDF saved: {OUTPUT}")

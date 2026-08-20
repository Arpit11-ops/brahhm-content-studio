"""
Client-facing August 2026 content calendar PDF — month-grid view.
Shows date cells with brand + format only. No angles, hooks, KPIs, product slots, or names.
"""

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

OUTPUT = r"C:\NITRO 4 BACKUP\IMPORTANT WORK\brahhm-content-studio\generated\August_2026_Client_Content_Calendar.pdf"

# Palette
DARK      = colors.HexColor("#1A1A1A")
TEAL      = colors.HexColor("#007878")
TEAL_DEEP = colors.HexColor("#003C32")
CREAM     = colors.HexColor("#F5F2E8")
GOLD      = colors.HexColor("#B49664")
GREY      = colors.HexColor("#666666")
LIGHT     = colors.HexColor("#F7F5EF")
RULE      = colors.HexColor("#D8D2C2")
WHITE     = colors.white
MUTED     = colors.HexColor("#EFECE2")

BRAND_COLOR = {
    "BIOMART":       colors.HexColor("#00A050"),
    "HEALTH FIELDS": colors.HexColor("#007878"),
    "PUSHT":         colors.HexColor("#143C28"),
    "CAVEMAN":       colors.HexColor("#BE1A1A"),
    "GREENDIPZ":     colors.HexColor("#1FAD10"),
}
BRAND_SHORT = {
    "BIOMART":       "BM",
    "HEALTH FIELDS": "HF",
    "PUSHT":         "PS",
    "CAVEMAN":       "CM",
    "GREENDIPZ":     "GZ",
}
TYPE_COLOR = {
    "POST":     colors.HexColor("#1A1A1A"),
    "CAROUSEL": colors.HexColor("#B86A00"),
    "REEL":     colors.HexColor("#7B2D8B"),
}
BRAND_ORDER = ["BIOMART", "HEALTH FIELDS", "PUSHT", "CAVEMAN", "GREENDIPZ"]

# (date_num, weekday, holiday, [(brand, type), ...])
CALENDAR = [
    (1,  "Sat", "Friendship Day",
        [("GREENDIPZ","REEL"), ("BIOMART","CAROUSEL"), ("CAVEMAN","POST"), ("GREENDIPZ","STORY"),
         ("HEALTH FIELDS","STORY"), ("PUSHT","STORY"), ("CAVEMAN","STORY"), ("BIOMART","STORY")]),
    (2,  "Sun", "",
        [("PUSHT","REEL"), ("HEALTH FIELDS","POST"), ("BIOMART","STORY"), ("GREENDIPZ","STORY")]),
    (3,  "Mon", "",
        [("CAVEMAN","POST"), ("HEALTH FIELDS","CAROUSEL"), ("PUSHT","STORY")]),
    (4,  "Tue", "",
        [("HEALTH FIELDS","REEL"), ("BIOMART","POST"), ("CAVEMAN","STORY")]),
    (5,  "Wed", "",
        [("GREENDIPZ","CAROUSEL"), ("PUSHT","POST"), ("BIOMART","STORY"), ("HEALTH FIELDS","STORY")]),
    (6,  "Thu", "",
        [("CAVEMAN","REEL"), ("BIOMART","POST"), ("PUSHT","STORY")]),
    (7,  "Fri", "",
        [("GREENDIPZ","POST"), ("HEALTH FIELDS","POST"), ("CAVEMAN","STORY"), ("BIOMART","STORY")]),
    (8,  "Sat", "Rakhi Eve",
        [("BIOMART","REEL"), ("HEALTH FIELDS","CAROUSEL"), ("CAVEMAN","POST"), ("PUSHT","STORY")]),
    (9,  "Sun", "Raksha Bandhan",
        [("PUSHT","REEL"), ("BIOMART","POST"), ("HEALTH FIELDS","POST"),
         ("GREENDIPZ","STORY"), ("CAVEMAN","STORY")]),
    (10, "Mon", "",
        [("HEALTH FIELDS","POST"), ("GREENDIPZ","CAROUSEL"), ("CAVEMAN","STORY")]),
    (11, "Tue", "",
        [("GREENDIPZ","REEL"), ("BIOMART","POST"), ("PUSHT","STORY")]),
    (12, "Wed", "Youth Day",
        [("HEALTH FIELDS","REEL"), ("CAVEMAN","POST"), ("BIOMART","STORY")]),
    (13, "Thu", "",
        [("PUSHT","CAROUSEL"), ("CAVEMAN","POST"), ("HEALTH FIELDS","STORY")]),
    (14, "Fri", "I-Day Eve",
        [("BIOMART","POST"), ("GREENDIPZ","POST"), ("PUSHT","STORY"), ("HEALTH FIELDS","STORY")]),
    (15, "Sat", "Independence Day",
        [("PUSHT","REEL"), ("BIOMART","POST"), ("HEALTH FIELDS","POST"),
         ("PUSHT","POST"), ("CAVEMAN","POST"), ("GREENDIPZ","POST"), ("BIOMART","STORY")]),
    (16, "Sun", "Janmashtami",
        [("HEALTH FIELDS","REEL"), ("PUSHT","POST"), ("BIOMART","CAROUSEL"), ("CAVEMAN","STORY")]),
    (17, "Mon", "",
        [("CAVEMAN","POST"), ("GREENDIPZ","CAROUSEL"), ("HEALTH FIELDS","STORY")]),
    (18, "Tue", "",
        [("BIOMART","REEL"), ("PUSHT","POST"), ("HEALTH FIELDS","STORY")]),
    (19, "Wed", "Photography Day",
        [("BIOMART","POST"), ("PUSHT","POST"), ("CAVEMAN","STORY"), ("GREENDIPZ","STORY")]),
    (20, "Thu", "",
        [("CAVEMAN","REEL"), ("HEALTH FIELDS","CAROUSEL"), ("BIOMART","STORY")]),
    (21, "Fri", "",
        [("GREENDIPZ","POST"), ("PUSHT","POST"), ("CAVEMAN","STORY")]),
    (22, "Sat", "",
        [("GREENDIPZ","REEL"), ("BIOMART","POST"), ("HEALTH FIELDS","STORY"), ("CAVEMAN","STORY")]),
    (23, "Sun", "",
        [("HEALTH FIELDS","REEL"), ("PUSHT","POST"), ("BIOMART","STORY"), ("GREENDIPZ","STORY")]),
    (24, "Mon", "",
        [("CAVEMAN","CAROUSEL"), ("BIOMART","POST"), ("HEALTH FIELDS","STORY")]),
    (25, "Tue", "Ganesh Chaturthi Eve",
        [("BIOMART","REEL"), ("PUSHT","POST"), ("HEALTH FIELDS","STORY")]),
    (26, "Wed", "Ganesh Chaturthi",
        [("BIOMART","POST"), ("PUSHT","POST"), ("HEALTH FIELDS","POST"),
         ("CAVEMAN","STORY"), ("GREENDIPZ","STORY")]),
    (27, "Thu", "Onam",
        [("PUSHT","REEL"), ("BIOMART","POST"), ("HEALTH FIELDS","STORY"), ("CAVEMAN","STORY")]),
    (28, "Fri", "",
        [("GREENDIPZ","POST"), ("CAVEMAN","POST"), ("BIOMART","STORY"), ("PUSHT","STORY")]),
    (29, "Sat", "Sports Day",
        [("CAVEMAN","REEL"), ("HEALTH FIELDS","POST"), ("BIOMART","POST"), ("GREENDIPZ","STORY")]),
    (30, "Sun", "",
        [("HEALTH FIELDS","REEL"), ("BIOMART","CAROUSEL"), ("PUSHT","STORY"), ("GREENDIPZ","STORY")]),
    (31, "Mon", "",
        [("PUSHT","REEL"), ("GREENDIPZ","REEL"), ("BIOMART","POST"),
         ("CAVEMAN","STORY"), ("HEALTH FIELDS","STORY")]),
]
DAY_INDEX = {d[0]: d for d in CALENDAR}

# ── Styles ─────────────────────────────────────────────────────────────
base = getSampleStyleSheet()
def style(name, parent="Normal", **kw):
    return ParagraphStyle(name, parent=base[parent], **kw)

TITLE   = style("TITLE",   "Title",  fontName="Helvetica-Bold", fontSize=24, textColor=TEAL_DEEP, alignment=TA_CENTER, leading=28, spaceAfter=2)
SUB     = style("SUB",     "Normal", fontName="Helvetica",      fontSize=10, textColor=GREY, alignment=TA_CENTER, leading=13, spaceAfter=1)
TAG     = style("TAG",     "Normal", fontName="Helvetica-Bold", fontSize=8,  textColor=GOLD, alignment=TA_CENTER, leading=10, spaceAfter=10)
DOWHEAD = style("DOWHEAD", "Normal", fontName="Helvetica-Bold", fontSize=9,  textColor=WHITE, alignment=TA_CENTER, leading=11)
CELLDATE= style("CELLDATE","Normal", fontName="Helvetica-Bold", fontSize=11, textColor=TEAL_DEEP, leading=13, spaceAfter=0)
HOLIDAY = style("HOLIDAY", "Normal", fontName="Helvetica-Oblique", fontSize=6.5, textColor=GOLD, leading=8, spaceAfter=2)
CELLLINE= style("CELLLINE","Normal", fontName="Helvetica",      fontSize=6.0,textColor=DARK, leading=6.6)
LEGEND  = style("LEGEND",  "Normal", fontName="Helvetica",      fontSize=7.2,textColor=GREY, alignment=TA_CENTER, leading=9)
SECT    = style("SECT",    "Normal", fontName="Helvetica-Bold", fontSize=13, textColor=TEAL_DEEP, leading=16, spaceBefore=10, spaceAfter=6)
BODY    = style("BODY",    "Normal", fontName="Helvetica",      fontSize=9,  textColor=DARK, leading=12)
FOOT    = style("FOOT",    "Normal", fontName="Helvetica",      fontSize=7.5,textColor=GREY, alignment=TA_CENTER, leading=9)

DOW = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
# Aug 1, 2026 = Saturday → offset 6 in Sun-start week
WEEKS = [
    [None]*6 + [1],
    list(range(2, 9)),
    list(range(9, 16)),
    list(range(16, 23)),
    list(range(23, 30)),
    [30, 31] + [None]*5,
]

def brand_label(brand):
    return "greendipz" if brand == "GREENDIPZ" else brand.title()

def cell_flowable(day_num):
    if day_num is None:
        return Paragraph("", CELLLINE)
    date, dow, holiday, items = DAY_INDEX[day_num]
    bits = [Paragraph(str(date), CELLDATE)]
    if holiday:
        bits.append(Paragraph(holiday, HOLIDAY))
    for b, t in items:
        if t == "STORY":
            continue
        color = BRAND_COLOR[b].hexval()
        tc = TYPE_COLOR[t].hexval()
        line = (
            f'<font color="{color}"><b>{BRAND_SHORT[b]}</b></font> '
            f'<font color="{tc}">{t.title()}</font>'
        )
        bits.append(Paragraph(line, CELLLINE))
    return bits

def build():
    doc = SimpleDocTemplate(
        OUTPUT, pagesize=landscape(A4),
        leftMargin=12*mm, rightMargin=12*mm,
        topMargin=12*mm, bottomMargin=10*mm,
        title="August 2026 Content Calendar", author="Brahhm Arpan Organic Pvt. Ltd."
    )
    story = []

    story.append(Paragraph("August 2026 · Content Calendar", TITLE))
    story.append(Paragraph("BRAHHM ARPAN ORGANIC PVT. LTD.", TAG))

    # Grid
    header_row = [Paragraph(d, DOWHEAD) for d in DOW]
    data = [header_row]
    for week in WEEKS:
        row = [cell_flowable(d) for d in week]
        data.append(row)

    page_w = landscape(A4)[0] - 24*mm
    col_w = page_w / 7.0

    grid = Table(data, colWidths=[col_w]*7, rowHeights=[8*mm] + [22*mm]*6)
    style_cmds = [
        ("BACKGROUND", (0,0), (-1,0), TEAL_DEEP),
        ("VALIGN", (0,0), (-1,0), "MIDDLE"),
        ("VALIGN", (0,1), (-1,-1), "TOP"),
        ("BOX", (0,0), (-1,-1), 0.4, RULE),
        ("INNERGRID", (0,0), (-1,-1), 0.4, RULE),
        ("LEFTPADDING", (0,1), (-1,-1), 4),
        ("RIGHTPADDING", (0,1), (-1,-1), 4),
        ("TOPPADDING", (0,1), (-1,-1), 3),
        ("BOTTOMPADDING", (0,1), (-1,-1), 3),
    ]
    # Grey out empty cells
    for r, week in enumerate(WEEKS, start=1):
        for c, d in enumerate(week):
            if d is None:
                style_cmds.append(("BACKGROUND", (c, r), (c, r), MUTED))
            else:
                _, dow, holiday, _ = DAY_INDEX[d]
                if dow in ("Sat", "Sun"):
                    style_cmds.append(("BACKGROUND", (c, r), (c, r), LIGHT))
    grid.setStyle(TableStyle(style_cmds))
    story.append(grid)
    story.append(Spacer(1, 8))

    # Client-facing format and brand legend
    format_legend = " &nbsp; · &nbsp; ".join(
        f'<font color="{c.hexval()}"><b>{t.title()}</b></font>' for t, c in TYPE_COLOR.items()
    )
    brand_legend = " &nbsp; · &nbsp; ".join(
        f'<font color="{BRAND_COLOR[b].hexval()}"><b>{BRAND_SHORT[b]}</b></font> {brand_label(b)}'
        for b in BRAND_ORDER
    )
    story.append(Paragraph(format_legend, LEGEND))
    story.append(Paragraph(brand_legend, LEGEND))
    story.append(Spacer(1, 2))
    story.append(HRFlowable(width="100%", thickness=0.4, color=RULE, spaceBefore=2, spaceAfter=3))
    story.append(Paragraph(
        "Brahhm Arpan Organic Pvt. Ltd.  ·  Monthly publishing schedule",
        FOOT
    ))

    story.append(PageBreak())

    # Totals table
    story.append(Paragraph("August 2026 · Publishing Quantity", TITLE))
    story.append(Paragraph("Posts, carousels and reels scheduled from the dated calendar", SUB))
    story.append(Spacer(1, 8))
    story.append(Paragraph("Monthly Volume by Brand", SECT))
    totals_header = ["Brand", "Posts", "Carousels", "Reels", "Total"]
    totals_data = [totals_header]
    grand = [0,0,0,0]
    for brand in BRAND_ORDER:
        counts = {"POST":0, "CAROUSEL":0, "REEL":0}
        for _, _, _, items in CALENDAR:
            for b, t in items:
                if b == brand and t in counts:
                    counts[t] += 1
        total = sum(counts.values())
        totals_data.append([
            brand_label(brand),
            str(counts["POST"]), str(counts["CAROUSEL"]),
            str(counts["REEL"]), str(total)
        ])
        grand[0]+=counts["POST"]; grand[1]+=counts["CAROUSEL"]
        grand[2]+=counts["REEL"]; grand[3]+=total
    totals_data.append(["Total", str(grand[0]), str(grand[1]), str(grand[2]), str(grand[3])])

    tt = Table(totals_data, colWidths=[62*mm, 31*mm, 38*mm, 31*mm, 31*mm])
    tt.setStyle(TableStyle([
        ("FONT", (0,0), (-1,0), "Helvetica-Bold", 10),
        ("FONT", (0,1), (-1,-2), "Helvetica", 10),
        ("FONT", (0,-1), (-1,-1), "Helvetica-Bold", 10),
        ("TEXTCOLOR", (0,0), (-1,0), WHITE),
        ("BACKGROUND", (0,0), (-1,0), TEAL_DEEP),
        ("BACKGROUND", (0,-1), (-1,-1), LIGHT),
        ("ROWBACKGROUNDS", (0,1), (-1,-2), [WHITE, LIGHT]),
        ("ALIGN", (1,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("LINEABOVE", (0,-1), (-1,-1), 0.5, GOLD),
    ]))
    story.append(tt)

    story.append(Spacer(1, 14))
    format_data = [
        ["Format", "Scheduled Quantity"],
        ["Posts", str(grand[0])],
        ["Carousels", str(grand[1])],
        ["Reels", str(grand[2])],
        ["Total Deliverables", str(grand[3])],
    ]
    ft = Table(format_data, colWidths=[92*mm, 48*mm])
    ft.setStyle(TableStyle([
        ("FONT", (0,0), (-1,0), "Helvetica-Bold", 10),
        ("FONT", (0,1), (-1,-2), "Helvetica", 10),
        ("FONT", (0,-1), (-1,-1), "Helvetica-Bold", 10),
        ("TEXTCOLOR", (0,0), (-1,0), WHITE),
        ("BACKGROUND", (0,0), (-1,0), TEAL_DEEP),
        ("BACKGROUND", (0,-1), (-1,-1), LIGHT),
        ("ROWBACKGROUNDS", (0,1), (-1,-2), [WHITE, LIGHT]),
        ("ALIGN", (1,0), (-1,-1), "CENTER"),
        ("BOX", (0,0), (-1,-1), 0.4, RULE),
        ("INNERGRID", (0,0), (-1,-1), 0.25, RULE),
        ("TOPPADDING", (0,0), (-1,-1), 7),
        ("BOTTOMPADDING", (0,0), (-1,-1), 7),
    ]))
    story.append(Paragraph("Quantity by Format", SECT))
    story.append(ft)

    story.append(Spacer(1, 14))
    story.append(HRFlowable(width="100%", thickness=0.4, color=RULE, spaceBefore=4, spaceAfter=4))
    story.append(Paragraph(
        "Brahhm Arpan Organic Pvt. Ltd.  ·  M-13, IIIrd Floor, South Ex. Part-II, New Delhi 110049",
        FOOT
    ))

    doc.build(story)
    print(f"Wrote {OUTPUT}")

if __name__ == "__main__":
    build()

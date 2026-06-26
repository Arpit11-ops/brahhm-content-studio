from docx import Document
from docx.shared import Pt, RGBColor, Cm, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

# ── Brand colours ──────────────────────────────────────────────────────────────
BRAND_COLORS = {
    "Caveman Organic":  RGBColor(0xBE, 0x1A, 0x1A),
    "Health Fields":    RGBColor(0x00, 0x78, 0x78),
    "Pusht Organic":    RGBColor(0x14, 0x3C, 0x28),
    "greendipz":        RGBColor(0x1F, 0xAD, 0x10),
    "Biomart":          RGBColor(0x1B, 0x8A, 0x3E),
}

TYPE_COLORS = {
    "Post":    RGBColor(0x1A, 0x1A, 0x1A),
    "Reel":    RGBColor(0x7B, 0x2D, 0x8B),
    "Story":   RGBColor(0x1A, 0x5C, 0x9E),
    "Carousel":RGBColor(0xB8, 0x6A, 0x00),
}

# ── Full June 2026 Calendar Data ───────────────────────────────────────────────
# Fields: date, day, holiday, items[]
# Each item: brand, type (Post/Reel/Story), product, angle, hook
CALENDAR = [
    # ── WEEK 1: June 1–7 ──────────────────────────────────────────────────────
    {
        "date": "June 1", "day": "Monday", "holiday": "World Milk Day",
        "items": [
            {"brand": "Caveman Organic",  "type": "Post",  "product": "Bakkit Cashew & Pista Cookies",   "angle": "ATTACK",  "hook": "Your milk biscuit has 14 ingredients. Ours has 4."},
            {"brand": "Health Fields",    "type": "Post",  "product": "Forest Honey 500g",               "angle": "EDUCATE", "hook": "Raw honey vs pasteurised. Same jar, different product."},
            {"brand": "greendipz",        "type": "Story", "product": "Butter Chicken Gravy 370g",       "angle": "CONVERT", "hook": "World Milk Day weekend cooking prompt."},
        ]
    },
    {
        "date": "June 2", "day": "Tuesday", "holiday": "",
        "items": [
            {"brand": "Biomart",          "type": "Post",  "product": "Certified Pantry Essentials",     "angle": "EDUCATE", "hook": "194 certified products. Start with 5."},
            {"brand": "Caveman Organic",  "type": "Post",  "product": "Ragi Cookies",                    "angle": "CONVERT", "hook": "2.5 lakh families switched. Your biscuit tin hasn't."},
            {"brand": "Health Fields",    "type": "Story", "product": "Calming Chamomile Tea",           "angle": "RELATE",  "hook": "Morning ritual tip — the cup that does more."},
            {"brand": "Caveman Organic",  "type": "Reel",  "product": "Bakkit Cashew & Pista Cookies",   "angle": "ATTACK",  "hook": "Monsoon snack swap. Chips vs millet cookies."},
        ]
    },
    {
        "date": "June 3", "day": "Wednesday", "holiday": "",
        "items": [
            {"brand": "Health Fields",    "type": "Post",  "product": "Calming Chamomile Tea",           "angle": "EDUCATE", "hook": "Most tulsi teas have flavouring. Not the herb."},
            {"brand": "greendipz",        "type": "Post",  "product": "Schezwan Sauce 200g",             "angle": "RELATE",  "hook": "Weeknight. Tired. Want something bold."},
            {"brand": "Pusht Organic",    "type": "Story", "product": "Cold Pressed Sunflower Oil 910ml","angle": "CONVERT", "hook": "Midweek oil recipe tip — cold pressed difference."},
        ]
    },
    {
        "date": "June 4", "day": "Thursday", "holiday": "",
        "items": [
            {"brand": "Biomart",          "type": "Post",  "product": "Dal + Masala Bundle",             "angle": "RELATE",  "hook": "One cart. Five certified brands. One Sunday order."},
            {"brand": "Pusht Organic",    "type": "Post",  "product": "Organic Forest Honey 500g",       "angle": "CONVERT", "hook": "Comment OIL and we'll tell you which cold-pressed to try."},
            {"brand": "Health Fields",    "type": "Reel",  "product": "Her Health Herbal Tea",           "angle": "RELATE",  "hook": "Morning ritual: what changes when tea is real."},
        ]
    },
    {
        "date": "June 5", "day": "Friday", "holiday": "World Environment Day",
        "items": [
            {"brand": "Pusht Organic",    "type": "Post",  "product": "FOODCERT Certification Story",    "angle": "EDUCATE", "hook": "Chemical-free farming doesn't start in the factory."},
            {"brand": "Biomart",          "type": "Post",  "product": "Certified Pantry — Env Day",      "angle": "ATTACK",  "hook": "194 products. Every one certified. Read the label."},
            {"brand": "greendipz",        "type": "Story", "product": "Schezwan Sauce 200g",             "angle": "RELATE",  "hook": "Environment Day — real ingredients, honest label."},
            {"brand": "Pusht Organic",    "type": "Reel",  "product": "Cold Pressed Sunflower Oil 910ml","angle": "EDUCATE", "hook": "Farm to bottle. What cold pressed actually means."},
        ]
    },
    {
        "date": "June 6", "day": "Saturday", "holiday": "",
        "items": [
            {"brand": "Caveman Organic",  "type": "Post",  "product": "Flax Amaranth Connection Cookies","angle": "ATTACK",  "hook": "Flip your biscuit packet. Read every ingredient."},
            {"brand": "Health Fields",    "type": "Post",  "product": "Her Health Herbal Tea",           "angle": "RELATE",  "hook": "You upgraded your phone. Your morning tea is the same."},
            {"brand": "greendipz",        "type": "Reel",  "product": "Arrabbiata Sauce 250g",           "angle": "RELATE",  "hook": "Rainy night pasta. 12 minutes. Done right."},
        ]
    },
    {
        "date": "June 7", "day": "Sunday", "holiday": "",
        "items": [
            {"brand": "Pusht Organic",    "type": "Post",  "product": "Cold Pressed Mustard Oil 910ml",  "angle": "EDUCATE", "hook": "Aapka tel actually cold-pressed hai? Here's how to check."},
            {"brand": "Biomart",          "type": "Post",  "product": "Seeds Combo — Pumpkin + Sunflower","angle": "CONVERT","hook": "Comment HAUL and we'll send the starter kit list."},
            {"brand": "Health Fields",    "type": "Post",  "product": "Since 2003 — Heritage Story",     "angle": "ATTACK",  "hook": "Organic since 2003. Before it was a trend."},
            {"brand": "Caveman Organic",  "type": "Story", "product": "Ragi Choco Chip Cookies",         "angle": "RELATE",  "hook": "Sunday snack prompt — what's in your tin?"},
        ]
    },

    # ── WEEK 2: June 8–14 ──────────────────────────────────────────────────────
    {
        "date": "June 8", "day": "Monday", "holiday": "World Ocean Day",
        "items": [
            {"brand": "Pusht Organic",    "type": "Post",  "product": "Organic Kabuli Chana",            "angle": "EDUCATE", "hook": "Teri dal kahan se aayi? Hum bata sakte hain."},
            {"brand": "Health Fields",    "type": "Post",  "product": "Since 2003 — Label Padhega Tie-in","angle": "ATTACK", "hook": "20 years before Label Padhega India. We were ready."},
            {"brand": "Caveman Organic",  "type": "Post",  "product": "Ragi Choco Chip Cookies",         "angle": "RELATE",  "hook": "The 4pm hunger that ruins every diet plan."},
            {"brand": "greendipz",        "type": "Story", "product": "Manchurian Sauce 240g",           "angle": "CONVERT", "hook": "Sunday dinner gravy — comment MAKHANI for recipe."},
        ]
    },
    {
        "date": "June 9", "day": "Tuesday", "holiday": "",
        "items": [
            {"brand": "Caveman Organic",  "type": "Post",  "product": "Kodo Coco Fun Millet Cookies",    "angle": "EDUCATE", "hook": "You've never heard of kodo millet. You should."},
            {"brand": "Biomart",          "type": "Post",  "product": "Jaivik Bharat Certification Ed.", "angle": "EDUCATE", "hook": "Jaivik Bharat logo dekha? FSSAI ki guarantee hai woh."},
            {"brand": "Pusht Organic",    "type": "Reel",  "product": "Cold Pressed Mustard Oil 910ml",  "angle": "RELATE",  "hook": "Rainy day tadka. What changes when oil is cold pressed."},
        ]
    },
    {
        "date": "June 10", "day": "Wednesday", "holiday": "",
        "items": [
            {"brand": "Health Fields",    "type": "Post",  "product": "Organic Black Pepper Whole 100g", "angle": "ATTACK",  "hook": "Your spices passed 250+ tests. Did theirs?"},
            {"brand": "greendipz",        "type": "Post",  "product": "Kung Pao Sauce 240g",             "angle": "EDUCATE", "hook": "Manchurian toh sab jaante hain. Kung Pao wale alag hote hain."},
            {"brand": "Caveman Organic",  "type": "Post",  "product": "Flax Amaranth Connection Cookies","angle": "CONVERT", "hook": "Drop LABEL in comments. We'll show our full ingredient list."},
            {"brand": "Biomart",          "type": "Story", "product": "Weekly Haul Discovery",           "angle": "RELATE",  "hook": "Midweek certified grocery reminder."},
        ]
    },
    {
        "date": "June 11", "day": "Thursday", "holiday": "",
        "items": [
            {"brand": "Pusht Organic",    "type": "Post",  "product": "White Sesame Oil 910ml",          "angle": "RELATE",  "hook": "Switched to cold-pressed oil. Here's what changed."},
            {"brand": "Biomart",          "type": "Post",  "product": "FSSAI Front-of-Pack Education",   "angle": "EDUCATE", "hook": "Sugar. Salt. Fat. Soon mandatory on the front. We've shown ours since 2003."},
            {"brand": "greendipz",        "type": "Reel",  "product": "Salsa Mexicana 325g",             "angle": "ATTACK",  "hook": "Your store-bought sauce has E-numbers. Ours doesn't."},
        ]
    },
    {
        "date": "June 12", "day": "Friday", "holiday": "",
        "items": [
            {"brand": "Health Fields",    "type": "Post",  "product": "Forest Honey 500g",               "angle": "RELATE",  "hook": "Monsoon immunity in one spoon. Comment HONEY for the ritual."},
            {"brand": "greendipz",        "type": "Post",  "product": "Biryani Gravy 370g",              "angle": "RELATE",  "hook": "Friday raat, khana banana nahi hai. Yeh bachayega."},
            {"brand": "Pusht Organic",    "type": "Post",  "product": "Browntop Millet",                 "angle": "CONVERT", "hook": "Browntop Millet — rare grain, limited stock. Order now."},
            {"brand": "Caveman Organic",  "type": "Story", "product": "Flax Amaranth Connection Cookies","angle": "ATTACK",  "hook": "Label transparency Friday — flip the packet."},
        ]
    },
    {
        "date": "June 13", "day": "Saturday", "holiday": "",
        "items": [
            {"brand": "Caveman Organic",  "type": "Post",  "product": "Ragi Choco Chip Cookies",         "angle": "CONVERT", "hook": "2.5 lakh families switched. What are you waiting for?"},
            {"brand": "Biomart",          "type": "Post",  "product": "Family Pantry Restock",           "angle": "RELATE",  "hook": "Family ki grocery list jo actually certified ho."},
            {"brand": "Caveman Organic",  "type": "Reel",  "product": "Ragi Choco Chip Cookies",         "angle": "CONVERT", "hook": "Cookie crunch vs chips. Real ingredients vs a list you can't read."},
        ]
    },
    {
        "date": "June 14", "day": "Sunday", "holiday": "World Blood Donor Day",
        "items": [
            {"brand": "Health Fields",    "type": "Post",  "product": "Organic Ragi Atta 500g",          "angle": "EDUCATE", "hook": "Browntop millet: the rarest grain in your kitchen."},
            {"brand": "Pusht Organic",    "type": "Post",  "product": "Panchranga Dal",                  "angle": "RELATE",  "hook": "Sunday dal tadka — organic ingredients, same recipe."},
            {"brand": "greendipz",        "type": "Post",  "product": "Butter Chicken Gravy 370g",       "angle": "EDUCATE", "hook": "What makes restaurant Butter Chicken taste different?"},
            {"brand": "Biomart",          "type": "Story", "product": "Sunday Haul",                     "angle": "CONVERT", "hook": "Sunday order prompt — your deliberate weekly restock."},
        ]
    },

    # ── WEEK 3: June 15–21 ──────────────────────────────────────────────────────
    {
        "date": "June 15", "day": "Monday", "holiday": "",
        "items": [
            {"brand": "Caveman Organic",  "type": "Post",  "product": "Bakkit Cashew & Pista Cookies",   "angle": "RELATE",  "hook": "Monday hunger hits hard. Reach for 4 ingredients, not 14."},
            {"brand": "Biomart",          "type": "Post",  "product": "Monsoon Pantry Restock",          "angle": "RELATE",  "hook": "Monsoon week ahead. Your pantry — deliberate this time."},
            {"brand": "Health Fields",    "type": "Story", "product": "Forest Honey 500g",               "angle": "RELATE",  "hook": "Monsoon immunity ritual — one spoon a morning."},
        ]
    },
    {
        "date": "June 16", "day": "Tuesday", "holiday": "",
        "items": [
            {"brand": "greendipz",        "type": "Post",  "product": "Butter Chicken Gravy 370g",       "angle": "EDUCATE", "hook": "Restaurant Butter Chicken at home. Here's the difference."},
            {"brand": "Pusht Organic",    "type": "Post",  "product": "Panchranga Dal",                  "angle": "ATTACK",  "hook": "Aapka dal chemical-free hai? Label check karo."},
            {"brand": "Biomart",          "type": "Reel",  "product": "Monsoon Pantry Haul",             "angle": "RELATE",  "hook": "Monsoon week ahead. One cart. Five certified brands. Done."},
        ]
    },
    {
        "date": "June 17", "day": "Wednesday", "holiday": "",
        "items": [
            {"brand": "Caveman Organic",  "type": "Post",  "product": "Flax Amaranth Connection Cookies","angle": "ATTACK",  "hook": "Maida. Palm oil. Artificial flavour. Your snack."},
            {"brand": "Health Fields",    "type": "Post",  "product": "Calming Chamomile Tea",           "angle": "EDUCATE", "hook": "The tulsi in your tea — is it actually tulsi?"},
            {"brand": "Biomart",          "type": "Post",  "product": "PGS-India Certification Ed.",     "angle": "EDUCATE", "hook": "Three organic certifications. Only one verifies at the farm."},
            {"brand": "greendipz",        "type": "Story", "product": "Kung Pao Sauce 240g",             "angle": "RELATE",  "hook": "Midweek recipe inspo — bold flavour, 15 minutes."},
        ]
    },
    {
        "date": "June 18", "day": "Thursday", "holiday": "Father's Day Teaser",
        "items": [
            {"brand": "Pusht Organic",    "type": "Post",  "product": "Cold Pressed Sunflower Oil 910ml","angle": "EDUCATE", "hook": "Aapka tel actually cold-pressed hai?"},
            {"brand": "Health Fields",    "type": "Post",  "product": "Calming Chamomile Tea",           "angle": "ATTACK",  "hook": "FSSAI wants front-of-pack honesty. We've shown ours for 23 years."},
            {"brand": "Caveman Organic",  "type": "Reel",  "product": "Ragi Cookies",                    "angle": "EDUCATE", "hook": "Millets fed India 5,000 years. Then maida happened."},
        ]
    },
    {
        "date": "June 19", "day": "Friday", "holiday": "Father's Day Build-Up",
        "items": [
            {"brand": "Biomart",          "type": "Post",  "product": "Father's Day Gift Hamper",        "angle": "CONVERT", "hook": "Dad deserves a gift he'll actually finish. Two days left."},
            {"brand": "greendipz",        "type": "Post",  "product": "Manchurian Sauce 240g",           "angle": "CONVERT", "hook": "Comment SCHEZWAN and get the recipe."},
            {"brand": "Caveman Organic",  "type": "Post",  "product": "Ragi Cookies",                    "angle": "RELATE",  "hook": "Monsoon mein chips nahi. Yeh try karo."},
            {"brand": "Pusht Organic",    "type": "Story", "product": "Organic Forest Honey 500g",       "angle": "RELATE",  "hook": "Father's Day gift hint — the jar he'll keep."},
        ]
    },
    {
        "date": "June 20", "day": "Saturday", "holiday": "Monsoon Begins · Father's Day Eve",
        "items": [
            {"brand": "Biomart",          "type": "Post",  "product": "Father's Day Last-Minute Haul",   "angle": "CONVERT", "hook": "Order tonight. Dad opens it tomorrow. Five certified brands."},
            {"brand": "Caveman Organic",  "type": "Post",  "product": "Bakkit Cashew & Pista Cookies",   "angle": "RELATE",  "hook": "Monsoon snacking. Your couch deserves better than chips."},
            {"brand": "greendipz",        "type": "Reel",  "product": "Arrabbiata Sauce 250g",           "angle": "RELATE",  "hook": "Rainy Saturday. Pasta craving. 12 minutes."},
        ]
    },
    {
        "date": "June 21", "day": "Sunday", "holiday": "Father's Day · International Yoga Day",
        "items": [
            {"brand": "Health Fields",    "type": "Post",  "product": "Tulsi Green Tea Premium",         "angle": "RELATE",  "hook": "Yoga Day morning. The only ritual worth keeping."},
            {"brand": "Pusht Organic",    "type": "Post",  "product": "Organic Forest Honey 500g",       "angle": "RELATE",  "hook": "Dad's first organic upgrade. One spoon, every morning."},
            {"brand": "Caveman Organic",  "type": "Post",  "product": "Bakkit Cashew & Pista Cookies",   "angle": "RELATE",  "hook": "Your dad's tea deserves a snack with 4 ingredients."},
            {"brand": "Biomart",          "type": "Reel",  "product": "Father's Day Gift Haul",          "angle": "CONVERT", "hook": "Five brands. One cart. Father's Day, sorted in one tap."},
        ]
    },

    # ── WEEK 4: June 22–28 ──────────────────────────────────────────────────────
    {
        "date": "June 22", "day": "Monday", "holiday": "",
        "items": [
            {"brand": "Caveman Organic",  "type": "Post",  "product": "Ragi Choco Chip Cookies",         "angle": "EDUCATE", "hook": "Foxtail millet: India grew this 8,000 years before protein bars."},
            {"brand": "Health Fields",    "type": "Post",  "product": "Organic Black Pepper Whole 100g", "angle": "ATTACK",  "hook": "Certification isn't a trend for us. It's 20 years of habit."},
            {"brand": "greendipz",        "type": "Post",  "product": "Salsa Mexicana 325g",             "angle": "EDUCATE", "hook": "Arrabbiata vs Salsa — which one and when?"},
            {"brand": "Biomart",          "type": "Story", "product": "Weekly Haul Discovery",           "angle": "RELATE",  "hook": "Monday restock — your certified pantry check."},
        ]
    },
    {
        "date": "June 23", "day": "Tuesday", "holiday": "",
        "items": [
            {"brand": "Pusht Organic",    "type": "Post",  "product": "Cold Pressed Mustard Oil 910ml",  "angle": "RELATE",  "hook": "Ghar ka khana tab sahi hota hai. Ingredients mein fark tha."},
            {"brand": "Biomart",          "type": "Post",  "product": "Multi-Brand Showcase",            "angle": "CONVERT", "hook": "Caveman. Pusht. Health Fields. greendipz. One cart."},
            {"brand": "Pusht Organic",    "type": "Story", "product": "Browntop Millet",                 "angle": "CONVERT", "hook": "Rare grain alert — limited stock, order today."},
            {"brand": "Caveman Organic",  "type": "Reel",  "product": "Bakkit Cashew & Pista Cookies",   "angle": "RELATE",  "hook": "Monsoon snacking. Your couch deserves better than chips."},
        ]
    },
    {
        "date": "June 24", "day": "Wednesday", "holiday": "",
        "items": [
            {"brand": "Health Fields",    "type": "Post",  "product": "Forest Honey 500g",               "angle": "CONVERT", "hook": "Monsoon cough season. Raw forest honey, not heated syrup."},
            {"brand": "greendipz",        "type": "Post",  "product": "Biryani Gravy 370g",              "angle": "RELATE",  "hook": "Weeknight. Tired. Want biryani. 15 minutes."},
            {"brand": "Pusht Organic",    "type": "Post",  "product": "Organic Kabuli Chana",            "angle": "EDUCATE", "hook": "Kisan ki mehnat seedha aapki rasoi tak."},
            {"brand": "Biomart",          "type": "Story", "product": "Weeknight Cooking Prompt",        "angle": "CONVERT", "hook": "Dinner sorted — comment HAUL for this week's list."},
        ]
    },
    {
        "date": "June 25", "day": "Thursday", "holiday": "",
        "items": [
            {"brand": "Caveman Organic",  "type": "Post",  "product": "Flax Amaranth Connection Cookies","angle": "CONVERT", "hook": "Comment COOKIES and get the full range guide."},
            {"brand": "Biomart",          "type": "Post",  "product": "Certified Pantry Education",      "angle": "EDUCATE", "hook": "Organic filter on your grocery app — certified by whom?"},
            {"brand": "Health Fields",    "type": "Reel",  "product": "Calming Chamomile Tea",           "angle": "RELATE",  "hook": "Yoga Day to today. 4 days of this ritual."},
        ]
    },
    {
        "date": "June 26", "day": "Friday", "holiday": "",
        "items": [
            {"brand": "greendipz",        "type": "Post",  "product": "Butter Chicken Gravy 370g",       "angle": "ATTACK",  "hook": "Flip your current sauce jar. Count the E-numbers."},
            {"brand": "Pusht Organic",    "type": "Post",  "product": "White Sesame Oil 910ml",          "angle": "EDUCATE", "hook": "Cold-pressed oil: one switch, everything changes."},
            {"brand": "Caveman Organic",  "type": "Post",  "product": "Ragi Cookies",                    "angle": "ATTACK",  "hook": "Stop calling it a health snack if it has maida."},
            {"brand": "Biomart",          "type": "Story", "product": "Farm Story",                      "angle": "EDUCATE", "hook": "Friday farm story — your dal's journey from soil to shelf."},
        ]
    },
    {
        "date": "June 27", "day": "Saturday", "holiday": "",
        "items": [
            {"brand": "Caveman Organic",  "type": "Post",  "product": "Ragi Choco Chip Cookies",         "angle": "RELATE",  "hook": "Tea time, but make it guilt-free."},
            {"brand": "Health Fields",    "type": "Post",  "product": "Organic Ragi Atta 500g",          "angle": "EDUCATE", "hook": "250 quality tests. Per batch. Every time."},
            {"brand": "greendipz",        "type": "Reel",  "product": "Salsa Mexicana 325g",             "angle": "EDUCATE", "hook": "Salsa Mexicana 5 ways you haven't tried yet."},
        ]
    },
    {
        "date": "June 28", "day": "Sunday", "holiday": "",
        "items": [
            {"brand": "Pusht Organic",    "type": "Post",  "product": "Panchranga Dal",                  "angle": "EDUCATE", "hook": "12 varieties of millets. You probably know 3."},
            {"brand": "Biomart",          "type": "Post",  "product": "Sunday Haul Showcase",            "angle": "RELATE",  "hook": "One deliberate order replaces five last-minute ones."},
            {"brand": "Health Fields",    "type": "Post",  "product": "Her Health Herbal Tea",           "angle": "CONVERT", "hook": "Everything in your kitchen — one certified brand."},
            {"brand": "Caveman Organic",  "type": "Story", "product": "Bakkit Cashew & Pista Cookies",   "angle": "CONVERT", "hook": "Sunday DM trigger — comment COOKIES for range guide."},
        ]
    },

    # ── WEEK 5: June 29–30 ──────────────────────────────────────────────────────
    {
        "date": "June 29", "day": "Monday", "holiday": "Kabirdas Jayanti",
        "items": [
            {"brand": "Pusht Organic",    "type": "Post",  "product": "Organic Kabuli Chana",            "angle": "RELATE",  "hook": "Simplicity is the highest wisdom. One ingredient. Your dal."},
            {"brand": "greendipz",        "type": "Post",  "product": "Biryani Gravy 370g",              "angle": "EDUCATE", "hook": "Our sauce label has 6 words. Most have 22."},
            {"brand": "Health Fields",    "type": "Reel",  "product": "Since 2003 — Heritage Brand Story","angle": "ATTACK", "hook": "23 years of the same standard. No shortcuts. Ever."},
        ]
    },
    {
        "date": "June 30", "day": "Tuesday", "holiday": "",
        "items": [
            {"brand": "Caveman Organic",  "type": "Post",  "product": "Flax Amaranth Connection Cookies","angle": "CONVERT", "hook": "The cookie that doesn't need Google to read the label."},
            {"brand": "Biomart",          "type": "Post",  "product": "Month-End Pantry Restock",        "angle": "CONVERT", "hook": "194 certifications checked so you don't have to."},
            {"brand": "greendipz",        "type": "Story", "product": "Schezwan Sauce 200g",             "angle": "CONVERT", "hook": "July is coming. Stock up on sauces tonight."},
        ]
    },
]


def set_cell_bg(cell, hex_color):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)


def set_cell_borders(cell, color="CCCCCC"):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for side in ['top', 'left', 'bottom', 'right']:
        border = OxmlElement(f'w:{side}')
        border.set(qn('w:val'), 'single')
        border.set(qn('w:sz'), '4')
        border.set(qn('w:space'), '0')
        border.set(qn('w:color'), color)
        tcBorders.append(border)
    tcPr.append(tcBorders)


def rgb_to_hex(rgb):
    return f"{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"


BRAND_HEX = {
    "Caveman Organic": "BE1A1A",
    "Health Fields":   "007878",
    "Pusht Organic":   "143C28",
    "greendipz":       "1FAD10",
    "Biomart":         "1B8A3E",
}

TYPE_LABEL_HEX = {
    "Post":    "1A1A1A",
    "Reel":    "7B2D8B",
    "Story":   "1A5C9E",
    "Carousel":"B86A00",
}

TYPE_BG_HEX = {
    "Post":    "F5F5F5",
    "Reel":    "F3E8F8",
    "Story":   "E8F0FA",
    "Carousel":"FDF3E3",
}

ANGLE_HEX = {
    "ATTACK":  "D32F2F",
    "EDUCATE": "1565C0",
    "RELATE":  "2E7D32",
    "CONVERT": "E65100",
}


def add_colored_run(para, text, bold=False, color_hex=None, size_pt=9, italic=False):
    run = para.add_run(text)
    run.bold = bold
    run.italic = italic
    run.font.size = Pt(size_pt)
    if color_hex:
        run.font.color.rgb = RGBColor(
            int(color_hex[0:2], 16),
            int(color_hex[2:4], 16),
            int(color_hex[4:6], 16)
        )
    return run


def build_document():
    doc = Document()

    # ── Page setup ─────────────────────────────────────────────────────────────
    section = doc.sections[0]
    section.page_width  = Cm(29.7)
    section.page_height = Cm(21.0)
    section.orientation = 1  # landscape
    section.left_margin   = Cm(1.5)
    section.right_margin  = Cm(1.5)
    section.top_margin    = Cm(1.5)
    section.bottom_margin = Cm(1.5)

    # ── Document styles ────────────────────────────────────────────────────────
    styles = doc.styles
    normal = styles['Normal']
    normal.font.name = 'Calibri'
    normal.font.size = Pt(9)

    # ── Cover / Title block ────────────────────────────────────────────────────
    title_para = doc.add_paragraph()
    title_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_run = title_para.add_run("BRAHHM ARPAN ORGANIC PVT. LTD.")
    title_run.font.size = Pt(18)
    title_run.font.bold = True
    title_run.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)
    title_run.font.name = 'Calibri'

    sub_para = doc.add_paragraph()
    sub_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub_run = sub_para.add_run("JUNE 2026 — CONTENT CALENDAR  |  5 Brands  |  30 Days  |  105 Content Pieces")
    sub_run.font.size = Pt(11)
    sub_run.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
    sub_run.font.name = 'Calibri'

    doc.add_paragraph()  # spacer

    # ── Count summary ──────────────────────────────────────────────────────────
    counts = {"Post": 0, "Reel": 0, "Story": 0}
    for day in CALENDAR:
        for item in day["items"]:
            counts[item["type"]] = counts.get(item["type"], 0) + 1

    summary_para = doc.add_paragraph()
    summary_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    summary_para.add_run(f"Posts: {counts['Post']}   |   Reels: {counts['Reel']}   |   Stories: {counts['Story']}").font.size = Pt(10)

    # ── Legend ─────────────────────────────────────────────────────────────────
    doc.add_paragraph()
    legend_para = doc.add_paragraph()
    legend_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    legend_run = legend_para.add_run(
        "BRANDS:  ● Caveman Organic   ● Health Fields   ● Pusht Organic   ● greendipz   ● Biomart"
    )
    legend_run.font.size = Pt(9)
    legend_run.font.color.rgb = RGBColor(0x44, 0x44, 0x44)

    type_legend = doc.add_paragraph()
    type_legend.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_colored_run(type_legend, "POST", bold=True, color_hex="1A1A1A", size_pt=9)
    type_legend.add_run("   ")
    add_colored_run(type_legend, "REEL", bold=True, color_hex="7B2D8B", size_pt=9)
    type_legend.add_run("   ")
    add_colored_run(type_legend, "STORY", bold=True, color_hex="1A5C9E", size_pt=9)

    doc.add_paragraph()

    # ── Week labels mapping ────────────────────────────────────────────────────
    week_breaks = {
        "June 1":  "WEEK 1  ·  June 1 – 7",
        "June 8":  "WEEK 2  ·  June 8 – 14",
        "June 15": "WEEK 3  ·  June 15 – 21",
        "June 22": "WEEK 4  ·  June 22 – 28",
        "June 29": "WEEK 5  ·  June 29 – 30",
    }

    # ── Build each day ─────────────────────────────────────────────────────────
    for day_data in CALENDAR:
        date_key = day_data["date"]

        # Week header
        if date_key in week_breaks:
            wk_para = doc.add_paragraph()
            wk_run = wk_para.add_run(week_breaks[date_key])
            wk_run.font.size = Pt(10)
            wk_run.font.bold = True
            wk_run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            wk_run.font.name = 'Calibri'
            # shade paragraph
            pPr = wk_para._p.get_or_add_pPr()
            shd = OxmlElement('w:shd')
            shd.set(qn('w:val'), 'clear')
            shd.set(qn('w:color'), 'auto')
            shd.set(qn('w:fill'), '1A1A1A')
            pPr.append(shd)
            wk_para.paragraph_format.space_before = Pt(6)
            wk_para.paragraph_format.space_after  = Pt(2)
            wk_para.paragraph_format.left_indent  = Cm(0.3)

        # Day header row
        day_para = doc.add_paragraph()
        day_para.paragraph_format.space_before = Pt(4)
        day_para.paragraph_format.space_after  = Pt(2)

        date_run = day_para.add_run(f"{day_data['date'].upper()}  {day_data['day'].upper()}")
        date_run.font.size = Pt(10)
        date_run.font.bold = True
        date_run.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)
        date_run.font.name = 'Calibri'

        if day_data.get("holiday"):
            holiday_run = day_para.add_run(f"   ·   {day_data['holiday']}")
            holiday_run.font.size = Pt(9)
            holiday_run.font.bold = False
            holiday_run.font.color.rgb = RGBColor(0x8B, 0x64, 0x27)
            holiday_run.font.name = 'Calibri'

        # Content table for the day
        items = day_data["items"]
        n_cols = len(items)

        # Table: one column per content item
        # Col widths split evenly across usable width (~25.7cm)
        usable_cm = 25.7
        col_w = usable_cm / n_cols

        tbl = doc.add_table(rows=5, cols=n_cols)
        tbl.style = 'Table Grid'
        tbl.alignment = WD_TABLE_ALIGNMENT.LEFT

        row_labels = ["BRAND", "TYPE", "PRODUCT", "ANGLE", "HOOK"]
        row_bold   = [True, True, True, True, False]

        for c_idx, item in enumerate(items):
            brand = item["brand"]
            itype = item["type"]
            brand_hex = BRAND_HEX.get(brand, "333333")
            type_hex  = TYPE_LABEL_HEX.get(itype, "333333")
            type_bg   = TYPE_BG_HEX.get(itype, "F5F5F5")
            angle_hex = ANGLE_HEX.get(item["angle"], "333333")

            # Row 0 — Brand
            cell0 = tbl.rows[0].cells[c_idx]
            set_cell_bg(cell0, brand_hex)
            set_cell_borders(cell0, brand_hex)
            p0 = cell0.paragraphs[0]
            p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r0 = p0.add_run(brand.upper())
            r0.font.size  = Pt(8)
            r0.font.bold  = True
            r0.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            r0.font.name  = 'Calibri'
            cell0.width   = Cm(col_w)

            # Row 1 — Type
            cell1 = tbl.rows[1].cells[c_idx]
            set_cell_bg(cell1, type_bg)
            set_cell_borders(cell1)
            p1 = cell1.paragraphs[0]
            p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r1 = p1.add_run(itype.upper())
            r1.font.size  = Pt(8)
            r1.font.bold  = True
            r1.font.color.rgb = RGBColor(
                int(type_hex[0:2], 16),
                int(type_hex[2:4], 16),
                int(type_hex[4:6], 16)
            )
            r1.font.name = 'Calibri'

            # Row 2 — Product
            cell2 = tbl.rows[2].cells[c_idx]
            set_cell_bg(cell2, "FFFFFF")
            set_cell_borders(cell2)
            p2 = cell2.paragraphs[0]
            r2 = p2.add_run(item["product"])
            r2.font.size  = Pt(8)
            r2.font.bold  = True
            r2.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)
            r2.font.name  = 'Calibri'

            # Row 3 — Angle
            cell3 = tbl.rows[3].cells[c_idx]
            set_cell_bg(cell3, "FAFAFA")
            set_cell_borders(cell3)
            p3 = cell3.paragraphs[0]
            r3 = p3.add_run(item["angle"])
            r3.font.size  = Pt(8)
            r3.font.bold  = True
            r3.font.color.rgb = RGBColor(
                int(angle_hex[0:2], 16),
                int(angle_hex[2:4], 16),
                int(angle_hex[4:6], 16)
            )
            r3.font.name = 'Calibri'

            # Row 4 — Hook
            cell4 = tbl.rows[4].cells[c_idx]
            set_cell_bg(cell4, "FFFFFF")
            set_cell_borders(cell4)
            p4 = cell4.paragraphs[0]
            r4 = p4.add_run(f'"{item["hook"]}"')
            r4.font.size   = Pt(8)
            r4.font.italic = True
            r4.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
            r4.font.name   = 'Calibri'

        doc.add_paragraph().paragraph_format.space_after = Pt(2)

    # ── Footer counts verification ─────────────────────────────────────────────
    doc.add_paragraph()
    footer_para = doc.add_paragraph()
    footer_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer_run = footer_para.add_run(
        f"TOTAL: {counts['Post']} Posts  |  {counts['Reel']} Reels  |  {counts['Story']} Stories  "
        f"|  {counts['Post']+counts['Reel']+counts['Story']} Content Pieces  |  June 2026"
    )
    footer_run.font.size = Pt(9)
    footer_run.font.color.rgb = RGBColor(0x88, 0x88, 0x88)
    footer_run.font.name = 'Calibri'

    # ── Save ───────────────────────────────────────────────────────────────────
    out_path = "June_2026_Content_Calendar_Brahhm.docx"
    doc.save(out_path)
    print(f"Saved: {out_path}")
    print(f"  Posts: {counts['Post']}  |  Reels: {counts['Reel']}  |  Stories: {counts['Story']}")
    print(f"  Total: {counts['Post']+counts['Reel']+counts['Story']}")


if __name__ == "__main__":
    build_document()

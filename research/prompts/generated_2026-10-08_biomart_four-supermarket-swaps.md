# Biomart · Oct 8 2026 · POST · EDUCATE — Four Supermarket Swaps

PRE-FLIGHT ✅ Skills read this session: humanizer-main/SKILL.md, social/SKILL.md, copywriting/SKILL.md, copy-editing/SKILL.md, gpt-image-2/SKILL.md (+ Biomart_Brand_Bible_v2.txt, biomart_content_identity.md, Hook_Matrix_Library.md Biomart block, Caption_Swipe_File.md Biomart block)

**Calendar slot:** research/oct_2026_content_calendar.md → OCTOBER 8 · THURSDAY → BIOMART · POST · EDUCATE · "4 packs that quietly outperform their supermarket cousins" · KPI Saves · Cross-brand

## Visual reference
Pinterest round 2, pick #6 — packs standing on stepped colour plinths ("All Over Spray Collection", https://www.pinterest.com/pin/48413764741625229/). Run archived in `research/reference_library/` (tag `biomart-oct8-4packs-premium-lineup-round2`).

## Auto-fetch receipts
**Product descriptions (Protocol 2):** live `biomart.in/products.json` pulled 2026-10-08 (208 products). All four SKUs in stock.
**Pack images (Protocol 2A):** local storage folder is not reachable from the cloud session, so front-of-pack photos were pulled from the biomart.in product images and saved to `research/prompts/assets/2026-10-08_biomart_four-swaps/`:
1. `1_hf_rozana_honey_front.jpg` — Health Fields Organic Rozana Honey 500g (glass jar, gold lid, cream label, orange "Honey" script)
2. `2_pusht_besan_front.jpg` — Pusht Organic Besan 500g (mustard-yellow pouch, Pusht badge, pakora + kadhi photo)
3. `3_caveman_bakkit_ajwain_front.jpg` — Caveman Bakkit Ajwain Cookies (brown carton, Cave Red Caveman badge, cookie photo)
4. `4_greendipz_tomato_ketchup_front.jpg` — greendipz Tomato Ketchup (glass bottle, black cap, white label, red "TOMATO Ketchup" vertical type)

Note: biomart.in lists the ketchup as "Greendipz Tomato Ketup" (typo on site). The pack itself reads "Tomato Ketchup", so all copy uses that.

## Protocol 3 — Claims Audit

| Claim | Source | Verdict | Action |
|---|---|---|---|
| Honey: raw and unfiltered | biomart.in description | ✅ | KEEP |
| Honey: free from heat treatment | biomart.in description | ✅ | KEEP |
| Honey: 0g added sugar | Pack nutrition panel (biomart.in image 3) | ✅ | KEEP |
| Honey: supports digestion, immunity | biomart.in description | ❌ health claim | REMOVE |
| Honey: rich in antioxidants, enzymes | biomart.in description | ❌ needs lab data | REMOVE |
| Besan: made from 100% chana dal | Pack front | ✅ | KEEP |
| Besan: free from bleaching agents, artificial preservatives, synthetic colours | biomart.in description | ✅ | KEEP |
| Besan: low glycemic index, rich in protein | biomart.in description | ❌ needs lab data | REMOVE |
| Cookies: millet-based | biomart.in description | ✅ | KEEP |
| Cookies: sweetened with honey | biomart.in description | ✅ | KEEP |
| Cookies: free from refined flour | biomart.in description | ✅ | KEEP |
| Cookies: ajwain supports digestion | biomart.in description | ❌ therapeutic | REMOVE |
| Cookies: rich in fibre, sustained energy | biomart.in description | ❌ needs lab data | REMOVE |
| Ketchup: made from organic tomatoes | biomart.in description | ✅ | KEEP |
| Ketchup: no artificial preservatives or colours | biomart.in description | ✅ | KEEP |
| Any claim about what supermarket brands contain | — | ❌ unverifiable | REMOVE: we only state what our label says and invite the reader to check theirs |

---

# 13-Point Post Package

**1. CONTENT ANGLE:** EDUCATE (label-literacy, curator voice)

**2. IDEA TITLE:** Same Aisle, Better Label — four everyday packs worth swapping in

**3. HOOK:** Same aisle. Better label.

**4. EXECUTION:**
- Four everyday staples that already live in an Indian cart (honey, besan, tea-time biscuits, ketchup), each swapped for a house-brand pack stocked on Biomart.
- One brand per pack (Health Fields, Pusht, Caveman, greendipz), so it reads as Biomart curating rather than one brand selling.
- The image teaches one label fact per pack. The caption asks the reader to turn their current pack around and compare, so the "supermarket cousin" is the reader's own jar. No competitor is named or shown.
- Biomart curation voice: a friend who runs an organic store and reads the back of the pack.

**5. VISUAL DIRECTION:**
- **New template: T96 — Stepped Plinth Quartet** (from Pinterest ref #6). Four packs stand on four stepped, rectangular colour plinths rising left to right, like a staircase of display blocks, shot slightly from the right so the steps read as depth.
- Plinth colours stay inside the Biomart world: deep market green, mid sage green, warm gold and warm ivory. Backdrop is a soft mint-cream wall with a gentle warm-gold light falling from the upper left.
- Pack order, low to high: ketchup (tallest pack, lowest step) → besan → cookies (carton lying flat, front facing camera) → honey (highest step). This balances pack heights so the four tops form a soft rising line.
- Headline sits in the clean upper-left negative space; each label callout sits on the plinth face directly under its pack; the CTA goes small, bottom-right.
- Callout mode: hairline-free bold labels printed on the plinth faces (no chips, no boxes).
- Ratio 4:5 (1080×1350). Model `gpt-image-2.5-sunburst` (four-pack fidelity) · quality `xhigh` (7 text zones).
- Template rotation: last Biomart posts used T94 (Sept 28) and editorial carousels. T96 is new, so no repeat.

**6. IN-IMAGE TEXT REVIEW — confirm before Point 7 is written**

| Element | Proposed Text | Style | Position |
|---|---|---|---|
| Headline line 1 | Same aisle | Large serif display, deep market green | Upper-left negative space |
| Headline line 2 | Better label | Same serif, warm gold, same size | Directly under line 1 |
| Callout — ketchup | NO ARTIFICIAL COLOURS | Bold sans caps, warm ivory | Printed on the face of the deep-green plinth under the ketchup |
| Callout — besan | 100% CHANA DAL · UNBLEACHED | Bold sans caps, warm ivory | Face of the sage plinth under the besan |
| Callout — cookies | MILLETS · NO REFINED FLOUR | Bold sans caps, deep market green | Face of the gold plinth under the cookies |
| Callout — honey | RAW · NEVER HEAT-TREATED | Bold sans caps, deep market green | Face of the ivory plinth under the honey |
| Website CTA | Shop now on biomart.in | Small quiet sans, deep market green | Bottom-right corner, generous margin |

**7. GPT IMAGE 2.5 PROMPT:** Held until the Point 6 text is confirmed (Protocol 6 text confirmation).

**8. CAPTION**

Humanizer audit: cut "quietly outperform their supermarket cousins" (sloganish calendar phrasing → replaced with the plain "Same aisle. Better label."), cut a "honey, besan, biscuits and ketchup, all upgraded" rule-of-four list ending (→ each pack gets its own sentence with one label fact), cut "It's not about changing your kitchen, it's about…" negative parallelism (→ "None of these ask you to cook differently").

Same aisle. Better label.

Half our grocery cart runs on autopilot. Honey, besan, the tea-time biscuits, ketchup. Nobody reads those labels twice.

So we did. Health Fields Rozana Honey is raw and never heat-treated. Pusht Besan is 100% chana dal with no bleaching agents. Caveman Bakkit Ajwain Cookies are made with millets and honey instead of refined flour. greendipz Tomato Ketchup skips artificial colours and preservatives.

None of these ask you to cook differently. They go where the old packs sat.

If the honey is going in, add Health Fields Calming Chamomile and your 9pm cup is sorted.

Turn your current packs around tonight and compare. Then pick your first swap.

Shop now on biomart.in

#Biomart #OrganicMegastore #ReadTheLabel

**10. WEBSITE CTA:** In-image "Shop now on biomart.in" (bottom-right, listed in Point 6). Caption ends "Shop now on biomart.in". All four SKUs are sold on biomart.in.

**11. VARIATION**

Humanizer audit: cut "Ever wondered what's really in…" (persuasive-authority opener → direct instruction), cut "simple, honest, pure" triple (rule of three → removed), cut a closing "Your pantry deserves better" generic upbeat line (→ concrete next step).

Flip your honey jar over. What does the back say?

That one habit is how we pick what goes on biomart.in. Four packs passed this week. The honey is raw and never heat-treated. The besan is 100% chana dal, unbleached. The ajwain cookies use millets in place of refined flour. The ketchup has no artificial colours.

Health Fields, Pusht, Caveman and greendipz, one order.

Save this for your next restock 🛒

Shop now on biomart.in

#Biomart #OrganicMegastore #PantrySwap

**12. WHY IT WILL PERFORM:**
- Saves: a four-item swap list is reference content people keep for their next grocery run, which matches the slot's Saves KPI.
- The reader's own jar plays the "supermarket cousin", so the post gets an action ("turn the pack around") without naming a competitor or making a comparative claim we can't prove.
- One brand per pack fits the curation identity ("the person who picked everything on the shelf") and spreads discovery across four house brands.
- The 4-word hook works as both headline and first caption line, and reads at thumbnail size.
- Stepped plinths are new on the Biomart grid and give a premium marketplace look without a busy flat-lay.

**13. BUNDLING SUGGESTION:** Health Fields Calming Chamomile with the Rozana Honey (evening cup). Surfaced in the caption as one line.

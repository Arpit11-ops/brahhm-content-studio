# Biomart · Oct 8 2026 · POST · EDUCATE — Four Supermarket Swaps

PRE-FLIGHT ✅ Skills read this session: humanizer-main/SKILL.md, social/SKILL.md, copywriting/SKILL.md, copy-editing/SKILL.md, gpt-image-2/SKILL.md (+ Biomart_Brand_Bible_v2.txt, biomart_content_identity.md, Hook_Matrix_Library.md Biomart block, Caption_Swipe_File.md Biomart block)

**Calendar slot:** research/oct_2026_content_calendar.md → OCTOBER 8 · THURSDAY → BIOMART · POST · EDUCATE · "4 packs that quietly outperform their supermarket cousins" · KPI Saves · Cross-brand

## Visual reference
Pinterest round 2, pick #6 — packs standing on stepped colour plinths ("All Over Spray Collection", https://www.pinterest.com/pin/48413764741625229/). Run archived in `research/reference_library/` (tag `biomart-oct8-4packs-premium-lineup-round2`).

## Auto-fetch receipts
**Product descriptions (Protocol 2):** live `biomart.in/products.json` pulled 2026-10-08 (208 products). All four SKUs in stock.
**Pack images (Protocol 2A):** local storage folder is not reachable from the cloud session, so front-of-pack photos were pulled from biomart.in, then replaced with the pack photos Puran uploaded on 2026-10-08, saved to `research/prompts/assets/2026-10-08_biomart_four-swaps/`:
1. `1_hf_rozana_honey_front.png` — Health Fields Organic Rozana Honey 500g (glass jar, gold lid, cream label, orange "Honey" script)
2. `2_pusht_besan_front.png` — Pusht Organic Besan 500g (mustard-yellow pouch, Pusht badge, pakora + kadhi photo)
3. `3_caveman_bakkit_ajwain_front.png` — Caveman Bakkit Ajwain Cookies (brown carton, Cave Red Caveman badge, cookie photo)
4. `4_greendipz_tomato_ketchup_front.png` — greendipz Tomato Ketchup (glass bottle, black cap, white label, red "TOMATO Ketchup" vertical type)

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

**7. GPT IMAGE 2.5 PROMPT** (Point 6 text confirmed by Puran 2026-10-08 with pack upload, no edits)

TEMPLATE: T96 — Stepped Plinth Quartet
Model: gpt-image-2.5-sunburst
Quality: xhigh
Upload (attach in this exact order) ✅ YES:
1. `research/prompts/assets/2026-10-08_biomart_four-swaps/1_hf_rozana_honey_front.png`
2. `research/prompts/assets/2026-10-08_biomart_four-swaps/2_pusht_besan_front.png`
3. `research/prompts/assets/2026-10-08_biomart_four-swaps/3_caveman_bakkit_ajwain_front.png`
4. `research/prompts/assets/2026-10-08_biomart_four-swaps/4_greendipz_tomato_ketchup_front.png`

GPT IMAGE 2.5 PROMPT:
```
Create a new image. Image 1 is the Health Fields Organic Rozana Honey 500g jar; Image 2 is the Pusht Organic Besan 500g pouch; Image 3 is the Caveman Bakkit Ajwain Cookies carton; Image 4 is the greendipz Tomato Ketchup bottle. All four are reference-only, reproduce each with total pack fidelity. Ignore all other images in the conversation.

Preserve on Image 1, the honey jar: the faceted glass jar silhouette with dark amber honey showing through, the gold metal lug lid, the gold-bordered cream label with its tall tab rising over the lid, the line-art bee hive and dripping honeycomb illustration, the Health Fields "SINCE 2003" badge, the green vegetarian dot, "ORGANIC" and "Rozana" in orange, the dripping orange-gold "Honey" script, "BEST FROM THE BEES", the line-art flowers on both sides and the orange base band reading "NET WT.: 500 g". Preserve on Image 2, the besan pouch: the mustard-yellow gusseted pouch with crimped top seal, "SINCE 2003" above the Pusht Organic tree badge, the green vegetarian dot, "ORGANIC Besan" in deep green, the small description line, the food photograph of pakoras, ladoo, dhokla, green chilli and a bowl of kadhi, the dark green ribbon reading "Made From 100% Chana Dal", the certification row with USDA Organic, India Organic, Jaivik Bharat and PGS-India Organic marks, "Net Weight : 500 g | 17.63 oz" and the small disclaimer line. Preserve on Image 3, the cookie carton: the long horizontal carton with a gold-brown sweep on the left and dark chocolate-brown on the right, the Cave Red Caveman badge, "BakkiT AJWAIN Cookies" with "with the goodness of millet & carom seeds", the four ajwain-topped cookies on a white tray, the spoon of carom seeds, the green vegetarian dot, the script line "Bridging superfoods & your lifestyle..." and "MADE WITH THE FINEST QUALITY OF INGREDIENTS" along the base. Preserve on Image 4, the ketchup bottle: the tall glass bottle with black cap and red ketchup visible above and below the label, the white label with the arched green line "GUILT FREE CLEAN FOOD", the greendipz green speech-bubble logo, the green vegetarian dot, red vertical "TOMATO Ketchup" type with "MADE WITH REAL TOMATOS" exactly as printed, the tomato photographs with basil leaves, and the bottom line "NO ADDED ARTIFICIAL PRESERVATIVES · NO ARTIFICIAL COLOUR · NO ARTIFICIAL FLAVOUR". Change nothing on any pack: no repositioned elements, no new text, no missing text, no spelling corrections, no colour shift, no logo redraw, no illustration redraw, no SKU substitution between the four.

Editorial product shot of four packs standing on four stepped rectangular display plinths that rise like a staircase from lower-left to upper-right, framed from a slight three-quarter angle from the right so each step reads as a solid block with a visible front face and top surface. The greendipz ketchup bottle stands upright on the lowest step at the left, the Pusht besan pouch stands upright on the second step, the Caveman carton stands upright on its long base on the third step with its front face toward camera, and the Health Fields honey jar sits on the highest step at the right, so the tops of the four packs form a gentle rising line. Every pack faces camera squarely, labels fully lit with zero shadow across any label face, each pack shown whole with nothing cropped, roughly equal visual weight across the four. The world is a soft mint-cream studio wall with warm daylight falling from the upper left, a clean Whole Foods calm with no props. The plinths stay inside one green-and-gold family: the lowest step in deep market green, the second in muted sage green, the third in warm honey gold, the highest in warm ivory, each with crisp matte edges and a soft contact shadow cast down onto the step below, and the background, plinths and light all belong to the same green, gold and cream colour world while the packs keep their own printed colours. Render exactly once: 'Same aisle' on line 1 in a large refined serif display face in deep market green in the clean upper-left negative space. Render exactly once: 'Better label' on line 2 in the same serif at the same size in warm gold directly beneath line 1. Render exactly once: 'NO ARTIFICIAL COLOURS' printed on the front face of the deep green plinth under the ketchup in bold sans-serif caps in warm ivory. Render exactly once: '100% CHANA DAL · UNBLEACHED' printed on the front face of the sage plinth under the besan in bold sans-serif caps in warm ivory. Render exactly once: 'MILLETS · NO REFINED FLOUR' printed on the front face of the gold plinth under the cookies in bold sans-serif caps in deep market green. Render exactly once: 'RAW · NEVER HEAT-TREATED' printed on the front face of the ivory plinth under the honey in bold sans-serif caps in deep market green. The four plinth labels are the second visual layer after the packs, sized roughly 1.5 times the website line, tight letter-spacing, immediately readable at Instagram feed thumbnail scale, set flat on the plinth faces with no chips, boxes or pills behind them. Render exactly once: 'Shop now on biomart.in' in a small quiet sans-serif in deep market green in the bottom-right corner with a generous margin. No full stops on any text, no extra text, no price, no offer, no logo added outside the packs, no props, no ingredients, no scattered seeds or crumbs, no wooden bowls, no burlap, no hands, no people, no tilted packs, no pack overlapping another pack, no duplicate text zones, no repeated headlines, no repeated callouts, no SKU swap on any pack. Abundant marketplace editorial, Whole Foods store aesthetic, clean warm studio light, market green and warm gold color world, premium organic curation, trustworthy Indian marketplace. 4:5 vertical portrait.
```

**Iteration path (Protocol 6A):** if one thing is off, send back: `Edit the previous image. Change: [one thing, e.g. "move 'RAW · NEVER HEAT-TREATED' up so it sits centred on the ivory plinth face"]. Preserve: headline, all four packs, all plinth labels, plinth colours, background, website CTA, lighting, ratio. Constraints: no new elements, no colour shift on the packs, no re-rendering of any preserved element, no duplicate text zones, no SKU swap on any pack.` A wrong-SKU pack means a full regen with the same prompt, not an edit.

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

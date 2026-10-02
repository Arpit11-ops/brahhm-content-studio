---
date: 2026-09-28
brand: Health Fields
type: CAROUSEL (6 slides, 4:5)
angle: EDUCATE ❤️ (Heart Day build — day 2 of 3-day HF tent-pole arc)
products: HealthFields Wellness Organic Tulsi Green Tea Premium (25 tea bags) + HealthFields Organic Ashwagandha Powder
tent-pole: World Heart Day (Sept 29) — Sept 27 tease → **Sept 28 carousel** → Sept 29 reel
silence-window: Pitru Paksha (Sept 26+) — quiet wellness voice, no aggressive ATTACK
website: healthfields.in
render-status: ✅ all 6 slides rendered — assets in `research/prompts/assets/2026-09-28_healthfields_heart-day-carousel/`
---

# PRE-FLIGHT ✅ Skills read this session
- `skills/humanizer-main/humanizer-main/SKILL.md`
- `skills/marketingskills-main/skills/social/SKILL.md`
- `skills/marketingskills-main/skills/copywriting/SKILL.md`
- `skills/marketingskills-main/skills/copy-editing/SKILL.md`
- `skills/gpt-image-2/SKILL.md`

---

## Auto-fetch receipts

**Product identity (Protocol 2):**
- `HealthFields Wellness Organic Tulsi Green Tea Premium | 25 Tea Bags` — handle `healthfields-wellness-organictulsi-green-tea-select` (confirmed in `research/catalogs/healthfields_catalog.json`)
- `Organic Ashwagandha Power` — handle `organic-ashwagandha-power` (catalog title has typo "Power" → actual product form is powder; on-slide + caption copy uses "Ashwagandha Powder")

**Pack references (Protocol 2A):**
- Tulsi Green Tea Premium: `C:\Users\arpit\Documents\storage\arpan organic\health fields\OrganicTulsiGreenTeaPremium01_2.jpg` (mirrored in assets as `tulsi_green_pack.jpg`)
- Ashwagandha Powder: `research/prompts/assets/2026-09-28_healthfields_heart-day-carousel/ashwagandha_pack.jpg`

---

## Protocol 3 — Claims Audit

| Claim | Source | Verdict | Action |
|---|---|---|---|
| Tulsi Green Tea Premium — 25 tea bags | SKU name | ✅ | KEEP |
| Ashwagandha powder form | SKU + slide render | ✅ | KEEP |
| Certified organic | SKU name + HF badge | ✅ | KEEP |
| Health Fields brand | SKU name | ✅ | KEEP |
| "5-minute morning ritual" framing | Editorial voice | ✅ | KEEP (describes format, not therapy) |
| "Heart that has done a lot" | Editorial voice | ✅ | KEEP (RELATE cadence, not medical claim) |
| Ancestral / grandmother recognition of the ritual | Category truth (tulsi + ashwagandha both centuries-old in Indian home use) | ✅ | KEEP |
| "Ashwagandha reduces stress" / "Tulsi lowers blood pressure" / adaptogen therapeutic claims | — | ❌ | REMOVE (no lab data referenced, therapeutic claim) |
| "Supports heart health" / "heart-friendly" | — | ❌ | REMOVE |
| Ingredient percentages | — | ❌ | REMOVE per strict rule |
| FSSAI / licence numbers | — | ❌ | REMOVE per GPT-no-FSSAI rule |
| "A quieter kind of care" | Editorial voice | ✅ | KEEP — voice, not claim |

---

# 13-Point Post Package

**1. CONTENT ANGLE:** EDUCATE ❤️ (Heart Day build — quiet ritual editorial)

**2. IDEA TITLE:** The 5-Minute Morning — A Health Fields Ritual for a Heart That Has Done a Lot

**3. HOOK (under 8 words):** Five minutes. Two staples. One heart.

**4. EXECUTION:**
6-slide carousel that positions the tulsi-green + ashwagandha-powder pairing as a quiet daily-morning ritual rather than a supplement stack. Deep teal HF world with warm-gold rim light, cream serif-hybrid display type, line-drawn cup + spoon icons standing in as motif. No health claims about either ingredient — the ritual itself IS the emotional promise. Sits inside the 3-day Heart Day arc (Sept 27 tease → Sept 28 carousel → Sept 29 reel). Fully compatible with Pitru Paksha silence — ancestral-wellness voice, zero aggression.

**5. VISUAL DIRECTION**

**New template: T95 — Quiet Ritual Editorial** (6-slide HF wellness ritual carousel — deep teal + warm gold upper-right rim + cream serif-hybrid display type + line-drawn ritual icons + steaming ceramic vessel motif + healthfields.in CTA baked lower-right or supporting-line placement)

**6-slide arc + rendered asset paths:**

| Slide | Beat | Headline (baked) | Support text (baked) | Visual anchor | Asset |
|---|---|---|---|---|---|
| 1 | COVER | *the 5-minute morning for a heart that has done a lot* | *one cup. one spoon. two organic staples* + `WORLD HEART DAY · SEPT 29` + `available on healthfields.in` | Steaming deep-teal ceramic bowl, lower-right | `slide1_cover.png` |
| 2 | SETUP | *before the phone. before the day.* | *five minutes belong to the heart* | Empty ceramic cup + spoon at rest | `slide2_setup.png` |
| 3 | TULSI | *step one — a cup of tulsi green* | *the tea an Indian grandmother would recognise* | Tulsi Green Tea Premium pack + poured cup | `slide3_tulsi.png` |
| 4 | ASHWA | *step two — a spoon of ashwagandha* | *stirred into warm milk while the tea steeps* | Ashwagandha Powder pack + spoon + warm-milk vessel | `slide4_ashwa.png` |
| 5 | COMPARE | *the pair on your counter* | *tulsi green + ashwagandha powder — the two-piece morning kit* | Both packs side by side, cup + spoon in front | `slide5_compare.png` |
| 6 | CLOSE | *one cup. one spoon / a quieter kind of care* | *the tulsi green + the ashwagandha powder now on* `HEALTHFIELDS.IN` + `WORLD HEART DAY · SEPT 29 · A HEALTH FIELDS RITUAL` | Line-drawn cup + spoon icons | `slide6_close.png` |

**Design DNA locked across the batch:** deep teal ground (Health Fields Deep Teal #003C32 territory), warm-gold rim light from upper-right, cream-white type in Aesop-clinical serif hybrid for display, small-caps letter-spaced sans for supporting lines, single accent uppercase healthfields.in in warm gold, hairline line-drawn ritual icons.

**Render status:** ✅ Complete — sunburst + xhigh already run in prior session, all 6 slides approved.

**6. IN-IMAGE TEXT REVIEW — locked (already rendered)**

All baked text as shown in the slide table above. `available on healthfields.in` appears on slide 1 (bottom-right, quiet) and `HEALTHFIELDS.IN` appears as the CTA anchor on slide 6 (warm gold, centred).

NO DOTS RULE: The internal full stops in prose lines like "one cup. one spoon." are sentence-ending punctuation between two complete short sentences, not decorative trailing dots on a headline — acceptable. Slide-anchor labels (`step one`, `step two`) end without dots. CTA `available on healthfields.in` ends without dots. Complies.

---

**7. GPT IMAGE 2.5 PROMPTS** (for reference / re-render — slides already rendered)

Because these 6 slides are already rendered and approved, the prompts below are documented as **reference** for any future surgical edits or re-runs. For any single-element fix, run Protocol 6A surgical edit on the existing asset rather than regenerating.

**Shared preamble to prepend to every slide prompt:**

```
Model: gpt-image-2.5-sunburst
Quality: xhigh
Ratio: 4:5 (1080×1350)
```

**Shared color + light + type system (fold into every slide brief):**

Deep teal ground (Health Fields Deep Teal, roughly #003C32), warm gold rim light glowing from upper-right corner and softly falling off across the frame, subtle watercolour wash texture in the ground for hand-painted depth, cream-white type in a confident Aesop-clinical serif-hybrid display face for headlines, letter-spaced cream small-caps for supporting lines, a single warm-gold accent uppercase mark for the CTA when present, hairline cream line-drawings for ritual icons.

**Iteration path (Protocol 6A) for any surgical edit on the existing renders:**

```
Change: [one specific thing — e.g. "swap the cover subhead to 'a heart that has carried a lot'"]
Preserve: cover headline "the 5-minute morning for a heart that has done a lot", WORLD HEART DAY · SEPT 29 date band, steaming bowl in lower-right, deep-teal ground, warm-gold rim light, cream type system, available on healthfields.in CTA
Constraints: no new elements, no colour shift, no re-render of any preserved element, no duplicate text zones
```

---

**8. CAPTION**

**Humanizer audit:** cut "Both organic, both from Health Fields, both now on healthfields.in" (rule-of-three parallelism — collapsed to the single compact clause "Organic, from Health Fields, on healthfields.in"), cut "asks for a little in return" (soft AI-sentimental slogan cadence — replaced with the plain factual line "for the mornings when your heart has done a lot"), cut a first-draft "That's the ritual" opener (persuasive-authority trope — replaced with the direct "The whole ritual takes five minutes").

Five minutes. Two staples. One heart.

A cup of Tulsi Green Tea Premium while the kettle cools. A spoon of Ashwagandha Powder stirred into warm milk. The whole ritual takes five minutes — for the mornings when your heart has done a lot.

Organic, from Health Fields, on healthfields.in.

Save it for tomorrow morning.

#HealthFields #HeartRitual #OrganicByNature

---

**10. WEBSITE CTA**
- In-image CTA (slide 1): `available on healthfields.in` — small warm-gold sans-serif, lower-right corner, no dots
- In-image CTA (slide 6): `HEALTHFIELDS.IN` — accent warm-gold uppercase, centred anchor
- Caption CTA: `Save it for tomorrow morning.` (soft close) + implicit domain via body line `on healthfields.in`
- Point 6 in-image text review includes the baked CTAs ✅

---

**11. VARIATION CAPTION**

**Humanizer audit:** cut "Not a supplement stack. Not a workout plan." (negative parallelism pattern — replaced with a direct declarative that skips the framing setup), cut a first-draft "Both on healthfields.in" (paired "both" cadence — collapsed to plain "On healthfields.in"), cut "in a form the morning actually has time for" second em-dash pass (em-dash overuse — merged into a single flowing clause).

A quieter kind of care.

A cup of tulsi green tea and a spoon of ashwagandha powder, the same ritual an Indian grandmother would recognise, in the form the morning actually has time for.

On healthfields.in for World Heart Day.

#HealthFields #QuietRitual #HeartDay

---

**12. WHY IT WILL PERFORM**
- **Save trigger:** the 6-slide ritual format is textbook save-native — Reels and feed both index for saves on step-by-step ritual carousels, and the calendar KPI for this slot is Saves + Reach.
- **Reach cushion (Heart Day halo):** posting on Sept 28 lets the carousel accumulate saves across the Sept 29 traffic spike, and the "Save it for tomorrow morning" CTA is a direct call for the save action that lifts distribution.
- **Pitru Paksha compliance:** ancestral-wellness voice, grandmother-recognisable ritual, no ATTACK energy, no launch push, no aggressive CTA. Respects the silence window while still delivering business intent.
- **Emotional altitude without medical claim:** "a heart that has done a lot" is the whole hook — RELATE-shaped even inside an EDUCATE angle — and it never asks the reader to believe the tea or the powder does anything therapeutic. Nothing to fact-check, nothing to be sued for.
- **Feed thumbnail read:** deep teal + cream serif at 1x thumbnail scale is instantly recognisable as Health Fields — the batch reads as a HF grid coherence hit, not a one-off.
- **Cross-brand tie-in:** shares the same product pair as the Sept 29 HF reel and the Biomart heart-shelf post — the three units together form a coordinated Heart Day cluster instead of three isolated posts.

---

**13. BUNDLING SUGGESTION**
Chamomile Calming Tea — sits in the same HF wellness shelf as the tulsi green tea and works as the evening companion to the morning ritual. Surface as a natural pairing in the caption body if the post over-performs (currently held back to keep the primary caption clean and single-focus).

---

## Point 7 upload flag
✅ N/A for this run — slides already rendered. If re-rendering any single slide, upload the corresponding pack ref (Tulsi Green Tea Premium jpg for slide 3, Ashwagandha Powder jpg for slide 4, both for slide 5).

## VEE log entry needed
Append T95 to `Visual_Execution_Engine_v4_txt.txt` — **T95 Quiet Ritual Editorial** (6-slide HF wellness ritual carousel — deep teal + warm gold upper-right rim + cream serif-hybrid display + line-drawn ritual icons + steaming ceramic vessel + healthfields.in CTA, Sept 28 2026).

## Heart Day cluster tie-in
This carousel is unit 2 of a 3-post Heart Day cluster:
- Sept 27 tease (HF story) — already posted
- **Sept 28 carousel — this file**
- Sept 29 reel (HF reel #35, "One heart, four decades" — 60s: 30s / 40s / 50s / 60s morning ritual with tea) — Tulsi Green + Chamomile

Same-day Biomart heart-shelf post ([generated_2026-09-28_biomart_heart-day-4-oils.md](generated_2026-09-28_biomart_heart-day-4-oils.md)) runs as the marketplace-voice counterpart to this HF wellness-voice unit.

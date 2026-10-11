# CODEX IMAGE-GEN RUN-BOOK
## Biomart Carousel — "What Organic Actually Looks Like" (7 slides)
Date: 2026-10-11 · Brand: Biomart · Ratio: 4:5 (1080×1350) · Template: T94

---

## ⚙️ INSTRUCTIONS TO CODEX — READ FIRST, THEN EXECUTE ALL 7 SLIDES

You are generating 7 carousel slide images. For **each** slide block below:

1. Use your **native image generation tool** — do NOT write Python, do NOT call the OpenAI API directly, do NOT write any code.
2. Pass the slide's **PROMPT verbatim** to the image tool. Do NOT summarise, condense, rewrite, or "improve" it. Character-for-character.
3. Attach the slide's **REFERENCE PACKS in the exact order listed** (Image 1 first, Image 2 second, …). Do not reorder or drop any. If a reference is a URL, download it to `research/prompts/assets/2026-10-11_biomart_what-organic-looks-like/refs/` first, then attach the local file.
4. **Model:** `gpt-image-2.5-sunburst` (do NOT swap or downgrade the model, even under load).
5. **Quality:** `xhigh`. **Aspect ratio:** `4:5` vertical.
6. Call the image tool **once** per slide and **save the PNG to the exact Output path** given in that slide block.
7. Generate slides in order 1 → 7. Keep going until all 7 PNGs exist.

Output folder (create if missing): `research/prompts/assets/2026-10-11_biomart_what-organic-looks-like/`

If a render comes back with duplicate text, missing callouts, or a swapped SKU, re-run that one slide once with the same prompt and references.

---

## 📦 REFERENCE PACKS (download these to `refs/` if local pack files aren't present)

| Key | Product | Local pack (if available) | Fallback image URL |
|---|---|---|---|
| PUMPKIN | HF Raw Pumpkin Seeds 250g | `C:\Users\arpit\Documents\storage\arpan organic\health fields\` | https://cdn.shopify.com/s/files/1/0740/9532/9337/files/pumpkin-seed-front.jpg?v=1761829264 |
| QUINOA | Pusht Quinoa Millet | `C:\Users\arpit\Documents\storage\arpan organic\pusht\` | https://cdn.shopify.com/s/files/1/0740/9532/9337/files/QuinoaMillet01.jpg?v=1771701940 |
| SESAME | Pusht Cold Pressed White Sesame Oil 1L | `C:\Users\arpit\Documents\storage\arpan organic\pusht\` | https://cdn.shopify.com/s/files/1/0740/9532/9337/files/pusht-sesame-oil.jpg?v=1761829376 |
| HONEY | Organic Rozana Honey 500G | `C:\Users\arpit\Documents\storage\arpan organic\health fields\` | https://cdn.shopify.com/s/files/1/0740/9532/9337/files/OrganicHoney01.jpg?v=1771687081 |
| AMARANTH | HF Amaranth Flour (Rajgira Atta) 500g | `C:\Users\arpit\Documents\storage\arpan organic\health fields\` | https://cdn.shopify.com/s/files/1/0740/9532/9337/files/amaranth-atta-front.jpg?v=1761829281 |

Prefer the real local pack file when it exists; use the URL only as a fallback.

---

## 🖼️ SLIDE 1 — COVER
**Output:** `research/prompts/assets/2026-10-11_biomart_what-organic-looks-like/slide1_cover.png`
**References (in order):** 1=PUMPKIN · 2=QUINOA · 3=SESAME · 4=HONEY · 5=AMARANTH

**PROMPT:**
```
Create a new image. Images 1 to 5 are the five Biomart product packs — Image 1 the HealthFields raw pumpkin seeds pouch, Image 2 the Pusht quinoa millet pouch, Image 3 the Pusht cold-pressed white sesame oil bottle, Image 4 the Organic Rozana honey jar, Image 5 the HealthFields amaranth flour pouch; all reference-only, reproduce each with total pack fidelity, attachment order matching this role order. Ignore every other image in the conversation. Preserve on every pack: its silhouette, cap seal and base geometry, ground colour exactly as printed, the brand wordmark and badge as printed, every illustration and product photograph on the pack, the full label with every line of printed copy and all multilingual subtitles, the quality seal, the green vegetarian dot, and the entire bottom certification row including every certification stamp and small-print element. Change nothing on any pack — no repositioned elements, no new or missing text, no colour shift, no logo redraw, no SKU substitution. Editorial wide shot of the five packs standing upright in one clean row on a warm oat-cream studio surface, premium organic marketplace feel, soft diffused daylight from the upper left with gentle long shadows, shallow depth so the packs stay crisp while the warm-neutral background falls away softly, abundant Whole Foods shelf calm, the whole frame living in one warm cream-and-oat colour world with only market-green and warm-gold as accents, every label fully lit with zero shadow on the label faces. Keep clean negative space across the top third for the headline. Render exactly once: 'WHAT ORGANIC ACTUALLY LOOKS LIKE' as a bold editorial serif headline in deep market-green across the top third. Render exactly once: 'five staples with the quality on the label' in a quiet warm-gold sans-serif directly beneath the headline. Render exactly once: a row of seven small dots centred at the very bottom with the first dot filled market-green and the rest hollow. Render exactly once: 'Shop now on biomart.in' in small quiet charcoal sans-serif anchored bottom-right. No full stops anywhere in the text, no duplicate text zones, no repeated headlines, no repeated dot row, no repeated CTA, no SKU swap on any pack, no rustic props, no wooden bowls, no burlap or jute, no price callouts, no promotional badges, no link-in-bio or swipe wording. abundant marketplace editorial, Whole Foods store aesthetic, clean warm studio light, market green and warm gold color world, premium organic curation, trustworthy Indian marketplace. 4:5 aspect ratio.
```

---

## 🖼️ SLIDE 2 — PICK 01 · RAW PUMPKIN SEEDS
**Output:** `research/prompts/assets/2026-10-11_biomart_what-organic-looks-like/slide2_pumpkin-seeds.png`
**References (in order):** 1=PUMPKIN

**PROMPT:**
```
Create a new image. Image 1 is the Health Fields Organic Raw Pumpkin Seeds 250g pouch — reference-only, reproduce with total pack fidelity. Ignore all other images in the conversation. Preserve on the pack: pouch silhouette, top seal and base geometry, the pack ground colour exactly as printed, the Health Fields wordmark and badge as printed, the pumpkin-seed illustration and any product photograph on the label, the full label with every line of printed copy including the raw pumpkin seeds lines and all multilingual subtitles, the quality seal, the green vegetarian dot, and the full bottom certification row including every certification stamp and small-print element. Change nothing on the pack — no repositioned elements, no new or missing text, no colour shift, no logo redraw, no illustration redraw, no SKU substitution. Editorial hero shot of the pouch standing upright and centred on a warm oat-cream studio surface, premium organic marketplace feel, soft diffused daylight from the upper left, a single soft long shadow, shallow depth so the label stays razor-sharp while the warm-neutral background falls away, the entire frame in one warm cream-and-oat colour world with only market-green and warm-gold as accents, the label fully lit with zero shadow on the label face. Three hairline callout pointers touch the pouch, their labels set as bold sans-serif caps roughly 1.5x the footer text with tight letter-spacing so they read clearly at feed-thumbnail scale, pure text on thin hairline pointers with no chips, no boxes and no coloured blocks, together forming the second visual layer after the pack. Render exactly once: '01' as an oversized warm-gold editorial numeral in the upper-left negative space. Render exactly once: 'Raw pumpkin seeds' as a bold deep-green serif product name in the upper third. Render exactly once: 'never roasted, grown without pesticides' as a quiet charcoal sans-serif line beneath the name. Render exactly once: 'RAW' as the first hairline callout label. Render exactly once: 'CERTIFIED ORGANIC' as the second hairline callout label. Render exactly once: 'NON-GMO' as the third hairline callout label. Render exactly once: 'SEEDS' as a small warm-gold category tag in a top corner. Render exactly once: a row of seven small dots centred at the very bottom with the second dot filled market-green and the rest hollow. Render exactly once: 'Shop now on biomart.in' in small quiet charcoal sans-serif anchored bottom-right. No full stops anywhere in the text, no duplicate text zones, no repeated numerals, no repeated callouts, no repeated dot row, no repeated CTA, no coloured chip blocks, no SKU swap, no rustic props, no wooden bowls, no burlap or jute, no price callouts, no promotional badges. abundant marketplace editorial, Whole Foods store aesthetic, clean warm studio light, market green and warm gold color world, premium organic curation, trustworthy Indian marketplace. 4:5 aspect ratio.
```

---

## 🖼️ SLIDE 3 — PICK 02 · QUINOA
**Output:** `research/prompts/assets/2026-10-11_biomart_what-organic-looks-like/slide3_quinoa.png`
**References (in order):** 1=QUINOA

**PROMPT:**
```
Create a new image. Image 1 is the Pusht Organic Quinoa Millet pouch — reference-only, reproduce with total pack fidelity. Ignore all other images in the conversation. Preserve on the pack: pouch silhouette, top seal and base geometry, the pack ground colour exactly as printed, the Pusht Organic wordmark and badge as printed, the quinoa illustration and any product photograph on the label, the full label with every line of printed copy including the quinoa millet lines and all multilingual subtitles, the quality seal, the green vegetarian dot, and the full bottom certification row including every certification stamp and small-print element. Change nothing on the pack — no repositioned elements, no new or missing text, no colour shift, no logo redraw, no illustration redraw, no SKU substitution. Editorial hero shot of the pouch standing upright and centred on a warm oat-cream studio surface, premium organic marketplace feel, soft diffused daylight from the upper left, a single soft long shadow, shallow depth so the label stays razor-sharp while the warm-neutral background falls away, the entire frame in one warm cream-and-oat colour world with only market-green and warm-gold as accents, the label fully lit with zero shadow on the label face. Three hairline callout pointers touch the pouch, their labels set as bold sans-serif caps roughly 1.5x the footer text with tight letter-spacing so they read clearly at feed-thumbnail scale, pure text on thin hairline pointers with no chips, no boxes and no coloured blocks, together forming the second visual layer after the pack. Render exactly once: '02' as an oversized warm-gold editorial numeral in the upper-left negative space. Render exactly once: 'Quinoa' as a bold deep-green serif product name in the upper third. Render exactly once: 'the whole grain, nothing stripped out' as a quiet charcoal sans-serif line beneath the name. Render exactly once: 'CERTIFIED ORGANIC' as the first hairline callout label. Render exactly once: 'WHOLE GRAIN' as the second hairline callout label. Render exactly once: 'GLUTEN-FREE' as the third hairline callout label. Render exactly once: 'GRAIN' as a small warm-gold category tag in a top corner. Render exactly once: a row of seven small dots centred at the very bottom with the third dot filled market-green and the rest hollow. Render exactly once: 'Shop now on biomart.in' in small quiet charcoal sans-serif anchored bottom-right. No full stops anywhere in the text, no duplicate text zones, no repeated numerals, no repeated callouts, no repeated dot row, no repeated CTA, no coloured chip blocks, no SKU swap, no rustic props, no wooden bowls, no burlap or jute, no price callouts, no promotional badges. abundant marketplace editorial, Whole Foods store aesthetic, clean warm studio light, market green and warm gold color world, premium organic curation, trustworthy Indian marketplace. 4:5 aspect ratio.
```

---

## 🖼️ SLIDE 4 — PICK 03 · COLD-PRESSED SESAME OIL
**Output:** `research/prompts/assets/2026-10-11_biomart_what-organic-looks-like/slide4_sesame-oil.png`
**References (in order):** 1=SESAME

**PROMPT:**
```
Create a new image. Image 1 is the Pusht Organic Cold Pressed White Sesame Oil 1Ltr bottle — reference-only, reproduce with total pack fidelity. Ignore all other images in the conversation. Preserve on the pack: bottle silhouette, cap and seal geometry, base geometry, the label ground colour exactly as printed, the Pusht Organic wordmark and badge as printed, the illustration and any product photograph on the label, the full label with every line of printed copy including the cold-pressed and white sesame oil lines and all multilingual subtitles, the quality seal, the green vegetarian dot, and the full bottom certification row including every certification stamp and small-print element. Change nothing on the pack — no repositioned elements, no new or missing text, no colour shift, no logo redraw, no illustration redraw, no SKU substitution. Editorial hero shot of the bottle standing upright and centred on a warm oat-cream studio surface, premium organic marketplace feel, soft diffused daylight from the upper left, a single soft long shadow, shallow depth so the label stays razor-sharp while the warm-neutral background falls away, the entire frame in one warm cream-and-oat colour world with only market-green and warm-gold as accents, the label fully lit with zero shadow on the label face. Three hairline callout pointers touch the bottle, their labels set as bold sans-serif caps roughly 1.5x the footer text with tight letter-spacing so they read clearly at feed-thumbnail scale, pure text on thin hairline pointers with no chips, no boxes and no coloured blocks, together forming the second visual layer after the pack. Render exactly once: '03' as an oversized warm-gold editorial numeral in the upper-left negative space. Render exactly once: 'Cold-pressed sesame oil' as a bold deep-green serif product name in the upper third. Render exactly once: 'pressed, not refined and relabelled' as a quiet charcoal sans-serif line beneath the name. Render exactly once: 'COLD-PRESSED' as the first hairline callout label. Render exactly once: 'CERTIFIED ORGANIC' as the second hairline callout label. Render exactly once: 'CHEMICAL-FREE FARMING' as the third hairline callout label. Render exactly once: 'OIL' as a small warm-gold category tag in a top corner. Render exactly once: a row of seven small dots centred at the very bottom with the fourth dot filled market-green and the rest hollow. Render exactly once: 'Shop now on biomart.in' in small quiet charcoal sans-serif anchored bottom-right. No full stops anywhere in the text, no duplicate text zones, no repeated numerals, no repeated callouts, no repeated dot row, no repeated CTA, no coloured chip blocks, no SKU swap, no rustic props, no wooden bowls, no burlap or jute, no price callouts, no promotional badges. abundant marketplace editorial, Whole Foods store aesthetic, clean warm studio light, market green and warm gold color world, premium organic curation, trustworthy Indian marketplace. 4:5 aspect ratio.
```

---

## 🖼️ SLIDE 5 — PICK 04 · RAW FOREST HONEY
**Output:** `research/prompts/assets/2026-10-11_biomart_what-organic-looks-like/slide5_honey.png`
**References (in order):** 1=HONEY

**PROMPT:**
```
Create a new image. Image 1 is the Organic Rozana Honey 500G jar — reference-only, reproduce with total pack fidelity. Ignore all other images in the conversation. Preserve on the pack: jar and lid silhouette, seal and base geometry, the label ground colour exactly as printed, the Rozana and Health Fields wordmarks and badges as printed, any illustration and product photograph on the label, the full label with every line of printed copy including the raw honey lines and all multilingual subtitles, the quality seal, the green vegetarian dot, and the full bottom certification row including every certification stamp and small-print element. Change nothing on the pack — no repositioned elements, no new or missing text, no colour shift, no logo redraw, no illustration redraw, no SKU substitution. Editorial hero shot of the honey jar standing upright and centred on a warm oat-cream studio surface, premium organic marketplace feel, soft diffused daylight from the upper left, a single soft long shadow, shallow depth so the label stays razor-sharp while the warm-neutral background falls away, the entire frame in one warm cream-and-oat colour world with only market-green and warm-gold as accents, the label fully lit with zero shadow on the label face. Three hairline callout pointers touch the jar, their labels set as bold sans-serif caps roughly 1.5x the footer text with tight letter-spacing so they read clearly at feed-thumbnail scale, pure text on thin hairline pointers with no chips, no boxes and no coloured blocks, together forming the second visual layer after the pack. Render exactly once: '04' as an oversized warm-gold editorial numeral in the upper-left negative space. Render exactly once: 'Raw forest honey' as a bold deep-green serif product name in the upper third. Render exactly once: 'honey the way the hive made it' as a quiet charcoal sans-serif line beneath the name. Render exactly once: 'RAW' as the first hairline callout label. Render exactly once: 'UNFILTERED' as the second hairline callout label. Render exactly once: 'NO HEAT TREATMENT' as the third hairline callout label. Render exactly once: 'HONEY' as a small warm-gold category tag in a top corner. Render exactly once: a row of seven small dots centred at the very bottom with the fifth dot filled market-green and the rest hollow. Render exactly once: 'Shop now on biomart.in' in small quiet charcoal sans-serif anchored bottom-right. No full stops anywhere in the text, no duplicate text zones, no repeated numerals, no repeated callouts, no repeated dot row, no repeated CTA, no coloured chip blocks, no SKU swap, no rustic props, no wooden bowls, no burlap or jute, no price callouts, no promotional badges. abundant marketplace editorial, Whole Foods store aesthetic, clean warm studio light, market green and warm gold color world, premium organic curation, trustworthy Indian marketplace. 4:5 aspect ratio.
```

---

## 🖼️ SLIDE 6 — PICK 05 · AMARANTH FLOUR
**Output:** `research/prompts/assets/2026-10-11_biomart_what-organic-looks-like/slide6_amaranth-flour.png`
**References (in order):** 1=AMARANTH

**PROMPT:**
```
Create a new image. Image 1 is the Health Fields Organic Amaranth Flour (Rajgira Atta) 500g pouch — reference-only, reproduce with total pack fidelity. Ignore all other images in the conversation. Preserve on the pack: pouch silhouette, top seal and base geometry, the pack ground colour exactly as printed, the Health Fields wordmark and badge as printed, the amaranth illustration and any product photograph on the label, the full label with every line of printed copy including the amaranth flour and rajgira atta lines and all multilingual subtitles, the quality seal, the green vegetarian dot, and the full bottom certification row including every certification stamp and small-print element. Change nothing on the pack — no repositioned elements, no new or missing text, no colour shift, no logo redraw, no illustration redraw, no SKU substitution. Editorial hero shot of the pouch standing upright and centred on a warm oat-cream studio surface, premium organic marketplace feel, soft diffused daylight from the upper left, a single soft long shadow, shallow depth so the label stays razor-sharp while the warm-neutral background falls away, the entire frame in one warm cream-and-oat colour world with only market-green and warm-gold as accents, the label fully lit with zero shadow on the label face. Three hairline callout pointers touch the pouch, their labels set as bold sans-serif caps roughly 1.5x the footer text with tight letter-spacing so they read clearly at feed-thumbnail scale, pure text on thin hairline pointers with no chips, no boxes and no coloured blocks, together forming the second visual layer after the pack. Render exactly once: '05' as an oversized warm-gold editorial numeral in the upper-left negative space. Render exactly once: 'Amaranth flour' as a bold deep-green serif product name in the upper third. Render exactly once: 'rajgira atta, nothing added' as a quiet charcoal sans-serif line beneath the name. Render exactly once: 'STONE-GROUND' as the first hairline callout label. Render exactly once: 'CERTIFIED ORGANIC' as the second hairline callout label. Render exactly once: 'GLUTEN-FREE' as the third hairline callout label. Render exactly once: 'FLOUR' as a small warm-gold category tag in a top corner. Render exactly once: a row of seven small dots centred at the very bottom with the sixth dot filled market-green and the rest hollow. Render exactly once: 'Shop now on biomart.in' in small quiet charcoal sans-serif anchored bottom-right. No full stops anywhere in the text, no duplicate text zones, no repeated numerals, no repeated callouts, no repeated dot row, no repeated CTA, no coloured chip blocks, no SKU swap, no rustic props, no wooden bowls, no burlap or jute, no price callouts, no promotional badges. abundant marketplace editorial, Whole Foods store aesthetic, clean warm studio light, market green and warm gold color world, premium organic curation, trustworthy Indian marketplace. 4:5 aspect ratio.
```

---

## 🖼️ SLIDE 7 — CTA
**Output:** `research/prompts/assets/2026-10-11_biomart_what-organic-looks-like/slide7_cta.png`
**References (in order):** 1=PUMPKIN · 2=QUINOA · 3=SESAME · 4=HONEY · 5=AMARANTH

**PROMPT:**
```
Create a new image. Images 1 to 5 are the five Biomart packs — the HealthFields raw pumpkin seeds pouch, the Pusht quinoa millet pouch, the Pusht cold-pressed white sesame oil bottle, the Organic Rozana honey jar, and the HealthFields amaranth flour pouch, in that attachment order; all reference-only, reproduce each with total pack fidelity. Ignore every other image in the conversation. Preserve on every pack: its silhouette, cap seal and base geometry, ground colour exactly as printed, the brand wordmark and badge as printed, every illustration and product photograph on the pack, the full label with every line of printed copy and all multilingual subtitles, the quality seal, the green vegetarian dot, and the entire bottom certification row including every certification stamp and small-print element. Change nothing on any pack — no repositioned elements, no new or missing text, no colour shift, no logo redraw, no SKU substitution. Editorial shot of the five packs grouped together as a tight clean cluster on a warm oat-cream surface, premium marketplace calm, soft diffused daylight from the upper left, one warm cream-and-oat colour world with only market-green and warm-gold as accents, every label fully lit with zero shadow on the label faces, generous negative space in the upper half for the closing headline. Render exactly once: 'QUALITY YOU CAN POINT TO' as a bold deep market-green editorial serif headline in the upper half. Render exactly once: 'every claim is on the pack, not just the front' as a quiet warm-gold sans-serif line beneath the headline. Render exactly once: 'Shop now on biomart.in' as a calm charcoal sans-serif line slightly larger than a footer, centred in the lower third. Render exactly once: a row of seven small dots centred at the very bottom with the seventh dot filled market-green and the rest hollow. No full stops anywhere in the text, no duplicate text zones, no repeated headline, no repeated CTA, no repeated dot row, no SKU swap on any pack, no rustic props, no wooden bowls, no burlap or jute, no price callouts, no promotional badges, no link-in-bio or swipe wording. abundant marketplace editorial, Whole Foods store aesthetic, clean warm studio light, market green and warm gold color world, premium organic curation, trustworthy Indian marketplace. 4:5 aspect ratio.
```

---

## ▶️ APPENDIX — DIRECT CODEX CLI COMMANDS (optional, one per slide)

If running the Codex CLI manually instead of handing it this file: save each slide's PROMPT block to its own `.txt` file, then run (Windows / Git Bash):

```bash
BIN="C:/Users/arpit/AppData/Local/OpenAI/Codex/bin/c6fe824d725f02d7/codex.exe"
OUT="research/prompts/assets/2026-10-11_biomart_what-organic-looks-like"
mkdir -p "$OUT/refs"

# Example — Slide 2 (single-pack). Repeat per slide, swapping prompt file, refs, and output name.
"$BIN" exec --dangerously-bypass-approvals-and-sandbox \
  "Generate a single image using your native image generation tool with model gpt-image-2.5-sunburst. The full image prompt is in this file: $OUT/prompts/slide2.txt — read it and pass it verbatim to your image tool. Use the product pack photo as a visual reference: Image 1 = $OUT/refs/pumpkin.jpg. Aspect ratio 4:5 vertical, quality xhigh. Save the generated PNG to: $OUT/slide2_pumpkin-seeds.png. Do not modify or summarize the prompt, do not swap the model, do not write any code, do not reorder or drop reference images, just call your image tool once." \
  2>&1 | tail -30
```

Reference-order reminder for the multi-pack slides (1 and 7): `Image 1 = pumpkin, Image 2 = quinoa, Image 3 = sesame, Image 4 = honey, Image 5 = amaranth`.

Binary note: if that path 404s after a Codex desktop update, re-derive it from `CODEX_CLI_PATH` in `~/.codex/config.toml`. Do NOT use the old sandbox binary at `~/.codex/.sandbox-bin/codex.exe`.

---

## ✅ AFTER GENERATION
Expected files in `research/prompts/assets/2026-10-11_biomart_what-organic-looks-like/`:
`slide1_cover.png · slide2_pumpkin-seeds.png · slide3_quinoa.png · slide4_sesame-oil.png · slide5_honey.png · slide6_amaranth-flour.png · slide7_cta.png`

Check each: label fidelity (no SKU swap), all three callouts legible at thumbnail scale, correct pagination dot filled, baked "Shop now on biomart.in" present, no full stops in any text, one warm cream-and-oat colour world across all seven.

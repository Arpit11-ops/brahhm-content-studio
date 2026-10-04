# FIRE — Biomart Pantry Sack Hero (2026-10-04)

Desktop Claude: this is a self-contained render brief. Follow the steps below in order. Do not re-derive the prompt, do not re-write the caption, do not ask Puran for the pack filenames — find them yourself. One turn, one PNG delivered via `SendUserFile`.

**Skill:** `codex-image-gen` (SKILL.md at `./skills/codex-image-gen/SKILL.md`) — read it if any step below is ambiguous.

**Protocol gates already cleared on 2026-10-04 cloud session:**
- Protocol 2 (product descriptions) — ✅ pulled from `research/catalogs/biomart_catalog.json`
- Protocol 3 (claims audit) — ✅ no health claims, prices verified against catalog
- Protocol 6 (text table confirmation) — ✅ pre-locked by Puran in cloud session
- Protocol 7 (reverse engineer) — ✅ T91 assigned, Homfert reference adapted

---

## STEP 1 — Find the 5 pack reference photos

Pack root on this laptop: `C:\Users\arpit\Documents\storage\arpan organic\`

Find the front-of-pack photo for each SKU below. Use `Glob` on the brand subfolder. If multiple matches, prefer the one with "front" / "hero" / "1.jpg" / "1.png" in the name. If no obvious front shot, pick the largest file.

| # | SKU | Brand folder | Glob hints (any match works) |
|---|---|---|---|
| 1 | Health Fields Raw Cashew Nut 250g | `health fields\` | `*cashew*`, `*raw*cashew*`, `*250*cashew*` |
| 2 | Pusht Jaggery Powder 500g | `pusht\` | `*jaggery*`, `*gur*powder*`, `*jaggery*powder*` |
| 3 | Pusht White Basmati Rice 1kg | `pusht\` | `*white*basmati*`, `*basmati*1kg*`, `*rice*1kg*` |
| 4 | Greendipz Schezwan Sauce 240g | `greendipz\` | `*schezwan*`, `*sichuan*`, `*schez*sauce*` |
| 5 | Caveman Millet Era Cookies 2×60g | `caveman\` | `*millet*era*`, `*era*cookies*`, `*milleera*` |

If any pack is missing, STOP and tell Puran which one — do not substitute a different SKU.

Confirm absolute paths for all five before continuing. Order matters — the preservation clause and the exec call both assume Image 1 = cashew, Image 2 = jaggery, Image 3 = basmati, Image 4 = Schezwan, Image 5 = Millet Era cookies.

---

## STEP 2 — Write the prompt file

Write the prompt below verbatim to `research/prompts/assets/2026-10-04_biomart_pantry-sack/prompt.txt` using the `Write` tool (not Bash heredoc — UTF-8 encoding matters for the em-dashes and curly quotes).

### Prompt (verbatim — do not edit, do not condense, do not re-flow)

```
Create a new image. Image 1 is the Health Fields Organic Raw Cashew Nut 250g pouch; Image 2 is the Pusht Organic Jaggery Powder 500g pouch; Image 3 is the Pusht Organic White Basmati Rice 1kg pouch; Image 4 is the Greendipz Schezwan Sauce 240g jar; Image 5 is the Caveman Millet Era Cookies 2x60g pack — all five are reference-only, reproduce with total pack fidelity. Ignore every other image in the conversation. Preserve on each pack: silhouette and geometry, every brand wordmark and badge exactly as printed, every illustration and product photograph on the pack face, every line of printed copy on the label including product name, net weight, variant description, multilingual subtitles, nutritional callouts, and every certification stamp in the bottom row — Jaivik Bharat, India Organic, FSSAI, USDA Organic where printed, green vegetarian dot, quality seal, tear-strip and resealable-zip strip where present, and all small-print. Change nothing on any pack — no repositioned elements, no new text, no missing text, no colour shift, no logo redraw, no illustration redraw, no SKU substitution across the five.

Editorial hero shot of a jute burlap sack sitting centred in the lower two-thirds of a 1:1 square frame, folded open at the top, five Biomart pantry packs mounded inside the sack as a platform — the Health Fields Raw Cashew Nut pouch standing dead-centre as the visual anchor and the tallest element with its label face reading flat to camera, the Pusht Jaggery Powder pouch rising just behind and slightly left of the cashew pack, the Pusht White Basmati Rice 1kg pouch standing upright behind and slightly right of the cashew pack, the Greendipz Schezwan Sauce jar seated at the front-left lip of the sack with its label face reading flat to camera, the Caveman Millet Era Cookies pack leaning diagonally at the front-right lip of the sack with its hero face reading flat to camera. The pack labels are flat, legible, fully lit, zero shadow across the label faces. The sack's burlap weave is sharp and tactile in the foreground, slightly softer at the back where it meets the field.

The sack sits on soft brown farm earth with a few blades of pale green grass at the base. Behind the sack a lush organic farmland stretches to a distant horizon — soft rows of green crop beds receding into warm bokeh, a single golden sun flare blooming at the upper-right corner, warm atmospheric haze rolling across the mid-ground, scattered dark green trees along the far horizon. The light is Kodak Portra 400 golden hour, backlit from the upper right, warm cream and honey-green temperature washing the entire frame, a soft golden rim glow outlining the sack rim and the pack silhouettes, Portra 400 film grain throughout, cinematic shallow depth of field with the sack and packs tack-sharp and the field falling into creamy bokeh.

Render exactly once: 'biomart' in white lowercase rounded sans on a Market Green rounded-rectangle badge in the top-left corner, inset roughly 5 percent from the top and left edges, with the small cream tagline 'truly organic' sitting tight under the wordmark inside the badge. Render exactly once: 'www.biomart.in' in a small quiet dark-charcoal light sans in the top-right corner, inset roughly 5 percent from the top and right edges. Render exactly once: 'Biomart — your pantry' on line 1 as a centred bold editorial serif in the upper third of the frame, with 'Biomart —' in Market Green and 'your pantry' in deep charcoal. Render exactly once: 'curated by farmers' on line 2 directly beneath line 1, same bold editorial serif, with 'curated by' in deep charcoal and 'farmers' in Market Green for the weight shift. Render exactly once: 'Shop now on biomart.in' in a small-caps warm cream white quiet sans, centred inside a softly darkened full-width thin band running across the bottom of the frame. No full stops anywhere, no exclamation marks, no bullets, no additional text, no price callouts anywhere in the image, no discount codes, no offer language, no logo redraws on any pack, no SKU swap, no vegetables of any kind inside the sack, no onions, no tomatoes, no broccoli, no herbs, no carrots, no greens, no loose cashews, no loose rice grains, no loose jaggery lumps, no spilled sauce, only the five named packs inside the sack; no duplicate text zones, no repeated headlines, no repeated badge, no repeated URL, no repeated CTA strip, no scattered flat ingredient layouts, no solid colored chip blocks, no rustic wooden bowls, no mortar and pestle, no burlap outside the sack itself, no model, no hand entering frame, no additional props beyond the sack and the five packs and the field.

Close in abundant marketplace editorial style — Whole Foods store aesthetic, clean warm studio light softened into golden hour, market green and warm gold color world, premium organic curation, trustworthy Indian marketplace. 1:1 square aspect ratio.
```

---

## STEP 3 — Create output folder

```bash
mkdir -p "research/prompts/assets/2026-10-04_biomart_pantry-sack"
```

(Already present from this FIRE.md's own folder — just confirm.)

---

## STEP 4 — Fire Codex

Model: **`gpt-image-2.5-sunburst`** (multi-pack composition, fidelity-critical).
Quality: **`max`** (5-pack hero, 5 text zones, label distortion is fatal).
Aspect ratio: **1:1 square**.

Substitute `<PACK_N>` with the absolute paths found in Step 1. Keep attachment order Image 1 → Image 5 as listed.

```bash
"C:/Users/arpit/AppData/Local/OpenAI/Codex/bin/c6fe824d725f02d7/codex.exe" exec \
  --dangerously-bypass-approvals-and-sandbox \
  "Generate a single image using your native image generation tool with model gpt-image-2.5-sunburst. The full image prompt is in this file: research/prompts/assets/2026-10-04_biomart_pantry-sack/prompt.txt — read it and pass it verbatim to your image tool. Use the product pack photos at these paths as visual references in the exact order given: Image 1 = <PACK_1_CASHEW_PATH>, Image 2 = <PACK_2_JAGGERY_PATH>, Image 3 = <PACK_3_BASMATI_PATH>, Image 4 = <PACK_4_SCHEZWAN_PATH>, Image 5 = <PACK_5_MILLET_ERA_COOKIES_PATH>. Aspect ratio 1:1 square, quality max. Save the generated PNG to: research/prompts/assets/2026-10-04_biomart_pantry-sack/hero.png. Do not modify the prompt text, do not summarize it, do not swap the model, do not downgrade quality from max, do not write any Python code, do not call the OpenAI API directly, do not reorder or drop reference images, just call your image generation tool once with the exact prompt and the five reference images in the given order." \
  2>&1 | tail -40
```

Wrap in a single Bash tool call with `timeout: 420000`.

If the live-binary path has changed on a Codex desktop update, re-derive it from `CODEX_CLI_PATH` in `~/.codex/config.toml`.

---

## STEP 5 — Verify

```bash
ls -la "research/prompts/assets/2026-10-04_biomart_pantry-sack/"
```

Expected: `prompt.txt` + `hero.png` (PNG size usually 1.5–4 MB for a `max` 1:1 render).

If `hero.png` is missing but the Codex log mentions `.codex/generated_images/<uuid>/call_*.png`, copy manually:

```bash
cp "/c/Users/arpit/.codex/generated_images/<uuid>/call_*.png" \
   "research/prompts/assets/2026-10-04_biomart_pantry-sack/hero.png"
```

---

## STEP 6 — Deliver

```
SendUserFile({
  files: ["research/prompts/assets/2026-10-04_biomart_pantry-sack/hero.png"],
  caption: "Biomart 2026-10-04 · T91 Golden Field Jute Sack Hero — check: all 5 pack labels tack-sharp and SKU-correct (no swap on cashew / jaggery / basmati / Schezwan / Millet Era), two-tone headline reads 'Biomart — your pantry / curated by farmers' with no stray full stops, baked CTA band 'Shop now on biomart.in' present at bottom, sack mounded not scattered, no vegetables sneaked in",
  status: "proactive",
  display: "render"
})
```

---

## STEP 7 — If Puran flags a fix

Default to a **surgical single-change edit** on `hero.png`, not a full regen. See `./skills/codex-image-gen/SKILL.md` → Section 5. Save edited output to `hero_v2.png` (then `v3`, `v4`) in the same folder. Keep every version on disk — Puran compares.

---

## Caption + variation (for Puran's convenience when the image lands)

**Caption:**

```
One jute sack. Four brands we actually stock the pantry with.

Health Fields raw cashews at ₹500 go into the chikki and the curd rice. Pusht jaggery powder at ₹97 does the chai and the kheer. The Pusht white basmati at ₹299 handles biryani Sundays. Greendipz Schezwan at ₹250 is the Friday noodle rescue. And Caveman Millet Era cookies at ₹124 disappear before the tin hits the shelf.

Nothing synthetic. No long shipping manifest. Just the shelf you'd build if someone handed you a Saturday.

Full basket ₹1,270. Order on biomart.in.
```

```
#Biomart #OrganicMegastore #PantryEssentials
```

**Variation:**

```
The grocery list that doesn't need defending.

Everything in this sack comes from one of four kitchens we actually visit — a cashew sorting floor in Panruti, a khandsari jaggery mill, a basmati farm in the Doon valley, and a sauce kitchen that still measures chillies by the handful. One basket, one tracking link.

Cashews ₹500, jaggery ₹97, basmati ₹299, Schezwan ₹250, cookies ₹124. Full basket ₹1,270.

Shop the whole basket on biomart.in.
```

```
#Biomart #TrulyOrganic #IndianOrganic
```

---

## Basket reference

| # | Product | Price | URL |
|---|---|---|---|
| 1 | Health Fields Organic Raw Cashew Nut 250g | ₹500 | biomart.in/products/health-fields-organic-raw-cashew-nut-250-gm |
| 2 | Pusht Organic Jaggery Powder 500g | ₹97 | biomart.in/products/pusht-organic-jaggery-powder-500gm |
| 3 | Pusht Organic White Basmati Rice 1kg | ₹299 | biomart.in/products/pusht-organic-white-basmati-rice |
| 4 | Greendipz Schezwan Sauce 240g | ₹250 | biomart.in/products/greendipz-schezwan-sauce |
| 5 | Caveman Organic Millet Era Cookies 2×60g | ₹124 | biomart.in/products/caveman-organic-millet-era-cookies |

**Basket total: ₹1,270**

VEE template logged: **T91 — Golden Field Jute Sack Hero** (Biomart marketplace curation, reverse-engineered from Homfert "Nature's Formula" reference, 2026-10-04).

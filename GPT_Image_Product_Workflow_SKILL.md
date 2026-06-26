# GPT Image 2.0 — Product Image Workflow (Shareable Skill)

A self-contained workflow for generating accurate, listing-ready product images in GPT Image 2.0 without hallucination. Built for e-commerce sellers (Shopify, Amazon, Etsy, D2C sites) shooting products with fixed physical shape — extension cords, boxes, bottles, electronics, tools, packaged goods.

If your prompts keep producing the *wrong* product — extra outlets, wrong cable count, reshaped boxes, invented branding, mutated bottles — this skill fixes it.

---

## CORE PHILOSOPHY

GPT Image 2.0 responds to **creative direction language**, not technical specs. But for the **product itself**, you flip the script and use **reproduction language**. Creative direction reinterprets. Reproduction copies. Listing images need copying.

Three non-negotiables for every prompt:

1. **Upload the real product photo** — text alone never reproduces a specific SKU
2. **Lock the product shape first** before scene, lighting, or styling
3. **Lean prompts beat long prompts** — GPT drops instructions past ~15 fields

---

## PRE-FLIGHT CHECKLIST (Before Writing Any Prompt)

- [ ] Real product photo uploaded as reference image
- [ ] You can name the exact: shape, colour, outlet/component count, branding text, plug/cap/closure type
- [ ] You know the final aspect ratio (1:1 main listing, 4:5 lifestyle, 16:9 banner)
- [ ] You know which text will be baked into the image vs added in Canva later
- [ ] You have a list of competitor or aspirational listing aesthetics to anchor mood (e.g. "Apple white cyclorama," "Aesop natural surfaces," "Anker tech editorial")

If any of these are missing, stop and gather them. Prompting on incomplete inputs wastes generations.

---

## MASTER PROMPT STRUCTURE

Every prompt must follow this exact order. Skipping or reordering breaks results.

```
LINE 1:        [Format/ratio] + [Output type] + [Real-world aesthetic reference]
PRODUCT SHAPE HARD CONSTRAINT: [Reproduction lockdown — see next section]
THEME:         Emotional anchor in 3–5 words — governs the whole image
MOOD:          [X meets Y] — two real-world aesthetic anchors as a hybrid
SCENE/SETUP:   Real surface + atmosphere as named elements
PRODUCT PLACEMENT: Spatial position + relative scale + camera angle
LIGHTING:      Real-world reference (studio softbox / golden hour / Portra 400 / ARRI key light)
NEGATIVE SPACE: Where text/badges will sit later — spatial language, never coordinates
TYPOGRAPHY:    Only if baking text in — style + position relative to layout zones
COLOR WORLD:   The single palette family every element lives within
EXCLUSIONS:    Explicit negative list — what must NEVER appear
QUALITY:       8K, ultra detailed, photorealistic, sharp focus, no watermark, no clutter
FORMAT:        [Ratio] — GPT Image 2.0
```

Keep total length around 120–180 words. Above ~250 words, GPT starts dropping fields.

---

## THE PRODUCT SHAPE HARD CONSTRAINT BLOCK

This is the single highest-leverage fix for hallucination. For any product with a fixed physical identity, this block sits at the **top of the prompt** — before scene, mood, or lighting.

Use **reproduction language** here, not creative direction. Tell GPT to copy, not interpret.

**Template:**

```
PRODUCT SHAPE HARD CONSTRAINT (DO NOT DEVIATE):
- Reproduce the uploaded [product type] EXACTLY as shown in reference image
- Body shape: [exact geometry — long horizontal rectangle / upright cylinder / square box]
- Body proportions: [ratio language — width 3x height, etc.] — never reshape
- Body colour: [exact colour from reference, named]
- Component count: [N outlets / N buttons / N caps] — no more, no less
- Cable/strap/handle: [colour, exit point, length ratio to body]
- Plug/cap/closure: [type — reproduce shape, prongs, threads exactly]
- Switch/button positions: [where they sit on the real product]
- Branding text on body: reproduce exactly as shown — do not invent new text
- Logo: reproduce position and size — do not relocate or resize
```

**Example for an extension cord:**

```
PRODUCT SHAPE HARD CONSTRAINT (DO NOT DEVIATE):
- Reproduce the uploaded extension cord EXACTLY as shown
- Body: long horizontal rectangle — width approximately 5x height
- 4 universal outlets in a single horizontal row, evenly spaced
- One black cable exiting from right end, length ratio 2x the body
- 3-pin Indian plug at cable end — reproduce shape and prong proportions exactly
- Master switch on far left of body
- Body colour: white matte plastic with grey accents
- Branding "BrandName" in black sans-serif on top face, centred
- Do not reshape body into square, cube, or vertical orientation
```

**Example for a bottle:**

```
PRODUCT SHAPE HARD CONSTRAINT (DO NOT DEVIATE):
- Reproduce the uploaded bottle EXACTLY as shown
- Upright cylindrical glass bottle — no tilt, no rotation
- Body proportions: height 4x diameter
- Amber glass colour — reproduce exact tint
- Black screw cap at top — reproduce thread visibility and cap height
- Label: reproduce all text, layout, and graphics exactly as shown
- Do not reshape bottle, do not change cap style, do not relocate label
```

---

## REPRODUCTION LANGUAGE vs CREATIVE DIRECTION

| Context | Use This Type |
|---------|---------------|
| The product itself | **Reproduction** — "reproduce exactly," "same shape," "do not deviate" |
| Scene around product | **Creative direction** — "warm marble surface," "soft morning light" |
| Lighting | **Creative direction** — real-world references like "Portra 400" |
| Atmosphere | **Creative direction** — "dreamy cloud diffusion," "studio cyclorama" |
| Branding/text on product | **Reproduction** — "exactly as shown in reference" |
| Background colours | **Creative direction** — descriptive atmospheric language |

The mistake most people make: they write the *product* in creative language ("a sleek, premium extension cord with elegant proportions") and GPT reinterprets every word. Lock the product. Style the world.

---

## COLOR WORLD RULE

Every image must maintain **monochromatic immersion**. Background, atmosphere, props, and any overlays must live within the same colour family. Only the product (when its real colour differs) and typography may break the palette.

Wrong: white background + product + bright red callout box + blue badge
Right: warm cream background + warm cream atmosphere + product + cream-toned semi-transparent overlays + one accent colour for headline

**Feature chips / overlay panels rule:** Never use solid coloured blocks. Always describe as "dark semi-transparent overlay so background colour bleeds through." Solid blocks kill atmospheric depth.

---

## LIGHTING — USE REAL-WORLD REFERENCES

| Avoid | Use Instead |
|-------|-------------|
| "Warm lighting" | "Kodak Portra 400 warmth" / "golden hour 5pm" |
| "Studio lighting" | "Profoto softbox key light from upper left, fill from right" |
| "Nice highlights" | "ARRI quality cinematic key light" |
| "Cool tones" | "Overcast daylight diffused through north-facing window" |
| "Dramatic" | "Single hard rim light from behind, deep shadow front" |

Real-world references trigger learned associations in GPT. Vague adjectives don't.

---

## SPATIAL LANGUAGE — NEVER COORDINATES

GPT Image 2.0 ignores pixel coordinates, X/Y values, and percentages. Use spatial language instead.

| Avoid | Use Instead |
|-------|-------------|
| "Text at x=200 y=400" | "Headline in upper-left third" |
| "Logo at 80% width" | "Logo bottom-right corner with breathing room" |
| "Product centred at 50%" | "Product centre-dominant, slight bias toward foreground" |
| "Negative space 30% top" | "Keep clean negative space across upper third for text overlay" |

---

## NO DOTS RULE

Never put full stops at the end of headlines, badges, callouts, or any in-image text. Dots break listing-image aesthetic. State this explicitly in the prompt if baking text in.

---

## EXCLUSIONS — ALWAYS EXPLICIT

GPT obeys negatives well when they're spelled out. Always include an EXCLUSIONS block listing common hallucinations for your product category.

**Generic e-commerce exclusions:**
```
EXCLUSIONS:
- No invented brand names, model numbers, or barcodes
- No fake certification logos
- No watermarks, no stock photo tags
- No extra components beyond what reference shows
- No reshaping of product geometry
- No damage cues, scratches, frayed wires, dents
- No multiple copies of the product unless requested
- No human hands or models unless requested
- No floor clutter, no background objects competing with product
```

Add product-specific exclusions on top of these.

---

## IN-IMAGE TEXT CONFIRMATION GATE

Before generating, list every piece of text going inside the image in a table:

| Element | Text | Style | Position |
|---------|------|-------|----------|
| Headline | [exact text] | [bold/serif/etc] | [zone] |
| Subhead | [exact text] | [style] | [zone] |
| Badge | [exact text] | [style] | [zone] |

Confirm with yourself or your client. Only then bake it into the prompt. Half of GPT regenerations happen because text was wrong.

---

## PROMPT LENGTH GUARDRAIL

Tested rule: ~120-word prompts beat ~300-word prompts on element completeness. GPT silently drops fields past ~15 distinct instructions.

If your prompt exceeds 200 words:
1. Cut adjectives — "beautiful elegant premium" → "premium"
2. Merge fields — combine MOOD and SCENE if redundant
3. Drop fields you'll fix in Canva (logo placement, certifications)
4. Keep the constraint block intact — cut elsewhere

---

## OUTPUT FORMAT

Always output the final prompt in a code block, paste-ready:

```
TEMPLATE: [Optional name]
GPT IMAGE 2.0 PROMPT:
[Full structured prompt — paste-ready]
```

Never mention Canva, logo placement, or post-production inside the prompt. Those happen after.

---

## REVERSE ENGINEER MODE

When you have a reference design image (competitor listing, Pinterest find, aspirational layout) and want GPT to produce something in that style — activate full visual analysis. This mode reverse-engineers any design into a clean GPT Image 2.0 prompt using creative direction language.

### STEP 0 — COMPOSITING DETECTION (Run First)

Before any analysis, identify the design mode of your reference:

- **Fully AI-generated:** Single prompt created the whole image
  → Reverse engineer into one creative brief prompt
- **Composited design:** Real photography + design software overlays (Photoshop, Canva, Figma text)
  → Note which elements need separate generation vs Canva overlay
  → Flag: "This reference is composited — workflow splits between GPT and Canva"

If composited: identify the *base photo* and reverse-engineer only that. Treat all text, badges, overlays as Canva work done after.

### 7-LAYER ANALYSIS

Run all seven layers on the reference image in order.

**LAYER 1 — STRUCTURAL ARCHITECTURE**
Canvas ratio. Panel count (single image / tri-panel / split-screen). Z-layer order (what sits in front of what). Composition type (hero product / editorial / lookbook / lifestyle / flat-lay).

**LAYER 2 — PRODUCT PLACEMENT**
Quadrant position. Relative scale (product fills 30%? 60%? 80% of frame?). Tilt angle (upright / 3/4 view / top-down / extreme angle). What the product is sitting on, emerging from, or floating above.

**LAYER 3 — BACKGROUND TREATMENT**
Colour world. Atmospheric quality (gradient / clouds / rays / solid / textured surface). Describe in language, not hex. Identify the monochrome immersion rule — what single colour family governs everything.

**LAYER 4 — TYPOGRAPHY SYSTEM**
Each text element: style (serif / sans / display / handwritten) + size hierarchy + position relative to layout zones. Identify size drama — which line dominates, by what multiple. Note if text is overlapping product or kept in negative space.

**LAYER 5 — LIGHTING & COLOUR**
Real-world lighting reference (golden hour / ARRI / studio diffused / Portra 400 / harsh midday / overcast). Colour temperature (warm / neutral / cool). What the light is doing to product surfaces — describe material behaviour, not hex codes (glossy reflection, matte absorption, transparent refraction).

**LAYER 6 — PROP / INGREDIENT / ATMOSPHERIC ELEMENTS**
Props in frame and their symbolic role. Any liquid or atmospheric flourish: is it one sweeping ribbon arc or scattered explosion? Ingredient/prop bed: flat scatter or mounded platform? Floating elements: depth variation across foreground / midground / background?

**LAYER 7 — CHIP / BADGE / UI ELEMENTS**
Are chips solid coloured blocks or dark semi-transparent overlays? Badge style. Footer treatment. Authenticity signals (barcode, URL, certification marks, FSSAI/USDA logos, model numbers).

### PROMPT TRANSLATION LAYER (Mandatory After Analysis)

After the 7 layers, translate findings into a creative brief, not a spec sheet:

1. Identify the real-world aesthetic anchor — "X meets Y" formula
2. Write the emotional theme line in 3–5 words
3. Describe atmosphere as named ingredients — never as gradient specs
4. Describe any liquid as a sweeping ribbon direction — never as scattered explosion
5. Describe chip/UI elements as semi-transparent overlays — never solid blocks
6. State the colour world immersion rule explicitly
7. Write all text placement relative to layout zones — never coordinates
8. Build an exclusion list based on what the reference does NOT have (no human, no floor clutter, no second product, etc.)

### REVERSE ENGINEER OUTPUT

Deliver in this order:

1. Full 7-layer analysis report (bullet form is fine)
2. STEP 0 result — fully AI vs composited
3. In-image text confirmation table — wait for approval before locking prompt
4. Final GPT Image 2.0 prompt in code block — creative brief format

---

## COMMON FAILURE MODES + FIXES

| Symptom | Root Cause | Fix |
|---------|-----------|-----|
| GPT invents extra outlets / buttons / components | Missing hard constraint block | Add component count explicitly with "no more, no less" |
| Product reshapes (box → cube, cord → square) | Creative language on product | Switch to reproduction language; add proportions ratio |
| Bottle/jar deforms in pour shots | Bottle and stream described as one | Separate bottle and stream into two instructions; add "visible gap between bottle mouth and liquid surface"; add rigidity lock — "bottle remains perfectly rigid, no warping" |
| Wrong branding text appears | Logo described creatively | Use "reproduce exactly as shown in reference, do not invent new text" |
| Fake certifications appear | No exclusion listed | Add "no fake certification logos" to EXCLUSIONS |
| Colours drift from reference | Hex codes used | Switch to descriptive language + named colour from reference |
| Wrong atmosphere / cluttered scene | Too many fields in prompt | Cut prompt below 180 words; merge redundant fields |
| Text positions wrong | Coordinates used | Switch to spatial language: "upper-left third," "centred at bottom" |
| Multiple products appear | No exclusion on quantity | Add "single product only, no duplicates, no multiple copies" |
| Models/hands appear unwanted | No exclusion | Add "no humans, no hands, product only" |

---

## QUICK-START TEMPLATE

Copy this, fill the blanks, and you have a working prompt:

```
1:1 square product listing image for [marketplace], premium [aesthetic anchor — e.g. Apple white cyclorama] style

PRODUCT SHAPE HARD CONSTRAINT (DO NOT DEVIATE):
- Reproduce the uploaded [product] EXACTLY as shown in reference
- Body: [shape, proportions]
- Colour: [exact colour]
- Components: [count + layout]
- Branding: reproduce exactly as shown
- Do not reshape, do not relocate elements

THEME: [3–5 word emotional anchor]
MOOD: [aesthetic A] meets [aesthetic B]
SCENE: Product on [surface], [atmosphere description]
PLACEMENT: [Quadrant], [scale], [camera angle]
LIGHTING: [Real-world reference]
NEGATIVE SPACE: Keep clean [zone] for text overlay
COLOR WORLD: Every element lives within [palette family]

EXCLUSIONS:
- No invented branding or text
- No fake certifications
- No watermarks or stock tags
- No extra components beyond reference
- No reshaping of product geometry
- No humans, no hands
- No background clutter
- No multiple copies of product

QUALITY: 8K, ultra detailed, photorealistic, sharp focus, no watermark, no clutter
FORMAT: 1:1 — GPT Image 2.0
```

---

## REMEMBER

- Upload the real product photo every time
- Constraint block first, scene second
- Reproduction language for product, creative direction for everything else
- Real-world references beat adjectives
- Spatial language beats coordinates
- Lean prompts beat long prompts
- Explicit exclusions beat hoping GPT figures it out
- No dots at the end of in-image text
- Confirm in-image text before generating
- For reference-based work, run all 7 reverse-engineer layers before writing the prompt

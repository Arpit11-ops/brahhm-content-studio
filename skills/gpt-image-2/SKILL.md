---
name: gpt-image-2
description: Generate and edit images using OpenAI's GPT Image 2.5 (released Sept 8, 2026 — successor to GPT Image 2.0). Interactive skill that guides users through image creation with style presets, cost-aware draft/final workflow, thinking mode, carousels, photo editing, reference-image role assignment, preservation clauses, and surgical multi-turn edits. This skill should be used when the user requests image generation via OpenAI/GPT Image, wants to create social media carousels, edit photos into artistic styles, or needs images with readable text (infographics, diagrams, posters).
---

# GPT Image 2.5 — Interactive Image Generation

Generate and edit images via OpenAI's GPT Image 2.5 API with an interactive, guided workflow. GPT Image 2.5 rolled out on Sept 8, 2026 as the successor to GPT Image 2.0 — same prompt shape, meaningfully better fidelity, editing precision, multi-turn stability, and two new quality tiers.

## What changed in 2.5 vs 2.0 — the deltas that matter

1. **Up to 50% faster generation** at matching quality.
2. **Better reference-photo preservation** — subjects (packs, faces, products) stay recognizable across new settings and styles. The single biggest fidelity lever for our workflow.
3. **Surgical editing** — edits change only the specified element and leave the rest of the image intact. Multi-turn edits are now trustworthy — earlier edits survive later ones instead of degrading.
4. **Two new quality tiers**: `xhigh` and `max` above the old `high` ceiling. Purpose-built for fine text detail, dense infographics, small callouts.
5. **Two new API model IDs**:
   - `gpt-image-2.5-flare` — default, speed-optimized, same quality + editing improvements as the ChatGPT UI. Right choice for daily post volume.
   - `gpt-image-2.5-sunburst` — designed for editing precision on premium creative work, longer generation times. Right choice for HF + Caveman hero shots and multi-pack layouts where any label distortion is fatal.
   Both priced identically ($8 input / $30 output per M image tokens, $2 cached, $5 per M text tokens).
6. **Sketch tool** in the ChatGPT UI — finger-sketch on touchscreen as spatial reference. Point-and-edit inside the UI now works instead of describing changes only in prose.
7. **More accurate rendering of real-world info** — brand names, prices, factual text, known references come through cleaner.

Text rendering is still imperfect on placement — treat text as a hard requirement, not a hope.

## Interactive Flow

When the user invokes this skill, guide them through these steps using AskUserQuestion. Do not skip steps — the interactive flow is the core experience.

### Step 1: What are we making?

Ask the user what they want to create. Offer these options:

- **Single image** — one image from a text prompt
- **Photo edit** — transform an existing photo into a style
- **Carousel** — 5-10 cohesive slides for LinkedIn/Instagram
- **Variants** — multiple versions of the same concept
- **Quick generate** — skip questions, just run the prompt

If the user already provided a clear prompt (e.g. "generate an editorial image of a rocket"), skip to Step 3.

### Step 2: Style selection

Show the user available presets grouped by category. Read `presets.yaml` and present them:

**Visual styles** (no text in image):
editorial, blueprint, ink, risograph, wireframe, constellation, brutalist, grain

**Text-heavy** (leverages GPT Image 2.5 text rendering):
infographic, slide, diagram, poster, menu, manga

**Community favorites:**
trading-card, pixar, app-mockup, isometric, action-figure, cinematic, panorama

**Custom** — user describes their own style

Ask: "Which style? Or describe your own."

### Step 3: Platform & sizing

Ask where this will be used:
- YouTube thumbnail (1280×720)
- Instagram square (1080×1080)
- Instagram feed portrait (1080×1350, 4:5)
- Slides/presentation (1920×1080)
- Blog hero (1200×630)
- X/Twitter (1600×900)
- Story / Reel end-frame (1080×1920, 9:16)
- Custom size
- No resize (use API default)

### Step 4: Model + quality tier

**Model picker (2.5 API):**
- Default → `gpt-image-2.5-flare` — daily posts, single-pack heroes, most carousels
- Premium → `gpt-image-2.5-sunburst` — HF wellness hero, Caveman lookbook, any multi-pack composition, any post where label distortion is fatal

**Quality tier picker:**
- `low` / `medium` — drafts only
- `high` — default for standard posts
- `xhigh` — information-dense EDUCATE posts, Amazon A+ T75 carousels, HF callout-heavy hero shots, price-pill + trust-ribbon + multi-callout compositions
- `max` — reserved for hero-slide reels, brand pitch decks, and multi-pack fidelity-critical renders where the extra render time is worth the credit spend

### Step 5: Draft first, then final

**Always generate a draft first** unless the user says "skip draft" or uses `--draft false`.

1. Generate with `--draft` (quality=low, ~$0.006/image)
2. Show the image to the user using the Read tool
3. Ask: "Like this direction? I can: (a) run a surgical edit on this image, (b) generate final quality, (c) adjust the prompt, (d) try a different style, (e) regenerate with a new seed"
4. If approved, generate final with `--quality high` (or `xhigh` / `max` per Step 4)
5. Use `--seed` from the draft to maintain composition when upgrading to final

The 2.5 change here: option (a) — surgical edit on the existing image — is now the correct default for "fix one thing." Do not regenerate from scratch when you only want to move a price pill, swap a colour, or change one line of text.

### Step 6: Show result and offer next actions

After generation, always:
1. Show the image using the Read tool
2. Open it with `open <path>` for full-resolution preview
3. Report the cost
4. Offer: "Want to (a) run a surgical single-change edit, (b) generate variants, (c) use as reference for more images, (d) done?"

## The 2.5 prompt-shape upgrades (mandatory when applicable)

These four additions land inside the same prose Protocol 6 cascade — they do NOT replace the cascade. Fold them in where they apply.

### 1. Reference-image role assignment (when 2+ refs are attached)

Assign an explicit role to each reference image in the opening paragraph. This prevents cross-contamination — 2.5 respects role labels cleanly when the prompt names them.

Pattern:
```
Image 1 is the [product A] pack — reference-only, reproduce with total fidelity.
Image 2 is the [product B] pack — reference-only, reproduce with total fidelity.
Ignore every other image in the conversation.
```

Extend for 3+ refs (identity ref, lighting ref, composition ref, etc):
```
Image 1 = product identity (preserve geometry, label, proportions).
Image 2 = lighting reference (use its soft warm rim; ignore its subject and background).
Image 3 = composition reference (use its left-weighted placement; do not copy its colours or text).
```

### 2. Preservation clause (mandatory when any reference pack is uploaded)

State explicitly what must not change. 2.5 is materially better at preservation but still needs the list — without it, drift still happens.

Pattern (adapt to the specific pack):
```
Preserve on the pack: pouch/bottle silhouette, seal geometry, base geometry, ground colour,
brand wordmark and badge as printed, illustration position and style, product photograph on
pack, product label with every line of printed copy including [key on-pack text], multilingual
subtitles, quality seal, vegetarian dot, tear-here / resealable strips, full bottom
certification row including every certification stamp and small-print element. Change nothing
on the pack — no repositioned elements, no new text, no missing text, no colour shift, no
logo redraw, no illustration redraw, no SKU substitution.
```

### 3. "Appears exactly once" text spec (every text zone)

Every quoted text zone must be marked with "render exactly once" — this kills 2.5's residual duplicate-text hallucination.

Pattern:
```
Render exactly once: 'RAW SEEDS' on line 1.
Render exactly once: 'PURE PANTRY' on line 2.
```

Also add to the negatives paragraph:
```
No duplicate text zones, no repeated headlines, no repeated ribbons, no repeated callouts,
no repeated price pills.
```

### 4. Surgical single-change edit (when iterating on an existing render)

When a render comes back 80–95% right and only one thing needs fixing, do NOT regenerate from scratch. Send an edit turn:

```
Change: [one specific thing — e.g. "move the left price pill 8% down, keeping its size and colour"]
Preserve: [everything else — "headline, tagline, packs, background bisection, trust ribbon,
right price pill, footer band, website CTA, callouts, colour temperature, lighting, film grain"]
Constraints: [no new elements, no colour shift on the pack, no re-rendering of any preserved item]
```

Run 2.5 in edit mode with the previous image as the base. Iterate one change per turn.

## Carousel Workflow

When the user wants a carousel (5-10 slides):

### 1. Story arc
Ask: "What's the story? Give me the key message and I'll draft a 10-slide arc."

Then propose a slide-by-slide plan like:
```
Slide 1: [Cover] — hook headline + hero image
Slide 2: [Problem] — bold statement
Slide 3: [Context] — illustration + explanation
...
Slide 10: [CTA] — call to action with URL
```

Ask the user to approve or modify the plan.

### 2. Style consistency
Use the same preset + seed range across all slides. For carousels:
- Pick one visual style for all slides
- Use `--seed` to lock composition patterns
- Include pagination dots in prompts (e.g., "10 small dots at bottom, third dot highlighted orange")
- Maintain consistent color palette and typography
- Assign consistent reference-role labels across slides so 2.5 threads visual identity through the batch

### 3. Draft batch
Generate all slides as drafts first ($0.006 × 10 = $0.06 total). Show them all to the user as a contact sheet or one by one. Ask which ones to regenerate or adjust — or which ones to fix via surgical edit.

### 4. Final batch
Only generate finals for approved slides. For information-dense carousels (T75 Amazon A+ patterns), bump quality to `xhigh`.

## Photo Edit Workflow

When the user wants to transform a photo:

1. Ask for the source image (file path or clipboard)
2. For clipboard: save with `osascript` to a temp file
3. Show available styles and ask which to try
4. Generate a draft edit first — with a Change / Preserve / Constraints block
5. Show result, ask if they want further edits
6. Chain surgical edits, one per turn, until locked

Use `--edit <path>` for the API call.

## Cost Awareness

Always communicate costs before generating. GPT Image 2.5 API pricing (per M tokens):
- Text input: $5
- Image input: $8 (cached: $2)
- Image output: $30

| Quality | Per image (approx) | 10-slide carousel |
|---------|--------------------|-------------------|
| `--draft` (low) | $0.006 | $0.06 |
| medium | $0.05 | $0.50 |
| high (default) | $0.21 | $2.10 |
| xhigh | $0.35 | $3.50 |
| max | $0.55 | $5.50 |
| high + thinking | $0.25-0.42 | $2.50-4.20 |

Thinking mode adds 20-100% cost. Only suggest it for text-heavy or complex compositions where `xhigh` alone did not resolve the density.

The script auto-confirms when cost < $0.50. Above that, it prompts the user.

## Prompt Engineering Tips

When helping users write prompts, apply these patterns:

1. **Structure**: Scene → Subject → Detail → Lighting → Constraint
2. **Front-load the subject**: put the main thing first (2.5 weights the opening words heaviest)
3. **For text in images**: quote exact text with single quotes: `'with the headline "Hello World"'` — and mark every zone `render exactly once`
4. **Character consistency**: maintain a 5-tuple: age + appearance + hairstyle + distinctive features + clothing
5. **Style tags at end**: append tags like `editorial-magazine`, `studio-product` to converge batches
6. **Use `--seed` for iteration**: lock composition, vary only the prompt details
7. **Preservation clause is mandatory when a reference pack is uploaded** — never rely on the reference alone
8. **Real-world references beat adjectives**: "Kodak Portra 400 warmth", "ARRI studio key", "Aesop store minimalism"
9. **Prose over labeled blocks in the ChatGPT UI** — the OpenAI cookbook now allows labeled segments in some contexts, but the ChatGPT UI's edit-mode router still rejects ALL-CAPS field labels. Prose wins.
10. **Surgical edits over regens** — the multi-turn edit stability in 2.5 makes single-change edits the correct default fix, not full regeneration

## CLI Reference

```bash
# Basic generation
scripts/gpt_image_2.py "prompt" output.png

# With preset and platform
scripts/gpt_image_2.py --preset editorial --platform square "subject" out.png

# Draft mode (~$0.006/image)
scripts/gpt_image_2.py --draft "prompt" out.png

# With thinking for complex layouts
scripts/gpt_image_2.py --thinking medium --preset diagram "OAuth flow" out.png

# xhigh quality for dense text/callouts
scripts/gpt_image_2.py --quality xhigh --preset infographic "prompt" out.png

# max quality for fidelity-critical multi-pack renders
scripts/gpt_image_2.py --quality max "prompt" out.png

# Premium model for hero shots
scripts/gpt_image_2.py --model gpt-image-2.5-sunburst --quality high "prompt" out.png

# Seed for reproducibility
scripts/gpt_image_2.py --seed 42 "prompt" out.png

# Edit existing photo (surgical)
scripts/gpt_image_2.py --edit photo.png "Change: swap chair colour to walnut. Preserve: everything else." out.png

# Variants with contact sheet
scripts/gpt_image_2.py --n 4 --preset ink "mountain" out.png

# Cost estimate
scripts/gpt_image_2.py --estimate --n 10 --quality xhigh "batch test"

# Skip confirmation
scripts/gpt_image_2.py -y --n 10 "batch" out.png

# Dry run (show prompt without API call)
scripts/gpt_image_2.py --dry-run --preset editorial "test" out.png
```

## Files

- `scripts/gpt_image_2.py` — main CLI (Python, requires PyYAML)
- `presets.yaml` — 21 style presets (visual + text-heavy + community)
- `platforms.yaml` — 8 platform sizing presets
- `references/api_reference.md` — full API documentation
- `~/.config/gpt-image-2/config.yaml` — user defaults
- `~/.config/gpt-image-2/history.jsonl` — generation log
- `~/.config/gpt-image-2/last.json` — last run (for `again`)

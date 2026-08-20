# Higgsfield Borrow Plan — Content Studio Typography + Auto-Fire Upgrade

**Session:** 2026-08-19 (planning) → next session (execution)
**Decision status:** Puran greenlit all three yes/no calls at end of planning session.
**Goal:** Fix pale typography + wire auto-firing skill hooks + fold Higgsfield's brand-kit / style-key / mode-taxonomy discipline into Content Studio 3.2 → producing Content Studio 3.3.

---

## 0. Session Kickoff — Read These First, In This Order

The new session must read the following before touching a single file. This is a hard gate.

**A. Our current workflow (project-side):**
1. [CLAUDE.md](../CLAUDE.md) — full project instructions (Protocols 1–11, VEE, banned words, brand directory).
2. Memory index — always loaded automatically. Cross-reference these specifically:
   - `feedback_typography_taste` (root diagnosis of the pale typography problem)
   - `feedback_gpt_creative_director_model` (the 6-part prose cascade in Protocol 6)
   - `feedback_gpt_text_zone_spec` (4-part text zone format)
   - `feedback_gpt_callout_size` (callout weight and size discipline)
   - `feedback_gpt_prose_not_structured` (the router-mechanic reason prompts must be prose)
   - `feedback_never_auto_generate_images` (auto-firing rule to respect)
   - `feedback_codex_image_gen_skill` + `feedback_codex_lean_execution` (how we currently invoke codex)
   - `feedback_amazon_a_plus_carousel` (T75 A+ carousel DNA we will upgrade with Higgsfield's 7-module taxonomy)
   - `feedback_pack_front_hero` + `feedback_no_tilted_packs` (pack fidelity rules that stay)
3. Evidence renders (visual diagnosis — Bakkit Ajwain carousel, 2026-08-19):
   - [S1 render](prompts/assets/2026-08-19_caveman_bakkit-ajwain/s1.png) — generic magazine bold serif (pale outcome)
   - [S5 render](prompts/assets/2026-08-19_caveman_bakkit-ajwain/s5.png) — heavy condensed industrial display serif (successful outcome)
   - **Both from same-batch same-template same style-tag close prompts. Wildly different type. Proves GPT rolls dice unless anchored to a reference image.**

**B. Higgsfield methodology (borrow-source, do NOT invoke — bound to another agency):**
1. `C:/Users/arpit/.agents/skills/higgsfield-product-photoshoot/SKILL.md` — the 10-mode taxonomy, the Type A–F interview pattern.
2. `C:/Users/arpit/.agents/skills/higgsfield-generate/SKILL.md` — model routing + Marketing Studio resource model + Virality Predictor.
3. `C:/Users/arpit/.agents/skills/higgsfield-generate/references/marketing-brand-kits.md` — the brand kit contract (name/logo/palette/fonts/tone/products fetched from a URL, attached once, reused everywhere).
4. `C:/Users/arpit/.agents/skills/higgsfield-generate/references/marketing-dtc-ads.md` — `--format-id` as hard-required creative choice.
5. `C:/Users/arpit/.agents/skills/higgsfield-generate/references/marketing-ad-references.md` — reusable inspiration reference contract (avatar-bound, product-bound, mutually exclusive with hook+setting).
6. `C:/Users/arpit/.agents/skills/higgsfield-generate/references/marketing-modes.md` — 9 marketing video modes with setup-item whitelists.
7. `C:/Users/arpit/.agents/skills/higgsfield-generate/references/prompt-engineering.md` — the ~200-token sweet spot rule (our prompts run 400–500 words; may be over the limit).
8. `C:/Users/arpit/.agents/skills/higgsfield-video-explainer/references/prompts.md` — one style-key image + one identical STYLE descriptor pasted into every clip. This is the pattern we copy for typography locking.
9. `C:/Users/arpit/.agents/skills/higgsfield-marketplace-cards/SKILL.md` — 14-asset taxonomy + 4 scope bundles (upgrade path for T75).

**C. Higgsfield CLI shape (for reference only — never invoke for our brands):**
- Binary: `/c/Users/arpit/.codex/.sandbox-bin/codex.exe` is UNRELATED. Higgsfield CLI is at `C:/Users/arpit/AppData/Roaming/npm/higgsfield`.
- 13 command groups: `generate / product-photoshoot / marketplace-cards / marketing-studio / soul-id / game / website / model / workflow / preset / voices / upload / account / auth / workspace`.
- 27 video models, 10 video workflows, 2 preset types (video-explainer + animation-action).

**Never call any `higgsfield ...` command from this repo. Read for methodology only.**

---

## 1. Diagnosis — Verified Root Cause

**Symptom Puran flagged:** "Our generation typography is very pale until I give references, and sometimes those references also fail."

**What I verified:**
- Same-batch same-template prompts produce inconsistent type quality (S1 generic vs S5 distinctive — both Bakkit Ajwain 2026-08-19 carousel).
- Our Protocol 6 prose describes typography in words only ("bold condensed serif") — a category, not a specific look.
- GPT Image 2 non-deterministically picks a serif family unless anchored to a **reference image**.
- Feedback memory `feedback_typography_taste` (64 days old) already knew: "distinctive branded type systems, not generic bold sans" — the rule exists, the enforcement mechanism does not.
- Our `.claude/settings.json` is effectively empty of hooks — the CLAUDE.md SKILL AUTO-TRIGGER MAP is aspirational, not enforced.
- Our prose runs 400–500 words per slide; Higgsfield's own prompt-engineering doc pegs the sweet spot at ~200 tokens ("models distort with very long prompts").

**Root cause statement:**
Type consistency is left to GPT's default heuristics because we anchor typography with descriptor words only, never with a reference image. Fix requires either (a) shortening prompts and hoping GPT respects "bold condensed serif" more reliably, or (b) attaching a style-key reference image that shows the exact type family. Higgsfield uses (b); we should too.

---

## 2. Five Ideas Borrowed from Higgsfield

Each idea → concrete studio pain it solves.

| # | Idea | Pain it fixes |
|---|---|---|
| 1 | **Brand Kit** — one persistent JSON per brand with name/logo/palette/type-refs/tagline/tone, injected into every prompt | Re-typing brand DNA in every prompt's style-tag close; drift between posts |
| 2 | **Style Key Image** — one reference plate per brand carrying type family + palette + grain + finish, attached to every codex call | The pale typography problem — GPT stops rolling type dice, matches the reference |
| 3 | **Ad Reference Library** — save every successful render as a reusable anchor for future prompts | Studio doesn't learn from itself; good renders are thrown away |
| 4 | **Mode field on every VEE template** — 10-mode taxonomy from product-photoshoot | Templates carry composition only; mode carries recipe + implicit rules |
| 5 | **Auto-fire hooks in .claude/settings.json** — enforce the SKILL AUTO-TRIGGER MAP | The map exists in CLAUDE.md but Claude can silently skip it; hooks make it mandatory |

**Bonus fixes surfaced during audit:**
- Shorten Protocol 6 prose to ~200 tokens (Higgsfield's stated sweet spot — controlled test on one slide before rolling out).
- Reel voice-over generated FIRST, visuals paced to voice (from higgsfield-video-explainer discipline).
- "Ad reference OR hook+setting, never both" mutual-exclusion rule for future ad briefs.

---

## 3. Five-Step Build Plan (Execute in New Session, In This Order)

### Step 1 — Wire auto-fire hooks (fastest, ~15 min)

**File:** `.claude/settings.json`

**Hooks to add:**
- `UserPromptSubmit` — when input matches `/^(Full post|Caption|Reel script|GPT prompt|Batch this week|Hashtags|carousel|generate the image|run codex|make the image)/i`, force pre-flight receipt to run.
- `PreToolUse` (Bash) — when the command contains `codex.exe`, verify:
  - Point 6 in-image text confirmation exists in the current turn context
  - Style key path exists for the active brand (once Step 2 is done)
  - Pack reference path exists

**Success criteria:** Type "Caption for Caveman — Bakkit" cold, watch the pre-flight receipt fire automatically without Claude having to remember.

**Risk:** If a hook is too aggressive it blocks legitimate work. Ship with soft warnings first (log, don't block); flip to block after a week of no false positives.

### Step 2 — Build 5 Brand Kit JSON files (~30 min per brand, 2.5 hours total)

**Files to create:**
- `research/brands/caveman/brand_kit.json`
- `research/brands/health_fields/brand_kit.json`
- `research/brands/pusht/brand_kit.json`
- `research/brands/greendipz/brand_kit.json`
- `research/brands/biomart/brand_kit.json`

**Schema per file:**
```json
{
  "brand_name": "Caveman Organic",
  "website": "caveman.co.in",
  "handle": "@cavemanorganic",
  "logo_path": "research/brands/caveman/assets/logo.png",
  "palette": {
    "primary": "#D20000",
    "primary_name": "Cave Red",
    "ground": "warm near-black charcoal",
    "type_offwhite": "warm cream off-white"
  },
  "type_system": {
    "headline": {
      "family_reference": "heavy condensed industrial display serif, Druk/Owners Wide weight",
      "style_key_path": "research/brands/caveman/style_key.png"
    },
    "callout": "bold sans-serif caps, tight letter-spacing",
    "footer_strip": "tight-tracked sans caps, warm cream on Cave Red hairline"
  },
  "lighting": "ARRI studio key top-left, warm rim glow on pack, Kodak Portra 400 grain",
  "aesthetic_anchor": "raw editorial product photography, Fear of God Essentials lookbook",
  "style_tag_cluster": "raw editorial product photography, Fear of God Essentials lookbook, Kodak Portra 400 warmth with heavy film grain, ARRI studio key light with warm rim glow, cinematic depth, dark editorial world, Cave Red accent, premium Indian organic",
  "tagline": "Eat Like A Caveman",
  "tone": "raw, blunt, Gen Z confidence, cave-red world",
  "products_url_root": "https://caveman.co.in/products/",
  "cta_domain": "caveman.co.in",
  "banned_lexicon_overrides": ["guilt-free", "millet-powered"]
}
```

**Success criteria:** Protocol 6 opens brand_kit.json for the active brand and injects palette + style_tag_cluster + lighting into the prompt — no manual re-typing in the prose.

**Risk:** Schema drift as we learn what fields matter. Ship v1, iterate. Version the schema.

### Step 3 — Generate 5 Style Key reference plates (needs Puran's approval on each plate, ~20 min per brand + review)

**Files to create:**
- `research/brands/caveman/style_key.png`
- `research/brands/health_fields/style_key.png`
- `research/brands/pusht/style_key.png`
- `research/brands/greendipz/style_key.png`
- `research/brands/biomart/style_key.png`

**Method (per brand):**
1. Write a Protocol 6 prose prompt for a pure aesthetic plate — no product, no scene, no lifestyle. Just: the brand ground colour + Portra grain + a sample headline in the exact type family we want, a sample callout, a sample footer strip, all laid out as an abstract type-and-colour reference plate.
2. Codex it at 1080×1350.
3. Deliver to Puran for approval.
4. Iterate until Puran says "this is the Caveman look I want locked."
5. Save as `style_key.png`.

**Then update Protocol 6:** every subsequent codex call attaches TWO reference images — the pack photo AND the style_key.png for the active brand.

**Success criteria:** Re-render Bakkit S1 with the new dual-reference setup. Type should match S5's heavy condensed display serif, not S1's generic bold serif. If it does → typography drift is solved. If it doesn't → we escalate to shorter prompts (bonus fix).

**Risk:** Highest-value step but also highest-review-cost step. Budget an hour of Puran's time across the 5 brands.

### Step 4 — Add MODE field to VEE + Point 5 (~1 hour editing pass)

**Files touched:**
- `Visual_Execution_Engine_v4_txt.txt` — add `MODE` column to every template row.
- `CLAUDE.md` Protocol 6 — add "MODE is mandatory in Point 5" rule.
- `CLAUDE.md` Required Output Format — add MODE line to Point 5 Visual Direction schema.

**Mode taxonomy to adopt (from Higgsfield product-photoshoot, tailored):**
- `product_shot` — pack on neutral/studio ground
- `lifestyle_scene` — pack in real-world scene with props
- `closeup_with_person` — hands or partial face demonstrating
- `moodboard_pin` — vertical 2:3 Pinterest-native
- `hero_banner` — wide-format website/email header
- `social_carousel` — 3–10 connected slides (default for our carousels)
- `ad_creative_pack` — Meta/paid social variants pack
- `conceptual_product` — surreal / CGI / floating
- `restyle` — transform existing image aesthetic
- `pack_panel_info_grid` — our own addition, the Bakkit S5 pattern (Amazon A+ style dense info card)

**Success criteria:** Every new post's Point 5 declares MODE. Protocol 6 uses the mode to pull the right style-key subset from brand kit.

**Risk:** Low. Mostly a labeling change.

### Step 5 — Seed the Ad Reference Library (ongoing, seed with 20 confirmed renders from last 30 days)

**Folder:** `research/ad_references/`

**Structure:**
```
research/ad_references/
├── caveman/
│   ├── 2026-08-19_bakkit_s5_pack_panel.png
│   ├── 2026-08-19_bakkit_s5_pack_panel.json
│   └── ...
├── biomart/
├── pusht/
├── health_fields/
└── greendipz/
```

**Per-reference JSON sidecar:**
```json
{
  "captured": "2026-08-19",
  "brand": "caveman",
  "product": "Bakkit Ajwain Cookies",
  "mode": "pack_panel_info_grid",
  "angle": "EDUCATE",
  "template": "T83",
  "works_for": ["pack_panel", "info_grid", "back_of_box_reveal"],
  "notes": "Heavy condensed display serif landed cleanly. Cave Red accent word works. Small print line under grid reads legibly at thumbnail scale.",
  "source_slide": "s5",
  "source_batch": "2026-08-19_caveman_bakkit-ajwain"
}
```

**Success criteria:** Next Caveman EDUCATE carousel briefs pull `bakkit_s5_pack_panel.png` as a third reference alongside pack + style_key when the mode matches. Aesthetic compounds instead of drifts.

**Risk:** Discipline drift — easy to forget to save winners. Mitigate with a Step 5-triggered hook: after every codex render Puran approves, prompt Claude to ask "save to ad references?".

---

## 4. New CLAUDE.md Sections to Add (v3.3)

Once Steps 1–5 land, CLAUDE.md gets these new sections:

- **Protocol 12 — Brand Kit Injection** (mandatory before Point 7)
- **Protocol 13 — Style Key Attachment** (mandatory on every codex call)
- **Protocol 14 — Ad Reference Lookup** (Protocol 6 opens the ad reference library and pulls closest match)
- **Skill Auto-Trigger Map v2** — replaces the current map with the actual hook definitions
- Point 5 schema update — MODE field added
- VEE column update — MODE column added

---

## 5. Success Criteria for the Overall Upgrade

The upgrade is a win if all four hold:

1. **Typography consistency across a batch** — S1 and S5 in a next Caveman carousel look like the same visual family, not two different designers. Measure by: Puran doesn't have to say "S1 typography is pale, please redo".
2. **Pre-flight receipt never missed** — for 10 consecutive posts, the receipt appears without Claude having to be reminded.
3. **Prompt length under 250 words per slide** — after brand kit injection removes the re-typed style-tag close, prose gets leaner. Measure by word count of Point 7 prompts before vs after.
4. **At least 15 ad references seeded** in the library within the first two weeks after Step 5 lands.

---

## 6. Sequence for the New Session

**Fresh session start command (paste this as the first message):**

> Read `research/higgsfield_borrow_plan_2026-08-19.md` end to end. Then read the Section 0 reading list (workflow + memory notes + Higgsfield reference files + evidence renders). Then confirm you have full context and propose Step 1 (auto-fire hooks) as the first implementation. Do not touch any file until I greenlight the Step 1 approach.

**Then Puran greenlights or edits Step 1 → Claude implements → verify → move to Step 2 → repeat.**

---

## 7. Files That Will Change (Impact Map)

| File | Change | Step |
|---|---|---|
| `.claude/settings.json` | Add UserPromptSubmit + PreToolUse hooks | 1 |
| `research/brands/*/brand_kit.json` (new × 5) | Create brand DNA JSON per brand | 2 |
| `research/brands/*/style_key.png` (new × 5) | Reference type/palette plate per brand | 3 |
| `Visual_Execution_Engine_v4_txt.txt` | Add MODE column | 4 |
| `CLAUDE.md` | Add Protocols 12–14, Point 5 MODE field, VEE MODE column reference | 4 + 3 |
| `research/ad_references/*/` (new × 5) | Seed with 20 winners | 5 |
| `CLAUDE.md` SKILL AUTO-TRIGGER MAP | Rewrite as v2 pointing at actual hooks | 1 |

---

## 8. What This Does Not Change

- Never invoke Higgsfield CLI for our brands. Read-only borrow.
- Protocol 6 prose-not-structured rule stays. All new content still goes through the 6-part cascade.
- Codex-image-gen skill workflow stays. Just gains a style-key reference alongside the pack.
- Banned words, NO DOTS RULE, no percentages in on-image text, no tilted packs — all stay.
- The 13-point post package structure stays. Point 5 gains a MODE line; Point 7 gets shorter prose after brand-kit injection.
- Humanizer sweep stays mandatory on every caption.

---

## 9. Open Questions Left for Puran

- On Step 3 style key plates: does Puran want one style key per brand, or two per brand (one for "dense info grid" mode, one for "hero product" mode)? Two per brand gives sharper anchoring; one per brand is faster to set up.
- On Step 5 ad reference seeding: which 20 renders from the last 30 days does Puran consider "confirmed winners"? He'll need to point Claude at the folders. Suggested candidates: T75 Amazon A+ Health Fields carousel, T80 Caveman Bakkit multi-pack, T82 HF doctor-sister rakhi bundle, Bakkit Ajwain S5 (proven this session).
- On the shorten-prompts bonus fix: ready to A/B test one slide (Bakkit re-render) at ~200 tokens vs ~400 tokens after Step 2 lands?

Answer these when the new session gets to those steps — no need to answer now.

---

## 10. Handoff Discipline

- The new session must Read this file first — before any other action.
- The new session must then Read every file in Section 0's reading list before proposing implementation.
- No file gets edited until Puran approves the approach for that step.
- One step at a time. Do not batch Steps 2–5 together — every step has a review gate.

**End of plan. Version 1.0. Puran-approved 2026-08-19.**

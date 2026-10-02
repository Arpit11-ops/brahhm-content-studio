---
name: codex-image-gen
description: Generate a Content Studio post image by handing a written GPT Image 2.5 prompt (plus the local pack reference file) to the OpenAI Codex CLI, which calls its native image tool and saves the PNG into the repo. MUST USE whenever Puran says any of "generate the image", "make the image", "run codex", "codex it", "gen the image", "create the image", "produce the still", or otherwise asks Claude to actually render the still after a Point 7 prompt has been locked in the current turn. Removes the copy-paste-into-ChatGPT step of the standard Content Studio 3.4 image workflow.
metadata:
  type: workflow
  triggers: [image generation, codex, gpt image 2, gpt image 2.5, render still, generate image, run codex]
---

# Codex Image Gen — Content Studio Workflow

Skip the copy-paste. When a Point 7 GPT Image 2.5 prompt is already locked and Puran says "generate the image" (or any close variant), hand the prompt straight to the OpenAI Codex CLI. Codex has native image generation — it will call its own image tool, honour the reference pack photo(s), and save the PNG into the repo. You then deliver the file back to Puran via `SendUserFile`.

This skill assumes:
- A locked GPT Image 2.5 prompt exists in the current turn (Point 7 of the standard 13-point package, written in Protocol 6 v3.4 prose format with preservation clause + reference-role assignment + appears-exactly-once text spec).
- The pack reference file path(s) is known (Point 7's upload flag line, sourced from `C:\Users\arpit\Documents\storage\arpan organic\[brand]\...`). Multi-pack renders may attach 2-5 refs — order matters (Image 1 first, Image 2 second, etc, matching the role assignment in the prompt).
- Puran has already confirmed Point 6 (in-image text table). Do not run this skill before Point 6 confirmation — that is a Protocol 6 gate.

## Model tier picker (2.5 API)

- **Default → `gpt-image-2.5-flare`** — daily posts, single-pack heroes, most carousels. Speed-optimized, same quality as the ChatGPT UI, 50% lower latency than 2.0.
- **Premium → `gpt-image-2.5-sunburst`** — HF wellness hero, Caveman lookbook, any multi-pack composition, any post where label distortion is fatal. Longer generation, tighter edit precision.

Puran can request premium explicitly ("run sunburst" / "premium render") or the skill auto-routes to sunburst when the prompt contains 2+ pack references OR the brand is HF or Caveman AND the render is a hero shot.

## Quality tier picker

- `high` (default) — standard posts
- `xhigh` — information-dense EDUCATE posts, T75 Amazon A+ carousels, HF callout-heavy hero shots, price-pill + trust-ribbon + multi-callout compositions
- `max` — hero-slide reels, brand pitch decks, multi-pack fidelity-critical renders

Puran can override ("run xhigh" / "max quality") or the skill auto-bumps to xhigh when the prompt contains 4+ text zones.

## Binary and paths

- Codex CLI binary: `C:/Users/arpit/AppData/Local/OpenAI/Codex/bin/c6fe824d725f02d7/codex.exe` — the live desktop binary. The old sandbox binary at `/c/Users/arpit/.codex/.sandbox-bin/codex.exe` is outdated (uses a stale model whitelist that server-side rolled off ChatGPT-account tier on 2026-09-25) and MUST NOT be used. If the live-binary path changes on a Codex desktop update, re-derive it from `CODEX_CLI_PATH` in `~/.codex/config.toml`.
- Scratchpad root for prompt files: `C:\Users\arpit\AppData\Local\Temp\claude\C--NITRO-4-BACKUP-IMPORTANT-WORK-brahhm-content-studio\<session>\scratchpad\` — Claude Code sets this per session, use whatever value appears in the `Scratchpad Directory` note at the top of the session.
- Asset output root: `research/prompts/assets/`
- Per-post asset folder: `research/prompts/assets/YYYY-MM-DD_<brand>_<slug>/`
- File naming: `hero.png` for the first attempt, `hero_v2.png`, `hero_v3.png`, etc. for iteration re-runs after feedback.

## Workflow

Run these steps in one turn — do not sequence them across multiple Claude turns unless a step fails.

### 1. Prepare the prompt file

Write the locked Point 7 prompt verbatim to the scratchpad as a single `.txt` file, one prompt per file. Name it descriptively so multiple runs in a session do not overwrite each other:

```
<scratchpad>/<brand>_<product-slug>_prompt.txt          (first attempt)
<scratchpad>/<brand>_<product-slug>_prompt_v2.txt       (second attempt after feedback)
```

Use the Write tool for this — do not echo/heredoc via Bash. Codex reads the file directly, so encoding matters (UTF-8 with the em-dashes, middots, and curly quotes preserved exactly as Protocol 6 requires).

### 2. Prepare the output folder

Ensure the per-post asset folder exists:

```bash
mkdir -p "research/prompts/assets/YYYY-MM-DD_<brand>_<slug>"
```

Use the same folder across iterations of the same post so `hero.png`, `hero_v2.png`, `hero_v3.png` accumulate in one place. This mirrors how VEE templates are versioned.

### 3. Invoke Codex

Call Codex CLI with `exec --dangerously-bypass-approvals-and-sandbox` so it runs non-interactively without prompting Puran for approvals mid-turn. The instruction to Codex must be direct: read the prompt file verbatim, use the pack as a visual reference, call the image tool once, save to the exact output path. Do not let Codex summarise or rewrite the prompt.

```bash
"C:/Users/arpit/AppData/Local/OpenAI/Codex/bin/c6fe824d725f02d7/codex.exe" exec \
  --dangerously-bypass-approvals-and-sandbox \
  "Generate a single image using your native image generation tool with model gpt-image-2.5-flare (or gpt-image-2.5-sunburst for premium renders). The full image prompt is in this file: <PROMPT_FILE_PATH> — read it and pass it verbatim to your image tool. Use the product pack photo(s) at these paths as visual references in the exact order given: Image 1 = <PACK_1_PATH>, Image 2 = <PACK_2_PATH> (add more numbered entries only if the prompt's reference-role assignment lists more). Aspect ratio 4:5 vertical (or 1:1 / 9:16 per the prompt's stated ratio), quality high (or xhigh / max per skill directive). Save the generated PNG to: <OUTPUT_PATH>. Do not modify the prompt text, do not summarize it, do not swap the model, do not write any code, do not reorder or drop reference images, just call your image generation tool once with the exact prompt and reference image(s) in the given order." \
  2>&1 | tail -30
```

Wrap this in a single Bash tool call with `timeout: 420000` (7 minutes) — image gen typically finishes in 60–120 seconds but occasionally takes longer under load.

Notes on the instruction wording:
- **"Read it and pass it verbatim"** — Codex has a tendency to condense long prompts before sending them to the image tool. The explicit "verbatim" plus "do not modify, do not summarise" fights that instinct. Protocol 6 v3.4 prompts (with preservation clauses + ref-role assignments + appears-exactly-once specs) are engineered for GPT Image 2.5, not for a summariser.
- **"Do not write any code"** — Codex will otherwise sometimes try to write a Python wrapper that calls the OpenAI API directly. That wastes tokens and fails. Its built-in image tool is faster and correctly authenticated.
- **"Do not reorder or drop reference images"** — 2.5 respects role assignments (Image 1 / Image 2) cleanly ONLY when the attachment order matches the prompt's assignment. Codex will occasionally strip refs or reorder them.
- **"Do not swap the model"** — Codex sometimes falls back to older models when the requested one is congested. Explicit lock stops that.
- **Aspect ratio** — 4:5 vertical is the Content Studio default for feed posts. For carousels use 4:5. For stories or reel end-frames use 9:16. For 1:1 grid coherence thumbnails, 1:1. Pass the correct ratio explicitly.

### 4. Verify and deliver

Codex prints a confirmation line ending in the copied output path (Codex saves to its own cache under `.codex/generated_images/` then copies to the destination you gave it). Confirm the PNG exists:

```bash
ls -la "research/prompts/assets/YYYY-MM-DD_<brand>_<slug>/"
```

Then deliver it to Puran:

```
SendUserFile({
  files: ["research/prompts/assets/YYYY-MM-DD_<brand>_<slug>/hero.png"],
  caption: "<Brand> <date> · <angle> — <one-line what to check>",
  status: "proactive",
  display: "render"
})
```

Caption pattern: brand + date + angle name + a specific "look for X" note (label fidelity, callout legibility at thumbnail scale, seed mound shape, colour warmth, baked CTA presence — whatever Point 6 emphasised).

### 5. Iterate on feedback — SURGICAL EDIT FIRST, regen only if needed

When Puran flags something off (typography too small, chip colours wrong, mound flat, callout unreadable, etc.), the default fix under 2.5 is a **surgical single-change edit** on the previous image, NOT a full regeneration from scratch. 2.5's multi-turn edit stability makes edits preserve everything else reliably.

**Surgical edit path (default):**
1. Write a targeted Change / Preserve / Constraints block:
   ```
   Change: [one specific thing — e.g. "move the left price pill 8% down, keeping its size and colour"]
   Preserve: [everything else, listed]
   Constraints: [no new elements, no colour shift on the pack, no re-render of any preserved item]
   ```
2. Write this as a small edit-prompt file: `<brand>_<slug>_edit_v2.txt`
3. Run Codex again with the previous `hero.png` as the base image:
   ```bash
   "C:/Users/arpit/AppData/Local/OpenAI/Codex/bin/c6fe824d725f02d7/codex.exe" exec \
     --dangerously-bypass-approvals-and-sandbox \
     "Edit the image at <PREVIOUS_HERO_PATH> using your native image edit tool with model gpt-image-2.5-flare. The edit instruction is in this file: <EDIT_FILE_PATH> — read it and pass it verbatim to your image tool. Save the edited PNG to: <OUTPUT_PATH>." \
     2>&1 | tail -30
   ```
4. Save to `hero_v2.png` in the same asset folder.
5. Deliver via `SendUserFile`.

**Full regen path (only when surgical edit fails or the composition needs a fundamental rethink):**
1. Rewrite the Protocol 6 prompt in Claude with the targeted fixes.
2. Present the revised Point 6 text table (only the changed rows) and get quick confirmation.
3. Write a new prompt file: `<brand>_<slug>_prompt_v2.txt` (v3, v4, …).
4. Run Codex again in generation mode, saving to `hero_v2.png` (v3, v4, …) in the same asset folder.
5. Deliver via `SendUserFile`.

Keep every version on disk. Puran often compares v1 vs v2 to decide which direction is closer.

## Failure modes and how to catch them

**Codex silently condensed the prompt.**
Symptom: image lacks text zones, chips missing, or the wrong headline appears. Cause: Codex summarised before calling the image tool.
Fix: re-run with an even more explicit "verbatim, character-for-character, do not condense" line prepended to the exec instruction.

**Codex wrote a Python script instead of using its image tool.**
Symptom: exec output shows `python -c` or writes to `.py` files, no PNG saved.
Fix: add `"Do NOT write any Python code. Do NOT call the OpenAI API directly. Use only your built-in image generation tool."` to the exec instruction. Re-run.

**Codex saved to its cache but did not copy to the destination.**
Symptom: exec log mentions `.codex/generated_images/<uuid>/call_*.png` but the destination path is empty.
Fix: pull the source path from the exec log and copy manually:
```bash
cp "/c/Users/arpit/.codex/generated_images/<uuid>/call_*.png" "research/prompts/assets/<folder>/hero.png"
```

**Pack image is missing from the local storage folder.**
Symptom: bottle shape/label wrong in the render.
Fix: this is a Protocol 2 problem, not a codex problem. Locate the correct pack file first (per CLAUDE.md `Fetch Pack Image` step), then re-run.

**Wrong SKU rendered (pack swap).**
Symptom: uploaded the sunflower pack as reference, render came back with a different HF SKU (cashew nuts, almonds, etc). Cause under 2.5: reference-role assignment missing from the prompt, OR attachment order did not match the prompt's role labels, OR the preservation clause did not name the specific SKU + colour + illustration to preserve.
Fix: add all three (role assignment + preservation clause with SKU-specific detail + explicit `no SKU substitution` in the negatives block) to the Point 7 prompt, then re-run. If it swaps again, route to `gpt-image-2.5-sunburst` — sunburst holds SKU identity harder than flare.

**Duplicate text zones (headline appears twice, price pill duplicated, etc).**
Symptom: 2.5 renders correct text but twice on the canvas.
Fix: verify every text zone in the prompt uses `render exactly once: '...'` phrasing, and the negatives block includes `no duplicate text zones, no repeated headlines, no repeated callouts, no repeated price pills`. Re-run.

**Codex exec hangs past the 7-minute timeout.**
Cause: OpenAI image tool queue is backed up.
Fix: re-run once. If it hangs again, tell Puran the tool is congested and fall back to the manual paste-into-ChatGPT workflow for that image only.

## What this skill does NOT do

- Does not write the GPT Image 2.0 prompt. That is Protocol 6's job — this skill only executes the prompt you already have.
- Does not fetch the product description. That is Protocol 2's job — done before Point 7 is even written.
- Does not fetch the pack image from local storage. That is CLAUDE.md's `Fetch Pack Image` step — done before Point 7.
- Does not run the Protocol 3 claims audit. That is a Protocol 3 gate — done before Point 6.
- Does not decide the caption, hashtags, or CTA. Those are Points 8, 10, 11 of the 13-point package.
- Does not animate the image, stitch reels, or handle Grok Agent Mode. That is Protocol 8.

This skill is one bottleneck removed: the copy-paste from Claude's Point 7 prompt into ChatGPT and back. Everything else in the 13-point package still applies.

## Why this works

Codex CLI has direct access to OpenAI's image tool with Puran's own auth already configured (`~/.codex/auth.json`). It is the same underlying `gpt-image-2.5` model family Puran would hit in ChatGPT, but scripted. The prompt file trick avoids shell-escaping hell for the long Protocol 6 v3.4 prose. The `hero.png` / `hero_v2.png` versioning mirrors how VEE templates iterate.

The one thing to watch is that Codex is an agent — it may occasionally decide to "help" by rewriting the prompt, writing a wrapper script, downgrading the model, or explaining what it plans to do before doing it. The exec instruction is written defensively to shut down all four tendencies. Re-read step 3 if a render comes back looking generic or missing preservation elements — usually a Codex summarisation is the reason.

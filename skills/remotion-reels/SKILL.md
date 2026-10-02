---
name: remotion-reels
description: Build reels as code-built motion graphics with Remotion inside this workspace, using real pack images, cut-outs, typography, Kokoro voiceover and licensed music, rendered locally to MP4. MUST USE whenever Puran says "remotion reel", "make the reel in remotion", "motion graphics reel", "build the reel in code", "render the reel", "animate this in remotion", or asks to produce a reel/video/animation in this repo without Grok. Gives the workspace context (paths, tools, brand tokens, which Content Studio protocols still apply, how to render and deliver). It does not prescribe a reel structure: Puran directs the creative.
metadata:
  type: workflow
  triggers: [remotion, motion graphics, reel in code, render reel, animate, video, voiceover, kokoro]
---

# Remotion Reels: Content Studio Workspace Guide

This skill is an alternative production path to Protocol 8. Instead of GPT stills → Grok Agent Mode → CapCut, the reel is **written as React code in Remotion and rendered locally**. Packs are the real photos (moved, never regenerated), text is live typography, and voice, music and timing are exact to the frame.

**Puran directs the creative.** This file only gives you the context and tools. Do not impose a fixed beat structure, template or script unless Puran asks for one. Build what is asked, propose ideas when invited, and iterate on feedback.

---

## 1. Load these before writing reel code

1. The Content Studio pre-flight still applies to any reel copy (hook, on-screen text, VO lines, caption). Read the 4 mandatory skills plus `./skills/marketingskills-main/skills/video/SKILL.md`, and output the `PRE-FLIGHT ✅` receipt.
2. **Remotion knowledge:** invoke the `remotion-best-practices` skill (installed in `.claude/skills/`, sources in `.agents/skills/`). It routes to `remotion-markup` (animation, audio, fonts, transitions, images, multi-scene), `remotion-render`, `remotion-studio`, `remotion-captions` and the rest. Load the specific reference you need before using a feature you haven't used this session.
3. The active brand's Brand Bible (`./<Brand>_Brand_Bible_v2.txt`). Only the active brand.

Core Remotion rules (non-negotiable for correct renders):
- Animate only with `useCurrentFrame()` + `interpolate()` / `Easing`. CSS `transition` / `animation` and Tailwind animate classes do **not** render.
- Assets must live under `remotion/public/` and be referenced with `staticFile()`.
- Use `<Img>` from `remotion` for images, and `<Audio>` / `<Video>` from `@remotion/media`.

---

## 2. Workspace map

| What | Where |
|---|---|
| Remotion project | `remotion/` (Remotion 4.0.532, npm, TypeScript) |
| Register compositions | `remotion/src/Root.tsx` (put reels in a `<Folder name="Reels">`) |
| Reel code | `remotion/src/reels/<YYYY-MM-DD>_<brand>_<slug>/` |
| Reel assets (packs, cut-outs, stills, VO, music) | `remotion/public/reels/<YYYY-MM-DD>_<brand>_<slug>/` |
| Pipeline smoke test | Composition `SetupCheck` (`remotion/src/SetupCheck.tsx`) |
| Pack photos (source) | `C:\Users\arpit\Documents\storage\arpan organic\<caveman \| health fields \| pusht \| biomart \| greendipz>\` |
| Certification logos (Jaivik Bharat, APEDA, India Organic, PGS) | `C:\Users\arpit\Documents\storage\arpan organic\` (root) |
| Existing GPT stills (reusable as backgrounds/beats) | `research/prompts/assets/<date>_<brand>_<slug>/` |
| Post packages | `research/prompts/generated_<date>_<brand>_<slug>.md` |
| Final delivered reel | `research/prompts/assets/<date>_<brand>_<slug>/reel.mp4` (`reel_v2.mp4`, … on iterations) |
| Python tools env (Kokoro TTS + rembg) | `remotion/.tts/` (gitignored), run as `.tts/Scripts/python` from `remotion/` |
| Voiceover tool | `remotion/tools/voiceover.py` |
| Pack cut-out tool | `remotion/tools/cutout.py` |

Use the same `<date>_<brand>_<slug>` folder name across code, assets and the final delivery, so one reel is traceable end to end.

**Composition IDs** may only contain letters, numbers and hyphens. Use `reel-<date>-<brand>-<slug>`, e.g. `reel-2026-10-02-healthfields-pumpkin-seeds`.

---

## 3. Content Studio rules that still apply

These come from CLAUDE.md and apply to Remotion reels exactly as to Grok reels:

- **Protocol 2:** fetch the live product description yourself; never ask Puran to paste it.
- **Protocol 3 claims audit** on every on-screen line and every VO line before building.
- **Protocol 5:** no offers, codes or pricing in VO, on-screen text or caption unless Puran says so.
- **Protocol 10:** the end frame carries the quiet website CTA (e.g. `Shop now on biomart.in`). Under the NO DOTS rule, the CTA has no trailing period. The spoken CTA, if there is VO, is the last line.
- **Reel rules:** English-only VO and caption, hook in the first 2 seconds, and no hero product in the hook if the angle is ATTACK.
- **Known used reel products:** check the list in CLAUDE.md before choosing a product, and add the product once the reel is delivered.
- **Pack fidelity:** the pack is the real photo. You may move, scale (uniformly), fade or gently rotate it, or put it behind or in front of other layers. **Never** skew, stretch, perspective-warp, crop off part of the pack, recolour it, or put text over the label face. The full pack stays visible whenever it is the subject.
- Captions, hashtags and the rest of the 13-point package are produced as usual. Point 4 (Execution) describes the Remotion build instead of Grok. Point 7 GPT prompts are only needed if the reel uses GPT stills.

Grok-specific rules (the 10-section master brief, `Stays still:` lines, Aurora negatives, the 720p ceiling) do **not** apply. Remotion renders exactly what the code says.

---

## 4. Format and safe zones

- Default **1080×1920, 30 fps**, 9:16. Typical length 15–30s unless Puran says otherwise.
- Instagram Reels covers parts of the frame with UI. Keep key text and the CTA out of the **bottom ~20%** (caption and audio bar), the **top ~10%**, and the **right ~12%** (like, comment and share buttons).
- On-screen text must be readable in time: about 3 words per second, and headlines large enough at phone size (roughly 90px+ for headlines, 48px+ for supporting lines at 1080 wide).

---

## 5. Brand tokens (canonical, from the Brand Bibles)

Remotion renders exact hex values, so use the **canonical** colours. The values in CLAUDE.md's brand directory are Firefly/GPT prompt approximations.

| Brand | Primary | Supporting |
|---|---|---|
| Caveman Organic | Cave Red `#BE1A1A` | Deep Crimson `#8B0000`, Black `#000000` (always around the logo), White `#FFFFFF`, Cave Brown `#1A0A00` |
| Health Fields | Teal Green `#1A6B5A` | Organic Red `#C0392B`, Leaf Green `#2E8B57`, Sky Blue `#87CEEB`, White `#FFFFFF` (deep teal `#003C32` acceptable for backgrounds) |
| Pusht Organic | Forest Green `#1A5C1A` | Leaf Green `#2E8B2E`, Cream Ivory `#F5F0D0`, Wheat Gold `#8B6914`, White `#FFFFFF` |
| greendipz | Vivid Green `#1FAD10` | Chili Red `#CC2229`, Fresh Blue `#2E7FD4`, Mint Mist `#E9F9E6`, Deep Charcoal `#1A1A1A` |
| Biomart | Forest Green `#1B8A3E` | Organic Gold `#8B6427`, Mint Cream `#E8F5EC`, Warm Ivory `#FBF5E6`, Deep Charcoal `#1A1A1A` |

Re-check the active Brand Bible if anything here looks stale. The bible wins.

**Fonts:** the Brand Bibles do not define brand typefaces. Ask Puran, or propose one that fits the brand's GPT aesthetic anchor. Load Google Fonts with `npx remotion add @remotion/google-fonts`, or local `.woff2` files with `@remotion/fonts` (see `remotion-markup` → `google-fonts.md` / `local-fonts.md`). Never rely on system fonts.

---

## 6. Assets

**Packs.** Copy the chosen pack file(s) from the storage folder into `remotion/public/reels/<folder>/`. Never reference the storage folder directly: everything in `public/` is bundled, and storage holds large videos and PSDs. Front-of-pack is the preferred hero.

**Cut-outs.** Most catalogue packs sit on white. Make transparent PNGs:

```bash
cd remotion
.tts/Scripts/python tools/cutout.py "C:/Users/arpit/Documents/storage/arpan organic/health fields/pumpkin-seed-front.webp" --out public/reels/<folder>/packs
```

The default model `u2net` was tested best on Health Fields pouches (`isnet-general-use` cut away printed wood texture). Use `--method white` for simple pure-white studio shots. **Always inspect the cut-out on a dark background** before using it, by compositing with ffmpeg and reading the image.

**GPT stills.** Any existing or new GPT Image still can be used as a background or a beat. Copy it into `public/reels/<folder>/`.

---

## 7. Voiceover (Kokoro, free, Apache-2.0, commercial use OK)

Write the lines as JSON (any keys, in order), then run:

```bash
cd remotion
.tts/Scripts/python tools/voiceover.py --script public/reels/<folder>/vo.json --out public/reels/<folder>/vo --voice af_heart --ts src/reels/<folder>/vo-timings.ts
```

- Output: one `<key>.wav` per line, normalized to -16 LUFS. `timings.json` holds each line's duration and **word start/end times**, and `--ts` writes the same data as a TypeScript module the reel can import.
- **Voices:** `af_heart` (best overall, warm female), `af_bella`, `bf_emma` (UK female), `am_michael`, `am_fenrir` (deep), `am_puck`; `bm_george` was disliked on another project. Use `--lang b` for British voices. To audition, render the same lines with several voices into separate `--out` folders and send the WAVs.
- **Pronunciation fixes** use inline phonemes: `[SEO](/ˌɛsˌiˈO/)`, `[demos](/ˈdɛmOz/)`, `[AI](/ˌAˈI/)`, `[iOS](/ˌIˌOˈɛs/)`. Brand names and Hindi food words often need one; ask Puran how they're said.
- **Sync technique (optional, strongly recommended):** derive reveal frames from the word timings, e.g. `lineStart + Math.round(VO.key.words[i].start * fps)`, so on-screen words appear as they're spoken and regenerating the VO re-syncs the reel automatically.
- Kokoro output varies by a few milliseconds between runs. That's harmless if timings are always read from the generated file.

---

## 8. Music and SFX

- Free commercial source: **Pixabay Music** (no attribution required). **Ask Puran before downloading**, and name the track, source and approximate size. If `curl` returns 403, send a browser user agent with `-e https://pixabay.com/` as the referer.
- Save to `public/reels/<folder>/audio/` and write `LICENSE-music.txt` there (track, artist, URL, license, date).
- To land cuts on the music, measure loudness every second with ffmpeg (`asetnsamples=48000,astats=metadata=1:reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level`). That shows where drums enter and where the track ends; then use `trimBefore` on `<Audio>`.
- When there's VO, duck the music (about 0.5 between lines, about 0.2 under speech) with a `volume` callback. Target -14 to -16 LUFS overall.

---

## 9. Preview, render, verify, deliver

```bash
cd remotion
npx tsc --noEmit                                   # type-check
npm run dev                                        # Remotion Studio preview (browser)
npx remotion render <composition-id> out/<folder>.mp4
```

**Verify before delivering:**
- Pull frames with `ffmpeg -ss <t> -i out/<folder>.mp4 -frames:v 1 -vf scale=360:-1 <png>`, tile them into a contact sheet (`-vf tile=4x5`) and read it. Check the hook frame, the pack beats (label sharp, full pack visible), text inside the safe zones, and the end-frame CTA.
- Loudness: `ffmpeg -i out/<folder>.mp4 -af ebur128=peak=true -f null -`.

**Deliver:**
1. Copy the render to `research/prompts/assets/<folder>/reel.mp4` (`reel_v2.mp4`, … for iterations; keep every version).
2. `SendUserFile` with a caption: brand + date + angle + what to check.
3. Update the post package `.md` and the known used reel products list in CLAUDE.md.

---

## 10. Gotchas (Windows, this machine)

- Paths contain spaces (`C:\NITRO 4 BACKUP\...`, `...\arpan organic\health fields\`): always quote them.
- ffmpeg's `drawtext` filter crashes here (Fontconfig error). Build contact sheets without text labels.
- Run ffmpeg `loudnorm` as its own step before mixing. Inside a larger filter graph it breaks MP3 timestamps.
- `getPointAtLength` from `@remotion/paths` is typed as possibly `null`, so give it a fallback.
- The Python tools need the `remotion/.tts` interpreter (CPython 3.11). Don't use the global Python, which belongs to another app's virtual environment.
- `.tts/` is gitignored. To rebuild it: `py -V:Astral/CPython3.11.15 -m venv .tts`, then `pip install torch --index-url https://download.pytorch.org/whl/cpu`, `pip install "kokoro>=0.9.4" soundfile "rembg[cpu]"`.

## 11. Licence note

Remotion is free for individuals and companies with **up to 3 people**. If the company producing these reels is larger, it needs a Remotion company licence (remotion.pro/license). Raise this with Puran before the reels are used commercially at scale.

# Reel Production — Dual-Track Workflow v5
Content Studio 3.2 · Protocol 8 v5 · effective 2026-08-16

Two video generation tools in rotation: **Google Flow** (Veo 3.1) and **Grok Imagine** (Aurora / Agent Mode). Every reel gets routed to one track based on the criteria below. Stages 1–2 (GPT Image 2.0 stills) and the 13-point package are identical across both tracks. Stages 3–4 differ.

---

## Track decision — first line of every reel package

At the top of every reel Point 4 (Execution), state one of:

- **Track: FLOW** — [one-line rationale]
- **Track: GROK** — [one-line rationale]

### Decision criteria

| Reel type | Track | Reason |
|---|---|---|
| Pack-heavy EDUCATE (HF clinical wellness, Biomart curation, Pusht editorial) | **FLOW** | Label fidelity + color world consistency + visual quality bar. Veo 3.1 anchors to reference image, prevents label warp. |
| Text-heavy reels where typography needs to stay sharp across motion | **FLOW** | Veo 3.1 holds baked type without drift better than Aurora. |
| Any brand-authority CONVERT reel where visual polish matters more than turnaround | **FLOW** | Trade CapCut work for quality. |
| Same-day turnaround reels | **GROK** | Agent Mode auto-stitches + auto-composes VO/SFX/music. One brief in, one MP4 out. |
| Caveman Gen Z rough, greendipz fast cuisine cuts | **GROK** | Aurora's "floaty" motion suits the rougher aesthetic; auto-audio saves a day. |
| Reels where the VO/SFX/music track needs to feel improvised rather than composed | **GROK** | Agent Mode's synced audio is naturalistic; Flow needs external VO layering. |
| Puran's Flow limit is at cap for the week | **GROK** | Practical fallback. |
| Puran's Grok limit is at cap for the week | **FLOW** | Practical fallback. |

Default routing when in doubt: **FLOW** for HF + Biomart + Pusht editorial; **GROK** for Caveman + greendipz + any RELATE lifestyle.

---

## Shared stages (both tracks)

### Stage 1 — GPT Image 2.0 stills
Unchanged from Protocol 8 v4.1. Build every still as a Protocol 6 prose prompt. Bake all on-screen text into the stills (hooks, headers, callouts, CTA). Upload pack reference photo for every still featuring the product. Output as prompt files (`codex-image-gen` skill) or copy-paste to ChatGPT if codex unavailable.

### Stage 2 — Still review
Puran uploads generated stills. Verify composition, text legibility at feed thumbnail scale, pack shape fidelity, colour world consistency. Flag stills needing v2. Only proceed to Stage 3 when all stills approved.

---

## FLOW track — Stages 3–4

### Stage 3a — Storyboard pre-pass (conditional — skip when GPT stills exist)

**Skip this stage entirely when Stage 1 has produced approved GPT Image 2.0 stills for every beat.** The stills ARE the storyboard, and they are more accurate than anything Flow would draft because they are anchored to real pack references. Running a Flow storyboard on top of finished stills wastes a render and risks introducing pack drift we would then have to fight in Stage 3b. Go straight to Stage 3b per-beat prompts.

**Run this stage only when you are going straight to Flow with no upstream stills** (e.g. a fast-turnaround reel where you skipped GPT Image 2.0 for pace reasons). In that case, per [[feedback_flow_storyboard_first]], ask Flow for a 6-panel storyboard from the prose reel brief before generating video. Prefix the brief with:

> First generate a 6-panel storyboard from this brief showing the key beats — do not generate the video yet. Storyboard panels 1–6, numbered, on a single sheet.

Review the storyboard for pack accuracy, pacing beats, color world consistency, hero moments, CTA typography. Regenerate the storyboard if beats are off — cheap iteration compared to full video re-render.

### Stage 3b — Per-beat Flow prompts (Scenebuilder)
Instead of Grok's single master brief, Flow needs **N prompts, one per beat**. Each prompt uploads the corresponding GPT still as the Ingredients-to-Video reference image (Veo 3.1 accepts up to 3 refs — use GPT still + pack ref + optional style board).

Per-beat prompt shape (Protocol 8 v4.1 block, adapted for Flow):

```
[Beat name — duration]
Visual: [what animates forward from this still, one clear moment]
Camera: [one explicit command: locked off / very slow push-in stopping before [X] / etc — with speed and endpoint]
Stays still: [what must NOT move — pack label, baked headline, callouts, background]
Reference image: [GPT still filename]
Style: [Health Fields cream + deep teal / brand style-tag cluster close]
Aspect: 9:16, [duration]s
```

Flow's Scenebuilder chains the beats inside one project — use "Extend" between shots to preserve continuity from the last frame of the previous clip.

### Stage 3c — Render each clip
Flow outputs one 4–8s (Veo 3.1 Lite) or up to 30s (Veo 3.1 full) MP4 per beat. Download each. Do not restitch inside Flow.

### Stage 4 — CapCut assembly (Flow track — expanded)
- Stitch clips in Grok's beat order using **hard cuts** — no dissolves, no whip transitions, no cross-fades
- Record or generate VO in ElevenLabs / CapCut TTS / phone recording — must be dominant channel, English, deliver the spoken CTA as the last line
- Pull music bed from CapCut library — instrumental, no vocals, mood-matched to brand lane (per each reel package's Point 4)
- Layer SFX only if a beat's Visual line calls for a specific sound
- Ducking: music -18dB relative to VO
- Logo watermark: brand mark top-right corner, small (~5% frame width), quiet
- Export 1080×1920, MP4, H.264
- Estimated CapCut time: 20–40 min per reel

---

## GROK track — Stages 3–4 (unchanged from Protocol 8 v4.1)

### Stage 3 — Single master brief + all stills to Agent Mode
Upload all stills to Grok Imagine web canvas in beat order. Paste the 10-section master brief (per Protocol 8 v4.1 spec: reel intent, still-to-beat map, palette lock, editing logic, per-beat timeline, global audio, locked CTA beat, packaging protection clause, negatives, style-tag close). Agent Mode animates + transitions + stitches + composes VO + SFX + music + outputs one MP4.

### Stage 4 — CapCut finishing (Grok track — minimal)
- Logo watermark
- Music polish or swap if the Agent's bed isn't right for the brand lane
- Auto-captions if VO isn't crisp
- Export 1080×1920
- Estimated CapCut time: 5–10 min per reel

---

## Format specs (both tracks)

- Aspect: 9:16 (1080×1920 export)
- Duration: 15–22s optimal
- Pacing: minimum 2s per beat, maximum 5s per beat
- Hook in first 2s — visual + VO + baked text hit together
- 3-Act: Visual Hook → Escalation → Website CTA
- VO: English, dominant channel, delivers CTA as last spoken line
- CTA: baked into final still + spoken by VO
- No offers, codes, pricing in reel captions or baked text unless Puran explicitly says so

---

## What changes in the 13-point package

| Point | Change |
|---|---|
| Point 4 (EXECUTION) | Add "Track: FLOW" or "Track: GROK" line with one-line rationale before the execution paragraph |
| Points 6–7 | Unchanged — same in-image text review table, same GPT prompts, same pack ref uploads |
| Point 8 (CAPTION) | Unchanged |
| Point 10 (WEBSITE CTA) | Unchanged |
| Point 11 (VARIATION) | Unchanged |
| Point 13 (BUNDLING) | Unchanged |
| Stage 3 output block | If FLOW: 6-panel storyboard instruction + N per-beat Flow prompts + Stage 4 CapCut checklist. If GROK: single 10-section master brief + minimal Stage 4 checklist |

---

## Known used reel products — never reuse
Same list as Protocol 8 v4.1 — track-agnostic. See CLAUDE.md `KNOWN USED REEL PRODUCTS` section.

---

## Validated examples
- **HF A2 Desi Cow Ghee reel (2026-08-16)** — first Flow-track shipment. GPT stills → Flow Ingredients-to-Video → CapCut assembly. Assets at `research/prompts/assets/2026-08-16_healthfields_a2-ghee-reel/`
- **Biomart × Pusht cold-pressed sesame oil cut (2026-07-24)** — original Flow storyboard-first validation, per [[feedback_flow_storyboard_first]]

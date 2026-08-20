# Grok Aurora Animation Prompts — greendipz Chilli Gravy Reel
**Date:** 2026-07-19
**Brand:** greendipz
**Product:** Chilli Gravy Sauce 240g (lead) + Manchurian + Kung Pao trio
**Reel angle:** CONVERT — "Sunday, sorted. One bottle."
**Format:** 9:16 vertical (1080×1920)
**Total runtime:** ~26 seconds
**Stack:** GPT Image 2.0 stills → **Grok Aurora animation** → CapCut assembly → Canva logo overlay

---

## INSTRUCTIONS FOR CODEX

1. **Feed each approved GPT still into Grok Aurora as the reference frame.** Grok animates the still — it does not generate the visual from scratch. Upload the correct still before running each prompt.
2. **6-second maximum per clip.** Never exceed. If a beat needs longer, split into two 6s clips and cross-fade in CapCut.
3. **Never animate baked-in GPT text.** The word SUNDAY, ONE BOTTLE, THAT'S IT, CHILLI GRAVY, OR ANY OF THESE, SUNDAY SORTED, and the biomart.in CTA — Grok animates the CARD (the whole frame), not the letters. If Grok tries to redraw text, restart.
4. **Bottle rotations are RIGID.** Bottles never deform. Rotation happens around the vertical axis of the jar, glass and label move as one unit at identical velocity.
5. **WHAT MUST NOT MOVE lock list is mandatory in every prompt.** Explicitly name what stays still.
6. **Physics specs are mandatory:** travel distance in px, duration in seconds, easing type, settle behaviour, bounce (zero or explicit px).
7. **Assemble the six clips in CapCut in F1→F6 order.** Add voiceover (English only), SFX, auto-captions.

---

## VOICEOVER SCRIPT (English only — CapCut layer, not baked)

| Frame | VO line |
|---|---|
| F1 (0–2s) | "Sunday." |
| F2 (2–6s) | "One bottle." |
| F3 (6–12s) | "That's it." |
| F4 (12–17s) | "Chilli Gravy." |
| F5 (17–22s) | "Or any of these." |
| F6 (22–26s) | "Sunday, sorted. Shop on biomart-dot-in." |

---

## F1 — SUNDAY (0–2s)

**Reference still:** approved F1 (red bg + white plate + chopsticks + giant SUNDAY type + greendipz corner mark).

```
SUBJECT: A single empty white ceramic plate with wooden chopsticks resting diagonally across it, floating dead-centre on a saturated cadmium-red background. Giant white display word SUNDAY sits behind and around the plate, plate occluding the middle letters.

ACTION: The plate rotates clockwise 5 degrees over 1.2 seconds with a soft ease-out, then holds still for 0.8 seconds. The chopsticks tap the rim once at the 0.4-second mark — a tiny 3px vertical bounce, hard-settle, zero bounce after settle. Camera holds locked-off. No zoom, no push-in.

CAMERA: Locked off. No movement.

STYLE: Modern hot-sauce brand ad, bold single-hex world, McDonald's motion-poster confidence.

MOOD: Anticipation. The plate is empty and waiting.

PHYSICS SPECS:
- Plate rotation: 5 degrees clockwise over 1200ms, ease-out, hard-settle, zero-bounce
- Chopstick tap: 3px vertical drop over 100ms at t=0.4s, hard-settle, zero-bounce
- SUNDAY type: absolute stillness — do not animate letters

WHAT MUST NOT MOVE:
- The giant SUNDAY word (baked type, no letter animation of any kind — no scale, no jitter, no fade)
- The red background (no atmosphere, no gradient shift)
- The greendipz corner mark
- The camera

Duration: 2 seconds. Aspect: 9:16 vertical, 1080x1920.
```

---

## F2 — ONE BOTTLE (2–6s)

**Reference still:** approved F2 (red bg + upright Chilli Gravy bottle + 5 chillies at 3 depths + giant ONE BOTTLE two-line type).

```
SUBJECT: An upright greendipz Chilli Gravy Sauce jar dead-centre on a saturated cadmium-red background, with five dried red Kashmiri chillies floating around it at three different depths (two foreground, two mid, one background). Giant white display headline ONE BOTTLE sits behind, jar occluding the middle of the word BOTTLE.

ACTION: The jar drifts gently upward 8px and back down 8px over the full 4-second clip (subtle floating hover, ease-in-out both directions, no bounce). The five chillies parallax slowly — foreground chillies drift downward at 25 px/second in a lazy diagonal, mid-depth chillies drift downward at 15 px/second, background chilli drifts downward at 8 px/second. All chillies rotate slightly around their own centres at 3 degrees per second. Camera holds locked-off.

CAMERA: Locked off. No movement.

STYLE: Modern hot-sauce brand ad, floating hero, Polo Sauces geometry.

MOOD: Confident reveal. The product enters and owns the frame.

PHYSICS SPECS:
- Jar hover: 8px vertical amplitude, 4-second sinusoidal cycle, ease-in-out
- Chilli parallax (foreground): 25 px/s downward, 3 deg/s rotation
- Chilli parallax (mid): 15 px/s downward, 3 deg/s rotation
- Chilli parallax (background): 8 px/s downward, 3 deg/s rotation
- Chillies exit bottom of frame naturally — do not respawn or loop
- ONE BOTTLE type: absolute stillness

WHAT MUST NOT MOVE:
- The giant ONE BOTTLE headline (baked type, zero animation)
- The red background
- The jar's label details (glass and label are rigid — no deformation, no shimmer, no text warp on the pack)
- The camera

Duration: 4 seconds. Aspect: 9:16 vertical, 1080x1920.
```

---

## F3 — THAT'S IT (6–12s)

**Reference still:** approved F3 (burgundy bg + horizontal Chilli Gravy jar with lid off + sauce ribbon arc from open mouth to paneer plate + THAT'S IT slab).

```
SUBJECT: A horizontal greendipz Chilli Gravy Sauce jar in the upper-left of the frame with its lid removed and open mouth facing down-right. A single sweeping ribbon of thick glossy deep-red chilli gravy sauce emerges directly from the open jar mouth and arcs down-right onto a white ceramic plate of sesame-glazed paneer cubes in the lower-right. Giant white display slab THAT'S IT sits behind the pour. Background is deep burgundy red.

ACTION: The sauce ribbon flows continuously along its existing arc path — the ribbon animates as flowing liquid moving from jar mouth to plate at a constant 180 px/second along the curve, sauce landing on the plate creates a subtle ripple every 0.8 seconds (3px amplitude, hard-settle). The jar wobbles very slightly on its horizontal axis (2-degree oscillation over 2-second cycle, ease-in-out) as if held by an unseen hand. The paneer cubes glisten with a subtle specular highlight shift.

CAMERA: Slow push-in on the plate — start at 100% scale, end at 105% scale over 6 seconds, ease-in-out. Very subtle.

STYLE: Hot Jiang chili oil thirst-trap energy, hero pour macro, single-hex world.

MOOD: Payoff. The bottle delivers on its promise.

PHYSICS SPECS:
- Sauce ribbon flow: 180 px/s along the arc path, continuous unbroken stream
- Sauce landing ripple: 3px amplitude every 800ms, hard-settle, zero-bounce
- Jar wobble: 2 deg oscillation, 2-second cycle, ease-in-out
- Camera push-in: 100% to 105% over 6000ms, ease-in-out
- THAT'S IT type: absolute stillness

WHAT MUST NOT MOVE:
- The giant THAT'S IT slab (baked type, zero animation)
- The burgundy background
- The jar's label details (rigid glass + label, no text warp)
- The connection point between the jar mouth and the sauce ribbon origin — the sauce must stay physically attached to the mouth throughout, no floating gap forming
- The plate position on the frame

Duration: 6 seconds. Aspect: 9:16 vertical, 1080x1920.
```

---

## F4 — CHILLI GRAVY (12–17s)

**Reference still:** approved F4 (burnt-orange bg + overhead plate of chilli paneer + CHILLI top / GRAVY bottom wrapping the plate + 3 dried chillies scattered + greendipz corner mark).

```
SUBJECT: A round white ceramic plate photographed dead top-down, holding a generous serving of chilli paneer stir-fry with sesame and spring onion garnish, floating dead-centre on a saturated burnt-orange background. Giant white display headline CHILLI wraps above the plate and GRAVY wraps below. Three dried red Kashmiri chillies scattered at three depths on the background.

ACTION: Thin wisps of steam rise from the plate — 3 to 4 soft steam trails drifting upward at 40 px/second, fading out at 60% frame height. The sauce sheen on the paneer shimmers subtly with a slow specular highlight shift left-to-right over the full 5 seconds. The three dried chillies drift slowly: foreground chilli drifts down-right at 12 px/second, mid chilli holds still, background chilli drifts up-left at 8 px/second. Plate holds locked centred.

CAMERA: Very subtle push-in on the plate — 100% to 103% scale over 5 seconds, ease-in-out.

STYLE: Perdue meal-flatlay editorial, appetite-first food photography, single-hex world.

MOOD: Delivery. The dish is real, the promise is proven.

PHYSICS SPECS:
- Steam wisps: 40 px/s upward, fade at 60% frame height, 3-4 wisps at staggered emit times
- Sauce sheen: specular highlight shift left-to-right over 5000ms, ease-in-out
- Foreground chilli drift: 12 px/s down-right diagonal
- Background chilli drift: 8 px/s up-left diagonal
- Mid chilli: static
- Camera push-in: 100% to 103% over 5000ms, ease-in-out
- CHILLI and GRAVY type: absolute stillness

WHAT MUST NOT MOVE:
- The giant CHILLI and GRAVY headlines (baked type, zero animation)
- The burnt-orange background
- The plate position (centred, no drift)
- The greendipz corner mark

Duration: 5 seconds. Aspect: 9:16 vertical, 1080x1920.
```

---

## F5 — OR ANY OF THESE (17–22s)

**Reference still:** approved F5 (burgundy bg + three greendipz jars in a straight row: Chilli Gravy / Manchurian / Kung Pao + giant OR ANY OF THESE type).

```
SUBJECT: Three greendipz sauce jars standing upright in a straight horizontal row on a deep burgundy-red background. Left to right: Chilli Gravy (peach label), Manchurian (teal-cyan label), Kung Pao (large dark-brown torn-paper banner covering upper 40% of label). Giant white display headline OR ANY OF THESE sits above the row across the top third.

ACTION: All three jars rotate slowly in place around their own vertical axis, rigid rotation as one unit each (glass + label as one solid object). Left jar rotates clockwise 8 degrees over 5 seconds, ease-in-out. Centre jar rotates counter-clockwise 8 degrees over 5 seconds, ease-in-out. Right jar rotates clockwise 8 degrees over 5 seconds, ease-in-out. Rotation is subtle — the labels stay mostly visible throughout, never turning past the label edge. All three jars hover gently 5px up and down over the full clip in unison.

CAMERA: Locked off. No movement.

STYLE: Editorial lookbook range reveal, three-hero shot, single-hex world.

MOOD: Options. The one bottle idea expands to the full range.

PHYSICS SPECS:
- Jar rotation: 8 deg over 5000ms, ease-in-out, each jar rotating around its own vertical axis
- Left jar: clockwise
- Centre jar: counter-clockwise
- Right jar: clockwise
- Jar hover: 5px vertical amplitude in unison, 5-second cycle, ease-in-out
- OR ANY OF THESE type: absolute stillness

WHAT MUST NOT MOVE:
- The giant OR ANY OF THESE headline (baked type, zero animation)
- The burgundy background
- Any jar's label details — labels are rigid, no deformation, no text warp on any pack, no colour shift, no swap between jars
- The relative spacing between the three jars (they rotate in place, do not drift horizontally)
- The camera

Duration: 5 seconds. Aspect: 9:16 vertical, 1080x1920.
```

---

## F6 — SUNDAY, SORTED end-card (22–26s)

**Reference still:** approved F6 (charcoal bg + three greendipz jars in equilateral triangle: Manchurian centre-front, Chilli Gravy upper-left, Kung Pao upper-right + SUNDAY, SORTED kicker top + Shop now on biomart.in CTA bottom).

```
SUBJECT: Three greendipz sauce jars arranged in a tight equilateral triangle on a deep near-black charcoal background. Manchurian jar at centre-front slightly lower, Chilli Gravy jar upper-left slightly higher, Kung Pao jar upper-right slightly higher. Warm rim-light catches the left edge of each glass jar. Small kicker SUNDAY, SORTED at very top. Small CTA line Shop now on biomart.in at bottom third.

ACTION: The three jars hold nearly still with only a very subtle breathing scale — all three jars pulse from 100% to 101% scale and back over a 4-second cycle, ease-in-out, in unison. The warm rim-light on each jar's left edge shimmers subtly — specular highlight shifts vertically over 4 seconds, ease-in-out. The Shop now on biomart.in CTA line at the bottom fades in from 0% opacity to 100% opacity over the first 1.5 seconds of the clip, then holds solid for the remaining 2.5 seconds. Camera holds locked.

CAMERA: Locked off. No movement.

STYLE: Fear of God Essentials lookbook end-card, premium range reveal, dark-hex world.

MOOD: Quiet conclusion. Confident sign-off.

PHYSICS SPECS:
- Jar breathing scale: 100% to 101% and back, 4000ms cycle, ease-in-out, all three in unison
- Rim-light shimmer: vertical specular shift over 4000ms, ease-in-out
- CTA fade-in: 0% to 100% opacity over 1500ms at start, ease-in
- CTA hold: solid at 100% from t=1.5s to t=4s
- SUNDAY, SORTED kicker and Shop now on biomart.in CTA text: absolute stillness after fade-in completes — no letter animation, no bounce, no scale on the text itself

WHAT MUST NOT MOVE:
- The SUNDAY, SORTED kicker text (baked type, zero letter animation)
- The Shop now on biomart.in CTA text after fade-in completes (no letter animation, no bounce)
- The charcoal background
- Any jar's label details (rigid glass + label, no text warp)
- The triangle formation — all three jars breathe in place, do not drift
- The camera

Duration: 4 seconds. Aspect: 9:16 vertical, 1080x1920.
```

---

## CAPCUT ASSEMBLY NOTES

1. Import all six 9:16 clips in order F1 → F6.
2. Add English voiceover per the script above — one line per frame, delivered at the timing shown in the header.
3. SFX to layer:
   - F1: light plate-rattle at 0.4s
   - F2: subtle whoosh as jar enters (start of clip)
   - F3: sauce pour SFX (continuous) + soft splash at ribbon landing
   - F4: kitchen ambience (soft) + fork-plate clink at 0.5s
   - F5: light glass clink as jars settle
   - F6: quiet end-card ambient hum, no percussive SFX
4. Auto-caption in English only, positioned bottom third, sans-serif, chalk-white with subtle drop-shadow — must not clash with any baked GPT type.
5. No music that fights the VO. Sub-bass warmth for F1-F3, brighter for F4-F5, quiet for F6.
6. Export: 1080×1920 MP4, 30fps, H.264, bitrate high enough for saturated colour retention (no banding on the red or burgundy backgrounds).

---

## KNOWN RISKS TO WATCH IN STAGE 4 (CAPCUT REVIEW)

- **F3 sauce ribbon detachment** — if Grok breaks the connection between jar mouth and sauce origin, restart. This is the reel's hero shot.
- **F5 jar rotation over-rotating** — if any jar rotates past its label edge and shows the back of the label, restart with a smaller rotation degree.
- **F6 CTA text animation** — if Grok tries to letter-animate the biomart.in line, restart. Text stays absolutely still.
- **Colour banding on saturated backgrounds** — export bitrate must be high enough for the reds and burgundies to hold without visible banding.

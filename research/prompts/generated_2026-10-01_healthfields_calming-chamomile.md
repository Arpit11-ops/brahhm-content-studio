# Health Fields · Calming Chamomile · "your 9pm cup" · Remotion Reel

PRE-FLIGHT ✅ Skills read this session: humanizer-main/SKILL.md, social/SKILL.md, copywriting/SKILL.md, copy-editing/SKILL.md, video/SKILL.md, remotion-reels/SKILL.md, remotion-best-practices (markup + create), ab-testing/SKILL.md, cro/SKILL.md, codex-image-gen/SKILL.md

- **Brand:** Health Fields (@healthfieldsorganic)
- **Product:** HealthFields Organic Calming Chamomile, Herbal Infusion Tea, Caffeine Free, 25 Tea Bags
- **Format:** Instagram Reel, 9:16, 1080×1920, 30fps, 24.6s, built in Remotion (first Remotion reel in the studio)
- **Reference:** Goli Superfruits motion ad (`C:\Users\arpit\Videos\images\f4bcfe46da960d0a8e830c75337cb414.mp4`), structure adapted
- **Final file:** `research/prompts/assets/2026-10-01_healthfields_chamomile-9pm-cup/reel_v2.mp4` (v1 kept alongside)
- **Code:** `remotion/src/reels/2026-10-01_healthfields_chamomile-9pm-cup/` · composition `reel-2026-10-01-healthfields-chamomile-9pm-cup`
- **Suggested slot:** Peak evening, 7:30–8:00 PM IST (lands just before the 9pm moment the reel names)

---

## Protocol 2 · Source

- Description: live biomart.in product page (`/products/healthfields-organic-calming-chamomile-herbal-infusion-tea-caffeine-free-25-tea-bags`), fetched 2026-10-01
- Ingredients: from the pack, supplied by Puran: Organic Chamomile (80%), Organic Fennel (10%), Organic Rose (6%), Organic Licorice (4%)
- Pack image: Biomart Shopify CDN original `OrganicCalmingChamomileTea01.jpg` (3000×3000), downloaded with Puran's approval and also saved to `storage\arpan organic\health fields\OrganicCalmingChamomileTea01_hires.jpg`

## Protocol 3 · Claims audit

| Claim | Source | Verdict | Action |
|---|---|---|---|
| Organic chamomile, fennel, rose, licorice | Pack | ✅ | KEEP (names only, no percentages on screen) |
| Caffeine free | Pack + biomart.in | ✅ | KEEP |
| Made with 100% unbleached paper (tea bags) | Pack + biomart.in | ✅ | KEEP |
| Certified organic (USDA Organic, IMO, PGS-India marks on pack) | Pack | ✅ | KEEP |
| 0% colours | Pack badge | ✅ | KEEP as "No added colours" |
| 25 infusion bags | Pack | ✅ | KEEP (caption only) |
| Steep 3–5 minutes | biomart.in | ✅ | KEEP (caption only) |
| Gentle floral aroma, mild taste | biomart.in | ✅ | KEEP (sensory, not a health claim) |
| Since 2003 | Pack | ✅ | KEEP (brand fact) |
| Promotes relaxation, reduces stress, supports better sleep | biomart.in | ❌ | REMOVE (therapeutic) |
| "Naturally calming experience", "premium chamomile flowers", "pure goodness", "perfect companion" | biomart.in | ❌ | REMOVE (vague or unverified) |

"Calming" appears only as part of the product name, never as a promise.

---

## 1. CONTENT ANGLE
EDUCATE · RELATE (ingredient transparency, framed around a familiar evening moment)

## 2. IDEA TITLE
Your 9pm cup: what's actually in it

## 3. HOOK
What goes into your 9pm cup? (6 words, spoken + typed on in the first 2.3s)

## 4. EXECUTION (Remotion build)

| Time | Beat | What happens |
|---|---|---|
| 0–3.0s | Hook | "What goes into" appears word by word in sync with the VO, "your 9pm cup" types on letter by letter, the pack drops in tilted and settles upright |
| 3.0–10.8s | Ingredients | Deep lilac iris with sunburst ticks opens on the ingredient. "Steeped from" curves on the ring. Hand-drawn labels with drawn arrows swap CHAMOMILE → FENNEL → ROSE → LICORICE (1.8s each), each name voiced the moment it appears. "in every bag" below |
| 10.8–16.8s | Facts | Pack slides in from the right. Curved Fraunces headline wipes through Unbleached paper bags → No added colours → Certified organic. Licorice, rose, fennel and chamomile float in the corners |
| 16.8–19.6s | Zero caffeine | "And" → "ZER" pops in → a chamomile flower spins in as the O → "caffeine" |
| 19.6–24.6s | End card | Iris opens to the HF logo, handwritten "your 9pm cup", full pack with flowers at its base, "Available on healthfields.in" |

**Production stack**
- **Packs:** real pack photo, cut out with `remotion/tools/cutout.py` (u2net), moved and scaled only (never warped or covered)
- **Ingredients:** 4 isolated renders from Codex (gpt-image-2.5-flare). Fennel was re-rendered (v1 read as cardamom). Chamomile was re-rendered on a dark background (white-on-white cut-out bit holes in the petals), then edge-cleaned. Prompts are in the session scratchpad; originals in `assets/.../ingredients/`
- **Logo:** `health-fields.com_Logo.jpg` (already transparent, 254×130), shown at native size on the end card only
- **VO:** Kokoro `hf_alpha` (Indian female voice, US English pronunciation rules), chosen after a 5-voice Whisper-checked audition. "Calming" is forced with phoneme `/kˈɑlmɪŋ/` (the voice was dropping the l under music)
- **Music:** "Calm - Carefree_28Sec" by Folk_Tales (Pixabay Content License, no vocals confirmed with Whisper). Trimmed 2.98s so its natural fade-out ends on the last frame. Ducked to 0.14 under speech, 0.5 between lines
- **Fonts:** Fraunces (headlines), Manrope (support + CTA), Amatic SC (ingredient labels), Caveat (handwritten accent)
- **Colour world:** soft lilac + cream (matches the pack), HF Teal Green `#1A6B5A` for all type and the CTA
- **Verification:** contact sheets checked for safe zones, pack visibility and CTA. Loudness -14.8 LUFS integrated. Whisper transcript of the final mix matches the script word for word

## 5. VISUAL DIRECTION
Goli-style pack-matched monochrome world: lilac/cream radial background, white concentric hairline rings, lilac zigzag border top and bottom, real cut-out pack and ingredients with soft lilac drop shadows, iris transitions in deep lilac. All text sits outside the IG UI zones (top 10%, bottom 20%, right 12%).

## 6. ON-SCREEN TEXT (confirmed)

| Element | Text | Style | Position |
|---|---|---|---|
| Hook line 1 | What goes into | Manrope 600, 66px, teal | Upper third |
| Hook line 2 | your 9pm cup | Fraunces 700, 132px, teal, typed on | Under line 1 |
| Ingredient arc | Steeped from | Manrope 600, 62px, curved | Above the ingredient |
| Ingredient labels | CHAMOMILE · FENNEL · ROSE · LICORICE | Amatic SC 700, 120px + drawn arrow | Upper left / right, alternating |
| Ingredient sub | in every bag | Manrope 600, 52px | Below the ingredient |
| Fact arc | Unbleached paper bags → No added colours → Certified organic | Fraunces 700, 72px, curved | Above the pack |
| Fun beat | And · ZER✿ · caffeine | Manrope 70px / Fraunces 900 250px / Fraunces 700 130px | Centre |
| End accent | your 9pm cup | Caveat 700, 92px, tilted | Upper left of the pack |
| CTA | Available on healthfields.in | Manrope 500, 54px, teal | Just above the bottom 20% |

No full stops or exclamation marks on any on-screen line.

**Voiceover (hf_alpha):** "What goes into your 9pm cup? Chamomile. Fennel. Rose. Licorice. Unbleached paper bags. No added colours. Certified organic. And zero caffeine. Calming Chamomile, on healthfields dot in."

## 7. GPT IMAGE PROMPT
Not used. The reel is code-built from the real pack photo. The four ingredient stills were rendered with Codex (prompts in the session scratchpad: `hf_chamomile_ing_*.txt`).

## 8. CAPTION

Humanizer audit: cut "Not just a tea, it's a ritual" (negative parallelism → replaced with the plain fact that there are four ingredients), cut "pure, gentle and soothing" (rule of three, and "soothing" smuggles in a therapeutic claim → replaced with "mild and floral" from the product page), cut "the perfect companion for your evenings" (promotional filler → replaced with the specific "the hour when coffee is off the table").

What goes into your 9pm cup? 🌼

Four things. Chamomile, fennel, rose and licorice, and that's the whole list.

Our Calming Chamomile has no caffeine, which matters at the hour when coffee is off the table. The tea bags are unbleached paper and there are no added colours.

Steep one bag for 3 to 5 minutes. It comes out mild and floral, and a spoon of Rozana Forest Honey goes in nicely if you take it sweet.

Available on healthfields.in

#HealthFields #ChamomileTea #NightRitual

## 10. WEBSITE CTA
- **In-reel CTA:** "Available on healthfields.in" (end card, Manrope 500, teal, above the bottom safe zone, no full stop)
- **Spoken CTA:** "Calming Chamomile, on healthfields dot in." (last line of the VO)
- **Caption CTA:** Available on healthfields.in
- **Link to use (CRO, the product page that matches the reel):** healthfields.in/products/healthfields-organic-calming-chamomile

## 11. VARIATION

Hypothesis (ab-testing): because HF's audience reads labels before buying (brand bible: "won't accept natural without certification"), a label-reading hook will drive more saves than the 9pm-moment hook. Primary metric: saves per 1,000 plays. Secondary: profile visits, link taps. Change only the caption; the reel stays the same.

Humanizer audit: cut "Transparency you can taste" (sloganish AI cadence → replaced with "That's the whole label"), cut "carefully selected premium ingredients" (vague superlative copied from the listing → replaced with the four named ingredients in pack order), cut "trusted by families for over two decades" (unprovable social proof → replaced with the checkable "Since 2003" and the named certification marks).

Flip your night tea box over.

Ours lists four ingredients. Chamomile first, then fennel, rose and licorice. That's the whole label.

No caffeine, no added colours, and the tea bags are unbleached paper. The box carries the USDA Organic and PGS-India marks, and the Health Fields name has been on organic food since 2003.

Steep it for 3 to 5 minutes. Add a spoon of Rozana Forest Honey if you like it sweeter.

Available on healthfields.in

#HealthFields #HerbalInfusion #CaffeineFree

## 12. WHY IT WILL PERFORM
- **Hook:** a question about the viewer's own routine ("your 9pm cup") lands in under 2.3s with voice, typed text and the pack all at once (the social skill's 3-second rule).
- **Saves:** four named ingredients plus three checkable facts is information people come back to, and saves are what Reels rewards. Every claim is verifiable, which fits HF's label-reading audience.
- **Retention:** something changes on screen at least every 1.8s, and the ZER✿ beat gives a small payoff near the end, the same retention pattern as the Goli reference.
- **Brand fit:** the lilac world matches the pack, so it reads as Health Fields at thumbnail size, and teal type keeps the brand anchor. It continues the RELATE/evening-ritual line from HF's best performer so far (the Chamomile reel at 16.4K views, brand bible §8).
- **Clean claims:** no health promises, so it's safe to boost if it performs organically.

## 13. BUNDLING SUGGESTION
**Health Fields Rozana Organic Forest Honey**: the natural sweetener for a herbal cup, and the brand bible pairs Rozana honey with the tea range. Mentioned once in the caption body as a usage tip, not a sales line.

---

## Post-delivery checklist
- [x] Reel rendered and verified (`reel_v2.mp4`)
- [x] Music licence recorded (`remotion/public/reels/.../audio/LICENSE-music.txt`)
- [x] Calming Chamomile added to the never-reuse reel list in CLAUDE.md
- [ ] Remotion licence: the free tier covers companies of up to 3 people. Confirm Brahhm Arpan's headcount or buy a company licence (remotion.pro/license) before commercial use at scale

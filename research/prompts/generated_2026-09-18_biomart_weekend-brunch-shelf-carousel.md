# Biomart — Weekend Brunch Shelf Carousel · Sept 18, 2026 (Fri)

**Calendar slot:** SEPT 18 · FRI · BIOMART · CAROUSEL · RELATE · "Weekend brunch shelf — 6 packs, one lazy morning"
**Biomart identity fit:** Pillar 2 — Haul / Bundle (curation voice)
**Template:** T87 — Biomart Curated Shelf Carousel (new; log to VEE after render approval)

---

## 1. CONTENT ANGLE
RELATE (Biomart curation voice, Pillar 2 — Haul/Bundle)

## 2. IDEA TITLE
Weekend Brunch Shelf — Six Packs, One Lazy Saturday

## 3. HOOK
Saturday brunch, shelf edition

## 4. EXECUTION
6-slide carousel. Cover = the whole shelf as one hero (2 rows of 3 packs, centered). Slides 2-5 = four brunch moments a lazy Saturday actually needs — the poha plate, the toast, the tea, the yogurt bowl + a cookie with coffee. Slide 6 = the shelf as a shop card with shelf total. Curation voice — Biomart picked the six; the reader picks the morning.

## 5. VISUAL DIRECTION
- Biomart color world — market green #00A050 + warm gold #B49664 accents on a cream-white studio ground
- Whole Foods editorial abundance meets clean Indian marketplace curation
- Soft warm north-light, subtle grain, editorial not commercial
- Every pack front-of-pack (never back)
- Hairline callouts with bold labels — no chip blocks, no colored pills backgrounds
- 4:5 aspect ratio (1080×1350) for feed carousel

## 6. IN-IMAGE TEXT REVIEW — CONFIRMED
(See prior turn — full table locked, all price pills included, shelf total ₹1,760, baked CTA on every slide, NO DOTS RULE applied, middot `·` allowed as separator only.)

**Uploads required (per slide):**
- **S1 + S6:** all 6 pack files (assembled as a labeled 2×3 reference sheet — per [[feedback_codex_5_image_cap]])
- **S2:** HF Poha (`organic-poha.webp`)
- **S3:** Pusht Forest Honey (`Pusht-Honey-Front-1.webp`)
- **S4:** HF Tulsi Green Tea Premium (`OrganicTulsiGreenTeaPremium01_2.jpg`)
- **S5:** Caveman Roasted Pumpkin Seeds + HF Raw Cashew + Caveman Super Kodo Honey Magic Cookies (3 packs)

Pack file root: `C:\Users\arpit\Documents\storage\arpan organic\`

---

## 7. GPT IMAGE 2.5 PROMPTS (LOCKED)

### SLIDE 1 — Cover · The Shelf Hero

```
Model: gpt-image-2.5-sunburst
Quality: xhigh
Aspect: 4:5 (1080×1350)
Pack refs (as one 2×3 labeled reference sheet):
  Row 1: Pusht Forest Honey | HF Tulsi Green Tea Premium | HF Poha 500g
  Row 2: Caveman Roasted Pumpkin Seeds | HF Raw Cashew 250g | Caveman Super Kodo Honey Magic Cookies
```

**PACK SHAPE HARD CONSTRAINT (top of prompt, non-negotiable):** Each of the six packs has a distinct silhouette. Do not average them into one shape. Top row left to right: (1) Pusht Forest Honey is a short wide-shouldered glass jar with a gold screw cap and a cream-and-gold rectangular label wrapping the front; (2) HF Tulsi Green Tea Premium is a vertical rectangular green paperboard carton; (3) HF Poha 500g is a standing flexible pouch with a wavy top seal. Bottom row left to right: (4) Caveman Roasted Pumpkin Seeds is a short round clear plastic jar with a white plastic screw lid and a green front label — the roasted pumpkin seeds are visible through the clear jar walls; (5) HF Raw Cashew 250g is a standing flexible teal pouch with tear-here strip and resealable zip-lock strip at the top; (6) Caveman Super Kodo Honey Magic Cookies is a HORIZONTAL RECTANGULAR CREAM-AND-BEIGE PAPERBOARD BOX — wider than tall, landscape orientation — reproduce the horizontal box geometry exactly, do not reshape it to a vertical carton or a pouch.

Create a new image. Image 1 is a 2×3 labeled reference sheet of six product packs matching the silhouettes above — reference-only, reproduce with total pack fidelity. Ignore all other images in the conversation. Preserve on every pack: full silhouette and geometry as specified above, ground colour exactly as printed (Pusht jar shows dark honey through glass with cream-and-gold label; HF Tulsi carton is fully green with tea-farmer field illustration; HF Poha pouch has a cream-and-white woven-textured top with a plated-poha photograph on the lower half and fresh basil and tomato illustration; Caveman Pumpkin Seeds jar shows visible roasted seeds through the clear plastic with a green front label; HF Cashew pouch is teal with a brown wooden bowl of cashews photograph and cashew-with-fruit botanical illustration on the left; Caveman Kodo Cookies box is cream-beige with the "Millets Cookies" gold-brown top ribbon, cookies + almonds + honey dipper photograph, and gluten-free badge), brand wordmark and badge as printed, illustration position and style as printed, every line of on-pack printed copy, all multilingual subtitles, the Jaivik Bharat mark, the green vegetarian dot, the resealable strip where present, the full bottom certification row including every stamp and small-print element as printed on each pack. Change nothing on any pack — no repositioned elements, no new text, no missing text, no colour shift, no logo redraw, no illustration redraw, no SKU substitution between the six.

Editorial overhead-angled hero shot of a warm cream-white studio counter, six product packs arranged as a curated shelf in two neat rows of three centred in the frame, each pack upright and static in its own silhouette, evenly spaced with generous negative space around the composition, top row left to right is Pusht Forest Honey wide glass jar, HF Tulsi Green Tea Premium green vertical carton, HF Poha 500g standing pouch, bottom row left to right is Caveman Roasted Pumpkin Seeds clear plastic jar with white lid, HF Raw Cashew 250g teal pouch, Caveman Super Kodo Honey Magic Cookies horizontal rectangular cream-beige box. Soft warm north-light from the upper left, gentle diffused fall, market green and warm gold accents living quietly on the ground plane, no rustic props, no wooden bowls, no burlap, no scattered ingredients, no whole spices, no hands, no models, no people. The pack labels are the hero — front-of-pack fully lit, zero shadow on the label face, every certification stamp legible, subtle film grain across the plate.

Render exactly once: 'SIX PACKS' on line 1 in bold sans-serif caps, market green #00A050, medium-large size, upper-left third of the frame above the shelf. Render exactly once: 'one lazy Saturday' on line 2 in italic serif, warm gold #B49664, same size as line 1, directly below line 1. Render exactly once: 'CURATED FOR YOU BY BIOMART' in small sans-serif caps, warm gold, tight letter-spacing, top-right corner of the frame. Render exactly once: 'SHELF TOTAL ₹1,760' in bold sans-serif caps, warm gold on cream with a hairline outline, small pill, bottom-left of the frame above the CTA line. Render exactly once: 'Shop the shelf on biomart.in' in small clean sans-serif, market green, quiet and bottom-anchored, centered. The callout labels and headline together form the second visual layer of the image after the packs — they must be immediately readable at Instagram feed thumbnail scale, not designer-decorative.

No dots or full stops at the end of any headline, label, price pill, or CTA. No duplicate text zones, no repeated headlines, no repeated ribbons, no repeated callouts, no repeated price pills, no SKU swap on any pack. No solid colored chip blocks anywhere. No scattered ingredient beds. No rustic props. No hands, no models, no people in frame. No promotional exclamation marks. No link-in-bio or swipe-up language.

Abundant marketplace editorial, Whole Foods store aesthetic, clean warm studio light, market green and warm gold color world, premium organic curation, trustworthy Indian marketplace. 4:5 aspect ratio.

**Iteration path (2.5 surgical edit):** if S1 comes back 80–95% right and only one thing needs fixing (headline colour, price-pill position, shelf-total wording, one pack rendered as wrong SKU), send an edit turn — `Change: [one specific thing]. Preserve: [every other element listed above verbatim]. Constraints: no new elements, no colour shift on any pack, no re-rendering of any preserved item, no duplicate text zones, no SKU swap on any of the six packs.`

---

### SLIDE 2 — The 10-Minute Plate · HF Poha

```
Model: gpt-image-2.5-flare
Quality: xhigh
Aspect: 4:5 (1080×1350)
Pack ref: organic-poha.webp
```

Create a new image. Image 1 is the Health Fields Organic Poha 500g standing pouch — reference-only, reproduce with total pack fidelity. Ignore all other images in the conversation. Preserve on the pack: full standing-pouch silhouette and geometry with the wavy top seal and flat base, cream-and-white woven-textured upper half, the red-and-black "Health Fields" wordmark inside the ornate dark banner as printed, the round "Organic by Nature" green seal top-left, the green vegetarian dot top-right, "Organic POHA" headline in black serif with "FLAKED RICE" gold sub-strip, the "Easy to digest and highly enriched..." tagline line, the lower-half product photograph showing a bowl of cooked yellow poha with peas and tomato beside fresh green basil leaves and whole tomatoes on a wood-grain surface, the round gold "The Best Choice" badge bottom-right, "NET WEIGHT: 500g" at bottom-left. Change nothing on the pack — no repositioned elements, no new text, no missing text, no colour shift, no logo redraw, no illustration redraw, no SKU substitution.

Editorial three-quarter hero shot of a warm cream-white studio counter, HF Organic Poha 500g pouch standing upright and static on the left third of the frame, a plated poha bowl in the centre-right — flat white ceramic plate, yellow poha grains cooked light and fluffy, one lemon wedge on the rim, one sprig of fresh curry leaf resting on top for garnish, gentle steam rising from the plate. Soft warm north-light from the upper left, gentle diffused fall, market green and warm gold living quietly on the ground plane, no rustic props, no wooden bowls, no burlap, no hands, no models. Pack label fully lit, zero shadow on the label face, every certification stamp legible, subtle film grain across the plate.

Render exactly once: 'THE 10-MINUTE PLATE' in bold sans-serif caps, market green #00A050, medium-large size, upper-left of the frame. Render exactly once: 'HEALTH FIELDS ORGANIC POHA 500G' in small sans-serif caps, warm gold #B49664, tight letter-spacing, as a hairline callout with a fine pointer line to the pack, positioned to the right of the pack. Render exactly once: '₹115' in bold sans-serif caps, warm gold on cream with a hairline outline, small pill, directly below the SKU callout. Render exactly once: 'Shop on biomart.in' in small clean sans-serif, market green, quiet and bottom-anchored, centered. The callout labels and headline together form the second visual layer after the pack — they must be immediately readable at Instagram feed thumbnail scale.

No dots or full stops at the end of any headline, label, price pill, or CTA. No duplicate text zones, no repeated headlines, no repeated callouts, no repeated price pills, no SKU swap on the pack. No solid colored chip blocks. No rustic props. No hands, no models, no people in frame. No promotional exclamation marks.

Abundant marketplace editorial, Whole Foods store aesthetic, clean warm studio light, market green and warm gold color world, premium organic curation, trustworthy Indian marketplace. 4:5 aspect ratio.

---

### SLIDE 3 — Toast, Honey, Done · Pusht Forest Honey

```
Model: gpt-image-2.5-flare
Quality: xhigh
Aspect: 4:5 (1080×1350)
Pack ref: Pusht-Honey-Front-1.webp
```

**PACK SHAPE HARD CONSTRAINT:** The Pusht Organic Forest Honey pack is a short wide-shouldered glass jar, not a tall bottle — approximately as wide as it is tall, with a smooth-sided body that tapers gently to the neck. It has a gold metal screw cap on top. Reproduce this squat wide-jar silhouette exactly. Do not render it as a tall slim bottle or a cylindrical honey bear.

Create a new image. Image 1 is the Pusht Organic Forest Honey wide glass jar — reference-only, reproduce with total pack fidelity. Ignore all other images in the conversation. Preserve on the pack: the short wide-shouldered glass-jar silhouette as specified above, gold screw-cap geometry and colour, dark amber honey visible through the glass, the cream-and-gold rectangular front label with rounded shoulders, the round green "PUSHT ORGANIC" circular badge with tree logo in the centre of the label, "SINCE 2003" small caps arched above the badge, the green vegetarian dot upper-right on the label, "ORGANIC" in dark green caps, "FOREST Honey" in the brown script-and-serif treatment with a small bee illustration, honeycomb graphic to the left of the weight, "NET WT.: 500g" in green caps, the small poppy-flower illustration at the bottom of the label. Change nothing on the pack — no repositioned elements, no new text, no missing text, no colour shift, no logo redraw, no illustration redraw, no SKU substitution.

Editorial three-quarter hero shot of a warm cream-white studio counter, Pusht Organic Forest Honey wide glass jar standing upright and static on the left third of the frame, cap sealed and undisturbed on top of the jar, a single slice of golden-crusted sourdough toast on a small cream ceramic plate in the centre-right, one clean single sweeping ribbon arc of forest honey drizzling from a small wooden honey dipper held mid-air just above the toast — the dipper is a separate object with a visible air gap between it and the toast, the honey ribbon is one graceful continuous arc, not scattered droplets. Soft warm north-light from the upper left, gentle diffused fall, market green and warm gold living quietly on the ground plane, no rustic props beyond the honey dipper, no wooden bowls, no burlap, no hands visible, no models. Pack label fully lit, zero shadow on the label face, every certification stamp legible, subtle film grain across the plate.

Render exactly once: 'TOAST, HONEY, DONE' in bold sans-serif caps, market green #00A050, medium-large size, upper-left of the frame. Render exactly once: 'PUSHT ORGANIC FOREST HONEY 500G' in small sans-serif caps, warm gold #B49664, tight letter-spacing, as a hairline callout with a fine pointer line to the pack, positioned to the right of the pack. Render exactly once: '₹450' in bold sans-serif caps, warm gold on cream with a hairline outline, small pill, directly below the SKU callout. Render exactly once: 'Shop on biomart.in' in small clean sans-serif, market green, quiet and bottom-anchored, centered. The callout labels and headline together form the second visual layer after the pack — they must be immediately readable at Instagram feed thumbnail scale.

No dots or full stops at the end of any headline, label, price pill, or CTA. No duplicate text zones, no repeated headlines, no repeated callouts, no repeated price pills, no SKU swap on the pack. No solid colored chip blocks. No scattered honey droplets or explosion — the drizzle is one clean sweeping ribbon. No rustic props beyond the small honey dipper. No hands visible in frame. No promotional exclamation marks.

Abundant marketplace editorial, Whole Foods store aesthetic, clean warm studio light, market green and warm gold color world, premium organic curation, trustworthy Indian marketplace. 4:5 aspect ratio.

---

### SLIDE 4 — The Morning Brew · HF Tulsi Green Tea Premium

```
Model: gpt-image-2.5-flare
Quality: xhigh
Aspect: 4:5 (1080×1350)
Pack ref: OrganicTulsiGreenTeaPremium01_2.jpg
```

Create a new image. Image 1 is the HealthFields Organic Tulsi Green Tea Premium 25 infusion bags vertical rectangular green paperboard carton — reference-only, reproduce with total pack fidelity. Ignore all other images in the conversation. Preserve on the pack: vertical rectangular carton silhouette and geometry, the fully green ground colour exactly as printed (not teal) with subtle white tea-leaf illustrations at top corners, the red-and-green "Health Fields" wordmark in a green rounded rectangle top-centre with a small "H" monogram badge, "SINCE 2003" small caps arched above the wordmark, the green vegetarian dot top-right, "ORGANIC" in white caps below the wordmark, "TULSI" in large white caps, "GREEN TEA" in white caps with "Premium" in a small gold-yellow ribbon, the "JUST PURE GOODNESS" tagline in a gold band, the round gold "100% NATURAL" seal on the right, the lower-half illustration of a tea-farmer bending in the tea-leaf hillside rows, the "MADE WITH 100% UNBLEACHED PAPER" small orange badge on the left, the certification row at the bottom including USDA ORGANIC, IMO, Jaivik Bharat and the "25 INFUSION BAGS" callout. Change nothing on the pack — no repositioned elements, no new text, no missing text, no colour shift, no logo redraw, no illustration redraw, no SKU substitution.

Editorial three-quarter hero shot of a warm cream-white studio counter, HF Tulsi Green Tea Premium green carton standing upright and static on the left third of the frame, a clear glass cup filled with pale-green brewed tulsi tea in the centre-right on a small cream ceramic saucer, one thin curl of steam rising off the surface of the tea, one single dried tulsi leaf resting on the saucer beside the cup. Soft warm north-light from the upper left, gentle diffused fall, deep green accent from the carton echoed subtly in the shadow of the glass, market green and warm gold living quietly on the ground plane, no rustic props, no wooden bowls, no burlap, no hands, no models. Pack label fully lit, zero shadow on the label face, every certification stamp legible, subtle film grain across the plate.

Render exactly once: 'THE MORNING BREW' in bold sans-serif caps, market green #00A050, medium-large size, upper-left of the frame. Render exactly once: 'HEALTH FIELDS TULSI GREEN TEA PREMIUM · 25 INFUSION BAGS' in small sans-serif caps, warm gold #B49664, tight letter-spacing, as a hairline callout with a fine pointer line to the pack, positioned to the right of the pack. Render exactly once: '₹215' in bold sans-serif caps, warm gold on cream with a hairline outline, small pill, directly below the SKU callout. Render exactly once: 'Shop on biomart.in' in small clean sans-serif, market green, quiet and bottom-anchored, centered. The callout labels and headline together form the second visual layer after the pack — they must be immediately readable at Instagram feed thumbnail scale.

No dots or full stops at the end of any headline, label, price pill, or CTA. No duplicate text zones, no repeated headlines, no repeated callouts, no repeated price pills, no SKU swap on the pack. No solid colored chip blocks. No rustic props. No hands, no models, no people in frame. No promotional exclamation marks.

Abundant marketplace editorial, Whole Foods store aesthetic, clean warm studio light, market green and warm gold color world, premium organic curation, trustworthy Indian marketplace. 4:5 aspect ratio.

---

### SLIDE 5 — Yogurt Bowl, Cookie With Coffee · Three Packs

```
Model: gpt-image-2.5-sunburst
Quality: xhigh
Aspect: 4:5 (1080×1350)
Pack refs (attach in this order):
  Image 1: Caveman Roasted Pumpkin Seeds 200g (caveman-roasted-pumpkin-seed-front.webp)
  Image 2: Health Fields Raw Cashew Nut 250g (organic-raw-cashew-jpg.webp)
  Image 3: Caveman Super Kodo Honey Magic Cookies (organic-super-kodo-honey-magic-1 (1).jpg)
```

**PACK SHAPE HARD CONSTRAINT (top of prompt, non-negotiable):** The three packs on this slide have three completely different silhouettes. Do not average them. (1) Caveman Roasted Pumpkin Seeds 200g is a SHORT ROUND CLEAR PLASTIC JAR with a WHITE PLASTIC SCREW LID, roughly as wide as it is tall, roasted olive-green pumpkin seeds visible through the clear jar walls, a green front label wrapped around the middle. (2) HF Raw Cashew Nut 250g is a STANDING FLEXIBLE TEAL POUCH with a tear-here strip and a resealable zip-lock strip at the top, taller than wide, flat-bottomed. (3) Caveman Super Kodo Honey Magic Cookies is a HORIZONTAL RECTANGULAR CREAM-AND-BEIGE PAPERBOARD BOX — landscape orientation, wider than tall — reproduce the horizontal box geometry exactly, do not reshape it to a vertical carton, a pouch, or a jar.

Create a new image. Image 1 is the Caveman Organic Roasted Pumpkin Seeds 200g clear plastic jar with white lid, Image 2 is the Health Fields Organic Raw Cashew Nut 250g standing teal pouch, Image 3 is the Caveman Super Kodo Honey Magic Cookies horizontal cream-beige box — all three reference-only, reproduce with total pack fidelity and the silhouettes specified above. Ignore all other images in the conversation. Preserve on pack 1 (Pumpkin Seeds jar): the short round clear-plastic-jar silhouette with white screw lid, the visible roasted pumpkin seeds inside, the green front label with the black-and-red "Caveman" wordmark inside the red splash badge, "Organic" in white script, "ROASTED" in a small red pill, "PUMPKIN SEEDS" in bold white caps, "WITH REAL SPICES" sub-line, "Bridging superfoods & your lifestyle..." tagline, green vegetarian dot at top-right. Preserve on pack 2 (Cashew pouch): the standing teal flexible-pouch silhouette with the "Tear Here to open" strip top-left and "Resealable Zip Lock Pack" strip top-right, the ornate "Health Fields" wordmark inside the golden oval badge with "SINCE 2003" and "ORGANIC BY NATURE" arched around it, the green vegetarian dot at top-right, the multilingual "ORGANIC" line in Arabic, Russian and English on the white label, "RAW CASHEW NUTS" in bold black caps, the round "Quality" seal on the right, the "SOURCE OF FIBER" label with Arabic and Russian translations on the left, the cashew-with-yellow-and-red-fruit botanical illustration on the left mid-pack, the lower-half photograph showing a brown wooden bowl full of raw cashews on a wood-grain surface, the full bottom certification row (USDA ORGANIC, Jaivik Bharat, GLUTEN FREE, 100% VEGAN, NO ADDITIVES). Preserve on pack 3 (Kodo Cookies box): the horizontal rectangular cream-beige paperboard-box silhouette in landscape orientation, the gold-brown "Millets Cookies" top ribbon in dark brown caps, the black-and-red "Caveman" wordmark inside the red splash badge, "organic cookies" in dark brown lowercase script, "Super Kodo Honey Magic" as the product name in dark brown, the "with the goodness of Almond, Honey & Kodo Millets with crispy and crunchy taste" tagline, the "Millet based organic cookies with butter" sub-line, the photograph on the right showing two dark millet cookies topped with almond chunks beside a small honey dipper pot, the green vegetarian dot, "Bridging superfoods & your lifestyle..." tagline, "NO WHEAT" caps and the green "GLUTEN FREE" wheat-icon badge on the right. Change nothing on any pack — no repositioned elements, no new text, no missing text, no colour shift, no logo redraw, no illustration redraw, no SKU substitution between the three.

Editorial three-quarter hero shot of a warm cream-white studio counter, three product packs arranged left to right with generous spacing, each pack upright and static in its own silhouette, packs occupying roughly the upper two-thirds of the frame — the short round Caveman Roasted Pumpkin Seeds clear jar with white lid on the left, the standing HF Raw Cashew Nut teal pouch in the centre, the horizontal Caveman Super Kodo Honey Magic Cookies cream-beige box on the right. Below the packs on the counter, a small still-life composition: one small cream ceramic bowl of thick set curd with a light sprinkle of roasted pumpkin seeds on top on the left, one small handful of raw cashews on a folded cream linen napkin in the centre, one small cream ceramic saucer with one honey-magic cookie and a small dark ceramic espresso cup on the right. Soft warm north-light from the upper left, gentle diffused fall, market green and warm gold living quietly on the ground plane, no rustic props beyond the ceramics and linen, no wooden bowls, no burlap, no scattered spices, no hands, no models. Pack labels fully lit, zero shadow on the label faces, every certification stamp legible, subtle film grain across the plate.

Render exactly once: 'YOGURT BOWL' on line 1 in bold sans-serif caps, market green #00A050, medium-large size, upper-left of the frame. Render exactly once: 'cookie with coffee' on line 2 in italic serif, warm gold #B49664, same size as line 1, directly below line 1. Render exactly once: 'CAVEMAN ROASTED PUMPKIN SEEDS 200G' in small sans-serif caps, warm gold, tight letter-spacing, as a hairline callout to the left pack. Render exactly once: '₹356' in bold sans-serif caps, warm gold on cream with a hairline outline, small pill, directly below that callout. Render exactly once: 'HEALTH FIELDS RAW CASHEW 250G' in small sans-serif caps, warm gold, as a hairline callout to the centre pack. Render exactly once: '₹500' in bold sans-serif caps, warm gold on cream with a hairline outline, small pill, directly below that callout. Render exactly once: 'CAVEMAN SUPER KODO HONEY MAGIC COOKIES · 2×60G' in small sans-serif caps, warm gold, as a hairline callout to the right pack. Render exactly once: '₹124' in bold sans-serif caps, warm gold on cream with a hairline outline, small pill, directly below that callout. Render exactly once: 'Shop on biomart.in' in small clean sans-serif, market green, quiet and bottom-anchored, centered. The three callout groups and the headline together form the second visual layer after the packs — they must be immediately readable at Instagram feed thumbnail scale, and each callout points cleanly to its own pack with no crossed lines.

No dots or full stops at the end of any headline, label, price pill, or CTA. No duplicate text zones, no repeated headlines, no repeated callouts, no repeated price pills, no SKU swap on any of the three packs, no callout pointing to the wrong pack. No solid colored chip blocks. No rustic props beyond ceramics and linen. No hands, no models, no people in frame. No promotional exclamation marks.

Abundant marketplace editorial, Whole Foods store aesthetic, clean warm studio light, market green and warm gold color world, premium organic curation, trustworthy Indian marketplace. 4:5 aspect ratio.

---

### SLIDE 6 — The Whole Shelf, One Order · Close CTA

```
Model: gpt-image-2.5-sunburst
Quality: xhigh
Aspect: 4:5 (1080×1350)
Pack refs: same 2×3 labeled reference sheet as Slide 1
```

**PACK SHAPE HARD CONSTRAINT (top of prompt, non-negotiable):** Same as Slide 1 — six distinct silhouettes, do not average. Top row: (1) Pusht Forest Honey short wide-shouldered glass jar with gold cap; (2) HF Tulsi Green Tea Premium vertical rectangular green carton; (3) HF Poha 500g standing pouch. Bottom row: (4) Caveman Roasted Pumpkin Seeds short round clear plastic jar with white lid (seeds visible); (5) HF Raw Cashew 250g standing teal pouch; (6) Caveman Super Kodo Honey Magic Cookies HORIZONTAL RECTANGULAR CREAM-AND-BEIGE PAPERBOARD BOX in landscape orientation.

Create a new image. Image 1 is the same 2×3 labeled reference sheet of six product packs used on Slide 1 — top row Pusht Forest Honey wide glass jar, HF Tulsi Green Tea Premium green vertical carton, HF Poha 500g standing pouch; bottom row Caveman Roasted Pumpkin Seeds clear plastic jar with white lid, HF Raw Cashew 250g teal pouch, Caveman Super Kodo Honey Magic Cookies horizontal cream-beige box — all reference-only, reproduce with total pack fidelity and the silhouettes specified above. Ignore all other images in the conversation. Preserve on every pack the same locked elements listed for Slide 1 — the specific silhouette per the hard constraint above, the ground colour and label design as printed on each pack (Pusht cream-and-gold label with green tree badge, HF Tulsi fully green with tea-farmer illustration, HF Poha cream-and-white with plated-poha photograph, Caveman Pumpkin Seeds green front label on clear jar, HF Cashew teal with wooden-bowl photograph, Caveman Kodo Cookies cream-beige with cookies-and-honey-dipper photograph), the wordmark, illustration, every line of printed copy, all certification stamps, the Jaivik Bharat mark, the vegetarian dot, and the small-print row. Change nothing on any pack — no repositioned elements, no new text, no missing text, no colour shift, no logo redraw, no illustration redraw, no SKU substitution between the six.

Editorial overhead-angled close shot of a warm cream-white studio counter, the same six product packs from Slide 1 arranged as a curated shelf in two neat rows of three centred in the frame, top row left to right is Pusht Forest Honey wide glass jar, HF Tulsi Green Tea Premium green vertical carton, HF Poha 500g standing pouch, bottom row left to right is Caveman Roasted Pumpkin Seeds clear plastic jar with white lid, HF Raw Cashew 250g teal pouch, Caveman Super Kodo Honey Magic Cookies horizontal cream-beige box, each pack upright and static in its own silhouette, evenly spaced with generous negative space around the composition, camera pulled slightly closer than Slide 1 so the shelf reads as a complete order ready to go. Soft warm north-light from the upper left, gentle diffused fall, market green and warm gold living quietly on the ground plane, no rustic props, no wooden bowls, no burlap, no scattered ingredients, no whole spices, no hands, no models, no people. Pack labels fully lit, zero shadow on the label faces, every certification stamp legible, subtle film grain across the plate.

Render exactly once: 'THE WHOLE SHELF' on line 1 in bold sans-serif caps, market green #00A050, medium-large size, upper-left of the frame. Render exactly once: 'one order' on line 2 in italic serif, warm gold #B49664, same size as line 1, directly below line 1. Render exactly once: 'CURATED FOR YOU BY BIOMART' in small sans-serif caps, warm gold, tight letter-spacing, top-right corner of the frame. Render exactly once: 'SHELF TOTAL ₹1,760' in bold sans-serif caps, warm gold on cream with a hairline outline, small pill, centered above the CTA card. Render exactly once: 'Available on biomart.in' in medium clean sans-serif, market green, quiet card treatment, centered in the bottom third of the frame. The callout labels and headline together form the second visual layer of the image after the packs — they must be immediately readable at Instagram feed thumbnail scale.

No dots or full stops at the end of any headline, label, price pill, or CTA. No duplicate text zones, no repeated headlines, no repeated ribbons, no repeated callouts, no repeated price pills, no SKU swap on any pack. No solid colored chip blocks. No scattered ingredient beds. No rustic props. No hands, no models, no people in frame. No promotional exclamation marks. No link-in-bio or swipe-up language.

Abundant marketplace editorial, Whole Foods store aesthetic, clean warm studio light, market green and warm gold color world, premium organic curation, trustworthy Indian marketplace. 4:5 aspect ratio.

---

## HUMANIZER AUDIT (Point 8 caption)
Humanizer audit: cut "a weekend curation you can actually finish" (sloganish AI cadence + copula avoidance → replaced with "six packs, one lazy Saturday"), cut "Both the honey and the poha are cold-morning heroes" (rule-of-three-adjacent parallelism → collapsed to a single specific line naming what each pack does), cut "quietly curated with intention" (superficial -ing significance inflation → replaced with the plain "we picked these six because they're the ones we actually reach for on a Saturday").

## 8. CAPTION

Saturday brunch, shelf edition.

Six packs from three of our house shelves — poha for the ten-minute plate, forest honey for the toast, tulsi green tea for the first cup, roasted pumpkin seeds on the curd bowl, raw cashews for the counter, and one honey magic cookie for the coffee. That's the whole morning.

We picked these six because they're the ones we actually reach for on a Saturday. Shelf total ₹1,760, one order.

Shop the shelf on biomart.in

#Biomart #OrganicMegastore #WeekendBrunch

## 10. WEBSITE CTA
- In-image CTA on every slide → `Shop on biomart.in` / `Shop the shelf on biomart.in` (S1) / `Available on biomart.in` (S6)
- Caption CTA → `Shop the shelf on biomart.in`
- Website mapping: Biomart → biomart.in (all six SKUs live on biomart.in — cross-brand catalog)
- Point 6 in-image text review includes the baked CTA on every slide ✅

## 11. VARIATION (caption alt)

Humanizer audit: cut "a Saturday morning that basically runs itself" (weasel filler + copula avoidance → replaced with the plain "one shelf, one order"), cut "curated with care for your weekend" (promotional AI cadence → cut entirely, replaced with the specific pack-by-pack list), cut "the six essentials your Saturday deserves" (rule-of-three + persuasive authority trope → replaced with "the six we reach for").

---

One shelf, one order, one lazy Saturday.

Poha and forest honey for the plate. Tulsi green tea for the first cup. Roasted pumpkin seeds on the curd. Raw cashews and a honey magic cookie for the counter. These are the six we reach for on a Saturday — so we put them on one shelf.

₹1,760 for the whole morning.

Available on biomart.in

#Biomart #OrganicMegastore #SaturdayShelf

## 12. WHY IT WILL PERFORM

- **Curation voice fit** — Biomart's Pillar 2 (Haul/Bundle) is a proven save-driver; this is the exact "I want that pantry" trigger with real prices attached
- **Cross-brand storytelling** — the shelf features three house brands (Pusht, HF, Caveman) in one frame, doing what @twobrothersorganicfarmsindia does with its farm story — using the marketplace to prove range, not just list SKUs
- **RELATE anchor + EDUCATE utility** — the emotional frame ("lazy Saturday") lands the save; the six-pack price list gives the "add-to-cart" nudge without a discount code
- **Feed-scroll geometry** — 2×3 shelf cover reads at thumbnail scale, quieter than a single-hero shot; the price pills give the algorithm text density for OCR + accessibility
- **Weekend timing** — Friday post lands in the feed exactly when a Saturday brunch shop happens; the shelf-total pill lowers cart-friction because the number is already visible before the user clicks
- **No-discount curation** — every recent AOV win in the account came from bundle framing without a code; the whole ₹1,760 shelf is the ask

## 13. BUNDLING SUGGESTION

Surfaced naturally inside the caption body — the shelf itself is the bundle. If a soft pairing addition is wanted for a comment reply or a story tile, HF Organic Rozana Honey 500g (same brunch shelf logic, different sweetener household) or Caveman Bakkit Cashew & Pista Cookies (coffee-side alternate) pair cleanly and stay on-shelf without breaking the six-pack story.

---

## PACK FILE PATHS (for GPT uploads)

| Slide | Pack file | Absolute path |
|---|---|---|
| S1, S6 | 2×3 reference sheet (build before render) | assemble via `scripts/pack_ref_sheet.py` into `research/prompts/assets/2026-09-18_biomart_brunch_shelf/refsheet_2x3.png` |
| S2 | HF Poha 500g | `C:\Users\arpit\Documents\storage\arpan organic\health fields\organic-poha.webp` |
| S3 | Pusht Forest Honey | `C:\Users\arpit\Documents\storage\arpan organic\pusht\Pusht-Honey-Front-1.webp` |
| S4 | HF Tulsi Green Tea Premium | `C:\Users\arpit\Documents\storage\arpan organic\health fields\OrganicTulsiGreenTeaPremium01_2.jpg` |
| S5 · pack 1 | Caveman Roasted Pumpkin Seeds 200g | `C:\Users\arpit\Documents\storage\arpan organic\caveman\caveman-roasted-pumpkin-seed-front.webp` |
| S5 · pack 2 | HF Raw Cashew 250g | `C:\Users\arpit\Documents\storage\arpan organic\health fields\organic-raw-cashew-jpg.webp` |
| S5 · pack 3 | Caveman Super Kodo Honey Magic Cookies | `C:\Users\arpit\Documents\storage\arpan organic\caveman\organic-super-kodo-honey-magic-1 (1).jpg` |

**Point 7 upload flags:**
- S1: ✅ YES — refsheet_2x3.png
- S2: ✅ YES — organic-poha.webp
- S3: ✅ YES — Pusht-Honey-Front-1.webp
- S4: ✅ YES — OrganicTulsiGreenTeaPremium01_2.jpg
- S5: ✅ YES — three separate packs in specified order
- S6: ✅ YES — refsheet_2x3.png (same as S1)

---

## VEE LOG ENTRY (append after render approval)
- **T87 — Biomart Curated Shelf Carousel** (assigned 2026-09-18)
- Format: 4:5 multi-slide, cover + interior + close, cross-brand shelf pattern with hairline callouts + small price pills + curator byline + shelf-total pill
- Aesthetic: Biomart abundant marketplace editorial cluster
- First use: Sept 18 Weekend Brunch Shelf (this file)

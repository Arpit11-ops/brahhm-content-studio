# Brahhm Content Studio: Remotion reels

Code-built motion-graphics reels for the Content Studio brands. Full workspace guide: `../skills/remotion-reels/SKILL.md`.

```bash
npm i --loglevel=error                             # install (first time / after a fresh clone)
npm run dev                                        # Remotion Studio preview
npx remotion render <composition-id> out/<name>.mp4
npx remotion render SetupCheck out/setup-check.mp4 # pipeline smoke test
```

- Reel code: `src/reels/<YYYY-MM-DD>_<brand>_<slug>/`, registered in `src/Root.tsx`
- Reel assets: `public/reels/<YYYY-MM-DD>_<brand>_<slug>/`
- Voiceover: `.tts/Scripts/python tools/voiceover.py --script <vo.json> --out <dir> [--voice af_heart] [--ts <file.ts>]`
- Pack cut-outs: `.tts/Scripts/python tools/cutout.py <image...> --out <dir>`

Remotion is free for teams of up to 3 people; larger companies need a licence (remotion.pro/license).

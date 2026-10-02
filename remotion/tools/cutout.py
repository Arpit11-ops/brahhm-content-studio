"""Remove the background from pack photos so they can be animated as clean cut-outs.

Usage (from the remotion/ folder):
  .tts/Scripts/python tools/cutout.py "<input image>" [more images...] --out public/reels/<slug>/packs
      [--model u2net | isnet-general-use | birefnet-general]  [--method white]

Writes <name>.png with a transparent background, trimmed to the pack.
- Default: rembg `u2net` (tested best on Health Fields pouches; `isnet-general-use` ate printed wood textures).
- `--method white`: flood-fills a pure-white studio background from the borders. No model, but can leave
  a faint halo on light pack edges.
First model run downloads its weights (~170 MB) to ~/.u2net. Always check the result on a dark background.
"""

import argparse
from collections import deque
from pathlib import Path

from PIL import Image, ImageChops, ImageFilter


def white_cutout(img: Image.Image) -> Image.Image:
    rgb = img.convert("RGB")
    w, h = rgb.size
    px = rgb.load()
    mask = Image.new("L", (w, h), 0)
    m = mask.load()
    is_white = lambda p: p[0] > 236 and p[1] > 236 and p[2] > 236
    q = deque()
    border = [(x, y) for x in range(w) for y in (0, h - 1)] + [(x, y) for y in range(h) for x in (0, w - 1)]
    for x, y in border:
        if not m[x, y] and is_white(px[x, y]):
            m[x, y] = 255
            q.append((x, y))
    while q:
        x, y = q.popleft()
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < w and 0 <= ny < h and not m[nx, ny] and is_white(px[nx, ny]):
                m[nx, ny] = 255
                q.append((nx, ny))
    out = img.copy()
    out.putalpha(ImageChops.invert(mask).filter(ImageFilter.GaussianBlur(0.8)))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inputs", nargs="+", type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--model", default="u2net")
    ap.add_argument("--method", choices=["model", "white"], default="model")
    args = ap.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    session = None
    if args.method == "model":
        from rembg import new_session

        session = new_session(args.model)
    for src in args.inputs:
        img = Image.open(src).convert("RGBA")
        if args.method == "white":
            cut = white_cutout(img)
        else:
            from rembg import remove

            cut = remove(img, session=session, post_process_mask=True)
        bbox = cut.getbbox()
        if bbox:
            cut = cut.crop(bbox)
        dest = args.out / f"{src.stem}.png"
        cut.save(dest)
        print(f"{src.name} -> {dest} ({cut.width}x{cut.height})", flush=True)


if __name__ == "__main__":
    main()

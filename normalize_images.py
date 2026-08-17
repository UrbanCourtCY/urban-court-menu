"""
Crop each PNG to its non-transparent content bbox, add 4% uniform padding,
and overwrite the file. Originals are backed up to Images/originals/.
"""
import os, shutil
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).parent

# Directories containing product PNGs to normalise
TARGET_DIRS = [
    "Images/Freshly Made",
    "Images/Kombucha",
    "Images/Ice Herbal Tea",
    "Images/Tea",
    "Images/Matcha",
    "Images/Coffee",
    "Images/Non-Alchoholic",
    "Images/Snacks",
]

BACKUP_DIR = ROOT / "Images" / "originals"
PADDING_PCT = 0.04   # 4% of the larger dimension as uniform padding
ALPHA_THRESHOLD = 10


def crop_and_pad(path: Path, backup_dir: Path) -> None:
    img = Image.open(path).convert("RGBA")
    alpha = img.split()[3]

    # Find the bounding box of pixels with alpha > threshold
    bbox = None
    w, h = img.size
    pixels = alpha.load()
    min_x, min_y, max_x, max_y = w, h, 0, 0
    for y in range(h):
        for x in range(w):
            if pixels[x, y] > ALPHA_THRESHOLD:
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y

    if max_x < min_x or max_y < min_y:
        print(f"  SKIP (fully transparent): {path.name}")
        return

    # Padding
    content_w = max_x - min_x + 1
    content_h = max_y - min_y + 1
    pad = max(int(max(content_w, content_h) * PADDING_PCT), 4)

    x0 = max(0, min_x - pad)
    y0 = max(0, min_y - pad)
    x1 = min(w, max_x + pad + 1)
    y1 = min(h, max_y + pad + 1)

    cropped = img.crop((x0, y0, x1, y1))

    # Skip if crop would be a no-op (already tight)
    if (x0, y0, x1, y1) == (0, 0, w, h):
        print(f"  SKIP (no change needed): {path.name}")
        return

    # Backup original
    rel = path.relative_to(ROOT / "Images")
    bak = backup_dir / rel
    bak.parent.mkdir(parents=True, exist_ok=True)
    if not bak.exists():   # only back up once
        shutil.copy2(path, bak)

    cropped.save(path, "PNG", optimize=True)
    print(f"  OK  {path.name}  {w}x{h} → {cropped.size[0]}x{cropped.size[1]}  (pad={pad}px)")


def main():
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    for dir_str in TARGET_DIRS:
        d = ROOT / dir_str
        if not d.exists():
            print(f"DIR NOT FOUND: {d}")
            continue
        pngs = sorted(d.glob("*.png"))
        if not pngs:
            print(f"no PNGs in {dir_str}")
            continue
        print(f"\n── {dir_str} ({len(pngs)} files)")
        for p in pngs:
            crop_and_pad(p, BACKUP_DIR)


if __name__ == "__main__":
    main()

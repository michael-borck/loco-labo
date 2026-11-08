#!/usr/bin/env python3
"""Generate, pick, and distribute LocoLabo pixel art with limn.

Recipe (see art/ART-BIBLE.md): juggernautXL_v9 + the pixel-art-xl LoRA, style
front-loaded, one shared palette, a strong anti-photo negative, fixed seeds.

  python3 scripts/loco_art.py list
  python3 scripts/loco_art.py generate                    # every job, 2 candidates
  python3 scripts/loco_art.py generate --name fosil-hero --candidates 3
  python3 scripts/loco_art.py pick fosil-hero 2           # choose candidate 2
  python3 scripts/loco_art.py process                     # picks -> site repos

Candidates and picks live in art/ (gitignored). Only processed files ship.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

HUB = Path(__file__).resolve().parents[1]          # loco-labo/
WORKSPACE = HUB.parent                              # sites/loco-labo/
CANDIDATES = HUB / "art" / "candidates"
PICKS = HUB / "art" / "picks"

MODEL = "juggernautXL_v9"
LORA = "pixel-art-xl:1"
SCENE_SIZE = "1216x832"
ICON_SIZE = "1024x1024"
BASE_SEED = 4100

PALETTE = "deep indigo night, warm amber lamplight, soft cyan screen glow"
NEGATIVE = (
    "photo, photorealistic, 3d render, bokeh, depth of field, film grain, blurry, "
    "soft focus, smooth gradients, text, letters, words, numbers, watermark, signature, "
    "logo, border, frame, UI elements, deformed, extra limbs"
)
SCENE = (
    "16-bit pixel art game scene, chunky pixels, limited color palette, crisp pixels, "
    "subtle dithering: {desc}, " + PALETTE + ", cozy, game art"
)
ICON = (
    "16-bit pixel art game inventory icon, chunky pixels, limited color palette, bold dark "
    "outline: a single large {desc}, centered and filling most of the frame, plain flat dark "
    "indigo background, " + PALETTE
    + ", game sprite"
)

# Site repo for each project id. The hub (loco-labo) also receives every icon
# so the overworld map can use them as markers.
SITES = {
    "labo": "loco-labo",
    "llm": "loco-llm",
    "banco": "loco-banco",
    "fosil": "loco-fosil",
    "agente": "loco-agente",
    "convoy": "loco-convoy",
    "notas": "loco-notas",
    "puente": "loco-puente",
    "musa": "loco-musa",
    "ensayo": "loco-ensayo/loco-ensayo",
}

# name -> (template, description, size)
JOBS = {
    "labo-map": (SCENE, "MOONLIT NIGHT, dark blue-green tones, a top-down overworld map of a small countryside valley at night, rolling hills, a winding river with a lake, pine forests, meandering dirt paths and open clearings, seen from directly above, no buildings", SCENE_SIZE),
    "llm-hero": (SCENE, "a tall crooked alchemist tower on a hill at night with glowing round windows, a friendly llama wearing a tiny wizard hat beside a bubbling cauldron, shelves of small potion bottles in many colours", SCENE_SIZE),
    "banco-hero": (SCENE, "a cluttered inventor workbench at night with a row of different graphics cards plugged into a test rig, glowing meters and dials, coiled cables, an open notebook, a small brass trophy", SCENE_SIZE),
    "fosil-hero": (SCENE, "a dim natural history museum hall at night, a big glass display case holding an old green graphics card mounted like a dinosaur fossil skeleton, other dusty computer parts on plinths, a curious visitor holding a lantern", SCENE_SIZE),
    "agente-hero": (SCENE, "a cozy robot workshop at night where small round helper robots work in a loop around a big table, passing tools and paper notes along a circular conveyor belt, gears and blueprints on the walls", SCENE_SIZE),
    "convoy-hero": (SCENE, "a convoy of small cargo trucks driving together in a line along a winding mountain road at night, each truck carrying a glowing computer part, headlights shining", SCENE_SIZE),
    "notas-hero": (SCENE, "a quiet library corner at night, an open field notebook with sketches and pressed leaves on a wooden desk, a candle and a small desk lamp, shelves of worn journals", SCENE_SIZE),
    "puente-hero": (SCENE, "a sturdy stone bridge over a river at night lit by warm lanterns, connecting a small town of glowing houses to a hillside cabin full of blinking computers, tiny people walking across", SCENE_SIZE),
    "musa-hero": (SCENE, "a small round observatory on a hilltop at night, two figures talking together beside a big brass telescope, glowing constellations swirling in the sky", SCENE_SIZE),
    "ensayo-hero": (SCENE, "a small cozy theatre at night, a wooden stage under warm spotlights where translucent glowing actor figures rehearse a scene with a student, red velvet curtains, rows of empty seats", SCENE_SIZE),
    "labo-icon": (ICON, "glowing brass lantern with a tiny circuit board inside", ICON_SIZE),
    "llm-icon": (ICON, "cute llama head wearing a tiny purple wizard hat", ICON_SIZE),
    "banco-icon": (ICON, "graphics card with a small brass medal on it", ICON_SIZE),
    "fosil-icon": (ICON, "dinosaur fossil bone made of green circuit board", ICON_SIZE),
    "agente-icon": (ICON, "small round friendly robot head with glowing eyes", ICON_SIZE),
    "convoy-icon": (ICON, "small cargo truck carrying a graphics card", ICON_SIZE),
    "notas-icon": (ICON, "open notebook with a pencil", ICON_SIZE),
    "puente-icon": (ICON, "small stone arch bridge", ICON_SIZE),
    "musa-icon": (ICON, "glowing lightbulb with a tiny star inside", ICON_SIZE),
    "ensayo-icon": (ICON, "pair of theatre masks", ICON_SIZE),
    "capstone-icon": (ICON, "black graduation mortarboard cap with a golden tassel", ICON_SIZE),
    "picker-icon": (ICON, "brass magnifying glass held over a small graphics card", ICON_SIZE),
    "base-icon": (ICON, "small canvas camping tent with a glowing campfire", ICON_SIZE),
}

HUB_ONLY_ICONS = ["capstone", "picker", "base"]

HERO_WIDTH = 1216
MAP_WIDTH = 1216
ICON_PX = 128        # marker sprite for the hub map
FAVICON_PX = 64


def seed_for(name: str, k: int) -> int:
    return BASE_SEED + list(JOBS).index(name) * 10 + k


def run_limn(prompt: str, size: str, seed: int, out: Path) -> bool:
    cmd = [
        "limn", "generate", prompt,
        "-m", MODEL, "--lora", LORA, "-s", size, "--seed", str(seed),
        "--negative", NEGATIVE, "-o", str(out),
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
    except subprocess.TimeoutExpired:
        print("    FAILED: timed out")
        return False
    if result.returncode != 0 or not out.exists():
        print(f"    FAILED: {(result.stderr or result.stdout).strip()[-400:]}")
        return False
    return True


def cmd_list(_: argparse.Namespace) -> int:
    for name, (_, desc, size) in JOBS.items():
        picked = "picked" if (PICKS / f"{name}.png").exists() else "-"
        cands = len(list(CANDIDATES.glob(f"{name}-*.png")))
        print(f"{name:14} {size:10} candidates={cands} {picked}")
    return 0


def cmd_generate(args: argparse.Namespace) -> int:
    names = args.name or list(JOBS)
    failures = 0
    CANDIDATES.mkdir(parents=True, exist_ok=True)
    for name in names:
        template, desc, size = JOBS[name]
        prompt = template.format(desc=desc)
        for k in range(1, args.candidates + 1):
            out = CANDIDATES / f"{name}-{k}.png"
            if out.exists() and not args.force:
                print(f"  {name}-{k} exists, skipped")
                continue
            print(f"  {name}-{k} seed={seed_for(name, k)} ...", flush=True)
            if not run_limn(prompt, size, seed_for(name, k), out):
                failures += 1
    return 1 if failures else 0


def cmd_pick(args: argparse.Namespace) -> int:
    src = CANDIDATES / f"{args.name}-{args.candidate}.png"
    if not src.exists():
        sys.exit(f"missing candidate: {src}")
    PICKS.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, PICKS / f"{args.name}.png")
    print(f"picked {src.name}")
    return 0


def _crop_subject(img):
    """Crop to the subject: drop the flat background measured from the corners."""
    from PIL import ImageChops, Image

    rgb = img.convert("RGB")
    bg = Image.new("RGB", rgb.size, rgb.getpixel((4, 4)))
    diff = ImageChops.difference(rgb, bg).convert("L").point(lambda v: 255 if v > 28 else 0)
    box = diff.getbbox()
    if not box:
        return rgb
    left, top, right, bottom = box
    side = max(right - left, bottom - top)
    side = int(side * 1.12)
    cx, cy = (left + right) // 2, (top + bottom) // 2
    half = side // 2
    box = (max(cx - half, 0), max(cy - half, 0), min(cx + half, rgb.width), min(cy + half, rgb.height))
    return rgb.crop(box)


def _pixel_downscale(img, px: int, transparent: bool = True):
    """Downscale to a small sprite with hard pixel edges and a keyed-out background."""
    from PIL import Image, ImageChops

    rgb = _crop_subject(img)
    small = rgb.resize((px, px), Image.Resampling.BOX)
    small = small.quantize(colors=32, method=Image.Quantize.MEDIANCUT).convert("RGBA")
    if not transparent:
        return small
    # Key out the flat background (sampled from the corners) so sprites sit on any surface.
    bg = Image.new("RGB", rgb.size, rgb.getpixel((2, 2)))
    mask = ImageChops.difference(rgb, bg).convert("L").point(lambda v: 255 if v > 30 else 0)
    mask = mask.resize((px, px), Image.Resampling.BOX).point(lambda v: 255 if v > 110 else 0)
    small.putalpha(mask)
    return small


def cmd_process(_: argparse.Namespace) -> int:
    from PIL import Image

    done = 0
    for pid, repo in SITES.items():
        site = WORKSPACE / repo
        art_dir = site / "src" / "assets" / "art"

        hero_name = "labo-map" if pid == "labo" else f"{pid}-hero"
        hero_src = PICKS / f"{hero_name}.png"
        if hero_src.exists():
            art_dir.mkdir(parents=True, exist_ok=True)
            img = Image.open(hero_src).convert("RGB")
            width = MAP_WIDTH if pid == "labo" else HERO_WIDTH
            img = img.resize((width, round(img.height * width / img.width)), Image.Resampling.LANCZOS)
            target = art_dir / ("map.webp" if pid == "labo" else "hero.webp")
            img.save(target, "WEBP", quality=88, method=6)
            print(f"  {target.relative_to(WORKSPACE)}")
            done += 1

        icon_src = PICKS / f"{pid}-icon.png"
        if icon_src.exists():
            img = Image.open(icon_src)
            fav = _pixel_downscale(img, FAVICON_PX, transparent=False)
            (site / "public").mkdir(parents=True, exist_ok=True)
            fav.save(site / "public" / "favicon.png")
            art_dir.mkdir(parents=True, exist_ok=True)
            _pixel_downscale(img, ICON_PX).save(art_dir / "icon.png")
            # The hub map needs every project's marker sprite.
            hub_icons = HUB / "src" / "assets" / "art" / "icons"
            hub_icons.mkdir(parents=True, exist_ok=True)
            _pixel_downscale(img, ICON_PX).save(hub_icons / f"{pid}.png")
            print(f"  {repo}/public/favicon.png + icon")
            done += 1
    hub_icons = HUB / "src" / "assets" / "art" / "icons"
    for pid in HUB_ONLY_ICONS:
        src = PICKS / f"{pid}-icon.png"
        if src.exists():
            hub_icons.mkdir(parents=True, exist_ok=True)
            _pixel_downscale(Image.open(src), ICON_PX).save(hub_icons / f"{pid}.png")
            print(f"  hub marker icon: {pid}")
            done += 1
    print(f"processed {done} files")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list").set_defaults(func=cmd_list)
    gen = sub.add_parser("generate")
    gen.add_argument("--name", action="append", choices=list(JOBS))
    gen.add_argument("--candidates", type=int, default=2)
    gen.add_argument("--force", action="store_true")
    gen.set_defaults(func=cmd_generate)
    pick = sub.add_parser("pick")
    pick.add_argument("name", choices=list(JOBS))
    pick.add_argument("candidate", type=int)
    pick.set_defaults(func=cmd_pick)
    sub.add_parser("process").set_defaults(func=cmd_process)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())

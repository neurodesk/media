#!/usr/bin/env python3
"""Validate the Neurodesk media repository.

Checks every tracked asset for:
  * an allowed file extension for the folder it sits in
  * a filename matching the naming convention (lowercase, hyphen-separated)
  * a size within the limits documented in CONTRIBUTING.md
  * accidentally committed design-tool masters or OS cruft

Run locally with:  python3 scripts/check_assets.py
Exits non-zero if anything fails, so it doubles as the CI gate.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

MAX_FILE_BYTES = 2 * 1024 * 1024   # 2 MB
MAX_SVG_BYTES = 500 * 1024         # 500 KB
MAX_DESIGN_BYTES = 8 * 1024 * 1024 # 8 MB, for palette swatches and deck templates

# Folders holding assets, and the extensions each accepts.
ASSET_DIRS: dict[str, set[str]] = {
    "logo/svg": {".svg"},
    "logo/png": {".png"},
    "icons": {".svg", ".png", ".ico", ".webmanifest"},
    "figures": {".svg", ".png", ".pdf"},
    "screenshots": {".png", ".jpg", ".jpeg", ".gif", ".webm"},
    "templates": {".pdf", ".pptx", ".potx", ".odp", ".otp", ".key"},
    # The official colour palette ships as an Illustrator swatch file, so .ai is
    # allowed here and only here. See BRAND.md.
    "palette": {".ai", ".ase", ".json", ".css", ".svg", ".png"},
}

# Formats that belong in the design drive, not in git.
BANNED_EXTENSIONS = {
    ".psd": "layered Photoshop master",
    ".psb": "large Photoshop master",
    ".ai": "Illustrator master",
    ".sketch": "Sketch master",
    ".tif": "uncompressed TIFF",
    ".tiff": "uncompressed TIFF",
    ".mov": "video master",
    ".zip": "archive",
}

# Folders exempt from the BANNED_EXTENSIONS check, for formats they legitimately need.
BANNED_EXEMPTIONS: dict[str, set[str]] = {
    "palette": {".ai"},
}

# <subject>-<variant>[-<size>].<ext> : lowercase alphanumerics separated by hyphens.
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*\.[a-z0-9]+$")

IGNORED_NAMES = {".gitkeep", ".DS_Store", "README.md"}

errors: list[str] = []
warnings: list[str] = []
checked = 0


def human(size: int) -> str:
    return f"{size / 1024:.0f} KB" if size < 1024 * 1024 else f"{size / (1024 * 1024):.1f} MB"


def check_file(path: Path, allowed: set[str], folder: str) -> None:
    global checked
    rel = path.relative_to(REPO)
    name = path.name

    if name in IGNORED_NAMES:
        return

    checked += 1
    ext = path.suffix.lower()

    if ext in BANNED_EXTENSIONS and ext not in BANNED_EXEMPTIONS.get(folder, set()):
        errors.append(
            f"{rel}: {BANNED_EXTENSIONS[ext]} ({ext}) should not be committed. "
            f"Keep it in the design drive and link to it from the folder README."
        )
        return

    if ext not in allowed:
        errors.append(
            f"{rel}: extension '{ext}' not allowed here. "
            f"Allowed: {', '.join(sorted(allowed))}"
        )

    if not NAME_RE.match(name):
        errors.append(
            f"{rel}: filename must be lowercase, hyphen-separated, no spaces or "
            f"underscores (e.g. neurodesk-logo-mono-white.svg)"
        )

    size = path.stat().st_size
    if ext == ".svg":
        cap = MAX_SVG_BYTES
    elif ext in {".ai", ".potx", ".pptx", ".odp", ".otp", ".key"}:
        cap = MAX_DESIGN_BYTES
    else:
        cap = MAX_FILE_BYTES
    if size > cap:
        errors.append(f"{rel}: {human(size)} exceeds the {human(cap)} limit for {ext} files")
    elif size > cap * 0.8:
        warnings.append(f"{rel}: {human(size)}, close to the {human(cap)} limit")

    if ext == ".svg":
        check_svg(path, rel)


def check_svg(path: Path, rel: Path) -> None:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        errors.append(f"{rel}: could not read ({exc})")
        return

    if "<svg" not in text:
        errors.append(f"{rel}: does not look like an SVG (no <svg> element)")
        return

    if "data:image/png;base64" in text or "data:image/jpeg;base64" in text:
        warnings.append(
            f"{rel}: contains an embedded raster image, so it is not a true vector"
        )

    if "sodipodi:" in text or "inkscape:" in text or 'id="Layer_' in text:
        warnings.append(f"{rel}: still has editor metadata — run `npx svgo --multipass {rel}`")

    if "<text" in text:
        warnings.append(
            f"{rel}: contains live <text>; convert text to paths so it renders "
            f"without the font installed"
        )


def main() -> int:
    for folder, allowed in ASSET_DIRS.items():
        directory = REPO / folder
        if not directory.is_dir():
            errors.append(f"{folder}/: expected directory is missing")
            continue
        for path in sorted(directory.rglob("*")):
            if path.is_file():
                check_file(path, allowed, folder)

    # Catch stray assets dumped at the repo root.
    for path in sorted(REPO.glob("*")):
        if path.is_file() and path.suffix.lower() in {
            ".png", ".jpg", ".jpeg", ".svg", ".gif", ".pdf", ".ico",
        }:
            errors.append(
                f"{path.name}: assets belong in a subfolder "
                f"({', '.join(sorted(ASSET_DIRS))}), not the repo root"
            )

    print(f"Checked {checked} asset(s).\n")

    for w in warnings:
        print(f"  warning: {w}")
    if warnings:
        print()

    for e in errors:
        print(f"  ERROR: {e}")

    if errors:
        print(f"\n{len(errors)} error(s). See CONTRIBUTING.md for the rules.")
        return 1

    print("All checks passed." if not warnings else f"No errors ({len(warnings)} warning(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())

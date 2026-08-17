#!/usr/bin/env bash
# Render PNG derivatives from the vector masters in logo/svg/.
#
# Usage:  ./scripts/render-png.sh
# Needs:  rsvg-convert  (brew install librsvg  |  apt install librsvg2-bin)
#
# Output lands in logo/png/ as <name>-<width>.png and is committed to the repo so
# consumers who cannot render SVG have something to point at.

set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$REPO/logo/svg"
OUT="$REPO/logo/png"
WIDTHS=(128 256 512 1024)

if ! command -v rsvg-convert >/dev/null 2>&1; then
  echo "error: rsvg-convert not found." >&2
  echo "  macOS:  brew install librsvg" >&2
  echo "  Debian: sudo apt install librsvg2-bin" >&2
  exit 1
fi

mkdir -p "$OUT"

shopt -s nullglob
svgs=("$SRC"/*.svg)

if [ ${#svgs[@]} -eq 0 ]; then
  echo "No SVGs in logo/svg/ yet — nothing to render."
  exit 0
fi

count=0
for svg in "${svgs[@]}"; do
  base="$(basename "$svg" .svg)"
  for w in "${WIDTHS[@]}"; do
    target="$OUT/${base}-${w}.png"
    rsvg-convert --width="$w" --keep-aspect-ratio --format=png \
      --output="$target" "$svg"
    echo "  rendered $(basename "$target")"
    count=$((count + 1))
  done
done

echo "Done — $count PNG(s) written to logo/png/."

if command -v oxipng >/dev/null 2>&1; then
  echo "Optimising with oxipng..."
  oxipng -o 4 --strip safe --quiet "$OUT"/*.png
  echo "Optimised."
else
  echo "Tip: install oxipng (\`npm i -g oxipng\`) to shrink the output further."
fi

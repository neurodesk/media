# palette/

The official Neurodesk colour palette, in every format anyone is likely to need.

**Hex is canonical.** RGB values are derived from hex by
[`scripts/build_palette.py`](../scripts/build_palette.py), never typed by hand — that is
how the two columns drifted apart in the first place.

## Which file do I want?

| File | Open it with | Use for |
|---|---|---|
| `neurodesk-palette.pptx` | PowerPoint, Keynote, Google Slides, LibreOffice | Looking at the palette; picking colours in a deck. **No paid software needed.** |
| `neurodesk-palette.ase` | Illustrator, Photoshop, InDesign, Affinity, Figma | Loading swatches into a design tool |
| `neurodesk-palette.gpl` | GIMP, Inkscape, Krita | Same, for open-source tools |
| `neurodesk-palette.css` | any text editor | Web work — custom properties, ready to `@import` |
| `neurodesk-palette.json` | any text editor | Scripts, build tooling, generating themes |
| `neurodesk-color-palette.ai` | Illustrator only | The original swatch file, kept for provenance |

`.ai` is listed last deliberately. It requires Illustrator, which most people outside a
university licence do not have, so it should not be the only way to get the palette.

## The colours

| Name | Hex | RGB | Usage |
|---|---|---|---|
| Seafoam green | `#6aa329` | 106, 163, 41 | Primary actions |
| Logo ink | `#101806` | 16, 24, 6 | The dark used in the logo artwork |
| Black | `#0c0e0a` | 12, 14, 10 | Regular text, menu bar |
| Darkest green | `#161c10` | 22, 28, 16 | Successful selection |
| Muted olive green | `#1e2a16` | 30, 42, 22 | Accent background |
| Dark olive green | `#4f7b38` | 79, 123, 56 | Selected buttons, hyperlinks |
| Light green | `#b7d886` | 183, 216, 134 | Hover over a button |
| Lighter green | `#d3e7b6` | 211, 231, 182 | |
| Verdant haze | `#e6f1d6` | 230, 241, 214 | Unselected buttons |
| Pale lime green | `#f0f7e7` | 240, 247, 231 | |
| White | `#ffffff` | 255, 255, 255 | |

### Logo ink is a new entry

`#101806` is the dark used across the logo artwork — stickers, the badge, the bumper
masters, the numbat illustration: eight files in all. It was never in the documented
palette under that hex.

It had been sitting in the *RGB cell* of the "Darkest green" row as `(16, 24, 6)`, which
is exactly `#101806`. That row's *hex* cell said `#161c10`, a colour that appears only in
the website theme and never in artwork. One row, two different colours. They are now
listed separately.

## Regenerating

Edit `PALETTE` in [`scripts/build_palette.py`](../scripts/build_palette.py), then:

```bash
python3 scripts/build_palette.py
```

Every file above except the `.ai` is rebuilt from that one list. Do not hand-edit the
generated files.

## Keeping exports on-palette

Artwork exported from CMYK Illustrator documents does **not** match this palette. The
platform figure exports contain `#1f2b17` where the palette specifies `#1e2a16`, and
`#171d11` where it should be `#161c10` — only one of nine colours survives the round trip
exactly.

Before exporting anything for screen, set **File → Document Color Mode → RGB Color**.
Keep a separate CMYK copy if a print house needs one.

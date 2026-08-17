# logo/

The Neurodesk wordmark and icon mark. **Read [BRAND.md](../BRAND.md) for licensing** —
the logo is a project mark, not CC-BY. Visual standards live in the
[Designer Guide](https://neurodesk.org/developers/designer/).

- `svg/` — vector masters. Source of truth. Edit these.
- `png/` — raster derivatives rendered by CI. Do not hand-edit.

## Inventory

Migrated from the website repo's `public/logos/` and renamed to a single convention:
`neurodesk[-org]-<form>[-pride][-on-dark].<ext>`.

| File | Variant | Use on | Status |
|---|---|---|---|
| `neurodesk-logo.png` | Simple | Light / neutral backgrounds | committed |
| `neurodesk-logo-pride.png` | Simple, Pride | Light / neutral backgrounds | committed |
| `neurodesk-logo-on-dark.png` | Simple | Dark backgrounds | committed |
| `neurodesk-logo-pride-on-dark.png` | Simple, Pride | Dark backgrounds | committed |
| `neurodesk-logo-horizontal.png` | Horizontal lockup | Wide headers | committed |
| `neurodesk-org-logo.png` | With web address | Light / neutral backgrounds | committed |
| `neurodesk-org-logo-pride.png` | With web address, Pride | Light / neutral backgrounds | committed |
| `neurodesk-org-logo-on-dark.png` | With web address | Dark backgrounds | committed |
| `neurodesk-org-logo-pride-on-dark.png` | With web address, Pride | Dark backgrounds | committed |
| `neurodesk-org-logo-horizontal.png` | With web address, horizontal | Wide headers | committed |
| `neurodesk-org-wordmark.png` | Text only, no mark | Where the icon is redundant | committed |

## Known gap: no vector masters

Every published logo is **PNG only**. There is no SVG anywhere, which means the logo
cannot be scaled cleanly for a poster, a print run, or a large display. Producing SVG
masters from the Illustrator source is the highest-value thing to add to this repo.

The logo font is [Scirich](https://github.com/micmas/Scirich-font) — convert text to
paths when exporting so the SVG renders without it installed.

## Regenerating PNGs

```bash
./scripts/render-png.sh
```

Renders each `svg/*.svg` at 128, 256, 512, and 1024 px wide into `png/`.

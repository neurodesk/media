# palette/

The official Neurodesk colour palette.

The authoritative values are documented in the
[Designer Guide](https://neurodesk.org/developers/designer/#color-palette). Primary is
**Seafoam green `#6aa329`**, with nine secondary tones.

`.ai` is allowed in this folder specifically — it is the format the palette ships in —
and nowhere else in the repo.

## Inventory

| File | Format | Purpose | Status |
|---|---|---|---|
| `neurodesk-color-palette.ai` | Illustrator swatches | Design tool import | committed |

## Possible additions

The palette is currently only usable from Adobe tools. Machine-readable exports would
let developers import it directly instead of copy-pasting hex codes:

- `neurodesk-palette.json` — for scripts and build tooling
- `neurodesk-palette.css` — custom properties for web use
- `neurodesk-palette.ase` — swatches for non-Adobe editors

Open an issue if you want these generated.

> **Note:** the logo artwork's ink is `#101806`, which is not in the documented palette
> under that hex — it appears only as the *RGB cell* of the "Darkest green" row, whose
> hex cell (`#161c10`) is used solely in the website theme. That row conflates two
> different colours. Resolve it before generating any derived formats.

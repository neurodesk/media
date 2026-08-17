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
| `neurodesk-color-palette.ai` | Illustrator swatches | Design tool import | pending migration |

## Possible additions

The palette is currently only usable from Adobe tools. Machine-readable exports would
let developers import it directly instead of copy-pasting hex codes:

- `neurodesk-palette.json` — for scripts and build tooling
- `neurodesk-palette.css` — custom properties for web use
- `neurodesk-palette.ase` — swatches for non-Adobe editors

Open an issue if you want these generated.

> **Note:** the RGB values in the Designer Guide's table disagree with their own hex
> codes in 8 of 10 rows. Resolve that before generating any derived formats — see
> [MIGRATION.md](../MIGRATION.md#also-worth-fixing-while-youre-in-there).

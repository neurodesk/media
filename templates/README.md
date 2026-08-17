# templates/

Editable templates people start from: conference posters, and slide decks.

This folder was called `slides/` until 17 August 2026. It was renamed because "slides"
described only part of what belongs here.

## Inventory

| File | Format | Purpose |
|---|---|---|
| `neurodesk-poster-vertical.potx` | PowerPoint template | Portrait conference poster |
| `neurodesk-poster-horizontal.potx` | PowerPoint template | Landscape conference poster |

### Pending

The **Neurodesk slide template** (`20250624-neurodesk-slides.potx`) is not here yet. The
current export is 46.8 MB, well over the 8 MB limit, and roughly 21 MB of that is the
same images stored several times over — `image22.emf` and `image6.emf` are byte-identical
9.4 MB copies, and there are four more such pairs.

Re-saving from PowerPoint with **File → Compress Pictures**, and deleting unused layouts
and masters, should collapse the duplicates. Add it here once it fits.

## Finished decks are not stored here

Delivered talks and the Neurodesk overview deck live outside this repository. See
**Template presentations** in the
[Designer Guide](https://neurodesk.org/developers/designer/#template-presentations) for
how to get them.

Commit editable templates (`.potx`, `.otp`), not finished decks (`.pptx`) — people should
start from a blank canvas, not someone else's talk.

## Adding a template

Keep it under 8 MB. Before committing:

- **File → Compress Pictures**, targeting 150 ppi
- delete unused slide layouts and masters
- strip embedded video and audio — link to it instead
- check for the same image placed on many slides; PowerPoint often stores repeats

Use the palette in [`palette/`](../palette/) and the fonts named in the
[Designer Guide](https://neurodesk.org/developers/designer/#typography).

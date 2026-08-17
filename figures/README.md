# figures/

Diagrams and conceptual illustrations — architecture diagrams, workflow schematics, and
figures reused across docs, papers, posters, and talks.

CC-BY-4.0. Anyone may reuse these with attribution:
`Neurodesk (https://neurodesk.org), CC BY 4.0`

## Inventory

| File | Describes | Notes |
|---|---|---|
| `neurodesk-contribution-workflow.svg` | How to contribute to Neurodesk | True vector, 360 KB |
| `neurodesk-contribution-workflow-screenshots.svg` | Same workflow, annotated with UI captures | 8.1 MB, **size-exempt** — see below |
| `neurodesk-tutorials-vs-examples.svg` | Difference between tutorials and examples | 105 KB, some embedded raster |
| `neurodesk-platform.png` | Platform overview — community, containers, target environments | 3000 px wide |
| `neurodesk-platform-panels.png` | Same, with **a**–**d** panel labels for papers | 3000 px wide |
| `neurodesk-platform-with-build.png` | Platform overview including Build & Test and Submit | 3000 px wide |
| `neurodesk-platform-with-build-panels.png` | Same, with **a**–**e** panel labels for papers | 3000 px wide |
| `neurodesk-platform.svg` | All four artboards, full image resolution | 96 MB, **size-exempt** — see below |

The four platform PNGs come from the four artboards of `neurodesk-platform.ai` in the
design drive. They were exported at ~32 megapixels and resampled here to 3000 px wide —
still 300 ppi across a 10-inch figure. The full-resolution exports are kept in
`1-neurodesk/figures/architecture/_full-res-exports/`.

## The size-exempt figures

`neurodesk-contribution-workflow-screenshots.svg` is ~100% embedded base64 raster — it is
a composite of UI screenshots in an SVG wrapper rather than a real vector. `svgo` recovers
about 0.2%, so the 500 KB SVG cap cannot be met without changing format.

It is listed in `SIZE_EXEMPTIONS` in `scripts/check_assets.py` with a 10 MB ceiling, so CI
accepts it but will still fail if it grows further. Keep that list short — each entry is a
deliberate exception, not a precedent.

If a smaller form is ever needed, a downsampled PNG export is the right answer; a 0.76 MB
PDF of the same figure also exists in the design drive.

`neurodesk-platform.svg` is exempt at 96 MB by explicit decision. Two things to know
about it: GitHub's hard limit is 100 MB per file, so it has little headroom; and every
clone of this repo downloads it. The same content is available as the four PNGs above, so
prefer those unless you specifically need this file.

### Source colour warning

`neurodesk-platform.ai` is a **CMYK** document, and the conversion shifts the palette:
exports contain `#1f2b17` where the brand palette specifies `#1e2a16`, and `#171d11`
where it should be `#161c10`. Only one of nine palette colours survives the round trip
exactly. Switch the document to RGB (File → Document Color Mode) before re-exporting
anything destined for screen.

## Rules of thumb

- Commit SVG, not a raster export of a diagram.
- Convert text to paths so rendering doesn't depend on installed fonts. All three figures
  here currently contain live `<text>` and will render in a substitute font on machines
  without it.
- Run `npx svgo --multipass <file>` before committing.
- Use the palette in [`palette/`](../palette/) so figures look like a set.
- Check legibility in greyscale — many journals still print in black and white.

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

## The size-exempt figure

`neurodesk-contribution-workflow-screenshots.svg` is ~100% embedded base64 raster — it is
a composite of UI screenshots in an SVG wrapper rather than a real vector. `svgo` recovers
about 0.2%, so the 500 KB SVG cap cannot be met without changing format.

It is listed in `SIZE_EXEMPTIONS` in `scripts/check_assets.py` with a 10 MB ceiling, so CI
accepts it but will still fail if it grows further. Keep that list short — each entry is a
deliberate exception, not a precedent.

If a smaller form is ever needed, a downsampled PNG export is the right answer; a 0.76 MB
PDF of the same figure also exists in the design drive.

## Rules of thumb

- Commit SVG, not a raster export of a diagram.
- Convert text to paths so rendering doesn't depend on installed fonts. All three figures
  here currently contain live `<text>` and will render in a substitute font on machines
  without it.
- Run `npx svgo --multipass <file>` before committing.
- Use the palette in [`palette/`](../palette/) so figures look like a set.
- Check legibility in greyscale — many journals still print in black and white.

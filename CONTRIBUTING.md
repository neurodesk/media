# Contributing assets

Thanks for adding to the Neurodesk asset library. The rules below exist so the repo
stays small, cloneable, and hot-linkable.

## Before you add anything

Confirm you have the right to publish it. Do **not** commit:

- Figures from an unpublished paper (wait until publication, or the preprint is out).
- Screenshots containing participant data, real subject IDs, or identifiable scans.
- Stock imagery, icon sets, or fonts whose licence forbids redistribution. (The logo
  font, [Scirich](https://github.com/micmas/Scirich-font), is not redistributed here —
  convert text to paths instead.)
- Third-party logos, unless you are illustrating an integration and the vendor's brand
  guidelines allow it.

If you are unsure, open an issue and ask before opening a PR.

## Adding a file

1. Fork this repo and create a branch.
2. Drop the file into the right folder (see the table in the [README](README.md)).
3. Name it `<subject>-<variant>[-<size>].<ext>`, lowercase and hyphen-separated.
4. Add a row to that folder's `README.md` table — what it is and where it is used.
5. Open a PR against `main`. CI will check naming, format, and size.

## Format rules

| Asset type | Commit | Never commit |
|---|---|---|
| Logos, icons | SVG master | Only a PNG with no vector source |
| Colour palette | `.ai` in `palette/` only | `.ai` anywhere else |
| Diagrams, figures | SVG (or PDF for print-only) | Screenshots of a diagram |
| UI screenshots | PNG | JPEG (artefacts on text) |
| Photos | JPEG, quality ~85 | Uncompressed TIFF |
| Animation | WebM, or GIF under the cap | MOV / ProRes masters |

**Always commit a vector master.** A PNG-only logo cannot be resized for a poster or a
print run. If you only have a raster version, say so in the PR and someone will help
trace it.

### Prepare SVGs before committing

Design tools emit enormous SVGs full of editor metadata. Clean them:

```bash
npx svgo --multipass logo/svg/your-file.svg
```

Then check by eye that it still renders. Remove embedded raster images and convert text
to paths so the file doesn't depend on a font being installed.

### Optimise PNGs

```bash
npx oxipng -o 4 --strip safe path/to/file.png
```

## Size limits

CI enforces these:

| | Limit |
|---|---|
| Any single file | **2 MB** |
| SVG | **500 KB** |
| Palette swatches and deck templates (`.ai`, `.potx`, `.pptx`, `.odp`, `.key`) | **8 MB** |
| Total repo growth per PR | **5 MB** |

A named file may be granted a higher ceiling via `SIZE_EXEMPTIONS` in
`scripts/check_assets.py`, but only where no smaller format exists — an SVG that is
entirely embedded raster, for example. Each entry records the reason and its own cap, so
CI still fails if the file grows past it. Ask before adding one.

**PowerPoint files need attention before committing.** Run File → Compress Pictures,
delete unused layouts and masters, and strip embedded video. PowerPoint frequently stores
the same image several times; the current slide template is 46.8 MB of which ~21 MB is
duplicates.

This repo does **not** use Git LFS, deliberately: LFS bandwidth is billed against the
org quota, and `raw.githubusercontent.com` serves LFS pointer text rather than the real
image — which would break every hot-link in our docs.

**Where large binaries go instead.** PSD, AI, Sketch, layered TIFF, and video masters
live in the shared Neurodesk design drive, not here. Commit the exported SVG/PNG and put
a link to the master in the folder README's `Source` column. If a master genuinely must
be version-controlled, open an issue first so we can discuss it.

## Generated files

`logo/png/` is produced from `logo/svg/` by CI. Don't hand-edit anything there — change
the SVG and let the workflow re-render. To preview locally:

```bash
./scripts/render-png.sh
```

Requires `rsvg-convert` (`brew install librsvg` or `apt install librsvg2-bin`).

## Checking your work locally

```bash
python3 scripts/check_assets.py
```

Same script CI runs. It validates naming, extensions, and sizes across the repo.

## Changing the logo itself

Logo changes need sign-off from the Neurodesk maintainers, not just a passing CI run.
Tag a maintainer on the PR and expect a conversation. Also update [BRAND.md](BRAND.md)
if the palette or clear-space rules change.

## Removing or replacing an asset

Deleting a file breaks every hot-link pointing at it. Prefer to:

1. Add the new version alongside the old one.
2. Update the folder README to mark the old one **deprecated**, with the replacement path.
3. Remove it only after a release cycle, in a PR titled `remove deprecated: <file>`.

Consumers who need stability should pin to a tag rather than `main`.

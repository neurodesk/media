# Migration: moving brand assets into this repo

The Neurodesk logos, palette, and templates currently live in
`neurodesk.github.io/static/logos/` and are published at
`https://neurodesk.org/static/logos/…`. This repo becomes the source of truth for those
files; the [Designer Guide](https://neurodesk.org/developers/designer/) stays as the
human-facing guide and links here for downloads.

**Status:** the files have been copied in under the new names (step 1 done). Steps 2–6
below are still outstanding.

## Why rename

The published set uses three different conventions at once — underscores
(`neurodesk_horizontal.png`), dots inside the stem (`neurodesk.org-pride.png`), and
mixed case (`Neurodesk-vertical-poster.potx`). The dot is the real problem: it makes the
stem look like a file extension, breaks naive extension parsing, and is awkward in URLs
and LaTeX `\includegraphics`.

New convention: `neurodesk[-org]-<form>[-pride][-on-dark].<ext>`, lowercase, hyphens only.

## Rename map

### Logos → `logo/png/`

| Current | New |
|---|---|
| `neurodesk.png` | `neurodesk-logo.png` |
| `neurodesk-pride.png` | `neurodesk-logo-pride.png` |
| `neurodesk-on-dark.png` | `neurodesk-logo-on-dark.png` |
| `neurodesk-pride-on-dark.png` | `neurodesk-logo-pride-on-dark.png` |
| `neurodesk_horizontal.png` | `neurodesk-logo-horizontal.png` |
| `neurodesk.org.png` | `neurodesk-org-logo.png` |
| `neurodesk.org-pride.png` | `neurodesk-org-logo-pride.png` |
| `neurodesk.org-on-dark.png` | `neurodesk-org-logo-on-dark.png` |
| `neurodesk.org-pride-on-dark.png` | `neurodesk-org-logo-pride-on-dark.png` |
| `neurodesk.org_horizontal.png` | `neurodesk-org-logo-horizontal.png` |
| `neurodesk.org-no-logo.png` | `neurodesk-org-wordmark.png` |

### Palette → `palette/`

| Current | New |
|---|---|
| `Neurodesk-color-palette.ai` | `neurodesk-color-palette.ai` |

### Templates → `templates/`

> This folder was called `slides/` until 17 August 2026, renamed because its
> contents are all poster templates.

| Current | New |
|---|---|
| `Neurodesk-vertical-poster.potx` | `neurodesk-poster-vertical.potx` |
| `Neurodesk-horizontal-poster.potx` | `neurodesk-poster-horizontal.potx` |

## Steps

1. ~~**Copy the files into this repo** under the new names.~~ Done — copied from
   `neurodesk.github.io-astro/public/logos/` and `public/template-presentations/`.
   Originals left in place deliberately; see step 6.
2. **Trace vector masters.** Every logo is currently PNG-only — there is no SVG anywhere.
   This is the biggest gap: PNG can't be scaled for a poster or a print run. Produce
   `logo/svg/*.svg` masters from the Illustrator source, commit them, and let CI render
   the PNG derivatives. Until then `logo/png/` holds hand-made files.
3. **Run `python3 scripts/check_assets.py`** — it should pass clean.
4. **Add redirects** on the website so old URLs keep working (below).
5. **Update the Designer Guide** download links to point at this repo.
6. **Only then** remove the originals from `neurodesk.github.io/static/logos/`.

## Keeping old URLs alive

Existing links from papers, slide decks, and third-party sites point at
`neurodesk.org/static/logos/…`. Those must not 404.

Hugo handles this with aliases. In `neurodesk.github.io`, add a redirect page per old
path, or configure a server-side redirect map:

```
/static/logos/neurodesk.png                   →  https://raw.githubusercontent.com/neurodesk/media/main/logo/png/neurodesk-logo.png
/static/logos/neurodesk_horizontal.png        →  https://raw.githubusercontent.com/neurodesk/media/main/logo/png/neurodesk-logo-horizontal.png
/static/logos/neurodesk.org-pride.png         →  https://raw.githubusercontent.com/neurodesk/media/main/logo/png/neurodesk-org-logo-pride.png
…and so on for each row in the table above
```

Simplest robust option: keep the files in `static/logos/` as-is for one release cycle so
nothing breaks, and have the Designer Guide link to the repo. Retire them once traffic
to the old paths drops off.

## How the website consumes the repo afterwards

Pick one:

- **Git submodule** — `git submodule add https://github.com/neurodesk/media.git assets/media`,
  then reference `assets/media/logo/…` in Hugo. Deterministic, pinned to a commit.
- **Sync action** — a scheduled workflow in `neurodesk.github.io` that copies the current
  `logo/` into `static/`. Simpler for contributors, but can drift.
- **Hot-link** — point at `raw.githubusercontent.com` or jsDelivr directly. No build
  step, but adds a third-party dependency to page loads.

Submodule is the usual choice for a docs site that already uses them — the site repo's
README shows it already clones with `--recurse-submodules`.

## Also worth fixing while you're in there

The Designer Guide's colour table lists RGB values that don't match their own hex codes
in 8 of 10 rows:

| Colour | Hex | Listed RGB | Actual RGB |
|---|---|---|---|
| Seafoam green | `#6aa329` | `(106, 163, 41)` | correct |
| Black | `#0c0e0a` | `(5, 8, 2)` | `(12, 14, 10)` |
| Darkest green | `#161c10` | `(16, 24 6)` — missing comma | `(22, 28, 16)` |
| Muted olive green | `#1e2a16` | `(26, 41, 10)` | `(30, 42, 22)` |
| Dark olive green | `#4f7b38` | `(79, 122, 31)` | `(79, 123, 56)` |
| Light green | `#b7d886` | `(181, 224, 133)` | `(183, 216, 134)` |
| Lighter green | `#d3e7b6` | `(211, 237, 182)` | `(211, 231, 182)` |
| Verdant Haze | `#e6f1d6` | `(230, 245, 214)` | `(230, 241, 214)` |
| Pale Lime Green | `#f0f7e7` | `(240, 249, 231)` | `(240, 247, 231)` |
| White | `#ffffff` | `(255, 255, 255)` | correct |

Check which column the design team considers authoritative before correcting — if the
RGB values are the intended colours, the hex codes are what need changing, not the RGB.

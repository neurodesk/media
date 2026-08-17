# media

> Shared visual assets for the [Neurodesk](https://neurodesk.org) project — logo source
> files, diagrams, figures, and screenshots used across Neurodesk docs, sites, papers,
> and talks.

[![Licence: CC BY 4.0](https://img.shields.io/badge/licence-CC--BY--4.0-6BA442.svg)](LICENSE)
[![Brand guidelines](https://img.shields.io/badge/logo-see%20BRAND.md-1E2327.svg)](BRAND.md)

One place to find the current version of any Neurodesk visual, so nobody has to dig
through Slack or an old slide deck for the logo again.

## Licensing at a glance

| What | Terms |
|---|---|
| Figures, diagrams, screenshots | [CC-BY-4.0](LICENSE) — reuse freely with attribution |
| The Neurodesk logo and name | Project marks — see [BRAND.md](BRAND.md) |

Visual standards — palette, typography, capitalization — are documented in the
[Neurodesk Designer Guide](https://neurodesk.org/developers/designer/), which stays the
canonical reference. This repo holds the files; the guide explains how to use them.


Attribution string: `Neurodesk (https://neurodesk.org), CC BY 4.0`

## Layout

```
logo/
  svg/          Vector masters — the source of truth for the mark
  png/          Rendered raster derivatives (generated, do not hand-edit)
icons/          Icon mark sources plus the full favicon set
figures/        Diagrams and conceptual illustrations for docs and papers
screenshots/    UI captures of Neurodesktop, the app, and web tools
templates/      Poster and deck templates (.potx)
palette/        Official colour palette source files
scripts/        Tooling used by CI and by contributors
```

Every asset folder has its own `README.md` describing what belongs there.

## Using an asset

### In Markdown, on a website, or in a README

Hot-link the raw file. Pin to a tag rather than `main` if you need the image to stay
stable over time.

```markdown
![Neurodesk](https://raw.githubusercontent.com/neurodesk/media/main/logo/svg/neurodesk-logo.svg)
```

| Need | URL pattern |
|---|---|
| Always latest | `https://raw.githubusercontent.com/neurodesk/media/main/<path>` |
| Pinned to a release | `https://raw.githubusercontent.com/neurodesk/media/v1.0.0/<path>` |
| CDN-cached (better for high traffic) | `https://cdn.jsdelivr.net/gh/neurodesk/media@main/<path>` |

`raw.githubusercontent.com` is served with `Content-Type: image/svg+xml` and works in
Markdown, HTML, and most static site generators. It is rate-limited, so prefer the
jsDelivr URL for anything embedded on a high-traffic page.

### In a paper, poster, or talk

Download the SVG from `logo/svg/` or `figures/` and place it directly — vectors stay
crisp at any print size. If your tooling cannot handle SVG, use the largest PNG in
`logo/png/`. Credit as above.

### As a git submodule

For repos that need the assets at build time:

```bash
git submodule add https://github.com/neurodesk/media.git assets/media
```

## Naming convention

```
<subject>-<variant>[-<size>].<ext>
```

Lowercase, hyphen-separated, no spaces or underscores. Examples:

- `neurodesk-logo.svg` — the primary mark
- `neurodesk-logo-mono-white.svg` — reverse variant for dark backgrounds
- `neurodesk-logo-512.png` — a 512 px wide raster derivative
- `neurodesktop-architecture.svg` — a figure
- `neurodesktop-jupyter-launcher.png` — a screenshot

CI rejects filenames that don't match this pattern.

## Formats

| Use | Format |
|---|---|
| Logos, icons, diagrams | **SVG** — always commit a vector master |
| Screenshots, photos | **PNG** (lossless UI) or **JPEG** (photographic) |
| Animation | **GIF** or **WebM**, under the size cap |

This repo deliberately does **not** use Git LFS. Binary source files (PSD, AI, TIFF,
video masters) are kept out of the repo — see [CONTRIBUTING.md](CONTRIBUTING.md) for
where they live and what the size limits are.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). In short: fork, add your file under the right
folder using the naming convention above, update that folder's README table, and open a
PR. CI checks naming, format, and file size automatically.

## Related repositories

- [neurodesk.github.io](https://github.com/neurodesk/neurodesk.github.io) — project website (staging)
- [neurodesk.org](https://github.com/neurodesk/neurodesk.org) — project website (production)
- [Designer Guide](https://neurodesk.org/developers/designer/) — visual standards and usage examples
- [neurodesktop](https://github.com/neurodesk/neurodesktop) — the containerised desktop environment
- [neurocontainers](https://github.com/neurodesk/neurocontainers) — container build recipes

_Information on the **Neurodesk** project is available at [neurodesk.org](https://neurodesk.org)._

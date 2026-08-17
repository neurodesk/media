# icons/

Square marks and the favicon set: anything that needs to read clearly at 16–64 px.

## Source icons

The scalable originals. Everything else here derives from these.

| File | Size | What it is |
|---|---|---|
| `neurodesk-icon.svg` | 980 × 981 | The icon mark — box, brain, green electrodes. Outlined, no font dependency. This is what the favicon set is rendered from. |
| `neurodesk-icon-solid.svg` | — | Solid dark box and brain |
| `neurodesk-icon-outline.svg` | — | White / outline treatment of the same mark |
| `neurodesk-icon-green-circle.png` | — | White box and brain inside a green circle |

All SVGs here have been run through `svgo --multipass` and have zero live `<text>`.

## Favicon set

| File | Purpose |
|---|---|
| `neurodesk-favicon.ico` | Multi-resolution `.ico` for legacy browsers |
| `neurodesk-favicon-16.png` | 16 × 16 |
| `neurodesk-favicon-32.png` | 32 × 32 |
| `neurodesk-apple-touch-icon.png` | 180 × 180, iOS home screen |
| `neurodesk-android-chrome-192.png` | 192 × 192, Android home screen |
| `neurodesk-android-chrome-512.png` | 512 × 512, PWA splash |
| `neurodesk-mstile-150.png` | 150 × 150, Windows tile |
| `neurodesk-safari-pinned-tab.svg` | Safari pinned-tab mask |
| `neurodesk.webmanifest` | Web app manifest |

Taken from `neurodesk.github.io-astro/public/favicons/` on 17 August 2026, which is
byte-identical to the Hugo site's set for every file.

### These are renamed — you will need to adjust when deploying

Browsers and site config reference favicons by **exact filename**, and the names here
follow this repository's convention instead (`neurodesk-` prefix, no `WxH` suffix). That
is deliberate: this repo stores assets, it isn't a deployment.

To use them on a site, copy them out and rename to whatever your framework expects. For
reference, the current Neurodesk sites use:

| Here | On the sites |
|---|---|
| `neurodesk-favicon.ico` | `favicon.ico` |
| `neurodesk-favicon-16.png` | `favicon-16x16.png` |
| `neurodesk-favicon-32.png` | `favicon-32x32.png` |
| `neurodesk-apple-touch-icon.png` | `apple-touch-icon.png` |
| `neurodesk-android-chrome-192.png` | `android-chrome-192x192.png` |
| `neurodesk-android-chrome-512.png` | `android-chrome-512x512.png` |
| `neurodesk-mstile-150.png` | `mstile-150x150.png` |
| `neurodesk-safari-pinned-tab.svg` | `safari-pinned-tab.svg` |
| `neurodesk.webmanifest` | `site.webmanifest` |

`neurodesk.webmanifest`'s `icons[].src` values point at the filenames **as they are in
this folder**, so the bundle is self-consistent. Rewrite them to match your deployment
paths when you copy it out.

## Two upstream bugs found while assembling this

Neither is fixed here — they need fixing in the site repos.

1. **`site.webmanifest` icon paths 404.** It lists `/android-chrome-192x192.png` and
   `/android-chrome-512x512.png`, but the files are served from `/favicons/`. Both
   entries resolve to nothing. `name` and `short_name` are also empty strings. The copy
   in this folder has corrected values, so use it as the reference when fixing upstream.
2. **`1-neurodesk/website/static/apple-touch-icon.png` is stale.** It is 37,808 bytes;
   both live sites ship a different 4,748-byte file. The OneDrive copy is not the one in
   production — the version here came from the Astro repo.

Also noted: `1-neurodesk/website/static/favicon2-16x16.png` is 57 KB and appears nowhere
else in any repo. A 16 × 16 PNG should be around 1 KB, so it is almost certainly not
16 × 16 and not in use. Not copied here.

## Regenerating the favicon set

All raster sizes derive from `neurodesk-icon.svg`. To re-render after the mark changes:

```bash
for s in 16 32 180 192 512; do
  rsvg-convert --width=$s --keep-aspect-ratio --format=png \
    --output=neurodesk-favicon-$s.png neurodesk-icon.svg
done
```

Then rename to the table above and rebuild the `.ico` with
`magick neurodesk-favicon-16.png neurodesk-favicon-32.png neurodesk-favicon.ico`.

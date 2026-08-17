# screenshots/

UI captures of Neurodesktop, the Neurodesk app, and the web tools.

## Naming

```
<subject>-<what-it-shows>.png
```

Lowercase, hyphen-separated. The subject is the tool; the rest describes what is on
screen.

| Good | Why |
|---|---|
| `neurodesktop-jupyter-launcher.png` | tool, then what's visible |
| `neurodeskapp-install-macos.png` | platform belongs in the description |
| `neurocontainers-build-log.png` | sorts next to other neurocontainers shots |

**No version number in the filename.** The version captured goes in the table below
instead. That way re-shooting a screenshot against a newer build keeps the same path, and
every link to it — from the docs site, a README, or a paper — keeps working.

## Before you commit

- **Scrub identifying data.** No real subject IDs, participant names, file paths
  containing usernames, tokens, hostnames, or email addresses.
- Capture at 2× / retina, then downscale — avoids blur on high-DPI displays.
- Use a clean window: default theme, no unrelated tabs, no personal bookmarks bar.
- PNG, not JPEG. JPEG artefacts ruin small text.
- Crop to the relevant region. A full 4K desktop to show one dialog wastes everyone's
  bandwidth and pushes against the 2 MB cap.
- Run `npx oxipng -o 4 --strip safe <file>` before committing.

## Keeping them current

Screenshots date faster than anything else in this repo. When a UI changes:

1. Replace the file in place, keeping the same name.
2. Update the "Version captured" cell below.

Only rename or delete if the feature itself is gone — and if so, follow the deprecation
process in [CONTRIBUTING.md](../CONTRIBUTING.md#removing-or-replacing-an-asset).

## Inventory

| File | Shows | Version captured | Appears in |
|---|---|---|---|
| _none yet_ | | | |

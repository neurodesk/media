# templates/

Reusable presentation material: conference poster templates, and deck templates for
talks about Neurodesk.

This folder was called `slides/` until 17 August 2026. It was renamed because everything
in it is a **poster** template, and "slides" was misleading.

## Inventory

| File | Format | Purpose |
|---|---|---|
| `neurodesk-poster-vertical.potx` | PowerPoint template | Portrait conference poster |
| `neurodesk-poster-horizontal.potx` | PowerPoint template | Landscape conference poster |

## Not stored here

The **Neurodesk overview slide deck** lives on UQ SharePoint and is access-controlled to
the Neurodesk team. Request access by emailing <mail.neurodesk@gmail.com>. It stays
there rather than moving here — it is internal, frequently edited, and too large for a
git repo.

If a version of it is ever cleared for public release, export it to `.potx` and add it
to the table above.

## Adding a template

Commit the editable template (`.potx`, `.otp`) rather than a finished deck (`.pptx`), so
people start from a blank canvas. Keep it under 8 MB — strip embedded video and
downsample images first. Use the palette in [`palette/`](../palette/) and the fonts named
in the [Designer Guide](https://neurodesk.org/developers/designer/#typography).

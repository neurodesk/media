# font/

**Scirich Regular** — the Neurodesk display typeface.

A modified version of [Aldrich](https://fonts.google.com/specimen/Aldrich) by Matt
McInerney, adapted and renamed by Michèle Masson-Trottier in April 2025 for the Sciget
and Neurodesk logos. Licensed under the
[SIL Open Font License 1.1](LICENSE.txt), as is the original.

Upstream: [micmas/Scirich-font](https://github.com/micmas/Scirich-font)

## Files

| File | What it is |
|---|---|
| `Scirich-Regular.ttf` | Installable TrueType font, 251 glyphs, full basic Latin |
| `Scirich-Regular.sfd` | FontForge source, for editing |
| `LICENSE.txt` | SIL OFL 1.1 — **must** travel with the font |

Filenames keep their vendor casing rather than this repo's lowercase convention, because
font filenames conventionally match the family name.

## Modifications from Aldrich

- Minor adjustments to spacing and glyph shapes
- Metadata and naming updated
- Renamed to "Scirich Regular", as the OFL requires derivatives to use a different name

## If you redistribute it

The OFL obliges you to:

- include the full `LICENSE.txt`
- not use the Reserved Font Name "Aldrich"
- attribute Matt McInerney and describe your changes
- keep it under the OFL — it cannot be relicensed

You may use it in personal, academic, or commercial projects, embed it in websites, apps
and print, and modify and redistribute it under a new name.

## Scirich is not NeuroRich

There are **two** Aldrich derivatives by the same designer, and they are different
typefaces:

- **Scirich** — this one, shipped here
- **NeuroRich** — referenced by the vertical logo masters, which draw the wordmark as
  live text in it

NeuroRich exists only as FontForge source (`Aldrich-NEURODESK-Regular.sfd` in the design
drive); no installable `.ttf` has been produced. Until one is, the `.ORG` and on-dark
vertical logo variants cannot be exported with correct lettering.

The [Designer Guide](https://neurodesk.org/developers/designer/#typography) names Scirich
as the logo font while the artwork uses NeuroRich. That contradiction is unresolved.

## Web use

Only `.ttf` is shipped. For a website, generate `.woff2` — roughly a third the transfer
size:

```bash
pip install fonttools brotli
python3 -c "
from fontTools.ttLib import TTFont
f = TTFont('Scirich-Regular.ttf'); f.flavor = 'woff2'
f.save('Scirich-Regular.woff2')"
```

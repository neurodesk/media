# Shared Neurodesk screenshots

This is the canonical library for screenshots that can be reused across Neurodesk
documentation. Link to these files directly; do not copy them into another repository.
Tutorial-specific scientific results can remain beside their tutorial assets.

Use the same path when refreshing an image. Tool versions and capture dates belong
in this inventory, rather than in filenames. The `*-guide.png` files are the one
published copy of each numbered menu/control screenshot. Unmarked working captures
are not also committed. The launcher has three intentional guide variants because
each points at a different destination.

## Inventory

Platform captures were made on 20 October 2026; Freeview startup, MRIQC terminal and MFCSC launch captures were added on 21 October 2026. Click-guide colours and launcher alignment were refreshed on 21 October 2026. Desktop captures use the VNC
desktop at its native 1280 × 720 proportions. Menus show actual installed entries;
an entry's presence does not establish that its launcher or a full analysis works.
See the NeurodeskEDU tutorial audit for execution results and workarounds.

| File | Shows / version captured | Consumers |
|---|---|---|
| `neurodesktop-jupyter-launcher.png` | Clean Neurodesk JupyterLab launcher | General platform documentation |
| `neurodesktop-launcher-desktop.png` | 1: RDP; 2: VNC | NeurodeskEDU access guide, fMRIPrep, MRIQC, MRSIProc |
| `neurodesktop-launcher-terminal.png` | JupyterLab terminal tile | NeurodeskEDU access guide, Conda |
| `neurodesktop-launcher-notebook.png` | Python notebook tile | NeurodeskEDU access guide |
| `neurodesktop-desktop.png` | Empty Neurodesktop workspace | NeurodeskEDU access guide |
| `neurodesktop-application-menu.png` | Neurodesk tool categories | NeurodeskEDU access guide |
| `neurodesktop-terminal.png` | Empty LXTerminal; commands go after the prompt | NeurodeskEDU access guide, SWI, ROMEO |
| `launch-mne-guide.png` | Neurodesk → Electrophysiology → mne → code 0.23.4 | MNE tutorial; reusable editor launch guide |
| `launch-fieldtrip-guide.png` | FieldTrip 20211114 | FieldTrip tutorial |
| `launch-workbench-guide.png` | Connectome Workbench 1.5.0 | Workbench tutorial |
| `launch-fmriprep-guide.png` | fMRIPrep 25.2.6 | fMRIPrep tutorial |
| `launch-mriqc-guide.png` | MRIQC 24.0.2 | MRIQC tutorial |
| `launch-physio-guide.png` | physioGUI r2021a | PhysIO tutorial and batch workflow |
| `launch-spm-guide.png` | spm12GUI r7771 | SPM tutorial; reusable SPM launch guide |
| `launch-matlab-guide.png` | matlabGUI 2022a | MATLAB tutorial |
| `launch-lcmodel-guide.png` | LCModel 6.3 terminal launcher | LCModel tutorial |
| `launch-clear-swi-guide.png` | CLEAR-SWI 1.7.0 | SWI tutorial |
| `launch-itksnap-guide.png` | itksnapGUI 4.4.0 | SWI and ROMEO tutorials |
| `launch-romeo-guide.png` | ROMEO 3.2.8 menu entry | ROMEO tutorial |
| `spm-change-directory-guide.png` | SPM Utils → CD | SPM and PhysIO tutorials |
| `spm-open-batch-guide.png` | SPM Batch button | PhysIO and batch workflow tutorials |
| `freeview-start.png` | Freeview 8.2.0 fully opened, before loading an image | FreeSurfer GUI tutorial |
| `mriqc-loaded-terminal.png` | MRIQC 24.0.2 loaded terminal and resolved executable | MRIQC tutorials |
| `launch-mfcsc-guide.png` | Neurodesk → Functional Imaging → mfcsc → mfcsc 1.1 | MFCSC tutorial |
| `freeview-menu-guide.png` | Freeview 8.2.0: Load Volume and Load Surface | FreeSurfer GUI tutorial |

Dataset downloads, selected file paths and scientific results belong in NeurodeskEDU, grouped by tutorial. The fsaverage walkthrough and MFCSC download screenshots have moved there; their generic application-opening controls stay here.

## Refreshing click guides

Capture the real interface without annotations and keep the working capture outside
the repository. Preserve its dimensions, or update the marker coordinates in
`scripts/screenshot-guides.json`. The manifest identifies each expected source name
and the canonical published output name.

With Pillow installed:

```bash
python scripts/render_screenshot_guides.py --source-dir /path/to/working-captures
```

Omit `--source-dir` to regenerate only the launcher variants from the shared launcher
master. The renderer centres numbers using their glyph bounds and uses the Neurodesk green palette. It adds boxes, leader lines and numbers; it does not synthesize UI.
Exports preserve full PNG colours without resizing. Check every resulting guide
visually, then optimize it with `oxipng -o 4 --strip safe` and run
`python scripts/check_assets.py`.

Use a stable media tag when an immutable published tutorial needs a pinned capture.
During coordinated PR review, a media feature-branch URL can be used; update consumers
to the maintained media branch after the media PR is merged.

Capture UI screenshots at the native desktop resolution, before browser scaling, and save the original PNG. Do not upscale a browser screenshot or convert a JPEG back to PNG. The click-guide renderer preserves the original pixel colours and adds green markers without palette quantisation.

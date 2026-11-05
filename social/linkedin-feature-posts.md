# LinkedIn feature posts

Drafts for [website issue #713](https://github.com/neurodesk/neurodesk.github.io-hugo/issues/713). Source checks: 5 November 2026. The text between each heading and its source note is the proposed post.

## 1. View images with NiiVue

Did you know you can inspect neuroimaging files inside JupyterLab?

Neurodesktop includes the NiiVue file viewer and notebook widget. Open a NIfTI file from the file browser, or put an interactive image view beside your analysis code with ipyniivue. It's a useful way to check an input or inspect an output while working through a notebook.

See the file-browser and notebook examples: https://neurodesk.org/getting-started/installations/sherlock/#neuroimaging-visualisation-in-the-file-browser-and-notebooks-of-jupyterlab

#Neurodesk #NiiVue #Neuroimaging

*Sources: [included JupyterLab extensions](https://github.com/neurodesk/neurodesktop/blob/main/Dockerfile); [file-browser and notebook examples](https://github.com/neurodesk/neurodesk.github.io/blob/main/src/content/docs/getting-started/installations/sherlock.mdx). The linked installation guide covers Sherlock; Neurodesktop already includes these extensions.*

## 2. Run jobs with Slurm

A small analysis can be a good place to learn batch scheduling.

Neurodesktop includes a local Slurm queue, so you can submit jobs with sbatch and inspect the queue with squeue inside your analysis environment. On an HPC system, host mode connects to the site's Slurm installation with the appropriate configuration and bindings.

Start with the local and HPC setup examples: https://github.com/neurodesk/neurodesktop/blob/main/config/slurm/README.md

#Neurodesk #Slurm #ResearchComputing

*Source: [Slurm modes and configuration](https://github.com/neurodesk/neurodesktop/blob/main/config/slurm/README.md). Local mode is a single-node queue; connecting to a cluster requires site-specific setup.*

## 3. Connect a local model with Ollama

Want to try a coding model running on your own computer?

Neurodesk's OpenCode and Notebook Intelligence guides show how to connect to an Ollama server on the host. You choose the model, configure the connection and use it from your analysis environment. Model size and context length need to fit the memory available on your machine.

Follow the Ollama setup: https://neurodesk.org/getting-started/agents/opencode/#self-host-a-model-in-ollama

#Neurodesk #Ollama #ScientificComputing

*Sources: [OpenCode with Ollama](https://github.com/neurodesk/neurodesk.github.io/blob/main/src/content/docs/getting-started/agents/opencode.mdx); [Notebook Intelligence with Ollama](https://github.com/neurodesk/neurodesk.github.io/blob/main/src/content/docs/getting-started/agents/notebook-intelligence.mdx).*

## 4. Use coding agents in Neurodesk

Working on an analysis script and need a second pair of eyes?

Neurodesk includes Claude Code, Codex and OpenCode. Start an agent from the terminal, connect your chosen provider and give it a concrete task: explain an unfamiliar script, investigate an error or help write a check for your analysis. Review the changes and run the analysis to check the result.

Choose a setup guide: https://neurodesk.org/getting-started/agents/

#Neurodesk #ResearchSoftware #Neuroimaging

*Sources: [Claude Code](https://github.com/neurodesk/neurodesk.github.io/blob/main/src/content/docs/getting-started/agents/claude.mdx), [Codex](https://github.com/neurodesk/neurodesk.github.io/blob/main/src/content/docs/getting-started/agents/codex.mdx), [OpenCode](https://github.com/neurodesk/neurodesk.github.io/blob/main/src/content/docs/getting-started/agents/opencode.mdx).*

## 5. Learn Nextflow with a brain-extraction workflow

How do you turn one working analysis command into a repeatable workflow?

The NeurodeskEDU Nextflow example starts with a small hello-world pipeline, then builds up to FSL brain extraction and a multi-subject demonstration. You'll work with processes, channels, output files and resuming completed tasks. The example uses public MRI data and introduces each piece along the way.

Try the notebook: https://neurodesk.org/edu/examples/workflows/nextflow_neurodesk.html

#Neurodesk #Nextflow #ReproducibleResearch

*Source: [Nextflow example notebook](https://github.com/neurodesk/neurodeskedu/blob/main/books/examples/workflows/nextflow_neurodesk.ipynb). Its multi-subject demonstration uses a copied scan as a simulated second subject.*

## 6. Build a Snakemake workflow

An analysis gets easier to rerun when its inputs, outputs and software requirements are written down.

The NeurodeskEDU Snakemake example turns FSL brain extraction and tissue segmentation into a small structural-MRI workflow. Each rule declares its Neurodesk modules with envmodules, keeping the required tool versions alongside the processing step. The notebook walks through the dependency graph, parallel execution and inspecting results.

Work through the example: https://neurodesk.org/edu/examples/workflows/snakemake.html

#Neurodesk #Snakemake #ReproducibleResearch

*Source: [Snakemake example notebook](https://github.com/neurodesk/neurodeskedu/blob/main/books/examples/workflows/snakemake.ipynb).*

## 7. Create a Neurocontainer recipe in the browser

Have a research tool you'd like to package for Neurodesk?

The Neurocontainers builder gives you a browser interface for creating a container recipe. Start from a Python or R package template, or build from scratch. Add installation steps, environment settings and documentation, then arrange the steps in the order the build needs them.

Open the builder: https://neurodesk.org/neurocontainers-ui/

Contribution guide: https://neurodesk.org/developers/new-tools/

#Neurodesk #ResearchSoftware #Containers

*Sources: [adding tools](https://github.com/neurodesk/neurodesk.github.io/blob/main/src/content/docs/developers/new-tools/index.mdx), [builder templates](https://github.com/neurodesk/neurocontainers-ui/blob/main/copy/help/ui/template-selection.md), [build directives](https://github.com/neurodesk/neurocontainers-ui/blob/main/copy/help/ui/directives-list.md).*

## 8. Explore Neurodesk webapps

Some neuroimaging tasks can start with a browser tab.

Neurodesk's webapps include tools for DICOM protocol comparison, image registration, brain extraction and QSM processing. Browse the directory, choose a task and follow the app's workflow with its example data or your own inputs. These apps run in the browser, so you can try them without first installing the Neurodesktop environment.

Explore the apps: https://webapps.neurodesk.org/

#Neurodesk #Neuroimaging #OpenScience

*Source: [Neurodesk webapp guide](https://github.com/neurodesk/neurodesk.github.io/blob/main/src/content/docs/getting-started/hosted/webapps.mdx).*

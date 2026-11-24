# Publish on GitHub

Suggested repository name: **under-observation**

Suggested description:

> Announced oversight, compliance and evaluation awareness in AI agents: a 90-game Catan study with interpretable surrogate analysis and inspectable source records.

Suggested topics: `explainable-ai`, `ai-evaluation`, `ai-governance`, `multi-agent-systems`, `catan`, `interpretability`.

## Fastest terminal route

The script creates a **public** repository under the GitHub account you sign into. From the extracted project directory:

```
bash scripts/publish_github.sh
```

It signs in through GitHub CLI, creates the repository, commits and pushes the files, then configures Pages. It uses only local repository identity settings, does not force-push, and stops if it encounters an unrelated origin. Git and GitHub CLI must already be installed. Run it from the extracted project directory.

## Option A: GitHub website

1. Extract the ZIP on your computer. Upload its **contents**, not the ZIP itself.
2. Sign in to GitHub. Choose **New repository**, enter `under-observation`, and create it. Choose public if you want a public portfolio site.
3. Choose **uploading an existing file**. Drag the extracted files and folders into the page. `index.html`, `README.md`, `site/`, `analysis/`, `data/`, `results/` and `scripts/` belong at the repository root.
4. Commit the upload. Check that `index.html` is visible at the root rather than inside a second enclosing folder.
5. Open **Settings → Pages**. Under Source, select **Deploy from a branch**. Choose the default branch (usually `main`) and **/ (root)**, then save.
6. Wait for GitHub's deployment to finish. Open the URL shown in Pages settings and check the charts, three episode selectors, note filters and downloads.
7. Submit that verified site URL and repository URL with the poster PDF.

Files beginning with a dot may be hidden by your computer. They include `.gitignore`, `.nojekyll` and the optional `.github/workflows/checks.yml`. The site works without the optional check workflow. Use Option B to preserve all files automatically.

If GitHub cannot preview a large HTML file as source, use the Pages URL to view it. The HTML intentionally embeds its fonts, image and data so it also works offline.

## Option B: Terminal with GitHub CLI

Open a terminal in the extracted project directory. You need Git and the GitHub CLI installed.

```
gh auth login
git init -b main
git add .
git commit -m "Add oversight study, interpretable analysis, site and poster"
gh repo create under-observation --public --source=. --remote=origin --push
```

If Git asks for your identity, configure your own name and email and repeat the commit. The supplied script does not set an identity or create a repository without you running it.

Then use **Settings → Pages → Deploy from a branch → main → / (root)**.

## What you should see

- The supplied Duke University wordmark and a visible credit naming Shreya Mendi as project lead.
- The shared Catan interface, 90-game findings and direct before/after charts.
- An implemented depth-three surrogate with held-out permutation importance.
- Three short record walkthroughs and the complete 96-note collection.
- Evaluation-awareness interpretation, sources and downloads.

Do not describe the surrogate's feature importance as an internal explanation of Qwen, and do not describe an inconclusive oversight effect as proof of no effect.

## After publication

The project-site QR points to https://maitsingh.github.io/mara_deception_auditor/site/index.html. A second QR links to the shared engine source. If the published URL changes, update `poster/build_poster.py`, regenerate the poster and check the code before printing.

## Open the downloaded HTML

ChatGPT may download or show source for an HTML attachment rather than host it. For the website-only ZIP, extract it and double-click its `index.html`, or use Open With → Chrome/Safari. For the full repository, open `site/index.html` directly. Keep the `.html` extension; do not save it as `.html.txt`. No web server or API key is required.

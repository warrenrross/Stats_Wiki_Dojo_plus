---
name: deploy
description: Render the Quarto site and push it to GitHub Pages. Use this skill when the user says "deploy", "publish the site", "push to GitHub Pages", "update the live site", "quarto publish", or "ship it". Also trigger after any session where wiki content or lesson files changed and the user says they're done editing.
---

# Deploy

Render the full Quarto site and push the output to the `gh-pages` branch on GitHub. The live site is at https://warrenrross.github.io/Stats_Wiki_Dojo_plus/.

---

## Prerequisites

- Quarto 1.9+ installed (`quarto --version`)
- R installed with packages: `qcc`, `agricolae`, `FrF2`, `tidyverse`, `pacman`
- GitHub credentials accessible (macOS Keychain or environment variable `GITHUB_TOKEN`)
- Working directory: project root (`Stats_Wiki_Dojo_plus/`)

---

## Steps

### 1. Render the site

```bash
cd "/Users/warrenrross/Education/INEG/INEG Stats/Stats_Wiki_Dojo_plus"
quarto render
```

This generates `_site/`. R code chunks are cached in `_freeze/` — only changed files are re-executed.

Watch for errors. Common ones and fixes:

| Error | Fix |
|-------|-----|
| `styles.css` SCSS error | First line of `assets/css/styles.css` must be `/*-- scss:rules --*/` |
| `object not found` in R chunk | The chunk uses a variable defined in a previous chunk — check `freeze: auto` cached the right version |
| WebR chunk error | These run in-browser only; render errors here are often just missing packages in the `webr: packages:` frontmatter list |

### 2. Push to gh-pages

Retrieve the GitHub token and push the rendered `_site/` to the `gh-pages` branch:

```bash
TOKEN=$(security find-internet-password -s github.com -w 2>/dev/null)
TMPDIR=$(mktemp -d)
cp -r _site/. "$TMPDIR/"
cd "$TMPDIR"
git init
git checkout --orphan gh-pages
git add -A
git commit -m "Deploy: <brief description of what changed>"
git remote add origin "https://warrenrross:${TOKEN}@github.com/warrenrross/Stats_Wiki_Dojo_plus.git"
git push --force origin gh-pages
```

If `security find-internet-password` returns nothing, ask the user to run:
```
! export GITHUB_TOKEN=<their-token>
```
and then substitute `$GITHUB_TOKEN` for `${TOKEN}` in the push URL.

### 3. Verify

GitHub Pages typically updates within 1–2 minutes. The live URL is:
https://warrenrross.github.io/Stats_Wiki_Dojo_plus/

Tell the user the deploy is complete and suggest opening the URL to verify.

---

## What NOT to commit

- `_site/` — rendered output, gitignored
- `wiki/**/*.html` — gitignored
- `.claude/settings.local.json` — machine-specific, gitignored

## What SHOULD be committed before deploying

- `_freeze/` — execution cache; commit if R chunks were re-run so CI has the latest output
- Any new or edited `.md` / `.qmd` source files

---

## Alternate: quarto publish (simpler, but requires interactive auth)

```bash
quarto publish gh-pages
```

This works if the `gh-pages` branch already exists (it does). It handles the push automatically but may prompt for credentials interactively — not suitable for non-interactive use.

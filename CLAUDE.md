# CLAUDE.md — Stats Wiki Dojo Plus

Project-specific instructions for Claude Code. Read this at the start of every session.

---

## What This Project Is

A Quarto website for INEG 2314H — Statistical Methods. It serves as a living textbook with three layers:

- **Wiki** (`wiki/`) — reference pages copied from Stats_Notes, organized as concepts / examples / r-code / reference
- **Lessons** (`lessons/`) — executable `.qmd` files with R code chunks, built by CPS tier
- **Dojo** (`dojo/r-drills/`) — R coding drills with worked solutions

**Primary source**: `../Stats_Notes/` (parent directory sibling). All wiki content was copied from there. Stats_Notes is the authoritative source; always sync from it rather than editing wiki pages independently.

**GitHub remote**: `https://github.com/warrenrross/Stats_Wiki_Dojo_plus`
**Deployed site**: `https://warrenrross.github.io/Stats_Wiki_Dojo_plus/`

---

## Session-Start Checklist

1. Read this file
2. Run `quarto check` to confirm R and knitr are wired up
3. If continuing a task, check the Known Issues table below and Pending Tasks section
4. Start `quarto preview` before editing `.qmd` files so you can verify renders

---

## Key Workflows

### Preview
```bash
cd "/Users/warrenrross/Education/INEG/INEG Stats/Stats_Wiki_Dojo_plus"
quarto preview
```
Preview runs on a random port (check output for URL). Re-run if port conflicts.

### Render all (production)
```bash
quarto render
```

### Render one file
```bash
quarto render lessons/quality-methods/p-c-u-charts.qmd
```

### Deploy to GitHub Pages
```bash
quarto publish gh-pages
```
(Requires remote already set; use `git remote -v` to verify.)

---

## Architecture Decisions

| Decision | Rationale |
|----------|-----------|
| `wiki/**/*.md` files rendered by Quarto | Quarto handles `.md` as plain markdown; wiki pages have no R code so no `.qmd` needed |
| `freeze: auto` in `_quarto.yml` | R chunks cached to `_freeze/`; commit `_freeze/` to git so CI/GitHub Pages doesn't need R installed |
| Relative Markdown links throughout | All wiki cross-references use `[text](relative/path.md)`; do not use `[[...]]` bracket syntax in any Quarto-rendered file |
| CPS tier model (`tier-focus:` frontmatter) | construct / procedure / script tiers drive lesson framing; see `wiki/concepts/taxonomy.md` |
| `pacman::p_load()` for all packages | Used consistently throughout all R code; do not switch to `library()` |
| Root design docs excluded via `.quartoignore` + `render:` list | `knowledge-dimensions.md`, `living_textbook.md`, `llm-wiki.md`, `quarto_site_scaffold.md`, `CLAUDE_CODE_SPEC.md` are not rendered |
| `assets/css/styles.css` must begin with `/*-- scss:rules --*/` | Quarto Bootstrap theme requires this SCSS layer marker; omitting it causes a render error |
| `wiki/CLAUDE.md` is for wiki management | The session-start checklist and ingest workflow in `wiki/CLAUDE.md` governs wiki-only sessions; this file governs the Quarto project |

---

## Directory Structure

```
Stats_Wiki_Dojo_plus/
├── CLAUDE.md                  ← this file
├── _quarto.yml                ← site config, sidebar, navbar, render list
├── .quartoignore              ← excludes design docs from rendering
├── .gitignore                 ← excludes _site/, *.quarto_ipynb, wiki HTML artifacts
├── index.qmd                  ← home page
├── about.qmd
├── syllabus-path.qmd
├── graph-navigation.qmd
├── assets/css/styles.css      ← custom CSS (must have SCSS layer marker at top)
├── wiki/                      ← reference pages (plain .md, copied from Stats_Notes)
│   ├── CLAUDE.md              ← wiki management schema (ingest, lint, query workflows)
│   ├── index.md               ← catalog of all wiki pages
│   ├── concepts/              ← 38 concept/formula pages
│   ├── examples/              ← 8 worked example pages
│   ├── r-code/                ← 8 R code interpretation pages
│   └── reference/             ← 6 quick-lookup sheets
├── lessons/                   ← executable .qmd lesson files
│   ├── foundations/           ← sampling, SE, CI
│   ├── inference/             ← HT, t-tests, ANOVA
│   ├── regression/            ← SLR, MLR, diagnostics
│   ├── quality-methods/       ← control charts, xbar-R, p/c/u charts
│   └── experimental-design/   ← CRD, factorial, 2^k
├── dojo/
│   └── r-drills/              ← 5 coding drill files (simulate-clt, fit-regression-model,
│                                 build-control-chart, fill-anova-table, factorial-anova)
├── _freeze/                   ← knitr execution cache (commit to git — needed for CI)
└── _site/                     ← rendered output (gitignored)
```

---

## Known Issues

| Issue | Status | Notes |
|-------|--------|-------|
| WebR dojo conversion | Done (2026-05-21) | All 5 dojo pages have `{webr-r}` interactive sections; quarto-webr 0.4.4 extension in `_extensions/` |
| `_freeze/` untracked | Done (2026-05-21) | Committed; GitHub Pages CI will use cached output |
| GitHub Pages deploy | Done (2026-05-21) | Live at `https://warrenrross.github.io/Stats_Wiki_Dojo_plus/`; gh-pages branch bootstrapped manually |
| Two empty stubs in wiki root | Harmless | `wiki/process-capability.md` and `wiki/regression-examples.md` are 1-line orphan stubs from original Stats_Notes; leave unless cleaning up |

### Future deploys

After any content change, rebuild and push the gh-pages branch:
```bash
quarto render
cd /tmp && rm -rf gh-pages-deploy && git clone --branch gh-pages \
  https://github.com/warrenrross/Stats_Wiki_Dojo_plus.git gh-pages-deploy
cp -r _site/. /tmp/gh-pages-deploy/
cd /tmp/gh-pages-deploy && git add -A && git commit -m "Deploy: <description>"
TOKEN=$(security find-internet-password -s github.com -w)
git push "https://warrenrross:${TOKEN}@github.com/warrenrross/Stats_Wiki_Dojo_plus.git" gh-pages
```
Or simply run `quarto publish gh-pages` — now that the branch exists, it will work without `--no-prompt`.

---

## Pending Tasks

1. **Section 4 quick reference .docx** — `wiki/reference/quick-reference-section4.md` exists but no Word version built
2. **Test WebR pages in browser** — confirm package loading works at deployed URL

---

## R Packages Used

| Package | Used In | Notes |
|---------|---------|-------|
| `qcc` | lessons/quality-methods, dojo/build-control-chart | control charts |
| `agricolae` | dojo/factorial-anova | Tukey HSD, RCBD |
| `FrF2` | lessons/experimental-design/two-k-design | fractional factorial, DanielPlot |
| `tidyverse` | dojo/simulate-clt, fit-regression-model, factorial-anova | ggplot2, dplyr, tidyr |
| `pacman` | all R files | `p_load()` pattern; load all packages through this |
| `rio` | some lessons | import/export data |

---

## Git Conventions

- Commit rendered artifacts separately from content changes
- Never commit `_site/` or `wiki/**/*.html` — both gitignored
- Commit `_freeze/` — it's the execution cache, not build output
- Commit messages follow: `Verb noun: short description` (e.g., `Add WebR support to dojo pages`)

---

## Session History

| Date | Work Done |
|------|-----------|
| 2026-05-21 | Full scaffold: GitHub repo created, Quarto installed (1.9.37), site scaffolded from Stats_Notes, render errors fixed (SCSS marker, c-chart data, root .md exclusion), wiki cross-references converted to relative Markdown links, 5 dojo drill files created, preview confirmed working |
| 2026-05-21 | WebR added to all 5 dojo pages (quarto-webr 0.4.4); _freeze/ committed; site deployed to GitHub Pages at https://warrenrross.github.io/Stats_Wiki_Dojo_plus/ |

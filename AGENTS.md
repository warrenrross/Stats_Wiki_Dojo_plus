# AGENTS.md — Agent Onboarding Guide

This file is for LLM coding agents (Claude Code, Cursor, Copilot, etc.) maintaining this repository. Read it at the start of any session where you'll be editing content or structure.

For human readers, see [README.md](README.md).

---

## What This Project Is

A Quarto website for INEG 2314H — Statistical Methods at the University of Texas at Arlington. It serves as a living textbook with three layers:

| Layer | Location | Purpose |
|-------|----------|---------|
| **Wiki** | `wiki/` | Static reference pages — concept definitions, formulas, worked examples, R code walkthroughs |
| **Lessons** | `lessons/` | Executable `.qmd` files with prose + math + R code output, one per major topic |
| **Dojo** | `dojo/r-drills/` | Interactive R drills using WebR (runs in browser, no installation required) |

**Primary content authority:** `../Stats_Notes/` (parent directory sibling) — the original exam-prep wiki. Wiki pages were copied from there. When content conflicts, trust `../Stats_Notes/`.

**Live site:** https://warrenrross.github.io/Stats_Wiki_Dojo_plus/

---

## Session Start

Before doing any work, orient yourself:

1. Read `CLAUDE.md` (project instructions, architecture decisions, pending tasks)
2. Read `wiki/CLAUDE.md` (wiki management rules — ingest, lint, query workflows)
3. Run `quarto check` to confirm R + knitr are wired up
4. Check `wiki/index.md` for stub entries (plain text rows without links = pages that need to be created)

Or use the `/get-familiar` skill to do steps 1–2 automatically.

---

## Available Skills

Skills are stored in `.claude/skills/`. Each skill is a markdown file of step-by-step instructions. They work as slash commands in Claude Code; other agents should read the `SKILL.md` file directly and follow the instructions.

### How to invoke

| Agent | How to use a skill |
|-------|--------------------|
| **Claude Code** | Type `/skill-name` in the chat prompt |
| **Other agents** | Tell your agent: *"Read `.claude/skills/skill-name/SKILL.md` and follow those instructions"* |
| **Manually** | Open the `SKILL.md` and follow the steps yourself |

---

### Skill Catalog

| Skill | Trigger phrases | What it does | When to use |
|-------|----------------|--------------|-------------|
| **`get-familiar`** | "get familiar", "orient yourself", "what's this project" | Reads all docs (`CLAUDE.md`, `README.md`, subdirectory docs) and gives a grounded summary | Start of any new session |
| **`ingest-examples`** | "ingest [file] as examples", "create example page from [homework/drill]", "stub in index.md needs content" | Reads a source R/homework file from `../Section*/Drill/`, writes a `wiki/examples/` page using the standard template, updates `wiki/index.md` | Whenever a drill or homework file needs to become a wiki example page |
| **`lint-wiki`** | "lint the wiki", "check for broken links", "wiki health check", "find orphans" | Audits `wiki/` for missing files, orphan pages, `[[bracket links]]`, missing tier/tag frontmatter, index coverage gaps | Periodic maintenance; before deploying; after adding many pages |
| **`deploy`** | "deploy", "publish the site", "push to GitHub Pages", "ship it" | Runs `quarto render`, then pushes `_site/` to the `gh-pages` branch via token | After any content changes are committed and ready to go live |
| **`wrap-up`** | "wrap up", "end of session", "close out" | Updates `CLAUDE.md` session history, checks related docs, saves memory, flags untracked files | End of every work session |

---

## Key Constraints

These are non-negotiable conventions. Violating them breaks the site or the wiki's internal consistency.

| Rule | Correct | Wrong |
|------|---------|-------|
| R packages | `pacman::p_load(pkg1, pkg2)` | `library(pkg1)` |
| Cross-references in wiki | `[page](../concepts/page.md)` | `[[page]]` (Obsidian syntax, breaks Quarto) |
| Unit labels | `unit-1` through `unit-5` | `section-1`, `unit-1-2`, `units-1-2` |
| Assign each file to ONE unit | `tags: [concept, unit-2]` | `tags: [concept, unit-1-2]` |
| CSS layer marker | First line of `assets/css/styles.css` must be `/*-- scss:rules --*/` | Omitting it → render error |
| `_freeze/` | Commit it | Never gitignore it — CI needs it |
| `_site/` | Never commit | Gitignored |
| New wiki pages | Must have `tier:` frontmatter | Tierless pages break the CPS taxonomy |

---

## Source Materials

Content comes from lecture slides and homework files in the parent directory. Always prefer sourcing from these rather than inventing content.

| Unit | Content Type | Source Path |
|------|-------------|-------------|
| Unit 1 (Foundations) | Drills, homework | `../Section1&2/Drill/` |
| Unit 2 (Inference) | Drills, homework | `../Section1&2/Drill/` |
| Unit 1–2 | Lecture slides | `../Section1&2/Slides/L001P–L25P.pdf` |
| Unit 1–2 | Formula PNGs | `../Section1&2/Slides/Formula Snippets/*.png` |
| Unit 3 (Regression) | Regression drills | `../Section_3/Drills/Regression in R/` |
| Unit 4 (Quality) | Control chart drills | `../Section_3/Drills/Control Charts in R/` |
| Unit 3–4 | Lecture slides | `../Section_3/Slides/L27P–L40-41P.pdf` |
| Unit 5 (DOE) | DOE drills | `../Section_4/Drills/` |
| Unit 5 | Lecture slides | `../Section_4/Slides/L42–L50P.pdf` |

---

## Wiki Structure

```
wiki/
├── CLAUDE.md          ← wiki management rules (ingest, lint, query, teacher-language)
├── index.md           ← catalog of all pages (update after every ingest)
├── concepts/          ← Tier 1 constructs + Tier 2 procedures (38 pages)
├── examples/          ← Tier 3 worked example pages (12 pages)
├── r-code/            ← Tier 3 R code + output interpretation pages (8 pages)
└── reference/         ← untiered quick-lookup sheets (6 pages)
```

**CPS tiers** (every wiki page has a `tier:` field):

| Tier | What it is | Examples |
|------|-----------|---------|
| `construct` | Mathematical building block used inside other techniques | standard-error, degrees-of-freedom, distributions |
| `procedure` | Analytical technique requiring judgment about which variant to apply | hypothesis-testing-overview, regression-slr, control-charts |
| `script` | Fixed-sequence workflow — learn by drilling the sequence | all `examples/` pages, all `r-code/` pages |
| `reference` | Cross-tier navigation aid | formula-sheet, which-test-flowchart |

---

## Deploy Architecture

```
Source (.qmd / .md)  →  quarto render  →  _site/  →  gh-pages branch  →  GitHub Pages
                         (uses _freeze/ for cached R output)
```

- `_freeze/` is committed; GitHub Pages CI never needs R installed
- `gh-pages` branch is an orphan branch (no commit history from `main`)
- `quarto publish gh-pages` works for interactive deploys; use the manual push from `.claude/skills/deploy/SKILL.md` for scripted/agent-driven deploys

---

## Common Tasks Quick Reference

| Task | Command / Skill |
|------|----------------|
| Preview locally | `quarto preview` |
| Render all | `quarto render` |
| Deploy to live site | `/deploy` skill |
| Add a new example page | `/ingest-examples [source file]` skill |
| Check wiki health | `/lint-wiki` skill |
| End-of-session cleanup | `/wrap-up` skill |
| Orient to the project | `/get-familiar` skill |

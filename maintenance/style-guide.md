# Style Guide

Conventions for all pages in this project.

## Lesson (.qmd) Conventions

- **Frontmatter:** always include `title`, `categories`, `tier-focus`, `related`
- **Structure:** Learning Goals → In Plain English → Key Formulas → R Example → Try It Yourself → Related Wiki Pages
- **R chunks:** labeled, with `#| label:` and `#| fig-cap:` where applicable
- **Packages:** load with `pacman::p_load()` in the first chunk of each file
- **Teacher phrasing:** use blockquote (`>`) for teacher-expected conclusion phrasing

## Wiki Page (.md) Conventions

- **Frontmatter:** `tags`, `tier`, `sources` required on every content page
- **Tier values:** `construct` | `procedure` | `script` | `reference`
- **Backlinks:** Obsidian style `[[page-name]]` inside wiki; relative links in .qmd files
- **Related section:** required at bottom of every page

## R Code Conventions

- `pacman::p_load()` for all package loading
- `trimws(rownames(aov_tbl))` after every `summary(aov)[[1]]` — mandatory
- Column names in `confint()`: `"2.5 %"` / `"97.5 %"` for 95%; exact string matching required
- `pivot_longer()` over `reshape2::melt()` for new code

## File Naming

- Lowercase hyphenated: `simple-linear-regression.qmd`
- Wiki pages: noun phrases for concepts, `topic-examples.md` for examples, `topic-r.md` for R code
- No spaces in filenames

## Teacher-Language Conventions

See `wiki/CLAUDE.md` for the full table of expected phrasing for exam answers.

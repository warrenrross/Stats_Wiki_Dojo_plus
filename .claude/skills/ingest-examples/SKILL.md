---
name: ingest-examples
description: Convert a source R script, Rmd, or homework file into one or more wiki example pages. Use this skill when the user says "ingest [file] as examples", "create an example page from [homework/drill]", or "add examples from [file or unit]". Also use it when the wiki/index.md has a stub entry (plain-text row with no link) in a Scripts section.
---

# Ingest Examples

Convert a source file (R script, Rmd, homework) into a wiki example page at `wiki/examples/`. The goal is a polished, exam-ready worked-problem page — not a transcription of the source code.

---

## Inputs

The user will typically provide one of:
- A file path (absolute or relative to the project root)
- A filename like "Drill Homework 04_Ross.R"
- A description like "Unit 2 two-sample tests" with no specific file

If no file is specified, search for candidates:
- `../Section1&2/Drill/` — Unit 1 and Unit 2 R scripts and homework files
- `../Section_3/Drills/Regression in R/` — Unit 3 regression R files
- `../Section_3/Drills/Control Charts in R/` — Unit 4 quality methods R files
- `../Section_4/Drills/` — Unit 5 DOE R files
- `../Stats_Notes/` — existing wiki stubs that have content there

---

## Steps

### 1. Read the source file

Read the full source file. If it is a multi-problem script, identify each logical problem block (usually separated by `##` comments or problem numbers).

### 2. Assess and plan

For each problem block, determine:
- **What concept does it demonstrate?** (Match to a wiki concept page)
- **Which unit does it belong to?**
  - Unit 1: Probability, distributions, descriptive stats, data wrangling
  - Unit 2: Hypothesis testing (z, t, χ², F, proportions, two-sample, paired)
  - Unit 3: Regression (SLR, MLR, HT, CI, model adequacy)
  - Unit 4: Control charts, process capability
  - Unit 5: CRD, RCBD, factorial ANOVA, 2^k factorial, random effects
- **Is there enough for a full example?** (At least: problem statement, given/find, solution steps, interpretation)
- **Does a `wiki/examples/` page already exist for this topic?** If so, add problems to it rather than creating a new file.

### 3. Determine the output filename

Use the naming convention: `wiki/examples/[topic]-examples.md`

Examples: `hw1-examples.md`, `two-sample-examples.md`, `regression-examples.md`

If the source file covers one specific drill or homework: use the drill name (e.g., `hw4-drill-examples.md`).
If the source covers a concept category: use the concept name (e.g., `control-chart-examples.md`).

### 4. Write the example page

Use the standard template:

```markdown
---
tags: [example, unit-X]
tier: script
sources: [source-filename.R, L##P]
---
# Examples: [Descriptive Title]

See also: [concept-page](../concepts/concept-page.md), [r-code-page](../r-code/r-code-page.md)

---

## Problem N — [Short Problem Title]

### Problem Statement
[Full context — enough for someone to understand without the source file]

### Given / Find
- **Given:** key facts (distribution parameters, sample sizes, α level)
- **Find:** what the student must compute or decide

### Solution

**Step 1 — [Action]**
[Prose explanation of the step, then the R code block]

```r
pacman::p_load(pacman, tidyverse)  # always use p_load, never library()

# code here
```

**Step 2 — [Action]**
...

### Interpreting the Output

| R Output | Symbol | Meaning | Teacher's Phrasing |
|----------|--------|---------|---------------------|

### Answer
[Conclusion in full sentence form using teacher-language conventions]
```

**Critical conventions:**

- `tier: script` always (example pages are always scripts)
- Single unit tag: `unit-1` through `unit-5` — never a range like `unit-1, unit-2` in a single tag. If a page genuinely spans two units, use both as separate tags: `unit-1, unit-2`
- All R code uses `pacman::p_load()` — never `library()`
- "Interpreting the Output" table maps R output → statistical symbol → plain meaning → teacher's exam phrasing
- "Answer" section must use teacher-language from `wiki/CLAUDE.md`:
  - `p < α`: "Reject H₀ at α = X. There is sufficient evidence to conclude [H₁ in context]."
  - `p > α`: "Fail to reject H₀ at α = X. There is insufficient evidence to conclude [H₁ in context]."
  - CI: "We are X% confident that [parameter] is between [lower] and [upper]."
  - R²: "X% of the variation in [Y] is explained by the regression model."
- Cross-reference links use relative paths: `../concepts/page.md`, `../r-code/page.md`

### 5. Update `wiki/index.md`

Find the correct unit and tier section. Example pages belong under **Tier 3 — Scripts**.

Replace any plain-text stub entry (e.g., `| hw1-examples | Homework 1 worked problems (stub) |`)
with a proper Markdown link:
```
| [hw1-examples](examples/hw1-examples.md) | Short description of what problems it covers |
```

If the page is new (no existing stub), add it to the right unit's Tier 3 table.

### 6. Update `wiki/CLAUDE.md` Known Issues

If you just resolved a stub listed in the "Known Issues / Pending Enrichment" table, update its status or remove the row.

### 7. Report back — do NOT commit

List:
- File(s) created or updated
- Which problems were included and which (if any) were skipped and why
- Whether `wiki/index.md` was updated
- Ask the user to review before committing

---

## Common Pitfalls

| Pitfall | How to avoid |
|---------|-------------|
| Using `library()` instead of `p_load()` | Always use `pacman::p_load()` |
| Using `[[bracket links]]` | Use relative Markdown links only: `[name](../path.md)` |
| Assigning `unit-1-2` or range tags | Pick a single unit; use two separate tags only if the page genuinely spans both |
| Transcribing source code without explanation | Source code is the starting point — add a problem statement, steps, and interpretation |
| Leaving `[1]` console output without context | Include output in comments or an "output" block with teacher-language annotation |
| Forgetting `"See also:"` links | Always link to the related concept page and R code page |

---

## Source Directory Reference

| Content Type | Source Path |
|-------------|-------------|
| Unit 1–2 drills and homework | `../Section1&2/Drill/` |
| Unit 3 regression R files | `../Section_3/Drills/Regression in R/` |
| Unit 4 control charts | `../Section_3/Drills/Control Charts in R/` |
| Unit 5 DOE drills | `../Section_4/Drills/` |
| Existing wiki stubs with content | `../Stats_Notes/wiki/examples/` |
| Formula reference images | `../Section1&2/Slides/Formula Snippets/*.png` |

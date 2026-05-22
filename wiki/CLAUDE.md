# Stats Notes Wiki — Agent Schema

This file defines how this wiki works. Read it at the start of every session.

## Session-Start Checklist

At the beginning of every wiki session, do these steps in order:

1. Read `HANDOFF.md` — process any `[pending]` entries before doing anything else
2. Read `index.md` — refresh your understanding of what pages exist
3. Scan `_inbox/` for any files not referenced in HANDOFF.md — if you find unrecognized files, ingest them using context clues (filename, content) and add a log entry
4. Check the user's stated goal for the session and cross-reference against pending items
5. After all work: update `index.md`, append to `log.md`, mark HANDOFF items `[done]`

## What This Wiki Is

A persistent, exam-prep reference wiki for INEG Statistics (Sections 1–4) covering probability, distributions, hypothesis testing, regression, control charts, and experimental design. Built incrementally from lecture slides, formula PNGs, homework files, and R projects. You (Claude) write and maintain it; Warren reads and queries it.

## Directory Layout

```
Stats_Notes/
├── CLAUDE.md              ← this file (schema)
├── index.md               ← catalog of all wiki pages (update every ingest)
├── log.md                 ← append-only operation log (update every ingest)
├── Welcome.md
├── llm-wiki.md
│
├── concepts/              ← concept + formula pages (Priority 1)
├── examples/              ← worked example pages (Priority 2)
├── r-code/                ← R code + output interpretation pages (Priority 3)
└── reference/             ← quick-lookup sheets
```

## Source Files (never modify these)

| Location | Contents |
|----------|----------|
| `../Section1&2/Slides/Formula Snippets/*.png` | 82 formula PNGs — primary formula source |
| `../Section1&2/Slides/L001P–L25P.pdf` | Section 1&2 lecture slides |
| `../Section_3/Slides/L27P–L40-41P.pdf` | Section 3 lecture slides |
| `../Section_4/Slides/L42–L50P.pdf` | Section 4 lecture slides (4 PDFs) |
| `../Section1&2/Drill/` | Homework R/Rmd files |
| `../Section_3/Drills/Regression in R/` | Regression homework/examples |
| `../Section_3/Drills/Control Charts in R/` | Control charts R code |
| `../Section_3/*.Rmd` | Section 3 study guides |
| `../Section_4/Drills/` | DOE homework and R drill scripts |

## Page Types and Templates

### 1. Concept + Formula Page (`concepts/topic-name.md`)

```markdown
---
tags: [concept, section-1-2]   # or section-3, section-4
tier: construct                 # construct | procedure | script | reference
sources: [L##P, formula-snippets]
---
# Topic Name

## In Plain English
One-paragraph intuition — what this is and why it matters.

## When To Use
- Condition 1
- Condition 2

## Formula(s)
| Symbol | Meaning |
|--------|---------|
| x̄     | sample mean |

$$\text{formula here}$$

## Key Assumptions
- Assumption 1

## Common Mistakes
- Mistake 1

## Related
- [[other-concept]]
- [[example-page]]
```

### 2. Worked Example Page (`examples/topic-examples.md`)

```markdown
---
tags: [example, section-1-2]
tier: script
sources: [Homework1_Ross, L##E]
---
# Example: Topic Name

## Problem Statement
Full problem text.

## Given / Find
- Given: ...
- Find: ...

## Solution
**Step 1 — ...**
Formula applied with numbers.

**Step 2 — ...**

## R Code
```r
code here
```

## Interpreting the Output
| R Output | Meaning | Teacher's Phrasing |
|----------|---------|---------------------|
| p-value = 0.032 | prob of test stat this extreme if H₀ true | "p-value < α, reject H₀" |

## Answer
State the conclusion in full sentence form.
```

### 3. R Code Page (`r-code/topic-r.md`)

```markdown
---
tags: [r-code, section-1-2]
tier: script
sources: [Drill files, homework R scripts]
---
# R: Topic Name

## Purpose
What analysis this performs.

## Full Code
```r
# annotated code block
```

## Output Walkthrough
| Output Term | What It Means | Teacher's Term |
|-------------|---------------|----------------|
| `p-value` | prob of Type I error | significance level evidence |
| `t value` | test statistic | t* or t-calculated |
| `Pr(>|t|)` | two-sided p-value | p-value |

## When to Use This vs. Alternatives
- Use this when: ...
- Use X instead when: ...
```

### 4. Reference Page (`reference/topic.md`)

Quick-lookup format. Minimal prose. Tables, lists, flowcharts.

---

## Naming Conventions

- File names: lowercase, hyphenated, no spaces (e.g., `hypothesis-testing-overview.md`)
- Concept pages: noun phrases (`confidence-intervals.md`)
- Example pages: `topic-examples.md` (e.g., `two-sample-examples.md`)
- R code pages: `topic-r.md` (e.g., `regression-r.md`)
- Obsidian links: **DO NOT USE `[[wikilinks]]`** — all 59 wiki pages were converted to relative Markdown links on 2026-05-21. New pages must use `[page-name](relative/path.md)` syntax. The `[[...]]` format is not supported by Quarto and will render as literal text.

---

## Ingest Workflow

When processing a new source file:

1. **Read** the source file(s)
2. **Identify** which concepts, formulas, examples, or R patterns it contains
3. **Create or update** concept pages in `concepts/` — add formulas, plain-English explanation, assumptions
4. **Create or update** example pages in `examples/` if worked problems are present
5. **Create or update** R code pages in `r-code/` if code is present, with output walkthrough table
6. **Update** `reference/formula-sheet.md` with any new formulas
7. **Update** `index.md` — add new pages, update summaries of changed pages
8. **Append** to `log.md` — format: `## [YYYY-MM-DD] ingest | Source: filename — Pages created/updated: list`

---

## Teacher-Language Conventions

These are the exact phrasings expected in exam answers. Use these in "Teacher's Phrasing" and "Interpreting the Output" sections.

| Statistical Action | Teacher's Expected Phrasing |
|-------------------|-----------------------------|
| p-value < α | "Reject H₀ at α = X. There is sufficient evidence to conclude [Ha in context]." |
| p-value > α | "Fail to reject H₀ at α = X. There is insufficient evidence to conclude [Ha in context]." |
| Confidence interval | "We are X% confident that [parameter] is between [lower] and [upper]." |
| Test statistic | "t* = value" or "z* = value" or "χ² = value" |
| R² interpretation | "X% of the variation in [Y] is explained by the regression model." |
| Residual plot diagnosis | "The residuals show [pattern], suggesting [violation/no violation] of the [assumption] assumption." |
| Control chart in-control | "The process appears to be in statistical control." |
| Control chart out-of-control | "Point(s) [#] fall outside the control limits / exhibit a non-random pattern, indicating the process is out of control." |
| Process capability Cp/Cpk | "The process [is/is not] capable of meeting specifications (Cp/Cpk [>/< ] 1)." |

---

## Query Workflow

When Warren asks a question:
1. Read `index.md` to find relevant pages
2. Read those pages
3. Answer with citations (e.g., "see [hypothesis-testing-overview](concepts/hypothesis-testing-overview.md)")
4. If the answer is non-trivial and reusable, file it as a new wiki page

---

## Lint Workflow

Periodically check for:
- Orphan pages (no inbound links from other pages)
- Concepts mentioned in examples but lacking their own concept page
- Formulas in `reference/formula-sheet.md` not linked back to a concept page
- Stale claims (e.g., "see homework X" where the example hasn't been created yet)
- Missing cross-references between related concepts

---

## Quick Reference Rebuild Workflow

The print-ready exam quick reference lives at `reference/Exam3_Quick_Reference.docx`.
To regenerate it after content changes:

```bash
cd "Stats_Notes/reference"
uvx --from python-docx python build_quick_ref.py
```

Then open in Word: **Ctrl+A → font 10pt → Layout → Margins → Narrow (0.5").** Target: 4 pages.

The markdown source of record is `reference/quick-reference-section3.md`. Edit that file first, then update `build_quick_ref.py` to match, then regenerate.

---

## CPS Cognitive Tiers

Every content page carries a `tier:` frontmatter field. Assign as follows:

- **construct** — a mathematical quantity or foundational principle with context-variable formula variants. No decision logic, no steps. Examples: standard error, degrees of freedom, distributions.
  Ask: "Does this concept appear as a building block inside multiple other techniques?" If yes → construct.

- **procedure** — an analytical technique that assembles 2+ constructs to achieve a specific goal, and requires judgment about which variant to apply. Examples: t-test, regression, control charts, ANOVA.
  Ask: "Does learning this require knowing *when* to use it and *which* construct variant to apply?" If yes → procedure.

- **script** — a fixed-sequence exam/task workflow where decisions are already collapsed. Examples: filling a partial ANOVA table, running diagnostic plots, interpreting R output. All `examples/` and `r-code/` pages are scripts.
  Ask: "Is the whole task learnable by practicing the sequence until it's automatic?" If yes → script.

- **reference** — cross-tier navigation aids (formula sheets, flowcharts). No tier assigned.

See `[taxonomy](concepts/taxonomy.md)` for the full page mapping and `[[knowledge-dimensions]]` for theoretical grounding.

---

## Section Coverage Map

| Section | Topics | Status |
|---------|--------|--------|
| 1–2 | Sampling, probability, distributions, CI, hypothesis testing, chi-square, proportions | Complete |
| 3 | Regression (SLR, MLR, HT, CI, model adequacy), control charts, PCR, correlation, transformations | Complete |
| 4 | CRD, RCBD, factorial ANOVA, 2^k factorial design, random effects model | Complete |

---

## Architectural Decisions (Persistent)

These decisions have been made and should not be revisited without deliberate intent.

| Decision | Rationale |
|----------|-----------|
| CPS tier model live (2026-04-22) | `tier:` field in all 39 content pages; new pages must get a tier at creation time — do not create pages without a tier |
| `concepts/taxonomy.md` is tier: reference | It spans all tiers; lives in concepts/ for Obsidian navigation, not because it is a concept page |
| `concepts/` holds both Constructs and Procedures | Tier captured in frontmatter, not directory — keeps folder structure flat |
| Quick reference is Section 3 only | `reference/quick-reference-section3.md` + `.docx` covers Sections 1–3. Section 4 has `quick-reference-section4.md` (markdown only; no .docx built yet) |
| Two misplaced empty stubs at wiki root | `process-capability.md` and `regression-examples.md` in root are empty 1-line files — orphaned stubs, harmless, leave unless actively cleaning up |
| Per-test pages for Section 1-2 HT (2026-04-23) | 10 `ht-*.md` pages, one per test (a–j from Exam2 quick reference), live in `concepts/`. Summary page at `reference/ht-tests-overview.md`. Existing broader pages (`chi-square.md`, `two-sample-tests.md`, etc.) remain; the per-test pages are the primary per-test reference. |
| GoF df general form is k−1−p (2026-04-23) | The Exam2 quick reference listed df = k−1 (special case, p=0 parameters estimated). General form used in class is k−1−p. Both documented in `ht-goodness-of-fit.md` and `ht-tests-overview.md`. Do not revert to k−1-only. |
| No separate `r-code/2k-r.md` (2026-05-16) | `factorial-anova-r.md` covers both factorial and 2^k R patterns. HANDOFF items referencing an optional `r-code/2k-r.md` were ingested into the existing script page instead. Do not create a duplicate 2k R page. |

---

## Known Issues / Pending Enrichment

| Item | Status | Notes |
|------|--------|-------|
| Stubs in index | Not yet filled | `hw1-examples`, `hw4-drill-examples`, `two-sample-examples`, `regression-examples` — listed in index but no file content |
| Section 4 quick reference .docx | Not built | `quick-reference-section4.md` exists but no print-ready Word version; build if exam prep requires it |
| data-wrangling-r stub | Exists but not cross-linked | `r-code/data-wrangling-r.md` not referenced from taxonomy.md |

# Quarto Site Scaffold for a Statistical Methods Wiki + Coding Dojo

*A practical project scaffold for turning an existing markdown wiki into a published, executable, university-level statistical methods resource.*

---

## 1. Project Purpose

This scaffold supports a living statistical methods resource that functions as:

- a textbook for structured reading
- a wiki for concept exploration
- a coding dojo for R-based technical drills
- a published website for students and instructors
- a maintained knowledge graph that evolves through use

The project assumes two existing reference documents are provided during setup:

1. `knowledge-dimensions.md`  
   Defines the CPS taxonomy: **Construct → Procedure → Script**.

2. `llm-wiki.md`  
   Defines the pattern for an LLM-maintained persistent markdown wiki.

The wiki is already established and will continue to be maintained. Quarto adds the publishing and executable lesson layer.

---

## 2. Recommended Repository Structure

```text
statistical-methods-resource/
│
├── _quarto.yml
├── index.qmd
├── about.qmd
├── syllabus-path.qmd
├── graph-navigation.qmd
│
├── wiki/
│   ├── index.md
│   ├── concepts/
│   ├── procedures/
│   ├── scripts/
│   └── reference/
│
├── lessons/
│   ├── index.qmd
│   ├── foundations/
│   │   ├── sampling-distributions.qmd
│   │   ├── standard-error.qmd
│   │   └── confidence-intervals.qmd
│   │
│   ├── inference/
│   │   ├── hypothesis-testing.qmd
│   │   ├── t-tests.qmd
│   │   └── anova.qmd
│   │
│   ├── regression/
│   │   ├── simple-linear-regression.qmd
│   │   ├── multiple-regression.qmd
│   │   └── diagnostics.qmd
│   │
│   └── quality-methods/
│       ├── control-charts.qmd
│       ├── xbar-r-charts.qmd
│       └── p-c-u-charts.qmd
│
├── dojo/
│   ├── index.qmd
│   ├── r-drills/
│   │   ├── simulate-clt.qmd
│   │   ├── fit-regression-model.qmd
│   │   └── build-control-chart.qmd
│   │
│   └── datasets/
│       ├── README.md
│       └── sample-data.csv
│
├── references/
│   ├── knowledge-dimensions.md
│   └── llm-wiki.md
│
├── maintenance/
│   ├── HANDOFF.md
│   ├── log.md
│   ├── style-guide.md
│   └── link-audit.md
│
├── assets/
│   ├── images/
│   ├── figures/
│   └── css/
│       └── styles.css
│
└── _site/
    └── generated site output
```

---

## 3. File and Folder Roles

### `_quarto.yml`

Main Quarto configuration file. Controls the website title, navigation, theme, rendering behavior, and output format.

### `index.qmd`

Public homepage. Should explain what the resource is, who it is for, and how to use it.

### `syllabus-path.qmd`

Suggested linear route through the material. This is the traditional textbook path.

### `graph-navigation.qmd`

Explains how to use backlinks, related pages, and the knowledge graph for exploration.

### `wiki/`

The established markdown knowledge base. This remains the conceptual backbone of the project.

### `lessons/`

Quarto-based instructional chapters. These are polished teaching documents with prose, math, code, plots, and exercises.

### `dojo/`

Practice-focused Quarto notebooks. These are meant for repetition, experimentation, and technical fluency.

### `references/`

Contains setup references and project-governance documents.

### `maintenance/`

Operational files for keeping the project healthy over time.

---

## 4. Starter `_quarto.yml`

```yaml
project:
  type: website
  output-dir: _site

website:
  title: "Statistical Methods Wiki + Coding Dojo"
  description: "A living university-level statistical methods resource built with Quarto, markdown, R, and a maintained knowledge graph."
  site-url: "https://your-username.github.io/statistical-methods-resource/"

  navbar:
    left:
      - text: Home
        file: index.qmd
      - text: Linear Path
        file: syllabus-path.qmd
      - text: Lessons
        file: lessons/index.qmd
      - text: Coding Dojo
        file: dojo/index.qmd
      - text: Knowledge Graph
        file: graph-navigation.qmd
      - text: Wiki Index
        file: wiki/index.md

  sidebar:
    style: docked
    search: true
    contents:
      - section: "Start Here"
        contents:
          - index.qmd
          - about.qmd
          - syllabus-path.qmd
          - graph-navigation.qmd

      - section: "Lessons"
        contents:
          - lessons/index.qmd
          - section: "Foundations"
            contents:
              - lessons/foundations/sampling-distributions.qmd
              - lessons/foundations/standard-error.qmd
              - lessons/foundations/confidence-intervals.qmd
          - section: "Inference"
            contents:
              - lessons/inference/hypothesis-testing.qmd
              - lessons/inference/t-tests.qmd
              - lessons/inference/anova.qmd
          - section: "Regression"
            contents:
              - lessons/regression/simple-linear-regression.qmd
              - lessons/regression/multiple-regression.qmd
              - lessons/regression/diagnostics.qmd
          - section: "Quality Methods"
            contents:
              - lessons/quality-methods/control-charts.qmd
              - lessons/quality-methods/xbar-r-charts.qmd
              - lessons/quality-methods/p-c-u-charts.qmd

      - section: "Coding Dojo"
        contents:
          - dojo/index.qmd
          - dojo/r-drills/simulate-clt.qmd
          - dojo/r-drills/fit-regression-model.qmd
          - dojo/r-drills/build-control-chart.qmd

format:
  html:
    theme:
      - cosmo
      - assets/css/styles.css
    toc: true
    toc-depth: 3
    number-sections: true
    code-fold: show
    code-tools: true
    code-copy: true
    fig-align: center
    smooth-scroll: true

execute:
  freeze: auto
  warning: false
  message: false
```

---

## 5. Starter Homepage: `index.qmd`

```markdown
---
title: "Statistical Methods Wiki + Coding Dojo"
---

# Statistical Methods Wiki + Coding Dojo

Welcome to a living resource for university-level statistical methods.

This site combines:

- a structured statistics wiki
- executable Quarto lessons
- R-based coding drills
- concept backlinks
- a suggested linear learning path
- graph-based exploration

## How to Use This Resource

### Follow the Linear Path

Use the linear path if you want a course-like sequence through the material.

Start here: [Linear Path](syllabus-path.qmd)

### Explore the Knowledge Graph

Use the wiki and backlinks if you want to move by conceptual relationship instead of chapter order.

Start here: [Knowledge Graph Navigation](graph-navigation.qmd)

### Practice in the Coding Dojo

Use the dojo when you want to run R code, modify examples, and build technical fluency.

Start here: [Coding Dojo](dojo/index.qmd)
```

---

## 6. Starter Linear Path: `syllabus-path.qmd`

```markdown
---
title: "Suggested Linear Path"
---

# Suggested Linear Path

This path gives students a traditional sequence through the resource.

The path is organized around the CPS learning model:

1. **Constructs** — foundational ideas
2. **Procedures** — statistical methods
3. **Scripts** — repeatable workflows and drills

## Unit 1: Foundations

- Sampling distributions
- Standard error
- Confidence intervals

## Unit 2: Inference

- Hypothesis testing
- t-tests
- ANOVA

## Unit 3: Regression

- Simple linear regression
- Multiple regression
- Model diagnostics

## Unit 4: Quality and Process Methods

- Control charts
- X-bar and R charts
- p, c, and u charts

## Unit 5: Coding Fluency

- Simulation drills
- Regression modeling drills
- Control chart construction drills
```

---

## 7. Starter Graph Navigation Page: `graph-navigation.qmd`

```markdown
---
title: "Knowledge Graph Navigation"
---

# Knowledge Graph Navigation

This resource is designed for both linear study and graph-based exploration.

The linear path acts like a road.

The wiki acts like a map.

## Backlinks

Backlinks connect related ideas across the resource.

For example:

- `standard error` connects to confidence intervals, hypothesis testing, regression, and control charts
- `degrees of freedom` connects to t-tests, ANOVA, regression, and chi-square methods
- `residuals` connects to regression, diagnostics, assumptions, and model adequacy

## Why This Matters

Statistical ideas rarely live in one chapter. Backlinks help students see how one idea keeps reappearing in new clothing.

## Suggested Use

When reading a lesson:

1. Follow links to unfamiliar constructs
2. Return to the lesson after reviewing the concept
3. Use related scripts for practice
4. Add new links when a useful connection appears during teaching
```

---

## 8. Starter Lesson Template

Use this template for files in `lessons/`.

```markdown
---
title: "Lesson Title"
categories: [statistics, lesson]
tier-focus: procedure
related:
  - ../wiki/concepts/example-construct.md
  - ../wiki/scripts/example-script.md
---

# Lesson Title

## Learning Goals

By the end of this lesson, students should be able to:

1. Explain the main idea in plain language
2. Identify when the method applies
3. Run the related R code
4. Interpret the output
5. Connect the method to related constructs and scripts

## In Plain English

Explain the idea before introducing formulas or code.

## Key Constructs

- [Construct 1](../wiki/concepts/construct-1.md)
- [Construct 2](../wiki/concepts/construct-2.md)

## Method

Explain the procedure and decision logic.

## R Example

```{r}
# Example R code goes here
```

## Interpretation

Explain what the output means in statistical language.

## Try It Yourself

Modify the code above and answer:

1. What changed?
2. Why did it change?
3. What stayed conceptually the same?

## Related Wiki Pages

- [Related construct](../wiki/concepts/related-construct.md)
- [Related procedure](../wiki/procedures/related-procedure.md)
- [Related script](../wiki/scripts/related-script.md)
```

---

## 9. Starter Coding Dojo Template

Use this template for files in `dojo/r-drills/`.

```markdown
---
title: "Coding Drill Title"
categories: [r, drill, coding-dojo]
tier-focus: script
---

# Coding Drill Title

## Drill Purpose

This drill builds fluency with a recurring statistical workflow.

## Trigger

Use this drill when you need to:

- recognize the task type
- run the correct R workflow
- interpret the output accurately

## Setup

```{r}
# Load packages
library(tidyverse)
```

## Fixed Sequence

1. Load or simulate data
2. Inspect the data
3. Run the method
4. Visualize the result
5. Interpret the output

## Worked Example

```{r}
# Worked example code
```

## Practice Variation

```{r}
# Student modifies this code
```

## Reflection Questions

1. What part of the workflow should become automatic?
2. What part requires statistical judgment?
3. Which wiki pages explain the underlying ideas?

## Related Wiki Pages

- [Related construct](../../wiki/concepts/related-construct.md)
- [Related procedure](../../wiki/procedures/related-procedure.md)
```

---

## 10. Wiki Page Frontmatter Convention

Existing wiki pages should keep using markdown, but should include consistent metadata where practical.

```yaml
---
title: "Standard Error"
tier: construct
tags: [statistics, inference, sampling]
sources: []
related:
  - confidence-intervals
  - hypothesis-testing
  - regression
---
```

Suggested tier values:

- `construct`
- `procedure`
- `script`
- `reference`

---

## 11. Backlinking Convention

Use backlinks deliberately.

Each page should include a `Related` section.

```markdown
## Related

- [[standard-error]]
- [[confidence-intervals]]
- [[hypothesis-testing]]
- [[sampling-distributions]]
```

Quarto pages may use relative markdown links for rendered website navigation:

```markdown
[Standard Error](../wiki/concepts/standard-error.md)
```

Obsidian-style backlinks may remain in wiki files if the wiki is also maintained in Obsidian:

```markdown
[[standard-error]]
```

Recommended approach:

- Use Obsidian backlinks inside the wiki layer
- Use relative links inside Quarto lesson pages
- Maintain both when a page needs to work well in both contexts

---

## 12. Human-in-the-Loop Maintenance Workflow

The expected workflow is continuous and instructor-led.

```text
Use lesson → observe student needs → edit .qmd → update wiki → add backlinks → render site → publish
```

### Instructor Responsibilities

- Edit Quarto lessons
- Add examples from class use
- Clarify explanations
- Identify missing links
- Add notes about common student errors

### LLM Responsibilities

- Suggest backlinks
- Update related wiki pages
- Maintain page consistency
- Check for duplicate or orphan pages
- Update index and log files
- Help convert rough notes into polished lessons

---

## 13. Maintenance Files

### `maintenance/HANDOFF.md`

Persistent queue for future work.

```markdown
# Handoff Queue

## Pending

### [pending] Add control chart drill variations
- Source: class notes
- Action: create
- Target: dojo/r-drills/build-control-chart.qmd
- Notes: Include x-bar/R and u-chart variants
- Added by: instructor
- Date: YYYY-MM-DD

## Processed
```

### `maintenance/log.md`

Chronological record of changes.

```markdown
# Project Log

## [YYYY-MM-DD] update | Standard error lesson

- Revised explanation
- Added R simulation
- Added links to confidence intervals and hypothesis testing
```

### `maintenance/link-audit.md`

Place to track missing, weak, or desirable links.

```markdown
# Link Audit

## Orphan Pages

- None currently listed

## Suggested Links

- Link `standard-error` to `control-charts`
- Link `degrees-of-freedom` to `anova`
```

---

## 14. Local Development Commands

Render the site:

```bash
quarto render
```

Preview locally:

```bash
quarto preview
```

Render one lesson:

```bash
quarto render lessons/regression/simple-linear-regression.qmd
```

---

## 15. Publishing to GitHub Pages

Recommended deployment model:

1. Author and maintain source files locally
2. Render with Quarto
3. Publish generated HTML to GitHub Pages

Two common options:

### Option A: GitHub Actions

Best for ongoing maintenance. The site renders automatically when changes are pushed.

### Option B: Manual Render

Best for early development. Render locally and push the output.

---

## 16. Suggested Growth Path

### Phase 1: Scaffold

- Create Quarto site structure
- Add homepage, linear path, and dojo index
- Link existing wiki index

### Phase 2: Convert Core Lessons

Start with high-value foundational lessons:

1. Sampling distributions
2. Standard error
3. Confidence intervals
4. Hypothesis testing
5. Simple linear regression

### Phase 3: Add Coding Dojo

Create focused R drills:

1. Simulate the central limit theorem
2. Fit and interpret regression models
3. Build control charts
4. Fill ANOVA tables
5. Diagnose model assumptions

### Phase 4: Strengthen Graph Navigation

- Add backlinks
- Add related sections
- Audit orphan pages
- Build reference maps and decision trees

### Phase 5: Publish and Iterate

- Deploy with GitHub Pages
- Use in class
- Refine based on instructor and student needs

---

## 17. Design Principle

The site should behave like a textbook when students need sequence, and like a knowledge graph when students need connection.

The Quarto lessons provide the road.

The wiki provides the terrain.

The coding dojo provides the reps.

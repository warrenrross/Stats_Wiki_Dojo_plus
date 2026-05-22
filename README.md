# INEG 2314H — Statistical Methods

A living textbook for university-level statistical methods in industrial engineering. Built as a Quarto website combining a structured reference wiki, executable R lessons, and an interactive coding dojo.

**Live site:** https://warrenrross.github.io/Stats_Wiki_Dojo_plus/

---

## What this is

The site has three distinct layers that serve different learning purposes:

### Wiki
Static reference pages covering every major concept in the course — probability, distributions, hypothesis testing, regression, control charts, ANOVA, and experimental design. Each page is organized around the CPS framework (see [Design Decisions](#design-decisions) below) so you always know whether you're reading a definition, a procedure, or a worked example. 55+ pages across four directories: `concepts/`, `examples/`, `r-code/`, and `reference/`.

### Lessons
Executable `.qmd` files that combine written explanation, mathematical derivations, and R code that runs at build time. These walk through the core procedures step by step. If you're learning a technique for the first time, start here.

### Coding Dojo
Interactive R drills that run directly in your browser — no installation required. The five dojo pages cover the most exam-critical workflows: simulating the CLT, fitting a regression model, building control charts, reconstructing ANOVA tables, and factorial ANOVA. Each has a worked example (pre-rendered) and an interactive sandbox where you modify the code and re-run it.

---

## How to use the site

**New to a topic?** Start with the relevant Lesson page. It will introduce the concept, show the math, and demonstrate the R code with real output.

**Need a quick formula or decision rule?** Go to the Wiki. The `reference/` section has one-page cheat sheets for each course section. The `which-test` flowchart tells you which test to use when.

**Practicing for an exam?** Use the Coding Dojo. Open one of the five drill pages, read the worked example, then modify the parameters in the interactive sandbox and re-run. The fill-anova-table drill is especially useful for reconstructing partial ANOVA tables from scratch.

**Looking for a specific concept?** Use the search bar (top right) or go to the Wiki Index for a full catalog organized by section and tier.

---

## Design decisions

### CPS cognitive tiers

Every wiki page carries a tier label: **Construct**, **Procedure**, or **Script**.

- **Construct** — a mathematical building block with no fixed procedure. Standard error, degrees of freedom, and distributions are constructs. You use them inside other techniques.
- **Procedure** — an analytical technique that assembles constructs and requires judgment about which variant to apply. Hypothesis tests, regression, and control charts are procedures.
- **Script** — a fixed-sequence workflow where all decisions are already collapsed. Worked examples and R walkthroughs are scripts. You learn them by practicing the sequence until it's automatic.

This distinction matters because it tells you *how* to study each page. Constructs need to be understood; procedures need to be practiced with judgment; scripts need to be drilled until they're automatic.

### WebR for interactive code

The Coding Dojo uses [WebR](https://docs.r-wasm.org/webr/latest/) — R compiled to WebAssembly — so code runs in your browser without any local R installation. When a dojo page loads, it downloads the required packages (ggplot2, qcc, agricolae, etc.) from the WebR repository. This takes 10–30 seconds on first load depending on your connection. Once loaded, the interactive cells let you edit and re-run code freely.

The worked example sections on each dojo page are pre-rendered server-side (static output), so you can always read them even if WebR hasn't loaded yet.

**In RStudio:** `{webr-r}` code chunks are treated as standard `{r}` chunks and execute normally with knitr. The dojo pages work as local notebooks with no changes needed.

### Frozen execution cache

R code in the lessons is executed at build time and the results are cached in `_freeze/`. This means the deployed site never needs R installed — GitHub Pages serves the pre-computed output. If you edit a lesson `.qmd` locally, Quarto will detect the change and re-execute only that file when you run `quarto render`.

### No Obsidian wikilinks

The wiki pages are plain Markdown rendered by Quarto. All cross-references use standard relative Markdown links (`[page name](../concepts/page.md)`), not Obsidian-style `[[wikilinks]]`. If you add new wiki pages, use relative paths.

---

## Running locally

Requires [Quarto](https://quarto.org/docs/get-started/) (1.9+) and R with the following packages: `qcc`, `agricolae`, `FrF2`, `tidyverse`, `pacman`.

```bash
# Preview with live reload
quarto preview

# Full render
quarto render

# Deploy (after first setup)
quarto publish gh-pages
```

---

## Course coverage

| Section | Topics |
|---------|--------|
| 1–2 | Sampling distributions, standard error, confidence intervals, hypothesis testing (z, t, χ², F), proportions, chi-square tests |
| 3 | Simple and multiple linear regression, model adequacy, control charts (X̄-R, p, c, u), process capability |
| 4 | CRD one-way ANOVA, RCBD blocking, factorial ANOVA, 2^k factorial design, random effects |

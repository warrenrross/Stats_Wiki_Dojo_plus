---
tags: [reference, concept]
tier: reference
sources: [knowledge-dimensions.md]
---
# Wiki Taxonomy — CPS Framework

Quick-lookup tier map for this wiki. Full theory at [[knowledge-dimensions]].

---

## The Three Tiers

| Tier | Name | What It Is | Study Cue |
|------|------|-----------|-----------|
| 1 | **Construct** | A mathematical quantity with context-variable formula variants — no steps, just recognition | "Understand this deeply — it shows up inside 5+ procedures in different forms." |
| 2 | **Procedure** | A technique assembling 2+ constructs; requires judgment about when and which variant | "Know when to use it. Know which constructs it calls." |
| 3 | **Script** | A fixed-sequence workflow — all decisions already collapsed; errors are arithmetic, not conceptual | "Practice until automatic. Recognize which script each exam scenario triggers." |

**Reference** pages (formula sheets, flowcharts) span multiple tiers — no tier assigned.

---

## Complete Page Map

### Tier 1 — Constructs

| Page | Why It's a Construct |
|------|---------------------|
| [standard-error](standard-error.md) | One concept (SD of sampling distribution) — formula slot varies by estimator and sample structure |
| [degrees-of-freedom](degrees-of-freedom.md) | Appears in every t, F, and χ² test with a different formula; not itself a technique |
| [variance-estimation](variance-estimation.md) | s², MSE, R̄/d₂, s̄/c₄ are all one idea — context changes which slot to use |
| [distributions](distributions.md) | t, χ², F, normal are called by procedures; not themselves inferential techniques |
| [probability](probability.md) | Foundation for all probability calculations; rules combine across contexts |
| [ss-decomposition](ss-decomposition.md) | The SS partition identity (SS_T = SS_Model + SS_E) underlies every ANOVA table; appears in 7+ procedures without a shared name |

### Tier 2 — Procedures (Unit 2: Inference)

**Broad coverage pages:**

| Page | Goal |
|------|------|
| [confidence-intervals](confidence-intervals.md) | Build an interval estimate on a parameter |
| [hypothesis-testing-overview](hypothesis-testing-overview.md) | 7-step test of a claim about a parameter |
| [which-test](which-test.md) | Meta-procedure: decide which test to use |
| [two-sample-tests](two-sample-tests.md) | Compare two populations (Z, pooled t, Welch t, paired t, F) |
| [chi-square](chi-square.md) | GoF and independence tests using categorical data |
| [proportions](proportions.md) | Test/estimate a population proportion |
| [power-sample-size](power-sample-size.md) | Compute required n or evaluate power for t-test and ANOVA F-test |

**Per-test pages (one per test, linked from [ht-tests-overview](../reference/ht-tests-overview.md)):**

| Page | Test |
|------|------|
| [ht-one-sample-z-mean](ht-one-sample-z-mean.md) | One-sample Z on mean (σ known or n≥40) |
| [ht-one-sample-t-mean](ht-one-sample-t-mean.md) | One-sample T on mean (σ unknown) |
| [ht-one-sample-chisq-variance](ht-one-sample-chisq-variance.md) | One-sample χ² on variance |
| [ht-one-sample-z-proportion](ht-one-sample-z-proportion.md) | One-sample Z on proportion |
| [ht-goodness-of-fit](ht-goodness-of-fit.md) | χ² Goodness-of-Fit (df = k−1−p) |
| [ht-independence](ht-independence.md) | χ² Test of Independence |
| [ht-two-sample-z-means](ht-two-sample-z-means.md) | Two-sample Z on means (both σ known) |
| [ht-two-sample-t-means](ht-two-sample-t-means.md) | Two-sample T on means (pooled or Welch) |
| [ht-paired-t](ht-paired-t.md) | Paired T-test |
| [ht-two-sample-f-variances](ht-two-sample-f-variances.md) | Two-sample F on equal variances |

### Tier 2 — Procedures (Units 3 and 4: Regression and Quality)

| Page | Goal |
|------|------|
| [regression-slr](regression-slr.md) | Fit and interpret a simple linear regression model |
| [regression-mlr](regression-mlr.md) | Extend regression to multiple predictors |
| [regression-ht](regression-ht.md) | Test individual βⱼ and overall model significance |
| [regression-ci](regression-ci.md) | CI on βⱼ, CI on mean response, PI on future observation |
| [model-adequacy](model-adequacy.md) | Diagnose assumption violations from residual plots |
| [correlation-transformations](correlation-transformations.md) | Test H₀:ρ=0 (and H₀:ρ=ρ₀), linearizing transformations |
| [control-charts](control-charts.md) | Monitor a process with X̄/R, X̄/S, p, c, u charts |
| [process-capability](process-capability.md) | Compute Cp/Cpk and assess spec conformance |

### Tier 2 — Procedures (Unit 5)

| Page | Goal |
|------|------|
| [crd-one-way-anova](crd-one-way-anova.md) | Test equality of 3+ treatment means (no nuisance variable) |
| [rcbd-blocking](rcbd-blocking.md) | Block for a nuisance variable; ANOVA with blocks |
| [factorial-anova](factorial-anova.md) | Test main effects and interactions in multi-factor experiments |
| [2k-factorial-design](2k-factorial-design.md) | Screen and estimate effects with 2-level factors |
| [random-effects-model](random-effects-model.md) | Estimate variance components when τᵢ is random |

### Tier 3 — Scripts (Examples)

| Page | Trigger Scenario |
|------|-----------------|
| [regression-ci-examples](../examples/regression-ci-examples.md) | "Find CI on β₁ / CI on mean response / PI on a new obs" |
| [model-adequacy-examples](../examples/model-adequacy-examples.md) | "Diagnose residual plots and check assumptions" |
| [anova-table-examples](../examples/anova-table-examples.md) | "Complete the partial ANOVA / regression summary table" |
| [control-chart-examples](../examples/control-chart-examples.md) | "Apply WE rules / read qcc output / compute Cp/Cpk" |
| [control-chart-practice](../examples/control-chart-practice.md) | "Compute X̄/R chart limits / p-chart limits from scratch" |
| [crd-examples](../examples/crd-examples.md) | "Run one-way ANOVA in R; compute CI on treatment difference" |
| [factorial-examples](../examples/factorial-examples.md) | "Interpret 2-factor ANOVA; complete partial ANOVA table" |
| [2k-factorial-examples](../examples/2k-factorial-examples.md) | "Compute effects manually / read Daniel plot" |

### Tier 3 — Scripts (R Code)

| Page | What It Automates |
|------|------------------|
| [summary-stats-r](../r-code/summary-stats-r.md) | Descriptive statistics in R |
| [hypothesis-tests-r](../r-code/hypothesis-tests-r.md) | t.test(), var.test(), chisq.test(), prop.test() |
| [regression-r](../r-code/regression-r.md) | lm(), anova(), confint(), predict(), diagnostics |
| [control-charts-r](../r-code/control-charts-r.md) | qcc package charts and process.capability() |
| [reading-r-output](../r-code/reading-r-output.md) | Translate every R output term to teacher phrasing |
| [anova-r](../r-code/anova-r.md) | CRD and RCBD templates, scalar extraction |
| [factorial-anova-r](../r-code/factorial-anova-r.md) | Multi-factor and 2^k patterns, DanielPlot() |

---

---

## Reference Pages (Untiered)

| Page | Purpose |
|------|---------|
| [formula-sheet](../reference/formula-sheet.md) | All formulas, all sections |
| [which-test-flowchart](../reference/which-test-flowchart.md) | Quick test-selection flowchart |
| [ht-tests-overview](../reference/ht-tests-overview.md) | Unit 2 all-tests summary table (a–j) with links to per-test pages |
| [quick-reference-section3](../reference/quick-reference-section3.md) | Exam 3 print-ready formula sheet |
| [quick-reference-section4](../reference/quick-reference-section4.md) | Unit 5 compact formula sheet |
| [anova-design-guide](../reference/anova-design-guide.md) | DOE design decision table |

---

## Related
- [[knowledge-dimensions]] — full theoretical grounding (Anderson, Schema Theory, Cognitive Load)
- [which-test](which-test.md) — Tier 2 meta-procedure for test selection
- [formula-sheet](../reference/formula-sheet.md) — cross-tier reference (untiered)

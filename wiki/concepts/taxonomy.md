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
| [[standard-error]] | One concept (SD of sampling distribution) — formula slot varies by estimator and sample structure |
| [[degrees-of-freedom]] | Appears in every t, F, and χ² test with a different formula; not itself a technique |
| [[variance-estimation]] | s², MSE, R̄/d₂, s̄/c₄ are all one idea — context changes which slot to use |
| [[distributions]] | t, χ², F, normal are called by procedures; not themselves inferential techniques |
| [[probability]] | Foundation for all probability calculations; rules combine across contexts |
| [[ss-decomposition]] | The SS partition identity (SS_T = SS_Model + SS_E) underlies every ANOVA table; appears in 7+ procedures without a shared name |

### Tier 2 — Procedures (Section 1–2)

**Broad coverage pages:**

| Page | Goal |
|------|------|
| [[confidence-intervals]] | Build an interval estimate on a parameter |
| [[hypothesis-testing-overview]] | 7-step test of a claim about a parameter |
| [[which-test]] | Meta-procedure: decide which test to use |
| [[two-sample-tests]] | Compare two populations (Z, pooled t, Welch t, paired t, F) |
| [[chi-square]] | GoF and independence tests using categorical data |
| [[proportions]] | Test/estimate a population proportion |
| [[power-sample-size]] | Compute required n or evaluate power for t-test and ANOVA F-test |

**Per-test pages (one per test, linked from [[ht-tests-overview]]):**

| Page | Test |
|------|------|
| [[ht-one-sample-z-mean]] | One-sample Z on mean (σ known or n≥40) |
| [[ht-one-sample-t-mean]] | One-sample T on mean (σ unknown) |
| [[ht-one-sample-chisq-variance]] | One-sample χ² on variance |
| [[ht-one-sample-z-proportion]] | One-sample Z on proportion |
| [[ht-goodness-of-fit]] | χ² Goodness-of-Fit (df = k−1−p) |
| [[ht-independence]] | χ² Test of Independence |
| [[ht-two-sample-z-means]] | Two-sample Z on means (both σ known) |
| [[ht-two-sample-t-means]] | Two-sample T on means (pooled or Welch) |
| [[ht-paired-t]] | Paired T-test |
| [[ht-two-sample-f-variances]] | Two-sample F on equal variances |

### Tier 2 — Procedures (Section 3)

| Page | Goal |
|------|------|
| [[regression-slr]] | Fit and interpret a simple linear regression model |
| [[regression-mlr]] | Extend regression to multiple predictors |
| [[regression-ht]] | Test individual βⱼ and overall model significance |
| [[regression-ci]] | CI on βⱼ, CI on mean response, PI on future observation |
| [[model-adequacy]] | Diagnose assumption violations from residual plots |
| [[correlation-transformations]] | Test H₀:ρ=0 (and H₀:ρ=ρ₀), linearizing transformations |
| [[control-charts]] | Monitor a process with X̄/R, X̄/S, p, c, u charts |
| [[process-capability]] | Compute Cp/Cpk and assess spec conformance |

### Tier 2 — Procedures (Section 4)

| Page | Goal |
|------|------|
| [[crd-one-way-anova]] | Test equality of 3+ treatment means (no nuisance variable) |
| [[rcbd-blocking]] | Block for a nuisance variable; ANOVA with blocks |
| [[factorial-anova]] | Test main effects and interactions in multi-factor experiments |
| [[2k-factorial-design]] | Screen and estimate effects with 2-level factors |
| [[random-effects-model]] | Estimate variance components when τᵢ is random |

### Tier 3 — Scripts (Examples)

| Page | Trigger Scenario |
|------|-----------------|
| [[regression-ci-examples]] | "Find CI on β₁ / CI on mean response / PI on a new obs" |
| [[model-adequacy-examples]] | "Diagnose residual plots and check assumptions" |
| [[anova-table-examples]] | "Complete the partial ANOVA / regression summary table" |
| [[control-chart-examples]] | "Apply WE rules / read qcc output / compute Cp/Cpk" |
| [[control-chart-practice]] | "Compute X̄/R chart limits / p-chart limits from scratch" |
| [[crd-examples]] | "Run one-way ANOVA in R; compute CI on treatment difference" |
| [[factorial-examples]] | "Interpret 2-factor ANOVA; complete partial ANOVA table" |
| [[2k-factorial-examples]] | "Compute effects manually / read Daniel plot" |

### Tier 3 — Scripts (R Code)

| Page | What It Automates |
|------|------------------|
| [[summary-stats-r]] | Descriptive statistics in R |
| [[hypothesis-tests-r]] | t.test(), var.test(), chisq.test(), prop.test() |
| [[regression-r]] | lm(), anova(), confint(), predict(), diagnostics |
| [[control-charts-r]] | qcc package charts and process.capability() |
| [[reading-r-output]] | Translate every R output term to teacher phrasing |
| [[anova-r]] | CRD and RCBD templates, scalar extraction |
| [[factorial-anova-r]] | Multi-factor and 2^k patterns, DanielPlot() |

---

---

## Reference Pages (Untiered)

| Page | Purpose |
|------|---------|
| [[formula-sheet]] | All formulas, all sections |
| [[which-test-flowchart]] | Quick test-selection flowchart |
| [[ht-tests-overview]] | Section 1–2 all-tests summary table (a–j) with links to per-test pages |
| [[quick-reference-section3]] | Exam 3 print-ready formula sheet |
| [[quick-reference-section4]] | Section 4 compact formula sheet |
| [[anova-design-guide]] | DOE design decision table |

---

## Related
- [[knowledge-dimensions]] — full theoretical grounding (Anderson, Schema Theory, Cognitive Load)
- [[which-test]] — Tier 2 meta-procedure for test selection
- [[formula-sheet]] — cross-tier reference (untiered)

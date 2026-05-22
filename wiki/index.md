# Wiki Index

Catalog of all pages in this wiki. Updated on every ingest.
Read this first when answering a query — find relevant pages, then drill in.

**Tier guide:** [taxonomy](concepts/taxonomy.md) — see how Constructs, Procedures, and Scripts differ and when to study each type.

---

## Tier 1 — Constructs (Cross-Cutting)

These appear as building blocks inside multiple Procedures. Understand them deeply — a weak Construct makes every Procedure that uses it unstable under novel conditions.

| Page | Summary |
|------|---------|
| [standard-error](concepts/standard-error.md) | Every SE formula in one place — means, proportions, regression coefficients, CI/PI bands |
| [degrees-of-freedom](concepts/degrees-of-freedom.md) | Every df formula — one/two-sample, chi-square, F, regression ANOVA, RCBD, factorial, Welch ν |
| [variance-estimation](concepts/variance-estimation.md) | How σ² is estimated in each context: s², pooled s², MSE, R̄/d₂, s̄/c₄ |
| [distributions](concepts/distributions.md) | Discrete (binomial, PMF), normal, t, chi-square, F; CLT; summary stats formulas |
| [probability](concepts/probability.md) | Sample spaces, rules of probability, conditional probability, counting |
| [ss-decomposition](concepts/ss-decomposition.md) | SS_T = SS_Model + SS_Error — the identity underlying every ANOVA table in the course |

---

## Unit 1: Foundations

### Tier 2 — Procedures

| Page | Summary |
|------|---------|
| [confidence-intervals](concepts/confidence-intervals.md) | Z and t intervals on μ; χ² interval on σ²; Z vs t decision; sample size |

### Tier 3 — Scripts

| Page | Summary |
|------|---------|
| [summary-stats-r](r-code/summary-stats-r.md) | Descriptive statistics: mean, sd, summary(), histogram, boxplot |

---

## Unit 2: Inference

### Tier 2 — Procedures

| Page | Summary |
|------|---------|
| [hypothesis-testing-overview](concepts/hypothesis-testing-overview.md) | 7-step procedure, H₀/H₁ setup, Type I/II error, Z-test, t-test, p-value, β, power |
| [which-test](concepts/which-test.md) | Full decision flowchart — mean, variance, proportion, two means, ANOVA, factorial |
| [two-sample-tests](concepts/two-sample-tests.md) | 2-sample Z, pooled t, Welch t, paired t, F-test on variances; all formulas + CIs |
| [chi-square](concepts/chi-square.md) | Goodness-of-fit (df=k−1), test of independence (df=(r−1)(c−1)), HT on variance |
| [proportions](concepts/proportions.md) | HT on proportion Z-test, CI on p, sample size formulas |
| [ht-one-sample-z-mean](concepts/ht-one-sample-z-mean.md) | One-sample Z on mean: σ known or n≥40; test stat, CI, β, sample size |
| [ht-one-sample-t-mean](concepts/ht-one-sample-t-mean.md) | One-sample T on mean: σ unknown, n<40; df=n−1 |
| [ht-one-sample-chisq-variance](concepts/ht-one-sample-chisq-variance.md) | One-sample χ² on variance; df=n−1; asymmetric CI |
| [ht-one-sample-z-proportion](concepts/ht-one-sample-z-proportion.md) | Z on proportion; count and proportion forms; CI uses P̂ not p₀ |
| [ht-goodness-of-fit](concepts/ht-goodness-of-fit.md) | χ² GoF: df = k−1−p (subtract estimated parameters); always upper-tail |
| [ht-independence](concepts/ht-independence.md) | χ² independence: Eᵢⱼ from marginals; df=(r−1)(c−1); always upper-tail |
| [ht-two-sample-z-means](concepts/ht-two-sample-z-means.md) | Two-sample Z on means: both σ² known; CI on μ₁−μ₂ |
| [ht-two-sample-t-means](concepts/ht-two-sample-t-means.md) | Two-sample T: Case 1 pooled (equal σ²) and Case 2 Welch (unequal σ²); Welch df formula |
| [ht-paired-t](concepts/ht-paired-t.md) | Paired T: compute differences first; df=n−1 (pairs); more powerful than 2-sample T |
| [ht-two-sample-f-variances](concepts/ht-two-sample-f-variances.md) | F-test on two variances; larger s² in numerator; run before choosing pooled vs Welch |
| [power-sample-size](concepts/power-sample-size.md) | β, power = 1−β, and required n — Z-test (exact), t-test and ANOVA F-test (OC curve); R: power.t.test(), power.anova.test() |

### Tier 3 — Scripts

| Page | Summary |
|------|---------|
| [hypothesis-tests-r](r-code/hypothesis-tests-r.md) | t.test(), var.test(), chisq.test(), prop.test(), critical values |
| [hw1-examples](examples/hw1-examples.md) | Normal distribution quantiles and probabilities (credit card, machinery); descriptive stats from sample data |
| [hw4-drill-examples](examples/hw4-drill-examples.md) | AirPassengers time series (tsibble → tidy → group_by → ggplot); Titanic frequency table (uncount, left_join, proportion by class) |
| [two-sample-examples](examples/two-sample-examples.md) | Pooled t (equal variances), Welch t (unequal variances after F-test), paired t — 3 worked problems with R |

---

## Unit 3: Regression

### Tier 2 — Procedures

| Page | Summary |
|------|---------|
| [regression-slr](concepts/regression-slr.md) | Model, least squares β̂₀/β̂₁, SS decomposition, R², F-test, t-tests, SLR formulas |
| [regression-mlr](concepts/regression-mlr.md) | MLR model, matrix form, ANOVA, R²_adj, interaction terms, MLR-specific traps |
| [regression-ht](concepts/regression-ht.md) | t-tests on βⱼ (including non-zero null), F-test, partial ANOVA table completion |
| [regression-ci](concepts/regression-ci.md) | CI on βⱼ (confint), CI on mean response, PI on future obs; CI vs PI comparison |
| [model-adequacy](concepts/model-adequacy.md) | Residual plots, 4 assumptions, outliers vs leverage vs influence, Cook's D |
| [correlation-transformations](concepts/correlation-transformations.md) | Pearson r, HT for ρ=0 and ρ=ρ₀ (Fisher Z), linearizing transformations |

### Tier 3 — Scripts

| Page | Summary |
|------|---------|
| [regression-r](r-code/regression-r.md) | Full workflow: lm(), anova(), summary(), confint(), predict(), diagnostics |
| [reading-r-output](r-code/reading-r-output.md) | Teacher-language guide for ALL R output terms — exam answer phrasing |
| [regression-examples](examples/regression-examples.md) | WireBond SLR: fit model, read summary output, complete ANOVA table, non-zero null β₁ test, CI vs PI |
| [regression-ci-examples](examples/regression-ci-examples.md) | CI/PI on βⱼ, mean response, and future observation — all 6 L36-37 homework problems (SLR & MLR) |
| [model-adequacy-examples](examples/model-adequacy-examples.md) | R², normality check (QQ + Shapiro-Wilk), residual plots, Cook's D — NFL QB example |
| [anova-table-examples](examples/anova-table-examples.md) | Completing partial ANOVA/summary tables; σ̂ = √MSE; recommendations from R output; DOE (RCBD) reverse-engineer from MS and F |

---

## Unit 4: Quality Methods

### Tier 2 — Procedures

| Page | Summary |
|------|---------|
| [control-charts](concepts/control-charts.md) | X̄/R, X̄/S, p-chart, c-chart, u-chart; control limits formulas; run rules; revising limits |
| [process-capability](concepts/process-capability.md) | Cp, Cpk, σ̂ from control chart, spec limits vs control limits; interpretation |

### Tier 3 — Scripts

| Page | Summary |
|------|---------|
| [control-charts-r](r-code/control-charts-r.md) | qcc package: xbar/R/S charts, p/c/u-charts, process.capability() |
| [control-chart-examples](examples/control-chart-examples.md) | WE rule application; reading qcc output; Cp/Cpk interpretation; chart characteristics |
| [control-chart-practice](examples/control-chart-practice.md) | 5 hand-calc practice problems: X̄/R limits, Cp/Cpk, raw-data subgroups, p-chart, WE rules |

---

## Unit 5: Experimental Design (DOE)

### Tier 2 — Procedures

| Page | Summary |
|------|---------|
| [crd-one-way-anova](concepts/crd-one-way-anova.md) | CRD model, ANOVA table (balanced/unbalanced), Fisher LSD, CI formulas, residual diagnostics |
| [rcbd-blocking](concepts/rcbd-blocking.md) | RCBD model, blocking for nuisance variable, df_error=(a−1)(b−1), variance components; CRD-vs-RCBD comparison showing how ignoring blocks inflates MS_Error |
| [factorial-anova](concepts/factorial-anova.md) | 2- and 3-factor factorial, main effects, interaction effects, ANOVA table df, interaction plot; 3× SD rule, marginality principle, LSD on marginal means |
| [2k-factorial-design](concepts/2k-factorial-design.md) | 2^k design, ±1 coding, effects/SS/contrasts, Daniel plot, lm() vs aov(), R vs Minitab; Lenth PSE/ME, single/two/three-replicate R patterns, null-result trap, borderline F rule |
| [random-effects-model](concepts/random-effects-model.md) | Fixed vs random distinction, variance components σ̂²τ=(MS_Trt−MSE)/n |

### Tier 3 — Scripts

| Page | Summary |
|------|---------|
| [anova-r](r-code/anova-r.md) | CRD and RCBD R templates, scalar extraction, %$% pipe, melt() vs gather(), output walkthrough |
| [data-wrangling-r](r-code/data-wrangling-r.md) | wide → long with melt(): before/after table, id.vars, keeping both shapes, NA pattern |
| [factorial-anova-r](r-code/factorial-anova-r.md) | 2/3/4-factor and 2^k R patterns, DanielPlot(), mutate_if vs mutate_at, lm() vs aov() side-by-side; trimws() rule, LSD.test(), pivot_longer for 2/3-replicate designs |
| [crd-examples](examples/crd-examples.md) | Balanced CRD (rodding/concrete) and unbalanced CRD (carbon/roughness) — 3 exam traps |
| [factorial-examples](examples/factorial-examples.md) | Primer paint 2-factor + surface roughness 3-factor — full ANOVA tables, interaction interpretation |
| [2k-factorial-examples](examples/2k-factorial-examples.md) | Epitaxial layer 2^2 (manual effects + R code) + unreplicated 2^3 Daniel plot |

---

## Reference (Untiered)

Quick-lookup pages spanning multiple tiers.

| Page | Summary |
|------|---------|
| [formula-sheet](reference/formula-sheet.md) | Consolidated formula reference — all sections, all tests, regression, control charts, DOE |
| [which-test-flowchart](reference/which-test-flowchart.md) | Quick-lookup flowchart for selecting the right test + "which t?" guide |
| [quick-reference-section3](reference/quick-reference-section3.md) | Exam quick reference — all Units 3–4 formulas, tables, WE rules, PCR/PCRk, t critical values |
| [anova-design-guide](reference/anova-design-guide.md) | Design decision table (CRD/RCBD/factorial/2^k), df by design, LSD/CI formulas, key distinctions |
| [quick-reference-section4](reference/quick-reference-section4.md) | Compact Unit 5 formula sheet — all ANOVA tables, Fisher LSD, 2^k effects, R cheat sheet |
| [ht-tests-overview](reference/ht-tests-overview.md) | Unit 2 all-tests summary table (a–j) with links to per-test pages; decision flow; z critical values |
| [knowledge-dimensions](reference/knowledge-dimensions.md) | CPS framework theory — Anderson, Schema Theory, Cognitive Load, Threshold Concepts; implementation blueprint for knowledge graph–style wikis |

---

## Meta / Wiki Design

| File | Purpose |
|------|---------|
| [taxonomy](concepts/taxonomy.md) | CPS page mapping — all pages classified by tier with rationale; study guide for what to learn how |
| [backlinks](backlinks.md) | Expected inbound links for hub pages — agent audit tool for backlink coverage |

---

*Last updated: 2026-05-22 (session 8) — knowledge-dimensions moved into wiki/reference/ and rendered in Quarto; backlinks.md created (agent audit tool); taxonomy updated with all current pages. Constructs: 5. Procedures: 29. Scripts: 19. Reference: 7.*

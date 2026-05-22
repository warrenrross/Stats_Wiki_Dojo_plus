# Wiki Index

Catalog of all pages in this wiki. Updated on every ingest.
Read this first when answering a query — find relevant pages, then drill in.

**Tier guide:** [[taxonomy]] — see how Constructs, Procedures, and Scripts differ and when to study each type.

---

## Tier 1 — Constructs (Cross-Cutting)

These appear as building blocks inside multiple Procedures. Understand them deeply — a weak Construct makes every Procedure that uses it unstable under novel conditions.

| Page | Summary |
|------|---------|
| [[standard-error]] | Every SE formula in one place — means, proportions, regression coefficients, CI/PI bands |
| [[degrees-of-freedom]] | Every df formula — one/two-sample, chi-square, F, regression ANOVA, RCBD, factorial, Welch ν |
| [[variance-estimation]] | How σ² is estimated in each context: s², pooled s², MSE, R̄/d₂, s̄/c₄ |
| [[distributions]] | Discrete (binomial, PMF), normal, t, chi-square, F; CLT; summary stats formulas |
| [[probability]] | Sample spaces, rules of probability, conditional probability, counting |
| [[ss-decomposition]] | SS_T = SS_Model + SS_Error — the identity underlying every ANOVA table in the course |

---

## Section 1–2: Probability, Distributions, Inference

### Tier 2 — Procedures

| Page | Summary |
|------|---------|
| [[confidence-intervals]] | Z and t intervals on μ; χ² interval on σ²; Z vs t decision; sample size |
| [[hypothesis-testing-overview]] | 7-step procedure, H₀/H₁ setup, Type I/II error, Z-test, t-test, p-value, β, power |
| [[which-test]] | Full decision flowchart — mean, variance, proportion, two means, ANOVA, factorial |
| [[two-sample-tests]] | 2-sample Z, pooled t, Welch t, paired t, F-test on variances; all formulas + CIs |
| [[chi-square]] | Goodness-of-fit (df=k−1), test of independence (df=(r−1)(c−1)), HT on variance |
| [[proportions]] | HT on proportion Z-test, CI on p, sample size formulas |
| [[ht-one-sample-z-mean]] | One-sample Z on mean: σ known or n≥40; test stat, CI, β, sample size |
| [[ht-one-sample-t-mean]] | One-sample T on mean: σ unknown, n<40; df=n−1 |
| [[ht-one-sample-chisq-variance]] | One-sample χ² on variance; df=n−1; asymmetric CI |
| [[ht-one-sample-z-proportion]] | Z on proportion; count and proportion forms; CI uses P̂ not p₀ |
| [[ht-goodness-of-fit]] | χ² GoF: df = k−1−p (subtract estimated parameters); always upper-tail |
| [[ht-independence]] | χ² independence: Eᵢⱼ from marginals; df=(r−1)(c−1); always upper-tail |
| [[ht-two-sample-z-means]] | Two-sample Z on means: both σ² known; CI on μ₁−μ₂ |
| [[ht-two-sample-t-means]] | Two-sample T: Case 1 pooled (equal σ²) and Case 2 Welch (unequal σ²); Welch df formula |
| [[ht-paired-t]] | Paired T: compute differences first; df=n−1 (pairs); more powerful than 2-sample T |
| [[ht-two-sample-f-variances]] | F-test on two variances; larger s² in numerator; run before choosing pooled vs Welch |
| [[power-sample-size]] | β, power = 1−β, and required n — Z-test (exact), t-test and ANOVA F-test (OC curve); R: power.t.test(), power.anova.test() |

### Tier 3 — Scripts

| Page | Summary |
|------|---------|
| [[summary-stats-r]] | Descriptive statistics: mean, sd, summary(), histogram, boxplot |
| [[hypothesis-tests-r]] | t.test(), var.test(), chisq.test(), prop.test(), critical values |
| [[hw1-examples]] | Homework 1 worked problems — descriptive stats and basic probability (stub) |
| [[hw4-drill-examples]] | Drill Homework 4 worked problems (stub) |
| [[two-sample-examples]] | 2-sample Z/t and paired t worked examples from L22–23 (stub) |

---

## Section 3: Regression, Control Charts

### Tier 2 — Procedures

| Page | Summary |
|------|---------|
| [[regression-slr]] | Model, least squares β̂₀/β̂₁, SS decomposition, R², F-test, t-tests, SLR formulas |
| [[regression-mlr]] | MLR model, matrix form, ANOVA, R²_adj, interaction terms, MLR-specific traps |
| [[regression-ht]] | t-tests on βⱼ (including non-zero null), F-test, partial ANOVA table completion |
| [[regression-ci]] | CI on βⱼ (confint), CI on mean response, PI on future obs; CI vs PI comparison |
| [[model-adequacy]] | Residual plots, 4 assumptions, outliers vs leverage vs influence, Cook's D |
| [[correlation-transformations]] | Pearson r, HT for ρ=0 and ρ=ρ₀ (Fisher Z), linearizing transformations |
| [[control-charts]] | X̄/R, X̄/S, p-chart, c-chart, u-chart; control limits formulas; run rules; revising limits |
| [[process-capability]] | Cp, Cpk, σ̂ from control chart, spec limits vs control limits; interpretation |

### Tier 3 — Scripts

| Page | Summary |
|------|---------|
| [[regression-r]] | Full workflow: lm(), anova(), summary(), confint(), predict(), diagnostics |
| [[control-charts-r]] | qcc package: xbar/R/S charts, p/c/u-charts, process.capability() |
| [[reading-r-output]] | Teacher-language guide for ALL R output terms — exam answer phrasing |
| [[regression-examples]] | Rocket Motor SLR: summary table reading, ANOVA completion, non-zero null tests (stub) |
| [[regression-ci-examples]] | CI/PI on βⱼ, mean response, and future observation — all 6 L36-37 homework problems (SLR & MLR) |
| [[model-adequacy-examples]] | R², normality check (QQ + Shapiro-Wilk), residual plots, Cook's D — NFL QB example |
| [[anova-table-examples]] | Completing partial ANOVA/summary tables; σ̂ = √MSE; recommendations from R output; DOE (RCBD) reverse-engineer from MS and F |
| [[control-chart-examples]] | WE rule application; reading qcc output; Cp/Cpk interpretation; chart characteristics |
| [[control-chart-practice]] | 5 hand-calc practice problems: X̄/R limits, Cp/Cpk, raw-data subgroups, p-chart, WE rules |

---

## Section 4: Experimental Design (DOE)

### Tier 2 — Procedures

| Page | Summary |
|------|---------|
| [[crd-one-way-anova]] | CRD model, ANOVA table (balanced/unbalanced), Fisher LSD, CI formulas, residual diagnostics |
| [[rcbd-blocking]] | RCBD model, blocking for nuisance variable, df_error=(a−1)(b−1), variance components; CRD-vs-RCBD comparison showing how ignoring blocks inflates MS_Error |
| [[factorial-anova]] | 2- and 3-factor factorial, main effects, interaction effects, ANOVA table df, interaction plot; 3× SD rule, marginality principle, LSD on marginal means |
| [[2k-factorial-design]] | 2^k design, ±1 coding, effects/SS/contrasts, Daniel plot, lm() vs aov(), R vs Minitab; Lenth PSE/ME, single/two/three-replicate R patterns, null-result trap, borderline F rule |
| [[random-effects-model]] | Fixed vs random distinction, variance components σ̂²τ=(MS_Trt−MSE)/n |

### Tier 3 — Scripts

| Page | Summary |
|------|---------|
| [[anova-r]] | CRD and RCBD R templates, scalar extraction, %$% pipe, melt() vs gather(), output walkthrough |
| [[data-wrangling-r]] | wide → long with melt(): before/after table, id.vars, keeping both shapes, NA pattern |
| [[factorial-anova-r]] | 2/3/4-factor and 2^k R patterns, DanielPlot(), mutate_if vs mutate_at, lm() vs aov() side-by-side; trimws() rule, LSD.test(), pivot_longer for 2/3-replicate designs |
| [[crd-examples]] | Balanced CRD (rodding/concrete) and unbalanced CRD (carbon/roughness) — 3 exam traps |
| [[factorial-examples]] | Primer paint 2-factor + surface roughness 3-factor — full ANOVA tables, interaction interpretation |
| [[2k-factorial-examples]] | Epitaxial layer 2^2 (manual effects + R code) + unreplicated 2^3 Daniel plot |

---

## Reference (Untiered)

Quick-lookup pages spanning multiple tiers.

| Page | Summary |
|------|---------|
| [[formula-sheet]] | Consolidated formula reference — all sections, all tests, regression, control charts, DOE |
| [[which-test-flowchart]] | Quick-lookup flowchart for selecting the right test + "which t?" guide |
| [[quick-reference-section3]] | Exam quick reference — all Section 3 formulas, tables, WE rules, PCR/PCRk, t critical values |
| [[anova-design-guide]] | Design decision table (CRD/RCBD/factorial/2^k), df by design, LSD/CI formulas, key distinctions |
| [[quick-reference-section4]] | Compact Section 4 formula sheet — all ANOVA tables, Fisher LSD, 2^k effects, R cheat sheet |
| [[ht-tests-overview]] | Section 1–2 all-tests summary table (a–j) with links to per-test pages; decision flow; z critical values |

---

## Meta / Wiki Design

| File | Purpose |
|------|---------|
| [[taxonomy]] | CPS page mapping — all 39 pages classified by tier with rationale; study guide for what to learn how |
| [[knowledge-dimensions]] | Full theoretical grounding — Anderson, Schema Theory, Cognitive Load, Threshold Concepts |

---

*Last updated: 2026-04-23 (session 6) — Section 1–2 per-test pages created. 10 new procedure pages (ht-one-sample-z-mean through ht-two-sample-f-variances) + 1 new reference page (ht-tests-overview). GoF df discrepancy documented: general form is k−1−p, not k−1. Constructs: 5. Procedures: 29. Scripts: 15. Reference: 6.*

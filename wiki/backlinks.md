# Backlinks Index

Agent audit tool. Specifies which pages are expected to link to each hub page. Used by the `lint-wiki` skill to detect under-linked pages that symmetric-Related checking alone would miss.

**When to use this file:**
- `lint-wiki` reads it to spot-check inbound links for each listed hub
- `ingest-examples` updates it when a new page uses a listed construct
- Run a full audit: for each entry, `grep` the source page for the target page name

**What belongs here vs. symmetry checking:**
- Hub pages where the relationship is **asymmetric** (procedures use a construct, but the construct page doesn't list every procedure that uses it)
- Same-tier sibling links (procedure ↔ procedure, example ↔ concept) are covered by the symmetric-Related convention and do NOT need entries here

---

## [standard-error](concepts/standard-error.md)

The universal SE formula (SD of a sampling distribution) appears in every CI, test statistic, regression coefficient, and control chart limit. Every procedure page that computes a test statistic or interval should link here.

Pages that should link to `standard-error`:

| Source page | Reason |
|-------------|--------|
| [confidence-intervals](concepts/confidence-intervals.md) | CI formula divides by SE |
| [hypothesis-testing-overview](concepts/hypothesis-testing-overview.md) | Test stat = (estimate − null) / SE |
| [two-sample-tests](concepts/two-sample-tests.md) | SE of difference of means |
| [regression-slr](concepts/regression-slr.md) | SE of β̂₁ and β̂₀ |
| [regression-mlr](concepts/regression-mlr.md) | SE of βⱼ from MLR |
| [regression-ht](concepts/regression-ht.md) | t = β̂ⱼ / SE(β̂ⱼ) |
| [regression-ci](concepts/regression-ci.md) | CI on βⱼ uses SE; CI/PI bands use SE of mean response |
| [control-charts](concepts/control-charts.md) | σ̂ = R̄/d₂ or s̄/c₄ plays the SE role in control limits |
| [ht-two-sample-z-means](concepts/ht-two-sample-z-means.md) | SE of X̄₁ − X̄₂ with known variances |
| [ht-two-sample-t-means](concepts/ht-two-sample-t-means.md) | Pooled SE and Welch SE |
| [ht-paired-t](concepts/ht-paired-t.md) | SE of D̄ = s_D / √n |
| [power-sample-size](concepts/power-sample-size.md) | n determines SE; n chosen to achieve target power |

---

## [ss-decomposition](concepts/ss-decomposition.md)

SS_T = SS_Model + SS_Error is the identity underlying every ANOVA table. Every page that builds or interprets an ANOVA table should link here.

Pages that should link to `ss-decomposition`:

| Source page | Reason |
|-------------|--------|
| [regression-slr](concepts/regression-slr.md) | SS_T = SS_R + SS_E is the SLR decomposition |
| [regression-mlr](concepts/regression-mlr.md) | Same identity; R² = SS_R / SS_T |
| [regression-ht](concepts/regression-ht.md) | F-test = MS_R / MS_E; both come from this partition |
| [crd-one-way-anova](concepts/crd-one-way-anova.md) | ANOVA identity: SS_T = SS_Trt + SS_E |
| [rcbd-blocking](concepts/rcbd-blocking.md) | Three-way partition: SS_T = SS_Trt + SS_Blk + SS_E |
| [factorial-anova](concepts/factorial-anova.md) | SS_Model split into main effects and interactions |
| [2k-factorial-design](concepts/2k-factorial-design.md) | Each effect gets its own SS row |
| [anova-table-examples](examples/anova-table-examples.md) | Every ANOVA table completion problem uses this identity |

---

## [degrees-of-freedom](concepts/degrees-of-freedom.md)

The df formula changes with every test and design. Every HT, CI, and ANOVA page has a specific df formula that belongs here.

Pages that should link to `degrees-of-freedom`:

| Source page | Reason |
|-------------|--------|
| [confidence-intervals](concepts/confidence-intervals.md) | t critical value uses df = n − 1 |
| [hypothesis-testing-overview](concepts/hypothesis-testing-overview.md) | df for one-sample t and chi-square |
| [two-sample-tests](concepts/two-sample-tests.md) | Pooled df = n₁+n₂−2; Welch df from Satterthwaite |
| [chi-square](concepts/chi-square.md) | GoF df = k−1−p; independence df = (r−1)(c−1) |
| [regression-slr](concepts/regression-slr.md) | df_Reg = 1, df_Res = n−2 |
| [regression-mlr](concepts/regression-mlr.md) | df_Reg = k, df_Res = n−k−1 |
| [regression-ht](concepts/regression-ht.md) | t-test df and F-test df |
| [crd-one-way-anova](concepts/crd-one-way-anova.md) | df_error = N − a |
| [rcbd-blocking](concepts/rcbd-blocking.md) | df_error = (a−1)(b−1) |
| [factorial-anova](concepts/factorial-anova.md) | df for main effects, interactions, error |
| [2k-factorial-design](concepts/2k-factorial-design.md) | df = 1 per effect; df_error from replicates |
| [ht-one-sample-t-mean](concepts/ht-one-sample-t-mean.md) | df = n − 1 |
| [ht-one-sample-chisq-variance](concepts/ht-one-sample-chisq-variance.md) | df = n − 1 |
| [ht-goodness-of-fit](concepts/ht-goodness-of-fit.md) | df = k − 1 − p |
| [ht-independence](concepts/ht-independence.md) | df = (r−1)(c−1) |

---

## [variance-estimation](concepts/variance-estimation.md)

How σ² is estimated differs by context: s² (one-sample), pooled s² (two-sample), MSE (regression/ANOVA), R̄/d₂ or s̄/c₄ (control charts). Every page that uses an estimated variance should link here.

Pages that should link to `variance-estimation`:

| Source page | Reason |
|-------------|--------|
| [confidence-intervals](concepts/confidence-intervals.md) | χ² interval on σ² |
| [two-sample-tests](concepts/two-sample-tests.md) | Pooled s² formula |
| [regression-slr](concepts/regression-slr.md) | MSE = σ̂² in SLR |
| [regression-mlr](concepts/regression-mlr.md) | MSE in MLR |
| [regression-ht](concepts/regression-ht.md) | MSE feeds F and t tests |
| [regression-ci](concepts/regression-ci.md) | MSE inside CI and PI formulas |
| [control-charts](concepts/control-charts.md) | σ̂ from R̄/d₂ or s̄/c₄ |
| [process-capability](concepts/process-capability.md) | σ̂ feeds Cp and Cpk |
| [crd-one-way-anova](concepts/crd-one-way-anova.md) | MS_Error = σ̂² |
| [rcbd-blocking](concepts/rcbd-blocking.md) | MS_Error = σ̂² |
| [random-effects-model](concepts/random-effects-model.md) | Variance components σ̂²τ = (MS_Trt − MS_E) / n |

---

## [distributions](concepts/distributions.md)

The sampling distribution determines what critical value and p-value formula to use. Every hypothesis test and CI page draws from a specific distribution.

Pages that should link to `distributions`:

| Source page | Reason |
|-------------|--------|
| [confidence-intervals](concepts/confidence-intervals.md) | Z (σ known), t (σ unknown), χ² (variance) |
| [hypothesis-testing-overview](concepts/hypothesis-testing-overview.md) | Which distribution gives the p-value |
| [two-sample-tests](concepts/two-sample-tests.md) | Z, t, F distributions |
| [chi-square](concepts/chi-square.md) | χ² distribution |
| [power-sample-size](concepts/power-sample-size.md) | OC curves based on non-central F and t |
| [ht-one-sample-z-mean](concepts/ht-one-sample-z-mean.md) | Standard normal Z |
| [ht-one-sample-t-mean](concepts/ht-one-sample-t-mean.md) | t distribution, df = n−1 |
| [ht-one-sample-chisq-variance](concepts/ht-one-sample-chisq-variance.md) | χ² distribution |
| [ht-two-sample-f-variances](concepts/ht-two-sample-f-variances.md) | F distribution |

---

## [probability](concepts/probability.md)

Probability rules underlie p-values, conditional logic in test selection, and CI interpretation. Foundational for Units 1–2.

Pages that should link to `probability`:

| Source page | Reason |
|-------------|--------|
| [distributions](concepts/distributions.md) | PMF/PDF are probability functions |
| [hypothesis-testing-overview](concepts/hypothesis-testing-overview.md) | p-value is a conditional probability |
| [confidence-intervals](concepts/confidence-intervals.md) | CI coverage probability interpretation |
| [hw1-examples](examples/hw1-examples.md) | Normal distribution probability problems |

---

## [reading-r-output](r-code/reading-r-output.md)

Every example page involving R output should link here so students know how to translate R terms to teacher phrasing on exams.

Pages that should link to `reading-r-output`:

| Source page | Reason |
|-------------|--------|
| [regression-examples](examples/regression-examples.md) | Reading lm() summary table |
| [anova-table-examples](examples/anova-table-examples.md) | Completing ANOVA from R output |
| [crd-examples](examples/crd-examples.md) | Reading aov() output |
| [factorial-examples](examples/factorial-examples.md) | Interpreting interaction output |
| [2k-factorial-examples](examples/2k-factorial-examples.md) | Reading Daniel plot and lm() output |
| [control-chart-examples](examples/control-chart-examples.md) | Reading qcc output |
| [model-adequacy-examples](examples/model-adequacy-examples.md) | Interpreting diagnostic plot output |

---

## [taxonomy](concepts/taxonomy.md)

The taxonomy is the CPS classification guide. Any page that is new or explains how the wiki is structured should link here.

Pages that should link to `taxonomy`:

| Source page | Reason |
|-------------|--------|
| [knowledge-dimensions](reference/knowledge-dimensions.md) | Taxonomy applies the theoretical framework |
| [data-wrangling-r](r-code/data-wrangling-r.md) | Already linked (tier: script guidance) |

---

## Maintenance Notes

- When a new procedure page is created, check whether it uses any of the 6 constructs above and add it to the relevant table.
- When a new example page is created, add it to the `reading-r-output` table if it includes R output interpretation.
- The symmetry rule covers sibling links — no entries needed here for procedure ↔ procedure or example ↔ concept pairs that are already in each page's `## Related` section.

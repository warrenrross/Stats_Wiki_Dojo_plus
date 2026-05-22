---
tags: [core-concept, section-1-2, section-3]
tier: construct
sources: [L14P, L22P, L31P, L27P, formula-snippets]
---
# Variance Estimation — Universal Reference

## In Plain English

σ² (population variance) is almost never known. Instead we estimate it from data. The estimator changes depending on the situation, but every estimator follows the same logic:

$$\hat{\sigma}^2 = \frac{\text{sum of squared deviations}}{\text{degrees of freedom}}$$

Knowing which estimator applies — and what its df is — is the key to choosing the right test and standard error.

---

## Variance Estimator Master Table

### From Raw Samples

| Context | Estimator | Formula | df |
|---------|----------|---------|-----|
| One sample | $s^2$ (sample variance) | $\dfrac{\sum_{i=1}^n (x_i - \bar{x})^2}{n-1}$ | n−1 |
| Two samples, equal σ assumed | $s_p^2$ (pooled variance) | $\dfrac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}$ | n₁+n₂−2 |
| Two samples, unequal σ (Welch) | Keep $s_1^2, s_2^2$ separate | No pooling | ν (Welch df) |
| Paired | $s_d^2$ (variance of differences) | Same as one-sample on $d_i = x_{1i} - x_{2i}$ | n−1 |

---

### From Regression

| Context | Estimator | Formula | df |
|---------|----------|---------|-----|
| SLR or MLR | $MSE$ (mean squared error) | $\dfrac{SS_E}{n - k - 1} = \dfrac{SS_E}{n-p}$ | n−k−1 |

MSE is the regression equivalent of s². It estimates σ², the variance of the errors εᵢ.

**In R:** `summary(fit)$sigma` gives $\hat{\sigma} = \sqrt{MSE}$ (the "Residual standard error" line). Square it to get MSE.

Or from `anova(fit)`: MSE = `Residuals` row, `Mean Sq` column.

---

### From Control Charts (SPC)

| Chart type | Estimator of σ | Formula | Notes |
|------------|---------------|---------|-------|
| X̄/R chart | $\hat{\sigma}$ | $\bar{R} / d_2$ | d₂ from control chart constants table |
| X̄/S chart | $\hat{\sigma}$ | $\bar{s} / c_4$ | c₄ from control chart constants table |
| p-chart | $\hat{\sigma}_p$ | $\sqrt{\bar{p}(1-\bar{p})/n}$ | for each subgroup |
| c-chart | $\hat{\sigma}_c$ | $\sqrt{\bar{c}}$ | Poisson: variance = mean |
| u-chart | $\hat{\sigma}_u$ | $\sqrt{\bar{u}/n}$ | per-unit defects |

These σ̂ values feed directly into control limit formulas (UCL/LCL = x̄ ± 3σ̂/√n structure).

---

## How Variance Estimation Connects to Everything Else

```
Raw data
    ↓
Estimate σ² (choose estimator for context)
    ↓
Take square root → σ̂ (standard deviation estimate)
    ↓
Divide by √n (or appropriate n-like term) → SE(estimate)
    ↓
Plug into:
    • CI formula:    estimate ± t_{α/2, df} × SE
    • Test stat:     (estimate − null) / SE   ~ t or Z
    • Control limit: centerline ± 3σ̂          (SPC)
```

---

## The Unbiasedness Point (Why n−1, Not n)

Dividing by n−1 instead of n makes s² an **unbiased** estimator of σ²:

$$E[s^2] = \sigma^2$$

If you divided by n, you'd systematically underestimate σ². The "lost" degree of freedom accounts for having estimated x̄ from the same data.

In regression: dividing SS_E by (n−k−1) accounts for estimating k+1 regression coefficients first.

---

## MSE vs s² — What's the Difference?

| Property | $s^2$ | $MSE$ |
|----------|-------|-------|
| What it estimates | σ² from raw data | σ² of regression errors |
| Numerator | $\sum(x_i - \bar{x})^2$ | $\sum(y_i - \hat{y}_i)^2 = SS_E$ |
| Denominator | n − 1 | n − k − 1 |
| Used in | t-tests, CIs on means | Regression SEs, regression CIs/PIs |
| R | `var(x)` | `anova(fit)["Residuals","Mean Sq"]` or `summary(fit)$sigma^2` |

---

## Back-Calculating σ from a CI

If you're given a CI [L, U] and the critical value t*:

$$se(\hat{\theta}) = \frac{(U - L)/2}{t^*}$$

For a regression coefficient CI: this gives you $se(\hat{\beta}_j) = \sqrt{MSE \cdot C_{jj}}$.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Using n in denominator of s² | Always use **n−1** for sample variance |
| Using s² from one group when equal variances not verified | Run F-test first; if p < α, use Welch (don't pool) |
| Forgetting MSE = σ̂² for regression (not σ̂) | `summary(fit)$sigma` is σ̂; square it to get MSE |
| Using R̄/d₂ formula without subgroup size | d₂ depends on subgroup size n — check the constants table |

---

## Related

- [standard-error](standard-error.md) — how variance estimates feed into SE formulas
- [degrees-of-freedom](degrees-of-freedom.md) — denominator df for each estimator
- [two-sample-tests](two-sample-tests.md) — pooled variance derivation
- [regression-ht](regression-ht.md) — how MSE feeds into F and t tests
- [regression-ci](regression-ci.md) — MSE inside CI and PI formulas
- [control-charts](control-charts.md) — σ̂ from R̄/d₂ in control limit formulas
- [process-capability](process-capability.md) — σ̂ feeds into Cp/Cpk
- [crd-one-way-anova](crd-one-way-anova.md) — MS_E in one-way ANOVA is the within-group variance estimate; same construct as s² but pooled across groups

---
tags: [core-concept, unit-1, unit-3]
tier: construct
sources: [L14P, L22P, L31P, L36-37P, formula-snippets]
---
# Standard Error — Universal Reference

## In Plain English

Standard error (SE) is the standard deviation of a sampling distribution — it measures **how uncertain your estimate is**. Every CI and test statistic divides by one. The formula changes depending on what you're estimating, but the structure is always the same:

$$\text{CI}: \quad \hat{\theta} \pm (\text{critical value}) \times SE(\hat{\theta})$$

$$\text{Test stat}: \quad \frac{\hat{\theta} - \theta_0}{SE(\hat{\theta})}$$

Larger SE → wider CI → harder to detect a difference.

---

## SE Master Table

### Means and Differences of Means

| Situation | SE Formula | Notes |
|-----------|-----------|-------|
| One-sample, σ known | $\sigma / \sqrt{n}$ | Use Z distribution |
| One-sample, σ unknown | $s / \sqrt{n}$ | Use t, df = n−1 |
| Two-sample pooled | $s_p\sqrt{\frac{1}{n_1} + \frac{1}{n_2}}$ | Use t, df = n₁+n₂−2; requires σ₁=σ₂ |
| Two-sample Welch | $\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}$ | Use t, df = ν (Welch formula); σ₁≠σ₂ |
| Paired | $s_d / \sqrt{n}$ | Use t, df = n−1; n = # pairs; sd = std dev of differences |

$$s_p = \sqrt{\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}}$$

$$\nu = \frac{\left(\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}\right)^2}{\frac{(s_1^2/n_1)^2}{n_1-1} + \frac{(s_2^2/n_2)^2}{n_2-1}} \quad \text{(round down)}$$

---

### Proportions

| Situation | SE Formula | Notes |
|-----------|-----------|-------|
| HT on one proportion | $\sqrt{\frac{p_0(1-p_0)}{n}}$ | Use p₀ (null value), not p̂ |
| CI on one proportion | $\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$ | Use p̂ (observed value) |

---

### Regression Coefficients

| Situation | SE Formula | Notes |
|-----------|-----------|-------|
| SLR slope β̂₁ | $\sqrt{MSE / S_{xx}}$ | $S_{xx} = \sum(x_i - \bar{x})^2$ |
| SLR intercept β̂₀ | $\sqrt{MSE\left(\frac{1}{n} + \frac{\bar{x}^2}{S_{xx}}\right)}$ | |
| MLR coefficient β̂ⱼ | $\sqrt{MSE \cdot C_{jj}}$ | $C_{jj}$ = j-th diagonal of $(\mathbf{X}'\mathbf{X})^{-1}$ |

R gives `se(β̂ⱼ)` in the `Std. Error` column of `summary(fit)`. You rarely need to compute it by hand.

---

### Regression Intervals (at a specific x₀)

| Interval | SE Formula | R Code |
|----------|-----------|--------|
| CI on mean response (SLR) | $\sqrt{MSE\left[\frac{1}{n} + \frac{(x_0-\bar{x})^2}{S_{xx}}\right]}$ | `predict(..., interval="confidence")` |
| PI on future obs (SLR) | $\sqrt{MSE\left[1 + \frac{1}{n} + \frac{(x_0-\bar{x})^2}{S_{xx}}\right]}$ | `predict(..., interval="prediction")` |
| CI on mean response (MLR) | $\sqrt{MSE \cdot \mathbf{x}_0'(\mathbf{X}'\mathbf{X})^{-1}\mathbf{x}_0}$ | same |
| PI on future obs (MLR) | adds +MSE under square root | same |

**The PI SE always has an extra term — that's the +1 (or +MSE) accounting for individual scatter.**

---

### Variance and Standard Deviation

| Situation | SE Formula | Distribution |
|-----------|-----------|-------------|
| HT on σ² | Use $\chi^2 = (n-1)s^2/\sigma_0^2$ | χ², df = n−1 |
| HT on σ₁²/σ₂² (equal variances?) | Use $F = s_1^2/s_2^2$ | F, df = (n₁−1, n₂−1) |

No "SE" in the classical sense — these use ratio-based test statistics directly.

---

## Why the SE Changes Shape

All SEs follow the same intuition:

1. **Variance of the estimate** (how wobbly is θ̂?) — comes from the sampling distribution
2. **Square root** → converts variance of estimate to standard deviation of estimate = SE
3. **n in denominator** → more data → smaller SE → narrower CI

For regression, MSE plays the role of σ² (it's the variance estimate from residuals), and the rest of the formula accounts for where x₀ is relative to the data centroid.

---

## Related

- [degrees-of-freedom](degrees-of-freedom.md) — which df goes with each SE
- [variance-estimation](variance-estimation.md) — how σ² (and hence MSE) gets estimated
- [confidence-intervals](confidence-intervals.md) — CI formulas using these SEs
- [hypothesis-testing-overview](hypothesis-testing-overview.md) — test statistics using these SEs
- [two-sample-tests](two-sample-tests.md) — pooled and Welch SE details
- [regression-ci](regression-ci.md) — regression-specific interval formulas
- [regression-slr](regression-slr.md) — SLR slope and intercept SEs are worked examples of the universal formula

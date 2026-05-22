---
tags: [concept, section-1-2]
tier: procedure
sources: [L13P, L17P, formula-snippets]
---
# One-Sample χ²-Test on Variance

## In Plain English
Use when you want to test a claim about the population variance σ². The test statistic is formed by scaling the sample variance S² by the hypothesized variance σ₀² — if H₀ is true, this ratio follows a chi-square distribution. Unlike Z and t tests, the χ² distribution is right-skewed, so the critical regions are asymmetric.

## When To Use
- Testing H₀: σ² = σ₀²
- One sample from a normal population
- Want to verify a process has acceptable variability

## Formula(s)

| Symbol | Meaning |
|--------|---------|
| S² | sample variance |
| σ₀² | hypothesized variance (from H₀) |
| n | sample size |
| df | n − 1 |

**Test statistic:**
$$\chi_0^2 = \frac{(n-1)S^2}{\sigma_0^2} \sim \chi^2_{n-1}$$

**Hypothesis table:**

| H₁ | Reject H₀ if |
|----|--------------|
| σ² ≠ σ₀² | χ₀² > χ²_{α/2, n−1} **or** χ₀² < χ²_{1−α/2, n−1} |
| σ² > σ₀² | χ₀² > χ²_{α, n−1} |
| σ² < σ₀² | χ₀² < χ²_{1−α, n−1} |

**Confidence interval on σ²:**
$$\frac{(n-1)s^2}{\chi^2_{\alpha/2,\,n-1}} \leq \sigma^2 \leq \frac{(n-1)s^2}{\chi^2_{1-\alpha/2,\,n-1}}$$

Note: the lower bound uses the **larger** χ² critical value (right tail), upper bound uses the **smaller** (left tail).

## Key Assumptions
- Population must be **normal** (χ² test on variance is not robust to non-normality)
- Observations are independent

## Common Mistakes
- Swapping χ²_{α/2} and χ²_{1−α/2} when computing CI bounds — remember larger χ² → smaller bound
- Using this test when the population is clearly non-normal (use a different approach)
- Confusing this χ² test (on σ²) with the GoF χ² test (on distribution fit)

## Related
- [ht-goodness-of-fit](ht-goodness-of-fit.md) — different χ² test, for distributional fit
- [ht-independence](ht-independence.md) — different χ² test, for contingency tables
- [ht-two-sample-f-variances](ht-two-sample-f-variances.md) — comparing two variances (use F-test)
- [confidence-intervals](confidence-intervals.md) — CI on σ²
- [ht-tests-overview](../reference/ht-tests-overview.md) — full test selection table

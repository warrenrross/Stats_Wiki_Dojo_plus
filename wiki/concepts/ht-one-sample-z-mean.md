---
tags: [concept, section-1-2]
tier: procedure
sources: [L15P, formula-snippets]
---
# One-Sample Z-Test on Mean (σ² Known)

## In Plain English
Use when you know the population variance and want to test a claim about the population mean. Because σ is known, the test statistic follows the standard normal distribution exactly. Also valid when n ≥ 40 and σ is unknown, because the CLT makes the sampling distribution approximately normal and S ≈ σ.

## When To Use
- Testing H₀: μ = μ₀
- σ² is **known** (given in the problem) **OR** n ≥ 40 (CLT applies — use S in place of σ)
- Population is normal (or n large enough for CLT)

## Formula(s)

| Symbol | Meaning |
|--------|---------|
| X̄ | sample mean |
| μ₀ | hypothesized mean (from H₀) |
| σ | known population standard deviation |
| n | sample size |
| δ | true departure from μ₀: δ = μ − μ₀ |

**Test statistic:**
$$Z_0 = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}} \sim N(0,1)$$

**Hypothesis table:**

| H₁ | p-value | Reject H₀ if |
|----|---------|--------------|
| μ ≠ μ₀ | 2[1 − Φ(\|Z₀\|)] | \|Z₀\| > z_{α/2} |
| μ > μ₀ | 1 − Φ(Z₀) | Z₀ > z_α |
| μ < μ₀ | Φ(Z₀) | Z₀ < −z_α |

**Confidence interval on μ:**
$$\bar{x} - z_{\alpha/2}\frac{\sigma}{\sqrt{n}} \leq \mu \leq \bar{x} + z_{\alpha/2}\frac{\sigma}{\sqrt{n}}$$

**Type II error (two-sided test):**
$$\beta = \Phi\!\left(z_{\alpha/2} - \frac{\delta\sqrt{n}}{\sigma}\right) - \Phi\!\left(-z_{\alpha/2} - \frac{\delta\sqrt{n}}{\sigma}\right)$$

**Sample size (two-sided):** $n \approx \dfrac{(z_{\alpha/2}+z_\beta)^2\sigma^2}{\delta^2}$

**Sample size (one-sided):** $n \approx \dfrac{(z_\alpha+z_\beta)^2\sigma^2}{\delta^2}$

**Common z critical values:**

| CI | α | Tails | z |
|----|---|-------|---|
| 0.99 | 0.01 | two | ±2.576 |
| 0.99 | 0.01 | one | ±2.326 |
| 0.95 | 0.05 | two | ±1.960 |
| 0.95 | 0.05 | one | ±1.645 |
| 0.90 | 0.10 | two | ±1.645 |
| 0.90 | 0.10 | one | ±1.282 |

## Key Assumptions
- Observations are independent
- Population is normal OR n ≥ 40 (CLT)
- σ² is truly known (not estimated from this sample)

## Common Mistakes
- Using Z when σ is unknown and n < 40 — use [ht-one-sample-t-mean](ht-one-sample-t-mean.md) instead
- Forgetting to halve α for two-sided tests when looking up z critical value
- Confusing "n ≥ 40" as a hard rule — it is a guideline; normality matters for small n

## Related
- [ht-one-sample-t-mean](ht-one-sample-t-mean.md) — same test, σ unknown → use t
- [confidence-intervals](confidence-intervals.md) — CI on μ with known σ
- [ht-tests-overview](../reference/ht-tests-overview.md) — full test selection table

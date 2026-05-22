---
tags: [concept, section-1-2]
tier: procedure
sources: [L18P, formula-snippets]
---
# One-Sample Z-Test on Proportion

## In Plain English
Use when you want to test a claim about a population proportion p (e.g., defect rate, pass rate). The test statistic uses the hypothesized proportion p₀ in the denominator — NOT the observed P̂ — because under H₀, we assume p = p₀ is true. The statistic follows an approximate standard normal distribution via the CLT.

## When To Use
- Testing H₀: p = p₀
- Data is counts of successes/failures from a binomial process
- np₀ ≥ 5 and n(1−p₀) ≥ 5 (so normal approximation is valid)

## Formula(s)

| Symbol | Meaning |
|--------|---------|
| X | number of successes in n trials |
| P̂ | sample proportion = X/n |
| p₀ | hypothesized proportion (from H₀) |
| n | sample size |

**Test statistic (count form):**
$$Z_0 = \frac{X - np_0}{\sqrt{np_0(1-p_0)}}$$

**Test statistic (proportion form — equivalent):**
$$Z_0 = \frac{\hat{P} - p_0}{\sqrt{p_0(1-p_0)/n}}$$

**Hypothesis table:**

| H₁ | p-value | Reject H₀ if |
|----|---------|--------------|
| p ≠ p₀ | 2[1 − Φ(\|Z₀\|)] | \|Z₀\| > z_{α/2} |
| p > p₀ | 1 − Φ(Z₀) | Z₀ > z_α |
| p < p₀ | Φ(Z₀) | Z₀ < −z_α |

**Confidence interval on p:**
$$\hat{p} - z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}} \leq p \leq \hat{p} + z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

Note: CI uses P̂ in the SE (not p₀), because we're estimating p, not testing it.

**Sample size (two-sided):**
$$n = \left[\frac{z_{\alpha/2}\sqrt{p_0(1-p_0)} + z_\beta\sqrt{p(1-p)}}{p - p_0}\right]^2$$

**Sample size (one-sided):**
$$n = \left[\frac{z_\alpha\sqrt{p_0(1-p_0)} + z_\beta\sqrt{p(1-p)}}{p - p_0}\right]^2$$

## Key Assumptions
- Observations are independent Bernoulli trials
- np₀ ≥ 5 and n(1−p₀) ≥ 5 for the normal approximation to hold

## Common Mistakes
- Using P̂ in the test statistic denominator — must use p₀ (the null value)
- Using p₀ in the CI denominator — must use P̂ (the estimate)
- Forgetting to check the np₀ ≥ 5 condition before applying the normal approximation

## Related
- [proportions](proportions.md) — broader coverage including two-proportion tests
- [hypothesis-tests-r](../r-code/hypothesis-tests-r.md) — `prop.test(x, n, p = p0, alternative = "...")`
- [ht-tests-overview](../reference/ht-tests-overview.md) — full test selection table

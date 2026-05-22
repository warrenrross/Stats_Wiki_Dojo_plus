---
tags: [concept, unit-2]
tier: procedure
sources: [L15P, L16P, formula-snippets]
---
# One-Sample T-Test on Mean (σ² Unknown)

## In Plain English
Use when σ² is unknown — the most common real-world case. You estimate σ with S, which introduces extra uncertainty, so the test statistic follows a t-distribution with n−1 degrees of freedom instead of standard normal. The t-distribution has heavier tails than Z, making it harder to reject H₀ (as it should be when you're estimating variance).

## When To Use
- Testing H₀: μ = μ₀
- σ² is **unknown** (must be estimated from the sample)
- n < 40 (if n ≥ 40, use [ht-one-sample-z-mean](ht-one-sample-z-mean.md) with S substituted for σ)
- Population is approximately normal

## Formula(s)

| Symbol | Meaning |
|--------|---------|
| X̄ | sample mean |
| μ₀ | hypothesized mean |
| S | sample standard deviation |
| n | sample size |
| df | degrees of freedom = n − 1 |

**Test statistic:**
$$T_0 = \frac{\bar{X} - \mu_0}{S / \sqrt{n}} \sim t_{n-1}$$

**Hypothesis table:**

| H₁ | p-value | Reject H₀ if |
|----|---------|--------------|
| μ ≠ μ₀ | prob in both tails of \|T₀\| | \|T₀\| > t_{α/2, n−1} |
| μ > μ₀ | prob above T₀ | T₀ > t_{α, n−1} |
| μ < μ₀ | prob below T₀ | T₀ < −t_{α, n−1} |

**In R:** `2 * pt(-abs(T0), df = n-1)` for two-sided p-value

**Confidence interval on μ:**
$$\bar{x} - t_{\alpha/2,\,n-1}\frac{S}{\sqrt{n}} \leq \mu \leq \bar{x} + t_{\alpha/2,\,n-1}\frac{S}{\sqrt{n}}$$

## Key Assumptions
- Observations are independent
- Population is approximately normal (critical for small n; robust for larger n)
- σ² unknown (estimated by S²)

## Common Mistakes
- Using t when σ is actually known — use [ht-one-sample-z-mean](ht-one-sample-z-mean.md)
- Looking up t with wrong df: df = n − 1, not n
- Forgetting t-tables are one-tailed by default — for two-sided test use t_{α/2, n−1}

## Related
- [ht-one-sample-z-mean](ht-one-sample-z-mean.md) — use instead when σ known or n ≥ 40
- [confidence-intervals](confidence-intervals.md) — CI on μ with unknown σ
- [hypothesis-tests-r](../r-code/hypothesis-tests-r.md) — `t.test(x, mu = mu0, alternative = "...")`
- [ht-tests-overview](../reference/ht-tests-overview.md) — full test selection table

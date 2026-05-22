---
tags: [concept, section-1-2]
tier: procedure
sources: [L21P, formula-snippets]
---
# Two-Sample Z-Test on Difference of Means (Both σ² Known)

## In Plain English
Use when you have two independent samples and want to test whether their population means differ, and both population variances are known. Because both σ² are known, the sampling distribution of (X̄₁ − X̄₂) is exactly normal. In practice this is rare — if σ² are unknown, use [[ht-two-sample-t-means]].

## When To Use
- Testing H₀: μ₁ − μ₂ = Δ₀ (usually Δ₀ = 0, i.e., equal means)
- Two **independent** samples
- Both σ₁² and σ₂² are **known**
- Populations are normal OR both n₁, n₂ large (CLT)

## Formula(s)

| Symbol | Meaning |
|--------|---------|
| X̄₁, X̄₂ | sample means |
| σ₁², σ₂² | known population variances |
| n₁, n₂ | sample sizes |
| Δ₀ | hypothesized difference (H₀ value; usually 0) |

**Test statistic:**
$$Z_0 = \frac{\bar{X}_1 - \bar{X}_2 - \Delta_0}{\sqrt{\dfrac{\sigma_1^2}{n_1} + \dfrac{\sigma_2^2}{n_2}}} \sim N(0,1)$$

**Hypothesis table:**

| H₁ | p-value | Reject H₀ if |
|----|---------|--------------|
| μ₁ − μ₂ ≠ Δ₀ | 2[1 − Φ(\|Z₀\|)] | \|Z₀\| > z_{α/2} |
| μ₁ − μ₂ > Δ₀ | 1 − Φ(Z₀) | Z₀ > z_α |
| μ₁ − μ₂ < Δ₀ | Φ(Z₀) | Z₀ < −z_α |

**Confidence interval on μ₁ − μ₂:**
$$(\bar{x}_1 - \bar{x}_2) - z_{\alpha/2}\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}} \leq \mu_1-\mu_2 \leq (\bar{x}_1 - \bar{x}_2) + z_{\alpha/2}\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}$$

**Type II error (two-sided, Δ = true difference):**
$$\beta = \Phi\!\left(z_{\alpha/2} - \frac{\Delta - \Delta_0}{\sqrt{\sigma_1^2/n_1 + \sigma_2^2/n_2}}\right) - \Phi\!\left(-z_{\alpha/2} - \frac{\Delta - \Delta_0}{\sqrt{\sigma_1^2/n_1 + \sigma_2^2/n_2}}\right)$$

## Key Assumptions
- Samples are **independent** (not paired — use [[ht-paired-t]] if paired)
- Both populations are normal OR sample sizes are large
- σ₁² and σ₂² are truly known

## Common Mistakes
- Using Z when σ² are unknown — use [[ht-two-sample-t-means]] (pooled or Welch's)
- Treating paired data as independent — use [[ht-paired-t]] instead (more powerful)
- Forgetting Δ₀ in the numerator when H₀ is not μ₁ = μ₂

## Related
- [[ht-two-sample-t-means]] — use when σ² are unknown (most common)
- [[ht-paired-t]] — use when observations are paired
- [[two-sample-tests]] — broader coverage of all two-sample procedures
- [[ht-tests-overview]] — full test selection table

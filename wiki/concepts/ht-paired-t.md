---
tags: [concept, section-1-2]
tier: procedure
sources: [L24P, formula-snippets]
---
# Paired T-Test

## In Plain English
Use when observations come in matched pairs — the same subject measured twice (before/after), two methods applied to the same unit, or subjects matched by a nuisance variable. By working with differences Dᵢ = X₁ᵢ − X₂ᵢ, you eliminate between-subject variability, making the test more powerful than an independent two-sample T-test.

## When To Use
- Two measurements on the **same** or **matched** subjects
- H₀: μ_D = Δ₀ (usually Δ₀ = 0, i.e., no difference)
- Differences D are approximately normally distributed

## Formula(s)

| Symbol | Meaning |
|--------|---------|
| Dᵢ | difference for pair i: X₁ᵢ − X₂ᵢ |
| D̄ | sample mean of differences |
| Sᴅ | sample standard deviation of differences |
| n | number of pairs |
| Δ₀ | hypothesized mean difference (usually 0) |

**Step 1 — Compute differences:** Dᵢ = X₁ᵢ − X₂ᵢ for each pair

**Step 2 — Compute D̄ and Sᴅ** from the n differences

**Test statistic:**
$$T_0 = \frac{\bar{D} - \Delta_0}{S_D / \sqrt{n}} \sim t_{n-1}$$

**df:** n − 1 (number of pairs minus 1)

**Hypothesis table:**

| H₁ | p-value | Reject H₀ if |
|----|---------|--------------|
| μ_D ≠ Δ₀ | prob in both tails | \|T₀\| > t_{α/2, n−1} |
| μ_D > Δ₀ | prob above T₀ | T₀ > t_{α, n−1} |
| μ_D < Δ₀ | prob below T₀ | T₀ < −t_{α, n−1} |

**Confidence interval on μ_D:**
$$\bar{d} - t_{\alpha/2,\,n-1}\frac{S_D}{\sqrt{n}} \leq \mu_D \leq \bar{d} + t_{\alpha/2,\,n-1}\frac{S_D}{\sqrt{n}}$$

## Key Assumptions
- Pairs are independent of each other
- Differences Dᵢ are approximately normally distributed (robust for large n)
- The pairing is meaningful — each X₁ᵢ is genuinely linked to its X₂ᵢ

## Common Mistakes
- Using independent two-sample T on paired data — loses power, inflates error variance
- Computing the standard error using individual observations instead of differences
- Using n₁ + n₂ − 2 degrees of freedom — df is n − 1 (n = number of pairs)
- Forgetting to define D direction consistently (X₁ − X₂ vs X₂ − X₁ changes the sign of T₀)

## Related
- [ht-two-sample-t-means](ht-two-sample-t-means.md) — use when observations are independent
- [hypothesis-tests-r](../r-code/hypothesis-tests-r.md) — `t.test(x, y, paired = TRUE)`
- [ht-tests-overview](../reference/ht-tests-overview.md) — full test selection table

---
tags: [concept, section-1-2]
tier: procedure
sources: [L22P, L23P, formula-snippets]
---
# Two-Sample T-Test on Difference of Means (σ² Unknown)

## In Plain English
The standard test for comparing two independent group means when variances are unknown. Two cases: **Case 1 (Pooled)** assumes σ₁² = σ₂² and estimates the common variance; **Case 2 (Welch's)** makes no assumption about equal variances. Always run an F-test ([ht-two-sample-f-variances](ht-two-sample-f-variances.md)) first — or use subject-matter knowledge — to decide which case applies.

## When To Use
- Testing H₀: μ₁ − μ₂ = Δ₀
- Two **independent** samples
- σ₁² and σ₂² are **unknown**
- Populations are approximately normal

## Case 1 — Equal Variances (Pooled T-Test)

**Use when:** F-test or prior knowledge supports σ₁² = σ₂²

**Pooled variance estimate:**
$$S_p^2 = \frac{(n_1-1)S_1^2 + (n_2-1)S_2^2}{n_1 + n_2 - 2}$$

**Test statistic:**
$$T_0 = \frac{\bar{X}_1 - \bar{X}_2 - \Delta_0}{S_p\sqrt{\dfrac{1}{n_1} + \dfrac{1}{n_2}}} \sim t_{n_1+n_2-2}$$

**df:** n₁ + n₂ − 2

**Confidence interval:**
$$(\bar{x}_1-\bar{x}_2) \pm t_{\alpha/2,\,n_1+n_2-2} \cdot S_p\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}$$

## Case 2 — Unequal Variances (Welch's T-Test)

**Use when:** F-test or prior knowledge suggests σ₁² ≠ σ₂²

**Test statistic:**
$$T_0 = \frac{\bar{X}_1 - \bar{X}_2 - \Delta_0}{\sqrt{\dfrac{S_1^2}{n_1} + \dfrac{S_2^2}{n_2}}}$$

**Welch–Satterthwaite degrees of freedom (round down to integer):**
$$\nu = \frac{\left(\dfrac{S_1^2}{n_1} + \dfrac{S_2^2}{n_2}\right)^2}{\dfrac{(S_1^2/n_1)^2}{n_1-1} + \dfrac{(S_2^2/n_2)^2}{n_2-1}}$$

**Confidence interval:**
$$(\bar{x}_1-\bar{x}_2) \pm t_{\alpha/2,\,\nu}\sqrt{\frac{S_1^2}{n_1}+\frac{S_2^2}{n_2}}$$

## Hypothesis Table (both cases)

| H₁ | p-value | Reject H₀ if |
|----|---------|--------------|
| μ₁ − μ₂ ≠ Δ₀ | prob in both tails | \|T₀\| > t_{α/2, df} |
| μ₁ − μ₂ > Δ₀ | prob above T₀ | T₀ > t_{α, df} |
| μ₁ − μ₂ < Δ₀ | prob below T₀ | T₀ < −t_{α, df} |

## Key Assumptions
- Samples are **independent** (use [ht-paired-t](ht-paired-t.md) if paired)
- Both populations approximately normal
- Case 1 additionally requires σ₁² = σ₂² (test with [ht-two-sample-f-variances](ht-two-sample-f-variances.md))

## Common Mistakes
- Using pooled T when variances are clearly unequal — inflates Type I error
- Forgetting to use F-test to decide which case applies
- Treating paired data as independent — paired T is more powerful for paired designs
- Rounding Welch ν up instead of down

## Related
- [ht-two-sample-f-variances](ht-two-sample-f-variances.md) — run this first to decide Case 1 vs Case 2
- [ht-paired-t](ht-paired-t.md) — use for paired/matched data
- [ht-two-sample-z-means](ht-two-sample-z-means.md) — use when both σ² are known
- [two-sample-tests](two-sample-tests.md) — broader coverage
- [hypothesis-tests-r](../r-code/hypothesis-tests-r.md) — `t.test(x, y, var.equal = TRUE/FALSE)`
- [ht-tests-overview](../reference/ht-tests-overview.md) — full test selection table

---
tags: [concept, unit-2]
tier: procedure
sources: [L21P, L22&23P, L24P, L25P, formula-snippets]
---
# Two-Sample Tests

## In Plain English
Two-sample tests compare parameters from two populations. The key decision: are the samples **paired** (matched observations, like before/after) or **independent** (separate groups)?

---

## Case 1: Two Means, Variances KNOWN — 2-Sample Z

**When:** σ₁ and σ₂ are known, samples are independent.

**Variance of difference:**
$$V(\bar{X}_1 - \bar{X}_2) = \frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}$$

**Test statistic:**
$$Z_0 = \frac{\bar{X}_1 - \bar{X}_2 - \Delta_0}{\sqrt{\dfrac{\sigma_1^2}{n_1} + \dfrac{\sigma_2^2}{n_2}}}$$

**CI on μ₁ − μ₂:**
$$\bar{X}_1 - \bar{X}_2 - z_{\alpha/2}\sqrt{\frac{\sigma_1^2}{n_1}+\frac{\sigma_2^2}{n_2}} \leq \mu_1-\mu_2 \leq \bar{X}_1 - \bar{X}_2 + z_{\alpha/2}\sqrt{\frac{\sigma_1^2}{n_1}+\frac{\sigma_2^2}{n_2}}$$

**Sample size** (two-sided, equal n):
$$n = \left(\frac{z_{\alpha/2}}{E}\right)^2(\sigma_1^2 + \sigma_2^2)$$

---

## Case 2: Two Means, Equal Unknown Variances — Pooled t-Test

**When:** σ₁² = σ₂² (equal variances assumed), unknown, samples independent.

**Pooled variance estimator:**
$$S_p^2 = \frac{(n_1-1)S_1^2 + (n_2-1)S_2^2}{n_1 + n_2 - 2}$$

**Test statistic:**
$$T_0 = \frac{\bar{X}_1 - \bar{X}_2 - \Delta_0}{S_p\sqrt{\dfrac{1}{n_1} + \dfrac{1}{n_2}}}, \quad \text{df} = n_1 + n_2 - 2$$

**CI on μ₁ − μ₂:**
$$\bar{X}_1 - \bar{X}_2 \pm t_{\alpha/2,\,n_1+n_2-2}\cdot S_p\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}$$

---

## Case 3: Two Means, Unequal Unknown Variances — Welch t-Test

**When:** σ₁² ≠ σ₂² (unequal variances), samples independent.

**Test statistic:**
$$T_0 = \frac{\bar{X}_1 - \bar{X}_2 - \Delta_0}{\sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}}, \quad \text{df} = \nu$$

**Welch degrees of freedom:**
$$\nu = \frac{\left(\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}\right)^2}{\dfrac{(s_1^2/n_1)^2}{n_1-1} + \dfrac{(s_2^2/n_2)^2}{n_2-1}}$$

**CI on μ₁ − μ₂:**
$$\bar{X}_1 - \bar{X}_2 \pm t_{\alpha/2,\,\nu}\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}$$

---

## Case 4: Paired t-Test

**When:** Observations are matched pairs (before/after, same subject, two methods on same unit).

**Setup:** Compute differences dᵢ = x₁ᵢ − x₂ᵢ for each pair, then treat as one-sample t-test on d̄.

**Test statistic:**
$$T_0 = \frac{\bar{D}}{S_D/\sqrt{n}}, \quad \text{df} = n-1$$

**CI on μ_D = μ₁ − μ₂:**
$$\bar{d} \pm t_{\alpha/2,\,n-1}\cdot \frac{s_D}{\sqrt{n}}$$

**Reject H₀: μ_D = Δ₀ if:**

| H₁ | Reject if |
|----|-----------|
| μ_D ≠ Δ₀ | \|t₀\| > t_{α/2,n−1} |
| μ_D > Δ₀ | t₀ > t_{α,n−1} |
| μ_D < Δ₀ | t₀ < −t_{α,n−1} |

---

## Case 5: Two Variances — F-Test

**When:** Testing whether σ₁² = σ₂² (often run before deciding pooled vs Welch t-test).

**Test statistic:**
$$F_0 = \frac{S_1^2}{S_2^2}, \quad \text{df: } n_1-1 \text{ (num)}, \; n_2-1 \text{ (den)}$$

**Reject H₀: σ₁² = σ₂² if:**

| H₁ | Reject if |
|----|-----------|
| σ₁² ≠ σ₂² | f₀ > f_{α/2,n₁−1,n₂−1} or f₀ < f_{1−α/2,n₁−1,n₂−1} |
| σ₁² > σ₂² | f₀ > f_{α,n₁−1,n₂−1} |
| σ₁² < σ₂² | f₀ < f_{1−α,n₁−1,n₂−1} |

**Lower tail shortcut:** $f_{1-\alpha,u,v} = \dfrac{1}{f_{\alpha,v,u}}$

**CI on σ₁²/σ₂²:**
$$\frac{s_1^2}{s_2^2} f_{1-\alpha/2,n_2-1,n_1-1} \leq \frac{\sigma_1^2}{\sigma_2^2} \leq \frac{s_1^2}{s_2^2} f_{\alpha/2,n_2-1,n_1-1}$$

---

## Pooled vs Welch: Which to Use?
- If problem says "assume equal variances" → Pooled
- If problem says "do not assume equal variances" → Welch
- If unsure: run F-test first; if fail to reject H₀: σ₁²=σ₂² → use Pooled

## Key Assumptions
- **Independent samples** (Cases 1–3, 5): samples drawn independently from separate populations
- **Paired** (Case 4): natural pairing, measure same experimental unit twice
- **Normality** of each population (or n large for CLT)

## Common Mistakes
- Using pooled t when variances are clearly unequal
- Forgetting to compute dᵢ for paired test (instead treating as independent)
- Swapping n₁−1 and n₂−1 in Welch df formula numerator/denominator

## Related
- [which-test](which-test.md)
- [hypothesis-testing-overview](hypothesis-testing-overview.md)
- [confidence-intervals](confidence-intervals.md)
- [crd-one-way-anova](crd-one-way-anova.md) — one-way ANOVA is the generalization of the two-sample t to k ≥ 3 groups
- [power-sample-size](power-sample-size.md) — sample size formula for detecting a two-sample mean difference

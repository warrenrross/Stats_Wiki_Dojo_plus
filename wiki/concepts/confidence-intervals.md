---
tags: [concept, section-1-2]
tier: procedure
sources: [L11P, L12P, L13P, formula-snippets]
---
# Confidence Intervals

## In Plain English
A confidence interval gives a range of plausible values for an unknown population parameter. "95% confident" means: if we repeated this process many times, 95% of the intervals we build would contain the true parameter. **It does NOT mean there is a 95% chance μ is in this particular interval.**

## Teacher's Phrasing
> "We are [100(1−α)]% confident that [parameter in context] is between [lower] and [upper]."

## General Structure
$$\text{Estimate} \pm \text{Score} \times \text{Standard Error}$$

---

## CI on Mean μ

### Case 1: Variance Known (or n ≥ 40, use CLT)  →  Z interval

$$\bar{x} - z_{\alpha/2} \frac{\sigma}{\sqrt{n}} \leq \mu \leq \bar{x} + z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$$

**One-sided bounds:**
- Upper: $\mu \leq \bar{x} + z_\alpha \frac{\sigma}{\sqrt{n}}$
- Lower: $\bar{x} - z_\alpha \frac{\sigma}{\sqrt{n}} \leq \mu$

**Sample size** to achieve margin of error E:
$$n = \left(\frac{z_{\alpha/2}\,\sigma}{E}\right)^2$$

### Case 2: Variance Unknown, Normal Population  →  t interval

$$\bar{x} - t_{\alpha/2,\,n-1} \frac{s}{\sqrt{n}} \leq \mu \leq \bar{x} + t_{\alpha/2,\,n-1} \frac{s}{\sqrt{n}}$$

- Use **t-table** with df = n − 1
- As n → ∞, t → z

---

## CI on Variance σ²  →  χ² interval

$$\frac{(n-1)s^2}{\chi^2_{\alpha/2,\,n-1}} \leq \sigma^2 \leq \frac{(n-1)s^2}{\chi^2_{1-\alpha/2,\,n-1}}$$

**CI on σ:** take square root of both bounds.

**One-sided bounds on σ²:**
- Lower: $\sigma^2 \geq \frac{(n-1)s^2}{\chi^2_{\alpha,n-1}}$
- Upper: $\sigma^2 \leq \frac{(n-1)s^2}{\chi^2_{1-\alpha,n-1}}$

---

## Common Z Critical Values

| Confidence Level | α | z_{α/2} (two-sided) | z_α (one-sided) |
|-----------------|---|---------------------|-----------------|
| 99% | 0.01 | 2.576 | 2.326 |
| 98% | 0.02 | 2.326 | 2.054 |
| 95% | 0.05 | 1.960 | 1.645 |
| 90% | 0.10 | 1.645 | 1.282 |

---

## Z vs. t Decision
- σ **known** → Z
- σ **unknown**, normal population → t (df = n−1)
- σ **unknown**, n ≥ 40 → Z (CLT approximation acceptable)

## Key Assumptions
- Random sample
- Normal population (or n large for CLT)
- Independence of observations

## Common Mistakes
- Using Z when σ is unknown and n is small
- Forgetting to take square root for CI on σ (vs σ²)
- Misidentifying α/2 vs α for one-sided intervals

## Related
- [distributions](distributions.md)
- [hypothesis-testing-overview](hypothesis-testing-overview.md)
- [which-test](which-test.md)
- [two-sample-tests](two-sample-tests.md)
- [regression-ci](regression-ci.md) — CI on βⱼ uses the same Estimate ± Score × SE structure

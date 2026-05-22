---
tags: [concept, section-1-2]
tier: procedure
sources: [L18P, formula-snippets]
---
# Inference on Proportions

## In Plain English
When your outcome is binary (success/failure), the parameter of interest is the population proportion p. The sample proportion p̂ = X/n follows an approximately normal distribution for large n.

**Normality condition (check both):** np₀ ≥ 5 and n(1−p₀) ≥ 5

---

## Hypothesis Test on a Proportion

**H₀:** p = p₀

**Test statistic (equivalent form):**
$$Z_0 = \frac{\hat{P} - p_0}{\sqrt{p_0(1-p_0)/n}}$$

or equivalently using counts:
$$Z_0 = \frac{X - np_0}{\sqrt{np_0(1-p_0)}}$$

| H₁ | P-value | Reject H₀ if |
|----|---------|--------------|
| p ≠ p₀ | 2[1−Φ(\|z₀\|)] | \|z₀\| > z_{α/2} |
| p > p₀ | 1−Φ(z₀) | z₀ > z_α |
| p < p₀ | Φ(z₀) | z₀ < −z_α |

---

## Confidence Interval on p

$$\hat{p} - z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}} \leq p \leq \hat{p} + z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

Note: use p̂ in the SE (not p₀), unlike the test statistic.

---

## Sample Size for Proportion

**Two-sided:**
$$n = \left[\frac{z_{\alpha/2}\sqrt{p_0(1-p_0)} + z_\beta\sqrt{p(1-p)}}{p - p_0}\right]^2$$

**One-sided:**
$$n = \left[\frac{z_\alpha\sqrt{p_0(1-p_0)} + z_\beta\sqrt{p(1-p)}}{p - p_0}\right]^2$$

Where p is the true (alternative) proportion you want to detect.

---

## Teacher's Conclusion Phrasing

**Example from L18 (process fraction defective):**
> "Because z₀ = −1.95, the P-value is Φ(−1.95) = 0.0256. Since p-value < 0.05, we reject H₀ and conclude that the process fraction defective p is less than 0.05. The process is capable."

---

## Key Assumptions
- Binary outcome (success/failure)
- Random sample
- np₀ ≥ 5 and n(1−p₀) ≥ 5 for normal approximation
- Independence

## Common Mistakes
- Using p̂ in the test statistic SE (should use p₀)
- Using p₀ in the CI SE (should use p̂)
- Forgetting to check normality condition

## Related
- [[hypothesis-testing-overview]]
- [[which-test]]
- [[chi-square]]

---
tags: [concept, unit-2]
tier: procedure
sources: [L14P, L15P, L16P, formula-snippets]
---
# Hypothesis Testing Overview

## In Plain English
Hypothesis testing is a formal decision procedure: you assume nothing is happening (H₀), then ask "how unlikely is my data if H₀ were true?" If very unlikely (p-value < α), you reject H₀. You never "prove" H₀ is true — you only fail to find evidence against it.

---

## The 7-Step Procedure (Teacher's Framework)

1. **Parameter of interest** — identify what parameter (μ, σ², p) the problem is about
2. **Null hypothesis H₀** — state the "no difference / no effect" hypothesis
3. **Alternative hypothesis H₁** — state the research claim (two-sided ≠, upper >, lower <)
4. **Test statistic** — choose and compute the appropriate formula
5. **Reject H₀ if** — state the rejection criterion (critical value or p-value < α)
6. **Computations** — plug in numbers, compute test statistic and p-value
7. **Draw conclusions** — state in plain language whether H₀ is rejected, in context

---

## Error Types

| | H₀ True | H₀ False |
|---|---------|---------|
| **Fail to reject H₀** | Correct | Type II error (β) |
| **Reject H₀** | Type I error (α) | Correct (Power = 1−β) |

$$\alpha = P(\text{reject } H_0 \mid H_0 \text{ true})$$
$$\beta = P(\text{fail to reject } H_0 \mid H_0 \text{ false})$$

**Power** = 1 − β = P(correctly rejecting a false H₀)

---

## Hypotheses Setup

| Test Direction | H₀ | H₁ |
|---------------|----|----|
| Two-sided | μ = μ₀ | μ ≠ μ₀ |
| Upper-tailed | μ = μ₀ | μ > μ₀ |
| Lower-tailed | μ = μ₀ | μ < μ₀ |

---

## Z-Test on Mean (σ Known or n ≥ 40)

$$Z_0 = \frac{\bar{X} - \mu_0}{\sigma/\sqrt{n}}$$

| H₁ | P-value | Reject H₀ if |
|----|---------|--------------|
| μ ≠ μ₀ | 2[1 − Φ(\|z₀\|)] | \|z₀\| > z_{α/2} |
| μ > μ₀ | 1 − Φ(z₀) | z₀ > z_α |
| μ < μ₀ | Φ(z₀) | z₀ < −z_α |

---

## t-Test on Mean (σ Unknown)

$$T_0 = \frac{\bar{X} - \mu_0}{S/\sqrt{n}}, \quad \text{df} = n-1$$

Same rejection logic as Z-test but use t-table with df = n−1.

---

## P-value Interpretation
- p-value = probability of getting a test statistic this extreme **or more**, assuming H₀ is true
- **p-value < α** → Reject H₀ → "sufficient evidence"
- **p-value > α** → Fail to reject H₀ → "insufficient evidence"

---

## Type II Error β (Two-Sided Z-Test)

$$\delta = \mu - \mu_0 \quad \text{(true difference from null)}$$

$$\beta = \Phi\!\left(z_{\alpha/2} - \frac{\delta\sqrt{n}}{\sigma}\right) - \Phi\!\left(-z_{\alpha/2} - \frac{\delta\sqrt{n}}{\sigma}\right)$$

---

## Sample Size Formulas

**Two-sided test on mean (σ known):**
$$n \approx \frac{(z_{\alpha/2} + z_\beta)^2 \sigma^2}{\delta^2}$$

**One-sided test on mean (σ known):**
$$n \approx \frac{(z_\alpha + z_\beta)^2 \sigma^2}{\delta^2}$$

---

## Teacher's Conclusion Phrasing

**Reject H₀:**
> "Because p-value = [value] < α = [value], we reject H₀. There is sufficient evidence to conclude that [H₁ in context] at α = [value]."

**Fail to reject H₀:**
> "Because p-value = [value] > α = [value], we fail to reject H₀. There is insufficient evidence to conclude that [H₁ in context] at α = [value]."

---

## Key Assumptions
- Random sample from normal population (or n ≥ 40 for Z-test via CLT)
- Independence of observations
- For σ known: population σ is truly known (not estimated)

## Related
- [which-test](which-test.md)
- [confidence-intervals](confidence-intervals.md)
- [two-sample-tests](two-sample-tests.md)
- [chi-square](chi-square.md)
- [regression-ht](regression-ht.md) — regression t and F tests follow the same 7-step structure
- [crd-one-way-anova](crd-one-way-anova.md) — the 7-step procedure applies directly to the ANOVA F-test
- [power-sample-size](power-sample-size.md) — full treatment of β, power, and sample size for t and F tests

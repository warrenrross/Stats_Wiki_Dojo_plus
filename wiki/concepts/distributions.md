---
tags: [concept, section-1-2]
tier: construct
sources: [L03-04P, L08P, L10P, formula-snippets/Exam1]
---
# Distributions

## In Plain English
A distribution describes all possible values a random variable X can take and their probabilities. Discrete distributions use a PMF (table or formula); continuous distributions use a PDF (area under curve = probability).

## Discrete Distributions

### PMF (Probability Mass Function)
- f(x) = P(X = x) for each value x
- Requirements: f(x) ≥ 0 for all x, Σf(x) = 1

### Expected Value (Mean)
$$\mu = E[X] = \sum x \cdot f(x)$$

### Variance
$$\sigma^2 = V[X] = E[X^2] - (E[X])^2 = \sum x^2 f(x) - \mu^2$$

### Standard Deviation
$$\sigma = \sqrt{V[X]}$$

**Calculation table pattern:**

| X | P(X=x) | x·f(x) | x²·f(x) |
|---|--------|--------|---------|
| 0 | ... | ... | ... |
| 1 | ... | ... | ... |
| Sum | 1 | = E[X] = μ | → then V[X] = E[X²]−μ² |

---

## Binomial Distribution
- n independent trials, each with probability p of success
- X = number of successes

$$f(x) = \binom{n}{x} p^x (1-p)^{n-x}, \quad x = 0, 1, \ldots, n$$

| Parameter | Formula |
|-----------|---------|
| Mean | μ = np |
| Variance | σ² = np(1−p) |

**Normal approximation valid when:** np ≥ 5 **and** n(1−p) ≥ 5

---

## Normal Distribution
- Continuous, bell-shaped, symmetric about μ
- Notation: X ~ N(μ, σ²)

**Standardization (Z-score):**
$$Z = \frac{X - \mu}{\sigma} \sim N(0,1)$$

Use Z-table to find P(Z < z) = Φ(z)

| Probability | Formula |
|-------------|---------|
| P(X < a) | Φ((a−μ)/σ) |
| P(X > a) | 1 − Φ((a−μ)/σ) |
| P(a < X < b) | Φ((b−μ)/σ) − Φ((a−μ)/σ) |

---

## Sampling Distribution of X̄ (CLT)
If X ~ N(μ, σ²) or n is large (n ≥ 40):
$$\bar{X} \sim N\!\left(\mu,\; \frac{\sigma^2}{n}\right)$$

**Standard error of the mean:** SE = σ/√n

---

## Numerical Summaries

| Measure | Formula / Description |
|---------|----------------------|
| Sample mean | x̄ = Σxᵢ/n |
| Sample variance | s² = Σ(xᵢ − x̄)²/(n−1) |
| Sample std dev | s = √s² |
| Median (Q2) | Middle value of sorted data |
| Q1 | 25th percentile (lower quartile) |
| Q3 | 75th percentile (upper quartile) |
| IQR | Q3 − Q1 |
| Range | max − min |

**Excel functions:** AVERAGE(), MEDIAN(), STDEV.S(), VAR.S(), MAX()−MIN()

---

## t-Distribution
Used when σ is **unknown** and population is normal (or n is large).
- ν = n − 1 degrees of freedom
- Notation: t_{α/2, n−1}
- Fatter tails than Z; approaches N(0,1) as n → ∞

$$T = \frac{\bar{X} - \mu}{S/\sqrt{n}} \sim t_{n-1}$$

## χ² (Chi-Square) Distribution
$$X^2 = \frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$$
- Right-skewed, non-negative
- Used for inference on variance and goodness-of-fit

## F Distribution
Ratio of two independent chi-square variables divided by their df:
$$F = \frac{W/u}{Y/v} \sim F_{u,v}$$
- Used for comparing two variances
- Lower tail: $f_{1-\alpha,u,v} = \frac{1}{f_{\alpha,v,u}}$

## Related
- [confidence-intervals](confidence-intervals.md)
- [hypothesis-testing-overview](hypothesis-testing-overview.md)
- [chi-square](chi-square.md)
- [two-sample-tests](two-sample-tests.md)
- [correlation-transformations](correlation-transformations.md) — Fisher Z-transform produces a statistic that follows the standard normal

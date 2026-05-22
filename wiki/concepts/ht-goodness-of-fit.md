---
tags: [concept, section-1-2]
tier: procedure
sources: [L19P, formula-snippets]
---
# χ² Goodness-of-Fit Test

## In Plain English
Use when you want to test whether observed category counts fit a claimed probability distribution. You compare what you observed (Oᵢ) to what you would expect under H₀ (Eᵢ = n·pᵢ). Large discrepancies produce a large χ² statistic. The test is **always upper-tail only** — a large χ² means poor fit.

## When To Use
- Testing whether data follows a specified distribution (uniform, binomial, Poisson, normal, etc.)
- Data are categorical counts across k categories
- All expected counts Eᵢ ≥ 5 (combine categories if needed)

## Formula(s)

| Symbol | Meaning |
|--------|---------|
| Oᵢ | observed frequency in category i |
| Eᵢ | expected frequency = n·pᵢ |
| k | number of categories |
| p | number of distribution parameters estimated from the data |

**Test statistic:**
$$\chi_0^2 = \sum_{i=1}^{k} \frac{(O_i - E_i)^2}{E_i}$$

**Degrees of freedom — GENERAL FORM:**
$$df = k - 1 - p$$

where p = number of parameters estimated from the sample data.

| Situation | p | df |
|-----------|---|----|
| Probabilities fully specified (e.g., uniform, or given p₁…pₖ) | 0 | k − 1 |
| Testing normal distribution, estimating μ and σ from data | 2 | k − 3 |
| Testing Poisson, estimating λ from data | 1 | k − 2 |
| Testing binomial, estimating p from data | 1 | k − 2 |

> **Note on the quick reference:** The Exam 2 quick reference sheet listed df = k−1. This is the special case when p = 0 (expected probabilities are fully specified in the problem). The general formula used in class is **df = k − 1 − p**. If you estimate any parameters from the data, subtract that count from df.

**Rejection criterion:** Reject H₀ if χ₀² > χ²_{α, df} (always upper-tail)

**Computing Eᵢ:**
$$E_i = n \cdot p_i$$
where pᵢ is the probability assigned to category i under H₀.

## Key Assumptions
- Observations are independent
- Each expected frequency Eᵢ ≥ 5 (if not, merge adjacent categories and recount k)
- Categories are mutually exclusive and exhaustive

## Common Mistakes
- Using df = k−1 when parameters were estimated from data — subtract p from df
- Forgetting that Eᵢ = n·pᵢ (not the same as the observed count)
- Using this test when data are continuous — bin into categories first, or use KS test
- Applying a two-tail test — GoF is always upper-tail only

## Related
- [ht-independence](ht-independence.md) — different χ² test, for testing association in a two-way table
- [ht-one-sample-chisq-variance](ht-one-sample-chisq-variance.md) — different χ² test, on σ²
- [chi-square](chi-square.md) — broader coverage of all χ² procedures
- [ht-tests-overview](../reference/ht-tests-overview.md) — full test selection table

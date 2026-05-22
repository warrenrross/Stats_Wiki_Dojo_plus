---
tags: [reference, unit-2]
tier: reference
sources: [L15P-L25P, quick_reference_Exam2]
---
# Hypothesis Tests — Unit 2 Overview

Quick-lookup table for all Unit 2 hypothesis tests. Each test has its own detailed page (linked in the Test column). Click through for full formulas, CI formulas, assumptions, and common mistakes.

---

## One-Sample Tests

| # | Test | Parameter | When to Use | Statistic | Distribution | df |
|---|------|-----------|-------------|-----------|--------------|-----|
| a | [[ht-one-sample-z-mean\|One-Sample Z (mean)]] | μ | σ² **known** or n ≥ 40 | Z₀ = (X̄ − μ₀)/(σ/√n) | Z | — |
| b | [[ht-one-sample-t-mean\|One-Sample T (mean)]] | μ | σ² **unknown**, n < 40 | T₀ = (X̄ − μ₀)/(S/√n) | t | n−1 |
| c | [[ht-one-sample-chisq-variance\|One-Sample χ² (variance)]] | σ² | One sample, normal pop | χ₀² = (n−1)S²/σ₀² | χ² | n−1 |
| d | [[ht-one-sample-z-proportion\|One-Sample Z (proportion)]] | p | Binomial, np₀≥5 & n(1−p₀)≥5 | Z₀ = (X − np₀)/√(np₀(1−p₀)) | Z | — |

---

## Categorical / Distribution Tests

| # | Test | Parameter | When to Use | Statistic | Distribution | df |
|---|------|-----------|-------------|-----------|--------------|-----|
| e | [[ht-goodness-of-fit\|χ² Goodness of Fit]] | distribution | Does data follow a claimed distribution? | χ₀² = Σ(Oᵢ−Eᵢ)²/Eᵢ | χ² | **k−1−p** |
| f | [[ht-independence\|χ² Test of Independence]] | association | Are two categorical variables independent? | χ₀² = ΣΣ(Oᵢⱼ−Eᵢⱼ)²/Eᵢⱼ | χ² | (r−1)(c−1) |

> **GoF df note:** df = k − 1 − p where p = number of parameters estimated from data. When expected probabilities are fully specified (p = 0), df = k − 1. Estimating μ and σ for a normal fit → p = 2, df = k − 3.

---

## Two-Sample Tests

| # | Test | Parameter | When to Use | Statistic | Distribution | df |
|---|------|-----------|-------------|-----------|--------------|-----|
| g | [[ht-two-sample-z-means\|Two-Sample Z (means)]] | μ₁−μ₂ | Both σ² **known** | Z₀ = (X̄₁−X̄₂−Δ₀)/√(σ₁²/n₁+σ₂²/n₂) | Z | — |
| h1 | [[ht-two-sample-t-means\|Two-Sample T, Case 1 (pooled)]] | μ₁−μ₂ | σ² unknown, **equal** variances | T₀ = (X̄₁−X̄₂−Δ₀)/(Sₚ√(1/n₁+1/n₂)) | t | n₁+n₂−2 |
| h2 | [[ht-two-sample-t-means\|Two-Sample T, Case 2 (Welch's)]] | μ₁−μ₂ | σ² unknown, **unequal** variances | T₀ = (X̄₁−X̄₂−Δ₀)/√(S₁²/n₁+S₂²/n₂) | t | ν (Welch) |
| i | [[ht-paired-t\|Paired T-Test]] | μ_D | Matched/paired observations | T₀ = (D̄−Δ₀)/(Sᴅ/√n) | t | n−1 |
| j | [[ht-two-sample-f-variances\|Two-Sample F (variances)]] | σ₁²/σ₂² | Compare two variances | F₀ = S₁²/S₂² (larger in numerator) | F | n₁−1, n₂−1 |

---

## Hypothesis Table Template (all tests)

| H₁ | p-value | Reject H₀ if |
|----|---------|--------------|
| θ ≠ θ₀ | Two-tailed | \|stat\| > critical value |
| θ > θ₀ | Upper-tail | stat > critical value |
| θ < θ₀ | Lower-tail | stat < −critical value |

χ² and F tests are **always upper-tail only.**

---

## Z Critical Values (common)

| CI | α | Tails | z |
|----|---|-------|---|
| 0.99 | 0.01 | two | ±2.576 |
| 0.99 | 0.01 | one | ±2.326 |
| 0.95 | 0.05 | two | ±1.960 |
| 0.95 | 0.05 | one | ±1.645 |
| 0.90 | 0.10 | two | ±1.645 |
| 0.90 | 0.10 | one | ±1.282 |

---

## Decision Flow: Which Two-Sample Test?

```
Two samples → independent or paired?
├── Paired → [ht-paired-t](../concepts/ht-paired-t.md)
└── Independent → σ² known or unknown?
    ├── Known → [ht-two-sample-z-means](../concepts/ht-two-sample-z-means.md)
    └── Unknown → run F-test [ht-two-sample-f-variances](../concepts/ht-two-sample-f-variances.md)
        ├── Equal variances → [ht-two-sample-t-means](../concepts/ht-two-sample-t-means.md) Case 1 (pooled)
        └── Unequal variances → [ht-two-sample-t-means](../concepts/ht-two-sample-t-means.md) Case 2 (Welch's)
```

---

## Related
- [which-test](../concepts/which-test.md) — broader flowchart including ANOVA, regression, control charts
- [confidence-intervals](../concepts/confidence-intervals.md) — CI formulas for all one-sample tests
- [two-sample-tests](../concepts/two-sample-tests.md) — additional detail on two-sample inference
- [hypothesis-tests-r](../r-code/hypothesis-tests-r.md) — R code for all tests above

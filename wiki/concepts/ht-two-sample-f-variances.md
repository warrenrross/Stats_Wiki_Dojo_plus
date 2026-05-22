---
tags: [concept, section-1-2]
tier: procedure
sources: [L25P, formula-snippets]
---
# Two-Sample F-Test on Equal Variances

## In Plain English
Use to test whether two populations have equal variances. This is typically run **before** a two-sample T-test to decide whether to use the pooled (Case 1) or Welch's (Case 2) version. The test statistic is the ratio of two sample variances, which follows an F-distribution under H₀. By convention, place the **larger** variance in the numerator so F₀ ≥ 1, simplifying table lookup.

## When To Use
- Testing H₀: σ₁² = σ₂²
- Two independent samples from normal populations
- Preliminary check before running [[ht-two-sample-t-means]]

## Formula(s)

| Symbol | Meaning |
|--------|---------|
| S₁² | sample variance (numerator — conventionally the larger one) |
| S₂² | sample variance (denominator) |
| n₁ | sample size for sample 1 |
| n₂ | sample size for sample 2 |

**Test statistic:**
$$F_0 = \frac{S_1^2}{S_2^2} \sim F_{n_1-1,\; n_2-1}$$

**Convention:** place the larger S² in the numerator so F₀ ≥ 1.

**Hypothesis table:**

| H₁ | Rejection Criterion |
|----|---------------------|
| σ₁² ≠ σ₂² | F₀ > F_{α/2, n₁−1, n₂−1} |
| σ₁² > σ₂² | F₀ > F_{α, n₁−1, n₂−1} |
| σ₁² < σ₂² | F₀ < F_{1−α, n₁−1, n₂−1} |

> For two-sided test with the larger-in-numerator convention: reject H₀ if F₀ > F_{α/2, n₁−1, n₂−1}. The lower critical value is automatically handled because F₀ ≥ 1.

**Confidence interval on σ₁²/σ₂²:**
$$\frac{s_1^2}{s_2^2} \cdot \frac{1}{F_{\alpha/2,\,n_1-1,\,n_2-1}} \leq \frac{\sigma_1^2}{\sigma_2^2} \leq \frac{s_1^2}{s_2^2} \cdot F_{\alpha/2,\,n_2-1,\,n_1-1}$$

Note: the two F critical values use **swapped** degrees of freedom.

**df:** numerator df = n₁ − 1, denominator df = n₂ − 1

## Key Assumptions
- Both populations must be **normal** (F-test on variances is very sensitive to non-normality)
- Samples are independent

## Common Mistakes
- Forgetting to put the larger variance in the numerator for two-sided test
- Using the wrong df order — F_{α/2, n₁−1, n₂−1} means numerator df first, denominator df second
- Swapping df in the CI formula — left bound uses F with (n₁−1, n₂−1), right uses (n₂−1, n₁−1)
- Concluding equal variances just because F-test doesn't reject — absence of evidence ≠ evidence of absence; Welch's is safer by default

## Related
- [[ht-two-sample-t-means]] — use this test first to decide Case 1 vs Case 2
- [[ht-one-sample-chisq-variance]] — one-sample variance test (use χ²)
- [[hypothesis-tests-r]] — `var.test(x, y)`
- [[ht-tests-overview]] — full test selection table

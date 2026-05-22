---
tags: [r-code, section-1-2]
tier: script
sources: [HT in R materials, Drill files]
---
# R: Hypothesis Tests and Confidence Intervals

## Purpose
Running one-sample tests, two-sample tests, chi-square tests, and reading their output in R.

## Setup

```r
pacman::p_load(pacman, rio, tidyverse)
```

---

## One-Sample t-Test (σ unknown)

**H₀: μ = μ₀**

```r
# From raw data vector
t.test(x, mu = mu0, alternative = "two.sided", conf.level = 0.95)

# alternative options: "two.sided", "greater", "less"
```

**Output walkthrough:**
```
t = -2.34, df = 19, p-value = 0.031
95 percent confidence interval:  47.21  49.85
sample estimates: mean of x = 48.53
```

| Output | Teacher's Term |
|--------|---------------|
| `t = -2.34` | T₀ = −2.34 (t test statistic) |
| `df = 19` | n − 1 degrees of freedom |
| `p-value = 0.031` | Compare to α; < α → reject H₀ |
| `95 percent confidence interval` | "We are 95% confident μ is between [lower] and [upper]" |

---

## One-Sample Z-Test (σ known)

R doesn't have a built-in z-test — compute manually:

```r
z0 <- (xbar - mu0) / (sigma / sqrt(n))

# Two-sided p-value:
p_val <- 2 * (1 - pnorm(abs(z0)))

# One-sided upper (H₁: μ > μ₀):
p_val <- 1 - pnorm(z0)

# One-sided lower (H₁: μ < μ₀):
p_val <- pnorm(z0)

# CI: 95%
lower <- xbar - qnorm(0.975) * sigma / sqrt(n)
upper <- xbar + qnorm(0.975) * sigma / sqrt(n)
```

---

## Two-Sample t-Tests

**Pooled (equal variances):**
```r
t.test(x1, x2, var.equal = TRUE, mu = 0, alternative = "two.sided")
```

**Welch (unequal variances — default):**
```r
t.test(x1, x2, var.equal = FALSE, mu = 0, alternative = "two.sided")
```

**Paired:**
```r
t.test(x1, x2, paired = TRUE, mu = 0, alternative = "two.sided")
# OR: compute differences first
d <- x1 - x2
t.test(d, mu = 0)
```

**Output:**
- `t = ` → T₀
- `df = ` → degrees of freedom (Welch df is non-integer)
- `p-value` → compare to α
- `95 percent confidence interval` → CI on μ₁ − μ₂

---

## F-Test for Equal Variances

```r
var.test(x1, x2, ratio = 1, alternative = "two.sided")
```

| Output | Meaning |
|--------|---------|
| `F = ` | F₀ = s₁²/s₂² |
| `df = ` | n₁−1, n₂−1 |
| `p-value` | for H₀: σ₁² = σ₂² |
| `95% CI on ratio` | CI on σ₁²/σ₂² |

---

## Chi-Square Goodness-of-Fit

```r
observed <- c(O1, O2, O3, O4)     # observed counts
expected <- c(E1, E2, E3, E4)     # expected counts (or probabilities)
probs    <- expected / sum(expected)

chisq.test(x = observed, p = probs)
```

**Or compute manually:**
```r
chi2_0 <- sum((observed - expected)^2 / expected)
df     <- length(observed) - 1
p_val  <- pchisq(chi2_0, df = df, lower.tail = FALSE)
```

---

## Chi-Square Test of Independence (Contingency Table)

```r
# From a matrix of counts
table_mat <- matrix(c(O11, O12, O21, O22), nrow = 2, byrow = TRUE)
chisq.test(table_mat)

# From a data frame with two categorical columns
chisq.test(table(df$var1, df$var2))
```

**Output:**
| Output | Teacher's Term |
|--------|---------------|
| `X-squared` | χ²₀ test statistic |
| `df` | (r−1)(c−1) degrees of freedom |
| `p-value` | p-value for independence test |

---

## Test on a Proportion

```r
# From counts: X successes in n trials, null proportion p0
prop.test(x = X, n = n, p = p0, alternative = "two.sided", correct = FALSE)

# Or compute manually:
p_hat <- X / n
z0    <- (p_hat - p0) / sqrt(p0 * (1 - p0) / n)
p_val <- 2 * (1 - pnorm(abs(z0)))   # two-sided
```

---

## Critical Values — Quick Reference

```r
# t critical values
qt(0.975, df = 18)    # two-sided α=0.05, df=18 → 2.101
qt(0.95,  df = 18)    # one-sided α=0.05 (or two-sided α=0.10) → 1.734

# Z critical values
qnorm(0.975)    # z_{0.025} = 1.960
qnorm(0.95)     # z_{0.05}  = 1.645

# Chi-square critical values
qchisq(0.95, df = 9)    # upper 5% with df=9
qchisq(0.05, df = 9)    # lower 5% with df=9

# F critical values
qf(0.95, df1 = 1, df2 = 18)    # F_{0.05, 1, 18}
```

---

## Common Summary Statistics

```r
mean(x)              # x̄
sd(x)                # s (sample standard deviation)
var(x)               # s² (sample variance)
length(x)            # n
median(x)            # median
quantile(x, 0.25)    # Q1
quantile(x, 0.75)    # Q3
IQR(x)               # Q3 - Q1
range(x)             # min, max
summary(x)           # 5-number summary + mean
```

---

## Teacher-Language Output Guide

| Situation | What to say |
|-----------|------------|
| p-value < α (any test) | "Reject H₀ at α = X. There is sufficient evidence that [H₁ in context]." |
| p-value > α | "Fail to reject H₀ at α = X. There is insufficient evidence that [H₁ in context]." |
| t₀ > t_{α/2, df} | Equivalent: "reject based on critical value" |
| CI doesn't contain μ₀ | Equivalent: "reject based on confidence interval" |

## Related
- [hypothesis-testing-overview](../concepts/hypothesis-testing-overview.md)
- [two-sample-tests](../concepts/two-sample-tests.md)
- [chi-square](../concepts/chi-square.md)
- [reading-r-output](reading-r-output.md)

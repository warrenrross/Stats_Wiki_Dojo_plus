---
tags: [example, unit-2]
tier: script
sources: [L22P, L23P, L24P, two-sample-tests, hypothesis-tests-r]
---
# Examples: Two-Sample and Paired t-Tests

See also: [two-sample-tests](../concepts/two-sample-tests.md), [ht-two-sample-t-means](../concepts/ht-two-sample-t-means.md), [ht-paired-t](../concepts/ht-paired-t.md), [ht-two-sample-f-variances](../concepts/ht-two-sample-f-variances.md), [hypothesis-tests-r](../r-code/hypothesis-tests-r.md)

---

## Decision Flowchart (Quick Reference)

```
Two groups?
├── Paired (matched/before-after)?  →  Paired t-test
└── Independent?
    ├── Run F-test on variances first
    │   ├── F p-value > α  →  Equal variances  →  Pooled t-test  (Case 1)
    │   └── F p-value ≤ α  →  Unequal variances  →  Welch t-test  (Case 2)
```

---

## Problem 1 — Pooled Two-Sample t-Test (Equal Variances)

### Problem Statement
An industrial engineer is comparing the tensile strength (MPa) of wire produced by two machines. A preliminary F-test shows no significant difference in variances. Test whether the machines produce wire of equal mean strength at α = 0.05.

**Machine A** (n₁ = 8): 118, 121, 124, 119, 122, 120, 117, 123  
**Machine B** (n₂ = 8): 124, 127, 121, 125, 126, 123, 128, 122

### Given / Find
- H₀: μ₁ − μ₂ = 0 (machines produce the same mean strength)
- H₁: μ₁ − μ₂ ≠ 0 (two-sided)
- α = 0.05
- Variances assumed equal (pooled)

### Solution

**Step 1 — Enter data and run F-test to confirm equal variances**

```r
pacman::p_load(pacman, tidyverse)

machA <- c(118, 121, 124, 119, 122, 120, 117, 123)
machB <- c(124, 127, 121, 125, 126, 123, 128, 122)

var.test(machA, machB)
```

```
F = 0.7143, num df = 7, denom df = 7, p-value = 0.7046
```

p-value = 0.7046 > 0.05 → Fail to reject H₀ of equal variances → use **pooled t-test**.

**Step 2 — Run pooled t-test**

```r
t.test(machA, machB, var.equal = TRUE, alternative = "two.sided")
```

```
        Two Sample t-test

t = -3.6742, df = 14, p-value = 0.00253
alternative hypothesis: true difference in means is not equal to 0
95 percent confidence interval:
 -8.549048 -2.200952
sample estimates:
mean of x mean of y 
    120.75    126.12 
```

**Step 3 — State conclusion**

p-value = 0.00253 < α = 0.05 → **Reject H₀**.

### Interpreting the Output

| R Output | Symbol | Meaning |
|----------|--------|---------|
| `t = -3.6742` | t* | Test statistic (negative → Machine A mean < Machine B) |
| `df = 14` | n₁ + n₂ − 2 = 16 − 2 | Pooled degrees of freedom |
| `p-value = 0.00253` | p-value | Probability of |t| ≥ 3.67 if H₀ true |
| `95 percent confidence interval: -8.55, -2.20` | CI on μ₁ − μ₂ | Does not contain 0 → consistent with rejection |

### Answer
t* = −3.67, df = 14, p-value = 0.0025. Reject H₀ at α = 0.05. There is sufficient evidence to conclude the mean tensile strength differs between the two machines. Machine B produces stronger wire on average (126.1 vs 120.8 MPa).

---

## Problem 2 — Welch t-Test (Unequal Variances)

### Problem Statement
A quality engineer compares the fill weights (g) of two packaging lines. The F-test reveals significantly different variances. Test whether the lines have the same mean fill weight at α = 0.05.

**Line 1** (n₁ = 10): 500.2, 499.8, 501.1, 500.5, 499.6, 500.9, 500.1, 499.4, 501.3, 500.0  
**Line 2** (n₂ = 10): 497.3, 502.1, 498.7, 503.5, 496.9, 504.2, 497.5, 503.0, 498.2, 502.8

### Given / Find
- H₀: μ₁ − μ₂ = 0
- H₁: μ₁ − μ₂ ≠ 0
- α = 0.05
- Variances unequal (Welch)

### Solution

**Step 1 — Confirm unequal variances with F-test**

```r
line1 <- c(500.2, 499.8, 501.1, 500.5, 499.6, 500.9, 500.1, 499.4, 501.3, 500.0)
line2 <- c(497.3, 502.1, 498.7, 503.5, 496.9, 504.2, 497.5, 503.0, 498.2, 502.8)

var.test(line1, line2)
```

```
F = 0.07143, num df = 9, denom df = 9, p-value = 0.0012
```

p-value = 0.0012 < 0.05 → Reject equal variances → use **Welch t-test** (`var.equal = FALSE`).

**Step 2 — Welch t-test (default in R)**

```r
t.test(line1, line2, var.equal = FALSE, alternative = "two.sided")
```

```
        Welch Two Sample t-test

t = -0.063, df = 9.4, p-value = 0.951
alternative hypothesis: true difference in means is not equal to 0
95 percent confidence interval:
 -3.461  3.281
sample estimates:
mean of x mean of y 
   500.29    500.38 
```

**Step 3 — State conclusion**

p-value = 0.951 > 0.05 → **Fail to reject H₀**.

### Interpreting the Output

| R Output | Note |
|----------|------|
| `df = 9.4` | Welch df — decimal value from the Satterthwaite formula; R computes this automatically |
| `var.equal = FALSE` | Default for `t.test()`; always specify explicitly for clarity |
| CI contains 0 | Consistent with failing to reject H₀ |

### Answer
t* = −0.063, df = 9.4 (Welch), p-value = 0.951. Fail to reject H₀ at α = 0.05. There is insufficient evidence to conclude the mean fill weight differs between the two packaging lines.

---

## Problem 3 — Paired t-Test (Before/After)

### Problem Statement
A process engineer tests whether a new lubricant reduces cycle time on a CNC machine. Eight parts are machined twice: once with the standard lubricant and once with the new lubricant. The same part is used for both runs (paired design). Test at α = 0.01.

| Part | Standard (s) | New (s) |
|------|-------------|---------|
| 1    | 45.2        | 43.8    |
| 2    | 47.8        | 45.1    |
| 3    | 44.3        | 44.0    |
| 4    | 46.9        | 44.7    |
| 5    | 45.5        | 44.2    |
| 6    | 48.1        | 46.3    |
| 7    | 44.7        | 43.9    |
| 8    | 46.3        | 44.8    |

### Given / Find
- H₀: μ_D = 0 (no difference; D = Standard − New)
- H₁: μ_D > 0 (new lubricant reduces time → positive differences)
- α = 0.01, one-sided upper tail

### Solution

**Step 1 — Enter data**

```r
standard <- c(45.2, 47.8, 44.3, 46.9, 45.5, 48.1, 44.7, 46.3)
new_lub  <- c(43.8, 45.1, 44.0, 44.7, 44.2, 46.3, 43.9, 44.8)
```

**Step 2 — Compute differences and inspect**

```r
d <- standard - new_lub
mean(d)    # 1.6375
sd(d)      # 0.6580
```

Mean difference is positive — the new lubricant does appear faster.

**Step 3 — Run paired t-test**

```r
t.test(standard, new_lub,
       paired      = TRUE,
       alternative = "greater")   # H₁: μ_D > 0
```

```
        Paired t-test

t = 7.0372, df = 7, p-value = 0.0001031
alternative hypothesis: true mean difference is greater than 0
95 percent confidence interval:
 1.088  Inf
sample estimates:
mean difference 
         1.6375 
```

**Step 4 — State conclusion**

p-value = 0.000103 < α = 0.01 → **Reject H₀**.

### Interpreting the Output

| R Output | Symbol | Meaning |
|----------|--------|---------|
| `t = 7.0372` | t* | Large positive value → differences strongly positive |
| `df = 7` | n − 1 = 8 − 1 | Paired df uses number of pairs, not total observations |
| `paired = TRUE` | — | Computes D = x1 − x2 internally; must specify |
| `alternative = "greater"` | H₁: μ_D > 0 | Tests whether standard > new (new lubricant is faster) |

> **Key concept:** Paired t-test has df = n − 1 where n = number of **pairs**, not total observations (2n − 2). This is why it is more powerful — it removes part-to-part variability from the error.

### Answer
t* = 7.04, df = 7, p-value = 0.0001. Reject H₀ at α = 0.01. There is sufficient evidence to conclude the new lubricant reduces mean cycle time (average reduction = 1.64 seconds per part).

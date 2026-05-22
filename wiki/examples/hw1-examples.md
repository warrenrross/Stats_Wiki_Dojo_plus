---
tags: [example, unit-1, unit-2]
tier: script
sources: [Homework_2.r, Drill 04 - Binom and Norm_Ross.R, L6-7P, L8-9P]
---
# Examples: Descriptive Statistics and Normal Distribution

See also: [distributions](../concepts/distributions.md), [standard-error](../concepts/standard-error.md), [hypothesis-tests-r](../r-code/hypothesis-tests-r.md)

---

## Problem 1 — Normal Distribution: Finding Probabilities (Credit Card Fraud)

### Problem Statement
A credit card company monitors cardholder transaction habits to detect unusual activity. The dollar value of unusual activity for a customer in a month follows a normal distribution with mean **μ = $250** and variance **σ² = $400** (so σ = $20).

Round all answers to four decimal places.

### Given / Find
- **Distribution:** X ~ N(250, 400)  →  X ~ N(μ = 250, σ = 20)
- **Find:**
  - (a) P(250 < X < 300)
  - (b) P(X > 300)
  - (c) If 10 customer accounts independently follow the same distribution, P(at least one exceeds $300)

### Solution

**Step 1 — Set up parameters**

```r
pacman::p_load(pacman, tidyverse)

mu    <- 250
sigma <- sqrt(400)   # σ = 20
```

**Step 2 — Part (a): P(250 < X < 300)**

Area between two values = right CDF minus left CDF.

```r
(pnorm(300, mu, sigma) - pnorm(250, mu, sigma)) %>% round(4)
# [1] 0.4938
```

**Step 3 — Part (b): P(X > 300)**

Upper-tail probability: use `lower.tail = FALSE` (or 1 − CDF).

```r
pnorm(300, mu, sigma, FALSE) %>% round(4)
# [1] 0.0062
```

**Step 4 — Part (c): P(at least one of 10 exceeds $300)**

"At least one" complement: 1 − P(none exceed). Each account independently has p = 0.0062 of exceeding $300.

$$P(\text{at least 1}) = 1 - (1 - p)^{10}$$

```r
p_one      <- pnorm(300, mu, sigma, FALSE)
p_atleast1 <- 1 - (1 - p_one)^10
p_atleast1 %>% round(4)
# [1] 0.0601
```

### Interpreting the Output

| Result | Value | Teacher's Phrasing |
|--------|-------|--------------------|
| P(250 < X < 300) | 0.4938 | "There is a 49.38% probability of $250–$300 in unusual activity" |
| P(X > 300) | 0.0062 | "There is a 0.62% probability of exceeding $300 in a month" |
| P(at least 1 of 10 > $300) | 0.0601 | "There is a 6.01% probability that at least one of the 10 accounts exceeds $300" |

### Answer
(a) P(250 < X < 300) = **0.4938**. (b) P(X > 300) = **0.0062**. (c) P(at least one of 10 exceeds $300) = **0.0601**.

---

## Problem 2 — Normal Distribution: Finding Quantiles

### Problem Statement
X is normally distributed with mean **μ = 5** and standard deviation **σ = 4**.

Find the value of x that satisfies each equation. Round to two decimal places.

### Given / Find
- **Distribution:** X ~ N(5, 16)
- **Find:** x such that:
  - (a) P(X > x) = 0.50
  - (b) P(X > x) = 0.95
  - (c) P(x < X < 9) = 0.20
  - (d) P(3 < X < x) = 0.95

### Solution

**Setup**

```r
mu    <- 5
sigma <- 4
```

**Part (a): P(X > x) = 0.50**

P(X > x) = 0.50 means x is the median = mean for a symmetric distribution.

```r
qnorm(1 - 0.50, mu, sigma) %>% round(2)
# [1] 5.00
```

**Part (b): P(X > x) = 0.95**

Upper tail of 0.95 → lower tail of 0.05 → x is well below the mean.

```r
qnorm(1 - 0.95, mu, sigma) %>% round(2)
# [1] -1.58
```

**Part (c): P(x < X < 9) = 0.20**

The area from x to 9 equals 0.20. Find the right-tail area beyond 9 first, then work backwards.

```r
right_tail <- pnorm(9, mu, sigma, lower.tail = FALSE)  # area beyond 9
left_tail  <- 1 - (right_tail + 0.20)                 # area below x
qnorm(left_tail, mu, sigma) %>% round(2)
# [1] 3.60
```

**Part (d): P(3 < X < x) = 0.95**

Area from 3 to x equals 0.95. CDF at 3 gives the left tail; add 0.95 to get CDF at x.

```r
left_tail <- pnorm(3, mu, sigma)
qnorm(left_tail + 0.95, mu, sigma) %>% round(2)
# [1] 11.58
```

### Answer
(a) x = **5.00**  (b) x = **−1.58**  (c) x = **3.60**  (d) x = **11.58**

---

## Problem 3 — Descriptive Statistics from Sample Data

### Problem Statement
Two samples of product measurements are collected from two different machines (n = 8 each).

**Machine 1:** 10, 9, 8, 7, 8, 6, 10, 6  
**Machine 2:** 10, 6, 10, 6, 8, 10, 8, 6

Compute the sample mean, standard deviation, and variance for each machine.

### Given / Find
- **Given:** Two raw data vectors, n = 8
- **Find:** x̄, s, s² for each sample

### Solution

```r
sample_1 <- c(10, 9, 8, 7, 8, 6, 10, 6)
sample_2 <- c(10, 6, 10, 6, 8, 10, 8, 6)

# Machine 1
mu_1  <- mean(sample_1)   # 8.0
s_1   <- sd(sample_1)     # 1.604
var_1 <- var(sample_1)    # 2.571

# Machine 2
mu_2  <- mean(sample_2)   # 8.0
s_2   <- sd(sample_2)     # 1.852
var_2 <- var(sample_2)    # 3.429
```

### Interpreting the Output

| Statistic | Machine 1 | Machine 2 | Note |
|-----------|-----------|-----------|------|
| x̄ | 8.0 | 8.0 | Same mean — but spread differs |
| s | 1.604 | 1.852 | Machine 2 is more variable |
| s² | 2.571 | 3.429 | s² = s × s (not just s rounded) |

> **Common mistake:** R's `sd()` uses the sample formula (divides by n−1). The population formula (divides by n) is not the default. On exams, always use the sample standard deviation unless σ is stated as known.

### Answer
Machine 1: x̄ = **8.0**, s = **1.60**, s² = **2.57**.  
Machine 2: x̄ = **8.0**, s = **1.85**, s² = **3.43**.  
Both machines have the same mean but Machine 2 has greater variability.

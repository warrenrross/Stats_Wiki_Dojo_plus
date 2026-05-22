---
tags: [example, unit-3]
tier: script
sources: [WireBond v1 - Introduction to SLR.R, WireBond v3 - Hypothesis Testing.R, Lesson31_Q1.R, L31P, L34-35P]
---
# Examples: Simple Linear Regression — Model Fitting and Hypothesis Tests

See also: [regression-slr](../concepts/regression-slr.md), [regression-ht](../concepts/regression-ht.md), [regression-r](../r-code/regression-r.md), [reading-r-output](../r-code/reading-r-output.md), [anova-table-examples](anova-table-examples.md)

---

## Problem 1 — WireBond SLR: Fitting the Model and Reading Output

### Problem Statement
Wire pull strength (y, in pounds-force) is modeled as a function of wire length (x, in inches). Data from n = 25 wire bond specimens. Fit the SLR model, identify the regression equation, and interpret the R output.

### Given / Find
- **Response (y):** `Strength`
- **Predictor (x):** `Length`
- **n = 25** specimens
- **Find:** β̂₀, β̂₁, σ̂, R², and the regression equation

### Solution

**Step 1 — Import data and fit the model**

```r
pacman::p_load(magrittr, rio, tidyverse)

df <- import("WireBond.xlsx") %>%
  as_tibble() %>%
  select(y = Strength, x = Length)

fit <- df %>% lm()
fit %>% summary()
```

**Step 2 — Read the summary output**

```
Call:
lm(formula = y ~ x, data = .)

Residuals:
    Min      1Q  Median      3Q     Max
-3.7331 -0.9655  0.3116  1.0888  3.6285

Coefficients:
            Estimate Std. Error t value Pr(>|t|)
(Intercept)  -5.1281     1.9818  -2.588   0.0163 *
x             2.9027     0.2991   9.703  4.5e-09 ***

Residual standard error: 1.936 on 23 degrees of freedom
Multiple R-squared:  0.8037
Adjusted R-squared:  0.7954
F-statistic: 94.15 on 1 and 23 DF,  p-value: 4.504e-09
```

**Step 3 — Extract key values**

| R Output | Symbol | Value | Teacher's Term |
|----------|--------|-------|----------------|
| `(Intercept) Estimate` | β̂₀ | −5.128 | Intercept |
| `x Estimate` | β̂₁ | 2.903 | Slope |
| `Residual standard error` | σ̂ = √MSE | 1.936 | Estimated process standard deviation |
| `Multiple R-squared` | R² | 0.8037 | Coefficient of determination |
| `F-statistic` | F₀ | 94.15 | Overall model F-test |

**Step 4 — Write the fitted model**

$$\hat{y} = -5.128 + 2.903\,x$$

**Step 5 — Predict mean strength at x = 8 inches**

```r
predict(fit, newdata = data.frame(x = 8))
# [1] 18.09
```

### Answer
Regression equation: ŷ = **−5.128 + 2.903x**.  
R² = 0.804: "**80.4% of the variation in wire pull strength is explained by the regression model.**"  
At x = 8 inches, predicted mean strength = **18.09 lbf**.

---

## Problem 2 — ANOVA Table Completion from SLR Output

### Problem Statement
Using the WireBond SLR fit from Problem 1, complete the ANOVA table by hand and verify with R.

**Partial table given:**

| Source | df | SS | MS | F | p |
|--------|----|----|----|----|---|
| Regression | ? | ? | ? | ? | ? |
| Residuals | ? | 86.17 | ? | | |
| **Total** | **24** | **440.00** | | | |

### Given / Find
- n = 25 → df_Total = 24
- SSE = 86.17 (from R `anova()` output: Residuals row)
- SST = 440.00 (SSR + SSE)
- **Find:** all missing cells

### Solution

**Step 1 — Degrees of freedom**

SLR has k = 1 predictor:

| Source | df |
|--------|-----|
| Regression | k = **1** |
| Residuals | n − 2 = **23** |
| Total | n − 1 = **24** ✓ |

**Step 2 — Sums of squares**

$$SS_R = SS_T - SS_E = 440.00 - 86.17 = 353.83$$

**Step 3 — Mean squares**

$$MS_R = \frac{SS_R}{df_R} = \frac{353.83}{1} = 353.83$$
$$MS_E = \frac{SS_E}{df_E} = \frac{86.17}{23} = 3.747 = \hat{\sigma}^2$$
$$\hat{\sigma} = \sqrt{3.747} = 1.936 \text{ (matches summary output)}$$

**Step 4 — F-statistic and p-value**

$$F_0 = \frac{MS_R}{MS_E} = \frac{353.83}{3.747} = 94.43$$

```r
pf(94.43, df1 = 1, df2 = 23, lower.tail = FALSE)
# [1] 4.504e-09
```

**Step 5 — Verify with R**

```r
fit %>% anova()
```

```
Analysis of Variance Table

Response: y
          Df Sum Sq Mean Sq F value    Pr(>F)
x          1 353.83  353.83  94.147 4.504e-09 ***
Residuals 23  86.17    3.75
```

**Completed ANOVA table:**

| Source | df | SS | MS | F | p |
|--------|----|----|----|----|---|
| Regression | 1 | 353.83 | 353.83 | 94.15 | 4.50 × 10⁻⁹ |
| Residuals | 23 | 86.17 | 3.747 | | |
| **Total** | **24** | **440.00** | | | |

### Answer
σ̂ = **1.936** lbf.  
F₀ = **94.15**, p-value < 0.0001 → **Reject H₀**. The model is statistically significant.

---

## Problem 3 — Hypothesis Test: Non-Zero Null (H₀: β₁ = β₁₀)

### Problem Statement
An engineer claims the true slope is **β₁ = 2.5** (each additional inch of wire adds exactly 2.5 lbf). Using the WireBond model, test this claim at α = 0.05.

### Given / Find
- H₀: β₁ = 2.5
- H₁: β₁ ≠ 2.5 (two-sided)
- From R: β̂₁ = 2.9027, SE(β̂₁) = 0.2991, df = 23

### Solution

**Step 1 — Compute the test statistic manually**

The t-statistic for a non-zero null:

$$t^* = \frac{\hat{\beta}_1 - \beta_{1,0}}{SE(\hat{\beta}_1)} = \frac{2.9027 - 2.5}{0.2991} = \frac{0.4027}{0.2991} = 1.346$$

```r
beta1_hat <- coef(fit)["x"]
se_beta1  <- summary(fit)$coefficients["x", "Std. Error"]
t_star    <- (beta1_hat - 2.5) / se_beta1
t_star
# [1] 1.346
```

**Step 2 — Compute p-value (two-sided)**

```r
p_value <- 2 * pt(abs(t_star), df = 23, lower.tail = FALSE)
p_value
# [1] 0.1916
```

**Step 3 — State conclusion**

p-value = 0.192 > α = 0.05 → **Fail to reject H₀**.

### Answer
t* = 1.35, df = 23, p-value = 0.192. Fail to reject H₀ at α = 0.05. There is insufficient evidence to conclude the slope differs from 2.5. The claim β₁ = 2.5 is consistent with the data.

> **Common mistake:** R's summary table always tests H₀: βⱼ = 0. For a non-zero null (like β₁ = 2.5), you must compute t* manually using the formula above. Do not use the p-value from the `summary()` output.

---

## Problem 4 — Predicting with SLR: Point Estimate vs Mean Response

### Problem Statement
For the WireBond model, find:
(a) The predicted pull strength for a **single new wire** of length 8 inches.
(b) A 95% CI on **mean strength** at x = 8 inches.
(c) A 95% **prediction interval** for a single new wire at x = 8 inches.

### Solution

```r
x0 <- data.frame(x = 8)

# (a) Point estimate
predict(fit, newdata = x0)
# [1] 18.09

# (b) 95% CI on mean response
predict(fit, newdata = x0, interval = "confidence", level = 0.95)
#    fit      lwr      upr
# 18.09   17.14    19.04

# (c) 95% PI for single future observation
predict(fit, newdata = x0, interval = "prediction", level = 0.95)
#    fit      lwr      upr
# 18.09   14.08    22.10
```

### Interpreting CI vs PI

| Interval | Width | Covers |
|----------|-------|--------|
| CI on mean response | Narrow (~1.9) | Where the **mean** of all wires at x = 8 falls |
| PI for single obs | Wide (~8.0) | Where a **single future wire** at x = 8 falls |

PI is always wider than CI because it accounts for both estimation uncertainty (same as CI) and individual-unit variability (σ²).

### Answer
(a) ŷ = **18.09 lbf** at x = 8 inches.  
(b) 95% CI on mean response: **(17.14, 19.04)** — "We are 95% confident the mean pull strength at x = 8 is between 17.14 and 19.04 lbf."  
(c) 95% PI: **(14.08, 22.10)** — "We are 95% confident a single new wire of length 8 will have pull strength between 14.08 and 22.10 lbf."

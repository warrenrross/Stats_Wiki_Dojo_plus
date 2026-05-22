---
tags: [r-code, section-3]
tier: script
sources: [Section3_Study_Guide.Rmd, L36-37_Study_Guide.Rmd, L38-39_App_HWQ1.Rmd, L36-37_App_HWQ1.Rmd]
---
# R: Regression Analysis Workflow

## Purpose
Complete workflow for fitting SLR and MLR, running hypothesis tests, computing CIs and PIs, and checking model adequacy.

## Setup

```r
pacman::p_load(magrittr, rio, tidyverse)

# Import — rename columns y, x (SLR) or y, x1, x2, ... (MLR)
df <- import("data.csv") %>%
  as_tibble() %>%
  select(y, x)      # or select(y, x1, x2, ...)
```

---

## Step 1: Fit the Model

```r
# SLR
fit <- lm(y ~ x, data = df)

# MLR
fit <- lm(y ~ x1 + x2 + x3, data = df)

# Interaction term (create first, then fit)
df <- df %>% mutate(x1x2 = x1 * x2)
fit2 <- lm(y ~ x1x2, data = df)
```

---

## Step 2: ANOVA Table (F-test, SS decomposition)

```r
fit %>% anova() %>% print()
```

**Reading anova() output:**
| Column | Meaning | Teacher's Term |
|--------|---------|----------------|
| `Df` (predictor row) | k (# predictors) | Regression df |
| `Df` (Residuals) | n − p = n − k − 1 | Error df |
| `Sum Sq` (predictor) | SSR | Regression SS |
| `Sum Sq` (Residuals) | SSE | Error SS |
| `Mean Sq` (Residuals) | MSE = SSE/(n−p) | Error variance estimate (σ̂²) |
| `F value` | F₀ = MSR/MSE | F test statistic |
| `Pr(>F)` | p-value for F-test | p-value |

**Extracting from anova():**
```r
a   <- anova(fit)
SSR <- a["x", "Sum Sq"]              # SLR
SSE <- a["Residuals", "Sum Sq"]      # always
MSE <- a["Residuals", "Mean Sq"]     # always

# MLR: sum all non-residual rows for total SSR
SSR_MLR <- sum(a[1:(nrow(a)-1), "Sum Sq"])
SST     <- SSR + SSE                  # SST = SSR + SSE

# Overall p-value (correct for both SLR and MLR)
f_info <- summary(fit)$fstatistic
p_overall <- pf(f_info[1], f_info[2], f_info[3], lower.tail = FALSE)
```

---

## Step 3: Summary Table (Coefficients, t-tests, R²)

```r
fit %>% summary() %>% print()
```

**Reading summary()$coefficients:**
```
             Estimate  Std. Error  t value  Pr(>|t|)
(Intercept)  2627.82     44.18     59.49    < 2e-16
x             -37.15      2.55    -14.57    < 2e-16
```

| Column | Meaning | Teacher's Term |
|--------|---------|----------------|
| `Estimate` | β̂ⱼ | Regression coefficient estimate |
| `Std. Error` | se(β̂ⱼ) | Standard error of estimate |
| `t value` | T₀ = β̂ⱼ/se(β̂ⱼ) | t test statistic (null = 0 only!) |
| `Pr(>|t|)` | two-sided p-value for H₀: βⱼ = 0 | p-value |

**Extracting specific values:**
```r
coef(fit)["x"]                                    # β̂₁
coef(fit)["(Intercept)"]                          # β̂₀
summary(fit)$coefficients["x", "Std. Error"]      # se(β̂₁)
summary(fit)$coefficients["x", "t value"]         # t₀ (null=0 only)
summary(fit)$coefficients["x", "Pr(>|t|)"]       # p-value (null=0 only)
summary(fit)$r.squared                            # R²
summary(fit)$adj.r.squared                        # R²_adj
summary(fit)$sigma                                # σ̂ = √MSE
summary(fit)$sigma^2                              # MSE = σ̂²
```

**Non-zero null hypothesis — MUST compute manually:**
```r
# H₀: β₁ = -30 (example)
null_value <- -30
t0 <- (coef(fit)["x"] - null_value) / summary(fit)$coefficients["x", "Std. Error"]

# Critical values:
qt(1 - alpha/2, df = n - 2)     # two-sided at α
qt(1 - alpha, df = n - 2)       # one-sided at α

# p-value for computed t0:
2 * pt(-abs(t0), df = n - 2)    # two-sided
pt(-t0, df = n - 2)             # one-sided upper (H₁: β > null)
pt(t0, df = n - 2)              # one-sided lower (H₁: β < null)
```

---

## Step 4: Confidence Intervals on Coefficients

```r
fit %>% confint(level = 0.95) %>% print()
```

**Column names by confidence level (CRITICAL — wrong name returns NA):**
```r
ci <- confint(fit, level = 0.95)   # columns: "2.5 %" and "97.5 %"

# 90%:  columns "5 %" and "95 %"
# 95%:  columns "2.5 %" and "97.5 %"
# 99%:  columns "0.5 %" and "99.5 %"

ci["x", "2.5 %"]          # β₁ lower bound
ci["x", "97.5 %"]         # β₁ upper bound
ci["(Intercept)", "2.5 %"]  # β₀ lower bound
```

**Back-calculate β̂ from CI bounds:**
```r
L <- ci["x", "2.5 %"]; U <- ci["x", "97.5 %"]
b_hat <- (L + U) / 2
t_crit <- qt(0.975, df = n - 2)
se     <- (U - L) / 2 / t_crit
```

---

## Step 5: CI on Mean Response and PI on Future Observation

```r
x0 <- 30    # the predictor value of interest

# CI on mean response at x₀
ci_mean <- fit %>%
  predict(newdata = data.frame(x = x0), interval = "confidence", level = 0.95)
ci_mean[, "fit"]   # ŷ₀ (point estimate)
ci_mean[, "lwr"]   # lower bound
ci_mean[, "upr"]   # upper bound

# PI on a future observation at x₀
pi_obs <- fit %>%
  predict(newdata = data.frame(x = x0), interval = "prediction", level = 0.95)
pi_obs[, "lwr"]    # lower bound (always wider than CI)
pi_obs[, "upr"]    # upper bound

# MLR: supply all predictors
predict(fit, newdata = data.frame(x1 = 30, x2 = 4), interval = "confidence", level = 0.99)
```

---

## Step 6: Model Adequacy (Residual Diagnostics)

```r
df <- df %>%
  mutate(resid  = residuals(fit),
         fitted = fitted(fit),
         rstud  = rstudent(fit),       # externally studentized residuals
         h      = hatvalues(fit))      # leverage

# Residuals vs Fitted (check linearity and constant variance)
ggplot(df, aes(x = fitted, y = resid)) +
  geom_point(size = 2.5) +
  geom_hline(yintercept = 0, linetype = "dashed", color = "red") +
  labs(x = "Fitted Values", y = "Residuals",
       title = "Residuals vs Fitted")

# Normal Q-Q plot (check normality)
ggplot(df, aes(sample = resid)) +
  stat_qq(size = 2.5, color = "steelblue") +
  stat_qq_line(color = "red") +
  labs(title = "Normal Q-Q Plot of Residuals")

# Cook's distance (influence)
cooks.distance(fit) %>% sort(decreasing = TRUE) %>% head(5)
influence.measures(fit)    # comprehensive: Cook's D, DFFITS, DFBETAS, leverage

# Flag outliers
df %>% filter(abs(rstud) > 3)    # externally studentized > 3 → potential outlier
```

---

## Complete Scatter + Regression Line Plot

```r
ggplot(df, aes(x = x, y = y)) +
  geom_point(size = 2.8, color = "steelblue") +
  geom_smooth(method = "lm", se = FALSE, color = "firebrick", linewidth = 1.1) +
  annotate("label", x = min(df$x), y = max(df$y) * 0.97,
           label = sprintf("y-hat = %.3f + %.3f * x",
                           coef(fit)[1], coef(fit)[2]),
           hjust = 0, size = 3.2, color = "firebrick", fill = "white") +
  labs(title = "Y vs X with Fitted Line",
       x = "X variable", y = "Y variable") +
  theme_bw()
```

---

## Teacher-Language Output Guide

| Output | Teacher's Phrasing |
|--------|-------------------|
| R² = 0.862 | "86.2% of the variation in [Y] is explained by the regression model." |
| p-value (F) < α | "The regression model is significant at α = X." |
| p-value (t, β₁) < α | "There is sufficient evidence that β₁ ≠ 0 at α = X." |
| CI on β₁ = (L, U) | "We are 95% confident that β₁ is between L and U." |
| 0 not in CI for β₁ | "We reject H₀: β₁ = 0 at α = X." |
| CI on mean at x₀ | "We are 95% confident the mean [Y] at x=[x₀] is between [L] and [U]." |
| PI on future obs | "We are 95% confident a new [Y] at x=[x₀] will fall between [L] and [U]." |

## Related
- [[regression-slr]]
- [[regression-ht]]
- [[regression-ci]]
- [[model-adequacy]]
- [[reading-r-output]]

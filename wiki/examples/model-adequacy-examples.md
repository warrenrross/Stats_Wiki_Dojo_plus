---
tags: [example, section-3]
tier: script
sources: [L38-39_App_HWQ1.Rmd, L38&39P Model Adequacy.txt]
---
# Examples: Model Adequacy

See also: [model-adequacy](../concepts/model-adequacy.md), [regression-r](../r-code/regression-r.md)

---

## Quick-Reference: Model Adequacy Checks

```r
fit <- lm(y ~ x, data = df)

# R² and adjusted R²
summary(fit)$r.squared
summary(fit)$adj.r.squared

# SS decomposition
anova(fit)   # anova: x row = SS_Reg, Residuals row = SS_Res

# Residuals
resid(fit)           # raw residuals e_i = y_i - y-hat_i
rstandard(fit)       # standardized residuals
rstudent(fit)        # studentized (externally standardized) — better for outliers

# Residual plots (base R)
plot(fit)            # 4 plots: Residuals vs Fitted, QQ, Scale-Location, Cook's D

# Influential observations
cooks.distance(fit)  # Cook's D: >0.5 worth investigating, >1 almost certainly influential

# Normality test
shapiro.test(resid(fit))   # p < 0.05 → reject normality
```

---

## Q1 — NFL QB Rating (SLR, Model Adequacy)

**Problem:** n = 32 QBs, 2008 season. y = QB rating, x = yards per attempt. Fit SLR and assess model adequacy.

**Data (inline):**
```r
df <- tibble(
  x = c(8.39, 7.67, 7.66, 7.98, 7.21, 7.53, 8.01, 7.66, 7.21, 7.16,
        7.93, 7.10, 6.33, 6.76, 6.86, 7.35, 7.22, 7.94, 6.41, 6.77,
        6.65, 6.94, 6.45, 7.04, 6.39, 6.58, 6.21, 7.17, 6.34, 6.18,
        5.12, 5.71),
  y = c(105.5, 97.4, 96.9, 96.2, 95.0, 93.8, 92.7, 91.4, 90.2, 89.4,
         87.7, 87.5, 87.0, 86.4, 86.4, 86.0, 85.4, 84.7, 84.3, 81.7,
         81.0, 80.3, 80.2, 80.1, 79.6, 77.1, 76.0, 73.7, 72.6, 71.4,
         70.0, 66.5)
)
fit <- lm(y ~ x, data = df)
n <- 32; df_resid <- 30
```

---

### (a)–(b) Calculate R² and Interpret

**Formula:** R² = SS_Reg / SS_T

**From `anova(fit)` (compute yourself):**
```r
anova_tbl <- anova(fit)
SS_Reg    <- anova_tbl["x", "Sum Sq"]
SS_Res    <- anova_tbl["Residuals", "Sum Sq"]
SS_T      <- SS_Reg + SS_Res
R2        <- SS_Reg / SS_T
```

**Or read directly:**
```r
summary(fit)$r.squared
```

**Teacher-language interpretation:**
> "The simple linear regression model using yards per attempt explains approximately **[R² × 100]%** of the variability in NFL quarterback ratings. The remaining **[100 − R² × 100]%** is due to other factors not captured by this model."

---

### (c) Normal Probability Plot of Residuals

```r
# ggplot QQ plot
ggplot(tibble(e = resid(fit)), aes(sample = e)) +
  stat_qq(size = 2.5, color = "steelblue") +
  stat_qq_line(color = "red", linewidth = 1) +
  labs(title = "Normal Probability Plot of Residuals",
       x = "Theoretical quantiles", y = "Sample residuals") +
  theme_bw()
```

**How to read:**
- Points closely following the diagonal line → residuals are approximately normal
- S-shaped curve → skewness
- Tails bowing off line → outliers or heavy tails

---

### (d) Is Normality Assumption Satisfied?

**Formal test (Shapiro-Wilk):**
```r
sw <- shapiro.test(resid(fit))
sw$statistic   # W
sw$p.value     # p > 0.05 → fail to reject normality
```

**Decision rule:** Reject normality if p < 0.05.

**Teacher-language answer (when normality holds):**
> "Yes — the normality assumption appears to be satisfied. The normal probability plot shows points tracking the reference line, and the Shapiro-Wilk test (W = [W], p = [p]) provides no evidence against normality."

**Teacher-language answer (when normality fails):**
> "No — the normality assumption appears to be violated. The normal probability plot shows systematic departure from the reference line (e.g., S-shape / heavy tails). The Shapiro-Wilk test (p = [p] < 0.05) confirms this."

---

### (e) Residuals vs Fitted and vs x — Constant Variance?

```r
# Residuals vs fitted
ggplot(tibble(fitted = fitted(fit), e = resid(fit)),
       aes(x = fitted, y = e)) +
  geom_point(color = "steelblue") +
  geom_hline(yintercept = 0, color = "red", linetype = "dashed") +
  labs(x = "Fitted values", y = "Residuals") +
  theme_bw()

# Residuals vs x
ggplot(tibble(x = df$x, e = resid(fit)),
       aes(x = x, y = e)) +
  geom_point(color = "steelblue") +
  geom_hline(yintercept = 0, color = "red", linetype = "dashed") +
  labs(x = "x", y = "Residuals") +
  theme_bw()
```

**What to look for:**

| Pattern | Conclusion |
|---------|-----------|
| Random scatter around 0, constant width | Constant variance — assumption satisfied |
| Funnel (spread increases with fitted) | Non-constant variance — assumption violated |
| Curvature (U or arch) | Non-linearity — wrong model form |
| One point far from the rest | Potential outlier |

**Teacher-language answer (when variance is constant):**
> "Yes — the assumption of constant variance appears reasonable. The residuals are scattered randomly around zero across the full range of fitted values and x values with no systematic pattern."

**Teacher-language answer (when variance is not constant):**
> "No — the residual plot shows a [funnel/systematic] pattern, suggesting non-constant variance."

---

## Residual Types — When to Use Which

| Type | R function | Use case |
|------|-----------|----------|
| Raw residuals | `resid(fit)` | Basic checks, interpretable units |
| Standardized | `rstandard(fit)` | Compare across models; ≈ z-score |
| Studentized (externally) | `rstudent(fit)` | Better outlier detection; adjusts for leverage |

**Rule of thumb:** |studentized residual| > 3 → potential outlier worth investigating.

---

## Cook's Distance — Influential Points

```r
D <- cooks.distance(fit)
plot(D, type = "h")
abline(h = c(0.5, 1), col = c("orange", "red"), lty = 2)
```

| D_i threshold | Interpretation |
|---------------|---------------|
| D_i < 0.5 | Not influential |
| 0.5 ≤ D_i < 1 | Worth investigating |
| D_i ≥ 1 | Almost certainly influential — consider removing and re-fitting |

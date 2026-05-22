---
tags: [concept, section-3]
tier: procedure
sources: [L34-35P, L34-35_Study_Sheet.Rmd, Section3_Study_Guide.Rmd]
---
# Hypothesis Testing in Regression

## In Plain English
Two main tests: (1) **t-test** on individual coefficients — is one predictor significant? (2) **F-test** — is the overall model significant (any predictor useful at all)?

---

## t-Test on Individual Coefficient βⱼ

**H₀:** βⱼ = β_{j,0} vs H₁: βⱼ ≠ β_{j,0} (or one-sided)

$$T_0 = \frac{\hat{\beta}_j - \beta_{j,0}}{se(\hat{\beta}_j)}, \quad T_0 \sim t(n-p)$$

where p = number of parameters (intercept + number of predictors), so df = n − p.
- SLR: df = n − 2
- MLR with k predictors: df = n − k − 1

| H₁ | Reject H₀ if |
|----|--------------|
| βⱼ ≠ β_{j,0} | \|T₀\| > t_{α/2, n−p} |
| βⱼ > β_{j,0} | T₀ > t_{α, n−p} |
| βⱼ < β_{j,0} | T₀ < −t_{α, n−p} |

> **CRITICAL WARNING:** The `t value` column in `summary()$coefficients` **ALWAYS tests H₀: βⱼ = 0**. If the null is anything other than 0, you **must** compute T₀ manually.

```r
# Standard case (null = 0): read directly
summary(fit)$coefficients["x", "t value"]

# Non-zero null (e.g., H₀: β₁ = -30):
t0 <- (coef(fit)["x"] - (-30)) / summary(fit)$coefficients["x", "Std. Error"]

# One-sided critical value (α = 0.025, one-sided upper):
qt(0.975, df = n - 2)   # same as two-sided at α = 0.05

# Two-sided critical value (α = 0.05):
qt(0.975, df = n - 2)   # = qt(1 - 0.05/2, df)
```

**Reading the summary table:**
```
             Estimate  Std. Error  t value  Pr(>|t|)
(Intercept)  2627.82     44.18     59.49    < 2e-16
x             -37.15      2.55    -14.57    < 2e-16
```
- β̂₁ = −37.15, se = 2.55, t₀ = −37.15/2.55 = −14.57
- T₀ = Estimate / Std. Error (always — verify this is consistent)

**Recovering a missing column:**
| Known | Missing | Formula |
|-------|---------|---------|
| Estimate, Std. Error | t value | T₀ = Est / SE |
| Estimate, t value | Std. Error | SE = Est / T₀ |
| t value, df | p-value | `2*pt(-abs(t0), df)` |

---

## F-Test: Overall Significance of Regression

**H₀:** β₁ = β₂ = … = βₖ = 0 (no linear relationship, model has no value)  
**H₁:** At least one βⱼ ≠ 0

$$F_0 = \frac{MSR}{MSE} = \frac{SSR/k}{SSE/(n-p)}, \quad F_0 \sim F(k,\; n-p)$$

Reject H₀ if F₀ > F_{α, k, n−p}

**Teacher's phrasing when rejecting:**
> "The regression model is significant at α = X. There is sufficient evidence that at least one of the regression coefficients is nonzero."

**ANOVA table structure:**
```
Source      Df     Sum Sq    Mean Sq   F value   Pr(>F)
x (SLR)     1      SSR       MSR       F₀        p
Residuals   n-2    SSE       MSE
```
For MLR: each predictor gets its own row (sequential SS). **Use `summary(fit)$fstatistic` for overall F in MLR.**

**Completing a partial ANOVA table — key relationships:**
$$SST = SSR + SSE$$
$$MSR = SSR/k, \quad MSE = SSE/(n-p)$$
$$F_0 = MSR/MSE, \quad R^2 = SSR/SST$$
$$R^2_{adj} = 1 - \frac{MSE}{SST/(n-1)}$$

```r
fit %>% anova() %>% print()          # full ANOVA table

# SLR: extract from anova()
anova(fit)["x", "Sum Sq"]            # SSR
anova(fit)["Residuals", "Sum Sq"]    # SSE
anova(fit)["Residuals", "Mean Sq"]   # MSE

# MLR: overall F from summary (NOT individual anova rows)
f_info <- summary(fit)$fstatistic
pf(f_info[1], f_info[2], f_info[3], lower.tail = FALSE)  # overall p-value

# MLR: total SSR = sum all non-Residual rows
a <- anova(fit)
SSR_total <- sum(a[1:(nrow(a)-1), "Sum Sq"])
```

> **MLR Trap:** In `anova()`, each predictor row shows *sequential* (Type I) SS — the contribution of adding that predictor given the ones already in the model. These do NOT sum to the overall significance. For overall model significance, always use `summary(fit)$fstatistic`.

---

## Coefficient of Determination R²

$$R^2 = \frac{SSR}{SST}, \qquad R^2_{adj} = 1 - \frac{SSE/(n-p)}{SST/(n-1)}$$

- R² increases whenever a predictor is added (even if useless)
- R²_adj penalizes for extra predictors — use when comparing models with different numbers of predictors
- **Teacher's phrasing:** "X% of the variation in [Y] is explained by the regression model."

```r
summary(fit)$r.squared        # R²
summary(fit)$adj.r.squared    # R²_adj
```

---

## Worked Example Pattern (Rocket Motor Strength, n=20, df=18)

**Standard test (null = 0):** Read `t value` and `Pr(>|t|)` directly.  
→ β̂₁ = −37.15, t₀ = −14.57, p < 0.001 → Reject H₀ at any α

**Non-standard test (null = −30):**
$$T_0 = \frac{-37.15 - (-30)}{2.55} = \frac{-7.15}{2.55} = -2.80$$
→ |T₀| = 2.80 > t_{0.05, 18} = 1.734 → Reject H₀ at α = 0.10

**One-sided test (H₁: β₀ > 2500):**
$$T_0 = \frac{2627.82 - 2500}{44.18} = 2.89 > t_{0.025, 18} = 2.101 \Rightarrow \text{Reject } H_0$$

---

## Key Assumptions
Same as [regression-slr](regression-slr.md) — normality, constant variance, independence, linearity.

## Common Mistakes
- Using `t value` from summary table for non-zero null hypotheses
- Using individual `anova()` F-values for overall MLR significance test
- Wrong df: SLR df = n−2; MLR with k predictors df = n−k−1

## Project Context — Coffee Bean Production Analysis

The coffee project uses MLR with k = 4 predictors (temp, rainfall, population, oil_price). Key HT applications:

- **Individual β t-tests** determine which factors are statistically significant predictors of production. With df_error ≈ 1495, t critical values are ≈ ±1.96 (effectively z).
- **Panel fixed effects** (country + year dummy terms) are added as additional predictors. Each dummy gets its own β and t-test row in the summary table. These are not the primary predictors of interest but control for unobserved heterogeneity.
- The `statsmodels` Python ANOVA table uses the same F₀ = MSR/MSE logic; column name `PR(>F)` = p-value.
- **Non-zero null:** If testing whether, say, β_rainfall > 0.5, compute T₀ = (β̂_rainfall − 0.5) / SE manually — the software t-column always tests null = 0.

## Related
- [regression-slr](regression-slr.md)
- [regression-mlr](regression-mlr.md)
- [regression-ci](regression-ci.md)
- [which-test](which-test.md)
- [hypothesis-testing-overview](hypothesis-testing-overview.md) — regression t-tests and F-test follow the same 7-step framework
- [ss-decomposition](ss-decomposition.md) — F-test numerator and denominator both come from the SS partition

---
tags: [concept, section-3]
tier: procedure
sources: [L32-33P, Section3_Study_Guide.Rmd]
---
# Multiple Linear Regression (MLR)

## In Plain English
MLR extends SLR to multiple predictors. The model finds the plane (or hyperplane) that best fits the data in the least-squares sense. Each coefficient β̂ⱼ represents the change in mean Y per unit increase in xⱼ, **holding all other predictors constant**.

## Model

$$Y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_k x_k + \varepsilon$$

Matrix notation (n observations, k predictors, p = k+1 parameters):
$$\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$$

**Design matrix X:** n × p, first column all 1s (for intercept).

## Least Squares Estimator
$$\hat{\boldsymbol{\beta}} = (\mathbf{X}'\mathbf{X})^{-1}\mathbf{X}'\mathbf{y}$$

## Variance-Covariance Matrix
$$\text{Var}(\hat{\boldsymbol{\beta}}) = \sigma^2 (\mathbf{X}'\mathbf{X})^{-1}$$

$$se(\hat{\beta}_j) = \sqrt{MSE \cdot C_{jj}}$$

where C_{jj} is the j-th diagonal of (X'X)⁻¹.

## ANOVA Decomposition (MLR)

| Source | df | SS |
|--------|----|----|
| Regression | k | SSR |
| Error | n − p = n − k − 1 | SSE |
| Total | n − 1 | SST |

$$MSE = \frac{SSE}{n-p}, \quad R^2 = \frac{SSR}{SST}, \quad R^2_{adj} = 1 - \frac{MSE}{SST/(n-1)}$$

**Use R²_adj (not R²) when comparing models** — R² always increases when a predictor is added.

## Key MLR df Rule
$$df_{resid} = n - k - 1 = n - p$$

| n | k | df_resid |
|---|---|----------|
| 20 | 1 (SLR) | 18 |
| 9 | 2 | 6 |
| 21 | 3 | 17 |
| 32 | 5 | 26 |

## R Code

```r
# Fit
fit <- lm(y ~ x1 + x2, data = df)

# Full output
fit %>% summary() %>% print()      # R², adj R², F, all t-tests
fit %>% anova() %>% print()        # ANOVA table (sequential SS)

# Extract individual values
coef(fit)                           # all β̂ estimates
sqrt(diag(vcov(fit)))               # se(β̂ⱼ) for all j
summary(fit)$r.squared              # R²
summary(fit)$adj.r.squared          # R²_adj
summary(fit)$sigma^2                # MSE = σ̂²
summary(fit)$sigma                  # σ̂ = √MSE (Residual SE)

# Overall F-test (correct for both SLR and MLR)
f_info <- summary(fit)$fstatistic
pf(f_info[1], f_info[2], f_info[3], lower.tail = FALSE)

# Total SSR for MLR (sum all non-Residuals rows)
a <- anova(fit)
SSR <- sum(a[1:(nrow(a)-1), "Sum Sq"])
SSE <- a["Residuals", "Sum Sq"]
```

## Interaction Terms

When the effect of x₁ on Y depends on x₂ (or vice versa), add an interaction term:

```r
df <- df %>% mutate(x1x2 = x1 * x2)
fit_interact <- lm(y ~ x1x2, data = df)
# OR
fit_interact <- lm(y ~ x1 * x2, data = df)    # includes x1, x2, and x1:x2
```

**Interpretation:** β̂ on x1x2 represents how the slope for x1 changes per unit increase in x2.

## Common MLR Traps

| Trap | Correct Approach |
|------|-----------------|
| Reading overall F from `anova()` row in MLR | Use `summary(fit)$fstatistic` for overall F |
| Comparing models with R² | Use R²_adj instead |
| Forgetting to update df when adding predictors | df_resid = n − k − 1 |
| Omitting intercept | Only if theory requires — R default includes it |

> **MLR anova() note:** Each predictor row shows *sequential* (Type I) SS — contribution of that predictor **given the ones already in the model**. Not the same as the overall F-test. For the overall test, use `summary(fit)$fstatistic`.

## Key Assumptions
Same as SLR — normality, constant variance, independence, linearity. MLR also assumes:
- **No perfect multicollinearity** (predictors should not be exact linear combinations of each other)
- Each coefficient interpretation holds only when all other predictors are held constant

## Project Context — Coffee Bean Production Analysis

The coffee project (`Project/`) applies MLR to panel data (~50 countries × ~30 years, n ≈ 1500 rows) analyzing whether temperature, rainfall, population, and oil price predict coffee bean production and export revenue.

**Primary model:**
```r
fit <- lm(production ~ temp + rainfall + population + oil_price, data = coffee)
```

- **df_error ≈ 1495** (n ≈ 1500, k = 4 predictors → df = 1500 − 4 − 1)
- **F-test df = (4, ~1495)** for the overall model
- **Use R²_adj** — comparing models with different subsets of the 4 predictors
- **Panel fixed effects** (country + year dummy terms) add to k; recompute df accordingly
- `statsmodels.formula.api.ols` (Python) maps to `lm()` in R — ANOVA table structure is identical; column names differ

**Known data issue:** Production (Y) is right-skewed. Expect fan-shaped residuals on raw data → log-transform Y before modeling. See [model-adequacy](model-adequacy.md) for diagnostic approach.

## Related
- [regression-slr](regression-slr.md)
- [regression-ht](regression-ht.md)
- [regression-ci](regression-ci.md)
- [model-adequacy](model-adequacy.md)
- [fwl-theorem](fwl-theorem.md) — the theorem that justifies partial regression coefficients
- [ss-decomposition](ss-decomposition.md) — R² and the ANOVA table structure derive from this identity

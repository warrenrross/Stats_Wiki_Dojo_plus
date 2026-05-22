---
tags: [concept, unit-3]
tier: procedure
sources: [L31P, Section3_Study_Guide.Rmd]
---
# Simple Linear Regression (SLR)

## In Plain English
SLR models the relationship between one predictor x and one response Y as a straight line. You find the line that minimizes the sum of squared vertical distances from the data points to the line (least squares).

## Model
$$Y = \beta_0 + \beta_1 x + \varepsilon, \quad \varepsilon \sim N(0, \sigma^2)$$

| Symbol | Meaning |
|--------|---------|
| β₀ | y-intercept (value of Y when x = 0) |
| β₁ | slope (change in mean Y per unit increase in x) |
| ε | random error — captures everything x doesn't explain |

## Least Squares Estimates

$$\hat{\beta}_1 = \frac{S_{xy}}{S_{xx}}, \qquad \hat{\beta}_0 = \bar{y} - \hat{\beta}_1\bar{x}$$

**Corrected sums:**
$$S_{xx} = \sum x_i^2 - \frac{(\sum x_i)^2}{n}, \qquad S_{xy} = \sum x_i y_i - \frac{(\sum x_i)(\sum y_i)}{n}$$

## Fitted Values and Residuals
$$\hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x_i, \qquad e_i = y_i - \hat{y}_i$$

## Sum of Squares Decomposition

| Source | Symbol | Formula | df |
|--------|--------|---------|-----|
| Total | SST | Σ(yᵢ − ȳ)² | n−1 |
| Regression | SSR | β̂₁ · S_{xy} | 1 |
| Error | SSE | SST − SSR | n−2 |

$$MSE = \frac{SSE}{n-2} \approx \sigma^2$$

## R² (Coefficient of Determination)
$$R^2 = \frac{SSR}{SST} = 1 - \frac{SSE}{SST}$$
**Teacher's phrasing:** "X% of the variation in [Y] is explained by the regression model."

## Standard Errors of Estimates
$$se(\hat{\beta}_1) = \sqrt{\frac{MSE}{S_{xx}}}, \qquad se(\hat{\beta}_0) = \sqrt{MSE\!\left(\frac{1}{n} + \frac{\bar{x}^2}{S_{xx}}\right)}$$

## F-Test: Overall Significance of Regression
**H₀:** β₁ = 0 (no linear relationship)  
**H₁:** β₁ ≠ 0

$$F_0 = \frac{MSR}{MSE} = \frac{SSR/1}{SSE/(n-2)}, \quad \text{df: } 1,\; n-2$$

Reject H₀ if F₀ > F_{α,1,n−2}

**Teacher's phrasing when rejecting:** "The regression model is significant at α = X. There is sufficient evidence that β₁ ≠ 0 (i.e., x is a significant predictor of Y)."

## t-Test: Individual Coefficient
**H₀:** βⱼ = β_{j,0} (often 0)

$$T_0 = \frac{\hat{\beta}_j - \beta_{j,0}}{se(\hat{\beta}_j)}, \quad \text{df} = n-2$$

> **Critical trap:** The `t value` column in `summary()$coefficients` **always tests H₀: β = 0**. For any other null, compute T₀ manually: `t0 = (b_hat - null_value) / se`

## R Code

```r
fit <- lm(y ~ x, data = df)

fit %>% anova() %>% print()         # SSR, SSE, MSE, F, p-value
fit %>% summary() %>% print()       # estimates, SEs, t-values, R²

coef(fit)["x"]                      # β̂₁
coef(fit)["(Intercept)"]            # β̂₀
summary(fit)$coefficients["x", "Std. Error"]    # se(β̂₁)
summary(fit)$r.squared              # R²
summary(fit)$sigma^2                # MSE (= σ̂²)
anova(fit)["Residuals", "Mean Sq"]  # MSE (same)
```

## Key Assumptions
- Linearity: true relationship is linear in x
- Constant variance (homoscedasticity): σ² doesn't change with x
- Independence of errors
- Normality of errors: ε ~ N(0, σ²)

Check these with residual plots — see [model-adequacy](model-adequacy.md).

## Common Mistakes
- Reading `t value` for a non-zero null (must compute manually)
- Confusing F-test df: it's (1, n−2) for SLR not (1, n−1)
- Forgetting that SSR = β̂₁ · S_{xy} for SLR

## Related
- [regression-mlr](regression-mlr.md)
- [regression-ht](regression-ht.md)
- [regression-ci](regression-ci.md)
- [model-adequacy](model-adequacy.md)
- [standard-error](standard-error.md) — SE(β̂₁) = √(MSE/S_xx) is an instance of the universal SE construct
- [ss-decomposition](ss-decomposition.md) — the SS identity underlying the ANOVA table

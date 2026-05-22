---
tags: [concept, section-3]
tier: procedure
sources: [L36-37P, L36-37_Study_Guide.Rmd, Section3_Study_Guide.Rmd]
---
# Confidence & Prediction Intervals in Regression

## The Three Intervals

| Interval | Question | R Argument |
|----------|----------|------------|
| CI on β̂ⱼ | Where is the true coefficient? | `confint(fit)` |
| CI on mean response | Where is the true mean Y at x₀? | `interval = "confidence"` |
| PI on future observation | Where will a single new Y fall at x₀? | `interval = "prediction"` |

**Key rule: PI is ALWAYS wider than CI on mean response at the same x₀.**

---

## Degrees of Freedom Reference

| Model | df (residuals) | p (# parameters) |
|-------|----------------|-------------------|
| SLR (1 predictor) | n − 2 | 2 |
| MLR, k predictors | n − k − 1 | k + 1 |

**Quick check:** df = Residuals row, Df column in `anova()` output.

---

## 1. CI on a Regression Coefficient βⱼ

$$\hat{\beta}_j \pm t_{\alpha/2,\; n-p} \cdot se(\hat{\beta}_j)$$

```r
confint(fit, level = 0.95)   # columns: "2.5 %" and "97.5 %"
```

**Column names depend on confidence level — this is the #1 trap:**

| Level | Lower Column | Upper Column |
|-------|-------------|-------------|
| 90% | `"5 %"` | `"95 %"` |
| 95% | `"2.5 %"` | `"97.5 %"` |
| 99% | `"0.5 %"` | `"99.5 %"` |

```r
ci <- confint(fit, level = 0.95)
ci["x1", "2.5 %"]    # lower bound on β₁ at 95%
ci["x1", "97.5 %"]   # upper bound on β₁ at 95%
ci["(Intercept)", "2.5 %"]   # β₀ lower
```

**Reading the CI to make a decision:** If 0 is NOT in the interval → reject H₀: βⱼ = 0.

**Back-calculating from CI bounds:**
$$\hat{\beta}_j = \frac{L + U}{2}, \qquad se(\hat{\beta}_j) = \frac{(U-L)/2}{t_{\alpha/2, n-p}}$$

---

## 2. CI on Mean Response at x₀

**SLR formula:**
$$\hat{y}_0 \pm t_{\alpha/2,\; n-2} \cdot \sqrt{MSE\left[\frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}}\right]}$$

- Narrowest at x₀ = x̄; widens as x₀ moves away from center of data

**MLR formula:**
$$\hat{y}_0 \pm t_{\alpha/2,\; n-p} \cdot \sqrt{MSE \cdot \mathbf{x}_0'(\mathbf{X}'\mathbf{X})^{-1}\mathbf{x}_0}$$

```r
ci_mean <- fit %>%
  predict(newdata = data.frame(x = 30), interval = "confidence", level = 0.95)
ci_mean[, "fit"]   # ŷ₀
ci_mean[, "lwr"]   # lower bound
ci_mean[, "upr"]   # upper bound

# MLR:
predict(fit, newdata = data.frame(x1 = 30, x2 = 4), interval = "confidence", level = 0.99)
```

**Teacher's phrasing:**
> "We are 95% confident that the true mean [Y in context] at x = [x₀] is between [lwr] and [upr]."

---

## 3. Prediction Interval (PI) on a Future Observation

**SLR formula:**
$$\hat{y}_0 \pm t_{\alpha/2,\; n-2} \cdot \sqrt{MSE\left[1 + \frac{1}{n} + \frac{(x_0 - \bar{x})^2}{S_{xx}}\right]}$$

**The only difference from CI: the extra +1 inside the square root.**  
That extra MSE·1 term accounts for individual observation scatter.

```r
pi_obs <- fit %>%
  predict(newdata = data.frame(x = 30), interval = "prediction", level = 0.95)
pi_obs[, "lwr"]   # lower bound
pi_obs[, "upr"]   # upper bound
```

**Teacher's phrasing:**
> "We are 95% confident that a single new observation of [Y in context] at x = [x₀] will fall between [lwr] and [upr]."

---

## CI vs PI Side-by-Side

| Feature | CI on Mean | PI on Future Obs |
|---------|-----------|-----------------|
| Covers | True mean μ_{Y\|x₀} | Single new Y₀ |
| SE includes | Parameter uncertainty only | + natural scatter of Y |
| Width | Narrower | **Always wider** |
| Point estimate | Same (ŷ₀) | Same (ŷ₀) |
| As n → ∞ | Width → 0 | Width → 2t·√MSE (never zero) |

---

## Reading `predict()` Output

```
    fit      lwr      upr
1  267.3   241.7   292.9
```
- ŷ₀ = 267.3
- Half-width = (292.9 − 241.7)/2 = 25.6
- Back-calculate SE: SE = half-width / t_{α/2, df}

---

## Extrapolation Warning
- SLR: check x₀ ∈ [min(xᵢ), max(xᵢ)]
- MLR: individual ranges can look fine but the joint region may be violated — R won't warn you

---

## df Quick Reference (from homework)
| Homework | n | k | df_resid |
|----------|---|---|----------|
| Fretting Wear (Q1) | 9 | 1 | 7 |
| Rocket Motor (Q2) | 20 | 1 | 18 |
| Toenail Arsenic (Q3) | 21 | 3 | 17 |
| Optical Correlator (Q4) | 9 | 2 | 6 |
| Coal Density (Q5) | 11 | 2 | 8 |
| Chemical Plant (Q6) | 12 | 4 | 7 |

## Common Mistakes
- Wrong column name in `confint()` — check level-specific column name
- Confusing CI (mean) with PI (individual) — PI is always wider
- Wrong df for t-critical value
- Extrapolating without checking x₀ is in range

## Related
- [regression-slr](regression-slr.md)
- [regression-ht](regression-ht.md)
- [regression-mlr](regression-mlr.md)
- [model-adequacy](model-adequacy.md)
- [confidence-intervals](confidence-intervals.md) — CI on βⱼ is an instance of the universal Estimate ± Score × SE structure
- [standard-error](standard-error.md) — SE(β̂ⱼ) that enters the CI formula is defined in the universal SE reference

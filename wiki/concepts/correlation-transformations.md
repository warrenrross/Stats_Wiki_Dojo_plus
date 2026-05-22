---
tags: [concept, unit-3]
tier: procedure
sources: [L40-41P, Section3_Study_Guide.Rmd]
---
# Correlation and Transformations

## Pearson Correlation Coefficient r

$$\hat{\rho} = r = \frac{S_{xy}}{\sqrt{S_{xx} \cdot S_{yy}}}$$

| Symbol | Meaning |
|--------|---------|
| S_{xy} | Σ(xᵢ−x̄)(yᵢ−ȳ) = Σxᵢyᵢ − nx̄ȳ |
| S_{xx} | Σ(xᵢ−x̄)² |
| S_{yy} | Σ(yᵢ−ȳ)² = SST |

**Properties:**
- Range: −1 ≤ r ≤ 1
- r = +1: perfect positive linear relationship
- r = −1: perfect negative linear relationship
- r = 0: no linear relationship (may still have nonlinear relationship)
- **SLR only:** R² = r²

## Hypothesis Test: H₀: ρ = 0

$$T_0 = r\sqrt{\frac{n-2}{1-r^2}}, \quad T_0 \sim t(n-2)$$

This test is **mathematically equivalent to the t-test on β₁** in SLR. If there is significant correlation, there is a significant linear relationship (and vice versa).

**p-value:** `2 * pt(-abs(T0), df = n-2)`

**No-data workflow:** When r and n are given directly (no dataset), skip `lm()` entirely — set r and n as scalars and apply the formula above. Do not try to reconstruct raw data.

```r
r  <- 0.83          # given sample correlation
n  <- 25            # given sample size
T0 <- r * sqrt((n - 2) / (1 - r^2))
p_val <- 2 * pt(-abs(T0), df = n - 2)

cor(df$x, df$y)            # sample correlation r from data
cor.test(df$x, df$y)       # full hypothesis test: t stat, p-value, 95% CI on ρ
```

---

## Fisher Z-Transform: H₀: ρ = ρ₀ (Non-Zero Null)

Use when comparing correlation strength to a specific non-zero reference value (e.g., "is the correlation at least 0.5?"). The T₀ above is only valid for H₀: ρ = 0; for any other null, use the Fisher Z-transform.

**Transform:** $Z = \text{arctanh}(r) = \frac{1}{2}\ln\!\left(\frac{1+r}{1-r}\right)$

**Test statistic (eq. 11.49/11.50):**
$$Z_0 = \left(\text{arctanh}(\hat{r}) - \text{arctanh}(\rho_0)\right)\sqrt{n-3} \sim N(0,1)$$

Compare Z₀ to z_{α/2} = 1.96 (for two-sided α = 0.05).

**p-value:** `2 * pnorm(-abs(Z0))`

> **Rounding instruction:** Some textbook problems specify "use z-values rounded to two decimal places." This means round arctanh(r) and arctanh(ρ₀) to 2 decimal places **before** computing Z₀ or CI bounds — it changes numerical answers materially.

---

## Confidence Interval on ρ (Fisher Z-Transform)

$$\text{CI on }\rho: \quad \tanh\!\left(\text{arctanh}(\hat{r}) \pm \frac{z_{\alpha/2}}{\sqrt{n-3}}\right)$$

Steps:
1. Compute $w = \text{arctanh}(r)$
2. Form bounds: $w \pm 1.96/\sqrt{n-3}$
3. Back-transform: $\rho_{L,U} = \tanh(\text{bound})$

**Note:** This CI is on ρ itself, not on Z. The CI from `cor.test()` uses this same Fisher Z method.

```r
r  <- 0.83
n  <- 25
rho0 <- 0.5       # non-zero null value

# Fisher Z transform
w    <- atanh(r)          # arctanh(r) — R function
w0   <- atanh(rho0)       # arctanh(ρ₀)

# Test statistic for H₀: ρ = ρ₀
Z0   <- (w - w0) * sqrt(n - 3)
p_val_fisher <- 2 * pnorm(-abs(Z0))

# 95% CI on ρ
margin <- 1.96 / sqrt(n - 3)
CI_low  <- tanh(w - margin)   # tanh = back-transform
CI_high <- tanh(w + margin)
```

**Which p-value formula to use:**

| Null hypothesis | Test statistic | p-value formula |
|-----------------|----------------|-----------------|
| H₀: ρ = 0 | T₀ ~ t(n−2) | `2 * pt(-abs(T0), n-2)` |
| H₀: ρ = ρ₀ (ρ₀ ≠ 0) | Z₀ ~ N(0,1) | `2 * pnorm(-abs(Z0))` |

---

## When to Transform

Transformations are needed when residual plots reveal violations of regression assumptions:
- **Non-linearity** (curved residual pattern) → transform x or y
- **Non-constant variance** (fan shape) → transform y

**How to choose:** Look at the scatter plot of y vs x and the residual plot. The shape of the relationship suggests what transformation works.

---

## Common Transformations and When to Use Them

| Original Relationship | Transform | Linearized Model |
|----------------------|-----------|-----------------|
| Y = β₀ eˢ¹ˣ (exponential) | Y* = ln(Y) | Y* = ln(β₀) + β₁x |
| Y = β₀ xᵝ¹ (power) | Y* = ln(Y), x* = ln(x) | Y* = ln(β₀) + β₁x* |
| Y = β₀ + β₁ ln(x) (log-linear) | x* = ln(x) | Y = β₀ + β₁x* |
| Y = β₀ + β₁/x (reciprocal) | x* = 1/x | Y = β₀ + β₁x* |
| Y = β₀ + β₁√x (square root) | x* = √x | Y = β₀ + β₁x* |

**Key caution:** Back-transforming predictions: if you transformed Y → ln(Y), the prediction is ln(ŷ). To get ŷ in original units: `exp(predicted value)`. Note this is an estimate of the **median** (not mean) of the original-scale distribution.

---

## R Code for Transformations

```r
df <- df %>% mutate(
  log_y  = log(y),      # natural log of y
  log_x  = log(x),      # natural log of x
  inv_x  = 1/x,         # reciprocal of x
  sqrt_x = sqrt(x),     # square root of x
  sq_x   = x^2          # polynomial term
)

# Fit transformed model:
fit_log <- lm(log_y ~ x, data = df)
summary(fit_log)

# Back-transform prediction:
x0 <- 30
pred_log <- predict(fit_log, newdata = data.frame(x = x0))
pred_original_scale <- exp(pred_log)
```

---

## Choosing the Right Transformation

**Step 1:** Plot y vs x → what is the shape?
- Concave up (increasing rate) → try ln(x) or √x on x
- Exponential growth → try ln(y) on y
- Power relationship → try ln(y) and ln(x) both

**Step 2:** Fit the transformed model and check residual plots
- Are residuals now random? Constant spread? Normal Q-Q good?
- If yes → transformation worked

**Step 3:** Verify R² improved and residual pattern resolved

---

## Teacher's Phrasing for Correlation

**Significant correlation:** "Because p-value = [X] < α = [X], we reject H₀: ρ = 0. There is sufficient evidence of a significant linear relationship between [X] and [Y]."

**Non-significant:** "Because p-value = [X] > α = [X], we fail to reject H₀: ρ = 0. There is insufficient evidence of a significant linear relationship."

## Key Assumptions
- Pearson r measures only **linear** association — two variables can be strongly related but have r ≈ 0 if the relationship is nonlinear
- Both variables should be continuous

## Common Mistakes
- Concluding no relationship when r ≈ 0 (only means no linear relationship)
- Forgetting to back-transform predictions from a log model
- Comparing r² between a transformed and untransformed model (not valid comparison)

## Related
- [regression-slr](regression-slr.md)
- [model-adequacy](model-adequacy.md)
- [regression-ht](regression-ht.md)
- [distributions](distributions.md) — the Fisher Z statistic Z₀ ~ N(0,1) under H₀

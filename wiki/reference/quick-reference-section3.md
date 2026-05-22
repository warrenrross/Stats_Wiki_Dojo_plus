---
tags: [reference, units-3-4]
sources: [Exam3_Quick_Reference.pdf, wiki concepts]
---
# Section 3 Quick Reference

---

## Model Forms & Least Squares

**SLR:** $Y = \beta_0 + \beta_1 x + \varepsilon, \quad \varepsilon \sim N(0, \sigma^2)$

**LSE:**
$$\hat{\beta}_1 = \frac{S_{xy}}{S_{xx}}, \qquad \hat{\beta}_0 = \bar{y} - \hat{\beta}_1\bar{x}$$

$$S_{xx} = \sum x_i^2 - \frac{(\sum x_i)^2}{n}, \qquad S_{xy} = \sum x_i y_i - \frac{(\sum x_i)(\sum y_i)}{n}$$

**SLR standard errors:**
$$se(\hat{\beta}_1) = \sqrt{\frac{MSE}{S_{xx}}}, \qquad se(\hat{\beta}_0) = \sqrt{MSE\!\left(\frac{1}{n} + \frac{\bar{x}^2}{S_{xx}}\right)}$$

**MLR:** $Y = \beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k + \varepsilon$

$$\hat{\boldsymbol{\beta}} = (\mathbf{X'X})^{-1}\mathbf{X'y}, \qquad se(\hat{\beta}_j) = \sqrt{MSE \cdot C_{jj}}$$

where $C_{jj}$ = j-th diagonal of $(\mathbf{X'X})^{-1}$

---

## ANOVA Table & R²

**p = k + 1** (# parameters = predictors + intercept)

| Source | df (SLR) | df (MLR) | SS | MS | F₀ |
|--------|----------|----------|----|----|----|
| Regression | 1 | k | SSR | MSR = SSR/k | F₀ = MSR/MSE |
| Residuals | n−2 | n−k−1 = n−p | SSE | MSE = SSE/(n−p) = σ̂² | |
| Total | n−1 | n−1 | SST = Σ(yᵢ−ȳ)² | | |

$$SST = SSR + SSE \qquad R^2 = \frac{SSR}{SST} \qquad R^2_{adj} = 1 - \frac{MSE}{SST/(n-1)} \qquad \hat{\sigma} = \sqrt{MSE}$$

---

## Summary Table (`summary(fit)$coefficients`)

```
             Estimate   Std.Error   t value   Pr(>|t|)
(Intercept)  β̂₀        se₀         t₀        p₀
x₁           β̂₁        se₁         t₁        p₁
x₂           β̂₂        se₂         t₂        p₂
```

| Want | Formula |
|------|---------|
| t value | Estimate / Std.Error |
| Std.Error | Estimate / t value |
| Estimate | t value × Std.Error |

> ⚠ **t value always tests H₀: β = 0 only.** For any other null: $T_0 = (\hat{\beta}_j - \beta_{j,0})\,/\,se(\hat{\beta}_j)$ — compute manually.

---

## Hypothesis Tests

**t-test on βⱼ:**
$$T_0 = \frac{\hat{\beta}_j - \beta_{j,0}}{se(\hat{\beta}_j)} \sim t(n-p)$$

| Test | Reject H₀ if | R critical value |
|------|-------------|-----------------|
| Two-sided ($H_1$: β ≠ β₀) | \|T₀\| > t_{α/2, n−p} | `qt(1-α/2, n-p)` |
| One-sided upper ($H_1$: β > β₀) | T₀ > t_{α, n−p} | `qt(1-α, n-p)` |
| One-sided lower ($H_1$: β < β₀) | T₀ < −t_{α, n−p} | `-qt(1-α, n-p)` |

**F-test (significance of regression):**
$$F_0 = MSR/MSE \sim F(k,\, n-p); \quad \text{reject if } F_0 > F_{\alpha,\,k,\,n-p} \;\to\; \texttt{qf(1-\alpha, k, n-p)}$$

> ⚠ **One-sided critical:** `qt(1-α, df)` — NOT `qt(1-α/2, df)`
> ⚠ **MLR overall F:** use `summary(fit)$fstatistic`, not `anova()` rows (anova shows sequential F per predictor, not the overall test)

---

## Confidence & Prediction Intervals

| Interval | Formula | R call |
|----------|---------|--------|
| CI on βⱼ | $\hat{\beta}_j \pm t_{\alpha/2,\,n-p} \cdot se(\hat{\beta}_j)$ | `confint(fit, level=)` |
| CI on mean at x₀ | $\hat{y}_0 \pm t_{\alpha/2,\,n-p}\sqrt{MSE \cdot \mathbf{x_0'(X'X)^{-1}x_0}}$ | `predict(fit, newdata, interval="confidence", level=)` |
| PI on future Y₀ | $\hat{y}_0 \pm t_{\alpha/2,\,n-p}\sqrt{MSE(1 + \mathbf{x_0'(X'X)^{-1}x_0})}$ | `predict(fit, newdata, interval="prediction", level=)` |

**PI > CI always** — the extra MSE·1 under √ accounts for individual observation scatter.

**df:** SLR → n−2; MLR with k predictors → n−k−1. Quick check: Residuals row, Df column in `anova()`.

---

## Model Adequacy

**Assumptions:** (1) E[εᵢ] = 0; (2) Var(εᵢ) = σ² (constant); (3) independent; (4) normal

**Residual plots:**

| Pattern in eᵢ vs ŷᵢ or xⱼ | Diagnosis |
|---------------------------|-----------|
| Random scatter around 0 | Assumptions OK |
| Fan/funnel (spread increases) | Non-constant variance — consider transform Y |
| Curve or arch | Nonlinearity — missing higher-order or cross term |
| Systematic time trend | Autocorrelation |

**Normal probability plot:** points on line → normal; bowed tails → heavy tails

**Unusual observations** (p = k + 1):

| Type | Rule | R function |
|------|------|-----------|
| Influential | Dᵢ > 4/n flag; Dᵢ > 0.5 investigate; Dᵢ > 1 refit without | `cooks.distance(fit)` |

**Deletion/refit:** remove flagged obs, refit, compare R² and σ̂² (MSE). Expect R² ↑ and MSE ↓ if the removed point was distorting the fit.

---

## Correlation

$$\hat{\rho} = \frac{S_{xy}}{\sqrt{S_{xx} \cdot S_{yy}}}; \qquad -1 \le \hat{\rho} \le 1; \qquad R^2 = \hat{\rho}^2 \text{ (SLR only)}$$

**Test H₀: ρ = 0:**
$$T_0 = \hat{\rho}\sqrt{\frac{n-2}{1-\hat{\rho}^2}} \sim t(n-2)$$

or read directly from `cor.test(df$x, df$y)`. Mathematically equivalent to t-test on β₁.

---

## Transformations to Linearize

| Nonlinear model | Apply | Then fit | Back-transform |
|-----------------|-------|----------|----------------|
| $Y = \beta_0 e^{\beta_1 x}$ | Y* = ln Y | Y* ~ x | exp(ŷ*) |
| $Y = \beta_0 x^{\beta_1}$ | Y* = ln Y, x* = ln x | Y* ~ x* | exp(ŷ*) |
| $Y = \beta_0 + \beta_1 \ln x$ | x* = ln x | Y ~ x* | none |
| $Y = \beta_0 + \beta_1/x$ | x* = 1/x | Y ~ x* | none |
| $Y = \beta_0 + \beta_1\sqrt{x}$ | x* = √x | Y ~ x* | none |

> **Caution:** back-transformed CI on log-Y model is a CI on the **median**, not the mean.

```r
df <- df %>% mutate(log_y=log(y), log_x=log(x), inv_x=1/x, sqrt_x=sqrt(x))
```

---

## Quick-Lookup: df and Critical Value Calls

| Situation | df | R critical value |
|-----------|----|-----------------|
| SLR t-test / CI | n−2 | `qt(1-α/2, n-2)` |
| MLR t-test / CI | n−k−1 | `qt(1-α/2, n-k-1)` |
| F-test (SLR) | num=1, den=n−2 | `qf(1-α, 1, n-2)` |
| F-test (MLR) | num=k, den=n−k−1 | `qf(1-α, k, n-k-1)` |
| Correlation test | n−2 | `qt(1-α/2, n-2)` |

**Common t critical values:**

| df | t_{0.100} (90% two-sided) | t_{0.050} (95% two-sided) | t_{0.010} (99% two-sided) |
|----|--------------------------|--------------------------|--------------------------|
| 10 | 1.812 | 2.228 | 3.169 |
| 15 | 1.753 | 2.131 | 2.947 |
| 18 | 1.734 | 2.101 | 2.878 |
| 20 | 1.725 | 2.086 | 2.845 |
| 22 | 1.717 | 2.074 | 2.819 |
| 25 | 1.708 | 2.060 | 2.787 |
| 30 | 1.697 | 2.042 | 2.750 |
| 40 | 1.684 | 2.021 | 2.704 |
| ∞  | 1.645 | 1.960 | 2.576 |

---

## Control Charts

### Western Electric (Out-of-Control) Rules

A process is **out of control** if any of:

| Rule | Signal |
|------|--------|
| 1 | One point beyond 3σ limits |
| 2 | 2 of 3 consecutive points beyond 2σ limits (same side) |
| 3 | 4 of 5 consecutive points beyond 1σ limits (same side) |
| 4 | 8 consecutive points on the same side of center line |
| 5 | 6 consecutive points steadily increasing or decreasing |

### Two Sigmas: σ_data vs σ_process

| Symbol | Meaning | Formula |
|--------|---------|---------|
| σ̂ (σ_data) | Estimated process std dev — spread of individual observations | R̄/d₂ or s̄/c₄ |
| σ̂/√n (σ_process) | Std dev of x̄ — spread of subgroup means; used implicitly in X̄ chart limits | σ̂/√n |

> X̄ chart limits: x̄̄ ± A₂R̄, where A₂ = 3/(d₂√n) encodes σ̂/√n

### PCR (Cp) vs PCRk (Cpk)

| Index | Formula | What it measures |
|-------|---------|-----------------|
| Cp (PCR) | (USL−LSL) / 6σ̂ | Spread only — assumes process is centered |
| Cpk (PCRk) | min[(USL−μ̂)/3σ̂, (μ̂−LSL)/3σ̂] | Spread AND centering |

- Cpk ≤ Cp always; Cpk = Cp only when process is perfectly centered
- **Cp overstates capability when process is off-center** — always report Cpk

| Value | Interpretation |
|-------|---------------|
| < 1.0 | Not capable |
| ≥ 1.0 | Barely capable |
| ≥ 1.33 | Capable |
| ≥ 1.67 | Highly capable |

### Attribute Chart Types

| Chart | Statistic | Distribution | When |
|-------|-----------|-------------|------|
| p-chart | p = proportion defective | Binomial | Binary (defective/not); n can vary |
| c-chart | c = count of defects | Poisson | Count data; fixed inspection unit |
| u-chart | u = defects per unit | Poisson | Count data; variable inspection unit |

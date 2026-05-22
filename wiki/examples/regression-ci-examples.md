---
tags: [example, section-3]
tier: script
sources: [L36-37_App_HWQ1.Rmd, L36-37_App_HWQ2.Rmd, L36-37_App_HWQ3.Rmd, L36-37_App_HWQ4.Rmd, L36-37_App_HWQ5.Rmd, L36-37_App_HWQ6.Rmd]
---
# Examples: Confidence and Prediction Intervals in Regression

See also: [regression-ci](../concepts/regression-ci.md), [regression-r](../r-code/regression-r.md)

---

## Quick-Reference: What R Gives You

```r
# CI on coefficients
confint(fit, level = 0.95)   # columns: "2.5 %"  "97.5 %"
confint(fit, level = 0.99)   # columns: "0.5 %"  "99.5 %"
confint(fit, level = 0.90)   # columns: "5 %"    "95 %"

# CI on mean response at x0
predict(fit, newdata = data.frame(x = x0), interval = "confidence", level = 0.95)
# returns: fit, lwr, upr

# PI on a single future observation at x0
predict(fit, newdata = data.frame(x = x0), interval = "prediction", level = 0.95)
# returns: fit, lwr, upr  — always WIDER than CI
```

**Column name rule for `confint()`:**

| Level | Lower col | Upper col |
|-------|-----------|-----------|
| 90%   | `5 %`     | `95 %`    |
| 95%   | `2.5 %`   | `97.5 %`  |
| 99%   | `0.5 %`   | `99.5 %`  |

**df for t-critical value:**
- SLR: `df = n − 2`
- MLR with k regressors: `df = n − k − 1` (same as residual df in R output)

---

## Q1 — Fretting Wear (SLR, 95% CI)

**Problem:** Fretting wear of mild steel. x = oil viscosity, y = wear volume (10⁻⁴ mm³). n observations. Find 95% CI on β₀, β₁, and mean wear at x = 30.

**Setup:**
```r
fit <- lm(y ~ x, data = df)
df_resid <- nrow(df) - 2   # SLR: df = n - 2
```

**Part (a)–(b): 95% CI on β₀ (Intercept)**
```r
ci <- confint(fit, level = 0.95)
# (a) lower: ci["(Intercept)", "2.5 %"]
# (b) upper: ci["(Intercept)", "97.5 %"]
```

**Part (c)–(d): 95% CI on β₁ (slope)**
```r
# (c) lower: ci["x", "2.5 %"]
# (d) upper: ci["x", "97.5 %"]
```

**Part (e)–(f): 95% CI on mean wear at x = 30**
```r
ci_mean <- predict(fit, newdata = data.frame(x = 30),
                   interval = "confidence", level = 0.95)
# (e) lower: ci_mean[, "lwr"]
# (f) upper: ci_mean[, "upr"]
```

---

## Q2 — Rocket Motor Bond Strength (SLR, 95% CI + PI)

**Problem:** Rocket motor bond shear strength (psi) vs propellant age (weeks). n = 20. Find 95% CI on β₀, β₁, mean shear at x = 20; also PI at x = 20.

**Setup:**
```r
fit <- lm(y ~ x, data = df)
df_resid <- 20 - 2   # = 18
```

**Parts (a)–(d): same as Q1** — use `confint(fit, level = 0.95)`, columns `2.5 %` / `97.5 %`.

**Parts (e)–(f): 95% CI on mean shear at x = 20**
```r
ci_x20 <- predict(fit, newdata = data.frame(x = 20),
                  interval = "confidence", level = 0.95)
# (e) lwr, (f) upr
```

**Parts (g)–(h): 95% PI at x = 20**
```r
pi_x20 <- predict(fit, newdata = data.frame(x = 20),
                  interval = "prediction", level = 0.95)
# (g) lwr, (h) upr
```

**Key distinction:** PI is always wider than CI — it must cover a single new observation, not just the mean. Same point estimate (`fit`), wider bounds.

---

## Q3 — Toenail Arsenic (MLR 3 regressors, 99% CI + PI)

**Problem:** Toenail arsenic (ppm) vs age (x₁), drink use (x₂), cook use (x₃). n = 21. Find 99% CIs on β₁, β₂, β₃; 99% CI and PI on mean at x₀ = (30, 4, 4).

**Setup:**
```r
fit <- lm(y ~ x1 + x2 + x3, data = df)   # or: fit <- df %>% lm()
p        <- 3
df_resid <- 21 - 3 - 1   # = 17
```

**Part (a): 99% CI on coefficients — columns are `0.5 %` / `99.5 %`**
```r
ci <- confint(fit, level = 0.99)
# β₁: ci["x1", "0.5 %"]  and  ci["x1", "99.5 %"]
# β₂: ci["x2", "0.5 %"]  and  ci["x2", "99.5 %"]
# β₃: ci["x3", "0.5 %"]  and  ci["x3", "99.5 %"]
```

**Part (b): 99% CI on mean arsenic at x₀ = (30, 4, 4)**
```r
ci_x0 <- predict(fit, newdata = data.frame(x1 = 30, x2 = 4, x3 = 4),
                 interval = "confidence", level = 0.99)
# lwr = Q7, upr = Q8
```

**Part (c): 99% PI at x₀ = (30, 4, 4)**
```r
pi_x0 <- predict(fit, newdata = data.frame(x1 = 30, x2 = 4, x3 = 4),
                 interval = "prediction", level = 0.99)
# lwr = Q9, upr = Q10
```

---

## Q4 — Optical Correlator (MLR 2 regressors, 99% CI + PI, two x₀ points)

**Problem:** Useful range (ng) vs brightness (x₁, %) and contrast (x₂, %). n = 9. Find 99% CIs on β₁, β₂; 99% CI and PI at (70, 80) and at (50, 25).

**Setup:**
```r
fit <- lm(y ~ x1 + x2, data = df)
p        <- 2
df_resid <- 9 - 2 - 1   # = 6   ← small n → large t_crit!
```

**Part (a): 99% CIs on coefficients** (columns `0.5 %` / `99.5 %`)
```r
ci <- confint(fit, level = 0.99)
```

**Part (b): 99% CI at brightness = 70, contrast = 80**
```r
ci_b <- predict(fit, newdata = data.frame(x1 = 70, x2 = 80),
                interval = "confidence", level = 0.99)
```

**Part (c): 99% PI at (70, 80)**
```r
pi_b <- predict(fit, newdata = data.frame(x1 = 70, x2 = 80),
                interval = "prediction", level = 0.99)
```

**Part (d): 99% CI and PI at (50, 25)**
```r
ci_d <- predict(fit, newdata = data.frame(x1 = 50, x2 = 25),
                interval = "confidence", level = 0.99)
pi_d <- predict(fit, newdata = data.frame(x1 = 50, x2 = 25),
                interval = "prediction", level = 0.99)
```

> Note: (50, 25) is an observed data point. CI will be tighter near the data centroid than extrapolated points.

---

## Q5 — Coal/Limestone Density (MLR 2 regressors, 90% CI + PI)

**Problem:** Density vs dielectric constant (x₁) and loss factor (x₂). n = 11. Find **90%** CIs and PI at x₀ = (2.3, 0.025).

**Setup:**
```r
fit <- lm(y ~ x1 + x2, data = df)
p        <- 2
df_resid <- 11 - 2 - 1   # = 8
```

**Key difference from Q3/Q4: level = 0.90 → columns `5 %` / `95 %`**
```r
ci <- confint(fit, level = 0.90)
# β₁: ci["x1", "5 %"]  and  ci["x1", "95 %"]
# β₂: ci["x2", "5 %"]  and  ci["x2", "95 %"]
```

**90% CI on mean density at (2.3, 0.025):**
```r
ci_b <- predict(fit, newdata = data.frame(x1 = 2.3, x2 = 0.025),
                interval = "confidence", level = 0.90)
```

**90% PI at (2.3, 0.025):**
```r
pi_b <- predict(fit, newdata = data.frame(x1 = 2.3, x2 = 0.025),
                interval = "prediction", level = 0.90)
```

---

## Q6 — Chemical Plant Power (MLR 4 regressors, 95% CI + PI)

**Problem:** Monthly power (kWh) vs temperature (x₁), days (x₂), purity (x₃), tons (x₄). n = 12. Find 95% CIs on β₁–β₄; 95% CI and PI at x₀ = (75, 24, 90, 98).

**Setup:**
```r
fit <- lm(y ~ x1 + x2 + x3 + x4, data = df)
p        <- 4
df_resid <- 12 - 4 - 1   # = 7
```

**Part (a): 95% CIs on all four coefficients** (columns `2.5 %` / `97.5 %`)
```r
ci <- confint(fit, level = 0.95)
# x1 row = β₁, x2 row = β₂, x3 row = β₃, x4 row = β₄
```

**Part (b): 95% CI at (75, 24, 90, 98)**
```r
ci_b <- predict(fit, newdata = data.frame(x1 = 75, x2 = 24, x3 = 90, x4 = 98),
                interval = "confidence", level = 0.95)
```

**Part (c): 95% PI at (75, 24, 90, 98)**
```r
pi_b <- predict(fit, newdata = data.frame(x1 = 75, x2 = 24, x3 = 90, x4 = 98),
                interval = "prediction", level = 0.95)
```

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Using wrong column name in `confint()` | Check: 95% → `"2.5 %"`, 99% → `"0.5 %"`, 90% → `"5 %"` |
| Using `n − 2` df for MLR | MLR df = `n − k − 1` where k = number of regressors |
| Confusing CI and PI | CI = where the **mean** is; PI = where a **single new value** is (always wider) |
| Wrong `newdata` variable names | Must match **exactly** the column names used when fitting (`x`, `x1`, `x2`, etc.) |
| Reading wrong row of `confint()` | Row name is the variable name: `(Intercept)`, `x`, `x1`, `x2`, etc. |

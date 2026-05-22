---
tags: [r-code, section-1-2, section-3]
tier: script
sources: [Section3_Study_Guide.Rmd, L34-35_Study_Sheet.Rmd, L36-37_Study_Guide.Rmd]
---
# Teacher-Language Guide: Reading R Output

**Purpose:** Map every R output term to the statistical language your instructor expects in exam answers.

---

## Hypothesis Test Conclusions (all tests)

| p-value vs α | What to say |
|-------------|------------|
| p-value < α | "Reject H₀ at α = X. There is **sufficient evidence** to conclude that [H₁ in context]." |
| p-value > α | "Fail to reject H₀ at α = X. There is **insufficient evidence** to conclude that [H₁ in context]." |

**Never say "accept H₀"** — always "fail to reject."

---

## `t.test()` Output (1-sample or 2-sample)

```
	One Sample t-test
t = -2.34, df = 19, p-value = 0.031
alternative hypothesis: true mean is not equal to 50
95 percent confidence interval:
 47.21  49.85
```

| R Output | Teacher's Term |
|----------|---------------|
| `t = -2.34` | T₀ = −2.34 (test statistic t*) |
| `df = 19` | degrees of freedom (n − 1) |
| `p-value = 0.031` | p-value; compare to α |
| `95 percent confidence interval` | "We are 95% confident that μ is between 47.21 and 49.85" |
| `alternative hypothesis` | H₁ |

---

## `summary(lm())` — Regression Coefficients Table

```
Coefficients:
             Estimate Std. Error t value Pr(>|t|)    
(Intercept) 2627.822     44.184  59.488  < 2e-16 ***
x            -37.154      2.550 -14.571  < 2e-16 ***
```

| Column | Teacher's Term | Usage |
|--------|---------------|-------|
| `Estimate` | β̂ⱼ — least-squares estimate | Coefficient estimate; report with units |
| `Std. Error` | se(β̂ⱼ) — standard error | Used in CI and t-test formulas |
| `t value` | T₀ — test statistic for H₀: βⱼ = 0 | Only valid if null IS zero |
| `Pr(>|t|)` | p-value (two-sided, null = 0) | Compare to α |
| `***` / `**` / `*` | Significance stars | Ignore for exams — use actual p-value |

**Bottom of summary:**
```
Residual standard error: 14.08 on 18 degrees of freedom
Multiple R-squared:  0.9219,	Adjusted R-squared:  0.9175
F-statistic: 212.3 on 1 and 18 DF,  p-value: < 2.2e-16
```

| R Output | Teacher's Term |
|----------|---------------|
| `Residual standard error: 14.08` | σ̂ = 14.08 (estimate of σ) |
| `on 18 degrees of freedom` | df = n − p = n − 2 for SLR |
| `Multiple R-squared: 0.9219` | R² = 0.9219; "92.19% of variation in Y is explained" |
| `Adjusted R-squared: 0.9175` | R²_adj; use when comparing models |
| `F-statistic: 212.3` | F₀ = 212.3 |
| `on 1 and 18 DF` | df₁ = k = 1, df₂ = n − p = 18 |
| `p-value: < 2.2e-16` | p-value for overall F-test |

---

## `anova(lm())` Output

```
Analysis of Variance Table

Response: y
          Df Sum Sq Mean Sq F value    Pr(>F)    
x          1  42113   42113  212.33 < 2.2e-16 ***
Residuals 18   3570     198
```

| R Output | Teacher's Term |
|----------|---------------|
| `Df` (x row) | k = number of predictors |
| `Df` (Residuals) | n − p = error df |
| `Sum Sq` (x) | SSR — Regression sum of squares |
| `Sum Sq` (Residuals) | SSE — Error sum of squares |
| `Mean Sq` (x) | MSR = SSR/k |
| `Mean Sq` (Residuals) | MSE = σ̂² (error variance estimate) |
| `F value` | F₀ = MSR/MSE (use `summary()$fstatistic` for MLR overall) |
| `Pr(>F)` | p-value for F-test on significance of regression |

---

## `confint()` Output

```
                 2.5 %    97.5 %
(Intercept)  2534.79   2720.85
x             -42.50    -31.81
```

| Reading | Interpretation |
|---------|---------------|
| Row `(Intercept)` | 95% CI on β₀: (2534.79, 2720.85) |
| Row `x` | 95% CI on β₁: (−42.50, −31.81) |
| 0 NOT in CI for `x` | Reject H₀: β₁ = 0; β₁ is significant |
| 0 IN CI for `x` | Fail to reject H₀: β₁ = 0; β₁ is not significant |

**Column name changes with confidence level:**
- 90% → `"5 %"` and `"95 %"`
- 95% → `"2.5 %"` and `"97.5 %"`
- 99% → `"0.5 %"` and `"99.5 %"`

---

## `predict()` Output

```
    fit      lwr      upr
1  267.3   241.7   292.9
```

| Output | CI on mean response | PI on future obs |
|--------|--------------------|--------------------|
| `fit` | ŷ₀ = point estimate | Same |
| `lwr` | Lower bound | Lower bound (wider) |
| `upr` | Upper bound | Upper bound (wider) |

**Teacher's phrasing (CI):** "We are X% confident that the **mean** [Y] at x = [x₀] is between [lwr] and [upr]."

**Teacher's phrasing (PI):** "We are X% confident that a **new individual** [Y] at x = [x₀] will fall between [lwr] and [upr]."

---

## `qcc()` Control Chart Output

```
Process statistics
               mean   std.dev
          1.491111 0.1113587

Control limits
    LCL   UCL
1.369 1.614
```

| Output | Teacher's Term |
|--------|---------------|
| `mean` | x̄̄ = grand mean (center line of X̄ chart) |
| `std.dev` | σ̂ estimated from R or S chart |
| `LCL` / `UCL` | Lower/Upper control limits |
| Red plotted points | Out-of-control signals |
| Orange/yellow zones | Warning zones (2σ) |

**In control:** "The process appears to be in statistical control."  
**Out of control:** "Point(s) [#] fall outside the 3σ control limits, indicating the process is out of statistical control."

---

## `process.capability()` Output

```
Process Capability Analysis

          mean    std.dev
     1.491111 0.09817419

     Target         LSL         USL
       1.500       1.300       1.700

Cp    Cpk   Cpm
2.26  2.22  2.25
```

| Output | Teacher's Term |
|--------|---------------|
| `Cp` | Process capability ratio — spread vs spec width |
| `Cpk` | Process capability index — accounts for centering |
| `Cp ≥ 1.33` | "The process is capable of meeting specifications." |
| `Cpk < Cp` | "The process is off-center." |

---

## `cor.test()` Output

```
Pearson's product-moment correlation

t = 8.54, df = 30, p-value = 3.2e-09
alternative hypothesis: true correlation is not equal to 0
95 percent confidence interval:
 0.743  0.938
sample estimates:
  cor 
0.843
```

| Output | Teacher's Term |
|--------|---------------|
| `cor = 0.843` | r = 0.843 (Pearson correlation) |
| `t = 8.54, df = 30` | T₀ = 8.54 for H₀: ρ = 0 |
| `p-value = 3.2e-09` | p-value; < α → significant linear relationship |
| `95 percent confidence interval` | CI on ρ |

---

## R Diagnostic Plot `plot(fit)`

| Plot # | Name | What to look for |
|--------|------|-----------------|
| 1 | Residuals vs Fitted | Random scatter around 0 → linearity + constant variance OK |
| 2 | Normal Q-Q | Points on line → normality OK |
| 3 | Scale-Location | Flat line → constant variance OK |
| 4 | Residuals vs Leverage | High Cook's D → influential points |

## Related
- [regression-r](regression-r.md)
- [hypothesis-tests-r](hypothesis-tests-r.md)
- [control-charts-r](control-charts-r.md)

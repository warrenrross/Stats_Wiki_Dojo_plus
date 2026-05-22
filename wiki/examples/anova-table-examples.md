---
tags: [example, section-3]
tier: script
sources: [L34&35P HT in Linear Regression, L36&37P CI in Regression, regression-ht]
---
# Examples: Completing ANOVA and Summary Tables

See also: [regression-ht](../concepts/regression-ht.md), [regression-slr](../concepts/regression-slr.md), [regression-mlr](../concepts/regression-mlr.md), [reading-r-output](../r-code/reading-r-output.md)

> **Exam focus:** You will NOT calculate from raw data. You WILL be given a partial table from R output and asked to fill in blanks, compute σ̂, interpret, and make recommendations.

---

## The Master Relationships (memorize these)

### ANOVA Table

```
Source      df       SS       MS          F           p
Regression  k        SSR      MSR=SSR/k   F₀=MSR/MSE  p-value
Residuals   n-p      SSE      MSE=SSE/(n-p)
Total       n-1      SST
```

**Abbreviations:**

| Symbol | Full name | Meaning |
|--------|-----------|---------|
| df | Degrees of freedom | Units of independent information available for estimation |
| SS | Sum of squares | A measure of total squared deviation |
| MS | Mean square | SS divided by its df; an estimated variance |
| F (F₀) | F-statistic | Test statistic for the overall model: MSR / MSE |
| p | p-value | Probability of observing F₀ this large if H₀ is true |
| SSR | Sum of squares — Regression | Variation in y *explained* by the model |
| SSE | Sum of squares — Error (Residuals) | Variation in y *not explained* by the model |
| SST | Sum of squares — Total | Total variation in y around its mean: SSR + SSE |
| MSR | Mean square — Regression | SSR / k |
| MSE | Mean square — Error | SSE / (n − p); also equals σ̂² |
| k | Number of predictors | Regression df; equals p − 1 |
| n | Sample size | Number of observations |
| p (parameter count) | Number of parameters | k + 1 (predictors + intercept); used in df_Res = n − p |
| σ̂ | Estimated standard deviation | √MSE; typical error of a prediction in original units |
| R² | Coefficient of determination | SSR / SST; proportion of variation explained by the model |

> **Note:** "p" is overloaded — it means *p-value* in the F column but *number of parameters* in the df formulas. Context makes it clear.

- **p** = number of parameters = k + 1 (intercept + number of predictors)
- **SLR:** k = 1, df_Reg = 1, df_Res = n − 2
- **MLR with k predictors:** df_Reg = k, df_Res = n − k − 1

**Key formulas to fill any blank:**

| Want | Formula |
|------|---------|
| SST | SSR + SSE |
| SSR | SST − SSE |
| SSE | SST − SSR |
| MSR | SSR / k |
| MSE | SSE / (n − p) |
| F₀ | MSR / MSE |
| σ̂² | MSE |
| σ̂ | √MSE |
| R² | SSR / SST |
| R²_adj | 1 − MSE / [SST / (n − 1)] |

### Summary Table (`summary(fit)$coefficients`)

```
             Estimate   Std. Error   t value   Pr(>|t|)
(Intercept)  β̂₀        se₀          t₀        p₀
x1           β̂₁        se₁          t₁        p₁
x2           β̂₂        se₂          t₂        p₂
```

**Key formulas:**

| Want | Formula |
|------|---------|
| t value | Estimate / Std. Error |
| Std. Error | Estimate / t value |
| Estimate | t value × Std. Error |

> **Warning:** The `t value` column ALWAYS tests H₀: βⱼ = 0. If the exam gives a non-zero null, compute T₀ manually: T₀ = (β̂ⱼ − β₀) / se(β̂ⱼ).

---

## Example 1 — SLR: Fill the ANOVA Table

**Given (Oxygen Purity, n = 20, k = 1):**
```
Source      df    SS        MS        F       p
Regression  1     ____      ____      ____    < 0.001
Residuals   18    21.25     ____
Total       19    ____
```
Also known: R² = 0.877

**Find:** Fill in all blanks. State σ̂. State the model conclusion at α = 0.05.

---

**Solution:**

**Step 1 — MSE from Residuals row:**
$$MSE = \frac{SSE}{df_{Res}} = \frac{21.25}{18} = 1.181$$

**Step 2 — σ̂:**
$$\hat{\sigma} = \sqrt{MSE} = \sqrt{1.181} = 1.087$$

**Step 3 — SST from R²:**
$$R^2 = \frac{SSR}{SST} \implies SST = \frac{SSR}{R^2}$$
We need SSR first. Since SST = SSR + SSE:
$$0.877 = \frac{SSR}{SSR + 21.25} \implies 0.877(SSR + 21.25) = SSR \implies 21.25 \times 0.877 = 0.123 \times SSR$$
$$SSR = \frac{21.25 \times 0.877}{0.123} = \frac{18.64}{0.123} = 151.5$$

Alternatively, once you have SSR: SST = SSR + SSE = 151.5 + 21.25 = 172.75

**Step 4 — MSR:**
$$MSR = \frac{SSR}{k} = \frac{151.5}{1} = 151.5$$

**Step 5 — F₀:**
$$F_0 = \frac{MSR}{MSE} = \frac{151.5}{1.181} = 128.3$$

**Completed table:**
```
Source      df    SS        MS        F       p
Regression  1     151.5     151.5     128.3   < 0.001
Residuals   18    21.25     1.181
Total       19    172.75
```

**Answer:**
> "The regression model is significant at α = 0.05. F₀ = 128.3 with p < 0.001 — there is sufficient evidence that at least one regression coefficient is nonzero. σ̂ = 1.087."

---

## Example 2 — MLR: Fill the ANOVA Table

**Given (Wirebond Pull Strength, n = 25, k = 2 predictors):**
```
Source      df    SS          MS          F        p
Regression  ____  ____        2995.39     ____     < 0.001
Residuals   ____  ____        5.235
Total       24    ____
```

**Find:** Fill all blanks. State σ̂, R², and the test conclusion.

---

**Solution:**

**Step 1 — Degrees of freedom:**
- df_Reg = k = 2
- df_Res = n − k − 1 = 25 − 2 − 1 = 22
- df_Total = n − 1 = 24 ✓ (check: 2 + 22 = 24 ✓)

**Step 2 — SS from MS × df:**
$$SSR = MSR \times df_{Reg} = 2995.39 \times 2 = 5990.78$$
$$SSE = MSE \times df_{Res} = 5.235 \times 22 = 115.17$$
$$SST = SSR + SSE = 5990.78 + 115.17 = 6105.95$$

**Step 3 — F₀:**
$$F_0 = \frac{MSR}{MSE} = \frac{2995.39}{5.235} = 572.2$$

**Step 4 — σ̂ and R²:**
$$\hat{\sigma}^2 = MSE = 5.235 \implies \hat{\sigma} = \sqrt{5.235} = 2.288$$
$$R^2 = \frac{SSR}{SST} = \frac{5990.78}{6105.95} = 0.981$$

**Completed table:**
```
Source      df    SS          MS          F        p
Regression  2     5990.78     2995.39     572.2    < 0.001
Residuals   22    115.17      5.235
Total       24    6105.95
```

**Answer:**
> "The regression model is significant at α = 0.05 (F₀ = 572.2, p < 0.001). 98.1% of the variation in pull strength is explained by the model. σ̂ = 2.288. There is sufficient evidence that at least one coefficient is nonzero."

---

## Example 2b — Reconstruct from F₀ and σ̂² (Scenario B)

**Given (MLR output, n = 30, k = 3 predictors):**
```
F-statistic: 42.6 on 3 and 26 DF,  p-value: < 0.001
Residual standard error: 4.12
```

**Find:** Reconstruct the full ANOVA table. Compute SST, SSR, SSE, R², R²_adj.

---

**Solution:**

**Step 1 — df from problem statement:**
- df_Reg = k = 3
- df_Res = n − k − 1 = 30 − 3 − 1 = 26  ← confirmed by "3 and 26 DF"
- df_Total = n − 1 = 29

**Step 2 — MSE from σ̂:**
$$MSE = \hat{\sigma}^2 = (4.12)^2 = 16.974$$

**Step 3 — MSR from F₀:**
$$MSR = F_0 \times MSE = 42.6 \times 16.974 = 723.09$$

**Step 4 — SS from MS × df:**
$$SSR = MSR \times df_{Reg} = 723.09 \times 3 = 2169.3$$
$$SSE = MSE \times df_{Res} = 16.974 \times 26 = 441.3$$
$$SST = SSR + SSE = 2169.3 + 441.3 = 2610.6$$

**Step 5 — R² and R²_adj:**
$$R^2 = \frac{SSR}{SST} = \frac{2169.3}{2610.6} = 0.831$$
$$R^2_{adj} = 1 - \frac{MSE}{SST/(n-1)} = 1 - \frac{16.974}{2610.6/29} = 1 - \frac{16.974}{90.02} = 0.811$$

**Completed table:**
```
Source      df    SS        MS        F       p
Regression  3     2169.3    723.09    42.6    < 0.001
Residuals   26    441.3     16.974
Total       29    2610.6
```

**Answer:**
> "The regression model is significant (F₀ = 42.6, p < 0.001). R² = 0.831 — 83.1% of the variation in Y is explained by the model. σ̂ = 4.12."

**Scenario B formula chain (memorize this order):**
```
Read:  F₀, σ̂ (or MSE), n, k
Derive:
  df_Reg = k,  df_Res = n−k−1,  df_Total = n−1
  MSE = σ̂²
  MSR = F₀ × MSE
  SSE = MSE × df_Res
  SSR = MSR × df_Reg
  SST = SSR + SSE
  R²  = SSR / SST
  R²_adj = 1 − MSE / (SST / df_Total)
```

---

## Example 3 — Completing the Summary Table

**Given (partial summary table, SLR, n = 20):**
```
             Estimate   Std. Error   t value   Pr(>|t|)
(Intercept)  74.28      ____         ____      0.0009
x            14.95      1.317        ____      < 0.001
```

**Find:** Fill in blanks. Which terms are significant at α = 0.05?

---

**Solution:**

**β̂₁ row (x):**
$$t_1 = \frac{\hat{\beta}_1}{se_1} = \frac{14.95}{1.317} = 11.35$$

**Intercept row:** The p-value is 0.0009, which is < 0.05. Work backwards:
- Two-sided p-value 0.0009 corresponds to |t| ≈ 3.92 at df = 18.
- se₀ = β̂₀ / t₀ = 74.28 / 3.92 ≈ 18.9
  *(Alternatively: if you know df, use `qt(1 - 0.0009/2, 18)` to find t₀, then SE = Est/t₀)*

**Completed table:**
```
             Estimate   Std. Error   t value   Pr(>|t|)
(Intercept)  74.28      ~18.9        ~3.92     0.0009
x            14.95      1.317        11.35     < 0.001
```

**Answer:**
> Both terms are significant at α = 0.05 (both p-values < 0.05). There is sufficient evidence to conclude that x has a significant linear effect on y (t₀ = 11.35, p < 0.001). The intercept is also significantly different from zero (p = 0.0009).

---

## Example 4 — Recommendations from Output

**Scenario:** MLR model with 3 predictors. Summary table:
```
             Estimate   Std. Error   t value   Pr(>|t|)
(Intercept)  45.32      5.12         8.85      < 0.001
x1           2.18       0.41         5.32      < 0.001
x2           -0.43      0.89        -0.48      0.634
x3           1.75       0.33         5.30      < 0.001
```
Overall F-test: F₀ = 48.3, p < 0.001

**Find:** Interpret the output. What recommendation would you make?

---

**Solution:**

- The overall model is significant (F₀ = 48.3, p < 0.001) → at least one predictor is useful.
- x1 and x3 are individually significant (both p < 0.001) → evidence their coefficients ≠ 0.
- x2 is **not** significant (t = −0.48, p = 0.634) → no evidence that x2 contributes beyond x1 and x3.

**Answer:**
> "x2 does not appear to contribute significantly to the model (p = 0.634). I would recommend removing x2 and refitting the model with x1 and x3 only. The overall F-test confirms the model has value, but x2's individual p-value suggests it adds no explanatory power beyond the other predictors."

---

## Quick-Reference: What to Do When a Cell Is Missing

| Missing cell | How to find it |
|-------------|---------------|
| MSE | SSE / df_Res |
| MSR | SSR / df_Reg |
| F₀ | MSR / MSE |
| SSR | SST − SSE **or** MSR × df_Reg |
| SSE | SST − SSR **or** MSE × df_Res |
| SST | SSR + SSE |
| σ̂² | MSE (they are the same thing) |
| σ̂ | √MSE |
| R² | SSR / SST |
| df_Reg | k (= number of predictors) |
| df_Res | n − k − 1 |
| df_Total | n − 1 |
| t value (summary) | Estimate / Std. Error |
| Std. Error (summary) | Estimate / t value |

---

---

## Practice Problems — Fill the ANOVA Table (Class Activity Format)

> **Instructions:** For each problem, compute SSR, fill in all blanks, state σ̂, compute F₀, and state the test conclusion at the given α. Answers are at the bottom of this page.

---

### Practice Problem 1 (SLR, k = 1)

$$H_0: \beta_1 = 0 \qquad H_1: \beta_1 \neq 0$$

$$SS_T = 520; \quad SS_{x_1} = 448; \quad SS_E = 72; \quad \alpha = 0.05; \quad n = 16$$

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | F₀ |
|---------------------|----------------|--------------------|-------------|----|
| Regression          |                |                    |             |    |
| Error or Residual   |                |                    |             |    |
| Total               |                |                    |             |    |

---

### Practice Problem 2 (MLR, k = 2)

$$H_0: \beta_1 = \beta_2 = 0 \qquad H_1: \beta_j \neq 0 \text{ for at least one } j$$

$$SS_T = 1840; \quad SS_{x_1} = 920; \quad SS_{x_2} = 745; \quad SS_E = 175; \quad \alpha = 0.05; \quad n = 22$$

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | F₀ |
|---------------------|----------------|--------------------|-------------|----|
| Regression          |                |                    |             |    |
| Error or Residual   |                |                    |             |    |
| Total               |                |                    |             |    |

---

### Practice Problem 3 (MLR, k = 3)

$$H_0: \beta_1 = \beta_2 = \beta_3 = 0 \qquad H_1: \beta_j \neq 0 \text{ for at least one } j$$

$$SS_T = 6200; \quad SS_{x_1} = 2800; \quad SS_{x_2} = 1900; \quad SS_{x_3} = 1050; \quad SS_E = 450; \quad \alpha = 0.01; \quad n = 30$$

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | F₀ |
|---------------------|----------------|--------------------|-------------|----|
| Regression          |                |                    |             |    |
| Error or Residual   |                |                    |             |    |
| Total               |                |                    |             |    |

---

### Practice Problem 4 (MLR, k = 4)

$$H_0: \beta_1 = \beta_2 = \beta_3 = \beta_4 = 0 \qquad H_1: \beta_j \neq 0 \text{ for at least one } j$$

$$SS_T = 9500; \quad SS_{x_1} = 3400; \quad SS_{x_2} = 2200; \quad SS_{x_3} = 1600; \quad SS_{x_4} = 850; \quad SS_E = 1450; \quad \alpha = 0.05; \quad n = 40$$

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | F₀ |
|---------------------|----------------|--------------------|-------------|----|
| Regression          |                |                    |             |    |
| Error or Residual   |                |                    |             |    |
| Total               |                |                    |             |    |

---

### Practice Problem 5 (MLR, k = 2)

$$H_0: \beta_1 = \beta_2 = 0 \qquad H_1: \beta_j \neq 0 \text{ for at least one } j$$

$$SS_T = 4100; \quad SS_{x_1} = 2200; \quad SS_{x_2} = 1560; \quad SS_E = 340; \quad \alpha = 0.01; \quad n = 18$$

| Source of Variation | Sum of Squares | Degrees of Freedom | Mean Square | F₀ |
|---------------------|----------------|--------------------|-------------|----|
| Regression          |                |                    |             |    |
| Error or Residual   |                |                    |             |    |
| Total               |                |                    |             |    |

---

## Practice Problem Answers

### Answer 1 (k = 1, n = 16)

**SSR** = SS_{x1} = 448

| Source     | SS  | df | MS     | F₀    |
|------------|-----|----|--------|-------|
| Regression | 448 | 1  | 448.00 | 87.11 |
| Residual   | 72  | 14 | 5.143  |       |
| Total      | 520 | 15 |        |       |

$$MSR = \frac{448}{1} = 448 \qquad MSE = \frac{72}{14} = 5.143 \qquad F_0 = \frac{448}{5.143} = 87.11$$

$$\hat{\sigma} = \sqrt{5.143} = 2.268$$

> F₀ = 87.11 >> F_{0.05,1,14} ≈ 4.60 → **Reject H₀.** There is sufficient evidence that β₁ ≠ 0. The regression is significant.

---

### Answer 2 (k = 2, n = 22)

**SSR** = 920 + 745 = 1665

| Source     | SS   | df | MS     | F₀    |
|------------|------|----|--------|-------|
| Regression | 1665 | 2  | 832.50 | 85.44 |
| Residual   | 175  | 19 | 9.211  |       |
| Total      | 1840 | 21 |        |       |

$$MSR = \frac{1665}{2} = 832.50 \qquad MSE = \frac{175}{19} = 9.211 \qquad F_0 = \frac{832.50}{9.211} = 90.38$$

$$\hat{\sigma} = \sqrt{9.211} = 3.035$$

> F₀ = 90.38 >> F_{0.05,2,19} ≈ 3.52 → **Reject H₀.** At least one predictor is significant.

---

### Answer 3 (k = 3, n = 30)

**SSR** = 2800 + 1900 + 1050 = 5750

| Source     | SS   | df | MS      | F₀     |
|------------|------|----|---------|--------|
| Regression | 5750 | 3  | 1916.67 | 110.77 |
| Residual   | 450  | 26 | 17.308  |        |
| Total      | 6200 | 29 |         |        |

$$MSR = \frac{5750}{3} = 1916.67 \qquad MSE = \frac{450}{26} = 17.308 \qquad F_0 = \frac{1916.67}{17.308} = 110.77$$

$$\hat{\sigma} = \sqrt{17.308} = 4.160$$

> F₀ = 110.77 >> F_{0.01,3,26} ≈ 4.64 → **Reject H₀.** At least one predictor is significant at α = 0.01.

---

### Answer 4 (k = 4, n = 40)

**SSR** = 3400 + 2200 + 1600 + 850 = 8050

| Source     | SS   | df | MS     | F₀    |
|------------|------|----|--------|-------|
| Regression | 8050 | 4  | 2012.5 | 55.52 |
| Residual   | 1450 | 35 | 41.429 |       |
| Total      | 9500 | 39 |        |       |

$$MSR = \frac{8050}{4} = 2012.50 \qquad MSE = \frac{1450}{35} = 41.429 \qquad F_0 = \frac{2012.50}{41.429} = 48.58$$

$$\hat{\sigma} = \sqrt{41.429} = 6.437$$

> F₀ = 48.58 >> F_{0.05,4,35} ≈ 2.64 → **Reject H₀.** At least one predictor is significant.

---

### Answer 5 (k = 2, n = 18)

**SSR** = 2200 + 1560 = 3760

| Source     | SS   | df | MS     | F₀     |
|------------|------|----|--------|--------|
| Regression | 3760 | 2  | 1880.0 | 110.59 |
| Residual   | 340  | 15 | 22.667 |        |
| Total      | 4100 | 17 |        |        |

$$MSR = \frac{3760}{2} = 1880.0 \qquad MSE = \frac{340}{15} = 22.667 \qquad F_0 = \frac{1880.0}{22.667} = 82.94$$

$$\hat{\sigma} = \sqrt{22.667} = 4.761$$

> F₀ = 82.94 >> F_{0.01,2,15} ≈ 6.36 → **Reject H₀.** At least one predictor is significant at α = 0.01.

---

---

## Example 5 — DOE (RCBD): Reverse-Engineer ANOVA Table from MS and F

This pattern is distinct from the regression reconstruction examples above. In DOE, the ANOVA table has **three sources** (Factor, Blocks, Error), and you are typically given MS values and F₀ rather than SS directly.

**Given (RCBD, a = 4 treatments, b = 5 blocks):**
```
Source      df    SS       MS          F₀
Factor      ____  ____     115.2067    3.498
Blocks      ____  ____     71.9775
Error       ____  ____     ____
Total       ____  ____
```

**Find:** Fill all blanks. What is the test conclusion at α = 0.05?

---

**Solution:**

**Step 1 — df from design parameters:**
$$df_{\text{Factor}} = a - 1 = 3$$
$$df_{\text{Blocks}} = b - 1 = 4$$
$$df_{\text{Error}} = (a-1)(b-1) = 3 \times 4 = 12$$
$$df_{\text{Total}} = ab - 1 = 19 \quad \text{(check: } 3+4+12=19 \checkmark\text{)}$$

**Step 2 — MS_E from F₀:**
$$MS_E = \frac{MS_{\text{Factor}}}{F_0} = \frac{115.2067}{3.498} = 32.94$$

**Step 3 — SS from MS × df:**
$$SS_{\text{Factor}} = MS_{\text{Factor}} \times df_{\text{Factor}} = 115.2067 \times 3 = 345.62$$
$$SS_{\text{Blocks}} = MS_{\text{Blocks}} \times df_{\text{Blocks}} = 71.9775 \times 4 = 287.91$$
$$SS_E = MS_E \times df_E = 32.94 \times 12 = 395.28$$
$$SS_{\text{Total}} = 345.62 + 287.91 + 395.28 = 1028.81$$

**Completed table:**
```
Source      df    SS        MS          F₀
Factor      3     345.62    115.2067    3.498
Blocks      4     287.91    71.9775
Error       12    395.28    32.94
Total       19    1028.81
```

**Decision:** F_crit(0.05, 3, 12) ≈ 3.49. Since F₀ = 3.498 > 3.49, **reject H₀ at α = 0.05**.

**Answer:**
> "Reject H₀ at α = 0.05. There is sufficient evidence to conclude that at least one treatment mean differs (F₀ = 3.498 > F_crit ≈ 3.49). This is a borderline result — always compare to the exact critical value."

---

**DOE reverse-engineer formula chain (memorize this order):**
```
Given: MS_Factor, F₀, MS_Blocks, design parameters a, b
Derive:
  df_Factor = a−1
  df_Blocks = b−1
  df_Error  = (a−1)(b−1)
  df_Total  = ab−1
  MS_E      = MS_Factor / F₀
  SS_Factor = MS_Factor × df_Factor
  SS_Blocks = MS_Blocks × df_Blocks
  SS_E      = MS_E × df_Error
  SS_Total  = SS_Factor + SS_Blocks + SS_E
```

See also: [rcbd-blocking](../concepts/rcbd-blocking.md) for the RCBD ANOVA structure; compare [regression-ht](../concepts/regression-ht.md) for the regression version of this pattern.

---

## Related
- [regression-ht](../concepts/regression-ht.md)
- [regression-slr](../concepts/regression-slr.md)
- [regression-mlr](../concepts/regression-mlr.md)
- [reading-r-output](../r-code/reading-r-output.md)
- [rcbd-blocking](../concepts/rcbd-blocking.md)
- [crd-one-way-anova](../concepts/crd-one-way-anova.md)

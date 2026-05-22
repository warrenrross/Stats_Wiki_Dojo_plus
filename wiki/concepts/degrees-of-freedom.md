---
tags: [core-concept, section-1-2, section-3]
tier: construct
sources: [L14P, L19P, L22P, L31P, L34-35P, formula-snippets]
---
# Degrees of Freedom — Universal Reference

## In Plain English

Degrees of freedom (df) = **number of values free to vary** after constraints are applied. Each estimated parameter "uses up" one df. df determines which t, F, or χ² distribution to use for critical values and p-values. Getting df wrong = wrong critical value = wrong conclusion.

---

## df Master Table

### One-Sample Tests

| Test | Distribution | df |
|------|-------------|-----|
| Z-test on mean (σ known) | Z (normal) | — (no df needed) |
| t-test on mean (σ unknown) | t | **n − 1** |
| χ²-test on variance σ² | χ² | **n − 1** |

---

### Two-Sample Tests

| Test | Distribution | df |
|------|-------------|-----|
| 2-sample Z on means (σ₁, σ₂ known) | Z | — |
| 2-sample pooled t (σ₁ = σ₂ assumed) | t | **n₁ + n₂ − 2** |
| 2-sample Welch t (σ₁ ≠ σ₂) | t | **ν** (see formula below) |
| Paired t-test | t | **n − 1** (n = # pairs) |
| F-test for equal variances | F | **df₁ = n₁−1, df₂ = n₂−1** |

**Welch df (round DOWN to nearest integer):**
$$\nu = \frac{\left(\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}\right)^2}{\dfrac{(s_1^2/n_1)^2}{n_1-1} + \dfrac{(s_2^2/n_2)^2}{n_2-1}}$$

---

### Chi-Square Tests

| Test | df |
|------|----|
| Goodness-of-fit (k categories) | **k − 1** |
| Test of independence (r rows, c cols) | **(r − 1)(c − 1)** |

---

### Regression

| Context | df_Regression | df_Error | df_Total |
|---------|--------------|----------|---------|
| SLR (1 predictor) | **1** | **n − 2** | n − 1 |
| MLR (k predictors) | **k** | **n − k − 1** | n − 1 |

**General rule for residual df: n − (number of parameters estimated)**
- SLR estimates β₀ and β₁ → df_E = n − 2
- MLR with k regressors estimates k+1 parameters → df_E = n − k − 1

**In R:** residual df = `Residuals` row, `Df` column in `anova(fit)`. This is also `df_resid` for t-critical values in `confint()` and `predict()`.

**ANOVA table summary for MLR (k regressors):**

| Source | SS | df | MS | F |
|--------|----|----|----|----|
| Regression | SS_R | k | SS_R / k | MS_R / MS_E |
| Residual | SS_E | n−k−1 | SS_E / (n−k−1) | |
| Total | SS_T | n−1 | | |

---

### df Quick Reference by Homework Problem

| Homework | n | k (# regressors) | df_resid |
|----------|---|------------------|---------|
| Q1: Fretting Wear (SLR) | 9 | 1 | 7 |
| Q2: Rocket Motor (SLR) | 20 | 1 | 18 |
| Q3: Toenail Arsenic (MLR) | 21 | 3 | 17 |
| Q4: Optical Correlator (MLR) | 9 | 2 | 6 |
| Q5: Coal Density (MLR) | 11 | 2 | 8 |
| Q6: Chemical Plant (MLR) | 12 | 4 | 7 |

---

## How to Find the Right t, F, or χ² Critical Value in R

```r
# t critical value (two-sided, α = 0.05, df = 18)
qt(0.975, df = 18)          # upper tail area = α/2

# t critical value (one-sided upper, α = 0.05, df = 18)
qt(0.95, df = 18)

# χ² critical value (upper tail)
qchisq(0.95, df = 10)

# F critical value (upper tail)
qf(0.95, df1 = 3, df2 = 20)
```

**Logic:** `q*(p, df)` returns the quantile at cumulative probability p. For two-sided α = 0.05, use p = 1 − α/2 = 0.975. For upper-tail only, use p = 1 − α = 0.95.

---

## Common Mistakes

| Mistake | Correct |
|---------|---------|
| Using df = n for one-sample t | df = **n − 1** |
| Using df = n−2 for MLR t-tests | df = **n − k − 1** |
| Forgetting df₁ and df₂ are separate for F | F always has **two** df values |
| Using n₁+n₂−1 for pooled t | pooled t df = **n₁ + n₂ − 2** |
| Using n (# pairs) as df for paired t | df = **n − 1** for paired t |

---

## Related

- [standard-error](standard-error.md) — SE formulas that pair with these df values
- [variance-estimation](variance-estimation.md) — how df enters variance estimation
- [hypothesis-testing-overview](hypothesis-testing-overview.md) — one-sample tests
- [two-sample-tests](two-sample-tests.md) — two-sample and Welch df
- [chi-square](chi-square.md) — GoF and independence df
- [regression-ht](regression-ht.md) — regression ANOVA df
- [regression-ci](regression-ci.md) — which df to use for t-critical in confint()

---
tags: [concept, section-4]
tier: procedure
sources: [L48-50P 2kFD, 4-2kFD 2Factor.R, 5-2kFD 3Factor.R, 6-2kFD 5Factor.R]
---
# 2^k Factorial Design

## In Plain English
When you have k factors and each one is tested at exactly 2 levels (low/−1 and high/+1), the complete design has 2^k runs per replicate. This makes it efficient for **screening** — quickly identifying which of many factors actually matter — and for estimating **main effects and interactions** with a minimum of runs.

The ±1 coding is not cosmetic: it creates orthogonal contrasts, meaning all effect estimates are independent of each other.

## When To Use
- k factors, each at exactly 2 levels (quantitative or qualitative — High/Low, On/Off)
- Goal is screening (finding important factors) or initial characterization
- When k ≥ 4, often run as a **single replicate** (no replication) to limit cost

## Formula(s)

### ±1 Coding
Low level → −1; High level → +1. The interaction column is the **product** of the main effect columns.

**2^2 design sign table:**

| Treatment | A | B | AB |
|-----------|---|---|----|
| (1) | − | − | + |
| a | + | − | − |
| b | − | + | − |
| ab | + | + | + |

**2^3 design** has 8 runs (cube vertices); sign table has columns I, A, B, AB, C, AC, BC, ABC.

### Effect Estimation
$$\text{Effect}_A = \frac{1}{n \cdot 2^{k-1}} \cdot \text{Contrast}_A = \bar{y}_{A+} - \bar{y}_{A-}$$

The effect is the **difference in means** between high and low levels of A, averaged over all combinations of other factors.

### Contrast → SS
$$SS = \frac{(\text{Contrast})^2}{n \cdot 2^k}$$

Each main effect and interaction has **df = 1**.

### Degrees of Freedom Summary

| Source | df |
|--------|----|
| Each effect (A, B, AB, …) | 1 |
| All 2^k − 1 effects combined | 2^k − 1 |
| SSTotal | n·2^k − 1 |
| SSError (with replication) | 2^k·(n−1) |

### Linear Model (Regression Approach)
$$Y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_{12} x_1 x_2 + \varepsilon$$

where x₁, x₂ ∈ {−1, +1}.

**Critical relationship:**
$$\hat{\beta} = \frac{\text{Effect}}{2} = \frac{\bar{y}_+ - \bar{y}_-}{2}$$

**Exam trap:** The `lm()` coefficient from R = Effect/2 = β̂. If asked for the **effect**, **double** the R coefficient.

The book (Minitab definition) reports Coef = Effect/2 (same as R), but β₀ in Minitab differs from R's intercept — don't try to match β₀ between R and Minitab.

### Two Analysis Approaches in R

| Approach | R call | Output | Use when |
|----------|--------|--------|----------|
| Regression | `lm(obs ~ A + B + AB)` | Coefficients = Effect/2; t-tests per term | Asked for regression equation or coefficient estimates |
| ANOVA | `aov(obs ~ A * B)` | F-tests, SS, MS per source | Asked for ANOVA table |

Both give the same SS; they're two views of the same analysis.

### Unreplicated Designs (n = 1, k ≥ 4)

When n=1 (single replicate), df_error = 0 — the F-test is **undefined**. The solution:

1. **Sparsity of effects principle:** Only a few effects are large; most high-order interactions are negligible
2. **Pool high-order interactions** as an estimate of error, OR
3. **Daniel plot** (normal probability plot of effects): Real effects fall off the straight line; noise effects cluster near the line

`FrF2::DanielPlot(lmmodel)` in R — effects far from the normal probability line are flagged as significant.

#### Lenth's PSE and ME (Formal Threshold for Unreplicated 2^k)

When you need a numerical cutoff rather than just a graphical read:

$$s_0 = 1.5 \times \text{median}(|effects|)$$
$$PSE = 1.5 \times \text{median}(|effects| \text{ where } |e| < 2.5 s_0)$$
$$ME = t_{\alpha/2,\; m/3} \times PSE$$

where m = total number of effects (m = 2^k − 1). For a 2^4 design: m = 15, df = m/3 = 5, so ME = t_{0.025,5} × PSE ≈ 2.571 × PSE. An effect with |e| ≥ ME is flagged significant. `FrF2::DanielPlot()` automates this calculation.

#### Effect Extraction from `lm()` When Using Colon-Notation

When `lm(y ~ A*B*C*D)` is used, R names interactions as `A:B`, `A:C`, etc. (with surrounding whitespace). To extract effects reliably:

```r
# Build named vectors to map colon-notation → short labels
effect_terms  <- c("A", "B", "C", "D", "A:B", "A:C", "B:D", ...)
effect_labels <- c("A", "B", "C", "D", "AB",  "AC",  "BD",  ...)

coef_tbl <- summary(fit_lm)$coefficients
effects  <- 2 * coef_tbl[effect_terms, "Estimate"]   # Effect = 2 × coefficient
names(effects) <- effect_labels
```

Alternatively, **pre-compute interaction columns** in the data frame using `mutate()` (`AB = A*B`) and use plain names in the `lm()` formula — avoids the colon-notation lookup entirely and is less error-prone.

#### R Pattern: Single Replicate (n = 1)

Do NOT use `aov()` when n=1 — df_error = 0 and F-tests are undefined. Use a saturated `lm()` instead:

```r
# 2^5 with n=1: pre-compute all interaction columns, then fit saturated model
df <- df %>%
  mutate(AB=A*B, AC=A*C, AD=A*D, AE=A*E,
         BC=B*C, BD=B*D, BE=B*E,
         CD=C*D, CE=C*E, DE=D*E, ...)  # as needed

fit_lm <- lm(obs ~ A+B+C+D+E+AB+AC+AD+AE+BC+BD+BE+CD+CE+DE, data=df)
coef_tbl <- summary(fit_lm)$coefficients
effects  <- 2 * coef_tbl[effect_terms, "Estimate"]   # Effect = 2 × coef
```

**Key nuclear pump results (2^5, n=1):** A=75.25, B=−48.75, C=158.00, D=−19.63, E=−35.25, AC=57.75, CE=−61.75.

#### R Pattern: Two-Replicate (n = 2)

When data has R1/R2 columns, pivot to long format first, then use `aov()`:

```r
dft <- df %>%
  pivot_longer(cols = c(R1, R2), names_to = "Rep", values_to = "Response") %>%
  mutate_at(vars(-Response), as.factor)

fit <- aov(Response ~ A * B * C, data = dft)
aov_tbl <- summary(fit)[[1]]
rownames(aov_tbl) <- trimws(rownames(aov_tbl))   # MANDATORY — R pads names with spaces
```

**Key cutting tool results (2^3, n=2):** F_B=11.53 sig, F_C=8.36 sig, F_AC=23.10 sig; F_A=0.54 not sig.

#### Three-Replicate Pattern (pivot_longer with 3 columns)

Same as two-replicate but with `cols = c(R1, R2, R3)`. The extra replicate improves power but the workflow is identical.

#### setwd Pattern for Drill Scripts

HWK scripts in `Section_4/Drills/` reference CSV/xlsx files by relative path. Add this after `p_load()` to auto-set working directory when opened in RStudio:

```r
if (rstudioapi::isAvailable()) {
  setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
}
```

Without this, running from a project root causes "file not found" for data files.

### R vs. Book (Minitab) Coefficients

| | R (`lm()` coefficient) | Book / Minitab Coef |
|-|------------------------|---------------------|
| Value | Effect / 2 | Effect / 2 |
| Same? | Yes — they match |
| β₀ | R intercept ≠ Minitab constant | Not directly comparable |

The R coefficients are the same as Minitab's "Coef" column, but not Minitab's "Effect" column (which is 2× larger). The ANOVA tables are identical.

## Key Assumptions
1. ±1 coding is applied correctly (pre-computed interaction columns in data)
2. Normality and constant variance (same as any ANOVA)
3. For unreplicated designs: sparsity of effects — only a few effects are real

## Common Mistakes
- Reading `lm()` coefficient as the effect — it is the effect **divided by 2**; if asked for the effect, multiply the R coefficient by 2
- Trying to F-test an unreplicated design without pooling — df_error = 0 and the test fails; use `lm()` + DanielPlot or Lenth's ME instead
- Using the no-gather pattern: for 2^k designs with no replication, the data already has one row per treatment combination — **do not `gather()`** (comment in 6-2kFD 5Factor.R: `## no replications = no gather`)
- Confusing the ±1 coded AB interaction column (product of A and B columns) with a separate variable that needs manual coding — `aov(obs ~ A * B)` handles this automatically when A and B are already ±1 factors
- **Null result ≠ no real effect** — high within-cell variance (large MS_Error) can make even a real biological or physical effect non-significant. Root vole experiment (2^2, n=3): within-cell SD ≈ 58 in no-predator cells vs ≈ 18 in predator cells → MS_Error = 1835, F_Pred = 5.08 non-significant at α = 0.05. A power-insufficient study can fail to detect real effects.
- **Borderline F requires exact comparison** — never judge an F value qualitatively. F_Pred = 5.08 vs F_crit(1,8) = 5.318 → not significant. The 0.23-unit gap matters. Always compute or look up F_crit and compare directly.
- **Heteroscedasticity tied to a factor level** — if one treatment-level has SD ≈ 3× the others, constant variance is violated. Root vole: max/min cell SD ratio ≈ 3.3×. Check residual vs fitted plot and note which cell/level is driving the inequality.

## Related
- [[factorial-anova]] — general factorial for any number of levels
- [[factorial-anova-r]] — R code including `DanielPlot()` and the 4-model hierarchy
- [[2k-factorial-examples]] — worked 2^2 and 2^3 examples with effect calculations
- [[anova-design-guide]] — design selection guide
- [[ss-decomposition]] — each 2^k effect gets one SS row in this framework

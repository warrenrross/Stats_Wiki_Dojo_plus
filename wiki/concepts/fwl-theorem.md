---
tags: [concept, unit-5, regression]
tier: construct
sources: [regression-mlr, rcbd-blocking, factorial-anova]
---
# Frisch-Waugh-Lovell (FWL) Theorem

## In Plain English
If you have a regression with two groups of predictors — a focal predictor X₂ and a control
variable X₁ — you get the **exact same coefficient for X₂** whether you:

1. Run the full MLR: regress Y on X₁ and X₂ together, or
2. Run the FWL shortcut: regress Y on X₁ → save residuals; regress X₂ on X₁ → save residuals; then regress those two sets of residuals on each other.

In plain English: **remove X₁'s influence from both Y and X₂, then correlate what's left.**

## When To Use
- You want to isolate the effect of X₂ after "controlling for" X₁ in observational data
- You want to understand *why* a partial regression coefficient differs from a bivariate correlation
- You need to verify that a partial correlation is truly "holding X₁ constant"

## Formula

Define the **annihilator matrix** for X₁ (the operator that removes X₁ from any vector):

$$M_1 = I - X_1(X_1^\top X_1)^{-1}X_1^\top$$

The FWL theorem states:

$$\hat{\beta}_2^{\text{FWL}} = (X_2^\top M_1 X_2)^{-1} X_2^\top M_1 Y = \hat{\beta}_2^{\text{MLR}}$$

The residualized variables are:

$$\tilde{Y} = M_1 Y \qquad \tilde{X}_2 = M_1 X_2$$

The partial correlation between X₂ and Y controlling for X₁ is:

$$r_{\text{partial}} = \frac{\tilde{X}_2^\top \tilde{Y}}{\|\tilde{X}_2\| \|\tilde{Y}\|}$$

## Mathematical Equivalence with RCBD

RCBD treatment estimation is a special case of FWL where X₁ = block dummy matrix and
X₂ = treatment dummy matrix:

$$\hat{\tau} = (X_T^\top M_B X_T)^{-1} X_T^\top M_B Y$$

Both solve the same equation $\hat{\beta}_2 = (\tilde{X}_2^\top \tilde{X}_2)^{-1}\tilde{X}_2^\top \tilde{Y}$:

| | FWL (observational) | RCBD (experimental) |
|---|---|---|
| M = | Regression annihilator for X₁ | Block-demeaning matrix M_B |
| $\tilde{Y}$ | Y residuals after regressing on X₁ | $Y_{ij} - \bar{Y}_{.j}$ (block-demeaned) |
| $\tilde{X}_2$ | X₂ residuals after regressing on X₁ | Treatment indicators (unchanged by M_B) |
| X₁ ⊥ X₂? | No — must residualize both | Yes by design — M_B X_T = X_T |

**The key difference:** RCBD forces orthogonality by design, so $M_B X_T = X_T$ — block-demeaning
doesn't change the treatment indicators because each treatment appears exactly once per block.
In observational FWL, X₁ correlates with X₂ in the data, so $M_1 X_2 \neq X_2$ — the
residualization does real algebraic work.

## Connection to the Incremental F-Test

The ANOVA incremental F-test (comparing restricted vs. full models) is structurally identical
to RCBD's $F_0 = MS_{\text{Trt}}/MS_E$:

$$F_0 = \frac{(SS_{E,\text{restricted}} - SS_{E,\text{full}}) / df_{\text{added}}}{SS_{E,\text{full}} / df_{E,\text{full}}}$$

Both measure reduction in SS_Error from adding focal terms after nuisance variables are
accounted for. In Python: `statsmodels.stats.anova.anova_lm(restricted_model, full_model)`.

## FWL vs. Course Methods — Summary

| Dimension | FWL | RCBD | General Factorial |
|---|---|---|---|
| Data source | Observational | Designed experiment | Designed experiment |
| Control mechanism | Algebraic residualization | Blocking by design | Randomization |
| Interactions detectable? | No | No (assumed absent) | Yes — core purpose |
| Supports causal claims? | No | Yes | Yes |
| Closest analog | — | ✓ Most similar | Less similar |

## Key Assumptions
1. The relationship between X₁ and Y is **linear** and **additive** — FWL only removes the linear component of X₁
2. No interaction between X₁ and X₂ — same assumption RCBD makes (`+` not `*`)
3. Standard OLS assumptions (independence, homoskedasticity, normality of residuals)

## Common Mistakes
- Interpreting the FWL partial r as a causal effect — statistical control ≠ experimental control
- Forgetting that FWL only partials out ONE nuisance variable at a time in its basic form
- Confusing the partial r (from residual correlation) with the standardized β (from full MLR)
  — they are related but not identical when multiple predictors are present

## Related
- [rcbd-blocking](rcbd-blocking.md) — RCBD treatment estimation is FWL with block dummies as X₁
- [factorial-anova](factorial-anova.md) — factorial regression coefficients are FWL partial coefficients under ±1 coding
- [regression-mlr](regression-mlr.md) — the full MLR that FWL decomposes
- [regression-ht](regression-ht.md) — t-tests on individual βⱼ use FWL-equivalent partial SS
- [correlation-transformations](correlation-transformations.md) — partial correlation vs. bivariate Pearson r

---
tags: [core-concept, section-3, section-4]
tier: construct
sources: [regression-slr, crd-one-way-anova, rcbd-blocking, factorial-anova]
---
# Sum of Squares Decomposition

## In Plain English
Every statistical model in this course boils down to the same question: how much of the total variation in the data does the model account for? The answer is always expressed as a partition of SS_Total into two parts — the variation the model explains and the leftover residual variation.

$$SS_{\text{Total}} = SS_{\text{Model}} + SS_{\text{Error}}$$

This identity holds in **every design covered in this course** — SLR, MLR, CRD, RCBD, factorial, 2^k. The model component may be further subdivided (e.g., SS_A + SS_B + SS_AB in a two-factor factorial), but the fundamental split between model and error never changes. "Explaining variance" literally means moving SS from the Error bucket into the Model bucket.

## The Fundamental Identity

$$SS_{\text{Total}} = SS_{\text{Model}} + SS_{\text{Error}}$$

Holds in ALL designs. The model component may be subdivided (e.g., SS_A + SS_B + SS_AB in factorial), but SS_Model + SS_Error always equals SS_Total.

## Why It Matters

Two key quantities derive directly from this partition:

- **R²** = SS_Model / SS_Total — the proportion of total variation explained by the model
- **F₀** = MS_Model / MS_Error, where MS = SS / df — tests whether the model explains more variation than random chance alone

Every F-test in the course is a ratio of two mean squares derived from this same decomposition.

## Context Table

How the identity appears in each course design:

| Design | Identity | df |
|--------|----------|----|
| SLR | SS_T = SS_R + SS_E | (n−1) = 1 + (n−2) |
| MLR (k predictors) | SS_T = SS_R + SS_E | (n−1) = k + (n−k−1) |
| CRD (a treatments) | SS_T = SS_Trt + SS_E | (N−1) = (a−1) + (N−a) |
| RCBD | SS_T = SS_Trt + SS_Blk + SS_E | adds (b−1) for blocks |
| 2-Factor Factorial | SS_T = SS_A + SS_B + SS_AB + SS_E | (a−1)+(b−1)+(a−1)(b−1)+ab(n−1) |
| 2^k | SS_T = Σ(effect SS) + SS_E | each of the 2^k−1 effects gets 1 df |

The df column partitions exactly the same way: df_T = df_Model + df_Error in every row.

## What MS Means

MS = SS / df converts from a total squared deviation to a per-degree-of-freedom variance estimate. This makes MS_Error comparable across designs despite different sample sizes and factor structures. F₀ = MS_Model / MS_Error tests whether the model-explained variance exceeds the random error variance.

- **MS_Error** estimates σ² — the underlying variance of individual observations around their true group mean
- **MS_Model** estimates σ² + (variance due to the model terms) — if the model terms have no real effect, MS_Model ≈ MS_Error and F₀ ≈ 1
- When F₀ is large, the model is accounting for real signal, not just noise

## Common Mistakes

- **Treating sequential `anova()` rows in MLR as SS_Model components** — they are Type I (sequential) SS, not the unique contribution of each predictor. They sum to SS_Model only when predictors are orthogonal. See [[regression-mlr]] and [[fwl-theorem]].
- **Confusing SS_R (regression) with SS_E (error)** — R uses "Residuals" for error and predictor name rows for model terms; do not read them backwards.
- **Forgetting that df partitions exactly like SS** — if you add a block factor, you lose (b−1) df from SS_Error and gain (b−1) df in SS_Blocks. The total df is unchanged.
- **Treating R² and adjusted R² as interchangeable** — R² always increases when predictors are added (SS_Error can only shrink); adjusted R² penalizes for extra df and is the correct comparison metric for MLR.

## Related

- [[regression-slr]] — worked SLR example of the decomposition (SS_T = SS_R + SS_E)
- [[regression-ht]] — F-test is the ratio of mean squares from this decomposition
- [[regression-mlr]] — R² and the ANOVA table structure derive from this identity
- [[crd-one-way-anova]] — ANOVA Identity section on that page names this construct
- [[rcbd-blocking]] — adds SS_Blocks as a third partition component
- [[factorial-anova]] — splits SS_Model into A, B, AB interaction components
- [[2k-factorial-design]] — each 2^k effect gets its own SS row
- [[degrees-of-freedom]] — df partitions exactly as SS does: df_T = df_Model + df_Error
- [[variance-estimation]] — MS is a variance estimate; same conceptual framework

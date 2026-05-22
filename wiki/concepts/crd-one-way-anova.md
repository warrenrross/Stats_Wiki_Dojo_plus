---
tags: [concept, unit-5]
tier: procedure
sources: [L42&43P, CRD.R, L42-43_App_HWK_Q1.R, L42-43_App_HWK_Q2.R]
---
# Completely Randomized Design — One-Way ANOVA

## In Plain English
You have one factor with 3 or more levels (treatments) and want to know: **does the treatment have any effect on the mean response?** Runs are assigned to treatments completely at random — no blocking, no structure. If the factor only has 1 or 2 levels, use a t-test instead; CRD / one-way ANOVA is the generalization to a treatments.

## When To Use
- One factor with **a ≥ 3 levels** (called treatments)
- Each treatment has **n replicates** (observations); can be unequal (unbalanced)
- Runs are assigned in **random order**
- Want to test whether the treatment means differ

## Formula(s)

### Model
$$Y_{ij} = \mu + \tau_i + \varepsilon_{ij} \quad i = 1,\ldots,a \quad j = 1,\ldots,n$$

- μ = overall mean; τ_i = treatment effect (Σ τ_i = 0); ε_ij ~ N(0, σ²)
- τ is called the **treatment effect**; this is a **fixed-effects model**

### Hypotheses
$$H_0: \tau_1 = \tau_2 = \cdots = \tau_a = 0 \qquad H_1: \tau_i \neq 0 \text{ for at least one } i$$

### Notation
| Symbol | Meaning |
|--------|---------|
| a | number of treatments |
| n | replicates per treatment (balanced) |
| N | total observations = an (balanced) or Σn_i (unbalanced) |
| y_i. | treatment total = Σ_j y_ij |
| ȳ_i. | treatment mean = y_i. / n |
| y.. | grand total = ΣΣ y_ij |
| ȳ.. | grand mean = y.. / N |

### ANOVA Identity
$$SS_T = SS_{\text{Treatments}} + SS_E$$

$$df_{\text{Total}} = df_{\text{Treatments}} + df_{\text{Error}} \quad \Rightarrow \quad (N-1) = (a-1) + (N-a)$$

### ANOVA Table (Balanced Design)

| Source | SS | df | MS | F₀ |
|--------|----|----|----|----|
| Treatments | SS_Trt | a − 1 | SS_Trt / (a−1) | MS_Trt / MS_E |
| Error | SS_E | a(n−1) | SS_E / a(n−1) | |
| Total | SS_T | an − 1 | | |

Note: a(n−1) = N−a for balanced designs. Both forms appear in the textbook.

**Reject H₀ if** F₀ > F_{α, a−1, N−a}  (equivalently, if p-value < α)

### Confidence Intervals

**On a single treatment mean:**
$$\bar{y}_{i.} \pm t_{\alpha/2,\, N-a} \sqrt{\frac{MS_E}{n}}$$

**On the difference in two treatment means (balanced):**
$$(\bar{y}_{i.} - \bar{y}_{j.}) \pm t_{\alpha/2,\, N-a} \sqrt{\frac{2MS_E}{n}}$$

**On the difference in two treatment means (unbalanced):**
$$(\bar{y}_{i.} - \bar{y}_{j.}) \pm t_{\alpha/2,\, N-a} \sqrt{MS_E\left(\frac{1}{n_i} + \frac{1}{n_j}\right)}$$

### Fisher's Least Significant Difference (LSD)

Used after rejecting H₀ to determine **which pairs** of treatments differ.

$$\text{LSD} = t_{\alpha/2,\, N-a} \sqrt{\frac{2MS_E}{n}} \quad \text{(balanced)}$$

$$\text{LSD} = t_{\alpha/2,\, N-a} \sqrt{MS_E\left(\frac{1}{n_i} + \frac{1}{n_j}\right)} \quad \text{(unbalanced)}$$

Pair (i, j) is **significantly different** if |ȳ_i. − ȳ_j.| > LSD.

In R: `LSD.test(model, "treatment_column")` from the `agricolae` package.

### Model Adequacy — Residuals

$$e_{ij} = y_{ij} - \bar{y}_{i.}$$

`plot(model)` produces 4 plots. Key plots:
- **Plot 1 (Residuals vs Fitted):** Check constant variance — spread should be roughly equal at each fitted value (each ȳ_i.)
- **Plot 2 (Normal Q-Q):** Check normality — points should follow the diagonal line

## Key Assumptions
1. **Normality:** ε_ij ~ N(0, σ²) — check Normal Q-Q plot
2. **Independence:** Runs are in random order
3. **Constant variance (homoscedasticity):** Same σ² for all treatments — check Residuals vs Fitted

## Common Mistakes
- Confusing df_treatments (a−1) with df_error (N−a) when computing MS or critical F
- Using the balanced CI formula (2MS_E/n) for an **unbalanced** design — must use (1/n_i + 1/n_j)
- Applying LSD when H₀ has **not** been rejected — LSD is a follow-up test only
- Forgetting that `aov()` in R needs the data in **tall (long) format** — one column for treatment labels, one for observations

## Related
- [crd-examples](../examples/crd-examples.md) — two worked homework problems (balanced and unbalanced)
- [anova-r](../r-code/anova-r.md) — complete R workflow for CRD and RCBD
- [rcbd-blocking](rcbd-blocking.md) — add a block factor to control nuisance variability
- [factorial-anova](factorial-anova.md) — extend to two or more factors
- [model-adequacy](model-adequacy.md) — full diagnostic plot guide
- [which-test](which-test.md) — decide which test to use
- [two-sample-tests](two-sample-tests.md) — two-sample t is the k=2 special case of one-way ANOVA
- [hypothesis-testing-overview](hypothesis-testing-overview.md) — the 7-step framework applies to the ANOVA F-test
- [variance-estimation](variance-estimation.md) — MS_E is a variance estimate; see the universal reference for context
- [ss-decomposition](ss-decomposition.md) — the ANOVA Identity is the SS version of this universal construct
- [power-sample-size](power-sample-size.md) — use OC curves (Φ²) to determine required replicates n before running a CRD

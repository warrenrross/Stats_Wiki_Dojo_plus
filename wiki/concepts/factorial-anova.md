---
tags: [concept, section-4]
tier: procedure
sources: [L46&47P, 1-TwoFactor.R, 2-ThreeFactor.R, 3-FourFactor.R]
---
# Factorial Experiments

## In Plain English
A **factorial experiment** tests all possible combinations of two or more factors simultaneously. This lets you detect not just whether each factor matters individually (main effects), but also whether the effect of one factor **depends on the level of another** (interaction effects). Running factors one-at-a-time misses interactions entirely.

The key insight: if an interaction is present, interpreting main effects alone gives the wrong answer.

## When To Use
- Two or more factors of interest (not nuisance — those go in RCBD)
- You want to investigate **main effects** and **interaction effects**
- You have n ≥ 2 replicates per cell (required to estimate error)

## Formula(s)

### 2-Factor Model (eq 14.1)
$$Y_{ijk} = \mu + \tau_i + \beta_j + (\tau\beta)_{ij} + \varepsilon_{ijk}$$
$$i=1,\ldots,a \quad j=1,\ldots,b \quad k=1,\ldots,n$$

- τ_i = main effect of A; β_j = main effect of B; (τβ)_ij = interaction effect

### 2-Factor Hypotheses
| Test | H₀ | H₁ |
|------|----|----|
| Factor A main effect | τ₁ = … = τ_a = 0 | at least one τ_i ≠ 0 |
| Factor B main effect | β₁ = … = β_b = 0 | at least one β_j ≠ 0 |
| AB Interaction | (τβ)₁₁ = … = (τβ)_ab = 0 | at least one (τβ)_ij ≠ 0 |

### 2-Factor ANOVA Table (Table 14.4)

| Source | SS | df | MS | F₀ |
|--------|----|----|----|----|
| A treatments | SS_A | a − 1 | SS_A/(a−1) | MS_A/MS_E |
| B treatments | SS_B | b − 1 | SS_B/(b−1) | MS_B/MS_E |
| Interaction AB | SS_AB | (a−1)(b−1) | SS_AB/((a−1)(b−1)) | MS_AB/MS_E |
| Error | SS_E | ab(n−1) | SS_E/(ab(n−1)) | |
| Total | SS_T | abn − 1 | | |

**Note:** df_error = ab(n−1). This requires n ≥ 2 replicates per cell.

### 3-Factor Model (eq 14.5)
$$Y_{ijkl} = \mu + \tau_i + \beta_j + \gamma_k + (\tau\beta)_{ij} + (\tau\gamma)_{ik} + (\beta\gamma)_{jk} + (\tau\beta\gamma)_{ijk} + \varepsilon_{ijkl}$$

### 3-Factor ANOVA Table — df column

| Source | df |
|--------|----|
| A | a − 1 |
| B | b − 1 |
| C | c − 1 |
| AB | (a−1)(b−1) |
| AC | (a−1)(c−1) |
| BC | (b−1)(c−1) |
| ABC | (a−1)(b−1)(c−1) |
| Error | abc(n−1) |
| Total | abcn − 1 |

All F₀ = MS_source / MS_E; each effect has its own SS with df as shown.

### Interaction — Reading the Plot
| Lines on interaction plot | Conclusion |
|---------------------------|------------|
| Parallel (or nearly parallel) | No interaction — main effects can be interpreted independently |
| Non-parallel (crossing or diverging) | Interaction present — must interpret A effect separately for each level of B |

**If AB interaction is significant:** report the interaction, not the main effects alone. Use cell means and an interaction plot.

### R Formula Shorthand
| R model formula | Expands to |
|-----------------|-----------|
| `aov(obs ~ F1 * F2)` | F1 + F2 + F1:F2 |
| `aov(obs ~ F1 * F2 * F3)` | F1 + F2 + F3 + F1:F2 + F1:F3 + F2:F3 + F1:F2:F3 |
| `aov(obs ~ F1 + F2)` | F1 + F2 only (no interaction) — this is RCBD syntax, NOT factorial |

**The `*` operator is required for factorial designs.**

## Diagnostic Rules for Constant Variance

**3× rule:** If one cell's within-cell standard deviation is approximately 3× larger than the other cells' SDs, the constant variance assumption is **not reasonable**.

Example: cell (Solder=260°C, Method=1) had within-cell SD ≈ 0.40 μm while all other cells ranged 0.07–0.13 μm. SD ratio ≈ 3.1× → constant variance NOT reasonable. Flag this in the residual vs fitted plot as a fan or funnel shape localized to that factor-level combination.

**Borderline cases:** When max/min cell SD ratio is between 2× and 3×, use judgment and state which cell is driving the inequality.

## Marginality Principle (Hierarchical Models)

If the AB interaction is retained in the model, **both A and B must remain** even if B's main-effect p-value is large. Dropping B from a model that contains AB creates an uninterpretable model because B's effect is inseparable from the interaction.

Teacher's phrasing: "Factor B is retained for model hierarchy (the AB interaction is present)."

## Non-Significant Interaction — Implication for Factor Recommendations

If the interaction F-test is **not significant**, the optimal level of Factor A does not change depending on Factor B's level. The factors act independently, and main effect conclusions apply across all levels of the other factor.

This is often tested directly: "If there is no significant interaction, does the recommended level of A change as B changes?" Answer: **No.**

## LSD on Factorial Marginal Means

When the interaction is negligible, apply Fisher's LSD to the marginal means of the significant factor. Use the full model's df_E and the marginal-mean sample size:

$$LSD = t_{\alpha/2,\, df_E} \times \sqrt{\frac{2 \cdot MS_E}{n_{\text{marginal}}}}$$

where df_E = ab(n−1) and n_marginal = a·n (the number of observations in each marginal mean for factor B, averaging over all levels of A).

In R: `agricolae::LSD.test(fit, "FactorB", group = TRUE)`

**Key warping results (a=4 Cu%, b=4 Temp, n=3):** MS_E from aov(); LSD = 2.76; significant pairs: 40v60, 40v80, 40v100, 60v100, 80v100; NOT 60v80.

## Key Assumptions
1. **Normality** of residuals — check Normal Q-Q plot
2. **Constant variance** across all cells — check Residuals vs Fitted
3. **Independence** — runs are randomized
4. **n ≥ 2 replicates per cell** — required to estimate error df = ab(n−1) > 0

## Common Mistakes
- Using `F1 + F2` instead of `F1 * F2` in `aov()` — the `+` model has zero interaction df and estimates no interaction
- Interpreting main effects when the interaction F-test is significant — the interaction supersedes main effects
- Confusing df_error = ab(n−1) with df_error = (a−1)(b−1); the latter is RCBD (no replication within cells)

## Related
- [crd-one-way-anova](crd-one-way-anova.md) — single-factor version
- [rcbd-blocking](rcbd-blocking.md) — one factor of interest + one nuisance (blocking) factor; uses `+` not `*`
- [2k-factorial-design](2k-factorial-design.md) — special case: all factors at exactly 2 levels
- [factorial-anova-r](../r-code/factorial-anova-r.md) — R code for 2-factor through 4-factor designs
- [factorial-examples](../examples/factorial-examples.md) — worked example with the aircraft primer paint dataset
- [fwl-theorem](fwl-theorem.md) — how FWL connects factorial regression coefficients to observational partial correlation
- [random-effects-model](random-effects-model.md) — factorial factors can be treated as random when levels are sampled from a population
- [ss-decomposition](ss-decomposition.md) — factorial ANOVA splits SS_Model into A, B, AB components

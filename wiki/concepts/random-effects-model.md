---
tags: [concept, section-4]
tier: procedure
sources: [L44&45P]
---
# Random Effects Model

## In Plain English
In a **fixed-effects** CRD, the a treatment levels you chose are the only ones you care about — you want to compare exactly those levels. In a **random-effects** model, those a levels are a random sample from a large population of possible levels. You're not interested in comparing those specific levels; you want to know **how much variability** exists across the population of levels.

Example: Testing 5 operators chosen at random from a pool of 50 — you don't care about those 5 specifically, you want to estimate the operator-to-operator variance in the production process.

## When To Use
- The factor levels are **randomly selected** from a larger population of possible levels
- Goal is to estimate **variance components** (σ²_τ, σ²), not to compare specific treatment means
- Conclusions are valid for the **entire population** of factor levels, not just the tested ones

## Formula(s)

### Model (same structure as CRD)
$$Y_{ij} = \mu + \tau_i + \varepsilon_{ij}$$

But now τ_i ~ N(0, σ²_τ) rather than being fixed constants.

$$V(Y_{ij}) = \sigma^2_\tau + \sigma^2$$

### Hypotheses
$$H_0: \sigma^2_\tau = 0 \qquad H_1: \sigma^2_\tau > 0$$

- If σ²_τ = 0, all treatments are identical (no between-treatment variability)
- If σ²_τ > 0, there is variability between treatment levels in the population

**What the null means in plain English:** H₀ says the factor levels contribute *zero* variance beyond the random noise already in σ². Rejecting it means the factor levels genuinely differ from each other across the population — the grouping variable (batches, operators, machines) matters.

**Teacher-language phrasing:**

| Outcome | Exam Answer |
|---------|------------|
| p < α (reject H₀) | "Reject H₀ at α = [X]. There is sufficient evidence that [factor] significantly affects [response] (σ²_τ > 0)." |
| p ≥ α (fail to reject) | "Fail to reject H₀ at α = [X]. There is insufficient evidence that [factor] contributes significant variability to [response]." |

Note: do **not** say "the batch means are equal" (that's the fixed-effects framing). Say "batch-to-batch variability is [significant / not significant]."

### F-Test
**Same ANOVA table and F₀ = MS_Treatments / MS_E** as the fixed-effects CRD — the test procedure is identical. Only the **interpretation** changes.

### Variance Component Estimates (eq 13.19, 13.20)

$$\hat{\sigma}^2 = MS_E \quad \text{(within-group variance)}$$

$$\hat{\sigma}^2_\tau = \frac{MS_{\text{Treatments}} - MS_E}{n} \quad \text{(between-group variance component)}$$

| Quantity | Meaning |
|----------|---------|
| σ̂² = MS_E | Variability within a given treatment level |
| σ̂²_τ | Variability attributable to differences among treatment levels |
| σ̂²_τ + σ̂² | Total variability in Y |

### Proportion of Variability Attributable to the Factor

$$\rho_\tau = \frac{\hat{\sigma}^2_\tau}{\hat{\sigma}^2_\tau + \hat{\sigma}^2}$$

This is the **intraclass correlation coefficient** — the fraction of total variance explained by differences between factor levels. Report as a percentage for intuition.

*Example (Box & Tiao batch yield):* σ̂²_τ = 1764, σ̂² = 2451 → 1764 / (1764 + 2451) = **41.9%** of yield variability is batch-to-batch; 58.1% is within-batch noise.

**Exam insight:** If σ̂²_τ is large relative to σ̂², improving batch consistency (reducing between-batch variance) is the higher-leverage improvement lever than reducing within-batch noise.

### What If σ̂²_τ Is Negative?

The ANOVA method can produce a negative estimate when MS_Treatments < MS_E. Since variance can't be negative, the standard practice is:
- Treat the negative estimate as **evidence that σ²_τ = 0** (most common)
- Do not re-estimate unless you have reason to believe the model is misspecified

## Key Assumptions
- τ_i ~ N(0, σ²_τ) and ε_ij ~ N(0, σ²), independent
- Same homogeneity of variance assumption as CRD

## Common Mistakes
- Reporting individual treatment-level comparisons (LSD, CIs on μ_i) for random effects — this is not the goal; report variance components instead
- Confusing fixed and random effects: if you specifically chose those factor levels (e.g., exactly temperatures 200°, 250°, 300°), it's fixed effects

## Random Effects vs. Blocks (RCBD) — The Key Distinction

Both random effects models and RCBD blocks represent nuisance sources of variability, but the intent differs:

| | Blocks (RCBD) | Random Effects Factor |
|---|---|---|
| **Why included** | Nuisance to *control away* | Variability you want to *estimate and quantify* |
| **Goal** | Remove block noise to see treatment effect clearly | Understand how much of total variance comes from this factor |
| **What you report** | Treatment means and their significance | Variance components σ̂²_τ and σ̂² |
| **LSD / pairwise CIs?** | Yes — on treatments | No — not the point of the analysis |
| **Question answered** | "Did treatment X work?" | "How consistent is production across [batches/operators/machines]?" |

**The math is identical** — same F-test, same ANOVA table. Only interpretation and what you do next differ.

**Exam angle:** If a problem gives you randomly selected factor levels (operators, batches, machines drawn from a larger pool), it is a random effects model. Report variance components, not pairwise comparisons. If the levels are specifically chosen (exactly these temperatures, exactly these machine settings), it is fixed effects — report means and LSD.

## Related
- [[crd-one-way-anova]] — the fixed-effects version of this design
- [[rcbd-blocking]] — RCBD also uses this model structure when blocks are random
- [[factorial-anova]] — random effects can be applied to factorial designs for variance component estimation

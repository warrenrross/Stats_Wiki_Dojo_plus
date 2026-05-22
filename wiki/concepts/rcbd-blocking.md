---
tags: [concept, section-4]
tier: procedure
sources: [L44&45P, RCBD.R]
---
# Randomized Complete Block Design (RCBD)

## In Plain English
When you have a **nuisance factor** — a variable that affects the response but isn't the factor you care about (e.g., day-to-day variation, different batches, different operators) — you can control it by **blocking**. Group experimental units into homogeneous blocks (one block per level of the nuisance factor), then run all treatments within each block. The result is that block-to-block variability is removed from the error term, making the F-test on treatments more powerful.

Think of RCBD as the multi-treatment extension of the **paired t-test**: pairing is blocking with b=2 blocks.

## When To Use
- One factor of interest (a treatments), plus one **nuisance factor** (b blocks)
- Each treatment appears **exactly once per block** (complete blocks)
- No replication within each block — one observation per (treatment, block) cell
- You expect substantial variation attributable to the nuisance factor

## Formula(s)

### Model
$$Y_{ij} = \mu + \tau_i + \beta_j + \varepsilon_{ij} \quad i = 1,\ldots,a \quad j = 1,\ldots,b$$

- τ_i = treatment effect; β_j = block effect; Σ τ_i = 0, Σ β_j = 0
- **Treatments and blocks do not interact** (this is an assumption of RCBD)

### Hypotheses (on treatments)
$$H_0: \tau_1 = \tau_2 = \cdots = \tau_a = 0 \qquad H_1: \tau_i \neq 0 \text{ for at least one } i$$

### ANOVA Identity
$$SS_T = SS_{\text{Treatments}} + SS_{\text{Blocks}} + SS_E$$

$$df: \quad (ab-1) = (a-1) + (b-1) + (a-1)(b-1)$$

### SS Computing Formulas
$$SS_T = \sum_{i}\sum_j y_{ij}^2 - \frac{y_{..}^2}{ab}$$

$$SS_{\text{Treatments}} = \frac{1}{b}\sum_i y_{i.}^2 - \frac{y_{..}^2}{ab}$$

$$SS_{\text{Blocks}} = \frac{1}{a}\sum_j y_{.j}^2 - \frac{y_{..}^2}{ab}$$

$$SS_E = SS_T - SS_{\text{Treatments}} - SS_{\text{Blocks}}$$

### ANOVA Table

| Source | SS | df | MS | F₀ |
|--------|----|----|----|----|
| Treatments | SS_Trt | a − 1 | SS_Trt / (a−1) | MS_Trt / MS_E |
| Blocks | SS_Blk | b − 1 | SS_Blk / (b−1) | MS_Blk / MS_E |
| Error | SS_E (by subtraction) | (a−1)(b−1) | SS_E / ((a−1)(b−1)) | |
| Total | SS_T | ab − 1 | | |

**Critical formula:** df_error = **(a−1)(b−1)** — not a(n−1) as in CRD.

**Reject H₀ on treatments if** F₀ > F_{α, a−1, (a−1)(b−1)}

### Residuals

$$e_{ij} = y_{ij} - \hat{y}_{ij} \qquad \hat{y}_{ij} = \bar{y}_{i.} + \bar{y}_{.j} - \bar{y}_{..}$$

Fitted value accounts for both treatment mean and block mean departures from grand mean.

### Variance Component Estimates (Random Effects Model)

If the treatments are a random sample from a large population:
- H₀: σ²_τ = 0 vs H₁: σ²_τ > 0; same F-test as CRD
- σ̂² = MS_E (within-group variance)
- σ̂²_τ = (MS_Treatments − MS_E) / n (between-treatment variance component)
- If σ̂²_τ comes out negative, treat it as zero (the variance component is essentially zero)

## When To Block?

Blocking is worthwhile if the block F-test is significant (large SS_Blocks). If you block when there's no real block variation, you lose (a−1)(b−1) degrees of freedom from error without gaining anything, making the test **less** powerful.

Rule of thumb: block when you expect the nuisance factor causes variation larger than your within-cell error.

## What Happens When Blocks Are Ignored (CRD on Blocked Data)

If you run a CRD analysis on data that actually has a blocking structure, SS_Blocks folds into SS_Error, inflating MS_Error and shrinking the F-test on treatments. This is the cost of ignoring a real nuisance factor.

**Formulas:**
$$SS_{\text{Error, CRD}} = SS_{\text{Blk}} + SS_{E,\text{ RCBD}}$$
$$df_{\text{Error, CRD}} = a(n-1) = ab - a$$

Compared to RCBD:
$$df_{\text{Error, RCBD}} = (a-1)(b-1)$$

**Cotton example** (a = 5 treatments, b = 5 blocks):

| | RCBD (blocks included) | CRD (blocks ignored) |
|-|------------------------|----------------------|
| SS_Error | SS_E only | SS_Blk + SS_E |
| df_Error | (4)(4) = 16 | 5(4) = 20 |
| MS_Error | 5.79 | 8.06 |
| F₀ (treatments) | 20.54 | 14.76 |

MS_Error inflates from 5.79 → 8.06 (+39%) and F₀ drops from 20.54 → 14.76 when blocks are discarded. Both would reject H₀ at α = 0.05 here, but in borderline cases the wrong conclusion follows from ignoring blocks.

**Takeaway:** Block when the block F-test is significant (large SS_Blk). Every df given to blocks is subtracted from df_error in RCBD — this is only worthwhile if SS_Blk is large enough to more than compensate by reducing MS_Error.

## Key Assumptions
1. **No interaction** between treatments and blocks — there is no replicate within cells to estimate this
2. **Normality** of residuals
3. **Constant variance** across all treatment × block combinations

## Common Mistakes
- Using `aov(obs ~ trt * blk)` instead of `aov(obs ~ trt + blk)` — the `*` implies interaction; RCBD requires `+` because there's only one observation per cell and no interaction term can be estimated
- Forgetting df_error = **(a−1)(b−1)**, not N−a; this changes the critical F value
- Treating RCBD as a two-factor factorial — RCBD has no replication within cells and no interaction

## Related
- [[crd-one-way-anova]] — the same design without blocking
- [[random-effects-model]] — when treatments are randomly sampled from a population
- [[anova-r]] — R code for RCBD (`aov(obs ~ trt + blk)`)
- [[factorial-anova]] — when you have two factors of equal interest (not nuisance blocking)
- [[fwl-theorem]] — algebraic equivalence between RCBD block-demeaning and FWL residualization
- [[ss-decomposition]] — RCBD adds SS_Blocks as a third term in the universal partition

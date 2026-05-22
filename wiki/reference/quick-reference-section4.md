---
tags: [reference, section-4]
sources: [L42&43P, L44&45P, L46&47P, L48-50P 2kFD]
---
# Quick Reference — Section 4: Experimental Design

## Design Selection Flowchart

```
How many factors?
├─ ONE factor, ≥ 3 levels
│   ├─ No nuisance variable → CRD: aov(obs ~ trt)
│   └─ Nuisance variable → RCBD: aov(obs ~ trt + blk)
└─ TWO OR MORE factors
    ├─ Multiple levels per factor → Factorial: aov(obs ~ F1 * F2 * ...)
    └─ Exactly 2 levels per factor → 2^k FD: lm() + aov() with ±1 coding
```

---

## ANOVA Tables at a Glance

### CRD (Balanced)
| Source | df | MS | F₀ |
|--------|----|----|-----|
| Treatments | a − 1 | SS/(a−1) | MS_Trt/MS_E |
| Error | a(n−1) | SS/(a(n−1)) | |
| Total | an − 1 | | |

### RCBD
| Source | df | MS | F₀ |
|--------|----|----|-----|
| Treatments | a − 1 | SS/(a−1) | MS_Trt/MS_E |
| Blocks | b − 1 | SS/(b−1) | MS_Blk/MS_E |
| Error | **(a−1)(b−1)** | SS/((a−1)(b−1)) | |
| Total | ab − 1 | | |

### 2-Factor Factorial
| Source | df | MS | F₀ |
|--------|----|----|-----|
| A | a − 1 | SS_A/(a−1) | MS_A/MS_E |
| B | b − 1 | SS_B/(b−1) | MS_B/MS_E |
| AB | (a−1)(b−1) | SS_AB/((a−1)(b−1)) | MS_AB/MS_E |
| Error | **ab(n−1)** | SS_E/(ab(n−1)) | |
| Total | abn − 1 | | |

### 2^k Factorial
| Source | df | Notes |
|--------|-----|-------|
| Each effect (A, B, AB, …) | 1 | SS = Contrast²/(n·2^k) |
| All effects | 2^k − 1 | |
| Error (if replicated) | 2^k(n−1) | |
| Total | n·2^k − 1 | |

---

## Key Formulas

### ANOVA Hypothesis
$$H_0: \tau_1 = \tau_2 = \cdots = \tau_a = 0 \qquad H_1: \text{at least one } \tau_i \neq 0$$

### Fisher LSD
$$\text{LSD} = t_{\alpha/2,\, df_E} \sqrt{\frac{2 \cdot MS_E}{n}} \quad \text{(balanced)}$$
$$\text{LSD} = t_{\alpha/2,\, df_E} \sqrt{MS_E\!\left(\tfrac{1}{n_i}+\tfrac{1}{n_j}\right)} \quad \text{(unbalanced)}$$

Pair (i,j) significantly different if |ȳ_i − ȳ_j| > LSD.

### CI on (μ_i − μ_j) — Unbalanced
$$(\bar{y}_{i.} - \bar{y}_{j.}) \pm t_{\alpha/2,\, df_E} \sqrt{MS_E\!\left(\tfrac{1}{n_i}+\tfrac{1}{n_j}\right)}$$

### 2^k Effect and Coefficient
$$\text{Effect} = \frac{\text{Contrast}}{n \cdot 2^{k-1}} \qquad \hat{\beta} = \frac{\text{Effect}}{2} \quad \text{(lm() Estimate)}$$

$$SS_{\text{effect}} = \frac{\text{Contrast}^2}{n \cdot 2^k}$$

### Random Effects Variance Components
$$\hat{\sigma}^2 = MS_E \qquad \hat{\sigma}^2_\tau = \frac{MS_{\text{Trt}} - MS_E}{n}$$

$$\text{Proportion attributable to factor} = \frac{\hat{\sigma}^2_\tau}{\hat{\sigma}^2_\tau + \hat{\sigma}^2}$$

---

## R Formula Cheat Sheet

| Design | aov() formula | Note |
|--------|--------------|-------|
| CRD | `aov(obs ~ trt)` | |
| RCBD | `aov(obs ~ trt + blk)` | `+` not `*` |
| 2-factor factorial | `aov(obs ~ F1 * F2)` | `*` expands to F1+F2+F1:F2 |
| 3-factor factorial | `aov(obs ~ F1 * F2 * F3)` | |
| 2^k ANOVA | `aov(obs ~ A * B * C)` | |
| 2^k regression | `lm(obs ~ A + B + AB + C + ...)` | pre-computed interaction columns |
| Unreplicated 2^k | `DanielPlot(lmmodel)` | from `FrF2` package |

---

## R Extraction Patterns

```r
s     <- summary(model)
f0    <- s[[1]][["F value"]][1]      # F0 (treatment row)
pv    <- s[[1]][["Pr(>F)"]][1]       # p-value
MSE   <- s[[1]][["Mean Sq"]][2]      # MSE (error row)
df_e  <- s[[1]][["Df"]][2]           # error df
t_crit <- qt(0.975, df_e)            # two-sided t critical value

# Unbalanced CI
means <- tapply(y, group, mean)
ns    <- tapply(y, group, length)
```

---

## Reshape Idioms

| Code | Package | Produces |
|------|---------|---------|
| `melt()` | reshape2 | columns: `variable`, `value` |
| `gather(key, val, -id)` | tidyverse | columns named by you |
| `mutate_if(is.character, as.factor)` | tidyverse | after gather() |
| `mutate_at(vars(-obs), as.factor)` | tidyverse | 2^k pattern |
| `filter(!is.na(col))` | tidyverse | unbalanced data cleanup |

---

## Teacher Phrasings

| Situation | Phrasing |
|-----------|---------|
| p < α (treatments) | "Reject H₀ at α = 0.05. There is sufficient evidence that [factor] has an effect on [response]." |
| p ≥ α (treatments) | "Fail to reject H₀ at α = 0.05. There is insufficient evidence that [factor] has an effect on [response]." |
| AB interaction significant | "The AB interaction is significant (F₀ = X, p < α), indicating that the effect of [A] depends on the level of [B]." |
| AB interaction not significant | "The AB interaction is not significant. Main effects can be interpreted independently." |
| Daniel plot result | "Based on the Daniel plot, effects [list] appear significant (fall off the normal probability line). The remaining effects are consistent with random variation." |
| Variance components | "The estimated variance component σ̂²_τ = [value] represents the variability attributable to [factor] in the population." |
| Random effects — reject H₀ | "Reject H₀ at α = [X]. There is sufficient evidence that [factor] significantly affects [response] (σ²_τ > 0)." |
| Random effects — fail to reject | "Fail to reject H₀ at α = [X]. There is insufficient evidence that [factor] contributes significant variability to [response]." |
| Random vs. fixed identification | "Because the [factor] levels were randomly selected from a larger population, this is a random effects model. Report variance components, not pairwise means." |

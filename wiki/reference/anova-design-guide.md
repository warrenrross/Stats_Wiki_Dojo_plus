---
tags: [reference, unit-5]
sources: [L42&43P, L44&45P, L46&47P, L48-50P 2kFD]
---
# ANOVA Design Selection Guide

## Design Decision Table

| Experimental Structure | Design | R Model Formula | Post-Hoc |
|------------------------|--------|-----------------|----------|
| One factor, ≥3 levels, random assignment | **CRD** | `aov(obs ~ trt)` | Fisher LSD |
| One factor + nuisance variable | **RCBD** | `aov(obs ~ trt + blk)` | Fisher LSD |
| Two factors, equal interest | **2-Factor Factorial** | `aov(obs ~ F1 * F2)` | Interaction plot |
| Three factors | **3-Factor Factorial** | `aov(obs ~ F1 * F2 * F3)` | Interaction plot |
| k factors, each at exactly 2 levels | **2^k Factorial** | `lm(obs ~ A+B+AB+...)` + `aov(obs ~ A*B*...)` | Daniel plot (if unreplicated) |
| k factors, 2 levels, n=1 per cell | **Unreplicated 2^k** | `lm()` → `DanielPlot()` | Sparsity of effects principle |

## ANOVA Table df Formulas by Design

| Design | Source | df |
|--------|--------|----|
| **CRD** | Treatments | a − 1 |
| | Error | N − a = a(n−1) for balanced |
| | Total | N − 1 |
| **RCBD** | Treatments | a − 1 |
| | Blocks | b − 1 |
| | **Error** | **(a−1)(b−1)** |
| | Total | ab − 1 |
| **2-Factor Factorial** | A | a − 1 |
| | B | b − 1 |
| | AB | (a−1)(b−1) |
| | **Error** | **ab(n−1)** |
| | Total | abn − 1 |
| **3-Factor Factorial** | A, B, C | a−1, b−1, c−1 |
| | AB, AC, BC | (a−1)(b−1), (a−1)(c−1), (b−1)(c−1) |
| | ABC | (a−1)(b−1)(c−1) |
| | **Error** | **abc(n−1)** |
| | Total | abcn − 1 |
| **2^k Factorial** | Each effect (A, B, AB, …) | 1 each |
| | All effects combined | 2^k − 1 |
| | **Error (replicated)** | **2^k(n−1)** |
| | Total | n·2^k − 1 |

## CI and LSD Formulas

### Fisher LSD (balanced)
$$\text{LSD} = t_{\alpha/2,\, df_E} \sqrt{\frac{2 \cdot MS_E}{n}}$$

### Fisher LSD (unbalanced)
$$\text{LSD} = t_{\alpha/2,\, df_E} \sqrt{MS_E\left(\frac{1}{n_i} + \frac{1}{n_j}\right)}$$

### CI on Treatment Mean
$$\bar{y}_{i.} \pm t_{\alpha/2,\, df_E} \sqrt{\frac{MS_E}{n}}$$

### CI on Difference in Treatment Means (unbalanced)
$$(\bar{y}_{i.} - \bar{y}_{j.}) \pm t_{\alpha/2,\, df_E} \sqrt{MS_E\left(\frac{1}{n_i} + \frac{1}{n_j}\right)}$$

### 2^k Effect and SS
$$\text{Effect} = \frac{\text{Contrast}}{n \cdot 2^{k-1}} \qquad SS = \frac{(\text{Contrast})^2}{n \cdot 2^k} \qquad \hat{\beta} = \frac{\text{Effect}}{2}$$

## Key Distinctions

| Confusion | Answer |
|-----------|--------|
| RCBD uses `+` or `*`? | `+` — no interaction term; only one obs per cell |
| Factorial uses `+` or `*`? | `*` — includes all interactions |
| Which design has df_error = (a−1)(b−1)? | **RCBD only** |
| Which design has df_error = ab(n−1)? | **2-factor factorial** |
| When is Daniel plot needed? | Unreplicated 2^k (n=1, df_error=0) |
| `lm()` coeff vs effect? | coeff = Effect/2 — **double** to get effect |

## R vs Book (Minitab) for 2^k

- R `lm()` Estimate = Effect/2 = Minitab "Coef" column
- Minitab "Effect" column = 2 × R Estimate
- ANOVA tables are identical between R and Minitab

## Related
- [crd-one-way-anova](../concepts/crd-one-way-anova.md) — CRD concept
- [rcbd-blocking](../concepts/rcbd-blocking.md) — RCBD concept
- [factorial-anova](../concepts/factorial-anova.md) — factorial concept
- [2k-factorial-design](../concepts/2k-factorial-design.md) — 2^k concept
- [quick-reference-section4](quick-reference-section4.md) — compact formula sheet

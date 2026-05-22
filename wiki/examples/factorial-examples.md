---
tags: [example, unit-5]
tier: script
sources: [L46&47P, L48-50P 2kFD, 1-TwoFactor.R, 2-ThreeFactor.R]
---
# Example: Factorial Experiments

---

## Example 1 — 2-Factor Factorial: Aircraft Primer Paint (From L46&47 Slides)

### Problem Statement
Aircraft primer paints are applied to aluminum surfaces by two methods: dipping and spraying. An experiment investigated the effect of **primer type** (3 types) and **application method** (2 methods) on **adhesion force**. Three specimens were painted for each combination.

### Given / Find
- **Factor A:** Primer type (a = 3 levels)
- **Factor B:** Application method (b = 2 levels: Dipping, Spraying)
- **Replicates:** n = 3 per cell; N = 3 × 2 × 3 = 18
- **Find:** ANOVA table, significance of main effects and interaction

### ANOVA Table (Table 14.6)

| Source | SS | df | MS | F₀ | p-value |
|--------|----|----|----|----|---------|
| Primer types (A) | 4.58 | 2 | 2.29 | 27.86 | 2.7 × 10⁻⁵ |
| Application methods (B) | 4.91 | 1 | 4.91 | 59.70 | 4.7 × 10⁻⁶ |
| Interaction (AB) | 0.24 | 2 | 0.12 | 1.47 | 0.262 |
| Error | 0.99 | 12 | 0.08 | | |
| Total | 10.72 | 17 | | | |

**df check:** A: a−1=2 ✓; B: b−1=1 ✓; AB: (a−1)(b−1)=2 ✓; Error: ab(n−1)=3×2×2=12 ✓; Total: abn−1=17 ✓

### Interpretation

**Interaction (AB):** F₀ = 1.47, p = 0.262 > 0.05. Fail to reject H₀ — **no significant interaction**. The effect of primer type does not depend on application method (lines on interaction plot are approximately parallel).

Since the interaction is not significant, interpret main effects separately:

**Primer type (A):** F₀ = 27.86, p < 0.05 — **significant**. "Reject H₀ at α = 0.05. There is sufficient evidence that primer type has an effect on adhesion force."

**Application method (B):** F₀ = 59.70, p < 0.05 — **significant**. "Reject H₀ at α = 0.05. There is sufficient evidence that application method has an effect on adhesion force." (Spraying gives higher adhesion.)

### R Code Pattern

```r
pacman::p_load(magrittr, rio, tidyverse)

df <- import("D1-2Factor.xlsx") %>% as_tibble()

dft <- df %>%
  gather(F1, obs, -F2) %>%
  mutate_if(is.character, as.factor) %>%
  select(obs, F1, F2)

model <- dft %$% aov(obs ~ F1 * F2)
model %>% summary()
model %>% plot()
```

---

## Example 2 — 3-Factor Factorial: Surface Roughness (From L48-50 Slides)

### Problem Statement
A mechanical engineer studied surface roughness produced in a metal-cutting operation. Three factors were investigated: feed rate (A), depth of cut (B), and tool angle (C). Each factor has 2 levels, with 2 replicates per treatment combination (2^3 design with replication).

### Given / Find
- **Factors:** A = feed rate (20 vs 30 in/min), B = depth (0.025 vs 0.040 in), C = tool angle (15° vs 25°)
- **Design:** 2^3 factorial, n = 2 replicates; N = 8 × 2 = 16
- **Find:** ANOVA table, which factors/interactions are significant

### ANOVA Table (Table 14.10)

| Source | df | SS | MS | F | p-value |
|--------|----|----|----|----|---------|
| Feed (A) | 1 | 45.563 | 45.563 | 18.69 | 0.003 |
| Depth (B) | 1 | 10.563 | 10.563 | 4.33 | 0.071 |
| Angle (C) | 1 | 3.063 | 3.063 | 1.26 | 0.295 |
| Feed×Depth (AB) | 1 | 7.563 | 7.563 | 3.10 | 0.116 |
| Feed×Angle (AC) | 1 | 0.062 | 0.062 | 0.03 | 0.877 |
| Depth×Angle (BC) | 1 | 1.563 | 1.563 | 0.64 | 0.446 |
| Feed×Depth×Angle (ABC) | 1 | 5.062 | 5.062 | 2.08 | 0.188 |
| Error | 8 | 19.500 | 2.437 | | |
| Total | 15 | 92.938 | | | |

**df check:** Each main effect = 1; each 2-way interaction = (1)(1)=1; 3-way = (1)(1)(1)=1; Error = abc(n−1) = 2×2×2×1 = 8; Total = 2^3 × n − 1 = 15 ✓

### R Output (from `lm(R1 ~ A+B+AB+C+AC+BC+ABC)`)

```
Coefficients:
              Estimate Std. Error t value Pr(>|t|)
(Intercept)    7.1250     1.1040   6.454  0.000197
A1             3.3750     0.7806   4.323  0.002534  **
B1             1.6250     0.7806   2.082  0.070931
AB1            1.3750     0.7806   1.761  0.116197
C1             0.8750     0.7806   1.121  0.294849
```

**Key:** R coefficient for A1 = 3.375 = Effect_A / 2, so Effect_A = 6.75 (change in roughness from low to high feed rate, averaged over all B and C combinations).

### Interpretation
- **Feed rate (A):** p = 0.003 < 0.05 — **significant**. "Reject H₀. Feed rate has a significant effect on surface roughness."
- **Depth (B):** p = 0.071 — marginally non-significant at α = 0.05
- **Angle (C) and all interactions:** p > 0.05 — not significant

Since **no interaction is significant**, main effects can be interpreted independently. Feed rate dominates.

---

## ANOVA Table Completion Practice

Given the following partial two-factor factorial ANOVA output, complete the table:

| Source | SS | df | MS | F₀ | p-value |
|--------|----|----|----|----|---------|
| A | 36.0 | 2 | ? | ? | |
| B | 20.0 | 1 | ? | ? | |
| AB | 9.0 | ? | ? | ? | |
| Error | 24.0 | 12 | ? | | |
| Total | 89.0 | 17 | | | |

*(Design: a=3, b=2, n=3)*

**Solution:**

| Source | SS | df | MS | F₀ |
|--------|----|----|----|----|
| A | 36.0 | 2 | 18.0 | 18.0/2.0 = 9.0 |
| B | 20.0 | 1 | 20.0 | 20.0/2.0 = 10.0 |
| AB | 9.0 | (3−1)(2−1)=2 | 4.5 | 4.5/2.0 = 2.25 |
| Error | 24.0 | ab(n−1)=3×2×2=12 | 2.0 | |
| Total | 89.0 | abn−1=17 | | |

---

## Related
- [factorial-anova](../concepts/factorial-anova.md) — concept and formula page
- [factorial-anova-r](../r-code/factorial-anova-r.md) — full R code patterns for factorial designs
- [2k-factorial-examples](2k-factorial-examples.md) — 2^k specific examples with effect estimation
- [anova-table-examples](anova-table-examples.md) — general ANOVA table completion practice

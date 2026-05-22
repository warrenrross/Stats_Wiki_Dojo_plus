---
tags: [example, section-4]
tier: script
sources: [L48-50P 2kFD, 4-2kFD 2Factor.R, 5-2kFD 3Factor.R, 6-2kFD 5Factor.R]
---
# Example: 2^k Factorial Design

---

## Example 1 — 2^2 Design: Epitaxial Layer Thickness (From L48-50 Slides)

### Problem Statement
An integrated circuit manufacturing study grew epitaxial layers on polished silicon wafers. Two factors were studied: **A = deposition time** (−=short, +=long) and **B = arsenic flow rate** (−=55%, +=59%). Four replicates (n=4) of each of the 2^2 = 4 treatment combinations were run. Response: epitaxial layer thickness (μm).

### Data (Table 14.12)

| Treatment | A | B | AB | Obs (4 reps) | Total | Avg |
|-----------|---|---|----|-------------|-------|-----|
| (1) | − | − | + | 14.037, 14.165, 13.972, 13.907 | 56.081 | 14.020 |
| a | + | − | − | 14.821, 14.757, 14.843, 14.878 | 59.299 | 14.825 |
| b | − | + | − | 13.880, 13.860, 14.032, 13.914 | 55.686 | 13.922 |
| ab | + | + | + | 14.888, 14.921, 14.415, 14.932 | 59.156 | 14.789 |

### Effect Calculations (Manual)

Using Effect = Contrast / (n·2^(k−1)) with n=4, k=2:

$$\text{Effect}_A = \frac{1}{2n}[a + ab - b - (1)] = \frac{1}{8}[59.299 + 59.156 - 55.686 - 56.081] = \frac{6.688}{8} = 0.836$$

$$\text{Effect}_B = \frac{1}{2n}[b + ab - a - (1)] = \frac{1}{8}[55.686 + 59.156 - 59.299 - 56.081] = \frac{-0.538}{8} = -0.067$$

$$\text{Effect}_{AB} = \frac{1}{2n}[ab + (1) - a - b] = \frac{1}{8}[59.156 + 56.081 - 59.299 - 55.686] = \frac{0.252}{8} = 0.032$$

### SS Calculations

$$SS_A = \frac{[6.688]^2}{16} = \frac{44.73}{16} = 2.796$$

$$SS_B = \frac{[-0.538]^2}{16} = \frac{0.289}{16} = 0.018$$

$$SS_{AB} = \frac{[0.252]^2}{16} = \frac{0.063}{16} = 0.004$$

$$SS_T = 14.037^2 + \cdots + 14.932^2 - \frac{(56.081 + \cdots + 59.156)^2}{16} = 3.067$$

### Interpretation

**Deposition time (A):** Effect = 0.836 μm. Increasing deposition time from short to long **increases** mean epitaxial layer thickness by 0.836 μm. This is the dominant effect.

**Arsenic flow rate (B):** Effect = −0.067 μm. Increasing flow rate slightly **decreases** thickness; likely not significant.

**Interaction (AB):** Effect = 0.032 μm. Very small; likely not significant.

### R Code (from `4-2kFD 2Factor.R`)

```r
pacman::p_load(magrittr, rio, tidyverse)

df <- import("D2-2kFD 2Factor.xlsx") %>% as_tibble()

dft <- df %>%
  gather(R, obs, R1:R4) %>%
  mutate_at(vars(-obs), as.factor) %>%
  select(obs, everything(), -c("Treatment", "Identity", R))

lmmodel  <- dft %$% lm(obs ~ A + B + AB)     # coefficients = Effect/2
aovmodel <- dft %$% aov(obs ~ A * B)          # ANOVA table

lmmodel  %>% summary()
aovmodel %>% summary()
```

**Reading `lm()` output:** `Estimate` for A = Effect_A/2 = 0.418. **Double it** to get Effect_A = 0.836. This matches the manual calculation above.

---

## Example 2 — 2^3 Unreplicated Design: Screening with Daniel Plot

### Problem Statement
A 2^3 design with factors A, B, C and **no replication** (n=1, 8 total runs). Goal: identify which effects are real using a Daniel plot, since F-tests are unavailable without replication.

### Class Activity Data (From L48-50 Slides)

| Trt | A | B | C | Response |
|-----|---|---|---|----------|
| (1) | −1 | −1 | −1 | 13.6 |
| a | 1 | −1 | −1 | 15.2 |
| b | −1 | 1 | −1 | 13.9 |
| ab | 1 | 1 | −1 | 14.6 |
| c | −1 | −1 | 1 | 14.9 |
| ac | 1 | −1 | 1 | 14.8 |
| bc | −1 | 1 | 1 | 11.8 |
| abc | 1 | 1 | 1 | 15.3 |

### Manual Effect Calculation for A

Using the contrast table (A has + for runs a, ab, ac, abc and − for runs (1), b, c, bc):

$$\text{Effect}_A = \frac{1}{n \cdot 2^{k-1}}[(15.2 + 14.6 + 14.8 + 15.3) - (13.6 + 13.9 + 14.9 + 11.8)]$$

$$= \frac{1}{4}[59.9 - 54.2] = \frac{5.7}{4} = 1.425$$

Similarly compute Effects for B, C, AB, AC, BC, ABC using the sign table.

### No-Replicate R Pattern (from `5-2kFD 3Factor.R`)

```r
df <- import("D2-2kFD 3Factor.xlsx") %>% as_tibble()

# No gather() — already one row per treatment combination
dft <- df %>%
  mutate_at(vars(-R1), as.factor) %>%   # R1 is the single observation column
  select(R1, everything())

lmmodel  <- dft %$% lm(R1 ~ A + B + AB + C + AC + BC + ABC)
aovmodel <- dft %$% aov(R1 ~ A * B * C)

lmmodel  %>% summary()
aovmodel %>% summary()

# Daniel plot — identify significant effects
library(FrF2)
DanielPlot(lmmodel)
```

### Reading the Daniel Plot

The Daniel plot places all 7 effect estimates (A, B, AB, C, AC, BC, ABC) on a normal probability scale.

- **Effects near the straight line:** consistent with random noise (not significant)
- **Effects falling far off the line:** real, systematic effects (include in reduced model)

Exam scenario: "Based on the Daniel plot, which effects would you include in the reduced model?"

Answer: List the 1–3 effects that fall noticeably off the line. Refit the model with only those terms. The remaining effects become the error estimate.

---

## Key Exam Formulas Summary

| Quantity | Formula | Notes |
|---------|---------|-------|
| Effect | Contrast / (n·2^(k−1)) | = difference in means between high and low |
| SS for effect | Contrast² / (n·2^k) | each effect has df = 1 |
| lm() coefficient | Effect / 2 | **double** to get effect |
| df_error (replicated) | 2^k·(n−1) | requires n ≥ 2 |
| df_error (unreplicated) | 0 | → use Daniel plot |

---

## Related
- [[2k-factorial-design]] — concept and formula page
- [[factorial-anova-r]] — R code including `DanielPlot()` pattern
- [[factorial-examples]] — 2-factor and 3-factor with replication

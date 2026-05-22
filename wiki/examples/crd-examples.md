---
tags: [example, unit-5]
tier: script
sources: [L42-43_App_HWK_Q1.R, L42-43_App_HWK_Q2.R, L42&43P]
---
# Example: CRD One-Way ANOVA

---

## Problem 1 — Balanced CRD (Rodding Level vs Concrete Strength)

### Problem Statement
A study from the ACI Materials Journal (Vol. 84, 1987) investigated the effect of rodding level on the compressive strength of concrete cylinders. Four rodding levels were tested, with 3 observations per treatment.

### Given / Find
- **Factor:** Rodding Level (4 treatments)
- **Response:** Compressive Strength (psi)
- **Design:** Balanced CRD, a = 4, n = 3, N = 12
- **Find:** F₀, p-value, normality check, constant variance check

### Solution

**Step 1 — Import and reshape data**

Excel layout: Row 1 is a label row; columns are RoddingLevel, Obs1, Obs2, Obs3.

```r
pacman::p_load(agricolae, magrittr, pacman, reshape2, rio, tidyverse)

df <- import("Lesson 42&43 App HWK Q1.xlsx") %>%
  slice(-1) %>%                          # drop the "Observations" header row
  select(1:4) %>%
  setNames(c("RoddingLevel", "Obs1", "Obs2", "Obs3")) %>%
  mutate(RoddingLevel = as.factor(RoddingLevel),
         across(Obs1:Obs3, as.numeric)) %>%
  as_tibble()

dft <- df %>%
  melt(id.vars = "RoddingLevel",
       variable.name = "Obs",
       value.name = "Strength")
```

**Step 2 — Fit model and get ANOVA table**

```r
model <- dft %$%
  aov(Strength ~ RoddingLevel)

model %>% summary()
```

**Step 3 — Extract answers**

```r
s    <- summary(model)
f0   <- s[[1]][["F value"]][1]
pval <- s[[1]][["Pr(>F)"]][1]

cat(sprintf("F0 = %.2f\n", f0))
cat(sprintf("P-value = %.2f\n", pval))
```

**Step 4 — Check assumptions**

```r
model %>% plot()   # advance through 4 plots with Enter
```

- **Plot 2 (Normal Q-Q):** Points should follow the diagonal — checks normality
- **Plot 1 (Residuals vs Fitted):** Spread should be roughly equal across all 4 treatment means — checks constant variance

**Step 5 — Fisher's LSD**

```r
model %>% LSD.test("RoddingLevel") %>% print()
```

### Interpreting the Output

| R Output | Meaning | Teacher's Phrasing |
|----------|---------|---------------------|
| `F value` row 1 | F₀ = MS_Trt / MS_E | "The test statistic is F₀ = X.XX" |
| `Pr(>F)` row 1 | p-value for treatment effect | "The p-value is X.XX" |
| p-value < 0.05 | Reject H₀ | "There is sufficient evidence that rodding level affects compressive strength at α = 0.05." |
| p-value ≥ 0.05 | Fail to reject H₀ | "There is insufficient evidence that rodding level affects compressive strength at α = 0.05." |
| Q-Q plot points on line | Normality assumption reasonable | "True" |
| Residuals vs Fitted — no fan pattern | Constant variance reasonable | "True" |

---

## Problem 2 — Unbalanced CRD (Carbon Material vs Surface Roughness)

### Problem Statement
A study from Lubrication Engineering (Dec. 1990) investigated the effect of carbon material type on surface roughness. Four materials were tested, but with **unequal** sample sizes.

### Given / Find
- **Factor:** Material type (4 levels: EC10, EC10A, EC4, EC1)
- **n per group:** EC10 n=4, EC10A n=6, EC4 n=3, EC1 n=2; **N=15** total
- **Design:** Unbalanced CRD
- **Find:** F₀, p-value, constant variance check, 95% CI on μ_EC10 − μ_EC1

### Three Exam Traps

> **Trap 1:** `col_names = FALSE` — the Excel file has no usable column header row; pass this argument to `rio::import()` or it will misread the data.

> **Trap 2:** `filter(!is.na(Roughness))` — unequal group sizes mean the Excel layout has NA cells as filler. After `melt()`, these NA rows must be dropped before fitting the model.

> **Trap 3:** Manual CI uses group-specific n — the unbalanced CI formula requires `1/n_i + 1/n_j` with **individual** group sizes from `tapply()`, not a single shared n.

### Solution

**Step 1 — Import and reshape (unbalanced pattern)**

```r
df <- import("L42 & 43 App Hwk Q2.xlsx", col_names = FALSE) %>%
  slice(-1) %>%                                    # drop header row
  setNames(c("Material", "R1", "R2", "R3", "R4", "R5", "R6")) %>%
  mutate(Material = as.factor(Material),
         across(R1:R6, as.numeric)) %>%
  as_tibble()

dft <- df %>%
  melt(id.vars = "Material",
       variable.name = "Rep",
       value.name = "Roughness") %>%
  filter(!is.na(Roughness))   # REQUIRED: drop NA filler from unequal-n layout
```

**Step 2 — Fit model**

```r
model <- dft %$%
  aov(Roughness ~ Material)

model %>% summary()
model %>% plot()

model %>% LSD.test("Material") %>% print()
```

**Step 3 — 95% CI on μ_EC10 − μ_EC1**

```r
s      <- summary(model)
MSE    <- s[[1]][["Mean Sq"]][2]
df_e   <- s[[1]][["Df"]][2]

means  <- tapply(dft$Roughness, dft$Material, mean)
ns     <- tapply(dft$Roughness, dft$Material, length)
t_crit <- qt(0.975, df_e)

diff_means <- means["EC10"] - means["EC1"]
se_diff    <- sqrt(MSE * (1/ns["EC10"] + 1/ns["EC1"]))  # unbalanced formula
lower      <- diff_means - t_crit * se_diff
upper      <- diff_means + t_crit * se_diff

cat(sprintf("95%% CI on (mu_EC10 - mu_EC1): [%.3f, %.3f]\n", lower, upper))
```

### Interpreting the Output

| R Output | Meaning | Teacher's Phrasing |
|----------|---------|---------------------|
| `Pr(>F)` < 0.05 | Reject H₀ | "There is sufficient evidence that material type affects mean surface roughness at α = 0.05." |
| CI does not contain 0 | EC10 mean differs from EC1 mean | "We are 95% confident that the mean roughness for EC10 is between [lower] and [upper] units higher than EC1." |
| Residuals vs Fitted — roughly equal spread | Constant variance reasonable | "True" |

### Answer
The 95% CI on μ_EC10 − μ_EC1 is [lower, upper]. Since the interval **excludes 0**, EC10 has significantly higher mean surface roughness than EC1 at the 95% confidence level.

---

## Related
- [crd-one-way-anova](../concepts/crd-one-way-anova.md) — concept and formula page
- [anova-r](../r-code/anova-r.md) — full R workflow with output table

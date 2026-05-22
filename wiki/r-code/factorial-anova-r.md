---
tags: [r-code, section-4]
tier: script
sources: [1-TwoFactor.R, 2-ThreeFactor.R, 3-FourFactor.R, 4-2kFD 2Factor.R, 5-2kFD 3Factor.R, 6-2kFD 5Factor.R]
---
# R: Factorial ANOVA and 2^k Factorial Design

## Purpose
Run 2-factor through 4-factor factorial ANOVA and 2^k factorial designs in R. Covers the `gather()` reshape pattern, `aov()` with interaction (`*`), `lm()` with ±1 coded factors, and `FrF2::DanielPlot()` for unreplicated screening designs.

---

## 2-Factor Factorial Template

```r
pacman::p_load(
  magrittr,    # %$% exposition pipe
  rio,         # import()
  tidyverse    # gather(), mutate_if(), ggplot
)

# Import: F2 values as row labels, F1 levels as column headers, obs as cell values
df <- import("D1-2Factor.xlsx") %>%
  as_tibble()

# Reshape wide → tall using gather() (different from melt() used in CRD)
dft <- df %>%
  gather(F1, obs, -F2) %>%          # F1 = new column name for keys; obs = value; -F2 keeps F2 as ID
  mutate_if(is.character, as.factor) %>%   # convert all character columns to factors
  select(obs, F1, F2) %>%
  as_tibble()

# Fit factorial ANOVA — * includes all main effects AND interaction
model <- dft %$%
  aov(obs ~ F1 * F2)   # expands to: F1 + F2 + F1:F2

model %>% summary()
model %>% plot()
```

---

## 3-Factor and 4-Factor Factorial

Same pattern, more factors:

```r
# 3-factor: aov(obs ~ F1 * F2 * F3)
# 4-factor: aov(obs ~ F1 * F2 * F3 * F4)
# R expands * to all main effects + all 2-way + all 3-way + ... interactions automatically
```

The gather step for 3-factor: gather one factor at a time, keeping others as ID columns.

---

## 2^k Factorial — With Replication

When data has ±1 coded factor columns and replicate columns (R1, R2, ...):

```r
# 2^2 design with 4 replicates
df <- import("D2-2kFD 2Factor.xlsx") %>%
  as_tibble()

# Gather replicates into obs column, keep factor code columns
dft <- df %>%
  gather(R, obs, R1:R4) %>%                    # gather replicate columns
  mutate_at(vars(-obs), as.factor) %>%          # convert everything except obs to factor
  select(obs, everything(), -c("Treatment", "Identity", R))   # drop index columns

# Run both lm() and aov()
lmmodel  <- dft %$% lm(obs ~ A + B + AB)    # regression: coefficients = Effect/2
aovmodel <- dft %$% aov(obs ~ A * B)         # ANOVA: F-tests per source

lmmodel  %>% summary()   # shows coefficients (= Effect/2), t-tests
aovmodel %>% summary()   # shows SS, MS, F, p-value per source
```

---

## 2^k Factorial — No Replication (5-Factor Example)

When n=1 (single replicate), there are no replicate columns to gather. The data already has one row per treatment combination.

```r
df <- import("D2-2kFD 5Factor.xlsx") %>%
  as_tibble()

## gather(R, obs, c(R1:RX)) %>%  ## NO — no replications = no gather

dff <- df %>%
  mutate_at(vars(-"obs"), as.factor) %>%     # all columns except obs become factors
  select(obs, everything(), -Treatment, -Identity) %>%
  as_tibble()

# Build multiple models of increasing complexity
lmmodel  <- dff %$% lm(obs ~ A+B+C+D+E + AB+AC+AD+AE+BC+BD+BE+CD+CE+DE)
lmmodel2 <- dff %$% lm(obs ~ A*B*C*D*E)
lmmodel3 <- dff %$% lm(obs ~ A+B+AB+C+AC+BC+ABC+D+AD+BD+ABD+CD+ACD+BCD+ABCD +
                               E+AE+BE+ABE+CE+ACE+BCE+ABCE+DE+ADE+BDE+ABDE+CDE+ACDE+BCDE+ABCDE)

lmmodel  %>% summary()
lmmodel2 %>% summary()
lmmodel3 %>% summary()

# Daniel plot — identify significant effects without replication
p_load(FrF2)
DanielPlot(lmmodel2)    # effects off the line are significant
DanielPlot(lmmodel3)
```

---

## `trimws()` — Mandatory After `summary(fit)[[1]]`

R pads ANOVA row names with trailing whitespace. Any named lookup returns `NA` without `trimws()`:

```r
aov_tbl <- summary(fit)[[1]]
rownames(aov_tbl) <- trimws(rownames(aov_tbl))   # ALWAYS add this line

# Now safe to extract by name:
MS_A <- aov_tbl["A", "Mean Sq"]
F_AB <- aov_tbl["A:B", "F value"]
```

This applies to every two-factor and higher ANOVA script — `trimws()` is not optional.

---

## LSD After Factorial ANOVA (`agricolae::LSD.test`)

When the interaction is non-significant, apply Fisher's LSD to marginal means of the significant factor:

```r
pacman::p_load(agricolae)

# group = TRUE returns letter groupings (a, b, ab, ...)
lsd_result <- LSD.test(fit, "FactorB", group = TRUE)
lsd_result$groups     # mean + letter group per level
lsd_result$statistics # LSD value, df, MSE
```

The LSD formula uses df_E = ab(n−1) and n_marginal = a·n (total observations per marginal level). Compare pairs: if their means differ by more than LSD, the pair is significant.

---

## `pivot_longer()` for 2- and 3-Replicate 2^k Data

When replicate columns (R1, R2, or R1, R2, R3) are present, use `pivot_longer()` before fitting:

```r
# 2-replicate (2^3 design)
dft <- df %>%
  pivot_longer(cols = c(R1, R2), names_to = "Rep", values_to = "Response") %>%
  mutate_at(vars(-Response), as.factor)

# 3-replicate (2^2 design)
dft <- df %>%
  pivot_longer(cols = c(R1, R2, R3), names_to = "Rep", values_to = "Response") %>%
  mutate_at(vars(-Response), as.factor)

# Then standard aov() — works identically for n=2 or n=3
fit <- aov(Response ~ A * B, data = dft)   # 2^2
fit <- aov(Response ~ A * B * C, data = dft)  # 2^3

aov_tbl <- summary(fit)[[1]]
rownames(aov_tbl) <- trimws(rownames(aov_tbl))
```

`pivot_longer()` and `gather()` are interchangeable here; `pivot_longer()` is the tidyverse successor.

---

## Worked Problem Key Results

| Problem | Design | Key Finding |
|---------|--------|-------------|
| Viscosity (Q1) | 2-factor, a×b, n=? | F_pH=6.44 sig, F_cat=0.00 not sig, F_int=25.22 sig; F_crit(0.05,1,12)=4.747 → interaction drives everything |
| Warping (Q4) | 2-factor, Cu%×Temp | F_Temp=7.67, F_Cu=34.33 sig; F_Int=1.86 not sig; LSD=2.76; significant pairs: 40v60, 40v80, 40v100, 60v100, 80v100 |
| Root vole (Q2, 2^2) | 2^2, n=3 | MS_Error=1835 (high variance in no-predator cell); F_Food=0.97, F_Pred=5.08 both non-sig at α=0.05; F_crit(1,8)=5.318 |

---

## Key Reshape Patterns — `gather()` vs `melt()`

| Function | Package | Used in | Result |
|----------|---------|---------|--------|
| `melt()` | `reshape2` | CRD, RCBD | columns named `variable` and `value` |
| `gather(key, value, -id_cols)` | `tidyverse` | Factorial, 2^k | columns named by you |

Both produce long-format data. Use whichever matches the script you're working from.

---

## Factor Conversion Patterns

| Code | What it does |
|------|-------------|
| `mutate_if(is.character, as.factor)` | Convert **all** character columns to factors (used after `gather()` which produces character labels) |
| `mutate_at(vars(-obs), as.factor)` | Convert **every column except obs** to factor (used in 2^k scripts where obs must stay numeric) |

---

## DanielPlot Output Interpretation

`FrF2::DanielPlot(lmmodel)` plots all regression coefficients (= Effect/2) on a normal probability plot.

- **Effects near the diagonal line:** consistent with random noise — likely not significant
- **Effects far from the line (outliers):** real effects that differ systematically from noise
- Include the off-line effects in your reduced model; pool the rest as error

Teacher's phrasing: "Based on the Daniel plot, effects A, B, and AB appear significant (they fall off the normal probability line). The remaining effects are consistent with random variation and are pooled as error."

---

## Output Walkthrough: `lm()` vs `aov()` Side by Side

### `summary(lmmodel)` — Coefficients Table
| Column | Meaning | Relationship to Effect |
|--------|---------|----------------------|
| `Estimate` | β̂ = Effect/2 | **Double this to get the effect** |
| `Std. Error` | SE of β̂ | |
| `t value` | t₀ = β̂/SE | significant if |t| > t_{α/2} |
| `Pr(>|t|)` | two-sided p-value | |

### `summary(aovmodel)` — ANOVA Table
| Column | Meaning | Teacher's term |
|--------|---------|----------------|
| `Df` | degrees of freedom | df |
| `Sum Sq` | SS for this source | SS |
| `Mean Sq` | MS = SS/df | MS |
| `F value` | F₀ = MS/MS_E | F₀ |
| `Pr(>F)` | p-value | p-value |

---

## When to Use This vs Alternatives
- **`aov()` with `*`**: always for factorial ANOVA — produces the standard ANOVA table
- **`lm()` with ±1 coded columns**: use when asked for regression equation, coefficient estimates, or when effect ↔ coefficient conversion is needed
- **`DanielPlot()`**: only for unreplicated 2^k designs (n=1 per treatment combination)
- For CRD / RCBD: see [[anova-r]]

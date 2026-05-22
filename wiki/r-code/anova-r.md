---
tags: [r-code, unit-5]
tier: script
sources: [CRD.R, RCBD.R, L42-43_App_HWK_Q1.R, L42-43_App_HWK_Q2.R, L44-45_App_HWK_Q1.R]
---
# R: CRD and RCBD ANOVA

## Purpose
Run one-way ANOVA (CRD) and randomized complete block design (RCBD) in R. Extract F₀, p-value, MSE, and pairwise comparisons using Fisher's LSD.

## The Five-Step Pattern (Every ANOVA Script)

```
1. p_load()       — load packages
2. import()       — read Excel data
3. melt()         — wide → tall format
4. aov()          — fit ANOVA model (with %$% pipe)
5. summary() + plot() + LSD.test()  — analyze
```

---

## CRD Template

```r
pacman::p_load(
  agricolae,   # LSD.test()
  magrittr,    # %$% exposition pipe
  pacman,
  reshape2,    # melt()
  rio,         # import()
  tidyverse
)

# Import: Excel layout = treatments as columns, equal-length rows of observations
df <- import("data.xlsx") %>%
  as_tibble()

# Reshape wide → tall
dft <- df %>%
  melt() %>%   # creates columns: variable (treatment), value (observation)
  print()

# Fit ANOVA model
model <- dft %$%                     # %$% unpacks df so aov() sees named vectors
  aov(value ~ variable)              # column names from melt() output

# Full ANOVA table
model %>% summary()

# Diagnostic plots (press Enter to advance through 4 plots)
model %>% plot()

# Fisher LSD multiple comparisons
model %>%
  LSD.test("variable") %>%          # argument must match factor column name
  print()
```

---

## RCBD Template

```r
# Import: treatments as columns, blocks as rows (no block label column)
df <- import("RCBDData.xlsx") %>%
  as_tibble()

a <- df %>% ncol()   # number of treatments
n <- df %>% nrow()   # number of blocks

# Reshape and add block labels
dft <- df %>%
  melt() %>%
  mutate(blk = as.factor(rep(1:n, a))) %>%   # create block ID column
  select(obs = value, trt = variable, blk) %>%
  as_tibble()

# Fit RCBD model — NOTE: + not * (no interaction term in RCBD)
model <- dft %$%
  aov(obs ~ trt + blk)

model %>% summary()
model %>% plot()

model %>%
  LSD.test("trt") %>%              # only compare on treatment, not block
  print()
```

---

## Unbalanced CRD (HW Q2 Pattern)

```r
# col_names = FALSE required when Excel has no header row usable as column names
df <- import("data.xlsx", col_names = FALSE) %>%
  slice(-1) %>%                                    # drop header row
  setNames(c("Material", "R1", "R2", "R3", "R4", "R5", "R6")) %>%
  mutate(Material = as.factor(Material),
         across(R1:R6, as.numeric)) %>%
  as_tibble()

dft <- df %>%
  melt(id.vars = "Material",
       variable.name = "Rep",
       value.name = "Roughness") %>%
  filter(!is.na(Roughness))   # drop NA filler cells from unequal-n Excel layout

model <- dft %$%
  aov(Roughness ~ Material)
```

---

## Extracting Scalars from Summary Output

```r
s <- summary(model)

# F0 and p-value (row 1 = treatments row)
f0  <- s[[1]][["F value"]][1]
pv  <- s[[1]][["Pr(>F)"]][1]

# MSE and error df (row 2 = error row)
MSE  <- s[[1]][["Mean Sq"]][2]
df_e <- s[[1]][["Df"]][2]

# 95% CI on pairwise difference (unbalanced)
means  <- tapply(dft$Roughness, dft$Material, mean)
ns     <- tapply(dft$Roughness, dft$Material, length)
t_crit <- qt(0.975, df_e)

diff_means <- means["Grp1"] - means["Grp2"]
se_diff    <- sqrt(MSE * (1/ns["Grp1"] + 1/ns["Grp2"]))
lower      <- diff_means - t_crit * se_diff
upper      <- diff_means + t_crit * se_diff
```

---

## The `%$%` Exposition Pipe — Why It's Needed

`aov(value ~ variable)` expects `value` and `variable` to be **named vectors** in the current environment, not columns of a data frame. The standard `%>%` pipe passes the whole data frame as the first argument, which doesn't work with `aov()`. The `%$%` pipe (from `magrittr`) **exposes** all columns of the data frame as individual named objects, so `aov()` can find them by name.

```r
dft %$% aov(value ~ variable)   # works: value and variable are exposed as vectors
dft %>% aov(value ~ variable)   # fails: aov() receives a data frame, not vectors
```

---

## `melt()` vs `gather()` — Two Ways to Go Wide→Tall

Both produce the same long-format result. The CRD/RCBD templates above use `melt()` from `reshape2`. Factorial scripts use `gather()` from `tidyverse`.

```r
# melt() — used in CRD.R and RCBD.R
df %>% melt()
# Result: columns named "variable" and "value"

# gather() — used in factorial drill scripts
df %>% gather(F1, obs, -F2)
# Result: columns named "F1" (key) and "obs" (value); -F2 keeps F2 as ID column
```

---

## Output Walkthrough Table

| R output column | Meaning | Teacher's term |
|-----------------|---------|----------------|
| `Df` | Degrees of freedom | df |
| `Sum Sq` | Sum of squares | SS |
| `Mean Sq` | Mean square = SS/df | MS |
| `F value` | F₀ = MS_Trt / MS_E | F₀ or test statistic |
| `Pr(>F)` | p-value for the F-test | p-value |
| Row 1 (treatments) | Treatment source of variation | Treatments |
| Row 2 (residuals) | Error source of variation | Error |

**Residual plot guide:**
| Plot | R label | What to check |
|------|---------|----------------|
| 1 | Residuals vs Fitted | Constant variance — spread roughly equal across treatments |
| 2 | Normal Q-Q | Normality — points follow the diagonal line |
| 3 | Scale-Location | Constant variance (alternate) |
| 4 | Cook's Distance | Influential observations |

---

---

## Random Effects Model — Extraction and Variance Components

The ANOVA table is identical to CRD. The difference is what you extract and report.

### Named-Row Extraction (Preferred for Random Effects)

When the factor name is known, index the ANOVA table by name rather than position — safer and self-documenting:

```r
# After: model <- df %$% aov(Yield ~ Batch)
aov_tbl <- summary(model)[[1]]

# Named-row extraction — row name matches the factor variable name in aov()
MS_Batch <- aov_tbl["Batch",     "Mean Sq"]
MS_E     <- aov_tbl["Residuals", "Mean Sq"]
SS_E     <- aov_tbl["Residuals", "Sum Sq"]
df_e     <- aov_tbl["Residuals", "Df"]
F0       <- aov_tbl["Batch",     "F value"]
pv       <- aov_tbl["Batch",     "Pr(>F)"]
```

Compare to the **positional extraction** used in the CRD/unbalanced patterns above:
```r
# Positional — works for any 2-row ANOVA table but hides intent
f0  <- s[[1]][["F value"]][1]    # row 1 = treatments
MSE <- s[[1]][["Mean Sq"]][2]    # row 2 = error
```

**Rule of thumb:** use named-row when reporting random effects (the names serve as documentation); use positional when writing generic extraction code for any design.

### Variance Component Calculation

```r
n <- 5   # observations per factor level (balanced design only)

# sigma^2 hat — within-level variability
sigma2     <- MS_E

# sigma^2_tau hat — between-level variability
sigma2_tau <- (MS_Batch - MS_E) / n

# Proportion of total variability attributable to the factor
prop <- sigma2_tau / (sigma2_tau + sigma2)
cat(sprintf("sigma^2 hat     = %d  (within)\n",    round(sigma2)))
cat(sprintf("sigma^2_tau hat = %d  (between)\n",   round(sigma2_tau)))
cat(sprintf("Proportion due to factor = %.1f%%\n", prop * 100))
```

**Use case:** Report variance components instead of LSD pairwise comparisons when the factor is random (randomly sampled levels). Do not call `LSD.test()` on a random effects model.

**Negative σ̂²_τ:** If MS_E > MS_Treatments, the estimate is negative — treat it as zero (σ²_τ ≈ 0; the factor contributes no variance beyond noise).

---

## Normal Probability Plot of Residuals — ANOVA (Blom Positions)

Use this when a homework or exam asks for the normal probability plot. This is the **textbook-style** plot: residuals on X, cumulative probability on Y. It is different from the base-R `qqnorm()` / `ggplot stat_qq` plots (which put residuals on Y and theoretical quantiles on X).

```r
# Blom plotting positions: p_i = (i - 0.5) / n
e_sorted    <- sort(resid(model))
n_resid     <- length(e_sorted)
p_i         <- (seq_along(e_sorted) - 0.5) / n_resid
z_i         <- qnorm(p_i)   # convert to normal scores

prob_ticks  <- c(0.01, 0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95, 0.99)
z_ticks     <- qnorm(prob_ticks)
prob_labels <- c("1%", "5%", "10%", "25%", "50%", "75%", "90%", "95%", "99%")

p_qq <- ggplot(tibble(e = e_sorted, z = z_i), aes(x = e, y = z)) +
  geom_point(size = 2.5, color = "steelblue") +
  geom_smooth(method = "lm", se = FALSE, color = "red", linewidth = 0.9) +
  scale_y_continuous(breaks = z_ticks, labels = prob_labels) +
  labs(title = "Normal Probability Plot of Residuals",
       x = "Residuals",
       y = "Probability") +
  theme_bw()
print(p_qq)
```

**How to read:**
| Pattern | Conclusion |
|---------|-----------|
| Points track the red reference line | Residuals approximately normal — assumption satisfied |
| S-curve (heavy tails) | Non-normal — skewed or heavy-tailed distribution |
| Points bow above/below line at ends | Outliers at the extremes |

**Blom vs. `stat_qq` — which to use:**

| Approach | Axes | Used in | When |
|----------|------|---------|------|
| Blom positions (above) | X = residuals, Y = probability % | DOE homework (this course) | Textbook-style probability plot |
| `stat_qq + stat_qq_line` | X = theoretical quantiles, Y = residuals | Regression adequacy checks | Standard QQ plot |
| `model %>% plot()` | Varies | Quick checks | Exploratory / not for exam submission |

Both Blom and `stat_qq` test the same thing (normality of residuals). The Blom version matches the layout shown in the L38–39 and L44–45 lecture material.

---

## When to Use This vs Alternatives
- **CRD** (`aov(obs ~ trt)`): one factor, completely random assignment, no blocks
- **RCBD** (`aov(obs ~ trt + blk)`): one factor + nuisance block variable
- **Random effects** (`aov(obs ~ trt)`, same formula): use when factor levels are randomly sampled — report variance components, not pairwise means
- **Factorial** (`aov(obs ~ F1 * F2)`): two or more factors of equal interest — see [factorial-anova-r](factorial-anova-r.md)

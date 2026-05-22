---
tags: [r-code, unit-5]
tier: script
sources: [L44-45_App_HWK_Q3.R, L42-43_App_HWK_Q1.R, L42-43_App_HWK_Q2.R, RCBD.R]
---
# R: Data Wrangling — Wide to Long with melt()

## Why This Matters

`aov()` requires data in **long (tall) format**: one row per observation, one column for the response, one column for each factor. Homework tables and Excel files are almost always in **wide format**: one row per subject, each treatment in its own column. `melt()` from `reshape2` converts between them.

---

## melt() — The Core Pattern

### Before (wide format — matches the homework table)

CSV / data frame as imported:

```
Sample  Type1  Type2
1       1.3    2.2
2       1.6    2.4
3       0.5    0.4
4       1.2    2.0
5       1.1    1.8
```

Each row is a fabric sample. Each column is a chemical type. This matches the homework table layout exactly.

### The melt() Call

```r
df_wide <- import("L44-45_App_HWK_Q3.csv") %>% as_tibble()

df_long <- df_wide %>%
  melt(
    id.vars       = "Sample",        # column(s) that stay as-is (the "who")
    variable.name = "Type",          # new column: holds the old column names
    value.name    = "Strength"       # new column: holds the values
  ) %>%
  mutate(Sample = factor(Sample), Type = factor(Type))
```

### After (long format — what aov() needs)

```
Sample  Type   Strength
1       Type1  1.3
2       Type1  1.6
3       Type1  0.5
4       Type1  1.2
5       Type1  1.1
1       Type2  2.2
2       Type2  2.4
3       Type2  0.4
4       Type2  2.0
5       Type2  1.8
```

Each row is now one observation. `Sample` identifies the block. `Type` is the treatment factor. `Strength` is the response.

---

## The Three melt() Arguments

| Argument | What it does | If omitted |
|----------|-------------|------------|
| `id.vars` | Columns to keep as identifier columns — not stacked | All columns are stacked; no ID column |
| `variable.name` | Name for the new column that holds the old column names | Defaults to `"variable"` |
| `value.name` | Name for the new column that holds the cell values | Defaults to `"value"` |

**Rule of thumb:** `id.vars` = the column that labels *who* or *which block*. Everything else becomes a factor level in the long format.

---

## Keep Both Shapes When You Need Both

In Q3 (L44-45 HWK), the paired t-test needs the wide format (two separate vectors), while RCBD `aov()` needs long format. Import once wide, reshape for ANOVA, keep the wide version for the t-test:

```r
# Import wide — matches homework table
df_wide <- import("L44-45_App_HWK_Q3.csv") %>% as_tibble()

# Extract vectors directly from wide (for paired t-test)
type1 <- df_wide$Type1
type2 <- df_wide$Type2
t.test(type1, type2, paired = TRUE)

# Reshape to long (for RCBD ANOVA)
df_long <- df_wide %>%
  melt(id.vars = "Sample", variable.name = "Type", value.name = "Strength") %>%
  mutate(Sample = factor(Sample), Type = factor(Type))

df_long %$% aov(Strength ~ Type + Sample) %>% summary()
```

---

## Variations by Data Layout

### No explicit ID column (RCBD.R pattern)

When the Excel file has no Subject/Block column — just treatment columns — melt() still works; block IDs are added afterward:

```r
df_wide <- import("RCBDData.xlsx") %>% as_tibble()
# df_wide has columns: Trt1, Trt2, Trt3 (no Sample column)

a <- ncol(df_wide)   # number of treatments
b <- nrow(df_wide)   # number of blocks

df_long <- df_wide %>%
  melt() %>%                                       # variable.name defaults to "variable"
  mutate(blk = factor(rep(1:b, a))) %>%            # add block IDs manually
  select(obs = value, trt = variable, blk)
```

### With NA filler (unbalanced CRD — L42-43 Q2 pattern)

Unequal group sizes leave NA cells in wide Excel layouts. Drop them after melting:

```r
df_long <- df_wide %>%
  melt(id.vars = "Material", variable.name = "Rep", value.name = "Roughness") %>%
  filter(!is.na(Roughness))    # drop NA rows from unequal-n layout
```

---

## melt() vs pivot_longer()

Both do the same thing. `melt()` (reshape2) is used throughout this course's scripts; `pivot_longer()` (tidyverse) is the modern replacement but either works.

```r
# melt() — used in all course scripts
df %>% melt(id.vars = "Sample", variable.name = "Type", value.name = "Strength")

# pivot_longer() — equivalent, tidyverse style
df %>% pivot_longer(cols = -Sample, names_to = "Type", values_to = "Strength")
```

Output is identical. Stick with `melt()` to stay consistent with existing course scripts.

---

## Related
- [anova-r](anova-r.md) — full CRD and RCBD templates using melt()
- [factorial-anova-r](factorial-anova-r.md) — factorial scripts use gather() instead of melt()
- [crd-examples](../examples/crd-examples.md) — unbalanced import pattern with melt() + filter(!is.na())
- [hw4-drill-examples](../examples/hw4-drill-examples.md) — tsibble and uncount() patterns for time series and frequency tables
- [taxonomy](../concepts/taxonomy.md) — tier guide: this page is Tier 3 / Script

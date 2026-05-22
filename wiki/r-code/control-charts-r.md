---
tags: [r-code, section-3]
tier: script
sources: [Control Charts.R, ControlCharts_Homework.R, Attribute Chart.R, Process Capability.R]
---
# R: Control Charts (qcc package)

## Purpose
Build X̄/R, X̄/S, p-chart, c-chart, u-chart, and process capability using the `qcc` package.

## Setup

```r
pacman::p_load(pacman, qcc, rio, tidyverse)

# Data format: rows = subgroups, columns = observations within subgroup
df <- import("data.xlsx") %>%
  as_tibble() %>%
  print()
```

---

## Variables Charts (X̄/R and X̄/S)

```r
# ─── Step 1: R Chart (ALWAYS first) ─────────────────────────────────────────
qqR <- df %>%
  qcc(type = "R", nsigmas = 3, title = "R Chart")

# ─── Step 2: X̄ Chart from R (sigma estimated from R chart) ─────────────────
qqX <- df %>%
  qcc(type = "xbar", nsigmas = 3, title = "Xbar Chart",
      std.dev = sd.R(df))    # use sd.S(df) to use S chart instead

# ─── Optional: S Chart ───────────────────────────────────────────────────────
qqS <- df %>%
  qcc(type = "S", nsigmas = 3, title = "S Chart")
```

**Output Walkthrough:**

| Output element | Meaning | Teacher's Term |
|----------------|---------|----------------|
| `center` | x̄̄ or R̄ or s̄ (center line) | Grand mean / Average range |
| `std.dev` | σ̂ estimated from chart | Process standard deviation |
| `limits` | [LCL, UCL] | Control limits |
| Plotted points | Each subgroup x̄ᵢ or Rᵢ | Subgroup statistic |
| Red points | Out-of-control signals | Out-of-control points |

---

## Removing Out-of-Control Points and Revising Limits

```r
# Identify out-of-control subgroup numbers (from chart output)
ooc <- c(18, 20)    # subgroup numbers that are out of control

# Remove those rows and refit
df_rev <- df[-ooc, ]

qqR_Rev <- df_rev %>%
  qcc(type = "R", nsigmas = 3, title = "Revised R Chart")

qqX_Rev <- df_rev %>%
  qcc(type = "xbar", nsigmas = 3, title = "Revised Xbar Chart")
```

---

## Applying Specified/Known Limits

```r
# Use known (specified) control limits instead of estimating from data
q1 <- df %>%
  qcc(type = "xbar", limits = c(LCL_value, UCL_value))
```

---

## Attribute Charts (p, c, u)

```r
# ─── p-Chart (fraction defective) ────────────────────────────────────────────
# Inputs: D = number of defectives per subgroup, sizes = sample size per subgroup
ccP <- qcc(data = df$D, type = "p", sizes = df$size, title = "P Chart")

# ─── c-Chart (defects per unit, fixed n) ─────────────────────────────────────
ccC <- qcc(data = counts_vec, type = "c", title = "C Chart")

# ─── u-Chart (defects per unit, variable n) ──────────────────────────────────
ccU <- qcc(data = df$x, type = "u", sizes = df$size, title = "U Chart")
```

**Built-in dataset examples:**
```r
data("orangejuice")    # for p-chart example (D and size columns)
data("circuit")        # for c/u-chart example (x and size columns)
```

---

## Process Capability

```r
# Build X-bar chart first (sigma estimated from R chart)
qqX <- qcc(data = df, type = "xbar", nsigmas = 3, std.dev = sd.R(df))

# Compute capability indices (LSL = lower spec, USL = upper spec)
pc <- process.capability(qqX, spec.limits = c(LSL, USL))
print(pc, digits = 10)

# Off-centered: specify target ≠ spec midpoint
pc_off <- process.capability(qqX, spec.limits = c(LSL, USL), target = target_value)
print(pc_off, digits = 10)
```

**Reading `process.capability()` output:**

| Output | Meaning | Teacher's Term |
|--------|---------|----------------|
| `Cp` | (USL−LSL)/(6σ̂) | Process capability ratio |
| `Cpk` | min[(USL−μ̂)/3σ̂, (μ̂−LSL)/3σ̂] | Process capability index |
| `Cpm` | Accounts for deviation from target | Taguchi index |
| `Exp<LSL` / `Exp>USL` | Expected fraction nonconforming | Parts per million failing |

---

## Out-of-Control Check Pattern

```r
# Print control chart object to see which points are flagged
print(qqR)        # shows center, limits, and violations
qqR$violations    # numeric indices of out-of-control points
```

---

## Teacher-Language Output Guide

| Situation | What to say |
|-----------|------------|
| All points in limits, no patterns | "The process is in statistical control." |
| Point(s) outside limits | "Point(s) [#] fall outside the control limits, indicating the process is out of statistical control." |
| Cp ≥ 1.33 and Cpk ≥ 1.33 | "The process is capable of meeting specifications." |
| Cp ≥ 1.33 but Cpk < 1.33 | "The process spread is adequate but the process is off-center. The mean should be adjusted." |
| Cp < 1.33 | "The process is not capable of meeting specifications." |

---

## Related
- [[control-charts]]
- [[process-capability]]

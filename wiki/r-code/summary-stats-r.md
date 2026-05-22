---
tags: [r-code, section-1-2]
tier: script
sources: [L08P, Drill files, Section1&2 R scripts]
---
# R: Summary Statistics and Descriptive Analysis

## Purpose
Computing and interpreting descriptive statistics, building histograms and boxplots, and understanding the output in teacher-expected language.

## Setup

```r
pacman::p_load(pacman, rio, tidyverse)

df <- import("data.xlsx") %>%
  as_tibble() %>%
  print()
```

---

## Core Summary Statistics

```r
# All at once (5-number summary + mean)
summary(df$x)

# Individual statistics
n    <- length(df$x)             # sample size
xbar <- mean(df$x)               # sample mean x̄
s    <- sd(df$x)                 # sample standard deviation s
s2   <- var(df$x)                # sample variance s²
med  <- median(df$x)             # median (Q2)
q1   <- quantile(df$x, 0.25)    # first quartile Q1
q3   <- quantile(df$x, 0.75)    # third quartile Q3
iqr  <- IQR(df$x)                # interquartile range Q3-Q1
rng  <- diff(range(df$x))        # range = max - min
```

**Excel equivalents:**
| R | Excel |
|---|-------|
| `mean(x)` | `=AVERAGE(range)` |
| `median(x)` | `=MEDIAN(range)` |
| `sd(x)` | `=STDEV.S(range)` |
| `var(x)` | `=VAR.S(range)` |
| `max(x)-min(x)` | `=MAX(range)-MIN(range)` |

---

## Histogram

```r
ggplot(df, aes(x = x)) +
  geom_histogram(binwidth = 5, fill = "steelblue", color = "white", alpha = 0.8) +
  labs(title = "Histogram of X",
       x = "X values", y = "Frequency") +
  theme_bw()
```

**What to look for:**
- Bell shape → normal distribution reasonable
- Skewed right/left → note the skew
- Outliers → extreme values on one side

---

## Boxplot

```r
ggplot(df, aes(y = x)) +
  geom_boxplot(fill = "steelblue", alpha = 0.7) +
  labs(title = "Boxplot of X", y = "X values") +
  theme_bw()
```

**Reading a boxplot:**
| Box element | Statistical meaning |
|-------------|---------------------|
| Bottom of box | Q1 (25th percentile) |
| Middle line | Median (Q2, 50th percentile) |
| Top of box | Q3 (75th percentile) |
| Box height | IQR = Q3 − Q1 |
| Whiskers | 1.5·IQR from Q1 and Q3 |
| Points beyond whiskers | Potential outliers |

---

## Grouped Summary Statistics (Two Groups)

```r
df %>%
  group_by(group_var) %>%
  summarize(
    n    = n(),
    mean = mean(y),
    sd   = sd(y),
    var  = var(y),
    med  = median(y),
    q1   = quantile(y, 0.25),
    q3   = quantile(y, 0.75)
  )
```

---

## Computing Z-scores

```r
df <- df %>%
  mutate(z = (x - mean(x)) / sd(x))

# Or standardize against known μ and σ:
z0 <- (xbar - mu0) / (sigma / sqrt(n))    # test statistic for Z-test
```

---

## Standard Error of the Mean

```r
se <- sd(df$x) / sqrt(length(df$x))    # SE = s/√n
```

**Teacher's phrasing:** SE is the standard deviation of the sampling distribution of x̄.

---

## Importing Data Patterns

```r
# From Excel
df <- import("data.xlsx") %>% as_tibble()

# From CSV
df <- import("data.csv") %>% as_tibble()

# Renaming columns for regression
df <- df %>% select(y = Response_Col, x = Predictor_Col)

# Viewing
df %>% print()
df %>% glimpse()
```

## Related
- [[distributions]]
- [[hypothesis-tests-r]]
- [[reading-r-output]]

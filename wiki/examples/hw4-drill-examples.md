---
tags: [example, unit-1]
tier: script
sources: [Drill Homework 04_Ross.R, Drill_07_Demo_Ross.R]
---
# Examples: Data Wrangling — Time Series and Frequency Tables

See also: [data-wrangling-r](../r-code/data-wrangling-r.md), [summary-stats-r](../r-code/summary-stats-r.md)

---

## Problem 1 — AirPassengers: Time Series to Tidy Data

### Problem Statement
The built-in `AirPassengers` dataset records monthly airline passenger counts from 1949–1960. The raw dataset is a `ts` (time series) object — not a data frame. Convert it to a tidy tibble with proper columns, compute the annual average passenger count, and graph the trend.

### Given / Find
- **Dataset:** `AirPassengers` (R built-in, 144 monthly obs, 1949–1960)
- **Find:**
  1. Load as `tsibble` and make tidy (date, year, month, passengers columns)
  2. Compute average passengers per year
  3. Plot the yearly averages with a smoothing line

### Solution

**Step 1 — Load and inspect the raw data**

```r
pacman::p_load(datasets, lubridate, pacman, tidyverse, tsibble)

dfAP <- AirPassengers %>% as_tsibble() %>% print()
```

Output shows a `tsibble` with `index` (yearmonth) and `value` (passenger count). Not yet tidy — column names are generic.

**Step 2 — Make tidy: rename and extract date components**

```r
dfAP_ts <- AirPassengers %>%
  as_tsibble() %>%
  select(date = index, passengers = value) %>%
  mutate(
    year  = year(date),
    month = month(date)
  ) %>%
  select(date, year, month, passengers) %>%
  print()
```

Now each row is one month with named columns.

**Step 3 — Compute average passengers per year**

The `tsibble` structure prevents direct `group_by` — convert to plain `tibble` first.

```r
dfAP_yearly <- dfAP_ts %>%
  as_tibble() %>%
  group_by(year) %>%
  summarize(passenger_average = mean(passengers)) %>%
  ungroup() %>%
  print()
```

**Step 4 — Plot the yearly averages**

```r
dfAP_yearly %>%
  ggplot(aes(x = year, y = passenger_average)) +
  geom_line() +
  geom_point() +
  geom_smooth() +
  xlab("Year") +
  ylab("Average Number of Passengers") +
  ggtitle("Average Number of Air Passengers per Year") +
  scale_x_continuous(breaks = seq(1949, 1960, 1)) +
  scale_y_continuous(breaks = seq(100, 700, 100))
```

### Interpreting the Output

| Step | What you see | Why |
|------|-------------|-----|
| `as_tsibble()` | `index` + `value` columns | Raw `ts` class has no column names |
| `year(date)` / `month(date)` | Integer year/month | `lubridate` extracts from the `yearmonth` index |
| `as_tibble()` before `group_by` | Removes tsibble index | `tsibble` `summarize()` works differently; tibble is safer here |
| `geom_smooth()` with no method | Loess by default | `ggplot2` auto-picks loess for n < 1000 |

### Answer
Air passenger averages grow steadily from ~127/month in 1949 to ~476/month in 1960 — a consistent upward trend with a smooth loess fit confirming no changepoint.

---

## Problem 2 — Titanic: Frequency Table to Tidy Data

### Problem Statement
The built-in `Titanic` dataset is stored as a frequency table (each row = a group count, not an individual passenger). Convert it to a tidy one-row-per-passenger format, then compute and visualize the survival proportion by passenger class.

### Given / Find
- **Dataset:** `Titanic` (R built-in, 32 rows of frequencies across Class × Sex × Age × Survived)
- **Find:**
  1. Total passengers and total survivors
  2. Passenger count by class
  3. Survivor count by class
  4. Survival proportion by class (with bar chart)

### Solution

**Step 1 — Load and inspect raw format**

```r
dfT <- Titanic %>% as_tibble() %>% print()
```

Each row has `Class`, `Sex`, `Age`, `Survived`, and `n` (count). This is a **frequency table** — not tidy. Multiple rows represent the same kind of observation.

**Step 2 — Uncount: one row per passenger**

`uncount(n)` expands each row into `n` individual rows, removing the count column.

```r
dfT_tidy <- dfT %>%
  uncount(n) %>%
  print()
```

**Step 3 — Total counts**

```r
count(dfT_tidy)                                   # total passengers: 2201

dfT_tidy %>% filter(Survived == "Yes") %>% count() # survivors: 711
```

**Step 4 — Count by class**

```r
dfT_class_counts <- dfT_tidy %>%
  group_by(Class) %>%
  count() %>%
  print()
```

**Step 5 — Survivor count by class**

```r
dfT_survived_class_counts <- dfT_tidy %>%
  filter(Survived == "Yes") %>%
  group_by(Class) %>%
  count() %>%
  print()
```

**Step 6 — Join and compute proportion**

Use `left_join` to bring the two count columns together, then compute the proportion.

```r
dfT_combined <- dfT_class_counts %>%
  left_join(dfT_survived_class_counts,
            by = "Class",
            suffix = c("_total", "_survived")) %>%
  mutate(proportion_survived = n_survived / n_total) %>%
  print()
```

**Step 7 — Bar chart**

```r
dfT_combined %>%
  ggplot(aes(x = Class, y = proportion_survived)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  xlab("Passenger Class") +
  ylab("Proportion Survived") +
  ggtitle("Proportion of Titanic Passengers Survived by Class")
```

### Interpreting the Output

| Step | R Pattern | Why |
|------|-----------|-----|
| `as_tibble()` on `Titanic` | Converts 4D array to data frame | `Titanic` is a `table` object, not a data frame |
| `uncount(n)` | Expands count column | Goes from frequency table → individual observations |
| `suffix = c("_total", "_survived")` | Disambiguates matching column names | Both joined data frames have a column named `n` |
| `geom_bar(stat = "identity")` | Uses y as-is | Default `geom_bar` counts rows; `stat = "identity"` uses the y value directly |

### Answer

| Class | n_total | n_survived | proportion_survived |
|-------|---------|------------|---------------------|
| 1st   | 325     | 203        | 0.625               |
| 2nd   | 285     | 118        | 0.414               |
| 3rd   | 706     | 178        | 0.252               |
| Crew  | 885     | 212        | 0.240               |

First class had dramatically higher survival than crew or third class, consistent with historical accounts of preferential lifeboat access.

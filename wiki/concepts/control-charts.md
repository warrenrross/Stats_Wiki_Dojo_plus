---
tags: [concept, unit-4]
tier: procedure
sources: [L27P, L28P, L29P, Control Charts.R, ControlCharts_Homework.R]
---
# Control Charts (SPC)

## In Plain English
Statistical Process Control (SPC) uses control charts to monitor a process over time and detect when it goes out of control (a special cause has entered). If all points fall within limits and show no non-random patterns → process is **in statistical control** (only common cause variation).

---

## Purpose of a Control Chart

> A control chart enables **just-in-time adjustments** to reduce overall variability by signaling when to investigate.

A control chart does NOT:
- Eliminate chance (common cause) variation — that requires process redesign
- Monitor sample averages only — it monitors both mean (X̄ chart) and variability (R/S chart)
- Tell you what the problem is — it signals that investigation is needed

**A process is "out of control"** when it is operating in the presence of **assignable (special) causes** of variation — not chance causes. Chance causes are always present; assignable causes are not.

---

## The Control Limit Formula

$$UCL = \mu + k\sigma, \quad LCL = \mu - k\sigma$$

- **k** = distance of the control limits from the center line, expressed in **standard deviation units** (commonly k = 3)
- k = 3 gives approximately 0.27% false alarm rate for a normal process

---

---

## Types of Control Charts

| Chart | What it monitors | When to use |
|-------|-----------------|-------------|
| X̄ & R | Process mean + range | Subgroups n ≤ 10 |
| X̄ & S | Process mean + std dev | Larger subgroups |
| I/MR | Individual measurements + moving range | n = 1 per time point |
| p-chart | Fraction defective | Binary (defective/not), variable n allowed |
| c-chart | Count of defects per unit | Count data, fixed inspection unit |
| u-chart | Defects per unit | Count data, variable inspection unit |

**Always build the variation chart (R, S, or MR) first.** If it is out of control, the X̄ chart limits are unreliable.

**Underlying distributions:**
| Chart | Based on |
|-------|---------|
| X̄, R, S | Normal distribution (CLT applies for X̄ with n ≥ 4) |
| p-chart | **Binomial** distribution (binary: defective or not) |
| c-chart | **Poisson** distribution (count of defects, fixed n) |
| u-chart | **Poisson** distribution (count of defects per unit, variable n) |

---

## X̄ & R Chart

**Setup:** m subgroups of size n each. Compute x̄ᵢ and Rᵢ for each subgroup.

| Quantity | Formula |
|----------|---------|
| Grand mean | x̄̄ = Σx̄ᵢ/m |
| Average range | R̄ = ΣRᵢ/m |
| UCL (X̄ chart) | x̄̄ + A₂R̄ |
| LCL (X̄ chart) | x̄̄ − A₂R̄ |
| UCL (R chart) | D₄R̄ |
| LCL (R chart) | D₃R̄ |
| σ̂ (process std dev) | R̄/d₂ |

Constants A₂, D₃, D₄, d₂ depend on subgroup size n (from control chart constants table).

| Constant | Used in | Role |
|----------|---------|------|
| A₂ | X̄ chart limits | UCL/LCL = x̄̄ ± A₂R̄ |
| D₃ | R chart **LCL** | LCL = D₃R̄ |
| D₄ | R chart **UCL** | UCL = D₄R̄ |
| d₂ | σ̂ estimation | σ̂ = R̄/d₂ |

---

## X̄ & S Chart

| Quantity | Formula |
|----------|---------|
| Average std dev | s̄ = Σsᵢ/m |
| UCL (X̄ chart) | x̄̄ + A₃s̄ |
| LCL (X̄ chart) | x̄̄ − A₃s̄ |
| UCL (S chart) | B₄s̄ |
| LCL (S chart) | B₃s̄ |
| σ̂ | s̄/c₄ |

**S chart constants:**
| Constant | Used in | Role |
|----------|---------|------|
| A₃ | X̄ chart limits (with S) | UCL/LCL = x̄̄ ± A₃s̄ |
| B₄ | S chart **UCL** | UCL = B₄s̄ |
| B₃ | S chart **LCL** | LCL = B₃s̄ |
| c₄ | σ̂ estimation | σ̂ = s̄/c₄ |

---

## p-Chart (Fraction Defective)

| Quantity | Formula |
|----------|---------|
| Center line | p̄ = total defectives / total inspected |
| UCL | p̄ + 3√(p̄(1−p̄)/n) |
| LCL | p̄ − 3√(p̄(1−p̄)/n) → max(0, …) |

Note: if variable sample sizes, control limits vary by subgroup.

---

## c-Chart (Count of Defects, Fixed n)

| Quantity | Formula |
|----------|---------|
| Center line | c̄ = total defects / m |
| UCL | c̄ + 3√c̄ |
| LCL | c̄ − 3√c̄ → max(0, …) |

---

## u-Chart (Defects per Unit, Variable n)

| Quantity | Formula |
|----------|---------|
| Center line | ū = total defects / total units |
| UCL | ū + 3√(ū/n) |
| LCL | ū − 3√(ū/n) → max(0, …) |

---

## Out-of-Control Signals (Western Electric Rules)

**What a triggered WE rule means:**
> "There might be an assignable cause for variation that needs investigation." — the process may be out of control; it does NOT mean the process is definitely producing bad product, and it does NOT mean the process is optimized.

**Erratic data points vs patterns within limits:**
- Erratic points (OOC signals, triggered WE rules) → investigate for assignable cause
- All points within limits with no non-random patterns → process is in statistical control — variation is chance causes only

A process is **out of control** if any of:
1. One point outside 3σ limits
2. Two of three consecutive points outside 2σ limits (same side)
3. Four of five consecutive points outside 1σ limits (same side)
4. Eight consecutive points on the same side of the center line
5. Six consecutive points steadily increasing or decreasing

---

## Revised Control Limits

When out-of-control points are found:
1. Identify the special cause
2. Remove those subgroups from the data (`df_rev <- df[-ooc,]`)
3. Recompute control limits from the remaining in-control data
4. Apply revised limits to future monitoring

---

## Teacher's Phrasing

**In control:**
> "The process appears to be in statistical control. All points fall within the control limits and no non-random patterns are present."

**Out of control:**
> "Point(s) [#] fall outside the control limits [/ exhibit a non-random pattern], indicating the process is out of statistical control. A special cause of variation is present."

---

## Key Assumptions
- Rational subgrouping: samples within a subgroup should be from the same process condition
- Observations within subgroups are independent
- Normality assumed for variables charts (CLT helps for X̄ chart with n ≥ 4)

## Common Mistakes
- Building X̄ chart before checking R/S chart
- Not removing out-of-control points before revising limits
- Using specification limits as control limits (they are different!)
- Applying chart to non-stationary data without investigating

## Related
- [process-capability](process-capability.md)
- [control-charts-r](../r-code/control-charts-r.md)

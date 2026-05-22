---
tags: [example, section-3]
tier: script
sources: [ControlCharts_Homework.R, Process Capability.R, Attribute Chart.R, L28P X and RorS Control Charts, L30E Fraction Defective and PCR Example, control-charts, process-capability]
---
# Examples: Control Charts and Process Capability

See also: [control-charts](../concepts/control-charts.md), [process-capability](../concepts/process-capability.md), [control-charts-r](../r-code/control-charts-r.md)

> **Exam focus:** You will interpret charts and output — not write R code. Know chart characteristics, apply Western Electric Rules, read Cp/Cpk output, and distinguish control limits from specification limits.

---

## Chart Types Quick Reference

| Chart | What it monitors | Input data | Use when |
|-------|-----------------|-----------|---------|
| X̄ (Xbar) | Process **mean** | Subgroup means x̄ᵢ | Always paired with R or S chart |
| R | Process **variability** (range) | Subgroup ranges Rᵢ | Subgroup size n ≤ 10 |
| S | Process **variability** (std dev) | Subgroup std devs sᵢ | Larger subgroups; more sensitive than R |
| p | Fraction **defective** | # defectives / sample size | Binary outcome (defective or not), n can vary |
| c | Count of **defects** per unit | Defect count per unit | Count data, **fixed** inspection unit size |
| u | Defects **per unit** (variable) | Defect count + unit size | Count data, **variable** inspection unit size |

**Critical rule — always build the variability chart first:**
> Build the R (or S) chart before the X̄ chart. If the R/S chart is out of control, the X̄ chart control limits are **unreliable** because σ̂ is inflated by special causes.

---

## Control Limits vs. Specification Limits

| | Control Limits | Specification Limits |
|--|--------------|---------------------|
| Set by | **Data** — calculated as x̄̄ ± 3σ̂ | **Customer/engineering** — defines acceptable range |
| Purpose | Detect special cause variation (process going wrong) | Define product acceptability |
| Can they differ? | Yes — a process can be in control but produce out-of-spec product |
| Are they the same? | **Never** — confusing these is a serious mistake |

---

## Example 1 — Applying Western Electric Rules

**Given:** An X̄ chart with center line at 50, UCL = 56, LCL = 44 (3σ control limits). The 1σ and 2σ zone boundaries are at 52, 54 (above CL) and 48, 46 (below CL).

The last 12 plotted points (in order) are:
```
Point:   1    2    3    4    5    6    7    8    9    10   11   12
Value:  51   52   53   54   52   53   55   54   53   52   51   50
```

**Find:** Is this process in or out of control? Which rule(s) are triggered?

---

**Solution:**

Check each Western Electric Rule:

| Rule | Trigger | This data |
|------|---------|-----------|
| 1. One point outside 3σ | Any point > 56 or < 44 | No — max is 55 |
| 2. Two of three outside 2σ (same side) | 2 of 3 consecutive > 54 or < 46 | Points 6, 7, 8: values 53, 55, 54 — two of three exceed 54 ✓ **TRIGGERED** |
| 3. Four of five outside 1σ (same side) | 4 of 5 consecutive > 52 or < 48 | Points 4–8: 54, 52, 53, 55, 54 — four of five exceed 52 ✓ **TRIGGERED** |
| 4. Eight consecutive same side | Eight points all above or all below CL | Points 1–12: mix of above/below — No |
| 5. Six consecutive trending | Six steadily increasing or decreasing | Points 1–7: mostly increasing (51→55) — Yes, 7 points ✓ **TRIGGERED** |

**Answer:**
> "Points 6–8 trigger Rule 2 (two of three outside 2σ). Points 4–8 trigger Rule 3 (four of five outside 1σ). Points 1–7 exhibit a steady increasing trend (Rule 5). The process is **out of statistical control** — a special cause of variation is present."

---

## Example 2 — Reading R Output: Identifying OOC Points

**Given:** R output from `qcc()` on a process with 25 subgroups:

```
R Chart

Number of groups:  25
Center:  5.74
StdDev:  2.469
Control limits:
   LCL    UCL
  0.00   19.18

Beyond limits of control (rules 1 violated):
 Group  18 20
```

**Find:** Interpret this output. What action should be taken?

---

**Solution:**

- Center line (R̄) = 5.74 — this is the average within-subgroup range
- UCL = 19.18, LCL = 0 (LCL floored at 0 for R charts with small n)
- σ̂ from R chart = StdDev = 2.469 (this is R̄/d₂ for the subgroup size used)
- Subgroups 18 and 20 are **beyond the control limits** (their ranges exceed 19.18)

**Next step:** Find and investigate the special cause in subgroups 18 and 20. Remove those subgroups, recompute revised control limits from the remaining 23 subgroups, then rebuild the chart.

**Answer:**
> "Subgroups 18 and 20 fall outside the control limits on the R chart, indicating the process variability is out of statistical control at those time points. A special cause of variation is present. These subgroups should be investigated, removed, and revised control limits computed."

---

## Example 3 — Process Capability from R Output

**Given:** `process.capability()` output for a process with spec limits LSL = 1.3, USL = 1.7:

```
Process Capability Analysis

Call:
process.capability(object = qqX, spec.limits = c(1.3, 1.7))

Number of obs: 100    Target: 1.5
Mean: 1.491   StdDev: 0.04812

          Value
Cp        1.386
Cp_l      1.378
Cp_u      1.323
Cp_k      1.323
Cpm       1.357

Exp<LSL  0.01%   Obs<LSL  0.00%
Exp>USL  0.09%   Obs>USL  0.00%
```

**Find:** Interpret Cp and Cpk. Is the process capable? Is it centered?

---

**Solution:**

- **Cp = 1.386** — The process spread (6σ̂ = 6 × 0.0481 = 0.289) fits within the spec width (USL − LSL = 0.4) with a ratio of 1.386. This exceeds the typical 1.33 threshold → process spread is adequate.
- **Cpk = 1.323** — This is Cpk = min(Cp_l, Cp_u) = min(1.378, 1.323) = 1.323. Slightly below 1.33.
  - Since Cpk < Cp, the process is **slightly off-center** (mean = 1.491 is below target 1.5).
  - Cpk = 1.323 is just under the 1.33 threshold.
- **Expected fraction nonconforming:** ~0.10% (Exp < LSL 0.01% + Exp > USL 0.09%)

**Answer:**
> "Cp = 1.386 indicates adequate process spread relative to specifications. However, Cpk = 1.323 < Cp indicates the process is slightly off-center (mean = 1.491 vs target = 1.500). Cpk is just below the 1.33 threshold, suggesting the process is marginally not capable. The process mean should be adjusted upward toward 1.500 to improve Cpk."

---

## Example 4 — Calculating Cp/Cpk by Hand from Given Values

**Given:** Specs at 125 ± 30 (USL = 155, LSL = 95). Process σ = 8. Two scenarios:

**Scenario A: Process mean μ = 125 (centered)**

$$C_p = \frac{USL - LSL}{6\sigma} = \frac{155 - 95}{6(8)} = \frac{60}{48} = 1.25$$

$$C_{pk} = \min\left[\frac{155-125}{3(8)},\; \frac{125-95}{3(8)}\right] = \min\left[\frac{30}{24}, \frac{30}{24}\right] = 1.25$$

When centered, Cp = Cpk = 1.25. Process is capable (> 1.0) but below 1.33 threshold.

**Scenario B: Process mean μ = 130 (off-center toward USL)**

$$C_p = \frac{60}{48} = 1.25 \quad \text{(unchanged — Cp ignores centering)}$$

$$C_{pk} = \min\left[\frac{155-130}{24},\; \frac{130-95}{24}\right] = \min\left[\frac{25}{24}, \frac{35}{24}\right] = \min[1.042, 1.458] = 1.042$$

**Answer:**
> "Scenario B: Although Cp = 1.25, Cpk = 1.042 because the process is shifted toward the USL. The fraction defective above USL is higher than a centered process would produce. Cp is the same in both scenarios — this illustrates why Cp alone is insufficient when the process may be off-center."

---

## Example 5 — Estimating σ̂ from Control Chart Output

**Given:** R chart with R̄ = 5.74, subgroup size n = 5. Control chart constants table gives d₂ = 2.326 for n = 5.

**Find:** σ̂

**Solution:**
$$\hat{\sigma} = \frac{\bar{R}}{d_2} = \frac{5.74}{2.326} = 2.467$$

> Note: This σ̂ is used to set X̄ chart limits AND to compute Cp/Cpk. The `StdDev` shown in qcc R output IS this value — qcc computes R̄/d₂ internally.

If using an S chart instead (s̄ = 2.35, n = 5, c₄ = 0.9400):
$$\hat{\sigma} = \frac{\bar{s}}{c_4} = \frac{2.35}{0.9400} = 2.500$$

---

## Example 6 — p-Chart Interpretation

**Given:** p-chart output on 25 subgroups, monitoring fraction of defective units. All points are within control limits. No non-random patterns observed.

**Find:** State the conclusion.

**Answer:**
> "The fraction defective p-chart shows the process is in statistical control. All 25 subgroup proportions fall within the control limits and no non-random patterns are present. The process appears stable with respect to the fraction of defective items produced."

---

## Example 7 — Fallout/Fraction Defective Calculation

**Given:** Spec limits: USL = 155, LSL = 95. Process: μ = 130, σ = 8. Find the fraction of output that fails specs.

---

**Solution:**

$$\text{Fallout} = P(X < LSL) + P(X > USL)$$

$$= P(X < 95) + P(X > 155)$$

$$= \Phi\!\left(\frac{95-130}{8}\right) + \left[1 - \Phi\!\left(\frac{155-130}{8}\right)\right]$$

$$= \Phi(-4.375) + \Phi(-3.125) \approx 0 + 0.000874 = 0.0874\%$$

**Common trap:** The formula on the exam may be written as Pr(X < (LSL − μ)/σ) + Pr(X > (USL − μ)/σ). This is **incorrect** — those expressions are already standardized Z-values, not X-values. The correct formula standardizes the raw X:

$$P(X < LSL) = \Phi\!\left(\frac{LSL - \mu}{\sigma}\right) \neq \Phi(LSL - \mu)/\sigma$$

**Answer:**
> "Approximately 0.087% of output is expected to fall outside specification limits, with virtually all of it exceeding the USL."

---

## Concept Checkpoint Q&A — Exam-Style Questions

These are the exact question types that appear on concept checkpoints (L27-28, L29-30):

| Question | Correct Answer |
|---------|---------------|
| A process is "out of control" when... | Operating in presence of **assignable causes** (not chance causes) |
| Purpose of a control chart | Enable **just-in-time adjustments** to reduce overall variability |
| k in the control limit formula | Distance from center line in **standard deviation units** (commonly = 3) |
| The chart that monitors the **average** | X̄ (Xbar) chart |
| A₂ is used in... | X̄ chart control limits |
| D₃ is used in... | R chart **lower** control limit |
| D₄ is used in... | R chart **upper** control limit |
| C₄ is used in... | S chart control limits (and σ̂ = s̄/c₄) |
| Spec limits = control limits? | **False** — completely different sources and purposes |
| Triggered WE rule means... | "Investigate for assignable cause" — not necessarily OOC, but warrants investigation |
| P-chart is based on which distribution? | **Binomial** |
| U-chart is based on which distribution? | **Poisson** |
| Cp overstates capability when... | Process is running **off-center** (use Cpk for actual capability) |
| Natural tolerance limits are... | μ ± 3σ (where the process actually puts 99.73% of its output) |
| PCR in plain English | Relationship between what customer wants (spec width) vs what we produce (6σ) |

---

## Common Mistakes on Exams

| Mistake | Correct approach |
|---------|----------------|
| Building X̄ chart before R chart | Build R (or S) chart FIRST — if it's OOC, X̄ limits are unreliable |
| Using raw sample s as σ̂ | Use R̄/d₂ or s̄/c₄ — not the raw standard deviation |
| Treating control limits as spec limits | Control limits = 3σ from data; spec limits = customer requirement — completely different |
| Concluding capable from Cp alone | Always check Cpk — Cp ignores off-centering |
| Revising limits without removing OOC | Find and remove OOC subgroups BEFORE recomputing revised limits |

---

## Related
- [control-charts](../concepts/control-charts.md)
- [process-capability](../concepts/process-capability.md)
- [control-charts-r](../r-code/control-charts-r.md)

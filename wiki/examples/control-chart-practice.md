---
tags: [example, practice, unit-4]
tier: script
sources: [ControlCharts_Assessment.docx, Control_Chart_Practice_V2.docx, control-charts, process-capability]
---
# Practice Problems: Control Charts

See also: [control-charts](../concepts/control-charts.md), [process-capability](../concepts/process-capability.md), [control-chart-examples](control-chart-examples.md), [control-charts-r](../r-code/control-charts-r.md)

> **Exam format:** Hand-calculated. Each problem includes a partial constants or reference table — read the scenario to identify which row applies, then use those values to compute limits or capability indices. No R code required.

---

## Problem 1 — X̄ & R Chart Control Limits  (n = 5)

**Scenario:** A manufacturer monitors shaft diameters (mm). Subgroups of n = 5 shafts are sampled every 30 minutes. After 25 preliminary subgroups:

- Grand mean: x̄̄ = 82.40 mm
- Average range: R̄ = 6.10 mm

**Control chart constants table (excerpt) — select the row that matches the subgroup size:**

| n | A₂ | D₃ | D₄ | d₂ |
|---|-----|-----|-----|-----|
| 4 | 0.729 | 0 | 2.282 | 2.059 |
| **5** | **0.577** | **0** | **2.115** | **2.326** |
| 6 | 0.483 | 0 | 2.004 | 2.534 |

**Three of the 25 subgroups (x̄ and R already computed):**

| Sample | x̄ (mm) | R (mm) |
|--------|---------|--------|
| 2  | 83.1 | 5.8  |
| 9  | 86.3 | 7.2  |
| 15 | 80.5 | 13.4 |

**Questions:**
- (a) Which row of the constants table applies? State the values of A₂, D₃, and D₄ you will use.
- (b) Compute UCL, CL, and LCL for the X̄ chart.
- (c) Compute UCL, CL, and LCL for the R chart.
- (d) Which of the 3 subgroups are out of control, and on which chart?

### Answers

**(a) Row selection:** n = 5 → A₂ = 0.577, D₃ = 0, D₄ = 2.115

**(b) X̄ Chart Limits**

A₂ × R̄ = 0.577 × 6.10 = 3.52

$$\text{UCL}_{\bar{x}} = 82.40 + 3.52 = \mathbf{85.92}$$
$$\text{CL}_{\bar{x}} = 82.40$$
$$\text{LCL}_{\bar{x}} = 82.40 - 3.52 = \mathbf{78.88}$$

**(c) R Chart Limits**

$$\text{UCL}_R = D_4 \bar{R} = 2.115 \times 6.10 = \mathbf{12.90}$$
$$\text{CL}_R = \bar{R} = 6.10$$
$$\text{LCL}_R = D_3 \bar{R} = 0 \times 6.10 = \mathbf{0.00} \quad (D_3 = 0 \text{ for } n \le 6)$$

**(d) Out-of-control check**

| Sample | x̄ | X̄ check [78.88, 85.92] | R | R check [0, 12.90] |
|--------|------|------------------------|------|-------------------|
| 2  | 83.1 | In control | 5.8  | In control |
| 9  | 86.3 | **OUT** (86.3 > UCL 85.92) | 7.2  | In control |
| 15 | 80.5 | In control | 13.4 | **OUT** (13.4 > UCL 12.90) |

> Sample 9 is out on the X̄ chart only; Sample 15 is out on the R chart only. In practice, investigate the R chart signal first — if variability is out of control, the X̄ limits may be unreliable.

---

## Problem 2 — R Chart Limits and Process σ̂ Estimation  (n = 3)

**Scenario:** A plastics extruder is monitored with subgroups of n = 3 parts. Phase I (20 subgroups) yields:

- x̄̄ = 25.00 mm,  R̄ = 2.40 mm

**Control chart constants table (excerpt):**

| n | A₂ | D₃ | D₄ | d₂ |
|---|-----|-----|-----|-----|
| 2 | 1.880 | 0 | 3.267 | 1.128 |
| **3** | **1.023** | **0** | **2.574** | **1.693** |
| 4 | 0.729 | 0 | 2.282 | 2.059 |

**Three Phase II subgroups:**

| Sample | x̄ (mm) | R (mm) |
|--------|---------|--------|
| 5  | 24.2 | 2.1 |
| 12 | 27.8 | 2.8 |
| 20 | 26.1 | 1.9 |

**Questions:**
- (a) Which row applies? Write down A₂, D₄, and d₂.
- (b) Compute the X̄ chart limits (UCL, CL, LCL).
- (c) Compute the R chart limits (UCL, CL, LCL).
- (d) Estimate the process standard deviation: σ̂ = R̄ / d₂.
- (e) Which Phase II subgroups are out of control, and on which chart?

### Answers

**(a) Row selection:** n = 3 → A₂ = 1.023, D₄ = 2.574, d₂ = 1.693

**(b) X̄ Chart Limits**

A₂ × R̄ = 1.023 × 2.40 = 2.46

$$\text{UCL}_{\bar{x}} = 25.00 + 2.46 = \mathbf{27.46}$$
$$\text{CL}_{\bar{x}} = 25.00$$
$$\text{LCL}_{\bar{x}} = 25.00 - 2.46 = \mathbf{22.54}$$

**(c) R Chart Limits**

$$\text{UCL}_R = D_4 \bar{R} = 2.574 \times 2.40 = \mathbf{6.18}$$
$$\text{CL}_R = 2.40$$
$$\text{LCL}_R = 0.00 \quad (D_3 = 0 \text{ for } n \le 6)$$

**(d) σ̂ Estimation**

$$\hat{\sigma} = \frac{\bar{R}}{d_2} = \frac{2.40}{1.693} = \mathbf{1.42}$$

**(e) Out-of-control check**

| Sample | x̄ | X̄ check [22.54, 27.46] | R | R check [0, 6.18] |
|--------|------|------------------------|------|-------------------|
| 5  | 24.2 | In control | 2.1 | In control |
| 12 | 27.8 | **OUT** (27.8 > UCL 27.46) | 2.8 | In control |
| 20 | 26.1 | In control | 1.9 | In control |

---

## Problem 3 — Process Capability  (Cp and Cpk, n = 4)

**Scenario:** A machined part has specifications USL = 132.0 mm and LSL = 108.0 mm. A control chart study with n = 4 yields x̄̄ = 120.0 mm and R̄ = 8.50 mm. Use the d₂ constant to estimate σ̂.

**Control chart constants table (excerpt) — d₂ column converts R̄ to σ̂:**

| n | A₂ | D₃ | D₄ | d₂ |
|---|-----|-----|-----|-----|
| 3 | 1.023 | 0 | 2.574 | 1.693 |
| **4** | **0.729** | **0** | **2.282** | **2.059** |
| 5 | 0.577 | 0 | 2.115 | 2.326 |

**Questions:**
- (a) Which d₂ applies? State the value.
- (b) Estimate σ̂ = R̄ / d₂.
- (c) Compute Cp = (USL − LSL) / (6σ̂).
- (d) Compute Cpk = min[(USL − μ̂)/(3σ̂), (μ̂ − LSL)/(3σ̂)].  Use μ̂ = x̄̄.
- (e) Is the process capable? Does Cp = Cpk here? What does that tell you?

### Answers

**(a) Row selection:** n = 4 → d₂ = 2.059

**(b) σ̂**

$$\hat{\sigma} = \frac{\bar{R}}{d_2} = \frac{8.50}{2.059} = \mathbf{4.13}$$

**(c) Cp**

$$C_p = \frac{132.0 - 108.0}{6 \times 4.13} = \frac{24.0}{24.78} = \mathbf{0.97}$$

**(d) Cpk**

$$3\hat{\sigma} = 3 \times 4.13 = 12.39$$
$$C_{pk} = \min\!\left[\frac{132.0 - 120.0}{12.39},\; \frac{120.0 - 108.0}{12.39}\right] = \min[0.97,\; 0.97] = \mathbf{0.97}$$

**(e) Interpretation**

Cp = Cpk = 0.97 < 1.0 → process is **not capable**.

Cp = Cpk because x̄̄ = 120.0 is exactly centered between USL and LSL (midpoint = (132+108)/2 = 120). The problem is spread, not alignment — σ̂ is too large. Re-centering will not help; variability must be reduced.

---

## Problem 4 — Attribute Chart Selection and p-Chart Limits

**Scenario:** A factory inspects batches of n = 200 bolts and counts how many are defective. Over 20 batches, 160 total defective bolts were found out of 4 000 inspected. Three recent batches:

| Batch | n (inspected) | d (defective) | p̂ = d/n |
|-------|--------------|--------------|---------|
| 6  | 200 | 12 | 0.060 |
| 13 | 200 | 25 | 0.125 |
| 19 | 200 | 8  | 0.040 |

**Attribute control chart reference table — select the chart type that fits this scenario:**

| Chart | What is counted | Distribution | n |
|-------|----------------|--------------|---|
| p | Items classed defective or not (each item is pass/fail) | Binomial | Can vary |
| c | Number of defects on a single fixed-size inspection unit | Poisson | Fixed unit |
| u | Defects per unit when inspection unit size varies | Poisson | Variable |

**Questions:**
- (a) Which row of the chart-type table applies? Name the chart and explain why in one sentence.
- (b) Compute p̄ = total defectives / total inspected (use all 20 batches).
- (c) Compute σ̂_p = √(p̄(1−p̄)/n).
- (d) Find UCL, CL, and LCL. Set LCL = 0 if the formula gives a negative value.
- (e) Which of the 3 batches shown are out of control?

### Answers

**(a) Chart type: p-chart** — each bolt is classified defective or not (binary pass/fail outcome with fixed n = 200), matching the p-chart row (Binomial distribution).

> If the scenario counted defects per bolt (a bolt can have multiple flaws), use a c- or u-chart instead.

**(b) p̄**

$$\bar{p} = \frac{160}{4000} = \mathbf{0.040}$$

> Always pool ALL batches — never average individual p̂ values.

**(c) σ̂_p**

$$\hat{\sigma}_p = \sqrt{\frac{0.040 \times 0.960}{200}} = \sqrt{0.000192} = \mathbf{0.014}$$

**(d) Control limits**

$$\text{UCL} = 0.040 + 3(0.014) = \mathbf{0.082}$$
$$\text{CL} = 0.040$$
$$\text{LCL} = 0.040 - 0.042 = -0.002 \to \mathbf{0.000} \quad (\text{floor at 0})$$

**(e) Out-of-control check** — limits [0, 0.082]:

| Batch | p̂ | Check vs [0, 0.082] | Result |
|-------|------|---------------------|--------|
| 6  | 0.060 | 0.060 ≤ 0.082 | In control |
| 13 | 0.125 | 0.125 > 0.082 | **OUT** (above UCL) |
| 19 | 0.040 | 0.040 ≤ 0.082 | In control (exactly at CL) |

---

## Problem 5 — Western Electric Out-of-Control Rules

**Scenario:** An X̄ chart has center line CL = 100.0 and σ_process = 2.0.

- 1σ zone: 98.0 – 102.0
- 2σ zone: 96.0 – 104.0
- 3σ limits: UCL = 106.0, LCL = 94.0

**Three consecutive subgroups (fill in the last three columns):**

| Subgroup | x̄ | Above or below CL? | Beyond 2σ boundary? | Beyond 3σ limit? |
|----------|------|-------------------|---------------------|-----------------|
| 1 | 104.2 | — | — | — |
| 2 | 103.1 | — | — | — |
| 3 | 104.8 | — | — | — |

**Western Electric rules reference table (excerpt) — identify which rule, if any, is triggered:**

| Rule | Signal — process is out of control if… |
|------|----------------------------------------|
| 1 | 1 point falls outside the 3σ control limits (beyond UCL or LCL) |
| 2 | 2 of any 3 consecutive points fall beyond the **same** 2σ boundary (both above or both below) |
| 4 | 8 or more consecutive points fall on the same side of the center line |

**Questions:**
- (a) Fill in the three columns of the subgroup table (Above/Below, Yes/No, Yes/No).
- (b) Does Rule 1 trigger? Explain briefly.
- (c) Does Rule 2 trigger? State which subgroups are involved.
- (d) Does Rule 4 trigger? Explain why or why not.
- (e) Overall verdict: is the process in control or out of control? Which rule(s) apply?

### Answers

**(a) Completed zone table**

| Subgroup | x̄ | Above CL (100)? | Beyond 2σ (> 104)? | Beyond 3σ (> 106)? |
|----------|------|-----------------|---------------------|---------------------|
| 1 | 104.2 | Above | Yes (104.2 > 104.0) | No (104.2 < 106) |
| 2 | 103.1 | Above | No (103.1 < 104.0) | No |
| 3 | 104.8 | Above | Yes (104.8 > 104.0) | No (104.8 < 106) |

**(b) Rule 1:** UCL = 106.0. All three x̄ values are below 106. Rule 1 does **NOT** trigger.

**(c) Rule 2:** Upper 2σ boundary = 104.0.
- Subgroup 1: 104.2 > 104 ✓
- Subgroup 2: 103.1 < 104 ✗ (inside 2σ band — only 2 of 3 need to qualify)
- Subgroup 3: 104.8 > 104 ✓

2 of 3 consecutive points are beyond the upper 2σ boundary, on the same side. **Rule 2 TRIGGERS** (Subgroups 1 and 3).

> Key: the middle point does NOT need to be beyond 2σ. Only 2 of any 3 consecutive must qualify.

**(d) Rule 4:** Requires 8 consecutive points on the same side. Only 3 subgroups are shown. Rule 4 cannot be evaluated — does **NOT** trigger.

**(e) Verdict: OUT OF CONTROL via Rule 2.** The process mean is drifting upward; individual points look within limits under Rule 1 alone, but the clustering pattern near the upper 2σ boundary reveals the shift.

---

## Concept Summary

| Concept | Rule to remember |
|---------|-----------------|
| Which constants row? | Match n (subgroup size) to the correct row. Wrong n → wrong limits |
| σ̂ from R̄ | σ̂ = R̄ / d₂ — d₂ encodes the expected range/σ ratio for that subgroup size |
| Build order | Always build R chart before X̄ chart — if R is out of control, X̄ limits are unreliable |
| LCL floor | Set LCL = 0 whenever the formula gives a negative value (D₃ = 0 for n ≤ 6; p-chart LCL can also go negative) |
| Cp vs Cpk | Cp = spread only; Cpk = spread + centering. Cp = Cpk only when μ̂ is exactly centered between USL and LSL |
| p̄ pooling | p̄ = Σdefectives / Σinspected — never average individual p̂ values |
| Rule 2 nuance | "2 of 3" triggers even if the middle point is inside the 2σ band — only 2 of the 3 need to be outside |

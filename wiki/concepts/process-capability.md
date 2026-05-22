---
tags: [concept, section-3]
tier: procedure
sources: [L30E, Process Capability.R]
---
# Process Capability

## In Plain English
Process capability indices measure whether a process that is **in statistical control** is capable of meeting specifications. "In control" and "capable" are separate questions: a process can be in control but not capable of meeting specs, or vice versa.

**Always verify the process is in control before computing capability indices.**

---

## What PCR Measures (Plain English)

> The Process Capability Ratio is the relationship between **what the customer/market wants** (specification width) versus **what we can produce** (6σ process spread).

---

## Natural Tolerance Limits

$$\text{NTL} = \mu \pm 3\sigma \quad \Rightarrow \quad [\mu - 3\sigma,\ \mu + 3\sigma]$$

These are the "natural" limits of what the process actually produces — where nearly all output (99.73%) will fall if the process is normal and in control. They are NOT set by the customer; they come from the data.

- If natural tolerance limits fall **inside** spec limits → process is capable
- If natural tolerance limits fall **outside** spec limits → process produces defectives

---

## Fraction Defective (Fallout)

The fraction of output that does NOT meet specifications:

$$\text{Fallout} = P(X < LSL) + P(X > USL)$$

Using standardization:

$$= \Phi\!\left(\frac{LSL - \mu}{\sigma}\right) + \left[1 - \Phi\!\left(\frac{USL - \mu}{\sigma}\right)\right]$$

> **Common trap:** The formula is Pr(X < LSL) + Pr(X > USL). This is NOT the same as Pr(X < (LSL−μ)/σ) — that would be applying the Z transformation to a number that's already been transformed. Always standardize the raw X value.

**Example (from slides):** Specs 125 ± 30 (USL=155, LSL=95), μ=130, σ=8:
$$\text{Fallout} = \Phi\!\left(\frac{95-130}{8}\right) + \left[1 - \Phi\!\left(\frac{155-130}{8}\right)\right] = \Phi(-4.375) + \Phi(-3.125) \approx 0 + 0.000874 = 0.0874\%$$

---

## Tolerance Chart

A **tolerance chart** (also called a "multi-vari chart" in some texts) plots **all individual observations** in each subgroup against the USL and LSL — not just subgroup averages.

- The X̄ chart can be in control (averages within limits) while individual units still fail specs
- A tolerance chart reveals this by showing the full range of individual values vs. spec limits
- Useful for process capability assessment before computing Cp/Cpk

---

## Specification vs Control Limits

| Term | Set by | Purpose |
|------|--------|---------|
| Control limits (UCL/LCL) | Data — 3σ from process mean | Detect out-of-control signals |
| Specification limits (USL/LSL) | Engineering / customer | Define acceptable product range |

---

## Process Capability Ratio Cp

$$C_p = \frac{USL - LSL}{6\hat{\sigma}}$$

Measures spread relative to specification width. Assumes process is **centered**.

| Cp value | Interpretation |
|----------|---------------|
| < 1.0 | Not capable — process is wider than specs |
| ≥ 1.0 | Barely capable |
| ≥ 1.33 | Capable (most industries require this minimum) |
| ≥ 1.67 | Highly capable |
| ≥ 2.0 | Six Sigma level |

**Limitation:** Cp ignores where the process is centered — a well-spread but off-center process looks capable when it isn't.

> **Key fact:** If the process is running off-center, its **actual capability is less than indicated by Cp (PCR)**. Cp always equals or overstates true capability when the process is off-center. Use Cpk for the true picture.

---

## Process Capability Index Cpk

$$C_{pk} = \min\left[\frac{USL - \hat{\mu}}{3\hat{\sigma}},\; \frac{\hat{\mu} - LSL}{3\hat{\sigma}}\right]$$

Accounts for both spread **and** centering. Cpk ≤ Cp always.

| Cpk = Cp | Process is perfectly centered |
|----------|-------------------------------|
| Cpk < Cp | Process is off-center |
| Cpk < 0 | Process mean is outside spec limits |

---

## Estimating σ from Control Charts

| Source chart | Formula |
|-------------|---------|
| R chart | σ̂ = R̄/d₂ |
| S chart | σ̂ = s̄/c₄ |

Constants d₂, c₄ depend on subgroup size n (from control chart constants table).

---

## R Code

```r
# First build the X-bar chart (sigma estimated from R chart by default)
qqX <- qcc(data = df, type = "xbar", nsigmas = 3,
           title = "Xbar Chart", std.dev = sd.R(df))

# Process capability (centered — Cp and Cpk)
pc <- process.capability(qqX, spec.limits = c(LSL, USL))
print(pc, digits = 10)

# Off-centered (specify target different from midpoint)
pc <- process.capability(qqX, spec.limits = c(LSL, USL), target = target_value)
print(pc, digits = 10)
```

**Reading `process.capability()` output:**
| Output | Meaning |
|--------|---------|
| `Cp` | Process capability ratio (centered) |
| `Cpk` | Process capability index (accounts for centering) |
| `Cpm` | Process capability index (accounts for target) |
| `exp/obs` | Expected/observed fraction nonconforming |

---

## Teacher's Phrasing

**Capable:**
> "The process [is/is not] capable of meeting specifications. Cp = [X] and Cpk = [X], both [≥ / <] 1.33, indicating the process [has/does not have] adequate capability."

**Off-center process:**
> "Although Cp = [X] suggests adequate spread, Cpk = [X] < Cp indicates the process is off-center. The process mean should be shifted toward the specification midpoint."

---

## Key Assumptions
- Process must be in statistical control before computing Cp/Cpk
- Process output is approximately normally distributed
- σ is estimated from the control chart (not raw sample standard deviation)

## Common Mistakes
- Computing Cpk before verifying in-control status
- Using raw sample s instead of R̄/d₂ or s̄/c₄ for σ̂
- Concluding a process is capable based on Cp alone when it's off-center

## Related
- [control-charts](control-charts.md)
- [control-charts-r](../r-code/control-charts-r.md)

---
tags: [reference, unit-1, unit-3, unit-4, unit-5]
sources: [all formula PNGs, L11P-L25P, exam2_formula_reff, L42&43P, L44&45P, L46&47P, L48-50P 2kFD]
---
# Formula Sheet — All Sections

Quick-reference. No prose — formulas, symbols, and conditions only.

---

## SECTION 1–2: Probability & Distributions

### Probability Rules
| Rule | Formula |
|------|---------|
| Complement | P(A') = 1 − P(A) |
| Addition (general) | P(A∪B) = P(A)+P(B)−P(A∩B) |
| Multiplication (conditional) | P(A∩B) = P(A)·P(B\|A) |
| Conditional | P(B\|A) = P(A∩B)/P(A) |
| Independence check | P(A∩B) = P(A)·P(B) |

### Discrete Distributions
| Quantity | Formula |
|----------|---------|
| Expected value | E[X] = Σ x·f(x) |
| Variance | V[X] = E[X²] − (E[X])² = Σx²f(x) − μ² |
| Binomial PMF | f(x) = C(n,x)·pˣ·(1−p)^(n−x) |
| Binomial mean | μ = np |
| Binomial variance | σ² = np(1−p) |

### Sampling Distribution of X̄
| Quantity | Formula |
|----------|---------|
| Mean of X̄ | E[X̄] = μ |
| Std error | SE = σ/√n |
| CLT (n≥40) | X̄ ~ N(μ, σ²/n) |

### Sample Statistics
| Measure | Formula |
|---------|---------|
| Sample mean | x̄ = Σxᵢ/n |
| Sample variance | s² = Σ(xᵢ−x̄)²/(n−1) |
| IQR | Q3 − Q1 |

---

## SECTION 1–2: Confidence Intervals

| Parameter | Condition | CI Formula |
|-----------|-----------|-----------|
| μ | σ known or n≥40 | x̄ ± z_{α/2}·σ/√n |
| μ | σ unknown | x̄ ± t_{α/2,n−1}·s/√n |
| σ² | — | [(n−1)s²/χ²_{α/2,n−1}, (n−1)s²/χ²_{1−α/2,n−1}] |
| p | large n | p̂ ± z_{α/2}·√(p̂(1−p̂)/n) |
| μ₁−μ₂ | σ known | (x̄₁−x̄₂) ± z_{α/2}·√(σ₁²/n₁+σ₂²/n₂) |
| μ₁−μ₂ | equal σ², unknown | (x̄₁−x̄₂) ± t_{α/2,n₁+n₂−2}·Sp·√(1/n₁+1/n₂) |
| μ₁−μ₂ | unequal σ², unknown | (x̄₁−x̄₂) ± t_{α/2,ν}·√(s₁²/n₁+s₂²/n₂) |
| μ_D (paired) | — | d̄ ± t_{α/2,n−1}·s_D/√n |
| σ₁²/σ₂² | — | (s₁²/s₂²)·[f_{lower}, f_{upper}] |

**Sample size formulas:**
| Goal | Formula |
|------|---------|
| CI on μ (σ known) | n = (z_{α/2}·σ/E)² |
| Test on μ (two-sided) | n ≈ (z_{α/2}+z_β)²σ²/δ² |
| Test on μ (one-sided) | n ≈ (z_α+z_β)²σ²/δ² |
| Test on p (two-sided) | n = [(z_{α/2}√(p₀(1−p₀))+z_β√(p(1−p)))/(p−p₀)]² |

---

## SECTION 1–2: Hypothesis Tests

### Test Statistics
| Test | H₀ | Statistic | df |
|------|----|-----------|----|
| Z on μ (σ known) | μ=μ₀ | Z₀=(x̄−μ₀)/(σ/√n) | — |
| t on μ (σ unknown) | μ=μ₀ | T₀=(x̄−μ₀)/(s/√n) | n−1 |
| χ² on σ² | σ²=σ₀² | χ²₀=(n−1)s²/σ₀² | n−1 |
| Z on p | p=p₀ | Z₀=(p̂−p₀)/√(p₀(1−p₀)/n) | — |
| 2-sample Z | μ₁−μ₂=Δ₀ | Z₀=(x̄₁−x̄₂−Δ₀)/√(σ₁²/n₁+σ₂²/n₂) | — |
| Pooled t | μ₁−μ₂=Δ₀ | T₀=(x̄₁−x̄₂−Δ₀)/[Sp√(1/n₁+1/n₂)] | n₁+n₂−2 |
| Welch t | μ₁−μ₂=Δ₀ | T₀=(x̄₁−x̄₂−Δ₀)/√(s₁²/n₁+s₂²/n₂) | ν (Welch) |
| Paired t | μ_D=Δ₀ | T₀=d̄/(s_D/√n) | n−1 |
| F on σ₁²=σ₂² | σ₁²=σ₂² | F₀=s₁²/s₂² | n₁−1, n₂−1 |
| χ² GoF | dist=hyp | χ²₀=Σ(Oᵢ−Eᵢ)²/Eᵢ | k−1 |
| χ² Indep | indep | χ²₀=ΣΣ(Oᵢⱼ−Eᵢⱼ)²/Eᵢⱼ | (r−1)(c−1) |

**Pooled variance:**
$$S_p^2 = \frac{(n_1-1)S_1^2 + (n_2-1)S_2^2}{n_1+n_2-2}$$

**Welch df:**
$$\nu = \frac{(s_1^2/n_1 + s_2^2/n_2)^2}{(s_1^2/n_1)^2/(n_1-1) + (s_2^2/n_2)^2/(n_2-1)}$$

**β for two-sided Z-test:**
$$\beta = \Phi\!\left(z_{\alpha/2} - \frac{\delta\sqrt{n}}{\sigma}\right) - \Phi\!\left(-z_{\alpha/2} - \frac{\delta\sqrt{n}}{\sigma}\right), \quad \delta=\mu-\mu_0$$

### Critical Value Summary
| α | z_α | z_{α/2} |
|---|-----|---------|
| 0.01 | 2.326 | 2.576 |
| 0.025 | 1.960 | 2.241 |
| 0.05 | 1.645 | 1.960 |
| 0.10 | 1.282 | 1.645 |

**F lower tail:** f_{1−α,u,v} = 1/f_{α,v,u}

---

## SECTION 3: Regression

### Simple Linear Regression (SLR)
$$\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x$$

| Quantity | Formula |
|----------|---------|
| β̂₁ (slope) | S_{xy}/S_{xx} |
| β̂₀ (intercept) | ȳ − β̂₁x̄ |
| S_{xx} | Σ(xᵢ−x̄)² = Σxᵢ² − n x̄² |
| S_{xy} | Σ(xᵢ−x̄)(yᵢ−ȳ) = Σxᵢyᵢ − nx̄ȳ |
| MSE (error variance) | SSE/(n−p−1) = s² |
| SST | Σ(yᵢ−ȳ)² |
| SSR | SST − SSE |
| R² | SSR/SST = 1 − SSE/SST |
| R²_adj | 1 − (SSE/(n−p−1))/(SST/(n−1)) |

### Multiple Linear Regression (MLR)
$$\hat{y} = \hat{\beta}_0 + \hat{\beta}_1 x_1 + \hat{\beta}_2 x_2 + \cdots + \hat{\beta}_k x_k$$

- p = number of predictors; df error = n − p − 1
- Use R: `lm(y ~ x1 + x2 + ...)`, then `summary()`

### ANOVA Table for Regression
| Source | SS | df | MS | F |
|--------|----|----|----|----|
| Regression | SSR | p | MSR=SSR/p | MSR/MSE |
| Error | SSE | n−p−1 | MSE=SSE/(n−p−1) | |
| Total | SST | n−1 | | |

### HT in Regression
| Test | H₀ | Statistic | df |
|------|----|-----------|----|
| Overall model | β₁=…=βₖ=0 | F₀=MSR/MSE | p, n−p−1 |
| Individual coefficient | βⱼ=0 | T₀=β̂ⱼ/SE(β̂ⱼ) | n−p−1 |

### CI and Prediction Intervals in Regression
| Interval | Formula | Notes |
|----------|---------|-------|
| CI on mean response | ŷ ± t_{α/2}·SE(ŷ) | Narrower |
| Prediction interval | ŷ ± t_{α/2}·√(MSE + SE²(ŷ)) | Wider — includes individual variability |

---

## SECTION 3: Control Charts

### X̄ & R Chart (Subgroup size n ≤ 10)
| Quantity | Formula |
|----------|---------|
| Center line (X̄ chart) | x̄̄ = Σx̄ᵢ/m |
| UCL (X̄) | x̄̄ + A₂R̄ |
| LCL (X̄) | x̄̄ − A₂R̄ |
| Center (R chart) | R̄ = ΣRᵢ/m |
| UCL (R) | D₄R̄ |
| LCL (R) | D₃R̄ |

### X̄ & S Chart (Larger subgroups)
| Quantity | Formula |
|----------|---------|
| UCL (X̄) | x̄̄ + A₃s̄ |
| LCL (X̄) | x̄̄ − A₃s̄ |
| UCL (S) | B₄s̄ |
| LCL (S) | B₃s̄ |

Constants (A₂, A₃, D₃, D₄, B₃, B₄) from standard control chart table (depend on subgroup size n).

### p-Chart (Fraction Defective)
| Quantity | Formula |
|----------|---------|
| p̄ | total defectives / total inspected |
| UCL | p̄ + 3√(p̄(1−p̄)/n) |
| LCL | p̄ − 3√(p̄(1−p̄)/n) (≥ 0) |

### c-Chart (Defects per unit, constant n)
| Quantity | Formula |
|----------|---------|
| c̄ | total defects / m |
| UCL | c̄ + 3√c̄ |
| LCL | c̄ − 3√c̄ (≥ 0) |

### Process Capability
| Index | Formula | Interpretation |
|-------|---------|----------------|
| Cp | (USL−LSL)/(6σ̂) | spread relative to spec width |
| Cpk | min[(USL−μ̂)/3σ̂, (μ̂−LSL)/3σ̂] | accounts for centering |

- Cp / Cpk ≥ 1.0: barely capable
- Cp / Cpk ≥ 1.33: capable
- Cp / Cpk ≥ 1.67: highly capable

**Estimate σ from control chart:** σ̂ = R̄/d₂ or σ̂ = s̄/c₄

---

## SECTION 3: Correlation & Transformations

| Quantity | Formula |
|----------|---------|
| Pearson r | S_{xy}/√(S_{xx}·S_{yy}) |
| Test H₀: ρ=0 | T₀ = r√(n−2)/√(1−r²), df=n−2 |

**Common transformations when assumptions violated:**

| Issue | Transformation |
|-------|---------------|
| Variance increases with mean | log(y) or √y |
| Curved relationship | log(x) or x² |
| Box-Cox | y^λ (λ chosen to best linearize) |

---

## SECTION 4: Experimental Design

### ANOVA Model and Hypothesis
$$Y_{ij} = \mu + \tau_i + \varepsilon_{ij}, \quad \varepsilon_{ij} \sim N(0,\sigma^2)$$
$$H_0: \tau_1 = \tau_2 = \cdots = \tau_a = 0 \qquad H_1: \text{at least one } \tau_i \neq 0$$

### ANOVA Tables by Design

| Design | Source | df | F₀ | R Formula |
|--------|--------|----|----|-----------|
| **CRD** | Treatments | a−1 | MS_Trt/MS_E | `aov(obs ~ trt)` |
| | Error | N−a | | |
| | Total | N−1 | | |
| **RCBD** | Treatments | a−1 | MS_Trt/MS_E | `aov(obs ~ trt + blk)` |
| | Blocks | b−1 | MS_Blk/MS_E | |
| | Error | **(a−1)(b−1)** | | |
| | Total | ab−1 | | |
| **2-Factor Factorial** | A | a−1 | MS_A/MS_E | `aov(obs ~ F1 * F2)` |
| | B | b−1 | MS_B/MS_E | |
| | AB | (a−1)(b−1) | MS_AB/MS_E | |
| | Error | **ab(n−1)** | | |
| | Total | abn−1 | | |
| **2^k (replicated)** | Each effect | 1 | SS_eff/MS_E | `aov(obs ~ A * B * ...)` |
| | Error | 2^k(n−1) | | |
| | Total | n·2^k−1 | | |

### Fisher LSD
$$\text{LSD (balanced)} = t_{\alpha/2,\,df_E} \sqrt{\frac{2 \cdot MS_E}{n}}$$
$$\text{LSD (unbalanced)} = t_{\alpha/2,\,df_E} \sqrt{MS_E\!\left(\tfrac{1}{n_i}+\tfrac{1}{n_j}\right)}$$

Pair (i,j) significant if |ȳᵢ − ȳⱼ| > LSD.

### CI on Treatment Mean
$$\bar{y}_{i.} \pm t_{\alpha/2,\,df_E}\sqrt{\frac{MS_E}{n}}$$

### CI on Difference of Treatment Means (unbalanced)
$$(\bar{y}_{i.} - \bar{y}_{j.}) \pm t_{\alpha/2,\,df_E}\sqrt{MS_E\!\left(\tfrac{1}{n_i}+\tfrac{1}{n_j}\right)}$$

### 2^k Effects and SS
$$\text{Effect} = \frac{\text{Contrast}}{n \cdot 2^{k-1}} \qquad SS = \frac{(\text{Contrast})^2}{n \cdot 2^k} \qquad \hat{\beta}_{\text{lm}} = \frac{\text{Effect}}{2}$$

### Random Effects Variance Components
$$\hat{\sigma}^2 = MS_E \qquad \hat{\sigma}^2_\tau = \frac{MS_{\text{Trt}} - MS_E}{n}$$

### Key Design Distinctions
| Confusion | Answer |
|-----------|--------|
| RCBD vs factorial df_error | RCBD: (a−1)(b−1) — factorial: ab(n−1) |
| RCBD R formula | `aov(obs ~ trt + blk)` — use `+`, not `*` |
| lm() coeff vs effect | coeff = Effect/2 — **double** to get effect |
| Unreplicated 2^k | df_error=0 → use DanielPlot (FrF2 package) |

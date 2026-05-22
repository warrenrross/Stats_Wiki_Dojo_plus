---
tags: [concept, section-1-2, section-3, section-4, reference]
tier: procedure
sources: [L26, L22&23W, formula-snippets, L42&43P, L44&45P, L46&47P, L48-50P 2kFD]
---
# Which Test to Use — Decision Guide

## Step 1: What parameter are you testing?

```
What is the parameter?
│
├─ Mean (μ) ──────────────────────────────────────────────────► Step 2a
├─ Variance/Std Dev (σ² or σ) ────────────────────────────────► Step 2b
├─ Proportion (p) ────────────────────────────────────────────► Proportion Z-test (L18)
├─ Comparing two means (μ₁ vs μ₂) ──────────────────────────► Step 2c
├─ Comparing 3+ treatment means (one factor) ────────────────► Step 2d (ANOVA)
├─ Comparing treatments with 2+ factors ─────────────────────► Step 2e (Factorial ANOVA)
├─ Comparing two variances (σ₁² vs σ₂²) ────────────────────► F-test (L25)
├─ Goodness-of-Fit ───────────────────────────────────────────► Chi-square GoF (L19)
├─ Independence (contingency table) ─────────────────────────► Chi-square Independence (L20)
└─ Regression coefficient ────────────────────────────────────► t-test on β (L34-35)
```

---

## Step 2a: Testing a Single Mean

```
Single mean μ — is σ known?
│
├─ YES (σ known) or n ≥ 40 ──► Z-test:  Z₀ = (x̄ − μ₀) / (σ/√n)
│
└─ NO (σ unknown), n < 40 ───► t-test:  T₀ = (x̄ − μ₀) / (s/√n),  df = n−1
```

---

## Step 2b: Testing a Single Variance

```
Single variance σ² ──► χ²-test:  χ²₀ = (n−1)s² / σ₀²,  df = n−1
```

---

## Step 2c: Comparing Two Means

```
Two means μ₁ vs μ₂ — are the samples PAIRED or INDEPENDENT?
│
├─ PAIRED (each obs matched) ──────────────────────────────────────────────────────────────────►
│     Compute dᵢ = x₁ᵢ − x₂ᵢ
│     Paired t-test:  T₀ = d̄ / (sD/√n),  df = n−1
│
└─ INDEPENDENT ────────────────────────────────────────────────────────────────────────────────►
      Are σ₁, σ₂ KNOWN?
      │
      ├─ YES ──► 2-Sample Z-test:  Z₀ = (x̄₁−x̄₂−Δ₀) / √(σ₁²/n₁ + σ₂²/n₂)
      │
      └─ NO ───► Are variances EQUAL? (check with F-test, or assume per problem)
                 │
                 ├─ EQUAL (pooled) ──► 2-Sample t (pooled):
                 │     Sp² = [(n₁−1)s₁² + (n₂−1)s₂²] / (n₁+n₂−2)
                 │     T₀ = (x̄₁−x̄₂−Δ₀) / [Sp√(1/n₁+1/n₂)],  df = n₁+n₂−2
                 │
                 └─ UNEQUAL (Welch) ──► 2-Sample t (unpooled):
                       T₀ = (x̄₁−x̄₂−Δ₀) / √(s₁²/n₁ + s₂²/n₂),  df = ν (Welch)
                       ν = (s₁²/n₁ + s₂²/n₂)² / [(s₁²/n₁)²/(n₁−1) + (s₂²/n₂)²/(n₂−1)]
```

---

## Step 2d: Comparing 3+ Treatment Means (One Factor)

```
One factor, ≥ 3 levels — is there a nuisance variable (batches, operators, days)?
│
├─ NO nuisance variable ──► CRD (Completely Randomized Design)
│     aov(obs ~ trt)
│     F₀ = MS_Trt / MS_E,  df: (a−1, N−a)
│     Post-hoc: Fisher LSD = t_{α/2, N−a} · √(2·MS_E/n)  [balanced]
│
└─ YES nuisance variable ──► RCBD (Randomized Complete Block Design)
      aov(obs ~ trt + blk)   ← use + not *
      F₀ = MS_Trt / MS_E,  df: (a−1, (a−1)(b−1))
      Post-hoc: Fisher LSD with df_E = (a−1)(b−1)
```

---

## Step 2e: Comparing Treatments with 2+ Factors

```
Multiple factors — are each factor's levels exactly ±1 (two levels each)?
│
├─ NO (general multilevel factorial) ──► Factorial ANOVA
│     2 factors: aov(obs ~ F1 * F2)       df_E = ab(n−1)
│     3 factors: aov(obs ~ F1 * F2 * F3)  df_E = abc(n−1)
│     If AB interaction significant: main effects cannot be interpreted separately
│
└─ YES (each factor has exactly 2 levels) ──► 2^k Factorial Design
      Replicated:   lm(obs ~ A + B + AB) + aov(obs ~ A * B)
                    Effect = Contrast / (n·2^{k−1}),  SS = Contrast² / (n·2^k)
                    lm() coefficient = Effect / 2  ← double to get effect
      Unreplicated: lm() → DanielPlot(lmmodel) from FrF2
                    (df_error = 0 → F-test undefined → use Daniel plot)
```

---

## Quick Summary Table

| Situation | Test | Test Statistic | df |
|-----------|------|----------------|----|
| 1 mean, σ known (or n≥40) | Z-test | (x̄−μ₀)/(σ/√n) | — |
| 1 mean, σ unknown | t-test | (x̄−μ₀)/(s/√n) | n−1 |
| 1 variance | χ²-test | (n−1)s²/σ₀² | n−1 |
| 1 proportion | Z-test | (p̂−p₀)/√(p₀(1−p₀)/n) | — |
| 2 means, σ known | 2-sample Z | (x̄₁−x̄₂−Δ₀)/√(σ₁²/n₁+σ₂²/n₂) | — |
| 2 means, equal σ², independent | Pooled t | (x̄₁−x̄₂−Δ₀)/[Sp√(1/n₁+1/n₂)] | n₁+n₂−2 |
| 2 means, unequal σ², independent | Welch t | (x̄₁−x̄₂−Δ₀)/√(s₁²/n₁+s₂²/n₂) | ν (Welch) |
| 2 means, paired | Paired t | d̄/(sD/√n) | n−1 |
| 2 variances | F-test | s₁²/s₂² | n₁−1, n₂−1 |
| Goodness-of-fit | χ² GoF | Σ(Oᵢ−Eᵢ)²/Eᵢ | k−1 |
| Independence (contingency) | χ² Indep | ΣΣ(Oᵢⱼ−Eᵢⱼ)²/Eᵢⱼ | (r−1)(c−1) |
| Regression coefficient | t-test | β̂ᵢ/SE(β̂ᵢ) | n−p−1 |
| Regression model overall | F-test | MSR/MSE | p, n−p−1 |
| 3+ means, no nuisance var | CRD (one-way ANOVA) | MS_Trt/MS_E | a−1, N−a |
| 3+ means, nuisance variable | RCBD | MS_Trt/MS_E | a−1, (a−1)(b−1) |
| 2-factor factorial | 2-factor ANOVA | MS_A/MS_E, MS_B/MS_E, MS_AB/MS_E | a−1; b−1; (a−1)(b−1); ab(n−1) |
| 2^k factorial (replicated) | 2^k ANOVA | Contrast²/(n·2^k) per effect | 1 each; 2^k(n−1) error |
| 2^k factorial (unreplicated) | Daniel plot | — | no error df |

---

## Key Questions to Ask in Any Problem
1. How many groups/populations? (1, 2, or more)
2. What is being measured? (mean, proportion, variance)
3. Are observations paired or independent?
4. Is σ known or unknown?
5. What is the sample size? (affects Z vs t)

## Related
- [[hypothesis-testing-overview]]
- [[two-sample-tests]]
- [[chi-square]]
- [[regression-ht]]
- [[crd-one-way-anova]]
- [[rcbd-blocking]]
- [[factorial-anova]]
- [[2k-factorial-design]]
- [[anova-design-guide]]

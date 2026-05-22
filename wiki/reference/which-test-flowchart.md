---
tags: [reference, section-1-2, section-3]
sources: [L26, L22&23W, 1-and-2-Sample-HT-Flowchart.pdf]
---
# Which Test Flowchart — Exam Quick Reference

## READ THIS FIRST on any problem

Ask yourself: **What does the problem want me to test or estimate?**

---

## Flowchart

```
ONE population? or TWO populations?
│
├─ ONE ────────────────────────────────────────────────────────────────────────────────────────
│   │
│   ├─ Testing μ (mean)?
│   │   ├─ σ known, or n ≥ 40 ──► Z-test | Z₀ = (x̄−μ₀)/(σ/√n)
│   │   └─ σ unknown, n < 40  ──► t-test | T₀ = (x̄−μ₀)/(s/√n), df=n−1
│   │
│   ├─ Testing σ² (variance)?
│   │   └─ ──► χ²-test | χ²₀ = (n−1)s²/σ₀², df=n−1
│   │
│   ├─ Testing p (proportion)?
│   │   └─ ──► Z-test | Z₀ = (p̂−p₀)/√(p₀(1−p₀)/n)
│   │
│   ├─ Testing distribution fit? ──► χ² Goodness-of-Fit | df=k−1
│   │
│   └─ Testing association in table? ──► χ² Independence | df=(r−1)(c−1)
│
└─ TWO ────────────────────────────────────────────────────────────────────────────────────────
    │
    ├─ Testing μ₁ vs μ₂?
    │   │
    │   ├─ Paired (matched pairs, before/after)?
    │   │   └─ ──► Paired t | dᵢ=x₁ᵢ−x₂ᵢ | T₀=d̄/(sD/√n), df=n−1
    │   │
    │   └─ Independent?
    │       ├─ σ₁,σ₂ known ──► 2-Sample Z | Z₀=(x̄₁−x̄₂−Δ₀)/√(σ₁²/n₁+σ₂²/n₂)
    │       ├─ σ unknown, equal variances ──► Pooled t | df=n₁+n₂−2
    │       └─ σ unknown, unequal variances ──► Welch t | df=ν (Welch formula)
    │
    ├─ Testing σ₁² vs σ₂² (variances)?
    │   └─ ──► F-test | F₀=s₁²/s₂², df: n₁−1, n₂−1
    │
    └─ Regression coefficient?
        └─ ──► t-test on βⱼ | T₀=β̂ⱼ/SE(β̂ⱼ), df=n−p−1
```

---

## "Which t?" — The Hardest Decision

| Clue in Problem | Use |
|-----------------|-----|
| "before and after on the same unit" | Paired t |
| "same subjects tested twice" | Paired t |
| "two independent groups / samples" | 2-sample t (pooled or Welch) |
| "assume equal variances" | Pooled t |
| "do not assume equal variances" | Welch t |
| "assume σ is known" | Z (not t) |
| large samples (n₁, n₂ ≥ 40) | Z acceptable |

---

## Rejection Criteria at a Glance

| Test Direction | H₁ | Reject H₀ if (fixed-level) | P-value |
|---------------|----|-----------------------------|---------|
| Two-sided | ≠ | \|stat\| > critical | 2·P(right tail) |
| Upper (right) | > | stat > critical | P(right tail) |
| Lower (left) | < | stat < −critical | P(left tail) |

---

## Common Trick Questions
- "Is there a difference?" → Two-sided (≠)
- "Does A exceed B?" → Upper-tailed (>)
- "Is A less than B?" → Lower-tailed (<)
- "Does the process meet spec?" → Often lower-tailed on fraction defective
- Δ₀ = 0 unless problem says "test if μ₁ − μ₂ = some value"

## Related
- [[which-test]]
- [[hypothesis-testing-overview]]
- [[two-sample-tests]]

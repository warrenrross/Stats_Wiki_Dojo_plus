---
tags: [concept, section-1-2, section-4]
tier: procedure
sources: [L14P, L15P, L44-45P]
---
# Power and Sample Size

## In Plain English
**Power** = probability of correctly detecting a real effect (= 1 − β).

Two types of error when making a decision about H₀:
- **Type I error (α):** Reject H₀ when it is actually true — a "false alarm." Controlled directly by your choice of significance level.
- **Type II error (β):** Fail to reject H₀ when it is actually false — a "missed detection."

**Power = 1 − β** — the probability of catching a real effect when it exists.

Three levers for increasing power:
1. **Larger effect size δ** — detect bigger differences more easily
2. **Larger sample size n** — the most principled lever when δ is fixed by the application
3. **Larger α** — buys power at the cost of more false alarms

## Error Table

| Decision | H₀ is True | H₀ is False |
|----------|-----------|------------|
| Reject H₀ | Type I error (prob = α) | Correct (power = 1−β) |
| Fail to reject H₀ | Correct (prob = 1−α) | Type II error (prob = β) |

## When To Use
- **Designing a study:** "How many observations do I need to detect an effect of size δ with 90% probability?"
- **Evaluating an existing study:** Did the study have adequate power to detect the hypothesized effect, or could a real effect have been missed?

## Formula(s)

### Case 1 — One-sample Z-test (σ known)

$$\beta = \Phi\!\left(z_{\alpha/2} - \frac{\delta\sqrt{n}}{\sigma}\right) - \Phi\!\left(-z_{\alpha/2} - \frac{\delta\sqrt{n}}{\sigma}\right)$$

Required n (two-sided):

$$n \approx \frac{(z_{\alpha/2} + z_\beta)^2 \sigma^2}{\delta^2}$$

where δ = |μ₁ − μ₀| is the **minimum detectable difference**.

---

### Case 2 — One-sample t-test (σ unknown, OC curve method)

1. Specify δ = minimum detectable difference and an estimate of σ
2. Compute d = δ / σ
3. For a trial n, compute df = n − 1
4. Look up β from the Operating Characteristic (OC) curve (Montgomery Appendix V, Chart VIa/VIb) using d and df
5. If 1 − β < target power, increase n and repeat

R: `power.t.test(n=NULL, delta=delta, sd=sigma, sig.level=alpha, power=0.90, type="one.sample")`

---

### Case 3 — Two-sample t-test (equal n per group, equal variances)

$$n \approx \frac{2(z_{\alpha/2} + z_\beta)^2 \sigma^2}{\delta^2}$$

R: `power.t.test(n=NULL, delta=delta, sd=sigma, sig.level=alpha, power=0.90, type="two.sample")`

---

### Case 4 — One-way ANOVA F-test (OC curve method)

1. Specify the τᵢ treatment effects (sum to zero) and estimate σ²
2. Compute $\Phi^2 = \frac{n \sum_i \tau_i^2}{a \sigma^2}$; then Φ = √Φ²
3. Use OC curve (Montgomery Appendix V) with ν₁ = a − 1, ν₂ = a(n − 1), α = 0.05
4. Read β; if 1 − β < target, increase n and repeat

R: `power.anova.test(groups=a, n=NULL, between.var=var(tau_vec), within.var=sigma2, power=0.90)`

Note: R's `between.var` takes the variance of the τᵢ vector (i.e., Στᵢ²/(a−1)), not Στᵢ²/a.

## Key Assumptions
- A prior estimate of σ is available — without this, sample size cannot be determined
- The minimum detectable difference δ is specified in advance based on practical importance, not statistical convenience
- Cases 1 and 3 use the normal approximation; Cases 2 and 4 use the t/F distributions via OC curves

## Common Mistakes
- Confusing β (Type II error probability) with power (= 1 − β)
- Using the Z-test n formula for t-test problems — always underestimates required n because it ignores the heavier tails of the t distribution
- Ignoring the OC curve for ANOVA — `power.anova.test()` uses a different parameterization than the formula; verify the `between.var` argument matches what you computed (variance of τ vector, not sum of τ²)
- Forgetting that power analysis requires a prior estimate of σ — without this, a sample size cannot be determined

## Key Insight
Increasing any one of {δ, n, α} increases power. Increasing α buys power at the cost of more false alarms. Increasing n is the most principled lever when δ is fixed by the application.

## Related
- [hypothesis-testing-overview](hypothesis-testing-overview.md) — 7-step procedure and error type definitions
- [crd-one-way-anova](crd-one-way-anova.md) — ANOVA F-test power: Case 4 above determines required replicates
- [two-sample-tests](two-sample-tests.md) — two-sample t power: Case 3 above
- [distributions](distributions.md) — power depends on the non-central t and F distributions
- [which-test](which-test.md) — choose the right power case once the test type is identified

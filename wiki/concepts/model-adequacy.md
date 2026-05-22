---
tags: [concept, section-3]
tier: procedure
sources: [L38-39P, Section3_Study_Guide.Rmd, L38_39W_ModelAdequacy_CA_Ross.pdf]
---
# Model Adequacy Checking

## In Plain English
Before trusting your regression results, check that the model's assumptions actually hold. The tool is residual analysis — looking at patterns in eᵢ = yᵢ − ŷᵢ. If assumptions are violated, your p-values and confidence intervals are wrong.

---

## The Four Assumptions on Errors

The regression model assumes εᵢ ~ N(0, σ²), independent. Equivalently:

1. **Mean zero:** E[εᵢ] = 0 — residuals should average to zero, no systematic pattern
2. **Constant variance (homoscedasticity):** Var(εᵢ) = σ² for all i — spread doesn't change with ŷ
3. **Independence:** εᵢ are uncorrelated — no time trend or autocorrelation
4. **Normality:** εᵢ is normally distributed

---

## Residual Plots and What They Reveal

| Plot | What to Look For | Violation Indicates |
|------|-----------------|---------------------|
| eᵢ vs ŷᵢ | Curved pattern | Nonlinearity — missing term |
| eᵢ vs ŷᵢ | Fan/funnel shape | Non-constant variance (heteroscedasticity) |
| eᵢ vs xⱼ | Curved pattern | Missed nonlinear term in that predictor |
| eᵢ vs time/run order | Trend or cycles | Autocorrelation |
| Normal Q-Q of eᵢ | Points off the line | Non-normality |

**Teacher's residual plot phrasing:**
> "The residuals show [no systematic pattern / a fan shape / a curved pattern], suggesting [no violation of / a violation of the constant variance / linearity] assumption."

```r
plot(fit)    # base R: 4 diagnostic plots automatically

# Custom ggplot residual vs fitted:
df$resid  <- residuals(fit)
df$fitted <- fitted(fit)
ggplot(df, aes(x = fitted, y = resid)) +
  geom_point() +
  geom_hline(yintercept = 0, linetype = "dashed") +
  labs(x = "Fitted Values", y = "Residuals")

# Normal Q-Q:
ggplot(df, aes(sample = resid)) + stat_qq() + stat_qq_line()
```

---

## Types of Unusual Observations

| Type | Definition | Detection |
|------|-----------|-----------|
| **Outlier** | Unusual y-value (large residual) | \|rᵢ\| > 3 (studentized) |
| **Leverage point** | Extreme x-value | hᵢᵢ > 2p/n |
| **Influential point** | Changes fit substantially if removed | Dᵢ > 0.5 or > 1 |

A point can be any combination. An outlier that is NOT a leverage point has limited influence on the fitted line. A leverage point with a small residual also has limited influence. **Concern is when both are true.**

---

## Standardized and Studentized Residuals

**Internally standardized:**
$$d_i = \frac{e_i}{\hat{\sigma}\sqrt{1 - h_{ii}}}$$

**Externally studentized (preferred):**
$$r_i = e_i\sqrt{\frac{n-p-1}{SSE(1-h_{ii}) - e_i^2}}$$

where hᵢᵢ = leverage (diagonal of hat matrix H = X(X'X)⁻¹X')

Rule of thumb: |rᵢ| > 3 → potential outlier

```r
rstandard(fit)     # dᵢ (internally standardized)
rstudent(fit)      # rᵢ (externally studentized — preferred)
hatvalues(fit)     # leverages hᵢᵢ
```

---

## Cook's Distance (Influence)

$$D_i = \frac{r_i^2}{p} \cdot \frac{h_{ii}}{1 - h_{ii}}$$

| Dᵢ value | Interpretation |
|----------|---------------|
| Dᵢ > 0.5 | Worth investigating |
| Dᵢ > 1.0 | Point is influential — substantially affecting the fit |

```r
cooks.distance(fit)
influence.measures(fit)    # comprehensive: DFFITS, DFBETAS, Cook's D
```

---

## Diagnostic Plot Guide — `plot(fit)` Outputs

R's `plot(fit)` generates four standard plots. The exam may show you one of these and ask which assumption can or cannot be evaluated.

| Plot | What you see | What it diagnoses | Violation sign |
|------|-------------|------------------|---------------|
| **1. Residuals vs Fitted** | eᵢ on Y, ŷᵢ on X | Linearity + constant variance | Curve = nonlinearity; funnel = heteroscedasticity |
| **2. Normal Q-Q** | Sorted residuals vs theoretical normal quantiles | Normality of errors | Points deviating from diagonal line (S-curve, heavy tails) |
| **3. Scale-Location** | √|rᵢ| on Y, ŷᵢ on X | Constant variance | Upward or downward trend in spread |
| **4. Cook's D** | Dᵢ on Y, observation index on X | Influence | Spikes above threshold (> 0.5 or > 1) |

**Evaluating each assumption:**
| Assumption | Which plot(s) to look at | "No violation" looks like |
|-----------|------------------------|--------------------------|
| Linearity | Plot 1 (Residuals vs Fitted) | Points scattered randomly around y = 0, no curve |
| Constant variance | Plot 1 + Plot 3 | Roughly equal spread across all fitted values |
| Normality | Plot 2 (Q-Q plot) | Points closely follow the diagonal line |
| Influential points | Plot 4 (Cook's D) | All bars below 0.5 |

**Exam phrasing when describing a plot:**
> "The residuals vs fitted plot shows [no systematic pattern / a funnel shape spreading from left to right / a curved U-shape], suggesting [no violation / non-constant variance / a nonlinear relationship that the model does not capture]."
> "The normal Q-Q plot shows [points closely following the diagonal / an S-shaped deviation from the line], suggesting [normality is approximately satisfied / the residuals have heavier tails than a normal distribution]."

---

## Necessary, Sufficient, and Definitive — How to Evaluate Models

This is a common exam question type: "What things are necessary but not sufficient? What things are definitive?"

### R² and Adjusted R²
- R² = SSR/SST — measures fraction of variance explained
- **R² can always be increased by adding more predictors** (even useless ones)
- A high R² does NOT mean the model is correct (spurious correlations, overfitting)
- R² is **necessary** context but **not sufficient** to validate a model
- R²_adj penalizes for extra predictors — **prefer adj R² when comparing models with different numbers of predictors**
- "R² increases" alone is **not sufficient evidence** that the new predictor belongs in the model

### F-test (Overall Model Significance)
- Tests H₀: all βⱼ = 0
- **Necessary:** If the F-test is not significant, the model has no value — stop here
- **Not sufficient:** A significant F-test means *at least one* predictor is useful, not that *all* are useful and not that the model is adequate
- A significant F-test says: "This model is better than nothing." It does not say: "This is the right model."

### Individual t-tests on βⱼ
- Tests H₀: βⱼ = 0 (given all other predictors in the model)
- **More definitive** than F-test for a specific predictor's contribution
- A non-significant t-test → that predictor does not contribute significantly beyond the others → candidate for removal
- A significant t-test → that predictor is worth keeping

### Residual Plots
- **Most definitive** for assumption checking — a visible pattern IS a violation
- Unlike R² or F-tests, you cannot argue around a pattern in residuals
- A fan shape in residuals vs fitted = constant variance is violated, period
- Clean residual plots are **necessary** for valid inference but don't tell you if the right predictors are in the model

### Summary — Decision Hierarchy

| Metric | What it tells you | Limitation |
|--------|------------------|-----------|
| F-test significant | At least one predictor is useful | Doesn't tell you which ones; doesn't validate assumptions |
| High R² | Model explains much of the variation | Inflated by adding predictors; doesn't catch assumption violations |
| High adj R² | Model explains variation, accounting for complexity | Better than R² but still not sufficient alone |
| t-test significant for βⱼ | That specific predictor contributes (given others) | Correlation between predictors can complicate this |
| Clean residual plots | Assumptions approximately satisfied | Doesn't tell you if you have the right predictors |

> **Exam application:** When asked to evaluate whether a model is adequate, you need ALL of: significant F-test + significant predictors have meaningful t-tests + clean residual plots. Any one alone is insufficient.

---

## Interpolation vs. Extrapolation

**Interpolation:** Predicting at an x₀ value **within** the range of observed data. Generally reliable.

**Extrapolation:** Predicting at an x₀ value **outside** the range of observed data. The linear relationship observed in the data range may not hold beyond it. Unreliable — extrapolation can be badly wrong.

**For MLR:** Extrapolation is more subtle — x₀ must be within the *joint* region of all predictor values, not just within each individual predictor's range. A combination of x₁ and x₂ values that is within each one's marginal range can still be extrapolation if that combination was never observed.

> "Predicting at x₀ = [value] is [interpolation / extrapolation] because [it falls within / outside] the range of observed x values ([min, max]). [Interpolation: the prediction is reliable within model assumptions. / Extrapolation: the prediction may be unreliable — the linear model may not hold outside the observed data range.]"

---

## What to Do When Assumptions Are Violated

| Violation | Solution |
|-----------|---------|
| Non-linearity | Add polynomial term (x²) or transform x (log x, √x) |
| Non-constant variance | Transform Y (log Y, √Y) or use weighted regression |
| Non-normality | Transform Y; check for outliers |
| Outlier | Investigate context — is it a data error? Report it. |
| Influential point | Refit without it and compare; report both |

See [[correlation-transformations]] for transformation details.

---

## Teacher's Conclusion Phrasing

**No violation:**
> "The residual plot shows no systematic pattern. The constant variance and linearity assumptions appear to be satisfied."

**Fan shape (non-constant variance):**
> "The residual plot shows a fan shape, suggesting that the constant variance assumption is violated. A transformation of Y may be appropriate."

**Curved pattern (nonlinearity):**
> "The residuals vs fitted plot shows a curved pattern, indicating that the linearity assumption is violated. A higher-order term or transformation should be considered."

**Influential point:**
> "Observation [#] has a Cook's distance of [D] > 1, indicating it is an influential point. The analysis should be repeated with this observation removed to assess its impact."

---

## Key Assumptions
Model assumptions must hold for valid inference. Residual analysis is not optional — especially for exam model adequacy questions.

## Common Mistakes
- Using raw residuals eᵢ instead of studentized rᵢ to detect outliers
- Concluding a point is influential based only on being an outlier (must check leverage too)
- Confusing leverage (unusual x) with influence (changing the fit)

## Project Context — Coffee Bean Production Analysis

Residual diagnostics are **required before interpreting any regression results** in the coffee project.

- **Expected finding on raw data:** Production (Y) is right-skewed → expect a fan-shaped residual plot (variance increasing with fitted values) → this is a non-constant variance violation
- **Recommended fix:** Log-transform Y (`log(production)`) before fitting. Fan shape in residuals vs fitted is the trigger.
- **Workflow:** Fit model on raw Y → check Plot 1 (residuals vs fitted) → if fan shape → refit with log(Y) → re-check residuals → if clean, proceed to t-tests and F-test
- With n ≈ 1500, the Q-Q plot will be reliable; minor deviations from normality are less critical at large n due to CLT, but non-constant variance affects CIs and p-values regardless of n

## Related
- [[regression-slr]]
- [[regression-mlr]]
- [[correlation-transformations]]

---
tags: [concept, section-1-2]
tier: procedure
sources: [L20P, formula-snippets]
---
# χ² Test of Independence (Contingency Table)

## In Plain English
Use when you have two categorical variables and want to test whether they are associated or independent. You arrange counts in a two-way table (r rows × c columns), compute expected counts under the assumption of independence, then measure how far the observed counts deviate from expected. Always upper-tail only.

## When To Use
- Two categorical variables measured on the same subjects
- Data organized as an r × c contingency table
- Testing whether the two variables are independent
- All expected counts Eᵢⱼ ≥ 5

## Formula(s)

| Symbol | Meaning |
|--------|---------|
| Oᵢⱼ | observed count in row i, column j |
| Eᵢⱼ | expected count in cell (i,j) under independence |
| r | number of rows |
| c | number of columns |
| n | grand total |

**Expected cell frequencies (under H₀: independence):**
$$E_{ij} = \frac{(\text{row } i \text{ total}) \times (\text{col } j \text{ total})}{n}$$

**Test statistic:**
$$\chi_0^2 = \sum_{i=1}^{r}\sum_{j=1}^{c} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$

**Degrees of freedom:**
$$df = (r-1)(c-1)$$

**Rejection criterion:** Reject H₀ if χ₀² > χ²_{α, (r−1)(c−1)} (always upper-tail)

## Hypotheses
- **H₀:** The two variables are independent
- **H₁:** The two variables are **not** independent (associated)

## Key Assumptions
- Observations are independent
- All expected frequencies Eᵢⱼ ≥ 5 (merge rows/columns if violated)
- Each subject falls in exactly one cell

## Common Mistakes
- Using observed counts to compute Eᵢⱼ — must use marginal totals
- Using df = r·c − 1 instead of (r−1)(c−1)
- Confusing this test with GoF — independence uses a 2-way table; GoF uses one-way category counts
- Forgetting that significance means association, not causation

## Related
- [[ht-goodness-of-fit]] — one-variable χ² test for distributional fit
- [[ht-one-sample-chisq-variance]] — χ² test on σ²
- [[chi-square]] — broader coverage of all χ² procedures
- [[ht-tests-overview]] — full test selection table

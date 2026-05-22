---
tags: [concept, section-1-2]
tier: procedure
sources: [L17P, L19P, L20P, formula-snippets]
---
# Chi-Square Tests

## In Plain English
Chi-square tests compare observed counts to expected counts. Two uses: (1) **Goodness-of-Fit** — does my data follow a claimed distribution? (2) **Test of Independence** — are two categorical variables related in a contingency table?

---

## Chi-Square Distribution
- Right-skewed, non-negative
- Shape controlled by degrees of freedom k
- As k increases, distribution becomes more symmetric

Critical values from χ² table: χ²_{α,k} is the upper α percentage point with k df.

---

## Test 1: Goodness-of-Fit (L19)

**When:** One categorical variable, testing whether observed frequencies match expected frequencies from a hypothesized distribution.

**H₀:** The population follows the hypothesized distribution  
**H₁:** It does not

**Test statistic:**
$$\chi_0^2 = \sum_{i=1}^{k} \frac{(O_i - E_i)^2}{E_i}$$

| Symbol | Meaning |
|--------|---------|
| k | number of categories |
| Oᵢ | observed count in category i |
| Eᵢ | expected count = n · p_i (hypothesized proportion) |

**Degrees of freedom:** df = k − 1 (subtract 1 more for each estimated parameter)

**Rejection criterion:** Reject H₀ if χ²₀ > χ²_{α, k−1}

**Assumption:** All Eᵢ ≥ 5 (combine categories if needed)

---

## Test 2: Test of Independence — Contingency Table (L20)

**When:** Two categorical variables; data is a two-way table of counts.

**H₀:** The two variables are independent  
**H₁:** They are not independent (associated)

**Test statistic:**
$$\chi_0^2 = \sum_{i=1}^{r}\sum_{j=1}^{c} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$

**Expected cell counts:**
$$E_{ij} = \frac{(\text{row } i \text{ total}) \times (\text{col } j \text{ total})}{\text{grand total}}$$

**Degrees of freedom:** df = (r − 1)(c − 1)  
where r = number of rows, c = number of columns

**Rejection criterion:** Reject H₀ if χ²₀ > χ²_{α, (r−1)(c−1)}

**Assumption:** All Eᵢⱼ ≥ 5 (or ≥ 1 with no more than 20% below 5)

---

## Test 3: HT on Variance (L17) — also uses χ²

**H₀:** σ² = σ₀²

**Test statistic:**
$$\chi_0^2 = \frac{(n-1)s^2}{\sigma_0^2}, \quad \text{df} = n-1$$

| H₁ | Reject H₀ if |
|----|--------------|
| σ² ≠ σ₀² | χ²₀ > χ²_{α/2,n−1} **or** χ²₀ < χ²_{1−α/2,n−1} |
| σ² > σ₀² | χ²₀ > χ²_{α,n−1} |
| σ² < σ₀² | χ²₀ < χ²_{1−α,n−1} |

---

## Contingency Table Worked Pattern

```
         Col 1    Col 2    Total
Row 1     O₁₁     O₁₂      R₁
Row 2     O₂₁     O₂₂      R₂
Total     C₁      C₂       N

E₁₁ = (R₁ × C₁)/N
```

---

## Teacher's Conclusion Phrasing

**GoF — Reject H₀:**
> "Because χ²₀ = [value] > χ²_{α,k−1} = [critical value], we reject H₀. There is sufficient evidence that the data do not follow the hypothesized distribution."

**Independence — Reject H₀:**
> "Because χ²₀ = [value] > χ²_{α,(r−1)(c−1)} = [critical value], we reject H₀. There is sufficient evidence that [variable A] and [variable B] are not independent."

## Key Assumptions
- Random sample
- Expected cell counts ≥ 5 (GoF and contingency)
- Categories are mutually exclusive and exhaustive

## Common Mistakes
- Using Oᵢⱼ instead of Eᵢⱼ in the denominator
- Forgetting to compute Eᵢⱼ from marginal totals (using raw column proportions instead)
- Wrong df: GoF is k−1, contingency is (r−1)(c−1), variance test is n−1

## Related
- [[distributions]]
- [[hypothesis-testing-overview]]
- [[which-test]]

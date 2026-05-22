# Handoff Queue

This file is the processing queue between other agents (or Warren) and the wiki agent.

**How it works:**
1. Any agent or Warren appends a `[pending]` entry to the Queue section below
2. Raw files go in `Stats Notes/_inbox/` — reference them by filename in the entry
3. At the start of each wiki session, the wiki agent reads this file, processes pending items in order, and marks them `[done]` or `[failed]`
4. Done entries stay here as a record (don't delete them)

---

## How to Write an Entry (Template)

Copy-paste this block and fill it in:

```
### [pending] Short descriptive title
- **Source:** path/to/file  OR  _inbox/filename.txt  OR  URL (if content already copied to _inbox)
- **Action:** ingest | enrich | create | update
- **Target:** concepts/topic.md  OR  examples/topic.md  OR  new page
- **Section:** 1-2 | 3 | core | all
- **Notes:** Any context the wiki agent needs — what the content is, what's most important, any specific formulas or examples to capture
- **Added by:** agent-name | user | web-research-agent
- **Date:** YYYY-MM-DD
```

**Action types:**
| Action | Meaning |
|--------|---------|
| `ingest` | New source — extract content and create/update wiki pages |
| `enrich` | Existing wiki page needs more detail added from this source |
| `create` | Create a specific new page (content described in Notes) |
| `update` | Correct or replace something specific in an existing page |

---

## Queue

### [done] Cross-link audit — 17 additions to 13 existing pages + 2 new core concept pages
- **Processed:** 2026-04-29 — Applied all Phase 1–4 changes from cross-link audit.
  Phase 1: Added 17+ cross-links across 13 concept pages (confidence-intervals, hypothesis-testing-overview, two-sample-tests, crd-one-way-anova, regression-slr, standard-error, correlation-transformations, distributions, regression-ht, regression-ci, random-effects-model, factorial-anova, variance-estimation). Key connections: CI↔regression-ci, HT overview↔regression-ht↔crd, two-sample-t↔CRD, distributions↔Fisher-Z, standard-error↔regression-slr.
  Phase 2: Created `concepts/ss-decomposition.md` (tier: construct) — hub page for the SS_Total = SS_Model + SS_Error identity that underpins every ANOVA table in the course. Back-links added to regression-slr, regression-ht, regression-mlr, crd-one-way-anova, rcbd-blocking, factorial-anova, 2k-factorial-design.
  Phase 3: Created `concepts/power-sample-size.md` (tier: procedure) — covers β/power/n for one-sample Z, one-sample t (OC curve), two-sample t, and one-way ANOVA F (Φ² formula and R code). Back-links added to hypothesis-testing-overview, crd-one-way-anova, two-sample-tests.
  Phase 4: Updated index.md (ss-decomposition in Tier 1 Constructs, power-sample-size in Section 1-2 Procedures) and taxonomy.md (both new pages added to their respective tiers).
- **Source:** Claude Code cross-link audit session 2026-04-29
- **Action:** update + create
- **Target:** Multiple pages — see notes
- **Section:** all
- **Added by:** Claude Code (cross-link audit 2026-04-29)
- **Date:** 2026-04-29

### [done] 2^2 Factorial — all effects non-significant due to high within-cell variance
- **Source:** `Section_4/Drills/L48-50_App_HWK_Q2.R`, `L48-50_App_HWK_Q2.csv`
- **Action:** enrich
- **Target:** `concepts/2k-factorial-design.md` or `concepts/factorial-anova.md`
- **Section:** 4
- **Notes:**
  1. **Null result possible even with real effects** — Root vole density experiment (2^2, n=3): high within-cell variance (SD≈58 in no-predator cells vs SD≈18 in predator cells) inflates MS_Error to 1835, making F_Food=0.97 and F_Pred=5.08 both non-significant at α=0.05. Real biological effect may exist but statistical power is insufficient.
  2. **Borderline F** — F_Pred=5.08 vs F_crit(1,8)=5.318; students must compare to the critical value, not just judge the number qualitatively.
  3. **Heteroscedasticity tied to treatment level** — variance was high for one level of a factor (no-predator) and low for the other (predator). Max/min cell SD ratio ≈3.3× triggers the constant variance flag.
  4. **Wide→long with 3 replicates** — `pivot_longer(cols=c(R1,R2,R3), names_to="Rep", values_to="Response")`. Same pattern as Q1 but 3 cols instead of 2.
  5. **Shapiro-Wilk on residuals** — use for normality check; right-skewed residuals from the large-outlier replicates (200.979, 172.339) expected to reject normality.
- **Added by:** Claude Code (L48-50 Q2 session 2026-04-30)
- **Date:** 2026-04-30
- **Processed:** 2026-05-12 — Added null result / power trap, borderline F rule, heteroscedasticity 3× rule, and three-replicate pivot_longer pattern to `2k-factorial-design.md` Common Mistakes and R Coding Patterns sections.

### [done] 2^4 single replicate — Lenth PSE/ME screening + setwd pattern for Drills/ HWK scripts
- **Source:** `Section_4/Drills/L48-50_App_HWK_Q4.R`, `L48-50_App_HWK_Q4.csv`
- **Action:** enrich
- **Target:** `concepts/2k-factorial-design.md`
- **Section:** 4
- **Notes:**
  1. **Lenth's ME formula for unreplicated 2^k** — s₀ = 1.5×median(|effects|); PSE = 1.5×median(|effects where |e|<2.5s₀|); ME = t(α/2, m/3)×PSE. For 2^4 (m=15): df=5, t(0.025,5)≈2.571, ME=2.571×PSE. Effects with |e|≥ME are flagged significant. This is what FrF2::DanielPlot automates.
  2. **Effect extraction with colon-notation** — when `lm(y ~ A*B*C*D)` is used, R creates interaction names like `A:B`. To map these to short labels (AB), build `effect_terms` and `effect_labels` vectors and index with `coef_tbl[effect_terms, "Estimate"]`.
  3. **setwd pattern for Drills/ HWK scripts** — HWK scripts live in `Drills/` with no .Rproj. Add `if (rstudioapi::isAvailable()) setwd(dirname(rstudioapi::getActiveDocumentContext()$path))` after `p_load()` to auto-set working directory when opened in RStudio. Without this, running from a subdirectory project context causes "file not found" for relative CSV/xlsx paths.
  4. **Biodiesel Q4 key results (2^4, n=1):** B=28.025, BD=6.800, AB=−6.675, D=5.550, C=4.925, A=4.175; Q16=Option E (all 4 mains + AB,BD), Q17=Option E (increase B,C,D), Q18=Option A (variation increases; normality OK).
- **Added by:** Claude Code (L48-50 Q4 session 2026-04-30)
- **Date:** 2026-04-30
- **Processed:** 2026-05-12 — Added Lenth's PSE/ME formula, effect extraction with colon-notation, and setwd pattern to `2k-factorial-design.md` (Unreplicated Designs section + R Coding Patterns).

### [done] 2^k Full Factorial — single replicate lm() pattern, effect estimates, and HWK scripts
- **Source:** `Section_4/Drills/L48-50_App_HWK_Q1.R`, `L48-50_App_HWK_Q3.R`
- **Action:** enrich
- **Target:** `concepts/2k-factorial-design.md` + `r-code/` (or create `r-code/2k-r.md`)
- **Section:** 4
- **Notes:**
  1. **Single replicate pattern** — 2^5 with n=1 has 0 error df; do NOT use aov(). Fit a saturated lm() with all 31 predictors (main + all interactions as pre-computed columns). Effect = 2 × lm coefficient. `coef_tbl <- summary(fit_lm)$coefficients; effects <- 2 * coef_tbl[term, "Estimate"]`.
  2. **Pre-compute interaction columns** — rather than relying on aov()'s "A:B" colon-notation row names, compute `AB = A*B` etc. via `mutate()` and name them explicitly. Avoids the trimws() problem for interaction lookups.
  3. **Two-replicate pattern** — for 2^3 with n=2, data has R1/R2 columns; `pivot_longer(cols=c(R1,R2), names_to="Rep", values_to="Response")` then standard `aov(Response ~ A*B*C)`. Row names still need `trimws()`.
  4. **Effect = 2 × lm coefficient** (not the coefficient itself) — common exam/HWK trap. The lm() spans ±1 (range = 2), so coefficient = Effect/2.
  5. **Pooled error for unreplicated 2^k** — fit main + 2-way only; 3-way+ (16 df for 2^5) become error. But homework may want effect estimates (lm route), not F-tests — read the question carefully.
  6. **Key nuclear pump results (2^5, n=1):** A=75.25, B=−48.75, C=158.00, D=−19.63, E=−35.25, AC=57.75, CE=−61.75.
  7. **Key cutting tool results (2^3, n=2):** F_A=0.54 not sig, F_B=11.53 sig, F_C=8.36 sig, F_AB=0.21 not sig, F_AC=23.10 sig, F_BC=0.96 not sig.
- **Added by:** Claude Code (L48-50 HWK session 2026-04-29)
- **Date:** 2026-04-29
- **Processed:** 2026-05-12 — Added single-replicate lm() pattern, pre-computed interaction columns, two-replicate pivot_longer+aov() pattern, and Effect=2×coef reinforcement to `2k-factorial-design.md` R Coding Patterns. Key results from nuclear pump (2^5) and cutting tool (2^3) included.

### [done] Two-Factor Factorial ANOVA — R patterns, diagnostic rules, interaction interpretation
- **Source:** `Section_4/Drills/L46-47_App_HWK_Q1.R`, `L46-47_App_HWK_Q2.R`, `L46-47_App_HWK_Q4.R`
- **Action:** enrich
- **Target:** `concepts/factorial-anova.md` + `r-code/` (or create `r-code/factorial-r.md`)
- **Section:** 4
- **Notes:**
  1. **trimws() is mandatory after `summary(fit)[[1]]`** — R pads ANOVA row names with trailing spaces; any named lookup returns NA without `rownames(aov_tbl) <- trimws(rownames(aov_tbl))`. Affects every two-factor+ ANOVA script.
  2. **Constant variance diagnostic rule** — if one cell's within-cell residuals are ~3× larger than all other cells, constant variance is NOT reasonable. Example: cell (Solder=260, Method=1) had range ≈0.40μm vs ≈0.07–0.13μm elsewhere → NOT reasonable.
  3. **Hierarchical (marginality) principle** — if the AB interaction is in the model, both A and B must remain even if B's p-value is large. Dropping B when AB is present creates an uninterpretable model.
  4. **Non-significant interaction implication** — if interaction is NOT significant, the optimal factor-A recommendation does not change regardless of factor B's level. Directly tested in exam questions.
  5. **LSD on factorial** — when interaction is negligible, apply Fisher LSD to marginal means of the significant factor using `LSD.test(fit, "FactorB", group=TRUE)`. LSD formula uses df_E = ab(n−1) and n_i = a·n (observations per marginal mean level).
  6. **Worked problem values to add to examples:**
     - Q1 (Viscosity): F_pH=6.44, F_cat=0.00, F_int=25.22; F_crit(0.05,1,12)=4.747 → interaction significant
     - Q4 (Warping): F_Temp=7.67, F_Cu=34.33, F_Int=1.86; LSD=2.76; significant pairs: 40v60, 40v80, 40v100, 60v100, 80v100; NOT 60v80
- **Added by:** Claude Code (L46-47 HWK session 2026-04-25)
- **Date:** 2026-04-25
- **Processed:** 2026-05-12 — Added trimws() mandatory pattern, LSD.test() for factorial marginal means, pivot_longer for 2/3-replicate designs, and worked problem key results to `factorial-anova-r.md`. Added 3× SD rule, marginality principle, non-significant interaction implication, and LSD formula to `factorial-anova.md`.

### [done] RCBD vs CRD comparison — blocking effect on MS_Error
- **Source:** `Section_4/Drills/L44-45_App_HWK_Q5.R` (Q6–Q8 block) + `Section4_study_guide.md`
- **Action:** enrich
- **Target:** `concepts/rcbd-blocking.md`
- **Section:** 4
- **Notes:** Add a section showing what happens when blocks are ignored (CRD on blocked data): SS_Block folds into SS_Error, MS_Error inflates, F₀ shrinks. Show the formula: SS_Error_CRD = SS_Blk + SS_E_RCBD; df_Error_CRD = a(n−1). Cotton % example: MS_Error 5.79 → 8.06, F₀ 20.54 → 14.76.
- **Added by:** Claude Code (L44-45 HWK session 2026-04-23)
- **Date:** 2026-04-23
- **Processed:** 2026-05-12 — Added "What Happens When Blocks Are Ignored" section to `rcbd-blocking.md` with formula chain (SS_Error_CRD = SS_Blk + SS_E_RCBD), df comparison table, and cotton example (MS_Error 5.79→8.06, F₀ 20.54→14.76).

### [done] Reverse-engineer ANOVA table from MS and F — new exam pattern
- **Source:** `Section_4/Drills/L44-45_App_HWK_Q4.qmd` + `Section4_study_guide.md`
- **Action:** enrich
- **Target:** `examples/anova-table-examples.md`
- **Section:** 4
- **Notes:** Add a DOE-specific worked example for the "given MS and F, fill the rest" pattern. Key formulas: SS = MS × df; MS_E = MS_Factor / F₀; SS_E = MS_E × df_E; SS_Total by addition. Distinct from the regression reconstruction example already in the file. Use Q4 numbers (a=4, b=5, MS_Fac=115.2067, F₀=3.498, MS_Blk=71.9775).
- **Added by:** Claude Code (L44-45 HWK session 2026-04-23)
- **Date:** 2026-04-23
- **Processed:** 2026-05-12 — Added Example 5 (DOE RCBD reverse-engineer from MS and F) to `anova-table-examples.md` with full formula chain, Q4 numbers (a=4, b=5, F₀=3.498), borderline-F note, and DOE memo distinguishing this from the regression reconstruction pattern.

### [done] Coffee bean production stats project — annotate wiki pages as project reference
- **Processed:** 2026-04-23 — Added "Project Context" sections to correlation-transformations.md, regression-mlr.md, regression-ht.md, model-adequacy.md with project-specific notes (log-transform Y, panel fixed effects, df ≈ 1495, Python/R mapping).
- **Source:** `/Users/warrenrross/Education/INEG/INEG Stats/Project/CLAUDE.md`, `data_transformations.md`
- **Action:** enrich
- **Target:** `concepts/correlation-transformations.md`, `concepts/regression-mlr.md`, `concepts/regression-ht.md`, `concepts/model-adequacy.md`
- **Section:** 3
- **Notes:** The Project folder contains a stats assignment (not a viz project) analyzing whether avg temperature, rainfall, population, and oil price correlate with coffee bean production and export revenue. The analytical methods map directly to Section 3 content. Cross-reference wiki pages most relevant to this project:
  1. **`[[correlation-transformations]]`** — Pearson r and H₀:ρ=0 test (T₀ formula) are the primary first-pass analysis. Production is right-skewed — the log transformations table (power/exponential) applies directly. Fisher Z-test (pending HANDOFF item) is needed if testing H₀:ρ=ρ₀ to compare correlation strength across variables.
  2. **`[[regression-mlr]]`** — Primary model: `production ~ temp + rainfall + population + oil_price`. MLR F-test and adjusted R² are the key outputs.
  3. **`[[regression-ht]]`** — t-tests on individual β coefficients to determine which factors are statistically significant. Panel fixed-effects adds country + year dummy terms as additional predictors.
  4. **`[[model-adequacy]]`** — Residual plots required before interpreting any regression results. Fan-shaped residuals expected on raw production (right-skewed) → log-transform Y first.
  5. **`[[regression-ci]]`** — CIs on β coefficients to quantify effect size ranges.
  6. **`[[standard-error]]`**, **`[[degrees-of-freedom]]`** — Cross-cutting; needed for manual checks against `statsmodels` output.
  - `statsmodels.formula.api.ols` (Python) maps to `lm()` in R — ANOVA table structure is identical; column names differ (see `[[reading-r-output]]` for R↔Python term mapping context).
  - Data panel covers ~50 coffee-producing countries × ~30 years ≈ n ≈ 1500 rows. With 4 predictors: df_error = ~1495, F-test df = (4, ~1495).
- **Added by:** Claude Code (project setup session 2026-04-20)
- **Date:** 2026-04-20

### [done] _inbox/ANOVA_learned.md — regression ANOVA formula chain scenarios
- **Processed:** 2026-04-23 — Added Example 2b (Scenario B: reconstruct from F₀ and σ̂²) to anova-table-examples.md with full formula chain. Scenarios A and C were already covered by existing examples. Source file may be deleted from _inbox/.
- **Source:** `_inbox/ANOVA_learned.md`
- **Action:** enrich
- **Target:** `examples/anova-table-examples.md`
- **Section:** 3
- **Notes:** Three scenarios for reconstructing a regression ANOVA table from partial information: (A) given SS components → build full table; (B) given F₀, σ̂², and n → reconstruct; (C) working from the coefficients table for CI and non-zero null t-tests. Includes formula chains for SSR, MSR, MSE, F₀, R², R²_adj. This enriches the existing anova-table-examples.md with regression-specific reconstruction patterns. Assign tier: script.
- **Added by:** Claude Code (wrap-up scan 2026-04-22)
- **Date:** 2026-04-22

### [done] CPS cognitive tier model — add tier: frontmatter + taxonomy page
- **Source:** knowledge-dimensions.md + sharded-finding-valiant.md plan
- **Action:** create + update
- **Target:** All 39 content pages (added `tier:` frontmatter), `CLAUDE.md` (CPS section + templates updated), `concepts/taxonomy.md` (created), `index.md` (reorganized by tier within section)
- **Section:** all
- **Processed:** 2026-04-22 — 39 pages tagged, taxonomy.md created, CLAUDE.md updated, index.md reorganized.
- **Added by:** user (Warren, session 2026-04-14)
- **Date:** 2026-04-14

### [done] Fisher Z-transformation formulas and R patterns for correlation — L40-41 HW session
- **Processed:** 2026-04-23 — Added to correlation-transformations.md: Fisher Z-test for H₀:ρ=ρ₀ (Z₀ formula), CI on ρ via tanh/arctanh, rounding instruction, p-value formulas for both nulls, no-data workflow, R code block (atanh/tanh/pnorm). Both test types now documented with clear "which formula to use" table.
- **Source:** `../Section_3/Drills/Regression in R/L40-41_App_HWQ1.R`, `L40-41_App_HWQ2.R`, `L40-41_App_HWQ3.R`
- **Action:** enrich
- **Target:** `concepts/correlation-transformations.md`
- **Section:** 3
- **Notes:** The page has T₀ for H₀: ρ=0 but is missing the following, all confirmed in slide eq. 11.49/11.50:
  1. **Fisher Z-test for H₀: ρ = ρ₀** — Z₀ = (arctanh(r̂) − arctanh(ρ₀)) × √(n−3), compared to z_{α/2} = 1.96; p-value = 2*pnorm(-abs(Z0))
  2. **CI on ρ** — tanh(arctanh(r̂) ± z_{α/2}/√(n−3)); uses z_{α/2} = 1.96 for 95%
  3. **Rounding instruction** — some textbook problems say "use z-values rounded to two decimal places"; this means round arctanh(r) and arctanh(ρ₀) to 2 dp before computing Z₀ or CI bounds — it changes answers materially
  4. **p-value for H₀: ρ=0** — `2 * pt(-abs(T0), df = n-2)`; p-value for H₀: ρ=ρ₀ — `2 * pnorm(-abs(Z0))`
  5. **No-data workflow** — when r and n are given directly (no dataset), skip lm() entirely; set r and n as scalars and proceed with formulas
  6. **R code block** to add: `atanh(r)` = arctanh(r); `tanh(z)` = back-transform; `2*pt(-abs(T0), n-2)` for p-value (a); `2*pnorm(-abs(Z0))` for p-value (b)
- **Added by:** Claude Code (L40-41 HW session 2026-04-16)
- **Date:** 2026-04-16

---

## Processed

### [done] Section 4 — Experimental Design ingest (Lessons 42–50)
- **Source:** Section_4/Slides/ (4 PDFs) + Section_4/Drills/ (10 R scripts)
- **Action:** ingest
- **Target:** 12 new pages + 4 updated pages
- **Section:** 4
- **Processed:** 2026-04-22 — All 12 pages created. Updated which-test.md (Step 2d/2e + ANOVA summary table), formula-sheet.md (Section 4 block), index.md (Section 4 section), log.md (this entry).



### [deferred] Normal probability plot with probability on Y axis (Blom positions)
- **Source:** `../Section_3/Drills/Regression in R/L38-39_App_HWQ1.R` (lines 73-91) and `L38-39_App_HWQ3.R`
- **Action:** enrich
- **Target:** `examples/model-adequacy-examples.md` — Probability-on-Y-axis format (textbook style)
- **Deferred:** 2026-04-14 — Cook's D is NOT on Test 3; deferred until post-exam session

### [deferred] car::qqPlot with confidence envelope bands
- **Source:** `../Section_3/Drills/Regression in R/L38-39_App_HWQ4.R` (lines ~58-70)
- **Action:** enrich
- **Target:** `examples/model-adequacy-examples.md` + `r-code/regression-r.md`
- **Deferred:** 2026-04-14 — post-exam; still valuable for R code fluency

### [deferred] Cook's distance 4/n threshold + deletion/refit workflow
- **Source:** `../Section_3/Drills/Regression in R/L38-39_App_HWQ4.R` (lines ~88-115) and `L38-39_App_HWQ5.R`
- **Action:** enrich
- **Target:** `concepts/model-adequacy.md` + `examples/model-adequacy-examples.md`
- **Deferred:** 2026-04-14 — Cook's D explicitly excluded from Test 3 scope; process post-exam

### [done] Concept checkpoint clippings L27-28 and L29-30
- **Source:** `Stats Notes/_inbox/Assessment Feedback.md`, `Assessment Feedback 1.md`, `Assessment Feedback 2.md`
- **Processed:** 2026-04-14 — enriched control-charts.md, process-capability.md, control-chart-examples.md; source files deleted

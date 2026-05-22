# Wiki Log

Append-only record of all wiki operations. Format: `## [YYYY-MM-DD] operation | description`

Parse recent entries: `grep "^## \[" log.md | tail -10`

---

## [2026-05-12] enrich | HANDOFF queue cleared — 6 pending Section 4 items processed

### Item 1: 2^2 null result — `concepts/2k-factorial-design.md`
- Added to Common Mistakes: null result ≠ no effect (power / high variance issue), borderline F requires exact F_crit comparison, heteroscedasticity tied to a treatment level (3× rule)
- Added three-replicate `pivot_longer` pattern to R Coding Patterns section

### Item 2: 2^4 Lenth PSE/ME — `concepts/2k-factorial-design.md`
- Added Lenth's PSE/ME formula subsection within Unreplicated Designs (s₀, PSE, ME = t_{α/2,m/3} × PSE)
- Added effect extraction with colon-notation (coef_tbl[effect_terms, "Estimate"])
- Added setwd auto-detect pattern for Drills/ scripts

### Item 3: 2^k single/two-replicate R patterns — `concepts/2k-factorial-design.md`
- Added single-replicate pattern: saturated lm() with pre-computed interaction columns, Effect = 2 × coef
- Added two-replicate pattern: pivot_longer + aov() + trimws()
- Key results: nuclear pump 2^5 (C=158.00 dominant) and cutting tool 2^3 (F_AC=23.10 sig)

### Item 4: Two-factor factorial ANOVA — `concepts/factorial-anova.md` + `r-code/factorial-anova-r.md`
- `factorial-anova.md`: Added Diagnostic Rules (3× SD rule), Marginality Principle, Non-significant Interaction Implication, LSD on Factorial section with formula and teacher's phrasing
- `factorial-anova-r.md`: Added trimws() mandatory pattern, LSD.test() usage, pivot_longer for 2/3-replicate 2^k data, worked problem key results table (Viscosity, Warping, Root vole)

### Item 5: RCBD vs CRD — `concepts/rcbd-blocking.md`
- Added "What Happens When Blocks Are Ignored" section: SS_Error_CRD = SS_Blk + SS_E_RCBD, df comparison, cotton example (MS_Error 5.79→8.06, F₀ 20.54→14.76)

### Item 6: DOE ANOVA reverse-engineer — `examples/anova-table-examples.md`
- Added Example 5: RCBD reconstruction from MS_Factor, F₀, MS_Blocks; Q4 numbers (a=4, b=5, F₀=3.498, MS_E=32.94); borderline F₀ vs F_crit; DOE formula chain memo

Pages updated: `concepts/2k-factorial-design.md`, `concepts/factorial-anova.md`, `concepts/rcbd-blocking.md`, `r-code/factorial-anova-r.md`, `examples/anova-table-examples.md`, `index.md` (5 summary lines updated), `HANDOFF.md` (6 items marked done)

---

## [2026-04-23] enrich | HANDOFF queue cleared — 3 pending items processed

### Item 1: Fisher Z-transform — correlation-transformations.md
- Added full Fisher Z section: H₀:ρ=ρ₀ test statistic Z₀ = (arctanh(r̂) − arctanh(ρ₀))√(n−3) ~ N(0,1)
- Added CI on ρ via tanh(arctanh(r̂) ± z_{α/2}/√(n−3))
- Added rounding instruction (round arctanh values to 2 dp when problem specifies)
- Added p-value decision table: t-distribution for H₀:ρ=0, normal for H₀:ρ=ρ₀
- Added no-data workflow and R code (`atanh()`, `tanh()`, `pnorm()`)

### Item 2: Coffee project cross-references — 4 pages enriched
- `correlation-transformations.md`: Fisher Z already added above; transformations apply to right-skewed production
- `regression-mlr.md`: primary model, panel fixed effects, df ≈ 1495, Python/R column mapping
- `regression-ht.md`: individual β t-tests, panel dummies, non-zero null workflow
- `model-adequacy.md`: expected fan-shape on raw data, log-transform Y workflow, n≈1500 Q-Q context

### Item 3: ANOVA_learned.md — anova-table-examples.md
- Added Example 2b: Scenario B (reconstruct from F₀ and σ̂²) with full formula chain memo
- Scenarios A and C were already covered by existing Examples 1, 2, 3, 4
- ANOVA_learned.md in _inbox/ can now be deleted

---

## [2026-04-23] ingest | Source: Section1&2 formula snippets (L15P–L25P) + quick_reference_Exam2.docx — Pages created/updated: 11 new pages

### New pages created (concepts/)
- `ht-one-sample-z-mean.md` — One-sample Z on mean: test stat, CI, β, sample size formulas
- `ht-one-sample-t-mean.md` — One-sample T on mean: σ unknown, t_{n−1} distribution
- `ht-one-sample-chisq-variance.md` — χ² test on σ²: test stat, rejection criteria, asymmetric CI
- `ht-one-sample-z-proportion.md` — Z test on proportion: count + proportion forms, CI uses P̂, sample size
- `ht-goodness-of-fit.md` — χ² GoF: test stat, df = k−1−p (general), Eᵢ = n·pᵢ
- `ht-independence.md` — χ² independence: Eᵢⱼ from marginals, df = (r−1)(c−1)
- `ht-two-sample-z-means.md` — 2-sample Z on μ₁−μ₂: both σ² known, CI formula
- `ht-two-sample-t-means.md` — 2-sample T: Case 1 pooled (equal σ²) + Case 2 Welch (df formula)
- `ht-paired-t.md` — Paired T: work with differences Dᵢ, df = n−1 (pairs)
- `ht-two-sample-f-variances.md` — F-test on σ₁²/σ₂²: larger variance in numerator, CI on ratio

### New pages created (reference/)
- `ht-tests-overview.md` — All-tests summary table (tests a–j, matching Exam2 quick reference structure) with links to per-test pages, z critical value table, and decision flow

### Formula correction documented
- GoF df discrepancy resolved: Exam2 quick reference listed df = k−1 (special case, p=0). General formula used in class is df = k−1−p where p = parameters estimated from data. Both are correct; k−1 applies only when expected probabilities are fully specified. Documented in `ht-goodness-of-fit.md` and `ht-tests-overview.md`.

### Updated
- `index.md` — added 10 new procedures + 1 new reference; updated page counts and last-updated note

---

## [2026-04-15] ingest | Control chart practice problems + quick reference update

### New files created
- `examples/control-chart-practice.md` — 5 hand-calculated practice problems with full answer walkthroughs:
  - Problem 1: X̄ & R chart limits from x̄̄/R̄ (n=4, A₂/D₃/D₄ given)
  - Problem 2: Process capability Cp and Cpk; demonstrates off-center scenario (Cp > 1 but Cpk < 1)
  - Problem 3: Compute x̄ and R from raw data (n=3), then check Phase II limits
  - Problem 4: p-chart with pooled p̄, σ̂_p, UCL/LCL; demonstrates LCL floor at 0
  - Problem 5: Western Electric Rule 2 (2 of 3 beyond 2σ) — points appear within 3σ limits but pattern signals drift
- `reference/Control_Chart_Practice.docx` — print-ready Word version built by `reference/build_control_practice.py`

### Quick reference updates (from Exam3_Quick_Reference 3.pdf annotations)
- Abbreviations table added at top (SST, SSR, SSE, MSR, MSE, R², σ̂, p)
- R²_adj restated as 1 − (n−1)/(n−p)·(1−R²)
- Common t critical values table removed (annotated as X)
- ANOVA Algebra table added: 5-row 4-col reconstruction guide covering all directions (SSR↔SSE↔MSR↔MSE↔F₀↔R²), plus F₀ from R² formula
- p-value R calls table added (two-sided/upper/lower/F)
- CI back-calculation note added: β̂ = (L+U)/2, se = (U−L)/(2t)
- ρ̂ = ±√R² note added in Correlation section
- X̄ & R Chart Limits subsection added with formulas
- Control chart constants table added (n=2–10, A₂/D₃/D₄/d₂)
- Capability threshold table condensed to inline note; ≥1.0/≥1.33 rows removed
- Attribute charts expanded with UCL/LCL formulas for p, c, u charts

### index.md updated
- control-chart-practice added to Examples table

## [2026-04-14] session-4 | Exam prep + quick reference rebuild + CPS taxonomy design

### New files created
- `examples/anova-table-examples.md` — enriched (2 additions):
  - Abbreviation glossary table for all ANOVA table symbols (df, SS, MS, F₀, SSR, SSE, SST, MSR, MSE, k, n, p, σ̂, R²) with note on p overload
  - 5 practice problems in class-activity format (give SST + individual SSx + SSE → fill full table); answers at end of file
- `knowledge-dimensions.md` (wiki root) — portable CPS taxonomy framework document; domain-agnostic; includes theory citations (Anderson & Krathwohl, Schema Theory, Cognitive Load, Threshold Concepts), implementation blueprint for Obsidian+AI wikis, domain suitability guide
- `reference/quick-reference-section3.md` — updated markdown version of exam quick reference with all PDF annotations applied
- `reference/Exam3_Quick_Reference.docx` — print-ready Word document (Narrow margins, 9pt Calibri); built by build_quick_ref.py
- `reference/build_quick_ref.py` — python-docx script (run with `uvx --from python-docx python build_quick_ref.py`) to regenerate the docx from scratch

### Changes applied to quick reference (from Exam3_Quick_Reference.pdf annotations)
- ANOVA table: expanded to wiki style (F₀ column, SLR/MLR df split, key identities row)
- R output map section: removed entirely
- Summary table section: added (`summary(fit)$coefficients` layout + back-calculation formulas + non-zero null warning)
- t-test table: tightened to 3 rows
- confint() column names table: removed
- Normal probability plot: "S-shape → skewness" removed
- Unusual observations: Outlier and Leverage rows removed; only Cook's D (Influential) remains
- Common t critical values table: added (df 10–∞, α = 0.10/0.05/0.01)
- Control chart section: added (WE rules 1–5, σ_data vs σ_process, PCR vs PCRk with thresholds, p/c/u chart type table)

### Design decisions
- CPS cognitive tier model designed (Construct → Procedure → Script); grounded in Anderson's Knowledge Dimensions + Schema Theory
- Implementation deferred to post-exam; queued in HANDOFF.md; saved to memory
- `knowledge-dimensions.md` placed at wiki root (not in concepts/) — it is meta-documentation about the wiki's design, not a content page
- `build_quick_ref.py` kept in reference/ alongside its outputs; run with uvx (no pip install needed)

### _inbox status
- `Exam3_Quick_Reference.pdf` — processed; quick reference rebuilt as .docx; PDF can be deleted

## [2026-04-14] ingest | Concept checkpoint clippings (L27-28 and L29-30)
- Sources: Stats Notes/_inbox/Assessment Feedback.md (L27-28 checkpoint, 110/120), Assessment Feedback 1+2.md (L29-30 checkpoint, duplicate)
- Enriched concepts/control-charts.md: added Purpose of Control Chart section (missed Q: just-in-time adjustments), k parameter definition, assignable vs chance causes distinction, WE rule triggered meaning, erratic vs pattern interpretation, underlying distributions (P=binomial, U=Poisson), control chart constants role table (A₂/D₃/D₄/C₄), S chart constants table
- Enriched concepts/process-capability.md: added natural tolerance limits (μ±3σ), fraction defective (fallout) calculation with correct standardization formula + worked example, tolerance chart definition, PCR overstates capability when off-center note
- Enriched examples/control-chart-examples.md: added fallout calculation worked example (with common trap about formula), concept checkpoint Q&A table (exam-style questions + answers)
- Deleted source files after ingest

## [2026-04-14] exam-prep | Test 3 prep session — ingest Test 3 Prep.docx + build exam-critical pages
- Source ingested: _inbox/Test 3 Prep.docx — defines what IS and is NOT on Test 3
- Key insight: R code writing NOT tested; regression section = output interpretation + table completion only
- Created examples/anova-table-examples.md: 4 worked examples — SLR ANOVA table completion, MLR ANOVA table completion, summary table completion (recover missing t/SE/Estimate), recommendations from output; master relationship quick-reference table
- Created examples/control-chart-examples.md: 6 worked examples — WE rules application, reading qcc output, Cp/Cpk from process.capability() output, by-hand Cp/Cpk calculation, σ̂ from R chart output, p-chart conclusion phrasing; chart characteristics quick-reference; control limits vs spec limits distinction; NOT R-code-focused
- Enriched concepts/model-adequacy.md: added diagnostic plot guide (4 plots from plot(fit), what each pattern means), "Necessary/Sufficient/Definitive" section (R², F-test, t-tests, residual plots hierarchy), Interpolation vs Extrapolation section
- Updated index.md and log.md

## [2026-04-13] next-session | Tasks queued for next session
- [ ] Finish handoff system: update Stats Notes/CLAUDE.md with HANDOFF.md workflow + unannotated-drop handling; create root-level CLAUDE.md; update Section_3/Drills/CLAUDE.md and Section1&2/CLAUDE.md to point to wiki and HANDOFF.md
- [ ] Enrich concept pages from _slide_text/ (L27-29 → control-charts, L31 → regression-slr, L32-33 → regression-mlr, L34-35 → regression-ht, L40-41 → correlation-transformations)
- [ ] Build control-chart-examples.md from ControlCharts_Homework.R
- [ ] Section 1&2 ingest — wait for Warren confirmation before starting

## [2026-04-13] create | Core Concepts section — standard-error, degrees-of-freedom, variance-estimation
- Added Core Concepts section to index.md (above Section 1-2 concepts)
- Created concepts/standard-error.md: all SE formulas — one/two-sample means, proportions, SLR/MLR regression coefficients, CI/PI SE formulas; explains why PI is wider than CI
- Created concepts/degrees-of-freedom.md: all df formulas — one-sample t/chi-square (n-1), pooled t (n₁+n₂-2), Welch ν, paired t, F, chi-square GoF/independence, SLR/MLR ANOVA table; R critical value functions
- Created concepts/variance-estimation.md: s², pooled s², MSE, control chart σ̂ (R̄/d₂, s̄/c₄); how variance estimation flows through to SE and CI; back-calculating σ from CI bounds

## [2026-04-13] ingest | Section 3 slide text extraction + L36-37 & L38-39 homework examples
- Extracted Section 3 lecture slide text: 11 PDFs → .txt files in Stats Notes/_slide_text/ (using pymupdf via uv)
  - L27P SPC, L28P X̄/R, L29P More Charts, L30E Fraction Defective, L31P SLR, L32&33P MLR, L34&35P HT in Regression, L36&37E Model Building, L36&37P CI in Regression, L38&39P Model Adequacy, L40&41P Correlation & Transformations
- Ingested all 6 L36-37 Applied HW Rmd files (CI/PI in regression) and L38-39 Applied HW Q1 (model adequacy)
- Created examples/regression-ci-examples.md: 6 worked problems (SLR & MLR) covering confint(), predict(interval="confidence"), predict(interval="prediction"); column name trap table; common mistakes
- Created examples/model-adequacy-examples.md: QB rating SLR example; R²; QQ plot; Shapiro-Wilk; residuals vs fitted; Cook's D; teacher-language answer templates
- Updated index.md and log.md

## [2026-04-13] ingest | Formula PNGs (82), Section 3 study guides, R project files
- Sources ingested: all 82 formula PNGs from Section1&2/Slides/Formula Snippets/ (Exam1 + main folders), Section3_Study_Guide.Rmd, L34-35_Study_Sheet.Rmd, L36-37_Study_Guide.Rmd, L38-39_App_HWQ1.Rmd, L36-37_App_HWQ1.Rmd, Control Charts.R, ControlCharts_Homework.R, Process Capability.R, Attribute Chart.R
- Pages created (concepts/): probability.md, distributions.md, confidence-intervals.md, hypothesis-testing-overview.md, which-test.md, two-sample-tests.md, chi-square.md, proportions.md, regression-slr.md, regression-mlr.md, regression-ht.md, regression-ci.md, model-adequacy.md, correlation-transformations.md, control-charts.md, process-capability.md
- Pages created (r-code/): summary-stats-r.md, hypothesis-tests-r.md, regression-r.md, control-charts-r.md, reading-r-output.md
- Pages created (reference/): formula-sheet.md, which-test-flowchart.md
- Not yet ingested: Section1&2 lecture slides (PDFs — poppler not available), homework examples (Homework1_Ross, Drill HW4), ANOVA concept page
- Next: ingest homework Rmd files for examples/ pages; add anova.md concept page

## [2026-04-13] bootstrap | Wiki infrastructure created
- Created: CLAUDE.md (wiki schema), index.md (catalog), log.md (this file)
- Directory structure defined: concepts/, examples/, r-code/, reference/
- Page templates defined in CLAUDE.md
- Teacher-language convention table established
- No source files ingested yet — all index entries are stubs pending ingest
- Next: Ingest formula PNGs → populate concepts/ pages and reference/formula-sheet.md

---

## [2026-04-22] ingest | Section 4 — Experimental Design (Lessons 42–50)

### Source files read
- `L42&43P CR Single Factor Experiments.pdf` — 14 slides; CRD model, ANOVA table, SS identity, CI formulas (13.8/13.9), unbalanced SS (13.10), Fisher LSD (13.11), model adequacy residuals
- `L44&45P Random Effect Model and Blocking.pdf` — 12 slides; random effects model, variance components (13.16–13.20), RCBD definition, ANOVA identity, ANOVA table (13.10), fabric strength example
- `L46&47P Factorial Experiments.pdf` — 13 slides; factorial definition, interaction plots, 2-factor model (14.1/14.4), primer paint example (Tables 14.5–14.6), 3-factor model (14.5/14.8), surface roughness example (Tables 14.9–14.10)
- `L48-50P 2kFD.pdf` — 20 slides; ±1 coding, sign tables, contrasts/effects/SS formulas, df summary, epitaxial layer 2^2 example (Table 14.12), lm() vs aov(), R vs Minitab (β̂=Effect/2), Daniel plot, sparsity of effects
- `CRD.R`, `RCBD.R` — template patterns; `%$%` pipe, melt(), ncol/nrow for a/n, block label creation
- `L42-43_App_HWK_Q1.R` — balanced CRD (rodding level vs concrete strength); scalar extraction pattern
- `L42-43_App_HWK_Q2.R` — unbalanced CRD (carbon material vs roughness); col_names=FALSE, filter(!is.na()), tapply() CI traps
- `1-TwoFactor.R` through `6-2kFD 5Factor.R` — gather()/mutate_if()/mutate_at() patterns, DanielPlot(), 4-model hierarchy

### New pages created (12)
- `concepts/crd-one-way-anova.md` — CRD model, ANOVA table, CI, LSD, residual diagnostics
- `concepts/rcbd-blocking.md` — RCBD model, blocking rationale, df_error=(a−1)(b−1), variance components
- `concepts/factorial-anova.md` — 2/3-factor factorial, interaction plots, ANOVA df tables
- `concepts/2k-factorial-design.md` — ±1 coding, effects, SS, Daniel plot, lm() vs aov(), R vs Minitab
- `concepts/random-effects-model.md` — fixed vs random, variance component estimation
- `r-code/anova-r.md` — CRD/RCBD templates, scalar extraction, %$% pipe, melt() vs gather()
- `r-code/factorial-anova-r.md` — 2-6 factor R patterns, DanielPlot(), mutate_if vs mutate_at
- `examples/crd-examples.md` — Q1 balanced CRD, Q2 unbalanced CRD (3 exam traps)
- `examples/factorial-examples.md` — primer paint 2-factor, surface roughness 3-factor, table completion practice
- `examples/2k-factorial-examples.md` — epitaxial layer 2^2 (manual + R), unreplicated 2^3 Daniel plot
- `reference/anova-design-guide.md` — design decision table, df by design, LSD/CI formulas, key distinctions
- `reference/quick-reference-section4.md` — compact formula sheet, R cheat sheet, reshape idioms, teacher phrasings

### Pages updated (4)
- `concepts/which-test.md` — added Step 2d (CRD/RCBD branch) and Step 2e (factorial/2^k branch) + ANOVA rows in Quick Summary Table
- `reference/formula-sheet.md` — added Section 4 block (ANOVA tables, Fisher LSD, CI, 2^k formulas, variance components, distinctions table)
- `index.md` — added Section 4 block with 12 new pages, updated last-updated line
- `log.md` — this entry

---

## [2026-04-22] implement | CPS Cognitive Tier Model — wiki-wide retrofit

### Changes made

**Frontmatter update — `tier:` field added to 39 content pages:**
- 5 pages → `tier: construct` (standard-error, degrees-of-freedom, variance-estimation, distributions, probability)
- 19 pages → `tier: procedure` (all remaining concept pages)
- 15 pages → `tier: script` (all examples/ and r-code/ pages)
- 5 reference pages — no tier field (formula-sheet, which-test-flowchart, quick-reference-section3, anova-design-guide, quick-reference-section4)

**New page created:**
- `concepts/taxonomy.md` — study-focused CPS page mapping (all 39 pages classified with rationale and trigger scenarios)

**CLAUDE.md updated:**
- `tier:` line added to concept, example, and r-code page templates
- "CPS Cognitive Tier Model (implementation pending)" section replaced with full CPS Cognitive Tiers section
- Section Coverage Map updated to show all three sections as "Complete"

**index.md reorganized:**
- Navigation pointer to [[taxonomy]] added at top
- "Core Concepts" and flat section lists replaced with Tier 1 / Tier 2 / Tier 3 subsections within each section
- All 39 content pages present; taxonomy and knowledge-dimensions added to Meta / Wiki Design section

**HANDOFF.md:**
- `[deferred] CPS cognitive tier model` entry marked `[done]`

## [2026-04-22] enrich | anova-r.md — random effects extraction, variance components, Blom normal probability plot
- **Page updated:** `r-code/anova-r.md`
- **Content added:**
  - Named-row extraction pattern (`aov_tbl["Batch", "Mean Sq"]`) vs. positional extraction — when to use each
  - Variance component calculation block: σ̂², σ̂²_τ, proportion of variability with `sprintf` print pattern
  - Use-case note: do not call `LSD.test()` on random effects models; report components instead
  - Blom plotting-positions normal probability plot (ggplot, probability on Y): full code block sourced from L44-45_App_HWK_Q1.R
  - Three-way comparison table: Blom vs. `stat_qq` vs. `model %>% plot()` — axes, context, when to use each
  - "When to Use" section updated to include random effects case

## [2026-04-22] enrich | Random effects model — hypothesis interpretation, proportion of variability, blocks comparison
- **Pages updated:** `concepts/random-effects-model.md`, `reference/quick-reference-section4.md`
- **Content added:**
  - Teacher-language phrasing table for rejecting / failing to reject H₀: σ²_τ = 0 (random effects framing, distinct from fixed-effects phrasing)
  - Proportion of variability formula: σ̂²_τ / (σ̂²_τ + σ̂²), with worked example from Box & Tiao batch yield data (41.9% between-batch)
  - Random Effects vs. Blocks comparison table: same math, different intent — blocks control away nuisance, random effects quantify it
  - Exam angle note: identify random vs. fixed effects by whether levels were randomly selected from a larger pool
  - Quick-reference Section 4 teacher phrasings extended with three new rows for random effects conclusions and model identification

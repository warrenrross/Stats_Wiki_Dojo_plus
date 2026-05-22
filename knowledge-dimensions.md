# Knowledge Dimensions: A Taxonomy for Technical Learning Wikis

> **What this document is:** A portable framework for organizing a wiki or knowledge base around any technical or STEM subject. It defines a three-tier taxonomy grounded in cognitive science, explains the structural decisions behind it, and gives an implementation blueprint for Obsidian-based wikis with an AI agent maintaining the content.

---

## The Problem This Solves

When you build a reference wiki for a technical subject, content naturally falls into different kinds of knowledge — but most wiki structures don't distinguish between them. A page defining what standard error *is* feels fundamentally different from a page explaining *how to run a t-test*, which feels different from a page walking through *how to fill in a partial ANOVA table*. These are not just different topics; they are different *types* of knowledge that require different study strategies.

Without an explicit taxonomy:
- Studying feels undifferentiated — you don't know whether you're trying to memorize a definition, learn a decision process, or practice a procedure
- Wiki pages get written at inconsistent levels of abstraction
- An AI agent maintaining the wiki may create redundant or misclassified pages

The **CPS Framework** (Construct → Procedure → Script) solves this by classifying every page by *structural type*, not topic or difficulty.

---

## The CPS Framework

### Tier 1 — Construct

> *"A mathematical quantity or foundational principle whose formula changes shape depending on context, but whose meaning stays fixed."*

**Characteristics:**
- Appears inside multiple Procedures — it is a building block, not a technique
- Has no "steps to follow"; understanding it means recognizing which variant applies in a given context
- Parametrically variable: the formula has slots that get filled differently depending on what you're estimating, how many groups, whether a parameter is known, etc.
- Often the thing that connects otherwise-unrelated topics: once you see that standard error is always "the SD of a sampling distribution," you stop memorizing five separate formulas

**Study cue:** "This will appear inside several Procedures. Understand the concept well enough to derive the right variant, not just recall one formula."

**Examples across domains:**

| Domain | Construct examples |
|--------|--------------------|
| Statistics | Standard error, degrees of freedom, variance estimation, probability distributions |
| Physics | Energy, force, field, potential |
| Economics | Elasticity, marginal cost, present value |
| Chemistry | Equilibrium constant, enthalpy, reaction rate |

---

### Tier 2 — Procedure

> *"An inferential technique or analytical method that assembles 2+ Constructs to achieve a specific goal, and requires judgment about which variant to apply."*

**Characteristics:**
- Has a defined purpose (test a claim, fit a model, build an interval, detect a shift)
- Requires conditional reasoning: *which* test? *which* distribution? Is a parameter known?
- The key question for this tier: "When do I use this, and what does it depend on?"
- Understanding a Procedure means being able to select it correctly from a decision tree *and* execute it

**Study cue:** "Know when to use it, which Constructs it calls, and what the output means."

**Examples across domains:**

| Domain | Procedure examples |
|--------|--------------------|
| Statistics | Hypothesis testing, confidence intervals, regression, chi-square test, control charting |
| Physics | Applying Newton's second law, circuit analysis, thermodynamic cycle analysis |
| Economics | Supply/demand equilibrium, NPV analysis, market structure classification |
| Chemistry | Titration calculation, equilibrium problem-solving, stoichiometry |

---

### Tier 3 — Script

> *"A fixed-sequence workflow for a recurring task where all decisions have already been made — errors come from execution, not from not knowing what to do."*

**Characteristics:**
- Triggered by a specific recognizable context ("I have a partial ANOVA table", "I need to check residual plots")
- Deterministic: no branching decisions once the script has been selected; the steps are fixed
- The goal is automaticity — you want to execute without using working memory to figure out what comes next
- Scripts are usually learned through worked examples and repetition

**Study cue:** "Practice until the sequence is automatic. Know which Script each exam scenario triggers."

**Examples across domains:**

| Domain | Script examples |
|--------|--------------------|
| Statistics | Fill in a partial ANOVA table, interpret residual diagnostic plots, read R regression output |
| Physics | Free-body diagram procedure, significant-figures rules in a calculation chain |
| Economics | Calculate consumer/producer surplus from a graph, draw a market shift |
| Chemistry | Limiting reagent calculation, pH from Ka |

---

## Why This Model, Not Others

Several established frameworks were considered and rejected for this specific use case:

| Framework | What it measures | Why it's wrong here |
|-----------|-----------------|---------------------|
| **Bloom's Taxonomy** | Cognitive difficulty (remember → create) | Treats standard error as "easier" than SLR — but they're structurally different, not difficulty-ordered |
| **SOLO Taxonomy** | Quality of a student's response on a task | Describes *how well* you answer, not *what type of thing* you're learning |
| **Gagne's Learning Hierarchy** | Prerequisite sequencing for instruction design | Designed to order *teaching*, not to classify *reference material* |
| **Skemp's Relational/Instrumental** | Depth of understanding (know why vs. know how) | Binary, not three-level; applies to how well you know something, not what kind of thing it is |
| **Threshold Concepts** | Whether a concept is transformative and irreversible | Identifies which Constructs are most important, but doesn't produce a complete taxonomy |

**CPS is appropriate because:**
- It classifies knowledge by *structure* rather than *difficulty* or *quality*
- The three tiers map directly onto three different study strategies (understand → decide → automate)
- It's stable: a Construct doesn't become a Procedure because you've studied it longer
- It's exhaustive for technical domains: every page in a STEM wiki fits one of these three categories

---

## Theoretical Sources

### Primary: Anderson & Krathwohl's Revised Bloom — Knowledge Dimension (2001)

The revised Bloom's taxonomy has two axes: cognitive process (the familiar remember/understand/apply/...) and **knowledge type**. The knowledge type axis is:
- **Factual** — isolated facts and terminology
- **Conceptual** — relationships, categories, principles (→ Construct)
- **Procedural** — how to do something; criteria for when to use which method (→ Procedure + Script combined)
- **Metacognitive** — awareness of one's own cognition

CPS separates Anderson's "Procedural" dimension into two tiers (Procedure vs. Script) because the distinction between "requires judgment" and "has collapsed decisions" is practically significant for study design and page-writing.

*Source:* Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). *A taxonomy for learning, teaching, and assessing: A revision of Bloom's educational objectives.* Longman.

---

### Supporting: Schema Theory (Bartlett 1932; Rumelhart 1980)

A **schema** is a structured, organized cluster of knowledge in long-term memory. New information is learned by integrating it into existing schemas (assimilation) or by restructuring schemas (accommodation).

The three CPS tiers correspond to three kinds of schemas:
- **Constructs** = primitive schemas — small, reusable knowledge structures that get instantiated with context-specific values (like a template with fill-in slots)
- **Procedures** = compound schemas — configurations that wire together several primitive schemas toward a goal; include conditional branches
- **Scripts** = procedural scripts — ordered action sequences for recurring, well-defined situations (Schank & Abelson's "script" concept, 1977)

This explains why Constructs *must be understood before* Procedures can be mastered: if the primitive schema is weak, the compound schema that depends on it will be unstable under novel conditions.

*Sources:*
- Bartlett, F. C. (1932). *Remembering.* Cambridge University Press.
- Rumelhart, D. E. (1980). Schemata: The building blocks of cognition. In R. J. Spiro et al. (Eds.), *Theoretical issues in reading comprehension.*
- Schank, R. C., & Abelson, R. P. (1977). *Scripts, plans, goals, and understanding.* Erlbaum.

---

### Supporting: Cognitive Load Theory (Sweller 1988, 1994)

Cognitive load theory distinguishes:
- **Intrinsic load** — inherent complexity of the material
- **Extraneous load** — unnecessary cognitive effort from poor presentation
- **Germane load** — effort that builds schemas (this is what you want)

The CPS hierarchy reduces cognitive load during exam performance: Constructs need to be recognized automatically (no working memory spent deriving them); Procedures need the decision logic internalized (no working memory spent choosing); Scripts need to run automatically (no working memory spent sequencing). The wiki structure supports this by writing each tier at the appropriate level of abstraction.

*Source:* Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257–285.

---

### Supporting: Threshold Concepts (Meyer & Land 2003)

A threshold concept is one that is *transformative* (changes how you see the field), *irreversible* (you can't un-understand it), *integrative* (connects previously disconnected ideas), and *troublesome* (counter-intuitive or alien). These are the most important Constructs — the ones that, once genuinely understood, unlock multiple Procedures simultaneously.

In statistics: the sampling distribution (→ standard error, p-value, CI all make sense); in physics: the field concept; in economics: opportunity cost.

Wiki implication: Tier 1 pages for threshold concepts should receive the most investment in plain-English explanation and motivation. The "In Plain English" section is doing the heavy lifting that multiple Procedure pages will depend on.

*Source:* Meyer, J. H. F., & Land, R. (2003). Threshold concepts and troublesome knowledge. In C. Rust (Ed.), *Improving student learning — Ten years on.* OCSLD.

---

## Implementation Blueprint for Obsidian + AI Agent

### Frontmatter Schema

Every content page carries a `tier:` field. The allowed values are `construct`, `procedure`, `script`, and `reference` (for cross-tier navigation aids).

```yaml
---
tags: [concept, section-name]
tier: construct        # construct | procedure | script | reference
sources: [source-1, source-2]
---
```

### Directory Structure

```
wiki-root/
├── CLAUDE.md              # Agent schema (includes CPS definitions)
├── index.md               # Page catalog, grouped by tier within section
├── log.md                 # Append-only ingest log
├── HANDOFF.md             # Processing queue between sessions
│
├── concepts/              # Tier 1 (Constructs) and Tier 2 (Procedures)
├── examples/              # Tier 3 (Scripts — worked problems)
├── r-code/                # Tier 3 (Scripts — tool/code workflows)
└── reference/             # Untiered — cross-tier navigation aids
```

Note: Constructs and Procedures share `concepts/` because the distinction is captured in the `tier:` field, not the folder. This keeps the directory flat and avoids over-engineering the structure.

### Page Templates by Tier

**Tier 1 — Construct page:**

```markdown
---
tags: [concept, ...]
tier: construct
sources: [...]
---
# Concept Name

## In Plain English
One paragraph: what this quantity *is*, not how to compute it. Answer: "Why does this exist?"

## How the Formula Changes Shape
Table showing all variants with context conditions:
| Context | Formula | When |
|---------|---------|------|

## The Constant Core
What stays the same across all variants. This is what to memorize.

## Common Mistakes
Confusions, wrong formula in wrong context, etc.

## Related
- [[procedure-that-uses-this]]
```

**Tier 2 — Procedure page:**

```markdown
---
tags: [concept, ...]
tier: procedure
sources: [...]
---
# Procedure Name

## In Plain English
What inferential goal this achieves.

## When To Use
- Condition 1
- Condition 2 (decision criteria vs. alternatives)

## Constructs This Uses
- [[construct-1]] — role it plays here
- [[construct-2]] — role it plays here

## Steps
1. ...
2. ...

## Key Assumptions
## Common Mistakes
## Related
```

**Tier 3 — Script page (example/worked problem):**

```markdown
---
tags: [example, ...]
tier: script
sources: [...]
---
# Script Name / Example Title

## Trigger
"Use this script when you see: ..."

## Fixed Sequence
1. Step 1 — what to do and why
2. Step 2 — ...

## Worked Example
...

## Answer Template
State the conclusion in the domain's expected phrasing.
```

### CLAUDE.md Section to Add

Add this section to the agent schema file so any AI agent can correctly classify new pages:

```markdown
## CPS Cognitive Tiers

Every concept and example page carries a `tier:` frontmatter field. Assign as follows:

- **construct** — a mathematical quantity or foundational principle with context-variable formula
  variants. No decision logic, no steps. Examples: standard error, degrees of freedom, energy.
  Ask: "Does this concept appear as a building block inside multiple other techniques?" If yes: construct.

- **procedure** — an analytical technique that assembles 2+ constructs to achieve a specific goal,
  and requires judgment about which variant to apply. Examples: t-test, regression, NPV analysis.
  Ask: "Does learning this require knowing *when* to use it and *which* construct variant to apply?" If yes: procedure.

- **script** — a fixed-sequence exam/task workflow where decisions are already collapsed.
  Examples: filling a partial ANOVA table, drawing a free-body diagram, running a titration calculation.
  Ask: "Is the whole task learnable by practicing the sequence until it's automatic?" If yes: script.

- **reference** — cross-tier navigation aids (formula sheets, decision flowcharts, index pages).
  These span multiple tiers and should not be classified into any one tier.
```

### Index Organization

The `index.md` should group pages by tier within each subject section:

```markdown
## Subject Section Name

### Tier 1 — Constructs
- [[construct-1]] — one-line description
- [[construct-2]] — one-line description

### Tier 2 — Procedures
- [[procedure-1]] — one-line description
- [[procedure-2]] — one-line description

### Tier 3 — Scripts
- [[script-examples-1]] — one-line description
```

---

## Domain Suitability

This model works well for any domain where:

1. **Some concepts are genuinely cross-cutting** — they appear in multiple methods with variant formulas (standard error in statistics; force in physics; opportunity cost in economics)
2. **Techniques have decision preconditions** — you must know *when* to apply them, not just *how*
3. **Exam or task performance requires automated workflows** — there are recurring task types that benefit from scripted practice

It works less well for:
- Purely narrative subjects (history, literature) where knowledge is mostly declarative and context-dependent rather than procedural
- Early introductory material where everything is new vocabulary and the distinctions between tiers aren't yet visible
- Research wikis where the goal is synthesis rather than mastery of established techniques

---

## Applied Example: Statistics Wiki (INEG)

| Page | Tier | Rationale |
|------|------|-----------|
| `standard-error` | Construct | Appears in CI, HT, regression, control charts — same concept, different formula slot |
| `degrees-of-freedom` | Construct | Appears in every test, CI, and ANOVA row; no standalone procedure |
| `variance-estimation` | Construct | s², MSE, R̄/d₂, s̄/c₄ are one idea with context-specific forms |
| `distributions` | Construct | t, χ², F, normal are called by procedures; not themselves procedures |
| `hypothesis-testing-overview` | Procedure | 7-step method with decision logic (which distribution? one or two tails?) |
| `regression-slr` | Procedure | Model-fitting technique assembling LS, ANOVA, SE, F-test constructs |
| `control-charts` | Procedure | SPC technique; requires judgment about which chart, which constants |
| `which-test` | Procedure | Meta-procedure (decision tree selecting among procedures) |
| `anova-table-examples` | Script | Fixed sequence: compute SSR, fill df, compute MS, compute F₀, state conclusion |
| `model-adequacy-examples` | Script | Fixed diagnostic sequence: R² → QQ → residuals → Cook's D |
| `formula-sheet` | Reference | Spans all tiers; no tier assigned |

---

## Changelog

| Date | Change |
|------|--------|
| 2026-04-14 | Initial framework defined for INEG Stats wiki |

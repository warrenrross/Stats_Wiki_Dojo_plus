# Statistical Methods Wiki + Coding Dojo

*A Living Textbook for University-Level Instruction*

---

## 🎯 Project Vision

This project is a **hybrid learning system**:

* 📖 **Wiki** → conceptual understanding (organized knowledge)
* 🧪 **Coding Dojo** → applied practice (R / Quarto execution)
* 🌐 **Published Site** → accessible teaching resource (GitHub Pages)

It is not a static textbook.
It is a **living, evolving system** that improves through use by instructors and students.

---

## 🧠 Core Philosophy

1. **Knowledge should be structured, not scattered**
2. **Concepts and computation should stay tightly coupled**
3. **Learning should support both linear progression and exploration**
4. **The system should improve over time through real usage**

---

## 🧱 Foundational References

This project is built on two core frameworks:

### 1. Knowledge Structure (CPS Framework)



* **Construct** → foundational ideas (e.g., standard error)
* **Procedure** → methods (e.g., hypothesis testing)
* **Script** → repeatable workflows (e.g., ANOVA table completion)

This defines *how knowledge is organized*.

---

### 2. LLM-Maintained Wiki Architecture



* Persistent, evolving markdown wiki
* LLM integrates sources and maintains structure
* Knowledge compounds over time instead of being re-derived

This defines *how knowledge is maintained and grows*.

---

## 🧭 System Architecture

The project has three tightly connected layers:

### 1. 📚 Wiki (Conceptual Layer)

* Markdown-based knowledge graph
* Organized using CPS taxonomy
* Maintained and expanded continuously
* Supports backlinks and graph navigation

---

### 2. 🧪 Quarto Notebooks (Execution Layer)

* `.qmd` files combining:

  * explanation
  * math
  * R code
* Render to:

  * HTML (for publishing)
  * runnable documents (for local use)

---

### 3. 🌐 Published Site (Presentation Layer)

* GitHub Pages deployment
* Clean, navigable interface
* Entry point for students and instructors

---

## 🔁 Continuous Improvement Workflow

This system is **human-in-the-loop** by design.

### Standard Workflow

1. Instructor uses a lesson (Quarto notebook)
2. Students interact with:

   * concepts
   * code
   * exercises
3. Instructor identifies:

   * unclear explanations
   * missing connections
   * common student mistakes
4. Instructor edits:

   * `.qmd` files (lesson layer)
   * wiki pages (concept layer)
5. LLM:

   * updates cross-links
   * refines summaries
   * integrates new insights

---

### Key Principle

> The resource improves because it is used.

---

## 🔗 Backlinks & Knowledge Graph Design

Backlinking is a **first-class feature**, not an afterthought.

### Goals:

* Connect related ideas across topics
* Reveal conceptual dependencies
* Enable non-linear exploration

---

### Example

* `[[standard-error]]` links to:

  * confidence intervals
  * hypothesis testing
  * regression

* `[[hypothesis-testing]]` links back to:

  * constructs it depends on
  * scripts that implement it

---

### Result

Students can:

* Follow a **linear curriculum**
* Or explore via **graph-based discovery**

---

## 🧭 Learning Modes Supported

### 1. Linear Path (Course Mode)

Suggested progression:

1. Constructs (foundations)
2. Procedures (methods)
3. Scripts (execution)

This supports traditional instruction.

---

### 2. Knowledge Graph (Exploration Mode)

Students can:

* Jump between related ideas
* Follow curiosity-driven paths
* Reinforce connections across topics

---

### 3. Coding Dojo (Practice Mode)

Students:

* Run `.qmd` locally
* Modify code
* Explore variations

---

## 📁 Repository Structure (Suggested)

```
stats-wiki/
│
├── wiki/                  # Core knowledge base (markdown)
│   ├── concepts/
│   ├── procedures/
│   ├── scripts/
│   └── reference/
│
├── lessons/               # Quarto notebooks (.qmd)
│   ├── clt.qmd
│   ├── regression.qmd
│
├── site/                  # Generated HTML (Quarto output)
│
├── _quarto.yml            # Site configuration
├── index.qmd              # Homepage
│
├── HANDOFF.md             # Task queue (LLM workflow)
├── log.md                 # Change history
```

---

## 🧪 Role of Quarto in the System

Quarto acts as the **bridge between theory and practice**:

| Function    | Role                       |
| ----------- | -------------------------- |
| Explanation | Human-readable lesson      |
| Code        | Executable R chunks        |
| Output      | Visualizations and results |
| Export      | HTML for publishing        |

---

### Key Property

> A `.qmd` file is both:

* a lesson
* a runnable lab

---

## 🤖 Role of the LLM

The LLM is not just a helper.
It is a **wiki maintainer and integrator**.

---

### Responsibilities

* Maintain consistency across pages
* Add and update backlinks
* Integrate new knowledge from lessons
* Identify gaps and redundancies
* Suggest improvements

---

### Human vs LLM Roles

| Human              | LLM                |
| ------------------ | ------------------ |
| Teach              | Organize           |
| Curate sources     | Integrate content  |
| Identify confusion | Maintain structure |
| Guide evolution    | Execute updates    |

---

## 🧠 Pedagogical Advantages

### 1. Aligns with Cognitive Science

* CPS structure supports how students actually learn

### 2. Reduces Fragmentation

* Concepts, methods, and execution stay connected

### 3. Encourages Active Learning

* Students run code, not just read results

### 4. Evolves with Teaching Experience

* Captures instructor insights over time

---

## 🚀 Future Extensions

* Interactive Shiny modules inside Quarto
* Auto-generated practice problems
* Dataset libraries for experimentation
* Assessment pipelines linked to scripts
* Multi-language support (Python + R)

---

## 🧩 Guiding Principle

> This is not a textbook you finish.
> It is a system you grow.

---

## 📌 Summary

This project combines:

* 📚 Structured knowledge (CPS wiki)
* 🧪 Executable learning (Quarto notebooks)
* 🤖 Continuous refinement (LLM maintenance)
* 🌐 Public access (GitHub Pages)

Into a single system that functions as:

> **Textbook + Wiki + Lab + Knowledge Graph**

---

---
tags: [concept, unit-1]
tier: construct
sources: [L02P, formula-snippets/Exam1]
---
# Probability

## In Plain English
Probability measures how likely an event is to occur, expressed as a number between 0 and 1. You build a sample space (all possible outcomes), identify your event, and count/calculate its probability using rules.

## When To Use
- You need P(some event) before doing inference
- Setting up a discrete distribution (PMF table)
- Combining events (AND, OR, conditional)

## Core Concepts

### Sample Space & Events
- **Sample space S**: all possible outcomes
- **Event A**: a subset of S
- **Tree diagram**: multiply branch probabilities along a path → P(outcome)

### Rules of Probability
| Rule | Formula |
|------|---------|
| Complement | P(A') = 1 − P(A) |
| Addition (general) | P(A ∪ B) = P(A) + P(B) − P(A ∩ B) |
| Addition (mutually exclusive) | P(A ∪ B) = P(A) + P(B) |
| Multiplication (general) | P(A ∩ B) = P(A) · P(B\|A) |
| Multiplication (independent) | P(A ∩ B) = P(A) · P(B) |
| Conditional | P(B\|A) = P(A ∩ B) / P(A) |

### Independence
Events A and B are **independent** if P(A ∩ B) = P(A) · P(B), equivalently P(B|A) = P(B).

### Counting (Combinatorics)
| Situation | Formula |
|-----------|---------|
| Ordered arrangements of n distinct objects | n! |
| Permutations (choose k from n, ordered) | P(n,k) = n!/(n−k)! |
| Combinations (choose k from n, unordered) | C(n,k) = n!/[k!(n−k)!] |

## Tree Diagram Rule
Multiply probabilities **along** a path to get P(that outcome). Add probabilities **across** paths to get P(event).

## Common Mistakes
- Forgetting to subtract P(A ∩ B) in the addition rule
- Confusing P(A|B) with P(B|A)
- Assuming independence when it hasn't been verified

## Related
- [distributions](distributions.md)
- [hypothesis-testing-overview](hypothesis-testing-overview.md)

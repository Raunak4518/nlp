# 11. Parsing & Grammar

## 1. What this topic is
This module explores syntactic parsing: how we determine the grammatical structure of a sentence. It covers Context-Free Grammars (Constituency Parsing) and word-to-word relationships (Dependency Parsing).

## 2. Why it matters in NLP
"The cop shot the thief with the gun." Did the cop use the gun, or did the thief have the gun? Without a parser to build the syntax tree and resolve structural ambiguity, a computer cannot extract the correct meaning from text.

## 3. What the student will learn
- How to define a CFG (Terminals, Non-Terminals, Rules).
- How to draw a Constituency Parse Tree and bracketed representation.
- The difference between Top-Down (Recursive Descent, Earley) and Bottom-Up (CYK) parsing algorithms.
- The concepts of Head, Dependent, and Root in Dependency Parsing.
- How to read the CoNLL-U format.

## 4. Prerequisites
- [08. POS Tagging & Sequence Labeling](../08-pos-tagging-and-sequence-labeling/README.md)

## 5. Complete subtopic list
- [Context-Free Grammars and Constituency Parsing](cfg-and-constituency.md)
- [Parsing Algorithms](parsing-algorithms.md)
- [Dependency Parsing](dependency-parsing.md)

## 6. Recommended learning order
Read sequentially.

## 7. Mathematical difficulty
★★☆☆☆ (Medium - Writing CFG rules requires logical formalism)

## 8. Implementation difficulty
★★★☆☆ (Medium - We focus on algorithm theory rather than code implementation for CYK/Earley due to their length)

## 9. Numerical-problem relevance
None, but drawing trees is highly relevant.

## 10. Exam importance
**Extremely High**. Every NLP exam features a question where you are given a grammar and a sentence and must draw the resulting parse tree(s).

## 11. Common mistakes
- In a CFG, having a non-terminal that never resolves to a terminal (an infinite loop).
- In Dependency parsing, giving a word multiple heads (a word can have many dependents, but only ONE head).

## 12. Related topics
- [12. TF-IDF & Vector Semantics](../12-tf-idf-and-vector-semantics/README.md)

## 13. Links to every subtopic
(See section 5)

## 14. Revision checklist
- [ ] Understand structural ambiguity ("I shot an elephant in my pajamas").
- [ ] Memorize CYK properties (Bottom-up, Chomsky Normal Form, $O(N^3)$).
- [ ] Understand why Dependency Parsing handles free-word-order languages better than Constituency Parsing.

## 15. Implementation checklist
- [ ] Write a CoNLL-U table for a 5-word sentence.

## 16. Numerical-practice checklist
- [ ] Draw a Constituency tree for a sentence given a toy CFG.

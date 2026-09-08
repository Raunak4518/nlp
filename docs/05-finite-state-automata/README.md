# 05. Finite State Automata

## 1. What this topic is
Finite State Automata (FSA) are the mathematical foundations of text parsing. We study them to understand exactly how regular expressions work under the hood and to prepare for building morphological analyzers in the next module.

## 2. Why it matters in NLP
Every time you run `re.findall` to extract an email, you are invoking a Finite State Automaton. Furthermore, understanding the limitations of an FSA (e.g., they cannot count, so they cannot parse HTML with nested tags) tells you when you must upgrade to a more powerful tool like a Context-Free Grammar.

## 3. What the student will learn
- The formal 5-tuple definition of an FSA.
- How to draw state transition diagrams.
- The difference between Deterministic (DFA) and Nondeterministic (NFA) automata.
- How to implement a DFA and an NFA with epsilon transitions from scratch in Python.

## 4. Prerequisites
- [04. Regular Expressions](../04-regular-expressions/README.md)

## 5. Complete subtopic list
- [Finite State Automata Fundamentals](fsa-fundamentals.md)
- [Deterministic Finite Automata (DFA)](dfa.md)
- [Nondeterministic Finite Automata (NFA)](nfa.md)

## 6. Recommended learning order
Read sequentially.

## 7. Mathematical difficulty
★★☆☆☆ (Medium - Requires understanding formal set notation)

## 8. Implementation difficulty
★★★★☆ (High - The NFA epsilon-closure algorithm is complex)

## 9. Numerical-problem relevance
None, but drawing state diagrams is required.

## 10. Exam importance
**High**. You will definitely be asked to trace a string through an NFA/DFA diagram to determine if it is accepted.

## 11. Common mistakes
- Forgetting that an NFA accepts a string if *any* valid path reaches the final state, even if other paths crash.
- Confusing the Alphabet $\Sigma$ with the set of states $Q$.

## 12. Related topics
- [06. Finite State Transducers & Morphology](../06-finite-state-transducers-and-morphology/README.md)

## 13. Links to every subtopic
(See section 5)

## 14. Revision checklist
- [ ] Memorized the 5-tuple.
- [ ] Understand Kleene's Theorem.

## 15. Implementation checklist
- [ ] Read and understand the NFA epsilon-closure algorithm.

## 16. Numerical-practice checklist
- [ ] Traced a string through an NFA diagram manually.

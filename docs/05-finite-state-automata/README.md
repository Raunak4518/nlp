# 05. Finite State Automata

## 1. Topic Overview
Finite State Automata (FSA) are the mathematical foundations of text parsing. We study them to understand exactly how regular expressions work under the hood, why they execute so fast, and to prepare for building morphological analyzers in the next module.

```mermaid
mindmap
  root((Finite State Automata))
    Fundamentals
      States and Transitions
      The 5-Tuple Definition
      State Diagrams
    DFA (Deterministic)
      One path per input
      O(N) Execution
    NFA (Nondeterministic)
      Multiple paths per input
      Epsilon transitions
      Search & Backtracking
```

## 2. Learning Path
1. [Finite State Automata Fundamentals](fsa-fundamentals.md)
2. [Deterministic Finite Automata (DFA)](dfa.md)
3. [Nondeterministic Finite Automata (NFA)](nfa.md)

## 3. Real-World Applications
- **Regex Engines**: Python's `re` module complies your regex string into an NFA, converts it to a DFA, and runs it on the text.
- **Spell Checkers**: Specialized automata (like Levenshtein automata) are used to quickly find words in a dictionary that are within a certain edit distance of a misspelled word.
- **Lexical Analyzers**: Compilers for programming languages use DFAs to group raw characters into meaningful code tokens.

## 4. Difficulty & Importance
- **Mathematical Difficulty**: ★★☆☆☆ (Medium - Requires understanding formal set notation)
- **Implementation Difficulty**: ★★★★☆ (High - The NFA epsilon-closure algorithm is complex)
- **Exam Importance**: **High**. You will definitely be asked to trace a string through an NFA/DFA diagram to determine if it is accepted, or write the formal 5-tuple for a given diagram.

## 5. Prerequisites
- [04. Regular Expressions](../04-regular-expressions/README.md)

## 6. External Resources
- 📘 **Textbook**: *Speech and Language Processing* (Jurafsky & Martin), Chapter 2.2.
- 🎓 **Visualization Tool**: [FSM Simulator](http://madebyevan.com/fsm/) (Great for drawing and testing automata).

---

### Can You Explain This?
- [ ] I can write the formal 5-tuple definition of an FSA.
- [ ] I can draw a state transition diagram for the regex `ab*c`.
- [ ] I can explain the fundamental difference between a DFA and an NFA.
- [ ] I understand how an NFA handles epsilon ($\epsilon$) transitions.

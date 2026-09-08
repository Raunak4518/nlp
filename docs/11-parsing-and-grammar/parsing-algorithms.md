# Parsing Algorithms

## 1. Top-Down vs Bottom-Up Parsing
Given a mathematical grammar (CFG) and a raw sentence, how do we algorithmically build the syntax tree? There are two directional strategies.

### Top-Down Parsing
Starts at the root node (`S`) and tries to grow the tree downwards, expanding non-terminals until the leaves exactly match the terminal words of the sentence.
- **Pros**: It never explores sub-trees that don't ultimately result in a valid `S`.
- **Cons**: It can waste massive amounts of time exploring rule expansions that don't match the actual words at the bottom. **Crucially, it will infinite-loop** if the grammar has "left-recursive" rules (e.g., `NP -> NP PP`).

### Bottom-Up Parsing
Starts with the terminal words and tries to combine them into larger and larger non-terminals until the entire sequence reduces to a single `S`.
- **Pros**: It never explores trees that don't match the input words. It handles left-recursion safely.
- **Cons**: It can build massive, useless sub-trees that successfully combine words at the bottom but ultimately fail to combine into an `S` at the top.

---

## 2. Recursive-Descent Parsing
Recursive-Descent is a classic, naive **top-down** algorithm. It uses a set of recursive functions (one for each non-terminal).

To parse `S -> NP VP`, the function `parse_S()` will call `parse_NP()`. If successful, it will call `parse_VP()`. If that fails, it backtracks and tries another rule. 

Because of backtracking, it is incredibly slow (exponential time $O(2^N)$ in the worst case) and cannot handle ambiguous NLP grammars efficiently because it recalculates the same failed sub-trees over and over again.

---

## 3. CYK Parsing (Cocke-Younger-Kasami)
The CYK algorithm is a **bottom-up dynamic programming** algorithm. It is arguably the most famous parsing algorithm in computer science.

### Chomsky Normal Form (CNF)
CYK mathematically requires the CFG to be converted into **Chomsky Normal Form**. This means all rules must strictly be one of two types:
1. `A -> B C` (A non-terminal expands to exactly two non-terminals).
2. `A -> "word"` (A non-terminal expands to exactly one terminal).

### How CYK Works
It builds a 2D triangular table (or chart) using dynamic programming (memoization).
1. It fills the bottom row of the table with the POS tags for the individual words.
2. It moves up row by row, looking at pairs of adjacent cells from lower rows to see if any `A -> B C` rule can combine them.
3. If the final top cell of the table contains `S`, the sentence is grammatically valid.

Because it uses a table to store partial results rather than backtracking, it calculates all possible ambiguous parse trees simultaneously in **$O(N^3)$ time**, making it vastly superior to Recursive-Descent.

---

## 4. Earley Parsing
The Earley algorithm is a **top-down dynamic programming** algorithm.

Unlike CYK:
- It **does not** require the grammar to be converted to Chomsky Normal Form.
- It parses left-to-right, maintaining a list of "states" representing partial rule matches (similar to an NFA).
- It operates in $O(N^3)$ time for highly ambiguous NLP grammars, but runs in an incredibly fast $O(N)$ for deterministic grammars (which is why variants of it are often used for compiling programming languages).

---

## 5. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: Compare the CYK algorithm and Recursive-Descent parsing. Why is CYK preferred for Natural Language Processing?
> **Answer**: 
> Recursive-Descent is a Top-Down algorithm that uses naive backtracking. It is susceptible to infinite loops caused by left-recursive grammars (common in English) and has an exponential time complexity $O(2^N)$ because it repeatedly re-calculates the same failed sub-trees.
> 
> CYK is a Bottom-Up algorithm. It is preferred for NLP because natural language is highly ambiguous (yielding many valid trees). CYK uses dynamic programming to store intermediate sub-trees in a table, allowing it to parse all possible ambiguous structures simultaneously in polynomial time $O(N^3)$. However, CYK strictly requires the grammar to be in Chomsky Normal Form.

**2-Mark Question**: What are the strict structural requirements for a Context-Free Grammar to be in Chomsky Normal Form (CNF)?
> **Answer**: Every production rule must either map a non-terminal to exactly two non-terminals (e.g., `A -> B C`) or map a non-terminal to exactly one terminal word (e.g., `A -> "dog"`).

---

### Can You Explain This?
- [ ] I can clearly explain the difference between Top-Down and Bottom-Up parsing.
- [ ] I can write the constraints for Chomsky Normal Form from memory.
- [ ] I can explain what dynamic programming is and how CYK uses it to beat Recursive-Descent.

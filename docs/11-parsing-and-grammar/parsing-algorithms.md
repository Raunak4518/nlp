# Parsing Algorithms

## 1. Top-Down vs Bottom-Up Parsing
Given a CFG and a sentence, how do we algorithmically build the tree?

### Top-Down Parsing
Starts at the root node (`S`) and tries to grow the tree downwards to match the terminal words.
- *Pros*: Never explores trees that don't result in an `S`.
- *Cons*: Can waste massive amounts of time exploring rule expansions that don't match the words at the bottom. Will infinite-loop if the grammar has "left-recursive" rules (e.g., `NP -> NP PP`).

### Bottom-Up Parsing
Starts with the terminal words and tries to combine them into larger non-terminals until reaching `S`.
- *Pros*: Never explores trees that don't match the input words. Handles left-recursion safely.
- *Cons*: Can build massive sub-trees that ultimately fail to combine into an `S`.

## 2. Recursive-Descent Parsing
A classic **top-down** algorithm. It uses a set of recursive functions (one for each non-terminal).
To parse `S -> NP VP`, the function `parse_S()` will call `parse_NP()`. If successful, it will call `parse_VP()`. If that fails, it backtracks and tries another rule. Because of backtracking, it is very slow (exponential time in the worst case) and cannot handle ambiguous grammars efficiently.

## 3. CYK Parsing (Cocke-Younger-Kasami)
The CYK algorithm is a **bottom-up** dynamic programming algorithm. It is arguably the most famous parsing algorithm in computer science.

### Chomsky Normal Form (CNF)
CYK requires the CFG to be in Chomsky Normal Form. This means all rules must strictly be one of two types:
1. `A -> B C` (A non-terminal expands to exactly two non-terminals).
2. `A -> "word"` (A non-terminal expands to exactly one terminal).

### How CYK Works
It builds a 2D triangular table (or chart).
1. It fills the bottom row of the table with the POS tags for the individual words.
2. It moves up row by row, looking at pairs of adjacent cells from lower rows to see if any `A -> B C` rule can combine them.
3. If the top cell of the table contains `S`, the sentence is grammatically valid.

Because it is dynamic programming, it calculates all possible parse trees simultaneously in **$O(N^3)$ time**, making it vastly superior to Recursive-Descent.

## 4. Earley Parsing
The Earley algorithm is a **top-down** dynamic programming algorithm.
Unlike CYK:
- It **does not** require the grammar to be converted to Chomsky Normal Form.
- It parses left-to-right, maintaining a list of "states" representing partial rule matches.
- It operates in $O(N^3)$ time for ambiguous grammars, but is incredibly fast $O(N)$ for deterministic grammars (like programming languages).

## 5. Exam Preparation
### Must Memorize
- CYK is Bottom-Up, requires Chomsky Normal Form, and runs in $O(n^3)$.
- Recursive Descent is Top-Down, uses backtracking, and is susceptible to infinite loops from left-recursion.

### Likely Theory Question
**Question**: Why is CYK parsing preferred over naive Recursive-Descent for natural language processing?
**Answer**: Natural language is highly ambiguous, meaning a sentence can have many valid parse trees. Naive recursive-descent parsing with backtracking has an exponential time complexity $O(2^N)$ in the worst case and re-calculates the same sub-trees repeatedly. CYK uses dynamic programming (memoization) to store sub-trees in a table, parsing all possible ambiguous structures simultaneously in polynomial time $O(N^3)$.

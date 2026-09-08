# Regex Applications & Automata

## 1. Information Extraction with Regex
Before the advent of Deep Learning, regex was the sole tool for Named Entity Recognition (NER). Today, it is still the standard, highly efficient tool for extracting structured patterns from unstructured text before passing the text to an ML model.

### Regex for Email Extraction
An email generally consists of an alphanumeric local part, an `@` symbol, and an alphanumeric domain part with a dot.
- **Regex**: `[\w.-]+@[\w.-]+\.\w+`
- **Explanation**: 
  - `[\w.-]+` matches one or more word characters, dots, or hyphens. 
  - `@` matches the literal at-symbol. 
  - `\.\w+` matches the dot and the Top Level Domain (like .com).

### Regex for URL Extraction
- **Regex**: `https?://[a-zA-Z0-9./-]+`
- **Explanation**: 
  - `https?` matches "http" or "https" (the `s` is optional). 
  - `://` matches the literal protocol separator. 
  - `[a-zA-Z0-9./-]+` matches the domain and routing path.

### Regex for Phone Numbers (US Format)
Matches formats like `123-456-7890` or `(123) 456-7890`.
- **Regex**: `\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}`
- **Explanation**: 
  - `\(?` matches an optional left parenthesis. 
  - `\d{3}` matches exactly 3 digits. 
  - `[-.\s]?` matches an optional separator (hyphen, dot, or space).

---

## 2. Regular Expressions and Finite Automata
There is a strict, mathematical equivalency between Regular Expressions and Finite State Automata (FSA).

### Kleene's Theorem (The Equivalency)
Any formal language (a set of strings) that can be described by a Regular Expression can be perfectly recognized by a Finite Automaton. Conversely, any language recognized by an FSA can be described by a Regex.

### Why This Matters in NLP
When you run `re.search()` in Python, the regex engine does not execute the raw string of symbols directly. Doing so would require backtracking logic that could run in exponential time $O(2^N)$, causing server crashes (a phenomenon known as Regex Denial of Service or ReDoS). 

Instead, professional regex engines perform a mathematical translation:
1. The regex engine **compiles** the regex string into a Nondeterministic Finite Automaton (NFA).
2. It mathematically translates the NFA into a Deterministic Finite Automaton (DFA) using the subset construction algorithm.
3. It minimizes the DFA to use the fewest possible states.
4. It feeds the input string through the optimized state machine.

This compilation guarantees that searching text with regex is extremely fast—executing in strict linear time $O(N)$ relative to the length of the document.

```mermaid
flowchart LR
    A["Regex: 'ab*c'"] -->|Thompson's Construction| B(NFA)
    B -->|Subset Construction| C(DFA)
    C -->|Hopcroft's Algorithm| D(Minimized DFA)
    D -->|O(N) Execution| E[Match Result]
    
    style D fill:#e8f5e9,stroke:#388e3c
```

We will explore the exact mechanics of Finite State Automata in the next module.

---

## 3. Exam Preparation

### How to Write This in an Exam

**10-Mark Question**: Write a Python script using `re.findall` to extract all prices in a document. Prices are formatted as a dollar sign followed by digits, an optional comma separating thousands, and optionally a decimal with exactly two digits (e.g., `$5`, `$100`, `$1,000.50`).
> **Answer**:
> ```python
> import re
> text = "I bought an apple for $5 and a car for $1,000.50."
> # Regex breakdown:
> # \$          : Literal dollar sign
> # \d+         : One or more digits
> # (?:,\d+)*   : Zero or more groups of a comma followed by digits. 
> #               We use (?:...) for a non-capturing group.
> # (?:\.\d{2})?: Optional non-capturing group for the decimal and 2 digits.
> prices = re.findall(r'\$\d+(?:,\d+)*(?:\.\d{2})?', text)
> print(prices)
> ```
> *(Note: `(?:...)` is a non-capturing group. If you use standard capturing groups `(...)` with `findall`, `findall` assumes you ONLY want the contents of the capturing groups, and will not return the full match. Using `(?:)` forces it to return the whole price).*

**2-Mark Question**: State Kleene's Theorem as it relates to Regular Expressions.
> **Answer**: Kleene's Theorem states that a language is regular if and only if it can be accepted by a finite automaton. Therefore, every Regular Expression has an equivalent Deterministic Finite Automaton (DFA) that can compute it.

---

### Can You Explain This?
- [ ] I can write a regex to extract standard emails.
- [ ] I can write a regex to extract standard URLs.
- [ ] I can state Kleene's Theorem.
- [ ] I can explain the compilation pipeline that allows Python to execute regex in linear time $O(N)$.
- [ ] I know why we must use non-capturing groups `(?:...)` when using `re.findall()`.

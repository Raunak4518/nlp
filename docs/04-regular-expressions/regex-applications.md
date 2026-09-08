# Regex Applications & Automata

## 1. Information Extraction with Regex
Regex is the standard tool for extracting structured patterns from unstructured text before passing the text to an ML model.

### Regex for Email Extraction
An email generally consists of an alphanumeric local part, an `@` symbol, and an alphanumeric domain part with a dot.
- Simple Regex: `[\w.-]+@[\w.-]+\.\w+`
- *Explanation*: `[\w.-]+` matches one or more word characters, dots, or hyphens. `@` matches the literal at-symbol. `\.\w+` matches the dot and the Top Level Domain (like .com).

### Regex for URL Extraction
- Simple Regex: `https?://[a-zA-Z0-9./-]+`
- *Explanation*: `https?` matches "http" or "https" (because the `s` is optional). `://` matches the literal. `[a-zA-Z0-9./-]+` matches the domain and path.

### Regex for Phone Numbers (US Format)
Matches formats like 123-456-7890 or (123) 456-7890.
- Regex: `\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}`
- *Explanation*: `\(?` matches an optional left parenthesis. `\d{3}` matches exactly 3 digits. `[-.\s]?` matches an optional separator.

## 2. Regex for Sentence Boundaries
As discussed in Tokenization, finding sentence boundaries can sometimes be handled by Regex if we assume standard punctuation rules (ignoring the abbreviation edge cases).

- Regex to find sentences: `[^.!?]+[.!?]`
- *Explanation*: `[^.!?]+` matches a sequence of one or more characters that are NOT sentence-ending punctuation. `[.!?]` matches the final punctuation mark.

## 3. Regular Expressions and Finite Automata
There is a strict, mathematical equivalency between Regular Expressions and Finite State Automata (FSA).

### The Equivalency Theorem (Kleene's Theorem)
Any language (set of strings) that can be described by a Regular Expression can be recognized by a Deterministic Finite Automaton (DFA) or Nondeterministic Finite Automaton (NFA). Conversely, any language recognized by an FSA can be described by a Regex.

### Why this matters in NLP
When you run `re.search()` in Python, the regex engine does not execute the string of symbols directly. Instead:
1. The regex engine **compiles** the regex string into an NFA.
2. It translates the NFA into a DFA.
3. It minimizes the DFA.
4. It feeds the input string through the state machine.

This guarantees that searching text with regex is extremely fast (linear time $O(N)$ relative to the length of the string, once the DFA is built).

We will explore Finite State Automata deeply in the next module.

## 4. Exam Preparation
### Must Memorize
- Kleene's Theorem: The 1-to-1 relationship between Regex and Finite Automata.

### Likely Practical Question
**Question**: Write a python script using `re.findall` to extract all prices in a document. Prices are formatted as a dollar sign followed by digits, an optional comma, and optionally a decimal with two digits (e.g., $5, $100, $1,000.50).
**Answer**:
```python
import re
text = "I bought an apple for $5 and a car for $1,000.50."
prices = re.findall(r'\$\d+(?:,\d+)*(?:\.\d{2})?', text)
print(prices)
```
*(Note: `(?:...)` is a non-capturing group. If you use standard capturing groups with `findall`, it only returns the captured groups, not the whole match).*

# 04. Regular Expressions

## 1. What this topic is
This module covers Regular Expressions (Regex), a specialized mini-language used universally in computer science to define and search for string patterns.

## 2. Why it matters in NLP
Before text can be tokenized or fed into a neural network, it must be cleaned. Regex is the primary tool used for text cleaning, data extraction (finding emails/URLs), and rule-based tokenization. It is also the practical implementation of theoretical Finite State Automata.

## 3. What the student will learn
- The syntax of Regex (wildcards, classes, anchors, quantifiers).
- The difference between Greedy and Non-greedy matching.
- How to use Python's `re` module (`search`, `match`, `findall`, `sub`).
- How to write practical regex for extracting emails, URLs, and phone numbers.
- The theoretical connection between Regex and Finite Automata.

## 4. Prerequisites
- [03. Tokenization](../03-tokenization/README.md)

## 5. Complete subtopic list
- [Regex Fundamentals](regex-fundamentals.md)
- [Advanced Regex and Python implementations](advanced-regex-and-python.md)
- [Regex Applications & Automata](regex-applications.md)

## 6. Recommended learning order
Read sequentially.

## 7. Mathematical difficulty
★☆☆☆☆ (Low - Based on logic and sets rather than numerical math)

## 8. Implementation difficulty
★★★☆☆ (Medium - Writing correct regex is notoriously tricky and requires practice)

## 9. Numerical-problem relevance
None.

## 10. Exam importance
**High**. You will almost certainly be asked to write a regex to match a specific pattern, or determine what strings a given regex matches.

## 11. Common mistakes
- Forgetting to escape special characters (e.g., using `.` instead of `\.` to match a literal period).
- Using greedy `.*` when non-greedy `.*?` is required.
- Confusing `re.match` (which only checks the start of the string) with `re.search` (which scans the whole string).

## 12. Related topics
- [05. Finite State Automata](../05-finite-state-automata/README.md)

## 13. Links to every subtopic
(See section 5)

## 14. Revision checklist
- [ ] Memorized `\w`, `\s`, `\d` and their uppercase negations.
- [ ] Memorized `+`, `*`, `?` quantifiers.

## 15. Implementation checklist
- [ ] Practiced writing `re.sub` for text cleaning.

## 16. Numerical-practice checklist
- [ ] N/A

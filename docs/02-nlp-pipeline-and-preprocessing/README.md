# 02. NLP Pipeline & Preprocessing

## 1. What this topic is
This module covers the critical first steps of any NLP project: gathering text data, ensuring the data splits are scientifically sound to avoid data leakage, and applying text cleaning and normalization to reduce noise.

## 2. Why it matters in NLP
"Garbage in, garbage out." The most advanced Transformer model in the world will fail if the text it receives is full of unhandled HTML tags or if the vocabulary was corrupted by data leakage during the training split.

## 3. What the student will learn
- The definition and causes of Data Leakage.
- How to perform Regex-based text cleaning.
- The tradeoffs of various normalization techniques (like lowercasing).
- How to construct a vocabulary and handle unknown tokens.

## 4. Prerequisites
- [01. NLP Fundamentals](../01-nlp-fundamentals/README.md)

## 5. Complete subtopic list
- [Data Collection and Splits](data-collection-and-splits.md)
- [Text Cleaning and Normalization](text-cleaning-and-normalization.md)
- [Vocabulary and Feature Engineering](vocabulary-and-features.md)

## 6. Recommended learning order
Read the modules sequentially.

## 7. Mathematical difficulty
★☆☆☆☆ (Very Low)

## 8. Implementation difficulty
★★☆☆☆ (Low - Basic Python string manipulation and Regular Expressions)

## 9. Numerical-problem relevance
None.

## 10. Exam importance
**Medium**. Expect theoretical questions on Data Leakage and practical questions asking you to write a Python function or Regex to clean a specific type of text.

## 11. Common mistakes
- Deduplicating data *after* splitting it, causing train/test contamination.
- Building the vocabulary over the test set.

## 12. Related topics
- [03. Tokenization](../03-tokenization/README.md)
- [04. Regular Expressions](../04-regular-expressions/README.md)

## 13. Links to every subtopic
(See section 5)

## 14. Revision checklist
- [ ] Understand Data Leakage
- [ ] Understand `<UNK>` handling

## 15. Implementation checklist
- [ ] Wrote a Regex-based cleaning function from scratch

## 16. Numerical-practice checklist
- [ ] N/A

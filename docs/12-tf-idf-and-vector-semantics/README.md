# 12. TF-IDF & Vector Semantics

## 1. What this topic is
This module introduces the mathematical foundation of converting text into numbers (Vectorization) so that algorithms can process it. It covers Bag of Words, TF-IDF, and measuring similarity using Vector Mathematics.

## 2. Why it matters in NLP
Every search engine in the 1990s and 2000s ran on TF-IDF and Cosine Similarity. Even though modern deep learning uses dense word embeddings (like Word2Vec) rather than sparse TF-IDF vectors, the foundational concepts of comparing mathematical vectors via cosine similarity remain identical.

## 3. What the student will learn
- The definition and flaws of Bag of Words and Count Vectorization.
- How TF-IDF counteracts frequency bias.
- How to calculate TF-IDF manually.
- How to calculate the dot product, vector magnitude, and cosine similarity.

## 4. Prerequisites
- Basic Algebra.
- [03. Tokenization](../03-tokenization/README.md)

## 5. Complete subtopic list
- [Bag of Words & Count Vectors](bag-of-words.md)
- [Term Frequency-Inverse Document Frequency (TF-IDF)](tf-idf.md)
- [Cosine Similarity & Vector Mathematics](cosine-similarity.md)

## 6. Recommended learning order
Read sequentially.

## 7. Mathematical difficulty
★★★☆☆ (Medium - Requires calculating logarithms, dot products, and square roots)

## 8. Implementation difficulty
★☆☆☆☆ (Very Low)

## 9. Numerical-problem relevance
**Extremely High**. Calculating TF-IDF and Cosine Similarity by hand are staple questions on NLP exams.

## 10. Exam importance
**Extremely High**. Expect heavy numerical problems from this module.

## 11. Common mistakes
- Using Euclidean distance instead of Cosine similarity.
- Forgetting that $IDF = \log(N / DF)$, not $\log(DF / N)$.

## 13. Links to every subtopic
(See section 5)

## 14. Revision checklist
- [ ] Understand why "the" gets an IDF score of 0.
- [ ] Memorize the Cosine Similarity formula.

## 15. Implementation checklist
- [ ] N/A

## 16. Numerical-practice checklist
- [ ] Given three documents, calculate the TF-IDF vector for Document 1.
- [ ] Calculate the Cosine Similarity between $[2, 0, 1]$ and $[1, 1, 1]$.

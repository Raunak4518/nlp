# 16. Laplace & Add-k Smoothing

## 1. What this topic is
This module introduces the mathematical techniques used to solve the Zero-Probability problem by shifting probability mass from seen events to unseen events.

## 2. Why it matters in NLP
Without smoothing, classical N-gram language models are completely unusable in the real world because they cannot generalize to novel, valid word combinations.

## 3. What the student will learn
- The Laplace (+1) smoothing formula.
- Why we must add $|V|$ (the vocabulary size) to the denominator.
- Why Laplace smoothing performs poorly on large vocabularies.
- The Add-k formula.
- How to tune hyperparameters like $k$ using a Validation Set.

## 4. Prerequisites
- [14. N-gram Language Models](../14-n-gram-language-models/README.md)
- [15. Sparsity & Zero-Probability Problem](../15-sparsity-and-zero-probability-problem/README.md)

## 5. Complete subtopic list
- [Laplace Smoothing (Add-One)](laplace-smoothing.md)
- [Add-k Smoothing](add-k-smoothing.md)

## 6. Recommended learning order
Read sequentially.

## 7. Mathematical difficulty
★★★☆☆ (Medium - Requires keeping track of vocabulary sizes and context counts)

## 8. Implementation difficulty
★☆☆☆☆ (Very Low - The formulas are one-liners)

## 9. Numerical-problem relevance
**Extremely High**. Calculating smoothed probabilities is one of the most common NLP exam questions.

## 10. Exam importance
**Extremely High**.

## 11. Common mistakes
- Adding $+1$ to the denominator instead of $+|V|$. You add $1$ to every word in the vocabulary, so the total added to the denominator is $1 \times |V|$.
- In Add-k smoothing, adding $+k$ to the denominator instead of $+k|V|$.

## 12. Related topics
- [17. Interpolation](../17-interpolation/README.md)
- [18. Naive Bayes Classification](../18-naive-bayes-classification/README.md) (Naive Bayes heavily relies on Laplace smoothing).

## 13. Links to every subtopic
(See section 5)

## 14. Revision checklist
- [ ] Memorize the Laplace and Add-k formulas.
- [ ] Understand why we tune $k$ on a validation set and not the training set.

## 15. Implementation checklist
- [ ] Write a python function for Add-k smoothing.

## 16. Numerical-practice checklist
- [ ] Calculate $P_{Laplace}(\text{word2} | \text{word1})$ given a small corpus.
- [ ] Calculate $P_{Add-k}(\text{word2} | \text{word1})$ with $k=0.5$ given a small corpus.

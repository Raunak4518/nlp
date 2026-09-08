# 13. Probability Foundations

## 1. What this topic is
This module is a brief review of the core mathematical statistics required to understand Language Models.

## 2. Why it matters in NLP
Every time you use an autocomplete feature on your phone or ask ChatGPT a question, the underlying model is calculating the conditional probability of the next word given the previous words using the Chain Rule of Probability.

## 3. What the student will learn
- The difference between Joint, Conditional, and Marginal probability.
- How to apply Bayes' Theorem.
- How to expand joint probabilities using the Chain Rule.
- How to estimate probabilities from raw text counts using MLE.

## 4. Prerequisites
- Basic Algebra.

## 5. Complete subtopic list
- [Probability Basics](probability-basics.md)
- [Bayes Theorem and The Chain Rule](bayes-and-chain-rule.md)
- [Maximum Likelihood Estimation (MLE)](maximum-likelihood-estimation.md)

## 6. Recommended learning order
Read sequentially.

## 7. Mathematical difficulty
★★★☆☆ (Medium - Requires understanding formal probability notation)

## 8. Implementation difficulty
★☆☆☆☆ (Very Low - Calculating counts is simple division)

## 9. Numerical-problem relevance
**High**. Calculating conditional probabilities from raw frequency counts is guaranteed to be on an exam.

## 10. Exam importance
**Medium-High**. The concepts here are fundamental prerequisites for N-gram Language Models and Naive Bayes classifiers.

## 11. Common mistakes
- Confusing $P(A|B)$ with $P(A, B)$. $P(A|B)$ assumes $B$ has already happened, so the denominator is only the count of $B$. $P(A, B)$ is the probability of both happening out of the *entire* dataset.
- Forgetting that the probabilities of all possible next words must sum to $1.0$.

## 12. Related topics
- [14. N-gram Language Models](../14-n-gram-language-models/README.md)
- [18. Naive Bayes Classification](../18-naive-bayes-classification/README.md)

## 13. Links to every subtopic
(See section 5)

## 14. Revision checklist
- [ ] Memorize the Chain Rule expansion.
- [ ] Understand why MLE fails for unseen words.

## 15. Implementation checklist
- [ ] N/A

## 16. Numerical-practice checklist
- [ ] Calculate $P(\text{"word2"} | \text{"word1"})$ given a small 3-sentence corpus.

# 23. Perplexity & Language Model Evaluation

## 1. What this topic is
This module explains how we objectively measure and compare the quality of different statistical language models using Intrinsic Evaluation (Perplexity) and Extrinsic Evaluation (Downstream Tasks).

## 2. Why it matters in NLP
You cannot improve what you cannot measure. If you write a new smoothing algorithm, the only way to prove it is better than Kneser-Ney is to evaluate both models on an unseen test set and show that your model achieves a lower perplexity.

## 3. What the student will learn
- Why multiplying raw probabilities causes underflow, and how Log Probabilities fix it.
- The definition of Cross-Entropy and Perplexity.
- Why $PP = \infty$ if the model encounters an unseen word without smoothing.
- The difference between Intrinsic and Extrinsic evaluation.

## 4. Prerequisites
- [14. N-gram Language Models](../14-n-gram-language-models/README.md)
- [15. Sparsity & Zero-Probability Problem](../15-sparsity-and-zero-probability-problem/README.md)

## 5. Complete subtopic list
- [Perplexity and Log Probabilities](perplexity-and-log-probabilities.md)
- [Intrinsic vs Extrinsic Evaluation](evaluation-methods.md)

## 6. Recommended learning order
Read sequentially.

## 7. Mathematical difficulty
★★★☆☆ (Medium - Requires understanding negative exponents and nth roots).

## 8. Implementation difficulty
★☆☆☆☆ (Very Low)

## 9. Numerical-problem relevance
**Extremely High**. Calculating the perplexity of a toy sentence given the probabilities is a guaranteed exam question.

## 10. Exam importance
**Extremely High**.

## 11. Common mistakes
- Thinking that *higher* perplexity is better. Perplexity is a measure of "surprise", so *lower* is better.
- Calculating perplexity using $P(W)^{1/N}$ instead of $P(W)^{-1/N}$. You must use the inverse!

## 12. Related topics
- [14. N-gram Language Models](../14-n-gram-language-models/README.md)

## 13. Links to every subtopic
(See section 5)

## 14. Revision checklist
- [ ] Memorize the formula for Perplexity.
- [ ] Understand why we must add Log probabilities instead of multiplying raw probabilities.

## 15. Implementation checklist
- [ ] N/A

## 16. Numerical-practice checklist
- [ ] Calculate the perplexity of a 4-word sentence where the probability of each word is $0.1$.

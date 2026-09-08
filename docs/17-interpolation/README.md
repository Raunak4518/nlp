# 17. Interpolation

## 1. What this topic is
This module covers Linear Interpolation, an advanced smoothing technique that combines multiple N-gram models together to solve the zero-probability problem.

## 2. Why it matters in NLP
While Laplace smoothing is easy to code, it destroys the probability distribution of frequent words. Interpolation allows us to keep the pure, unaltered MLE probabilities of the Trigram model, while using Bigram and Unigram models as a safety net for unseen phrases.

## 3. What the student will learn
- The Linear Interpolation formula.
- The conceptual difference between Interpolation (mixing) and Backoff (falling back).
- Why interpolation weights ($\lambda$) must sum to $1.0$.
- How to estimate $\lambda$ weights using Held-Out data.

## 4. Prerequisites
- [14. N-gram Language Models](../14-n-gram-language-models/README.md)
- [15. Sparsity & Zero-Probability Problem](../15-sparsity-and-zero-probability-problem/README.md)

## 5. Complete subtopic list
- [Linear Interpolation](linear-interpolation.md)
- [Estimating Interpolation Weights](estimating-weights.md)

## 6. Recommended learning order
Read sequentially.

## 7. Mathematical difficulty
★★☆☆☆ (Low - Basic weighted averages)

## 8. Implementation difficulty
★☆☆☆☆ (Very Low - The interpolation equation is straightforward)

## 9. Numerical-problem relevance
**High**. Calculating the final probability given three MLE tables and three $\lambda$ weights is a very common exam question.

## 10. Exam importance
**Medium-High**.

## 11. Common mistakes
- Thinking that Interpolation and Backoff are exactly the same thing.
- Forgetting that the $\lambda$ weights must sum to exactly $1.0$.

## 12. Related topics
- [16. Laplace & Add-k Smoothing](../16-laplace-and-add-k-smoothing/README.md)

## 13. Links to every subtopic
(See section 5)

## 14. Revision checklist
- [ ] Memorize the interpolation formula.
- [ ] Understand why Held-Out data is required to estimate the weights.

## 15. Implementation checklist
- [ ] N/A

## 16. Numerical-practice checklist
- [ ] Calculate an interpolated probability given three raw MLE scores and their respective weights.

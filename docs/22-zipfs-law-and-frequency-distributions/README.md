# 22. Zipf's Law & Frequency Distributions

## 1. What this topic is
This module covers Zipf's Law, the empirical rule governing the frequency distribution of words in natural language.

## 2. Why it matters in NLP
Zipf's Law is the mathematical proof that Data Sparsity is a permanent feature of human language. It proves that you cannot solve the OOV (Out of Vocabulary) problem just by collecting more data.

## 3. What the student will learn
- The relationship between Frequency and Rank.
- The concept of the "Long Tail" in a power-law distribution.
- Why plotting in Log-Log space yields a straight line.
- How to calculate expected frequencies using the Zipfian constant.

## 4. Prerequisites
- [15. Sparsity & Zero-Probability Problem](../15-sparsity-and-zero-probability-problem/README.md)

## 5. Complete subtopic list
- [Zipf's Law and Frequency Distributions](zipfs-law.md)

## 6. Recommended learning order
Read sequentially.

## 7. Mathematical difficulty
★☆☆☆☆ (Very Low - Basic division)

## 8. Implementation difficulty
★☆☆☆☆ (Very Low)

## 9. Numerical-problem relevance
**High**. Calculating the expected frequency of a word given the frequency of the top-ranked word is a common, easy exam question.

## 10. Exam importance
**Medium-High**.

## 11. Common mistakes
- Confusing Zipf's Law ($f \propto 1/r$) with Heaps' Law (which describes vocabulary growth over time).

## 12. Related topics
- [18. Good-Turing Smoothing](../18-good-turing-smoothing/README.md) (Good-Turing relies on the Zipfian distribution of singletons).

## 13. Links to every subtopic
(See section 5)

## 14. Revision checklist
- [ ] Understand why the Log-Log plot is a straight line.
- [ ] Memorize $f \times r = c$.

## 15. Implementation checklist
- [ ] N/A

## 16. Numerical-practice checklist
- [ ] Given $f_1 = 10000$, find $f_5$.

# 20. Backoff & Discounting

## 1. What this topic is
This module explores Backoff algorithms, a conditional alternative to Interpolation. It covers how we combine Backoff with Absolute Discounting to mathematically guarantee that all probabilities sum to 1.0, and how Stupid Backoff throws away the math for the sake of speed.

## 2. Why it matters in NLP
Stupid Backoff was the de-facto standard language modeling algorithm used by Google for large-scale systems (like machine translation) before the deep learning revolution, proving that massive data often beats complex math.

## 3. What the student will learn
- The conceptual difference between Backoff and Interpolation.
- The Absolute Discounting formula ($C^* = C - d$).
- How to estimate the discount $D$ using $N_1$ and $N_2$.
- The logic of Katz Backoff weights.
- The Stupid Backoff algorithm and why it is "stupid".

## 4. Prerequisites
- [17. Interpolation](../17-interpolation/README.md)
- [18. Good-Turing Smoothing](../18-good-turing-smoothing/README.md)

## 5. Complete subtopic list
- [Backoff and Absolute Discounting](backoff-and-absolute-discounting.md)
- [Katz and Stupid Backoff](katz-and-stupid-backoff.md)

## 6. Recommended learning order
Read sequentially.

## 7. Mathematical difficulty
★★★☆☆ (Medium - Understanding how leftover probability mass is distributed can be tricky).

## 8. Implementation difficulty
★★☆☆☆ (Low - Stupid Backoff is very easy to code).

## 9. Numerical-problem relevance
**High**. Calculating absolute discounted probabilities is a common exam question.

## 10. Exam importance
**High**.

## 11. Common mistakes
- Applying the discount $d$ to unseen words (counts of 0). The discount is *only* subtracted from words that actually appeared (counts $> 0$).
- Assuming Stupid Backoff outputs real probabilities. It does not; it outputs relative scores that can exceed 1.0.

## 12. Related topics
- [21. Kneser-Ney Smoothing](../21-kneser-ney-smoothing/README.md)

## 13. Links to every subtopic
(See section 5)

## 14. Revision checklist
- [ ] Memorize the Stupid Backoff algorithm logic.
- [ ] Understand why we must discount seen events before backing off to unseen events.

## 15. Implementation checklist
- [ ] Trace the Stupid Backoff python function.

## 16. Numerical-practice checklist
- [ ] Given an $N=100$ context, $T=5$ unique words, and $d=0.75$, calculate the total leftover probability mass available for unseen words.

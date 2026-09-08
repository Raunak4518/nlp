# 25. Text Classification

## 1. What this topic is
This module introduces supervised machine learning for NLP. It covers the Naive Bayes algorithm for categorization, and the standard evaluation metrics (Precision, Recall, F1) used to grade classification models.

## 2. Why it matters in NLP
Assigning categories to text is one of the most common commercial applications of NLP (e.g., routing customer support tickets to the right department, filtering spam, detecting toxic language). Understanding how to properly evaluate these systems using F1-score instead of Accuracy is critical for any data scientist.

## 3. What the student will learn
- How Naive Bayes uses Bayes' Theorem to classify documents.
- Why the "naive" independence assumption is made.
- Why Laplace smoothing is required for Naive Bayes.
- How to implement Naive Bayes from scratch using log probabilities.
- How to calculate Precision, Recall, and F1 from a Confusion Matrix.

## 4. Prerequisites
- [12. TF-IDF & Vector Semantics](../12-tf-idf-and-vector-semantics/README.md)
- [13. Probability Foundations](../13-probability-foundations/README.md)
- [16. Laplace & Add-k Smoothing](../16-laplace-and-add-k-smoothing/README.md)

## 5. Complete subtopic list
- [Text Classification and Naive Bayes](classification-and-naive-bayes.md)
- [Evaluation Metrics: Precision, Recall, and F1](evaluation-metrics.md)

## 6. Recommended learning order
Read sequentially.

## 7. Mathematical difficulty
★★★☆☆ (Medium - Requires combining log probabilities and calculating harmonic means).

## 8. Implementation difficulty
★★★☆☆ (Medium - Tracking vocabularies and class counts in nested dictionaries).

## 9. Numerical-problem relevance
**Extremely High**. Calculating P, R, and F1 from a confusing matrix is guaranteed to be on an exam.

## 10. Exam importance
**Extremely High**.

## 11. Common mistakes
- Confusing Precision and Recall. Remember: **P**recision is about **P**redictions (denominator is TP+FP). Recall is about Reality (denominator is TP+FN).
- Forgetting to use Log space, resulting in $0.0$ due to underflow.

## 12. Related topics
- [26. Sentiment Analysis](../26-sentiment-analysis/README.md)

## 13. Links to every subtopic
(See section 5)

## 14. Revision checklist
- [ ] Understand why Accuracy fails on imbalanced datasets.
- [ ] Memorize the formulas for Precision, Recall, and F1.

## 15. Implementation checklist
- [ ] Trace the Naive Bayes class prediction loop.

## 16. Numerical-practice checklist
- [ ] Given $TP=50, FP=10, FN=5$, calculate F1.

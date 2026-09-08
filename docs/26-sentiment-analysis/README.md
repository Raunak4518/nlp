# 26. Sentiment Analysis

## 1. What this topic is
This module applies the text classification techniques learned in Module 25 specifically to the task of Sentiment Analysis (Opinion Mining).

## 2. Why it matters in NLP
Sentiment Analysis is one of the most commercially valuable NLP tasks. Companies use it to automatically track brand health on social media, analyze product reviews, and flag angry customer support emails for immediate human intervention.

## 3. What the student will learn
- The definition of Sentiment Analysis.
- How Lexicon-based classification works.
- The severe limitations of Lexicons regarding negation.
- Why Bigram Naive Bayes solves the negation problem.
- Why Accuracy is a terrible metric for sentiment datasets.

## 4. Prerequisites
- [25. Text Classification](../25-text-classification/README.md)

## 5. Complete subtopic list
- [Sentiment Analysis](sentiment-analysis.md)

## 6. Recommended learning order
Read sequentially.

## 7. Mathematical difficulty
★☆☆☆☆ (Very Low - Basic summation for Lexicons).

## 8. Implementation difficulty
★☆☆☆☆ (Very Low - The lexicon loop is a few lines of code).

## 9. Numerical-problem relevance
**Medium**. Scoring a sentence given a small lexicon dictionary is a common short-answer question.

## 10. Exam importance
**Medium**. Usually tested as an application of Naive Bayes rather than a standalone mathematical topic.

## 11. Common mistakes
- Assuming Sentiment Analysis is an entirely different algorithm from Text Classification. It is the exact same math, just with the specific labels `POSITIVE` and `NEGATIVE`.

## 12. Related topics
- [25. Text Classification](../25-text-classification/README.md)

## 13. Links to every subtopic
(See section 5)

## 14. Revision checklist
- [ ] Understand why Lexicons fail on phrases like "not terrible".
- [ ] Explain why F1 score must be used instead of Accuracy for Amazon product reviews.

## 15. Implementation checklist
- [ ] Trace the Lexicon sentiment loop.

## 16. Numerical-practice checklist
- [ ] Given a lexicon, calculate the sentiment score of a 5-word sentence.

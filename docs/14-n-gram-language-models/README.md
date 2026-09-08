# 14. N-gram Language Models

## 1. What this topic is
This module introduces the classical approach to Language Modeling: predicting the probability of text sequences using N-grams and the Markov Assumption.

## 2. Why it matters in NLP
Every modern Large Language Model (like GPT-4) is fundamentally doing the exact same task described in this module: Next-Token Prediction. While modern models use deep neural networks instead of MLE counting tables, the mathematical framing of the task—calculating $P(w_n | w_1...w_{n-1})$—remains identical.

## 3. What the student will learn
- The formal definition of a Language Model.
- The Markov assumption and how it defines Unigram, Bigram, and Trigram models.
- How to calculate n-gram probabilities by hand using count data.
- How start/end markers and `<UNK>` tokens are used in generation.
- How to build a Bigram generator from scratch in Python.

## 4. Prerequisites
- [13. Probability Foundations](../13-probability-foundations/README.md)
- [03. Tokenization](../03-tokenization/README.md)

## 5. Complete subtopic list
- [Language Models and N-grams](language-models-and-ngrams.md)
- [N-gram Probabilities](n-gram-probabilities.md)
- [Text Generation and Boundaries](text-generation.md)

## 6. Recommended learning order
Read sequentially.

## 7. Mathematical difficulty
★★★☆☆ (Medium - Requires carefully tracking counts and numerators/denominators)

## 8. Implementation difficulty
★★★☆☆ (Medium - Writing the nested dictionaries for the Python generator takes practice)

## 9. Numerical-problem relevance
**Extremely High**. "Given this 3-sentence corpus, what is the probability of the sentence X under a Bigram model?" is a guaranteed exam question.

## 10. Exam importance
**Extremely High**. This is the core of statistical NLP.

## 11. Common mistakes
- Dividing the count of a bigram by the total number of words in the corpus, instead of dividing it by the count of the unigram context.
- Forgetting to include the probability of transitioning from `<s>` to the first word when calculating the probability of a full sentence.

## 12. Related topics
- [15. Sparsity & Zero-Probability Problem](../15-sparsity-and-zero-probability-problem/README.md)

## 13. Links to every subtopic
(See section 5)

## 14. Revision checklist
- [ ] Memorize the formula for the number of n-grams in a sentence: $N - n + 1$.
- [ ] Understand why we can't use 10-gram models.

## 15. Implementation checklist
- [ ] Trace the Bigram Generator python script.

## 16. Numerical-practice checklist
- [ ] Calculate $P(\text{"I am Sam"}) = P(\text{"I"} | \text{"<s>"}) \times P(\text{"am"} | \text{"I"}) \times P(\text{"Sam"} | \text{"am"}) \times P(\text{"</s>"} | \text{"Sam"})$ using the toy corpus.

# 24. Byte Pair Encoding (BPE)

## 1. What this topic is
This module explains Byte Pair Encoding (BPE), the Subword Tokenization algorithm used by almost every modern Large Language Model (including GPT-4 and LLaMA) to process text.

## 2. Why it matters in NLP
Before subword tokenization, Language Models failed spectacularly when encountering Out Of Vocabulary (OOV) words. BPE elegantly solves this by breaking unknown words down into known, constituent subword pieces (and ultimately down to individual characters if necessary), ensuring the model never has to output a meaningless `<UNK>` token.

## 3. What the student will learn
- The flaws of pure word-level and pure character-level tokenization.
- The 5 steps of the BPE algorithm.
- How to perform BPE merges manually.
- How to implement the counting and merging BPE loops from scratch in Python.
- The differences between BPE, WordPiece, and Unigram LM tokenization.

## 4. Prerequisites
- [03. Tokenization](../03-tokenization/README.md)

## 5. Complete subtopic list
- [Byte Pair Encoding (BPE) Fundamentals](bpe-fundamentals.md)
- [BPE Implementation and Alternatives](bpe-implementation-and-alternatives.md)

## 6. Recommended learning order
Read sequentially.

## 7. Mathematical difficulty
★☆☆☆☆ (Very Low - Just basic counting and finding the maximum value).

## 8. Implementation difficulty
★★★☆☆ (Medium - Writing the string replacement logic requires being careful with spaces and boundaries).

## 9. Numerical-problem relevance
**Extremely High**. "Perform 3 iterations of BPE on the following toy corpus" is a highly standard exam question.

## 10. Exam importance
**Extremely High**. BPE is the foundation of modern NLP tokenization.

## 11. Common mistakes
- Forgetting to append the end-of-word token (`</w>`) to the words before starting the algorithm. The `</w>` token is crucial because it helps the model distinguish between a subword at the end of a word (like "er" in "lower") and a subword in the middle of a word (like "er" in "very").
- Replacing strings blindly during the merge step (e.g., replacing "a" and "t" with "at" without checking if they are actually adjacent space-separated tokens).

## 12. Related topics
- [03. Tokenization](../03-tokenization/README.md)
- [26. Naive Bayes Classification](../26-naive-bayes-classification/README.md)

## 13. Links to every subtopic
(See section 5)

## 14. Revision checklist
- [ ] Understand why BPE is better than `<UNK>` tokens.
- [ ] Know the difference between BPE (frequency) and WordPiece (likelihood).

## 15. Implementation checklist
- [ ] Trace the BPE Trainer python script.

## 16. Numerical-practice checklist
- [ ] Perform two manual BPE merges on a 3-word toy corpus.

# 03. Tokenization

## 1. What this topic is
This module covers how we slice a continuous string of text into the fundamental atomic units (tokens) that machine learning models process.

## 2. Why it matters in NLP
Tokenization dictates the size of your vocabulary. If you tokenize poorly, your vocabulary explodes, and the model encounters thousands of `<UNK>` (Unknown) tokens in production, destroying its ability to understand context.

## 3. What the student will learn
- The tradeoffs between character, word, and subword tokenization.
- The mechanics and difficulties of sentence boundary disambiguation.
- How to implement Whitespace, Punctuation, Regex, and N-gram tokenizers from scratch.

## 4. Prerequisites
- [02. NLP Pipeline & Preprocessing](../02-nlp-pipeline-and-preprocessing/README.md)
- Basic Python string manipulation.

## 5. Complete subtopic list
- [Tokenization Fundamentals](tokenization-fundamentals.md)
- [Sentence Segmentation](sentence-segmentation.md)
- [Tokenization Algorithms & Scratch Implementations](tokenization-algorithms.md)

## 6. Recommended learning order
Read the modules sequentially.

## 7. Mathematical difficulty
★☆☆☆☆ (Very Low)

## 8. Implementation difficulty
★★★☆☆ (Medium - Requires algorithmic thinking for n-grams and regex)

## 9. Numerical-problem relevance
None.

## 10. Exam importance
**High**. Implementing an n-gram extractor from scratch is a highly common interview and exam question.

## 11. Common mistakes
- Forgetting that the number of n-grams in a sequence of length $N$ is $N - n + 1$.
- Assuming periods always mark the end of a sentence.

## 12. Related topics
- [04. Regular Expressions](../04-regular-expressions/README.md)
- [14. N-gram Language Models](../14-n-gram-language-models/README.md)

## 13. Links to every subtopic
(See section 5)

## 14. Revision checklist
- [ ] Understand why `<UNK>` tokens appear.
- [ ] Memorize the formula for the number of n-grams.

## 15. Implementation checklist
- [ ] Wrote a pure whitespace tokenizer.
- [ ] Wrote a regex tokenizer.
- [ ] Wrote an n-gram extractor.
- [ ] Wrote a rule-based sentence segmenter.

## 16. Numerical-practice checklist
- [ ] N/A

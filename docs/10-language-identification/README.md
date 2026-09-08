# 10. Language Identification

## 1. What this topic is
This module covers Language Identification (LangID), the computational task of predicting the natural language of a given document.

## 2. Why it matters in NLP
Every downstream NLP tool (tokenizers, stemmers, POS taggers, dependency parsers) is language-specific. Feeding Spanish text into an English POS tagger will crash the pipeline or produce garbage output. LangID is the required "Step 0" routing mechanism for any system that ingests raw internet text.

## 3. What the student will learn
- Why LangID is considered a solved problem for long texts but remains difficult for short texts.
- Why models must handle "Unknown" languages using confidence thresholds.
- The concept of Character N-gram Language Profiles.
- How to implement the Out-of-Place rank-distance algorithm from scratch.

## 4. Prerequisites
- [03. Tokenization](../03-tokenization/README.md) (Specifically, N-gram tokenization)

## 5. Complete subtopic list
- [Language Identification Fundamentals](language-identification-fundamentals.md)
- [N-Gram Language Profiles](n-gram-language-profiles.md)

## 6. Recommended learning order
Read sequentially.

## 7. Mathematical difficulty
★☆☆☆☆ (Very Low - Basic arithmetic and ranking)

## 8. Implementation difficulty
★★☆☆☆ (Low - The OoP algorithm is very straightforward to code)

## 9. Numerical-problem relevance
**High**. You may be given two small language profiles and a document profile, and asked to calculate the Out-of-Place distance manually.

## 10. Exam importance
**Medium**. Character n-grams are a favorite topic because they demonstrate that you don't always need complex grammar to solve an NLP task.

## 11. Common mistakes
- Confusing Character N-Grams (used here) with Word N-Grams (used in Language Modeling/Text Generation).
- Trying to calculate distance based on the *count* of the n-gram rather than its *rank*.

## 12. Related topics
- [14. N-gram Language Models](../14-n-gram-language-models/README.md)

## 13. Links to every subtopic
(See section 5)

## 14. Revision checklist
- [ ] Understand why LangID struggles with 2-word sentences.
- [ ] Memorize the OoP distance calculation.

## 15. Implementation checklist
- [ ] Trace the Language Profiler python script.

## 16. Numerical-practice checklist
- [ ] Calculate the absolute difference in ranks for a given n-gram manually.

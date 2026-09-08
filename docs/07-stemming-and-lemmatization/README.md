# 07. Stemming & Lemmatization

## 1. What this topic is
This module covers two foundational techniques used to reduce words to their base forms, which is critical for reducing vocabulary size and clustering semantically related words in traditional NLP pipelines.

## 2. Why it matters in NLP
If a user searches Google for "how to fix running shoes", they expect results containing "runs" and "ran" as well. Stemming and Lemmatization are the classic Information Retrieval techniques used to normalize these variations so the search engine recognizes them as the same underlying concept.

## 3. What the student will learn
- How rule-based suffix strippers (like Porter) work and fail.
- Why Lemmatization requires Part-of-Speech tagging.
- The tradeoff between speed/recall (Stemming) and precision/accuracy (Lemmatization).

## 4. Prerequisites
- [06. Finite State Transducers & Morphology](../06-finite-state-transducers-and-morphology/README.md)

## 5. Complete subtopic list
- [Stemming](stemming.md)
- [Lemmatization](lemmatization.md)
- [Stemming vs Lemmatization](stemming-vs-lemmatization.md)

## 6. Recommended learning order
Read sequentially.

## 7. Mathematical difficulty
★☆☆☆☆ (Very Low)

## 8. Implementation difficulty
★☆☆☆☆ (Very Low - Basic string matching and dictionary lookups)

## 9. Numerical-problem relevance
None.

## 10. Exam importance
**Extremely High**. "Compare and contrast Stemming and Lemmatization" is one of the most common standard exam questions in any introductory NLP course.

## 11. Common mistakes
- Believing that a Stem must be a valid English word.
- Forgetting that Lemmatizers require POS tags to resolve ambiguity.

## 12. Related topics
- [08. POS Tagging & Sequence Labeling](../08-pos-tagging-and-sequence-labeling/README.md)

## 13. Links to every subtopic
(See section 5)

## 14. Revision checklist
- [ ] Memorize the comparison table.
- [ ] Understand why Deep Learning pipelines rarely use these techniques today.

## 15. Implementation checklist
- [ ] Trace the POS-aware lemmatizer with "leaves".

## 16. Numerical-practice checklist
- [ ] N/A

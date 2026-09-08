# 06. Finite State Transducers & Morphology

## 1. What this topic is
This module introduces Morphology (the linguistic study of word formation) and Finite State Transducers (FSTs), the computational tool used to model morphological rules.

## 2. Why it matters in NLP
Languages like English have millions of valid word forms, but they are generated from a much smaller set of roots and affixes. If a system encounters the word "antidisestablishmentarianisms", it won't be in the dictionary. An FST-based morphological analyzer is required to break it down into known components so the system can infer its meaning.

## 3. What the student will learn
- Linguistic definitions of Morphs, Morphemes, Roots, and Stems.
- The critical difference between Inflectional and Derivational morphology.
- How to handle English plural and verb rules.
- How Finite State Transducers (FSTs) differ from FSAs.
- How to implement a basic FST in Python to handle morphological generation.

## 4. Prerequisites
- [05. Finite State Automata](../05-finite-state-automata/README.md)

## 5. Complete subtopic list
- [Morphology Fundamentals](morphology-fundamentals.md)
- [Finite State Transducers](finite-state-transducers.md)

## 6. Recommended learning order
Read sequentially.

## 7. Mathematical difficulty
★☆☆☆☆ (Very Low)

## 8. Implementation difficulty
★★★☆☆ (Medium - Understanding the two-tape FST concept in code requires careful tracking)

## 9. Numerical-problem relevance
None.

## 10. Exam importance
**Medium-High**. The distinction between inflectional and derivational morphology is a guaranteed multiple-choice or short-answer question.

## 11. Common mistakes
- Confusing a Morph (the physical letters) with a Morpheme (the abstract meaning).
- Assuming FSTs can only run in one direction (they are bidirectional).

## 12. Related topics
- [07. Stemming & Lemmatization](../07-stemming-and-lemmatization/README.md)

## 13. Links to every subtopic
(See section 5)

## 14. Revision checklist
- [ ] Understand Inflection vs Derivation.
- [ ] Understand why FSTs are used instead of dictionaries.

## 15. Implementation checklist
- [ ] Trace the Plural FST code with the input `"box+#"`.

## 16. Numerical-practice checklist
- [ ] N/A

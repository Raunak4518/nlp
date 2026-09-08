# 08. POS Tagging & Sequence Labeling

## 1. What this topic is
This module covers Part-of-Speech (POS) tagging, the first major "Sequence Labeling" task in NLP, where every word in a sequence must be assigned a label.

## 2. Why it matters in NLP
Words are highly ambiguous. Is "book" a noun or a verb? Is "back" an adjective, adverb, noun, or verb? Without resolving this ambiguity, downstream systems cannot accurately parse the syntactic structure of a sentence or determine its meaning. Furthermore, the sequence labeling concepts learned here (like BIO encoding) are the exact same concepts used for Named Entity Recognition.

## 3. What the student will learn
- The definitions of major Open and Closed word classes.
- How BIO and BILOU encoding allow us to label multi-token entities.
- How Hidden Markov Models (HMM) combine transition and emission probabilities to tag sequences.
- How the Viterbi algorithm prevents exponential time complexity.

## 4. Prerequisites
- Basic understanding of probabilities.

## 5. Complete subtopic list
- [Parts of Speech](parts-of-speech.md)
- [Sequence Labeling](sequence-labeling-fundamentals.md)
- [POS Tagging Algorithms](pos-tagging-algorithms.md)

## 6. Recommended learning order
Read sequentially.

## 7. Mathematical difficulty
★★★☆☆ (Medium - Understanding HMM probabilities requires focus)

## 8. Implementation difficulty
★★★★☆ (High - The Viterbi algorithm is a complex dynamic programming concept)

## 9. Numerical-problem relevance
**High**. You may be asked to calculate the HMM probability of a specific tag sequence given a set of transition/emission tables.

## 10. Exam importance
**Extremely High**. HMMs and Viterbi are foundational concepts in classical NLP and Speech Recognition. BIO encoding is universally asked about in NER contexts.

## 11. Common mistakes
- Confusing Emission Probability $P(word|tag)$ with the reverse $P(tag|word)$.
- Improperly applying BIO tags (e.g., starting an entity with `I-` instead of `B-`).

## 12. Related topics
- [09. Named Entity Recognition](../09-named-entity-recognition/README.md)

## 13. Links to every subtopic
(See section 5)

## 14. Revision checklist
- [ ] Memorized the difference between Transition and Emission probabilities.
- [ ] Understand BIO vs BILOU encoding.

## 15. Implementation checklist
- [ ] Read and trace the Viterbi python implementation.

## 16. Numerical-practice checklist
- [ ] Calculate the probability of a 3-word sequence manually using an HMM table.

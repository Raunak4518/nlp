# 09. Named Entity Recognition

## 1. What this topic is
This module covers Named Entity Recognition (NER), the process of locating and classifying proper nouns (people, places, organizations) and numerical data (dates, money) within raw text.

## 2. Why it matters in NLP
NER is the cornerstone of Information Extraction. If you want to build a system that reads financial news and alerts you whenever a "COMPANY" mentions a "MONEY" amount regarding an "EVENT", you must use an NER model.

## 3. What the student will learn
- The standard CoNLL-2003 entity types.
- How to apply BIO encoding to multi-token entities.
- How to extract entities from BIO tags programmatically.
- The difference between Strict and Partial evaluation metrics.
- The concept of Entity Linking (Disambiguation).

## 4. Prerequisites
- [08. POS Tagging & Sequence Labeling](../08-pos-tagging-and-sequence-labeling/README.md)

## 5. Complete subtopic list
- [Named Entity Recognition Fundamentals](ner-fundamentals.md)
- [NER Tagging and Evaluation](ner-tagging-and-evaluation.md)
- [Entity Linking](entity-linking.md)

## 6. Recommended learning order
Read sequentially.

## 7. Mathematical difficulty
★☆☆☆☆ (Very Low - Basic Precision/Recall concepts)

## 8. Implementation difficulty
★★☆☆☆ (Low - The BIO extraction logic requires some careful loop tracking)

## 9. Numerical-problem relevance
None.

## 10. Exam importance
**High**. Expect to be given a sentence and asked to manually tag it using BIO format for specified entities.

## 11. Common mistakes
- Tagging words like "he" or "she" as PERSON entities. (NER generally only applies to *named* entities, proper nouns, not pronouns).
- Failing to distinguish between NER (finding the string) and Entity Linking (resolving the string to a database).

## 12. Related topics
- [10. Language Identification](../10-language-identification/README.md)

## 13. Links to every subtopic
(See section 5)

## 14. Revision checklist
- [ ] Understand Strict vs Partial evaluation.
- [ ] Know the difference between NER and Entity Linking.

## 15. Implementation checklist
- [ ] Implement the BIO extraction python script.

## 16. Numerical-practice checklist
- [ ] N/A

# 29. Summarization, QA & Information Extraction

## 1. What this topic is
This module provides a high-level overview of three major NLP applications: Summarization (shortening text), Question Answering (finding facts in text), and Information Extraction (turning text into structured databases).

## 2. Why it matters in NLP
Language Models on their own are just text generators. Wrapping them in these application frameworks turns them into highly lucrative products (like Google Search, ChatGPT, and enterprise knowledge graphs).

## 3. What the student will learn
- The difference between Extractive and Abstractive summarization.
- How to implement a basic sentence-scoring algorithm using TF-IDF.
- The difference between Retrieval-based QA and Generative QA.
- What Entity Linking and Relation Extraction are used for.

## 4. Prerequisites
- [09. Named Entity Recognition](../09-named-entity-recognition/README.md)
- [12. TF-IDF & Vector Semantics](../12-tf-idf-and-vector-semantics/README.md)

## 5. Complete subtopic list
- [Summarization](summarization.md)
- [QA and Information Extraction](qa-and-information-extraction.md)

## 6. Recommended learning order
Read sequentially.

## 7. Mathematical difficulty
★☆☆☆☆ (Very Low - Basic averaging for sentence scores).

## 8. Implementation difficulty
★★☆☆☆ (Low - The extractive summarization script is easy to write).

## 9. Numerical-problem relevance
**Low**.

## 10. Exam importance
**Medium**. Usually tested via conceptual multiple-choice questions.

## 11. Common mistakes
- Forgetting to normalize sentence scores by sentence length when building an extractive summarizer.
- Confusing NER (which just tags "Apple" as an ORG) with Entity Linking (which maps "Apple" to the database ID for the tech company).

## 12. Related topics
- [27. Sequence Generation](../27-sequence-generation/README.md)

## 13. Links to every subtopic
(See section 5)

## 14. Revision checklist
- [ ] Understand why Abstractive Summarization is much harder than Extractive Summarization.
- [ ] Define the term "Knowledge Graph" in the context of Relation Extraction.

## 15. Implementation checklist
- [ ] Trace the Extractive Sentence Scoring Python function.

## 16. Numerical-practice checklist
- [ ] Given a 3-word sentence and 3 TF-IDF scores, calculate the normalized sentence score.

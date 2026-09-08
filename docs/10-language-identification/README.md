# 10. Language Identification

## 1. Topic Overview
This module covers Language Identification (LangID), the computational task of predicting the natural language of a given document. 

```mermaid
mindmap
  root((Language ID))
    Challenges
      Short Texts
      Multilingual Documents
      Unknown Languages
    Techniques
      Stop-word counting (Naive)
      Character N-grams (Robust)
    Evaluation
      Out-of-Place (OoP) Metric
      Rank Distance
```

## 2. Learning Path
1. [Language Identification Fundamentals](language-identification-fundamentals.md)
2. [N-Gram Language Profiles](n-gram-language-profiles.md)

## 3. Real-World Applications
- **The "Step 0" Routing Mechanism**: Every downstream NLP tool (tokenizers, stemmers, POS taggers, dependency parsers) is deeply language-specific. Feeding Spanish text into an English POS tagger will crash the pipeline or produce garbage output. LangID acts as a router, directing incoming internet text to the correct language-specific pipeline.
- **Web Browsers**: Browsers use LangID to detect when a webpage is written in a language different from your system default, triggering the "Translate this page?" popup.
- **Social Media Moderation**: Ensuring that hate-speech detection algorithms are applied using the correct localized models for tweets.

## 4. Difficulty & Importance
- **Mathematical Difficulty**: ★☆☆☆☆ (Very Low - Basic arithmetic and ranking)
- **Implementation Difficulty**: ★★☆☆☆ (Low - The OoP algorithm is very straightforward to code)
- **Exam Importance**: **Medium**. Character n-grams are a favorite topic because they demonstrate a beautiful NLP principle: you don't always need complex grammar or dictionaries to solve an NLP task. Pure statistical frequency is often enough.

## 5. Prerequisites
- [03. Tokenization](../03-tokenization/README.md) (Specifically, N-gram tokenization)

## 6. External Resources
- 📘 **Classic Paper**: [N-Gram-Based Text Categorization (Cavnar & Trenkle, 1994)](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.53.9367&rep=rep1&type=pdf) - The foundational paper on the Out-of-Place algorithm.

---

### Can You Explain This?
- [ ] I can explain why Language ID is considered a "solved" problem for whole documents, but remains difficult for tweets.
- [ ] I can explain why we must use *Character* N-grams instead of *Word* N-grams for this task.
- [ ] I can calculate the Out-of-Place distance between a document profile and a language profile manually.

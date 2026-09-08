# Stemming vs Lemmatization

## 1. Direct Comparison

Both stemming and lemmatization share the exact same goal: mapping related words back to a common base to reduce the vocabulary size and group semantically similar concepts together (e.g., ensuring a search for "running" also finds documents containing "runs").

However, they achieve this in fundamentally different ways. This table is one of the most frequently tested concepts in introductory NLP.

| Feature | Stemming | Lemmatization |
| :--- | :--- | :--- |
| **Mechanism** | Rule-based suffix stripping (raw string manipulation) | Dictionary lookup and morphological analysis |
| **Output** | A "stem" (often not a real word, e.g., `univers`) | A "lemma" (always a valid dictionary word, e.g., `university`) |
| **Speed** | Extremely fast | Slower (requires dictionary search) |
| **Context Awareness** | Blind to context | Requires POS tag context to resolve ambiguity |
| **Handling Irregulars** | Fails completely (`mice` $\rightarrow$ `mic`) | Handles perfectly (`mice` $\rightarrow$ `mouse`) |

---

## 2. When to Use Which?

### Use Stemming When:
- **Speed is critical**: Indexing billions of documents for a search engine where absolute precision isn't required and memory/compute is a bottleneck.
- **Recall is more important than Precision**: You want a search for "organize" to return documents containing "organization" and "organ" just in case they are relevant, even if some are false positives (over-stemming).

### Use Lemmatization When:
- **Precision is critical**: Building a high-quality chatbot or translation engine where the exact grammatical meaning of the word matters.
- **Working with Morphologically Rich Languages**: Stemming works reasonably well for English, but fails catastrophically for languages like Arabic or Turkish. Lemmatization via FSTs is required for these languages.
- **Readability matters**: If you are generating text or displaying keywords to a human user, showing stems like "presum" looks broken. You must use lemmas.

---

## 3. The Modern Deep Learning Context

Do modern Large Language Models (like GPT-4 or BERT) use Stemming or Lemmatization? 

**Generally, NO.**

Modern deep learning pipelines use **Subword Tokenization** (like BPE or WordPiece). Subword tokenization inherently handles morphological variations by splitting prefixes and suffixes into separate tokens without destroying them. 
- *Example*: `running` $\rightarrow$ `run`, `##ning`

Because the neural network can learn the mathematical relationship between these subwords dynamically during training, explicitly forcing words into stems or lemmas beforehand actually *destroys* valuable grammatical information (like tense, mood, and number) that the neural network could have used to understand the exact nuance of the sentence.

---

## 4. Exam Preparation

### How to Write This in an Exam

**10-Mark Question**: Compare and contrast Stemming and Lemmatization. Discuss their mechanisms, outputs, and dependencies. Provide an example where stemming fails but lemmatization succeeds. Finally, discuss their relevance in modern Deep Learning pipelines.
> **Answer**: 
> Stemming and lemmatization both aim to reduce morphological variations to a base form. 
> 
> **Mechanism & Output**: Stemming uses crude, rule-based string manipulation (suffix stripping) to chop words down. It is blind to context and often outputs non-dictionary strings (e.g., `university` $\rightarrow$ `univers`). Lemmatization uses morphological analysis and dictionary lookups to return a valid linguistic lemma (e.g., `better` $\rightarrow$ `good`).
> 
> **Dependencies**: Because stemming is purely string-based, it requires no prior context. Lemmatization strictly requires Part-of-Speech (POS) tagging to resolve ambiguous words before lookup.
> 
> **Example of Failure**: Stemmers fail completely on highly irregular verbs. Given the word `was`, a stemmer might strip the 's' to output `wa`. A lemmatizer correctly identifies the verb and maps it to `be`.
> 
> **Modern Relevance**: In modern Deep Learning, neither technique is widely used. Subword tokenization (like BPE) handles morphological variations by breaking words into smaller known chunks, allowing the neural network to retain and learn from grammatical information (like tense markers) rather than destroying it during preprocessing.

---

### Can You Explain This?
- [ ] I can reproduce the comparison table from memory.
- [ ] I can list two scenarios where stemming is preferred over lemmatization.
- [ ] I can explain why BERT and GPT-4 do not use stemming or lemmatization.

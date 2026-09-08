# Stemming vs Lemmatization

## 1. Direct Comparison
Both stemming and lemmatization share the same goal: mapping related words back to a common base to reduce the vocabulary size and group semantically similar concepts together (e.g., ensuring a search for "running" also finds documents containing "runs").

However, they achieve this in fundamentally different ways.

| Feature | Stemming | Lemmatization |
|---------|----------|---------------|
| **Mechanism** | Rule-based suffix stripping (string manipulation) | Dictionary lookup and morphological analysis |
| **Output** | A "stem" (often not a real word, e.g., `univers`) | A "lemma" (always a valid dictionary word, e.g., `university`) |
| **Speed** | Extremely fast | Slower (requires dictionary lookup) |
| **Context Awareness** | Blind to context | Requires POS tag context |
| **Handling Irregulars** | Fails completely (`mice` $\rightarrow$ `mic`) | Handles perfectly (`mice` $\rightarrow$ `mouse`) |

## 2. When to Use Which?

### Use Stemming When:
- **Speed is critical**: Indexing billions of documents for a search engine where absolute precision isn't required.
- **Recall is more important than Precision**: You want a search for "organize" to return documents containing "organization" and "organ" just in case they are relevant, even if some are false positives.

### Use Lemmatization When:
- **Precision is critical**: Building a high-quality chatbot or translation engine where the exact grammatical meaning of the word matters.
- **Working with Morphologically Rich Languages**: Stemming works reasonably well for English, but fails catastrophically for languages like Arabic or Turkish. Lemmatization is required for these languages.
- **Readability matters**: If you are generating text or displaying keywords to a human user, showing stems like "presum" looks broken. You must use lemmas.

## 3. Exam Preparation
### Must Memorize
- The table above comparing the two approaches.

### Likely Theory Question
**Question**: In a modern Deep Learning pipeline using Subword Tokenization (like BERT), do we still perform Stemming or Lemmatization?
**Answer**: Generally, **no**. Subword tokenization inherently handles morphological variations by splitting prefixes and suffixes into separate tokens (e.g., `running` $\rightarrow$ `run`, `##ning`). Because the deep learning model can learn the relationship between these subwords dynamically during training, explicitly forcing words into stems or lemmas beforehand destroys valuable grammatical information (like tense and number) that the neural network could have used.

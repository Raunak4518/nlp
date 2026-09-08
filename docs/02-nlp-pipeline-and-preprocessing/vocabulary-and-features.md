# Vocabulary Construction and Feature Engineering

## 1. Vocabulary Construction
After text is normalized and tokenized (covered deeply in Module 3), we are left with a list of words. Machine learning models cannot process strings; they process numbers. The first step to converting text to numbers is building a vocabulary.

### Mechanism
A **vocabulary** (often denoted as $V$) is a deterministic mapping from a known string token to an integer index.
```json
{
  "the": 0,
  "cat": 1,
  "sat": 2,
  "<UNK>": 3
}
```

### Out of Vocabulary (OOV)
Inevitably, the model will encounter words in the test set or real world that were not in the training set. We handle this using an Unknown token, often written as `<UNK>`.

## 2. Feature Engineering
Once we have a vocabulary index, we convert the documents into numerical features.

### One-Hot Encoding
Each word is a vector of size $|V|$, with a `1` at its index and `0` everywhere else.
- Very sparse.
- Cannot capture semantic meaning.

### Bag of Words (BoW) / Count Vectorization
A document is represented as the sum of its one-hot encoded words.
- *Document*: "the cat sat"
- *Vector*: `[1, 1, 1, 0]`

### TF-IDF
Term Frequency-Inverse Document Frequency. Weights words based on how frequently they appear in the document versus how rare they are across the whole corpus. (Covered extensively in Module 12).

### Word Embeddings
Dense vectors (like Word2Vec or GloVe) where vectors that are close in space represent words with similar semantic meanings.

## 3. Exam Preparation
### Must Memorize
- Vocabulary $V$ maps a string to an integer index.
- OOV words are mapped to `<UNK>`.

### Common Mistake
> [!WARNING]
> Building the vocabulary on the entire dataset (Train + Test) is a form of Data Leakage. The vocabulary must only contain words found in the Training Set.

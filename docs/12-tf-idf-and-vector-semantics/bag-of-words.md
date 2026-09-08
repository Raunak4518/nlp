# Bag of Words & Count Vectors

## 1. The Need for Vectorization
Machine learning algorithms (like Logistic Regression, SVMs, or Neural Networks) require numerical input. They cannot read the string `"The cat sat"`. We must convert text into mathematical vectors. This process is called **Vectorization**.

## 2. Bag of Words (BoW)
The simplest vectorization strategy is the **Bag of Words**. It operates on two assumptions:
1. Every word in the vocabulary gets its own dimension in the vector.
2. Grammar and word order are completely ignored (hence a "bag" of words).

If our vocabulary $V$ has 10,000 words, every document will be represented as a vector of length 10,000.

## 3. Count Vectorization
The most basic implementation of BoW is the Count Vector.
1. Define the vocabulary $V$ by extracting all unique words from the training set.
2. For each document, count how many times each word in $V$ appears.

### Example
Assume our training corpus has exactly two documents:
- $D_1$: "the cat sat on the mat"
- $D_2$: "the dog chased the cat"

**Vocabulary ($V$)**: `['the', 'cat', 'sat', 'on', 'mat', 'dog', 'chased']`

**Count Vectors**:
- $V(D_1)$: `[2, 1, 1, 1, 1, 0, 0]` (Because "the" appears twice).
- $V(D_2)$: `[2, 1, 0, 0, 0, 1, 1]`

## 4. Binary Word Features (Boolean Vectorization)
Sometimes, the frequency of a word doesn't matter; we only care if it is present or absent. In binary vectorization, the vector only contains `0`s and `1`s.
- $V(D_1)_{binary}$: `[1, 1, 1, 1, 1, 0, 0]`
- $V(D_2)_{binary}$: `[1, 1, 0, 0, 0, 1, 1]`

This is often used in Sentiment Analysis, where the mere presence of the word "terrible" is enough to classify the review as negative, regardless of whether it was said once or five times.

## 5. The Problems with Count Vectors
Count vectors have two massive flaws:
1. **Sparsity**: If $V$ has 10,000 words, a 10-word tweet will be a vector with 10 non-zero values and 9,990 zeros. This wastes massive amounts of memory.
2. **Frequency Bias**: In English, the word "the" will appear dozens of times in every document. A Count Vectorizer will give "the" the highest mathematical weight, even though "the" carries zero semantic meaning. We need a way to discount common words.

## 6. Exam Preparation
### Must Know
- BoW completely destroys syntactic structure (word order). "The dog bit the man" and "The man bit the dog" have the exact same count vector.

### Likely Practical Question
**Question**: Given $V = [apple, banana, cherry]$ and $D = "apple cherry apple"$, what is the Count Vector and what is the Binary Vector?
**Answer**: 
- Count Vector: `[2, 0, 1]`
- Binary Vector: `[1, 0, 1]`

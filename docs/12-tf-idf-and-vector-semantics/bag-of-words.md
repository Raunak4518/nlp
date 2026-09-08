# Bag of Words & Count Vectors

## 1. The Need for Vectorization
Machine learning algorithms (like Logistic Regression, SVMs, or Neural Networks) require numerical input to perform calculus and algebra. They cannot natively read the string `"The cat sat"`. We must convert raw text into mathematical vectors. This process is called **Vectorization**.

## 2. Bag of Words (BoW)
The simplest vectorization strategy in NLP is the **Bag of Words**. It operates on two foundational assumptions:
1. Every unique word in the entire vocabulary gets its own dedicated dimension in the vector space.
2. Grammar and word order are completely ignored (hence treating the document as an unstructured "bag" of words).

If our dataset vocabulary $V$ has 10,000 unique words, every single document will be mathematically represented as a massive vector of length 10,000.

---

## 3. Count Vectorization
The most basic implementation of the BoW concept is the **Count Vector**.

1. **Fit**: Define the vocabulary $V$ by extracting all unique words from the training set. Fix their alphabetical order so that Index 0 always refers to the same word.
2. **Transform**: For each document, simply count how many times each word in $V$ appears.

### Example
Assume our training corpus has exactly two documents:
- **$D_1$**: `"the cat sat on the mat"`
- **$D_2$**: `"the dog chased the cat"`

**Vocabulary ($V$)**: `['cat', 'chased', 'dog', 'mat', 'on', 'sat', 'the']` *(Alphabetized)*

**Count Vectors**:
- $V(D_1)$: `[1, 0, 0, 1, 1, 1, 2]` *(Notice the '2' at the end because "the" appears twice).*
- $V(D_2)$: `[1, 1, 1, 0, 0, 0, 2]`

---

## 4. Binary Vectorization (Boolean Vectors)
Sometimes, the *frequency* of a word doesn't matter; we only care if it is present or absent. In binary vectorization, the vector only contains `0`s and `1`s.

- $V(D_1)_{binary}$: `[1, 0, 0, 1, 1, 1, 1]`
- $V(D_2)_{binary}$: `[1, 1, 1, 0, 0, 0, 1]`

This is very frequently used in Sentiment Analysis. The mere presence of the word *"terrible"* is usually enough to classify a review as negative, regardless of whether the user said it once or five times.

---

## 5. The Fatal Flaws of Count Vectors
Count vectors suffer from two massive problems that make them unsuitable for advanced NLP:

> [!WARNING]
> **1. Memory Sparsity**
> If $V$ has 50,000 words, a 10-word tweet will be represented as a vector with 10 non-zero values and 49,990 zeros. Storing billions of these massive, mostly-empty vectors wastes huge amounts of RAM.

> [!WARNING]
> **2. Frequency Bias**
> In English, structural words like "the", "a", and "of" will appear dozens of times in every document. A Count Vectorizer will give "the" the highest mathematical weight, causing the machine learning model to focus on it, even though "the" carries zero semantic meaning regarding the topic of the text. We need a way to mathematically punish common words.

---

## 6. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: Define the Bag of Words (BoW) assumption. Provide one concrete example of how this assumption causes the model to lose critical linguistic information.
> **Answer**: The Bag of Words assumption states that a document can be represented purely by the frequency of the words it contains, completely ignoring grammar, syntax, and word order. 
> 
> Because word order is destroyed, BoW loses critical semantic relationships. For example, the sentence *"The dog bit the man"* and *"The man bit the dog"* have the exact same vocabulary counts. A BoW model will represent them as the exact same mathematical vector, completely failing to understand who was the attacker and who was the victim.

**3-Mark Question**: Given the vocabulary $V = [apple, banana, cherry]$ and the document $D = "apple cherry apple"$, write out both the Count Vector and the Binary Vector.
> **Answer**: 
> - Count Vector: `[2, 0, 1]`
> - Binary Vector: `[1, 0, 1]`

---

### Can You Explain This?
- [ ] I can define Vectorization.
- [ ] I understand why Count Vectors result in highly sparse data structures.
- [ ] I understand why Count Vectors fail to capture the true semantic importance of words.

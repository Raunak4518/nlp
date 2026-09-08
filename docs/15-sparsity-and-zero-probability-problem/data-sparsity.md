# Data Sparsity and Vocabulary Explosion

## 1. The Vocabulary Explosion
In the previous module, we learned that an N-gram Language Model calculates probabilities based on how many times a sequence of words appeared in the training data.

Let's look at the mathematical scale of this. Assume we have a very small, toy vocabulary ($V$) of exactly 10,000 unique words.

- **Unigrams**: There are $|V| = 10,000$ possible unigrams.
- **Bigrams**: There are $|V|^2 = 100,000,000$ possible bigrams (e.g., every word followed by every other word).
- **Trigrams**: There are $|V|^3 = 1,000,000,000,000$ (one trillion) possible trigrams.

If we want to build a Trigram Language Model, we conceptually need to create a matrix with one trillion cells to hold the counts of every possible 3-word sequence.

## 2. Data Sparsity
**Data Sparsity** refers to the fact that the vast majority of mathematically possible combinations never actually occur in real life.

Even if we trained our model on the entire text of Wikipedia (which has about 3 billion words), we could only ever observe, at maximum, 3 billion trigrams. 

This means that out of our 1,000,000,000,000 possible trigrams, at least 997,000,000,000 of them will have a count of exactly **zero** in our training data. Our count matrix is incredibly "sparse" (mostly zeros).

## 3. Sparse Count Tables
Because of this sparsity, we cannot store N-gram models as dense multi-dimensional arrays (like a standard NumPy array). A dense array of 1 trillion integers would require terabytes of RAM.

Instead, N-gram counts are stored in **Sparse Hash Maps** (like Python nested dictionaries). We only store the n-grams that actually appeared; if an n-gram is not in the dictionary, we assume its count is 0.

## 4. Exam Preparation
### Must Memorize
- The number of *possible* n-grams given a vocabulary size $|V|$ is $|V|^n$.

### Likely Theory Question
**Question**: Why is data sparsity considered the primary limiting factor for building 5-gram or 6-gram classical language models?
**Answer**: As $n$ increases, the number of possible word combinations grows exponentially ($|V|^n$). No matter how large the training corpus is, the overwhelming majority of grammatically valid 5-grams will never appear in the text, leaving the model with no data to estimate their probabilities.

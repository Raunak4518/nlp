# Laplace Smoothing (Add-One)

## 1. What is Laplace Smoothing?
Laplace Smoothing (also called Add-One smoothing) is the simplest technique to solve the Zero-Probability problem in N-gram models. 

The core idea is incredibly simple: **pretend that every possible n-gram occurred exactly one more time than it actually did.**

## 2. The Laplace Formula
Let's look at the standard Maximum Likelihood Estimation (MLE) formula for a bigram $P(w_i | w_{i-1})$:
$$ P_{MLE} = \frac{\text{Count}(w_{i-1}, w_i)}{\text{Count}(w_{i-1})} $$

To apply Laplace smoothing, we simply add $1$ to the numerator (the count of the specific bigram).
$$ P_{Laplace} = \frac{\text{Count}(w_{i-1}, w_i) + 1}{\text{Denominator}} $$

## 3. Why the Denominator becomes $+V$
Because we added $1$ to the numerator of *every single possible* next word, our probabilities will no longer sum to $1.0$ if we keep the old denominator. 

Let $V$ be the Vocabulary (the set of all unique words). There are $|V|$ possible next words. Since we added $1$ to each of them, we have added a total of $|V|$ fake counts to the system for the context $w_{i-1}$. 

To mathematically balance this and ensure all probabilities still sum to $1.0$, we must add $|V|$ to the denominator.

$$ P_{Laplace}(w_i | w_{i-1}) = \frac{\text{Count}(w_{i-1}, w_i) + 1}{\text{Count}(w_{i-1}) + |V|} $$

## 4. How it affects Probabilities

### Unseen Events
If a bigram never occurred, its original count is $0$.
$$ P_{MLE}(\text{unseen}) = \frac{0}{\text{Count}} = 0.0 $$
$$ P_{Laplace}(\text{unseen}) = \frac{0 + 1}{\text{Count} + |V|} > 0.0 $$
The unseen bigram now has a small, non-zero probability! The sentence probability calculation will no longer collapse.

### Seen Events
If a bigram occurred $100$ times, its probability is actually *reduced*. We "stole" probability mass from the seen events to give to the unseen events.

## 5. Limitations of Laplace Smoothing
While it solves the math error, Laplace smoothing is conceptually terrible for NLP.
Because the vocabulary $V$ is often huge (e.g., $50,000$ words), adding $1$ to every single unseen combination introduces massive amounts of "fake" data into the model. In a sparse dataset, the denominator becomes heavily inflated, crushing the probabilities of valid, highly-frequent words and giving way too much weight to nonsense combinations.

## 6. Scratch Implementation
```python
def laplace_smoothing(bigram_count: int, context_count: int, vocab_size: int) -> float:
    # Adding 1 to the specific bigram, and V to the context total
    return (bigram_count + 1) / (context_count + vocab_size)

# --- Trace ---
V = 10000 # 10,000 words in vocabulary
count_the = 500
count_the_cat = 20
count_the_xylophone = 0

# Normal MLE
mle_cat = count_the_cat / count_the
mle_xylo = count_the_xylophone / count_the

# Laplace
lap_cat = laplace_smoothing(count_the_cat, count_the, V)
lap_xylo = laplace_smoothing(count_the_xylophone, count_the, V)

print(f"MLE Cat: {mle_cat:.4f} | Laplace Cat: {lap_cat:.4f}")
print(f"MLE Xylo: {mle_xylo:.4f} | Laplace Xylo: {lap_xylo:.4f}")

# Output:
# MLE Cat: 0.0400 | Laplace Cat: 0.0020
# MLE Xylo: 0.0000 | Laplace Xylo: 0.0001
# (Notice how heavily "the cat" was penalized to make room for the unseen words).
```

## 7. Exam Preparation
### Must Memorize
- The Laplace formula: $\frac{Count + 1}{ContextCount + |V|}$.
- The $+V$ in the denominator is strictly the size of the vocabulary, NOT the total number of words in the corpus.

### Likely Theory Question
**Question**: Why is it mathematically necessary to add $|V|$ to the denominator in Laplace smoothing?
**Answer**: Because we added a fake count of $1$ to every possible next word in the vocabulary $V$. To ensure that the sum of the probabilities of all possible next words still perfectly equals $1.0$, the denominator must account for all $|V|$ fake counts we injected into the numerator.

# Add-k Smoothing

## 1. What is Add-k Smoothing?
Because Laplace Smoothing (+1) steals far too much probability mass from seen words when the vocabulary is large, Add-k smoothing (sometimes called Add-alpha smoothing) generalizes the approach. 

Instead of pretending every unseen word occurred exactly $1$ time, we pretend it occurred a fractional amount, $k$ times (where $0 < k < 1$).

## 2. The Add-k Formula
For a bigram:
$$ P_{Add-k}(w_i | w_{i-1}) = \frac{\text{Count}(w_{i-1}, w_i) + k}{\text{Count}(w_{i-1}) + (k \times |V|)} $$

- If $k = 1$, this is standard Laplace smoothing.
- If $k = 0$, this is standard MLE (no smoothing).
- Typical values for $k$ are $0.01$, $0.05$, or $0.1$.

By adding a tiny fraction instead of a whole $1$, we still solve the zero-probability problem without destroying the true probability distribution.

## 3. Choosing the right 'k'
$k$ is a **Hyperparameter**. The algorithm cannot learn $k$ from the training data, because evaluating $k$ on the training data will always suggest $k=0$ (the training data fits the training data perfectly).

### Grid Search and Validation Sets
To find the best $k$, we use a separate dataset called a **Validation Set** (or Dev Set/Held-out data).
1. We train our language model (calculate the counts) on the Training Set.
2. We evaluate the model's accuracy on the Validation Set using various values of $k$ (e.g., $k=0.1, 0.5, 1.0$). This is called a **Grid Search**.
3. We select the $k$ that yields the highest probability (or lowest Perplexity) on the Validation Set.
4. We report our final results on a purely unseen Test Set.

## 4. Scratch Implementation & Numerical Problem
```python
def add_k_smoothing(bigram_count: int, context_count: int, vocab_size: int, k: float) -> float:
    return (bigram_count + k) / (context_count + (k * vocab_size))

# --- Numerical Problem Walkthrough ---
# Corpus:
# "i like apples"
# "i like bananas"
# "she likes apples"
# 
# Vocab V = {i, like, likes, apples, bananas, she} -> |V| = 6
V = 6

# We want P("cars" | "like"). "cars" is OOV, so it is an unseen unigram mapped to <UNK>.
# Let's assume V includes <UNK>, so V = 7.
V = 7

count_like = 2
count_like_cars = 0

# Try different k values
print(f"k=1.00: {add_k_smoothing(count_like_cars, count_like, V, 1.0):.4f}")
print(f"k=0.10: {add_k_smoothing(count_like_cars, count_like, V, 0.1):.4f}")
print(f"k=0.01: {add_k_smoothing(count_like_cars, count_like, V, 0.01):.4f}")

# Output:
# k=1.00: 0.1111  (1 / 9)
# k=0.10: 0.0370  (0.1 / 2.7)
# k=0.01: 0.0048  (0.01 / 2.07)
```
*(Notice how much smaller the probability is for $k=0.01$. This preserves the real probabilities of the seen words much better).*

## 5. Exam Preparation
### Must Memorize
- The Add-k formula: $\frac{Count + k}{ContextCount + k|V|}$.
- Hyperparameters like $k$ must be tuned on a **Validation Set**, never the Test Set or Training Set.

### Likely Practical Question
**Question**: You have a vocabulary size of $100$. The word "data" appears $50$ times. The bigram "data science" appears $10$ times. Calculate $P(\text{"science"} | \text{"data"})$ using Add-k smoothing where $k = 0.5$.
**Answer**:
- Numerator: $\text{Count("data science")} + k = 10 + 0.5 = 10.5$
- Denominator: $\text{Count("data")} + k|V| = 50 + (0.5 \times 100) = 50 + 50 = 100$
- $P(\text{"science"} | \text{"data"}) = 10.5 / 100 = 0.105$

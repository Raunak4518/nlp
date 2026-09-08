# Add-k Smoothing

## 1. What is Add-k Smoothing?
Because standard Laplace Smoothing (+1) is far too aggressive and steals way too much probability mass from seen words when the vocabulary is large, **Add-k smoothing** (sometimes called *Add-alpha smoothing*) was invented to generalize and soften the approach. 

Instead of mathematically pretending every unseen word occurred exactly $1$ whole time, we pretend it occurred a tiny fractional amount, **$k$** times (where $0 < k < 1$).

---

## 2. The Add-k Formula
For a bigram probability:
$$ P_{Add-k}(w_i \mid w_{i-1}) = \frac{\text{Count}(w_{i-1}, w_i) + \mathbf{k}}{\text{Count}(w_{i-1}) + (\mathbf{k} \times |V|)} $$

- If **$k = 1.0$**, this formula simplifies back to standard Laplace Add-1 smoothing.
- If **$k = 0.0$**, this formula simplifies back to raw Maximum Likelihood Estimation (no smoothing).
- Typical real-world values for $k$ are very small, such as $0.01$, $0.05$, or $0.001$.

By adding a tiny fractional count to the numerator instead of a whole $1$, we successfully solve the zero-probability mathematical crash without radically altering the true underlying probability distribution of the highly frequent words.

---

## 3. Choosing the right 'k'
$k$ is a **Hyperparameter**. A hyperparameter is a setting that controls the behavior of the algorithm but cannot be automatically learned by the algorithm from the training data itself. (If you ask the algorithm to evaluate the "best" $k$ based on the Training Data, it will always stubbornly suggest $k=0$, because the unsmoothed training data perfectly predicts itself).

### Grid Search and Validation Sets
To find the optimal value of $k$ without cheating, we use a separate, held-out dataset called a **Validation Set** (or Dev Set).

1. **Train**: We calculate our raw N-gram counts on the core Training Set.
2. **Search**: We mathematically evaluate the model's accuracy (or Perplexity) on the Validation Set using various manual values of $k$ (e.g., trying $k=0.1, 0.5, 0.01$). Trying multiple hyperparameters like this is called a **Grid Search**.
3. **Select**: We select the specific value of $k$ that yields the highest probability / best accuracy on the Validation Set.
4. **Test**: We report our final academic results on a purely unseen Test Set to prove the model generalizes.

---

## 4. Scratch Implementation & Trace

```python
def add_k_smoothing(bigram_count: int, context_count: int, vocab_size: int, k: float) -> float:
    """Calculates smoothed probability using fractional k."""
    # Add k to the numerator, and k * |V| to the denominator
    return (bigram_count + k) / (context_count + (k * vocab_size))
```

??? question "Trace the Math"
    ```python
    # Corpus:
    # "i like apples"
    # "i like bananas"
    # "she likes apples"
    
    # Vocab V = {i, like, likes, apples, bananas, she, <UNK>} -> |V| = 7
    V = 7
    
    # We want to calculate the probability of the user typing the phrase "I like cars".
    # "cars" is Out-Of-Vocabulary, so it maps to <UNK>.
    # Therefore we are mathematically calculating P(<UNK> | like).
    
    count_like = 2
    count_like_unk = 0 # Unseen
    
    # Let's try different k hyperparameters
    print(f"k=1.00: {add_k_smoothing(count_like_unk, count_like, V, 1.0):.4f}")
    print(f"k=0.10: {add_k_smoothing(count_like_unk, count_like, V, 0.1):.4f}")
    print(f"k=0.01: {add_k_smoothing(count_like_unk, count_like, V, 0.01):.4f}")
    
    # Output:
    # k=1.00: 0.1111  (Formula: 1 / 9)
    # k=0.10: 0.0370  (Formula: 0.1 / 2.7)
    # k=0.01: 0.0048  (Formula: 0.01 / 2.07)
    
    # Notice how much smaller and more realistic the probability is for k=0.01. 
    # This prevents the unseen word from overpowering the words we actually saw.
    ```

---

## 5. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: You have a calculated vocabulary size of exactly $100$ words. The unigram "data" appears $50$ times in your training corpus. The bigram "data science" appears $10$ times. 
Calculate the Add-k smoothed probability of $P(\text{"science"} \mid \text{"data"})$ assuming the hyperparameter $k = 0.5$. Show your formula and work.
> **Answer**:
> **Formula**: $P_{Add-k}(w_i \mid w_{i-1}) = \frac{\text{Count}(w_{i-1}, w_i) + k}{\text{Count}(w_{i-1}) + (k \times |V|)}$
> 
> **Variables**: $|V| = 100$, $\text{Count("data")} = 50$, $\text{Count("data science")} = 10$, $k = 0.5$
> 
> 1. Numerator: $\text{Count("data science")} + k = 10 + 0.5 = 10.5$
> 2. Denominator: $\text{Count("data")} + (k \times |V|) = 50 + (0.5 \times 100) = 50 + 50 = 100$
> 3. $P(\text{"science"} \mid \text{"data"}) = \frac{10.5}{100} = 0.105$

**2-Mark Question**: Why must we use a Validation Set to tune the hyperparameter $k$, rather than tuning it on the Training Set?
> **Answer**: The value of $k$ cannot be learned directly from the Training Set because the unsmoothed Training Set perfectly predicts itself. If we attempted to optimize $k$ for maximum probability on the Training Set, the math would strictly dictate $k=0$ (raw MLE) every time. We must use a held-out Validation Set to accurately simulate how the model behaves when encountering unseen data.

---

### Can You Explain This?
- [ ] I can write the Add-k formula from memory.
- [ ] I can explain why $k|V|$ is added to the denominator.
- [ ] I can define what a Hyperparameter is.
- [ ] I can explain the conceptual role of a Validation Set.

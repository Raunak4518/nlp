# Interpolated and Recursive Kneser-Ney

## 1. Interpolated Kneser-Ney
In the previous section, we showed the mathematical formula for Bigram Kneser-Ney. That specific formula represents the **Interpolated** version of Kneser-Ney. 

Unlike strict Backoff (which completely discards the highest-order model if its count is 0 and only uses the lower-order model), Interpolated Kneser-Ney mathematically *always* mixes the discounted higher-order probability with the lower-order Continuation Probability simultaneously. 

$$ P_{KN}(w_i \mid w_{i-1}) = \frac{\max(c(w_{i-1}, w_i) - d, 0)}{c(w_{i-1})} + \lambda(w_{i-1}) P_{CONTINUATION}(w_i) $$

If the bigram count is mathematically exactly $0$, the first term automatically evaluates to $0.0$, and the formula seamlessly and elegantly "backs off" entirely to the Continuation term without needing a clunky `if/else` statement. If the bigram count is $>0$, both terms are mathematically active. This mathematically guarantees much smoother and more accurate overall probability distributions.

---

## 2. Recursive Kneser-Ney (Higher-Order Models)
What if we want to build a Trigram, 4-gram, or 5-gram Kneser-Ney model? 
We define the Kneser-Ney mathematical function **recursively**.

Let $N$ be the strict order of the model (e.g., $N=3$ for a Trigram model).
- The absolute **highest-order model** ($N$) strictly uses standard, raw empirical text counts and standard Absolute Discounting.
- Every single **lower-order model** ($N-1, N-2, \dots, 1$) below it does *not* use raw text counts; they all use Continuation Counts instead!

### The Recursive Formula
For a sequence of words $w_{i-n+1}^{i} = w_{i-n+1}, \dots, w_i$:

$$ P_{KN}(w_i \mid w_{i-n+1}^{i-1}) = \frac{\max(c_{KN}(w_{i-n+1}^{i}) - d, 0)}{c_{KN}(w_{i-n+1}^{i-1})} + \lambda(w_{i-n+1}^{i-1}) P_{KN}(w_i \mid w_{i-n+2}^{i-1}) $$

Where the specialized count function $c_{KN}$ is defined mathematically as:
- **If evaluating the highest order:** $c_{KN}$ is the actual raw empirical number of times the sequence appeared in the training text.
- **If evaluating a lower order:** $c_{KN}$ is the **Continuation Count** (the number of unique word types that historically precede the sequence).

---

## 3. Why it is the Classical State-of-the-Art
Interpolated Recursive Kneser-Ney with Absolute Discounting is widely considered by researchers to be the absolute mathematical pinnacle of classical statistical NLP. 

Before the invention of massive Neural Language Models (like RNNs and Transformers) disrupted the field, Kneser-Ney consistently achieved the lowest Perplexity scores on almost every standardized dataset in the world. It is the only classical algorithm that perfectly mathematically balances raw empirical frequencies with rigorous context-diversity fallbacks.

---

## 4. Scratch Implementation (Interpolated Bigram KN)

```python
def kneser_ney_bigram(w1: str, w2: str, 
                      bigram_counts: dict, unigram_counts: dict, 
                      total_bigram_types: int, d: float = 0.75) -> float:
    """Calculates Interpolated Bigram Kneser-Ney Probability."""
    
    # 1. Absolute Discounted highest-order count
    c_w1_w2 = bigram_counts.get((w1, w2), 0)
    discounted_term = max(c_w1_w2 - d, 0) / unigram_counts[w1]
    
    # 2. Calculate Lambda (Normalizer weight)
    # How many unique word types historically follow w1?
    types_following_w1 = sum(1 for (a, b) in bigram_counts.keys() if a == w1)
    lambda_w1 = (d / unigram_counts[w1]) * types_following_w1
    
    # 3. Continuation Probability for w2 (The core KN innovation)
    # How many unique word types historically precede w2?
    types_preceding_w2 = sum(1 for (a, b) in bigram_counts.keys() if b == w2)
    p_continuation = types_preceding_w2 / total_bigram_types
    
    # 4. Interpolate and return the mathematically pure probability
    return discounted_term + (lambda_w1 * p_continuation)
```

---

## 5. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: In Recursive Kneser-Ney for a Trigram model, when calculating the probability at the Bigram and Unigram backoff levels, do you ever use the raw token count of the Bigram/Unigram from the text? Why or why not?
> **Answer**: No. In Recursive Kneser-Ney, only the absolute highest-order model (the Trigram) uses actual raw empirical token counts extracted from the text. When recursively falling back to the lower-order models (the Bigram and Unigram levels), the algorithm strictly replaces raw token frequency with the **Continuation Count** (the number of unique preceding contexts). 
> 
> This is done to prevent high-frequency but low-diversity words (like "Francisco") from artificially inflating the backoff probability, ensuring the model prioritizes words with high context diversity when evaluating unseen phrases.

**2-Mark Question**: Explain how Interpolated Kneser-Ney seamlessly transitions to backoff without requiring an explicit `if/else` statement.
> **Answer**: The Interpolated Kneser-Ney formula is a mathematically unified equation containing two terms added together. The first term incorporates the absolute discounted highest-order count ($\max(c - d, 0)$). If the specific higher-order sequence was completely unseen, its count $c$ is exactly $0$, meaning the entire first term mathematically evaluates to $0.0$. The equation therefore gracefully simplifies to solely returning the normalized Continuation Probability (the second term), perfectly replicating a backoff fallback purely through arithmetic.

---

### Can You Explain This?
- [ ] I can explicitly define the mathematical difference between $c_{KN}$ at the highest order vs. lower orders.
- [ ] I can trace the Python implementation of Bigram Kneser-Ney.
- [ ] I can explain why Kneser-Ney is considered the state-of-the-art classical smoothing algorithm.

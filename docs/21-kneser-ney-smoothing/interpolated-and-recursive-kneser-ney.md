# Interpolated and Recursive Kneser-Ney

## 1. Interpolated Kneser-Ney
In the previous section, we showed the formula for Bigram Kneser-Ney. That formula is an **Interpolated** version of Kneser-Ney. 

Unlike strict backoff (which only uses the lower-order model if the higher-order count is 0), Interpolated Kneser-Ney *always* mixes the discounted higher-order probability with the lower-order Continuation Probability. 

$$ P_{KN}(w_i | w_{i-1}) = \frac{\max(c(w_{i-1}, w_i) - d, 0)}{c(w_{i-1})} + \lambda(w_{i-1}) P_{CONTINUATION}(w_i) $$

If the bigram count is 0, the first term becomes $0.0$, and it seamlessly "backs off" entirely to the Continuation term. If the bigram count is $>0$, both terms are active. This guarantees smoother probability distributions.

## 2. Recursive Kneser-Ney (Higher-Order)
What if we want to build a Trigram or 4-gram Kneser-Ney model? 
We define the Kneser-Ney function **recursively**.

Let $N$ be the order of the model (e.g., $N=3$ for Trigram).
The highest-order model ($N$) uses standard raw counts and absolute discounting.
Every lower-order model ($N-1, N-2, ... 1$) does *not* use raw counts; they all use Continuation Counts!

### The Recursive Formula
For a sequence of words $w_{i-n+1}^{i} = w_{i-n+1}, ..., w_i$:

$$ P_{KN}(w_i | w_{i-n+1}^{i-1}) = \frac{\max(c_{KN}(w_{i-n+1}^{i}) - d, 0)}{c_{KN}(w_{i-n+1}^{i-1})} + \lambda(w_{i-n+1}^{i-1}) P_{KN}(w_i | w_{i-n+2}^{i-1}) $$

Where the count function $c_{KN}$ is defined as:
- **If it is the highest order:** $c_{KN}$ is the actual number of times the sequence appeared in the text.
- **If it is a lower order:** $c_{KN}$ is the **Continuation Count** (the number of unique words that precede the sequence).

## 3. Why it is the State-of-the-Art
Interpolated Recursive Kneser-Ney with Absolute Discounting is widely considered the absolute pinnacle of classical statistical NLP. 
Before the invention of Neural Language Models (RNNs and Transformers), Kneser-Ney consistently achieved the lowest perplexity on almost every dataset in the world. It perfectly balances raw empirical frequencies with context-diversity fallbacks.

## 4. Scratch Implementation (Interpolated Bigram KN)
```python
def kneser_ney_bigram(w1: str, w2: str, bigram_counts: dict, unigram_counts: dict, total_bigram_types: int, d: float = 0.75) -> float:
    # 1. Absolute Discounted highest-order count
    c_w1_w2 = bigram_counts.get((w1, w2), 0)
    discounted_term = max(c_w1_w2 - d, 0) / unigram_counts[w1]
    
    # 2. Calculate Lambda (Normalizer weight)
    # How many unique words follow w1?
    types_following_w1 = sum(1 for (a, b) in bigram_counts.keys() if a == w1)
    lambda_w1 = (d / unigram_counts[w1]) * types_following_w1
    
    # 3. Continuation Probability for w2
    # How many unique words precede w2?
    types_preceding_w2 = sum(1 for (a, b) in bigram_counts.keys() if b == w2)
    p_continuation = types_preceding_w2 / total_bigram_types
    
    # 4. Interpolate
    return discounted_term + (lambda_w1 * p_continuation)
```

## 5. Exam Preparation
### Must Memorize
- Highest-order KN models use raw text counts. Lower-order backoff KN models use continuation counts.
- Interpolated Kneser-Ney is considered the most accurate classical smoothing algorithm.

### Likely Theory Question
**Question**: In Recursive Kneser-Ney for a Trigram model, when calculating the backoff probability for the Bigram level, do you use the raw count of the Bigram?
**Answer**: No. In Recursive Kneser-Ney, only the highest-order model (the Trigram) uses actual raw counts from the text. When backing off to the lower-order models (the Bigram and Unigram), the algorithm uses the Continuation Count (the number of unique preceding contexts) rather than the raw token frequency.

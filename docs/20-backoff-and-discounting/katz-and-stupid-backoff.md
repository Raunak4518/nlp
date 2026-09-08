# Katz and Stupid Backoff

## 1. Katz Backoff
**Katz Backoff** is the formal algorithm that combines Good-Turing discounting with the Backoff concept.

It relies on two components:
1. **Discounted Probability ($P^*$):** For seen N-grams, we do not use MLE. We use a discounted probability (usually calculated via Good-Turing or Absolute Discounting) to ensure probability mass is saved.
2. **Backoff Weight ($\alpha$):** For unseen N-grams, we back off to the $N-1$ gram model. But we cannot just use the raw $N-1$ probability. We must multiply it by a backoff weight $\alpha$ to ensure the final probabilities sum exactly to 1.0.

### The Algorithm (Simplified Bigram)
To calculate $P_{Katz}(w_i | w_{i-1})$:
- **If $\text{Count}(w_{i-1}, w_i) > 0$:**
  Return the discounted probability $P^*(w_i | w_{i-1})$.
- **If $\text{Count}(w_{i-1}, w_i) == 0$:**
  Return $\alpha(w_{i-1}) \times P_{Katz}(w_i)$.

*(Where $\alpha(w_{i-1})$ is the exact amount of "leftover" probability mass from the context $w_{i-1}$, divided by the total unigram probabilities of all the unseen words).*

## 2. Stupid Backoff
Katz Backoff is mathematically pure, ensuring everything sums to 1.0. However, calculating the exact $\alpha$ weights for every single context in a trillion-word corpus is computationally exhausting.

In 2007, Google researchers (Brants et al.) introduced **Stupid Backoff**, named because it is so simple it seems stupid, yet it performs almost identically to Katz Backoff on massive datasets.

### The Algorithm
There is no discounting. There are no $\alpha$ weights.
1. Check the Trigram. If count > 0, return the raw MLE probability.
2. If count == 0, back off to the Bigram, but multiply the Bigram MLE by a fixed penalty score (usually $0.4$).
3. If Bigram count == 0, back off to Unigram, multiplying by $0.4$ again.

$$ S(w_i | w_{i-2}, w_{i-1}) = \begin{cases} \frac{\text{Count}(w_{i-2}, w_{i-1}, w_i)}{\text{Count}(w_{i-2}, w_{i-1})} & \text{if } \text{Count} > 0 \\ 0.4 \times S(w_i | w_{i-1}) & \text{otherwise} \end{cases} $$

### Why it's "Stupid"
Because it uses raw MLEs and fixed penalties, the scores returned by Stupid Backoff **do not sum to 1.0**. They are not valid mathematical probabilities. They are just relative scores. However, for the task of Next-Word Prediction (where we just use `argmax` to find the highest score), it doesn't matter if the scores sum to 1.0.

## 3. Scratch Implementation (Stupid Backoff)
```python
def stupid_backoff_trigram(w1: str, w2: str, w3: str, trigram_counts: dict, bigram_counts: dict, unigram_counts: dict, corpus_size: int, penalty: float = 0.4) -> float:
    # 1. Try Trigram
    count_123 = trigram_counts.get((w1, w2, w3), 0)
    if count_123 > 0:
        return count_123 / bigram_counts[(w1, w2)]
        
    # 2. Try Bigram (Backed off)
    count_23 = bigram_counts.get((w2, w3), 0)
    if count_23 > 0:
        return penalty * (count_23 / unigram_counts[w2])
        
    # 3. Try Unigram (Backed off twice)
    count_3 = unigram_counts.get(w3, 0)
    if count_3 > 0:
        return (penalty * penalty) * (count_3 / corpus_size)
        
    # 4. Total failure (OOV word)
    return 0.0

# Example usage conceptually:
# score = stupid_backoff_trigram("i", "am", "sam", trigrams, bigrams, unigrams, 1000)
```

## 4. Exam Preparation
### Must Memorize
- Katz Backoff calculates exact $\alpha$ weights to ensure probabilities sum to 1.0.
- Stupid Backoff uses a fixed penalty (0.4) and does not produce valid probabilities (they do not sum to 1.0).

### Likely Theory Question
**Question**: Why is Stupid Backoff preferred over Katz Backoff for web-scale datasets (like training on the entire internet)?
**Answer**: Katz Backoff requires calculating precise discount amounts and normalizer weights ($\alpha$) for every single context in the dataset, which requires massive memory and computation time. Stupid Backoff avoids this entirely by using a fixed 0.4 penalty. While Stupid Backoff does not output true probabilities, its relative ranking of words is highly accurate on massive datasets, making it vastly more efficient for tasks like machine translation or autocomplete.

# Linear Interpolation

## 1. The Problem with Trigrams
Trigram models generate much better text than Unigram models because they have more context. However, Trigrams suffer massively from Data Sparsity. If a specific 3-word sequence never appeared in the training data, its probability is 0 (or heavily penalized by Laplace Smoothing).

Meanwhile, Unigram models are terrible at generating coherent text, but they almost never suffer from Data Sparsity (because almost every individual word will appear at least once).

**Interpolation** is the mathematical technique of combining multiple models together to get the best of both worlds: the high accuracy of Trigrams, supported by the robust fallback of Bigrams and Unigrams.

## 2. Linear Interpolation Formula
To calculate the probability of the next word using Linear Interpolation, we calculate the MLE probabilities from the Unigram, Bigram, and Trigram models separately, and then take a weighted average of them.

$$ P_{Interpolated}(w_n | w_{n-2}, w_{n-1}) = \lambda_1 P_{MLE}(w_n) + \lambda_2 P_{MLE}(w_n | w_{n-1}) + \lambda_3 P_{MLE}(w_n | w_{n-2}, w_{n-1}) $$

### The Lambda Weights ($\lambda$)
The weights $\lambda_1, \lambda_2, \lambda_3$ represent how much we "trust" each model. 
Because we are mixing probabilities, the weights must perfectly sum to 1.0 to ensure the final result remains a valid probability distribution.

$$ \lambda_1 + \lambda_2 + \lambda_3 = 1.0 $$

## 3. Fixed Interpolation
The simplest way to implement this is **Fixed Interpolation**, where the engineer manually hardcodes the weights.
For example, we might strongly trust the Trigram, somewhat trust the Bigram, and barely trust the Unigram:
- $\lambda_3 = 0.7$ (Trigram weight)
- $\lambda_2 = 0.2$ (Bigram weight)
- $\lambda_1 = 0.1$ (Unigram weight)

If the Trigram MLE returns $0.0$ because the sequence is unseen, the formula will still return a non-zero probability because the Bigram and Unigram models will likely return $>0.0$, multiplied by their respective $\lambda$ weights.

## 4. Interpolation vs Backoff
Interpolation is often compared to a similar technique called **Backoff** (specifically Katz Backoff).
- **Interpolation** *always* calculates and mixes all three models (Unigram, Bigram, Trigram) for every single prediction.
- **Backoff** only uses the Trigram model. If (and only if) the Trigram count is exactly 0, it *backs off* to the Bigram model. If the Bigram count is 0, it *backs off* to the Unigram model. 

Interpolation is generally preferred in modern systems because it is mathematically cleaner and often yields better perplexity scores.

## 5. Exam Preparation
### Must Memorize
- The interpolation formula is a weighted sum of MLEs: $\lambda_1 P_1 + \lambda_2 P_2 + \lambda_3 P_3$.
- $\sum \lambda = 1.0$.

### Likely Theory Question
**Question**: Why does Linear Interpolation help solve the Zero-Probability problem for Trigram models without needing to add fake counts like Laplace Smoothing?
**Answer**: Because even if a specific Trigram has a count of 0 (yielding $P_{MLE} = 0.0$), the Unigram and Bigram MLE components of the interpolation equation will almost certainly be greater than 0. The weighted sum will therefore be greater than 0, preventing the sentence probability from collapsing, entirely bypassing the need for artificial +1 counts.

# Linear Interpolation

## 1. The Problem with Pure Trigrams
Trigram models generate significantly better, more coherent text than Unigram or Bigram models because they utilize a longer context window. However, Trigrams suffer massively from **Data Sparsity**. If a specific 3-word sequence never happened to appear in the training data, its probability drops to exactly $0.0$. 

If we try to fix this with Laplace Add-1 Smoothing, we end up severely distorting the true mathematical probability of highly common words because the vocabulary size $|V|$ is added to every denominator.

Meanwhile, Unigram models are terrible at generating coherent text (they just spit out the most common words randomly), but they almost *never* suffer from Data Sparsity, because almost every individual word will appear at least once in the training corpus.

**Interpolation** is the mathematical technique of dynamically combining multiple different models together to get the best of both worlds: the high accuracy of Trigrams, supported by the robust, non-zero safety net of Bigrams and Unigrams.

---

## 2. Linear Interpolation Formula
To calculate the probability of the next word using Linear Interpolation, we calculate the raw MLE probabilities from the Unigram, Bigram, and Trigram models separately, and then take a **weighted average** of all three.

$$ P_{Interpolated}(w_n \mid w_{n-2}, w_{n-1}) = \lambda_1 P_{MLE}(w_n) + \lambda_2 P_{MLE}(w_n \mid w_{n-1}) + \lambda_3 P_{MLE}(w_n \mid w_{n-2}, w_{n-1}) $$

### The Lambda Weights ($\lambda$)
The weights $\lambda_1, \lambda_2, \text{ and } \lambda_3$ represent how much mathematical "trust" we place in each respective model. 

> [!IMPORTANT]
> Because we are mathematically mixing independent probability distributions, the sum of all weights must perfectly equal exactly $1.0$ to ensure the final result remains a mathematically valid probability distribution (no numbers over 1.0).
> $$ \lambda_1 + \lambda_2 + \lambda_3 = 1.0 $$

---

## 3. Fixed Interpolation Example
The simplest way to implement this is **Fixed Interpolation**, where the engineer manually hardcodes the weights as static hyperparameters.

For example, we might strongly trust the Trigram (because it has the most context), somewhat trust the Bigram, and barely trust the Unigram (only relying on it if absolutely necessary):
- **$\lambda_3 = 0.7$** (Trigram weight)
- **$\lambda_2 = 0.2$** (Bigram weight)
- **$\lambda_1 = 0.1$** (Unigram weight)

If the Trigram MLE returns exactly $0.0$ because the sequence is unseen, the formula will still return a non-zero probability because the Bigram and Unigram models will likely return $>0.0$. These non-zero values will be multiplied by their respective $\lambda$ weights and added to the total, saving the sentence from collapsing to $0.0$.

---

## 4. Interpolation vs. Backoff
Interpolation is frequently compared to a competing classical technique called **Backoff** (specifically Katz Backoff). It is critical to understand the mechanical difference:

- **Interpolation** *always* calculates and mixes the math from all three models (Unigram, Bigram, Trigram) simultaneously for every single prediction.
- **Backoff** acts like an `if/else` statement. It only calculates the Trigram model. If (and *only* if) the Trigram count is exactly 0, it entirely abandons the Trigram and *backs off* to the Bigram model. If the Bigram count is 0, it *backs off* to the Unigram model. 

Interpolation is generally preferred in modern systems because mixing probabilities is mathematically cleaner and generally yields better Perplexity scores than hard threshold backoffs.

---

## 5. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: You are given the following raw MLE probabilities for predicting the word "dog": 
Unigram $P(\text{"dog"}) = 0.10$, Bigram $P(\text{"dog"} \mid \text{"the"}) = 0.20$, Trigram $P(\text{"dog"} \mid \text{"saw the"}) = 0.0$. 
Using Fixed Linear Interpolation with weights $\lambda_1=0.1, \lambda_2=0.3, \lambda_3=0.6$, calculate the interpolated probability. Does this solve the zero-probability problem? Explain why.
> **Answer**: 
> 1. Formula: $P = \lambda_1 P_1 + \lambda_2 P_2 + \lambda_3 P_3$
> 2. Calculation: $P = (0.1 \times 0.10) + (0.3 \times 0.20) + (0.6 \times 0.0)$
> 3. $P = 0.01 + 0.06 + 0.0 = \mathbf{0.07}$
> 
> Yes, it successfully solves the zero-probability problem. Even though the Trigram MLE was exactly $0.0$, the sentence probability will not collapse because the Unigram and Bigram components provided a non-zero "safety net" that resulted in a final positive probability of $0.07$.

**2-Mark Question**: What is the fundamental difference between Linear Interpolation and Katz Backoff?
> **Answer**: Interpolation calculates and mathematically mixes the probability distributions of all available n-gram models simultaneously via a weighted average for every prediction. Backoff uses only the highest-order model available, and completely discards it to "back off" to a lower-order model only if the higher-order count is exactly zero.

---

### Can You Explain This?
- [ ] I can write the Linear Interpolation formula using the $\lambda$ notation.
- [ ] I know the exact mathematical rule that all $\lambda$ weights must follow.
- [ ] I can explain the mechanical difference between Interpolation and Backoff.

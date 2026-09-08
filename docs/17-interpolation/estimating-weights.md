# Estimating Interpolation Weights

## 1. The Problem with Fixed Weights
In the previous section, we simply hardcoded the mathematical interpolation weights as fixed numbers ($\lambda_3=0.7$, $\lambda_2=0.2$, $\lambda_1=0.1$). 

This is incredibly inefficient in practice. If our training corpus is very small, we should mathematically trust the Trigram model *less* because its count tables will be highly unreliable due to extreme Data Sparsity. Conversely, if our corpus contains 10 billion words, we should trust the Trigram model *significantly more* because the counts are statistically robust.

We need a way to mathematically and algorithmically estimate the optimal $\lambda$ weights based on the actual shape of the data.

---

## 2. Held-Out Data
Just like choosing the hyperparameter $k$ for Add-k smoothing, we cannot calculate the optimal $\lambda$ weights by testing them on the Training Set. 

If we run an optimization algorithm on the Training Set, the math will perfectly maximize the Trigram weight ($\lambda_3 = 1.0$) because the Trigram fits the training data perfectly (it perfectly memorized the sentences it already saw).

Instead, we must partition our dataset:
1. **Training Set (e.g., 80%)**: Used to explicitly calculate the raw MLE fraction tables for the Unigrams, Bigrams, and Trigrams.
2. **Held-Out Set (Validation Set) (e.g., 10%)**: Used exclusively to mathematically test different combinations of $\lambda_1, \lambda_2, \text{ and } \lambda_3$ to see which specific combination yields the highest overall probability for the unseen text.

---

## 3. The Estimation Algorithm (Deleted Interpolation)
Finding the mathematically optimal $\lambda$ weights involves an iterative statistical optimization process, usually a variant of the **Expectation-Maximization (EM) algorithm**.

A common, conceptually simple approach to understand this is **Deleted Interpolation**:
1. Take every single trigram sequence present in the Held-Out set.
2. For each trigram $(w_{n-2}, w_{n-1}, w_n)$, compare its Unigram MLE, Bigram MLE, and Trigram MLE (using the tables calculated from the Training set).
3. Whichever specific model gave the highest raw mathematical probability for that word gets a "vote" (or a partial weight assignment).
4. After processing the entire Held-Out set, normalize the total votes to determine the final decimal values for $\lambda_1, \lambda_2, \lambda_3$.

> [!TIP]
> **Intuition**: If the Held-Out set is full of rare, novel phrases, the Trigram model will frequently output $0.0$, and the Bigram/Unigram models will get all the votes. The final $\lambda_1$ and $\lambda_2$ weights will naturally become larger, permanently adjusting the model to rely more heavily on smaller contexts.

---

## 4. Numerical Problem Walkthrough

**Problem**: You have built an interpolated model and tuned it on a Held-Out set, resulting in the optimized weights: **$\lambda_3 = 0.5, \lambda_2 = 0.3, \lambda_1 = 0.2$**.
Using the raw training MLE tables provided below, calculate the final interpolated probability $P(\text{"apples"} \mid \text{"eat green"})$.

**Raw Training MLE Tables:**
- $P_{MLE}(\text{"apples"} \mid \text{"eat green"}) = \mathbf{0.0}$ *(Trigram - Unseen)*
- $P_{MLE}(\text{"apples"} \mid \text{"green"}) = \mathbf{0.10}$ *(Bigram)*
- $P_{MLE}(\text{"apples"}) = \mathbf{0.05}$ *(Unigram)*

**Solution**:
1. Apply the interpolation formula:
$$ P_{Interp} = \lambda_3(P_3) + \lambda_2(P_2) + \lambda_1(P_1) $$
2. Substitute the exact values:
$$ P_{Interp} = (0.5 \times 0.0) + (0.3 \times 0.10) + (0.2 \times 0.05) $$
3. Solve the arithmetic:
$$ P_{Interp} = 0.0 + 0.03 + 0.01 = \mathbf{0.04} $$

> [!NOTE]
> Notice how despite the Trigram probability collapsing to exactly $0.0$, the final smoothed probability is a mathematically healthy $0.04$ thanks to the weighted Bigram and Unigram fallbacks.

---

## 5. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: Explain exactly why using the Expectation-Maximization (EM) algorithm to estimate interpolation weights on the Training Data itself will always disastrously result in $\lambda_n = 1.0$.
> **Answer**: 
> The highest-order N-gram (e.g., the Trigram model) perfectly memorizes the specific sequences within the Training Data. If we attempt to optimize the weights by evaluating the models on the exact same sentences they were trained on, the Trigram model will output exceptionally high probabilities for those sequences, while the Unigram and Bigram models will output lower probabilities. 
> 
> Because the EM algorithm's sole goal is to maximize the final probability score, it will aggressively assign $100\%$ of the mathematical weight to the Trigram model ($\lambda_3 = 1.0$), reducing the other weights to $0.0$. This completely defeats the purpose of smoothing, resulting in a model that is completely overfit and will crash with a probability of $0.0$ the moment it sees real-world, unseen data.

**2-Mark Question**: Check the following set of weights. Are they mathematically valid for Linear Interpolation? 
$\lambda_3 = 0.45, \lambda_2 = 0.45, \lambda_1 = 0.20$
> **Answer**: No, they are mathematically invalid. The sum of the weights is $0.45 + 0.45 + 0.20 = 1.10$. In linear interpolation, the weights must strictly sum to exactly $1.0$ to ensure the final result remains a valid probability distribution.

---

### Can You Explain This?
- [ ] I can explicitly define what Held-Out Data is.
- [ ] I can calculate an interpolated probability given three raw MLE scores and three $\lambda$ weights.
- [ ] I can conceptually explain how the EM algorithm assigns larger weights to the models that perform better on the validation set.

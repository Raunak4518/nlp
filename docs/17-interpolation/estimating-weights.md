# Estimating Interpolation Weights

## 1. The Problem with Fixed Weights
In the previous section, we hardcoded the interpolation weights ($\lambda_3=0.7$, $\lambda_2=0.2$, $\lambda_1=0.1$). This is inefficient. If our training corpus is very small, we should trust the Trigram model *less* because its counts are likely unreliable due to sparsity. If the corpus is massive, we should trust the Trigram model *more*.

We need a way to algorithmically estimate the optimal $\lambda$ weights based on the data.

## 2. Held-Out Data
Just like choosing $k$ for Add-k smoothing, we cannot calculate the optimal $\lambda$ weights by testing them on the training data. If we do, the math will perfectly maximize the Trigram weight ($\lambda_3 = 1.0$) because the Trigram fits the training data perfectly.

Instead, we must partition our dataset:
1. **Training Set**: Used to calculate the raw MLE counts for the Unigrams, Bigrams, and Trigrams.
2. **Held-Out Set (Validation Set)**: Used exclusively to test different combinations of $\lambda_1, \lambda_2, \lambda_3$ to see which combination yields the highest overall probability for the held-out text.

## 3. The Estimation Algorithm (EM / Deleted Interpolation)
Finding the optimal $\lambda$ weights involves an iterative optimization process, usually a variant of the Expectation-Maximization (EM) algorithm.

A common simplified approach is **Deleted Interpolation**:
1. Take every trigram in the Held-Out set.
2. For each trigram $(w_{n-2}, w_{n-1}, w_n)$, compare its Unigram MLE, Bigram MLE, and Trigram MLE (calculated from the Training set).
3. Whichever model gave the highest probability gets a "vote" (or a partial weight assignment).
4. After processing the entire Held-Out set, normalize the votes to determine the final $\lambda_1, \lambda_2, \lambda_3$.

*Intuition*: If the Held-Out set is full of rare phrases, the Trigram model will frequently output $0.0$, and the Bigram/Unigram models will get all the votes. The final $\lambda_1, \lambda_2$ weights will naturally become larger, adjusting the model to rely more heavily on smaller contexts.

## 4. Numerical Problem Walkthrough

**Problem**: You have built an interpolated model with $\lambda_3 = 0.5, \lambda_2 = 0.3, \lambda_1 = 0.2$.
Using the training MLE tables below, calculate the interpolated probability $P(\text{"apples"} | \text{"eat green"})$.

**Training MLE Tables:**
- $P_{MLE}(\text{"apples"} | \text{"eat green"}) = 0.0$ *(Trigram)*
- $P_{MLE}(\text{"apples"} | \text{"green"}) = 0.1$ *(Bigram)*
- $P_{MLE}(\text{"apples"}) = 0.05$ *(Unigram)*

**Solution**:
1. Apply the interpolation formula:
$$ P_{Interp} = \lambda_3(P_3) + \lambda_2(P_2) + \lambda_1(P_1) $$
2. Substitute the values:
$$ P_{Interp} = (0.5 \times 0.0) + (0.3 \times 0.1) + (0.2 \times 0.05) $$
3. Solve:
$$ P_{Interp} = 0.0 + 0.03 + 0.01 = \mathbf{0.04} $$

*Notice how despite the Trigram probability being exactly 0.0, the final smoothed probability is a healthy 0.04 thanks to the Bigram and Unigram fallbacks.*

## 5. Exam Preparation
### Must Memorize
- $\lambda$ weights must be trained on **Held-Out Data**, never the Training Data.

### Likely Practical Question
**Question**: Explain why estimating $\lambda$ weights on the training data always results in $\lambda_{max\_n} = 1.0$.
**Answer**: The highest-order N-gram (e.g., Trigram) perfectly memorizes the training data. If we evaluate the Trigram model on the exact same sentences it trained on, it will output very high probabilities for those exact sequences. An optimization algorithm will therefore assign $100\%$ of the weight to the Trigram model to maximize the score, resulting in a model that is completely overfit and incapable of generalizing.

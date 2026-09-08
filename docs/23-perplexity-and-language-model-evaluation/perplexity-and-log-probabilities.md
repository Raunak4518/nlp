# Perplexity and Log Probabilities

## 1. The Problem with Raw Probabilities
Because a language model calculates the probability of a sentence by multiplying fractions ($P \times P \times P$), the final probability for a long document quickly approaches zero. This causes **Underflow**, where computers round the number down to exactly $0.0$ because it is too small to store in memory.

To prevent this, we operate in **Log Space**.
Instead of multiplying probabilities:
$$ P(w_1, w_2) = P(w_1) \times P(w_2) $$
We add log probabilities:
$$ \log P(w_1, w_2) = \log P(w_1) + \log P(w_2) $$

## 2. Cross-Entropy
Cross-entropy measures how well our Language Model (a probability distribution) predicts a real, physical sample of text. If the text is $W = w_1, w_2, ..., w_N$, the cross-entropy $H(W)$ is:

$$ H(W) = -\frac{1}{N} \log_2 P(w_1, ..., w_N) $$
*(Which is exactly the average negative log probability per word).*

## 3. Perplexity Definition
**Perplexity (PP)** is the standard metric used to evaluate how "good" a language model is. It is mathematically defined as $2^{\text{Cross-Entropy}}$.

Alternatively, it is the inverse probability of the test set, normalized by the number of words $N$:
$$ PP(W) = P(w_1, w_2, ..., w_N)^{-\frac{1}{N}} $$
$$ PP(W) = \sqrt[N]{\frac{1}{P(w_1, w_2, ..., w_N)}} $$

### The Intuition of Perplexity
Perplexity can be thought of as the **Weighted Average Branching Factor** of a language.
- If a model has a perplexity of 100, it means that at any given point in the sentence, the model is "guessing" between 100 equally likely next words.
- If a model has a perplexity of 1, it means the model is absolutely certain of what the next word is.

Therefore, **Lower Perplexity is better.** A model that assigns a high probability to the real, observed test text will yield a low perplexity score.

## 4. Why Zero Probability Breaks Perplexity
If the model encounters an unseen N-gram without smoothing, its probability is $0.0$.
$$ PP(W) = \sqrt[N]{\frac{1}{0.0}} = \infty $$
A single zero probability makes the Perplexity explode to infinity, completely ruining the evaluation. This is why smoothing must be applied before calculating perplexity.

## 5. Comparing Two Language Models
To prove that Model A (e.g., Kneser-Ney) is better than Model B (e.g., Laplace), you must test both models on the *exact same unseen test set*.
- The model that produces the **lowest perplexity** score is the better model, because it was less "surprised" by the real text.

## 6. Exam Preparation
### Must Memorize
- $PP(W) = P(W)^{-\frac{1}{N}}$.
- **Lower perplexity is better**.

### Likely Practical Question
**Question**: You have a 3-word test sentence with the following model probabilities: $P(w_1)=0.5$, $P(w_2|w_1)=0.5$, $P(w_3|w_2)=0.5$. Calculate the Perplexity.
**Answer**:
1. Calculate sentence probability: $P(W) = 0.5 \times 0.5 \times 0.5 = 0.125 = 1/8$.
2. Calculate Perplexity: $PP = (1/8)^{-1/3} = 8^{1/3} = 2$.
*(Notice how the perplexity is exactly 2, matching the fact that at every step, the model had a 50% chance, meaning it was choosing between 2 equally likely options).*

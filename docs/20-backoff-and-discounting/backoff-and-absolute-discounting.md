# Backoff and Absolute Discounting

## 1. The Concept of Backoff
In Module 17, we introduced Interpolation, which *always* mixes the probabilities of Unigram, Bigram, and Trigram models together using $\lambda$ weights.

**Backoff** is a conditional approach. 
1. We check the Trigram model. If the specific 3-word sequence was seen in the training data (count > 0), we use the Trigram probability. We **do not** mix in the Bigram or Unigram models.
2. If the Trigram count is exactly 0, we *back off* to the Bigram model.
3. If the Bigram count is exactly 0, we *back off* to the Unigram model.

## 2. The Need for Discounting
There is a mathematical problem with naive backoff. 
If we use the raw MLE for the seen Trigrams, all of the probability mass ($1.0$) is consumed by the seen events. When we "back off" to the Bigram model for unseen events, there is no probability mass left to give them. If we just add the Bigram probabilities, our total probability will exceed $1.0$.

To fix this, we must **Discount** the probabilities of the seen events to save some probability mass (the "leftover" mass) for the unseen events that we back off to.

## 3. Absolute Discounting
The simplest and most highly effective way to discount counts is **Absolute Discounting**.
Instead of using complex Good-Turing fractions, we simply subtract a fixed constant $d$ (usually $0.75$) from every non-zero count.

$$ c^* = c - d $$

*(Note: If the result is negative, we set it to $0$. We only subtract $d$ from counts that are greater than $0$).*

### Why this works
By subtracting $0.75$ from every seen word's count, we gather a "pool" of leftover probability mass. We then take this entire pool and distribute it among the unseen words by backing off to the lower-order N-gram model.

### Estimating $D$
While $d=0.75$ is a common heuristic, the optimal discount $D$ can be estimated using the count of singletons ($N_1$) and doubletons ($N_2$) in the corpus:
$$ D = \frac{N_1}{N_1 + 2N_2} $$

## 4. Numerical Problem Walkthrough (Absolute Discounting)

**Problem**:
- Context: "the" appears 100 times ($N=100$).
- "the" is followed by exactly 10 unique words.
- You are using Absolute Discounting with $d=0.75$.
- "the cat" appeared 5 times.
- "the xylophone" appeared 0 times.

Calculate the discounted probability of "the cat", and calculate the total leftover probability mass available for all unseen words.

**Solution**:
1. Discount the seen event:
   $$ P(\text{"cat"} | \text{"the"}) = \frac{c - d}{N} = \frac{5 - 0.75}{100} = \frac{4.25}{100} = 0.0425 $$
2. Calculate Leftover Mass:
   We subtracted $0.75$ from exactly 10 unique words (because 10 unique words followed "the").
   Total subtracted counts = $10 \times 0.75 = 7.5$.
   Total leftover probability mass = $\frac{7.5}{100} = 0.075$.
   *(This $0.075$ mass is what will be distributed to unseen words like "xylophone" using the lower-order Unigram model).*

## 5. Exam Preparation
### Must Memorize
- Absolute discounting formula: subtract a fixed $d$ from all $c > 0$.
- The total probability mass reserved for backoff is $\frac{\text{unique\_words} \times d}{N}$.

### Likely Theory Question
**Question**: Explain the conceptual difference between Interpolation and Backoff.
**Answer**: Interpolation always calculates a weighted sum of all N-gram levels (Unigram, Bigram, Trigram) for every prediction, regardless of whether the highest-order N-gram was seen or unseen. Backoff only uses the highest-order N-gram if it was seen in the training data, and only falls back to lower-order models if the higher-order count is strictly zero.

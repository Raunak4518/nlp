# Kneser-Ney Fundamentals

## 1. The "Francisco" Problem
Why do we need yet another smoothing algorithm? Kneser-Ney was invented to solve a specific, glaring flaw in standard Backoff and Interpolation: **they only look at how frequently a word appears, not how *diverse* its contexts are.**

Consider the word "Francisco". In a large corpus, it might appear 10,000 times.
However, it almost *exclusively* appears after the word "San". It has a very high frequency, but extremely low **Context Diversity**.

If a standard language model encounters the unseen phrase "I want to read Francisco", it backs off to the unigram probability $P(\text{"Francisco"})$. Because "Francisco" appears 10,000 times, the unigram probability is quite high. The model will confidently predict that "I want to read Francisco" is a highly probable sentence.

This is wrong. "Francisco" shouldn't get a high backoff probability just because "San Francisco" is a common city. 

## 2. Continuation Probability
**Kneser-Ney Smoothing** fixes this by fundamentally changing how we calculate the fallback unigram probability. 

Instead of asking: "How many times did word $w$ appear?"
We ask: "How many *different* words precede word $w$?"

This is called the **Continuation Probability** $P_{CONTINUATION}(w)$. It measures how likely word $w$ is to appear as a novel continuation of a new context.

## 3. Continuation Count
To calculate $P_{CONTINUATION}(w)$, we count the number of unique Bigram types that end in $w$.
$$ \text{Continuation Count}(w) = |\{ w_{i-1} : \text{Count}(w_{i-1}, w) > 0 \}| $$

- "Francisco" only has 1 preceding word type ("San"). Continuation count = $1$.
- "read" has thousands of preceding word types ("I", "to", "will", "cannot", "must"). Continuation count = $5000$.

Even though "Francisco" might appear more total times than "read", "read" will get a vastly higher continuation probability.

$$ P_{CONTINUATION}(w) = \frac{|\{ w_{i-1} : c(w_{i-1}, w) > 0 \}|}{\sum_{w'} |\{ w_{i-1} : c(w_{i-1}, w') > 0 \}|} $$
*(The denominator is simply the total number of unique bigram types in the entire corpus).*

## 4. Bigram Kneser-Ney
To build the final Bigram Kneser-Ney formula, we combine **Absolute Discounting** (to save probability mass from the seen bigrams) with **Continuation Probability** (to distribute that mass to unseen bigrams).

$$ P_{KN}(w_i | w_{i-1}) = \frac{\max(c(w_{i-1}, w_i) - d, 0)}{c(w_{i-1})} + \lambda(w_{i-1}) P_{CONTINUATION}(w_i) $$

Where $\lambda(w_{i-1})$ is the normalizing weight that ensures the leftover mass perfectly matches the mass we discounted:
$$ \lambda(w_{i-1}) = \frac{d}{c(w_{i-1})} \times |\{w : c(w_{i-1}, w) > 0\}| $$

## 5. Numerical Problem Walkthrough

**Problem**:
- The corpus has 1,000 unique bigram types total.
- The word "glasses" is preceded by exactly 5 unique words in the corpus ("reading", "my", "sun", "water", "wine").
- Calculate $P_{CONTINUATION}(\text{"glasses"})$.

**Solution**:
1. Continuation count of "glasses" = $5$.
2. Total bigram types = $1000$.
3. $P_{CONTINUATION} = 5 / 1000 = 0.005$.

## 6. Exam Preparation
### Must Memorize
- Kneser-Ney replaces the Unigram backoff probability with the **Continuation Probability**.
- Continuation Probability is based on how many *unique preceding words* exist for the target word.

### Likely Theory Question
**Question**: Explain how Kneser-Ney smoothing prevents the model from incorrectly predicting "I read Francisco".
**Answer**: In standard backoff, the unigram probability of "Francisco" is high because it appears frequently in the corpus (e.g., in "San Francisco"). Kneser-Ney replaces this with the Continuation Probability, which measures context diversity. Because "Francisco" is only ever preceded by "San", its continuation count is 1, yielding a near-zero continuation probability. The model correctly realizes "Francisco" does not easily attach to novel contexts like "read", preventing the error.

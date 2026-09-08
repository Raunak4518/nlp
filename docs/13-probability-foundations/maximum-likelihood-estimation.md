# Maximum Likelihood Estimation (MLE)

## 1. Where do probabilities come from?
The mathematical formulas for Bayes Theorem and the Chain Rule assume we already know the probabilities $P(A)$ or $P(A|B)$. But in NLP, we don't start with probabilities; we start with raw text data. We have to *estimate* the probabilities from the data.

The most common way to do this is **Maximum Likelihood Estimation (MLE)**.

## 2. Relative Frequency
The core intuition of MLE is that the probability of an event happening in the future is exactly equal to its relative frequency in the past data.

$$ P(\text{Event}) = \frac{\text{Count of Event}}{\text{Total Count of All Possible Events}} $$

### Example: Unigram MLE
If we have a training corpus of 10,000 total words, and the word "dog" appears 50 times:
$$ P_{MLE}(\text{"dog"}) = \frac{50}{10,000} = 0.005 $$

### Example: Conditional MLE
To estimate $P(w_i | w_{i-1})$ (e.g., $P(\text{"cat"} | \text{"the"})$):
We count how many times the sequence "the cat" occurs, and divide it by the total number of times the word "the" occurs.

$$ P_{MLE}(w_i | w_{i-1}) = \frac{\text{Count}(w_{i-1}, w_i)}{\text{Count}(w_{i-1})} $$

If "the cat" appears 40 times, and "the" appears 1000 times overall:
$$ P_{MLE}(\text{"cat"} | \text{"the"}) = \frac{40}{1000} = 0.04 $$

## 3. The Flaw with MLE
MLE is perfectly accurate *for the training data*. However, it assigns a probability of exactly $0.0$ to any event that did not occur in the training data.

If "the dog" never appeared in our 10,000-word corpus, $P_{MLE}(\text{"dog"} | \text{"the"}) = 0$. 
Because of the Chain Rule (which multiplies probabilities), a single $0.0$ will cause the probability of an entire sentence to become $0.0$. This is disastrous for NLP.

To fix this, we use smoothing techniques (like Laplace Smoothing), which take a small amount of probability away from seen events and give it to unseen events so that no probability is ever exactly zero.

## 4. Exam Preparation
### Must Memorize
- The MLE formula for conditional probability: $\frac{\text{Count}(A, B)}{\text{Count}(A)}$.
- The primary flaw of MLE: It assigns zero probability to unseen events.

### Likely Practical Question
**Question**: You are given a corpus with the following sentence: "I saw the man who saw the dog." Calculate the MLE probability of $P(\text{"the"} | \text{"saw"})$.
**Answer**:
1. How many times does "saw" appear? 2 times.
2. How many times does the sequence "saw the" appear? 2 times.
3. $P(\text{"the"} | \text{"saw"}) = 2 / 2 = 1.0$. 
*(In this tiny corpus, "the" always follows "saw" 100% of the time).*

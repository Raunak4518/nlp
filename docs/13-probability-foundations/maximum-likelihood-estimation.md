# Maximum Likelihood Estimation (MLE)

## 1. Where do probabilities come from?
The mathematical formulas for Bayes' Theorem and the Chain Rule assume we *already know* the underlying probabilities $P(A)$ or $P(A \mid B)$. But in real-world NLP, we don't start with magical probability tables; we start with gigabytes of raw text data. We have to *estimate* the true probability from the raw text.

The most mathematically standard way to do this is **Maximum Likelihood Estimation (MLE)**.

---

## 2. Relative Frequency
The core intuition of MLE is straightforward: it assumes that the probability of an event happening in the future is exactly equal to its relative frequency in the past training data.

$$ P(\text{Event}) = \frac{\text{Count of Event occurrences}}{\text{Total Count of All Possible Events}} $$

### Example: Unigram MLE
If we have a training corpus of 10,000 total words, and the word "dog" appears exactly 50 times, the MLE probability is:
$$ P_{MLE}(\text{"dog"}) = \frac{50}{10,000} = 0.005 $$

### Example: Conditional MLE
To estimate $P(w_i \mid w_{i-1})$ (e.g., $P(\text{"cat"} \mid \text{"the"})$), we count how many times the exact sequence "the cat" occurs, and divide it by the total number of times the prefix word "the" occurs.

$$ P_{MLE}(w_i \mid w_{i-1}) = \frac{\text{Count}(w_{i-1}, w_i)}{\text{Count}(w_{i-1})} $$

If "the cat" appears 40 times, and the word "the" appears 1,000 times overall in the corpus:
$$ P_{MLE}(\text{"cat"} \mid \text{"the"}) = \frac{40}{1000} = 0.04 $$

---

## 3. The Fatal Flaw with MLE

MLE is perfectly accurate *for the training data it has seen*. However, it possesses a catastrophic flaw when applied to real-world predictions: **it assigns a probability of exactly $0.0$ to any sequence that did not occur in the training data.**

If the sequence "the dog" never randomly happened to appear in our specific 10,000-word training corpus, then $P_{MLE}(\text{"dog"} \mid \text{"the"}) = 0$. 

Because the Chain Rule multiplies conditional probabilities together, a single $0.0$ anywhere in the equation will mathematically cause the probability of the entire sentence to become $0.0$. The model will assume the sentence is physically impossible to ever be spoken. This is disastrous for NLP, because human language is infinitely creative and we constantly speak sentences that have never been recorded before.

### The Solution: Smoothing
To fix this fatal flaw, we use mathematical **smoothing techniques** (like Laplace Add-1 Smoothing, covered in later modules). Smoothing takes a tiny fraction of probability mass away from events we *have* seen and redistributes it to events we *haven't* seen, ensuring that no probability is ever exactly zero.

---

## 4. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: You are given a tiny training corpus containing exactly one sentence: *"I saw the man who saw the dog."* Calculate the MLE probability of $P(\text{"the"} \mid \text{"saw"})$. Show your work.
> **Answer**:
> 1. The formula is $P(\text{"the"} \mid \text{"saw"}) = \frac{\text{Count}(\text{"saw the"})}{\text{Count}(\text{"saw"})}$
> 2. How many times does the unigram "saw" appear in the corpus? 2 times.
> 3. How many times does the bigram "saw the" appear? 2 times.
> 4. $P(\text{"the"} \mid \text{"saw"}) = \frac{2}{2} = 1.0$. 
> 
> *(In this tiny corpus, "the" follows "saw" 100% of the time).*

**3-Mark Question**: What is the primary flaw of Maximum Likelihood Estimation in NLP, and how does it negatively affect the Chain Rule?
> **Answer**: The primary flaw of MLE is that it assigns a probability of exactly $0.0$ to any sequence that did not explicitly appear in the training data (the zero-probability problem). Because the Chain Rule calculates the joint probability of a sentence by multiplying all conditional probabilities together, encountering a single unseen bigram with a probability of $0.0$ will collapse the entire multiplication equation to $0.0$, making the model believe the entire sentence is completely impossible.

---

### Can You Explain This?
- [ ] I can write the MLE formula for calculating a conditional probability.
- [ ] I can explain why a probability of $0.0$ is disastrous for a language model.
- [ ] I can explain the conceptual purpose of Smoothing algorithms.

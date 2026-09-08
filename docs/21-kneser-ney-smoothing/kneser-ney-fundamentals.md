# Kneser-Ney Fundamentals

## 1. The "Francisco" Problem
Why do we mathematically need yet another smoothing algorithm? Kneser-Ney was historically invented to solve a specific, glaring mathematical flaw in standard Backoff and Interpolation algorithms: **they only measure how *frequently* a word appears overall, not how *diverse* its contexts actually are.**

Consider the word "Francisco". In a large corpus of text, it might appear 10,000 times.
However, it almost *exclusively* appears directly after the word "San". It has a very high raw frequency, but extremely low **Context Diversity**.

If a standard Backoff language model evaluates the unseen phrase *"I want to read Francisco"*, it backs off to the unigram probability $P(\text{"Francisco"})$. Because "Francisco" appears 10,000 times, the raw unigram probability is actually quite high. The model will confidently and incorrectly predict that *"I want to read Francisco"* is a highly probable sentence.

This is a catastrophic error. "Francisco" shouldn't get a high backoff probability just because "San Francisco" happens to be a common city name. 

---

## 2. Continuation Probability
**Kneser-Ney Smoothing** elegantly fixes this by fundamentally changing how we mathematically calculate the fallback unigram probability. 

Instead of asking: *"How many times did word $w$ appear in total?"*
Kneser-Ney asks: *"How many **different** words historically precede word $w$?"*

This new metric is called the **Continuation Probability** $P_{CONTINUATION}(w)$. It measures how statistically likely the word $w$ is to appear as a novel continuation of a brand-new, unseen context.

---

## 3. Continuation Count
To calculate $P_{CONTINUATION}(w)$, we count the number of unique Bigram types in the training text that end in $w$.
$$ \text{Continuation Count}(w) = |\{ w_{i-1} : \text{Count}(w_{i-1}, w) > 0 \}| $$

- "Francisco" only has 1 preceding word type ("San"). Continuation count = $\mathbf{1}$.
- "read" has thousands of preceding word types ("I", "to", "will", "cannot", "must"). Continuation count = $\mathbf{5000}$.

Even though "Francisco" might appear more total times in the text than "read", "read" will get a vastly higher continuation probability because its context is diverse.

> [!IMPORTANT]
> **Continuation Probability Formula**
> $$ P_{CONTINUATION}(w) = \frac{|\{ w_{i-1} : c(w_{i-1}, w) > 0 \}|}{\sum_{w'} |\{ w_{i-1} : c(w_{i-1}, w') > 0 \}|} $$
> *(Note: The mathematical denominator is simply the total number of unique bigram types in the entire corpus).*

---

## 4. Bigram Kneser-Ney Equation
To build the final Bigram Kneser-Ney formula, we mathematically combine **Absolute Discounting** (to aggressively save probability mass from the seen bigrams) with **Continuation Probability** (to intelligently distribute that leftover mass to the unseen bigrams).

$$ P_{KN}(w_i \mid w_{i-1}) = \frac{\max(c(w_{i-1}, w_i) - d, 0)}{c(w_{i-1})} + \lambda(w_{i-1}) P_{CONTINUATION}(w_i) $$

Where the normalizer $\lambda(w_{i-1})$ is the specific weight that explicitly ensures the leftover mass perfectly matches the mass we discounted:
$$ \lambda(w_{i-1}) = \frac{d}{c(w_{i-1})} \times |\{w : c(w_{i-1}, w) > 0\}| $$

---

## 5. Numerical Problem Walkthrough

**Problem**:
You are examining a small text corpus. 
- The corpus has exactly $1,000$ unique bigram types total.
- The specific word `"glasses"` is preceded by exactly 5 unique words in the historical corpus (`"reading"`, `"my"`, `"sun"`, `"water"`, `"wine"`).
- Calculate the mathematically exact $P_{CONTINUATION}(\text{"glasses"})$.

**Solution**:
1. Calculate the Continuation Count of "glasses". It is preceded by 5 unique contexts, so the count is $5$.
2. Note the total bigram types = $1000$.
3. Apply the formula:
   $P_{CONTINUATION} = \frac{5}{1000} = \mathbf{0.005}$.

---

## 6. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: Explain specifically how Kneser-Ney smoothing prevents the statistical model from incorrectly assigning a high probability to the anomalous sentence "I read Francisco".
> **Answer**: In standard Backoff or Interpolation models, the raw unigram probability of "Francisco" is high because it appears very frequently in the corpus (e.g., inside the phrase "San Francisco"). Kneser-Ney permanently replaces this raw unigram probability with the **Continuation Probability**, which strictly measures context diversity rather than total frequency. 
> 
> Because "Francisco" is almost exclusively preceded by the word "San", its continuation count is very low (e.g., 1). Therefore, it yields a near-zero continuation probability. The Kneser-Ney model correctly realizes "Francisco" does not probabilistically attach to novel contexts like "read", cleanly preventing the prediction error.

**2-Mark Question**: In the Kneser-Ney Bigram formula, what specific mathematical algorithm is used on the "Seen" events to generate the leftover probability mass for the $\lambda$ normalizer?
> **Answer**: It strictly utilizes Absolute Discounting ($\max(c - d, 0)$) to subtract a fixed constant from the seen events to generate the leftover probability mass.

---

### Can You Explain This?
- [ ] I can conceptually explain the "Francisco" problem.
- [ ] I can mathematically define exactly what a Continuation Count is.
- [ ] I can explicitly state the two algorithms that Kneser-Ney structurally combines (Absolute Discounting + Continuation Probability).

# Backoff and Absolute Discounting

## 1. The Concept of Backoff
In Module 17, we introduced **Interpolation**, which mathematically *always* mixes the probabilities of Unigram, Bigram, and Trigram models together simultaneously using $\lambda$ weights.

**Backoff** is a conditional, `if/else` alternative to interpolation. 
1. We first check the Trigram model. If the specific 3-word sequence was seen in the training data (count > 0), we use the Trigram probability. We **do not** mix in the Bigram or Unigram models.
2. If the Trigram count is exactly 0, we abandon the Trigram and *back off* to the Bigram model.
3. If the Bigram count is exactly 0, we abandon the Bigram and *back off* to the Unigram model.

---

## 2. The Absolute Need for Discounting
There is a massive mathematical problem with naive backoff: ensuring the probabilities sum to $1.0$.

If we use the raw Maximum Likelihood Estimation (MLE) for the seen Trigrams, all of the mathematically available probability mass ($1.0$) is consumed by the seen events. When we "back off" to the Bigram model for unseen events, there is physically no probability mass left to give them. If we simply add the Bigram probabilities on top of the Trigram probabilities, our total probability will exceed $1.0$, rendering the math invalid.

To permanently fix this, we must **Discount** the probabilities of the seen events. By artificially lowering the scores of the things we *did* see, we gather a "pool" of leftover probability mass that we can legally distribute to the unseen events when we back off.

---

## 3. Absolute Discounting
The simplest, most elegant, and highly effective way to discount counts is called **Absolute Discounting**.

Instead of using incredibly complex Good-Turing fractional mathematics ($N_{c+1} / N_c$), we simply subtract a fixed, flat constant $d$ (usually around $0.75$) from every single non-zero count.

> [!IMPORTANT]
> **Absolute Discounting Formula**
> $$ c^* = c - d $$
> *(Note: We only subtract $d$ from counts that are greater than $0$. If a count is 0, we do not subtract to make it negative).*

### Why this trivially simple math works
By mechanically subtracting $0.75$ from every seen word's count, we mathematically gather a "pool" of leftover probability mass. We then take this entire gathered pool and distribute it evenly among the unseen words by backing off to the lower-order N-gram model.

### Estimating the optimal $d$
While manually hardcoding $d=0.75$ is a common heuristic, the mathematically optimal discount $D$ can actually be statistically estimated directly from the training text using the count of singletons ($N_1$) and doubletons ($N_2$) in the corpus:
$$ D = \frac{N_1}{N_1 + 2N_2} $$

---

## 4. Numerical Problem Walkthrough (Absolute Discounting)

**Problem**:
You are calculating probabilities for a Bigram model.
- Context: The word `"the"` appears 100 times in the corpus ($N=100$).
- `"the"` is historically followed by exactly 10 unique words ($T=10$).
- You are using Absolute Discounting with a fixed $d = 0.75$.
- The bigram `"the cat"` appeared exactly 5 times.
- The bigram `"the xylophone"` appeared exactly 0 times.

**Question 1**: Calculate the absolute discounted probability of `"the cat"`.
**Question 2**: Calculate the total leftover probability mass available to be distributed to all unseen words.

**Solution**:
1. Discount the seen event:
   $$ P(\text{"cat"} \mid \text{"the"}) = \frac{c - d}{N} = \frac{5 - 0.75}{100} = \frac{4.25}{100} = \mathbf{0.0425} $$

2. Calculate Total Leftover Mass:
   We mathematically subtracted $0.75$ from exactly 10 unique words (because 10 unique words followed "the").
   Total subtracted counts = $10 \times 0.75 = 7.5$.
   Total leftover probability mass = $\frac{7.5}{100} = \mathbf{0.075}$.

> [!NOTE]
> This mathematically pure $0.075$ mass is exactly what will be distributed to unseen words like `"xylophone"` when the algorithm backs off to the lower-order Unigram model.

---

## 5. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: A training corpus has 500 singletons ($N_1 = 500$) and 200 doubletons ($N_2 = 200$). Calculate the statistically optimal Absolute Discount $D$. If the bigram "data science" occurs 3 times in a context of 100, what is its discounted probability using this $D$?
> **Answer**: 
> 1. Calculate $D$:
>    $D = \frac{N_1}{N_1 + 2N_2} = \frac{500}{500 + 2(200)} = \frac{500}{900} \approx \mathbf{0.555}$
> 2. Calculate Discounted Probability:
>    $P(\text{"science"} \mid \text{"data"}) = \frac{c - D}{N} = \frac{3 - 0.555}{100} = \frac{2.445}{100} = \mathbf{0.02445}$

**2-Mark Question**: Explain the conceptual difference between Interpolation and Backoff.
> **Answer**: Interpolation always mathematically calculates a weighted sum of all available N-gram levels (e.g., Unigram, Bigram, Trigram) simultaneously for every prediction, regardless of whether the highest-order sequence was seen or unseen. Backoff acts as a strict fallback mechanism: it uses only the highest-order N-gram if it was seen, and only falls back (backs off) to lower-order models if the higher-order count is strictly zero.

---

### Can You Explain This?
- [ ] I can write the Absolute Discounting formula ($c^* = c - d$).
- [ ] I can explain mathematically why $d$ is only subtracted from counts $>0$.
- [ ] I can calculate the total leftover probability mass given $T$ unique words and $d$.

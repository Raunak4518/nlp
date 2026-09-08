# Laplace Smoothing (Add-One)

## 1. What is Laplace Smoothing?
Laplace Smoothing (frequently called **Add-One smoothing**) is the oldest and simplest mathematical technique used to permanently solve the Zero-Probability problem in classical N-gram Language Models. 

The core intuition is incredibly simple: **we mathematically pretend that every possible n-gram sequence occurred exactly one more time than it actually did in the training data.**

---

## 2. The Laplace Formula
Let's review the standard Maximum Likelihood Estimation (MLE) formula for a bigram probability $P(w_i \mid w_{i-1})$:
$$ P_{MLE} = \frac{\text{Count}(w_{i-1}, w_i)}{\text{Count}(w_{i-1})} $$

To apply Laplace smoothing, we simply add the number $1$ to the numerator (representing the $1$ "fake" time we pretend we saw the specific bigram).
$$ P_{Laplace} = \frac{\text{Count}(w_{i-1}, w_i) + \mathbf{1}}{\text{Denominator}} $$

### Why the Denominator becomes $+|V|$
Because we added $1$ to the numerator of *every single mathematically possible* next word in the vocabulary, our probabilities will no longer sum to $1.0$ if we keep the old denominator. 

Let **$V$** be the Vocabulary (the set of all unique words). There are exactly $|V|$ possible next words that could follow $w_{i-1}$. Since we added $1$ "fake" count to each of them, we have essentially hallucinated a total of $|V|$ fake counts into the system for the context $w_{i-1}$. 

To mathematically balance this and explicitly ensure all probabilities still sum to exactly $1.0$, we must add $|V|$ to the denominator.

> [!IMPORTANT]
> **The Laplace Add-1 Formula**
> $$ P_{Laplace}(w_i \mid w_{i-1}) = \frac{\text{Count}(w_{i-1}, w_i) + 1}{\text{Count}(w_{i-1}) + |V|} $$

---

## 3. How it affects Probabilities

### Unseen Events (The Zero Problem Fixed!)
If a valid bigram never occurred in training, its original count is $0$.
$$ P_{MLE}(\text{unseen}) = \frac{0}{\text{Count}} = 0.0 $$
$$ P_{Laplace}(\text{unseen}) = \frac{0 + 1}{\text{Count} + |V|} > 0.0 $$
The previously unseen bigram now has a very small, non-zero probability! The Chain Rule multiplication for the sentence will no longer collapse to $0.0$.

### Seen Events (Discounting)
If a bigram actually occurred $100$ times in training, its probability is noticeably *reduced* under Laplace smoothing. We essentially "stole" probability mass from the highly frequent seen events to give to the unseen events. This process is formally known as **Discounting**.

---

## 4. The Fatal Limitation of Laplace Smoothing
While it elegantly solves the math error (no more zero probabilities), Laplace smoothing is conceptually terrible for real-world NLP text generation.

Because the vocabulary $V$ is usually huge (e.g., $50,000$ unique words), adding $1$ to every single unseen, nonsensical combination introduces a massive amount of "fake" data into the model. In a sparse dataset, adding $|V|$ to the denominator heavily inflates it, brutally crushing the probabilities of valid, highly-frequent words and giving way too much statistical weight to nonsense combinations (like *"the xylophone"*).

*Note: While bad for text generation, Laplace Smoothing is still heavily used today in Naive Bayes text classification (like Spam Filters).*

---

## 5. Scratch Implementation

```python
def laplace_smoothing(bigram_count: int, context_count: int, vocab_size: int) -> float:
    """Calculates the smoothed probability of a bigram."""
    # Numerator: Add 1 "fake" count to the specific bigram
    # Denominator: Add |V| "fake" counts to the context total
    return (bigram_count + 1) / (context_count + vocab_size)
```

??? question "Trace the Math"
    ```python
    V = 10000 # 10,000 unique words in the vocabulary
    count_the = 500
    count_the_cat = 20
    count_the_xylophone = 0
    
    # Normal MLE
    mle_cat = count_the_cat / count_the
    mle_xylo = count_the_xylophone / count_the
    
    # Laplace
    lap_cat = laplace_smoothing(count_the_cat, count_the, V)
    lap_xylo = laplace_smoothing(count_the_xylophone, count_the, V)
    
    print(f"MLE Cat: {mle_cat:.4f}  | Laplace Cat: {lap_cat:.4f}")
    print(f"MLE Xylo: {mle_xylo:.4f} | Laplace Xylo: {lap_xylo:.4f}")
    
    # Output:
    # MLE Cat: 0.0400  | Laplace Cat: 0.0020
    # MLE Xylo: 0.0000 | Laplace Xylo: 0.0001
    
    # Notice the massive discounting: "the cat" had its probability 
    # slashed by 95% just to make room for the unseen words!
    ```

---

## 6. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: A training corpus has a vocabulary of 5,000 words. The unigram "I" appears 100 times. The bigram "I saw" appears 15 times. The bigram "I fly" appears 0 times. Calculate the Laplace smoothed probability for both $P(\text{"saw"} \mid \text{"I"})$ and $P(\text{"fly"} \mid \text{"I"})$. Show your formula.
> **Answer**: 
> **Formula**: $P_{Laplace}(w_i \mid w_{i-1}) = \frac{\text{Count}(w_{i-1}, w_i) + 1}{\text{Count}(w_{i-1}) + |V|}$
> 
> **Variables**: $|V| = 5000$, $\text{Count("I")} = 100$.
> 
> 1. $P_{Laplace}(\text{"saw"} \mid \text{"I"}) = \frac{15 + 1}{100 + 5000} = \frac{16}{5100} \approx 0.0031$
> 2. $P_{Laplace}(\text{"fly"} \mid \text{"I"}) = \frac{0 + 1}{100 + 5000} = \frac{1}{5100} \approx 0.0002$

**3-Mark Question**: Why is it mathematically strictly necessary to add $|V|$ to the denominator in Laplace smoothing instead of simply adding $1$?
> **Answer**: Because we added a fake count of $1$ to the numerator of *every mathematically possible next word* in the vocabulary $V$. In order to maintain a valid probability distribution, the sum of the probabilities of all possible next words must still perfectly equal exactly $1.0$. To balance the equation, the denominator must account for all $|V|$ fake counts we injected into the numerators.

---

### Can You Explain This?
- [ ] I can write the Laplace formula from memory.
- [ ] I can explicitly define what the variable $|V|$ represents (Vocabulary size, NOT total word count).
- [ ] I can explain why Laplace smoothing is considered "too aggressive" for sparse N-gram language models.

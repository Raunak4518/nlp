# Witten-Bell Smoothing

## 1. The Witten-Bell Intuition
Good-Turing uses the raw frequency of singletons to estimate the probability of unseen words. **Witten-Bell Smoothing** uses a slightly different, highly intuitive approach: it estimates the probability of encountering an unseen word by looking at *how often a new, unique word appears for the first time*.

Imagine you are reading a book. 
- In the very first sentence, practically every word you read is a "new" word. 
- By chapter 10, almost every word you read is a word you've seen before. 
- Occasionally, the author uses a word you haven't seen yet.

Witten-Bell explicitly models this phenomenon: The mathematical probability of encountering a completely unseen word in the future is proportional to the number of *unique* words (types) you have already encountered in the past.

---

## 2. Tokens (N) vs Types (T)
To use Witten-Bell correctly, we must define two distinct mathematical variables for a given context $w_{i-1}$:
1. **Tokens ($N$)**: The total number of times the context $w_{i-1}$ occurred. *(This is just the standard Unigram count).*
2. **Types ($T$)**: The number of *unique* words that historically followed the context $w_{i-1}$.

**Example**:
Corpus: *"the cat, the dog, the cat, the bird, the cat"*
Context: `"the"`
- **Tokens ($N$)**: "the" appears exactly 5 times. **$N = 5$**.
- **Types ($T$)**: "the" is followed by exactly 3 unique words: "cat", "dog", "bird". **$T = 3$**.

---

## 3. Probability Calculations

### Unseen Events (The Z Variable)
The total, combined probability mass mathematically reserved for *all* unseen words following a specific context is calculated using $T$ and $N$:
$$ P(\text{all unseen combined}) = \frac{T}{N + T} $$

If we want the probability of one *specific* unseen word (e.g., "xylophone"), we must divide that total combined mass equally by the number of mathematically unseen words **$Z$**. 
*(Where $Z = |V| - T$)*.

> [!IMPORTANT]
> **Specific Unseen Word Formula**
> $$ P(\text{specific unseen}) = \frac{T}{(N + T) \times Z} $$

### Seen Events (Discounting)
If a word actually occurred $c$ times after the context in the training data, its new mathematically smoothed probability is:

> [!IMPORTANT]
> **Seen Word Formula**
> $$ P(\text{seen}) = \frac{c}{N + T} $$

*Notice how incredibly similar this formula is to standard Laplace Add-1 smoothing, where we used $\frac{c}{N + |V|}$. Witten-Bell uses $+T$ in the denominator instead of $+|V|$. Because the number of Types $T$ is drastically smaller than the entire Vocabulary $|V|$, Witten-Bell steals far less probability mass from seen words, preserving the true natural distribution much better.*

---

## 4. Numerical Problem Walkthrough

**Problem**:
You are building an autocomplete system.
- Total Vocabulary Size $|V| = 1000$.
- You are examining the context word: `"big"`
- `"big"` appears 100 times total ($N=100$).
- `"big"` is followed by exactly 10 unique words in the training text ($T=10$).
- The specific bigram `"big house"` appears 40 times ($c=40$).
- The specific bigram `"big xylophone"` never appears ($c=0$).

Calculate the exact Witten-Bell smoothed probability for both "big house" and "big xylophone".

**Solution**:
1. First, mathematically find $Z$ (the exact number of unseen types): 
   $Z = |V| - T = 1000 - 10 = \mathbf{990}$.
2. Calculate "big house" (A Seen event):
   $$ P(\text{"house"} \mid \text{"big"}) = \frac{c}{N + T} = \frac{40}{100 + 10} = \frac{40}{110} \approx \mathbf{0.363} $$
3. Calculate "big xylophone" (An Unseen event):
   $$ P(\text{"xylophone"} \mid \text{"big"}) = \frac{T}{(N + T) \times Z} = \frac{10}{110 \times 990} = \frac{10}{108,900} \approx \mathbf{0.00009} $$

??? question "Trace the Math (Summing to 1.0)"
    We know there are 10 seen words and 990 unseen words. 
    Let's prove the distribution is mathematically valid.
    
    1. Sum of all seen probabilities: We don't have individual counts, but we know the total count $c$ of all seen words combined is equal to $N = 100$. So the total sum is $100/110$.
    2. Sum of all unseen probabilities: There are 990 unseen words, each with a probability of $(10 / 108900)$. 
       $990 \times (10 / 108900) = 9900 / 108900 = 10/110$.
    3. Total Sum: $100/110 + 10/110 = 110/110 = 1.0$. The math holds perfectly!

---

## 5. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: You are given a vocabulary $|V| = 500$. The word "data" appears $20$ times in your corpus. It is followed by $4$ unique words. The bigram "data science" occurs $15$ times. The bigram "data structure" occurs $0$ times. Calculate the Witten-Bell smoothed probability for $P(\text{"science"} \mid \text{"data"})$ and $P(\text{"structure"} \mid \text{"data"})$. Show all variables and formulas.
> **Answer**: 
> **Variables**: $|V| = 500$, $N = 20$, $T = 4$, $Z = |V| - T = 496$.
> 
> **Seen Event ("data science", $c=15$)**:
> Formula: $P(\text{seen}) = \frac{c}{N + T}$
> $P(\text{"science"} \mid \text{"data"}) = \frac{15}{20 + 4} = \frac{15}{24} = \mathbf{0.625}$
> 
> **Unseen Event ("data structure", $c=0$)**:
> Formula: $P(\text{unseen}) = \frac{T}{(N + T) \times Z}$
> $P(\text{"structure"} \mid \text{"data"}) = \frac{4}{24 \times 496} = \frac{4}{11,904} \approx \mathbf{0.000336}$

**3-Mark Question**: In Witten-Bell smoothing, conceptually explain the statistical intuition behind the fraction $\frac{T}{N+T}$ for calculating the total unseen probability mass.
> **Answer**: Think of every unique word type ($T$) as a historical "new word" event, and every total token ($N$) as a standard historical event. Out of the total $N+T$ events that explicitly occurred in the sequence's history, exactly $T$ of them were completely "new word" events. Therefore, the mathematical probability that the *very next* event will also be a "new word" event is strictly estimated as the relative frequency of "new word" events: $\frac{T}{N+T}$.

---

### Can You Explain This?
- [ ] I can explicitly state the difference between Tokens ($N$) and Types ($T$).
- [ ] I can write out the specific mathematical formula to calculate $Z$.
- [ ] I can manually calculate the Witten-Bell probability for a seen bigram.

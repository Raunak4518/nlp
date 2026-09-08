# Witten-Bell Smoothing

## 1. The Witten-Bell Intuition
Good-Turing uses the frequency of singletons to estimate the probability of unseen words. **Witten-Bell Smoothing** uses a different intuition: it estimates the probability of unseen words by looking at *how often a new word appears for the first time*.

Imagine reading a book. 
- In the first sentence, every word is a "new" word. 
- By chapter 10, almost every word you read is a word you've seen before. 
- Occasionally, the author uses a word you haven't seen yet.

Witten-Bell states: The probability of encountering an unseen word in the future is proportional to the number of *unique* words (types) you have already encountered in the past.

## 2. Tokens (N) vs Types (T)
To use Witten-Bell, we must understand two definitions for a given context $w_{i-1}$:
1. **Tokens ($N$)**: The total number of times the context $w_{i-1}$ occurred. (This is just the standard Unigram count).
2. **Types ($T$)**: The number of *unique* words that followed the context $w_{i-1}$.

**Example**:
Corpus: "the cat, the dog, the cat, the bird, the cat"
Context: "the"
- Tokens ($N$): "the" appears 5 times. $N = 5$.
- Types ($T$): "the" is followed by exactly 3 unique words: "cat", "dog", "bird". $T = 3$.

## 3. Probability Calculations

### Unseen Events
The total probability mass reserved for all unseen words following a specific context is calculated using $T$ and $N$:
$$ P(\text{unseen}) = \frac{T}{N + T} $$

If we want the probability of a *specific* unseen word, we divide that mass by the number of unseen words $Z$ (where $Z = |V| - T$):
$$ P(\text{specific unseen}) = \frac{T}{(N + T) \times Z} $$

### Seen Events
If a word actually occurred $c$ times after the context, its new smoothed probability is:
$$ P(\text{seen}) = \frac{c}{N + T} $$

*(Notice how similar this is to Laplace smoothing, where we used $\frac{c}{N + |V|}$. Witten-Bell uses $+T$ in the denominator instead of $+|V|$. Because $T \ll |V|$, Witten-Bell steals far less probability mass from seen words, preserving the true distribution much better).*

## 4. Numerical Problem Walkthrough

**Problem**:
Vocabulary Size $|V| = 1000$.
Context: "big"
"big" appears 100 times total ($N=100$).
"big" is followed by 10 unique words ($T=10$).
"big house" appears 40 times ($c=40$).
"big xylophone" never appears ($c=0$).

Calculate the Witten-Bell probability for "big house" and "big xylophone".

**Solution**:
1. Find $Z$ (the number of unseen types): $Z = |V| - T = 1000 - 10 = 990$.
2. Calculate "big house" (Seen event):
   $$ P(\text{"house"} | \text{"big"}) = \frac{c}{N + T} = \frac{40}{100 + 10} = \frac{40}{110} \approx 0.363 $$
3. Calculate "big xylophone" (Unseen event):
   $$ P(\text{"xylophone"} | \text{"big"}) = \frac{T}{(N + T) \times Z} = \frac{10}{110 \times 990} = \frac{10}{108,900} \approx 0.00009 $$

*(Self-Check: 10 seen words + 990 unseen words. 
Sum of all seen probabilities: We don't have individual counts, but we know total $c = N = 100$. So sum is $100/110$.
Sum of all unseen probabilities: $990 \times (10 / 108900) = 9900 / 108900 = 10/110$.
Total Sum: $100/110 + 10/110 = 110/110 = 1.0$. The math holds!)*

## 5. Exam Preparation
### Must Memorize
- Seen formula: $\frac{c}{N+T}$.
- Unseen formula: $\frac{T}{(N+T)Z}$.
- $Z = |V| - T$.

### Likely Theory Question
**Question**: In Witten-Bell smoothing, explain the intuition behind the fraction $\frac{T}{N+T}$ for unseen events.
**Answer**: Think of every unique word type ($T$) as a "new word" event, and every total token ($N$) as a standard event. Out of the $N+T$ total events in the sequence's history, exactly $T$ of them were "new word" events. Therefore, the probability that the *next* event is also a "new word" event is simply the relative frequency of "new word" events: $\frac{T}{N+T}$.

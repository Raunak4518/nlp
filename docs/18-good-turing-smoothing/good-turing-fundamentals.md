# Good-Turing Smoothing

## 1. The Good-Turing Intuition
Laplace smoothing (+1) uses an arbitrary, heavy-handed assumption. Add-k uses an optimized fractional assumption. **Good-Turing Smoothing** attempts to be strictly statistical: it mathematically uses the count of things you've seen exactly *once* to estimate the probability of things you've *never* seen.

Imagine you are fishing in a massive lake. Over a week, you catch 10 carp, 3 bass, 2 trout, 1 salmon, 1 catfish, and 1 eel. 
- You have seen 3 species exactly *once*. 
- The Good-Turing theorem states that the probability of the *very next fish* you catch being a brand-new, unseen species is mathematically proportional to the number of species you have only caught once (singletons).

---

## 2. Frequency of Frequencies ($N_c$)
To execute Good-Turing, we must calculate a concept called the **Frequency of Frequencies**. We mathematically define $N_c$ as the total number of distinct N-grams that occur exactly $c$ times in the training data.

Let's look at a tiny training corpus of bigrams:
- "the cat" *(appears 10 times)*
- "a dog" *(appears 10 times)*
- "my car" *(appears 2 times)*
- "his house" *(appears 2 times)*
- "red apple" *(appears 1 time)*
- "fast runner" *(appears 1 time)*
- "loud bell" *(appears 1 time)*

What are our $N_c$ values?
- **$N_{10} = 2$** *(Because exactly 2 distinct bigrams appear 10 times).*
- **$N_2 = 2$** *(Because exactly 2 distinct bigrams appear 2 times).*
- **$N_1 = 3$** *(Because exactly 3 distinct bigrams appear 1 time. These are called **singletons**).*
- **$N_0 = ?$** *(The massive number of mathematically possible bigrams that never appeared).*

---

## 3. Probability of Unseen Events
Good-Turing calculates the total, combined probability mass of *all* unseen events ($c=0$) using $N_1$.
$$ P(\text{all unseen combined}) = \frac{N_1}{N} $$
*(Where $N$ is the total count of all bigram tokens in the corpus).*

If we want to calculate the specific probability of just *one* specific unseen bigram (e.g., "blue sky"), we must divide that combined mass equally by $N_0$:
$$ P(\text{specific unseen}) = \frac{N_1}{N \times N_0} $$

---

## 4. Adjusted Count ($c^*$)
To ensure the total probabilities across the model still sum perfectly to 1.0, we must mathematically lower (discount) the counts of the things we *did* see to make room for the unseen mass. Good-Turing calculates an **adjusted count** ($c^*$) for every seen N-gram.

> [!IMPORTANT]
> **The Adjusted Count Formula**
> $$ c^* = \frac{(c + 1) \times N_{c+1}}{N_c} $$

If a bigram appeared $c = 2$ times in the training data, its new adjusted count is:
$$ 2^* = \frac{(3) \times N_3}{N_2} $$

---

## 5. Numerical Problem Walkthrough

**Provided Data**:
- Total bigram tokens $N = 100,000$.
- Total mathematically possible bigrams $|V|^2 = 1,000,000$.
- $N_1 = 1,500$ *(1500 bigrams appear exactly 1 time)*
- $N_2 = 400$
- $N_3 = 100$

**Question 1**: What is the probability of one specific unseen bigram?
1. Calculate $N_0$: Total possible bigrams minus all distinctly seen bigrams. Let's assume the sum of all seen distinct bigrams is $5,000$. 
   $N_0 = 1,000,000 - 5,000 = 995,000$.
2. $P(\text{specific unseen}) = \frac{N_1}{N \times N_0} = \frac{1500}{100,000 \times 995,000} \approx 1.5 \times 10^{-8}$.

**Question 2**: What is the adjusted count ($c^*$) for a bigram that appeared exactly 2 times?
1. $c = 2$. Therefore $c+1 = 3$.
2. $2^* = \frac{(3) \times N_3}{N_2} = \frac{3 \times 100}{400} = \frac{300}{400} = \mathbf{0.75}$.
*(Notice how the count was heavily discounted from 2.0 down to 0.75 to make room for the unseen events).*

---

## 6. The Fatal Limitation of Raw Good-Turing
Raw Good-Turing has a fatal mathematical flaw: what happens if $N_{c+1} = 0$? 

In real datasets, low counts are continuous ($N_1, N_2, N_3$ all exist). But for high counts, the data is sparse. What if the word "the" appears exactly 100 times, but absolutely no word in the entire corpus occurs exactly 101 times? Then $N_{101} = 0$.

If we try to calculate $c^*$ for the word "the" ($c=100$):
$$ 100^* = \frac{101 \times N_{101}}{N_{100}} = \frac{101 \times 0}{N_{100}} = \mathbf{0.0} $$

A highly frequent word's count suddenly mathematically collapses to exactly zero! This requires us to use **Good-Turing Regression** (covered in the next topic) to smooth the $N_c$ values themselves before applying the formula.

---

## 7. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: You are given a corpus with the following Frequency of Frequencies: $N_1 = 200, N_2 = 50, N_3 = 10$. Calculate the Good-Turing adjusted count ($c^*$) for an N-gram that appeared exactly 2 times. Show your formula.
> **Answer**: 
> **Formula**: $c^* = \frac{(c + 1) \times N_{c+1}}{N_c}$
> 
> **Variables**: $c = 2$. Therefore $c+1 = 3$.
> $N_2 = 50$. $N_3 = 10$.
> 
> **Calculation**:
> $c^* = \frac{3 \times 10}{50} = \frac{30}{50} = \mathbf{0.6}$

**3-Mark Question**: Explain the intuition behind using $N_1$ to estimate the total probability mass of unseen events in Good-Turing smoothing.
> **Answer**: In any statistical sample, the items you have seen exactly once (singletons, $N_1$) are the items that were right on the verge of not being seen at all. Statistically, the volume of singletons acts as a highly accurate proxy and predictor of the volume of completely unseen items that still exist in the broader, unobserved population.

---

### Can You Explain This?
- [ ] I can explicitly define the difference between the variables $c$ and $N_c$.
- [ ] I can write out the Good-Turing formula for the adjusted count $c^*$.
- [ ] I can explain mathematically why $N_{c+1} = 0$ causes the algorithm to crash for high-frequency words.

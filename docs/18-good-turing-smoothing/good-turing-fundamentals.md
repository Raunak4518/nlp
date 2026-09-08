# Good-Turing Smoothing

## 1. The Good-Turing Intuition
Laplace smoothing (+1) uses an arbitrary, heavy-handed assumption. Add-k uses an optimized fractional assumption. **Good-Turing Smoothing** attempts to be strictly mathematical: it uses the count of things you've seen *once* to estimate the probability of things you've *never* seen.

Imagine you are fishing in a lake. You catch 10 carp, 3 bass, 2 trout, 1 salmon, 1 catfish, and 1 eel. 
- You have seen 3 species exactly *once*. 
- Good-Turing states that the probability of the *next* fish you catch being a brand-new, unseen species is proportional to the number of species you have only caught once.

## 2. Frequency of Frequencies ($N_c$)
To use Good-Turing, we must calculate the **Frequency of Frequencies**. We define $N_c$ as the number of N-grams that occur exactly $c$ times in the training data.

Let's look at a corpus of bigrams:
- "the cat" (appears 10 times)
- "a dog" (appears 10 times)
- "my car" (appears 2 times)
- "his house" (appears 2 times)
- "red apple" (appears 1 time)
- "fast runner" (appears 1 time)
- "loud bell" (appears 1 time)

What are our $N_c$ values?
- $N_{10} = 2$ (Because exactly 2 bigrams appear 10 times).
- $N_2 = 2$ (Because exactly 2 bigrams appear 2 times).
- $N_1 = 3$ (Because exactly 3 bigrams appear 1 time. These are called **singletons**).
- $N_0 = ?$ (The number of mathematically possible bigrams that never appeared).

## 3. Probability of Unseen Events
Good-Turing calculates the total probability mass of all unseen events ($c=0$) using $N_1$.
$$ P(unseen) = \frac{N_1}{N} $$
*(Where $N$ is the total number of bigrams in the corpus).*

If we want the probability of a *specific* unseen bigram (e.g., "blue sky"), we divide that mass by $N_0$:
$$ P(\text{specific unseen}) = \frac{N_1}{N \times N_0} $$

## 4. Adjusted Count ($c^*$)
To ensure the total probabilities sum to 1.0, we must lower the counts of the things we *did* see to make room for the unseen mass. Good-Turing calculates an **adjusted count** ($c^*$) for every seen N-gram.

$$ c^* = \frac{(c + 1) \times N_{c+1}}{N_c} $$

If a bigram appeared $c = 2$ times, its new adjusted count is:
$$ 2^* = \frac{(3) \times N_3}{N_2} $$

## 5. Numerical Problem Walkthrough

**Data**:
- Total bigram tokens $N = 100,000$.
- Total possible bigrams $|V|^2 = 1,000,000$.
- $N_1 = 1,500$ (1500 bigrams appear exactly 1 time)
- $N_2 = 400$
- $N_3 = 100$

**Question 1**: What is the probability of a specific unseen bigram ("zero count")?
1. Calculate $N_0$: Total possible bigrams minus all seen bigrams. Let's assume the sum of all seen bigrams is $5,000$. $N_0 = 1,000,000 - 5,000 = 995,000$.
2. $P(\text{specific unseen}) = \frac{N_1}{N \times N_0} = \frac{1500}{100,000 \times 995,000} \approx 1.5 \times 10^{-8}$.

**Question 2**: What is the adjusted count ($c^*$) for a bigram that appeared exactly 2 times?
1. $c = 2$. Therefore $c+1 = 3$.
2. $2^* = \frac{(3) \times N_3}{N_2} = \frac{3 \times 100}{400} = \frac{300}{400} = 0.75$.
*(Notice how the count was discounted from 2.0 down to 0.75).*

## 6. Limitations of Raw Good-Turing
Raw Good-Turing has a fatal flaw: what happens if $N_{c+1} = 0$? 
If no bigrams in the entire corpus occur exactly 101 times, then $N_{101} = 0$.
If we try to calculate $c^*$ for a bigram that occurred 100 times:
$$ 100^* = \frac{101 \times N_{101}}{N_{100}} = \frac{101 \times 0}{N_{100}} = 0 $$
A highly frequent bigram's count suddenly collapses to exactly zero! This requires us to use Good-Turing Regression (covered in the next topic) to smooth the $N_c$ values themselves.

## 7. Exam Preparation
### Must Memorize
- The $c^*$ formula: $c^* = (c + 1) \frac{N_{c+1}}{N_c}$.
- Unseen mass is estimated using $N_1$ (singletons).

### Likely Theory Question
**Question**: Explain the intuition behind using $N_1$ to estimate the probability of unseen events in Good-Turing smoothing.
**Answer**: In any sample, the things you have seen exactly once ($N_1$) are the things that are right on the verge of not being seen at all. Statistically, the number of singletons is a highly accurate predictor of the number of completely unseen species (or N-grams) that exist in the broader population.

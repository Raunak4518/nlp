# N-gram Probabilities

## 1. Calculating N-gram Probabilities via MLE
As covered in the Probability module, we use Maximum Likelihood Estimation (MLE) to estimate probabilities by dividing counts from our training corpus.

### Unigram Probability
$$ P_{MLE}(w_i) = \frac{\text{Count}(w_i)}{\text{Total Words in Corpus}} $$

### Bigram Probability
$$ P_{MLE}(w_i | w_{i-1}) = \frac{\text{Count}(w_{i-1}, w_i)}{\text{Count}(w_{i-1})} $$
*(Note: We divide the count of the bigram by the count of the unigram that begins it).*

### Trigram Probability
$$ P_{MLE}(w_i | w_{i-2}, w_{i-1}) = \frac{\text{Count}(w_{i-2}, w_{i-1}, w_i)}{\text{Count}(w_{i-2}, w_{i-1})} $$
*(Note: We divide the count of the trigram by the count of the bigram that begins it).*

## 2. Calculating Sentence Probability
Once we have our MLE tables calculated for our vocabulary, we can calculate the probability of any sentence.

Assume a **Bigram Model**:
$$ P(\text{I saw the cat}) \approx P(\text{I}) \times P(\text{saw} | \text{I}) \times P(\text{the} | \text{saw}) \times P(\text{cat} | \text{the}) $$

## 3. Numerical Problem Walkthrough

**The Corpus**:
1. "I am Sam"
2. "Sam I am"
3. "I do not like green eggs and ham"

**Question 1**: What is the Unigram probability of "I"?
- Total words in corpus: $3 + 3 + 8 = 14$.
- Count("I"): $3$.
- **Answer**: $P(\text{"I"}) = 3 / 14 \approx 0.214$.

**Question 2**: What is the Bigram probability $P(\text{"am"} | \text{"I"})$?
- Count("I"): $3$.
- Count("I am"): $2$. (Occurs in sentence 1 and sentence 2).
- **Answer**: $P(\text{"am"} | \text{"I"}) = 2 / 3 \approx 0.667$.

**Question 3**: What is the Bigram probability $P(\text{"do"} | \text{"I"})$?
- Count("I"): $3$.
- Count("I do"): $1$. (Occurs in sentence 3).
- **Answer**: $P(\text{"do"} | \text{"I"}) = 1 / 3 \approx 0.333$.

*(Self-Check: Notice that $P(\text{"am"} | \text{"I"}) + P(\text{"do"} | \text{"I"}) = 2/3 + 1/3 = 1.0$. This is correct, because "am" and "do" are the only two words that ever follow "I" in this tiny corpus).*

**Question 4**: Calculate the probability of the sentence "I am" using a Bigram model.
- $P(\text{"I am"}) = P(\text{"I"}) \times P(\text{"am"} | \text{"I"})$
- $P(\text{"I am"}) = (3 / 14) \times (2 / 3) = 6 / 42 \approx 0.142$.

## 4. Exam Preparation
### Must Memorize
- The formulas for Unigram, Bigram, and Trigram MLE probabilities. Always remember that the denominator is the count of the $n-1$ gram context.

### Likely Practical Question
**Question**: Using the corpus above, what is $P(\text{"Sam"} | \text{"am"})$?
**Answer**: 
- Count("am"): $2$.
- Count("am Sam"): $1$. (Occurs in sentence 1).
- $P(\text{"Sam"} | \text{"am"}) = 1 / 2 = 0.5$.

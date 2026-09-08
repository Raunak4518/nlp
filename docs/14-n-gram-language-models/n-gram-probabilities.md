# N-gram Probabilities

## 1. Calculating N-gram Probabilities via MLE
As covered in the Probability module, we use Maximum Likelihood Estimation (MLE) to mathematically estimate probabilities by dividing actual sequence counts extracted from our training corpus.

> [!IMPORTANT]
> **The Golden Rule of MLE Fractions**
> The numerator is always the count of the full N-gram. The denominator is always the count of the $(N-1)$-gram context that precedes the final word.

### Unigram Probability (N=1)
$$ P_{MLE}(w_i) = \frac{\text{Count}(w_i)}{\text{Total Words in Corpus}} $$

### Bigram Probability (N=2)
$$ P_{MLE}(w_i \mid w_{i-1}) = \frac{\text{Count}(w_{i-1}, w_i)}{\text{Count}(w_{i-1})} $$
*(Note: We divide the count of the 2-word bigram by the count of the 1-word unigram that begins it).*

### Trigram Probability (N=3)
$$ P_{MLE}(w_i \mid w_{i-2}, w_{i-1}) = \frac{\text{Count}(w_{i-2}, w_{i-1}, w_i)}{\text{Count}(w_{i-2}, w_{i-1})} $$
*(Note: We divide the count of the 3-word trigram by the count of the 2-word bigram that begins it).*

---

## 2. Calculating Sentence Probability
Once we have our MLE tables calculated for our entire vocabulary, we can calculate the mathematical probability of any full sentence being spoken.

Assume a **Bigram Model**:
$$ P(\text{I saw the cat}) \approx P(\text{I}) \times P(\text{saw} \mid \text{I}) \times P(\text{the} \mid \text{saw}) \times P(\text{cat} \mid \text{the}) $$

---

## 3. Numerical Problem Walkthrough

**The Training Corpus**:
1. "I am Sam"
2. "Sam I am"
3. "I do not like green eggs and ham"

**Question 1**: What is the Unigram probability of "I"?
- Total words in corpus: $3 + 3 + 8 = 14$.
- Count("I"): $3$.
- **Answer**: $P(\text{"I"}) = 3 / 14 \approx 0.214$.

**Question 2**: What is the Bigram probability $P(\text{"am"} \mid \text{"I"})$?
- Count("I"): $3$.
- Count("I am"): $2$. (Occurs in sentence 1 and sentence 2).
- **Answer**: $P(\text{"am"} \mid \text{"I"}) = 2 / 3 \approx 0.667$.

**Question 3**: What is the Bigram probability $P(\text{"do"} \mid \text{"I"})$?
- Count("I"): $3$.
- Count("I do"): $1$. (Occurs only in sentence 3).
- **Answer**: $P(\text{"do"} \mid \text{"I"}) = 1 / 3 \approx 0.333$.

*(Self-Check: Notice that $P(\text{"am"} \mid \text{"I"}) + P(\text{"do"} \mid \text{"I"}) = 2/3 + 1/3 = 1.0$. This is mathematically correct, because "am" and "do" are the absolutely only two words that ever follow "I" in this tiny, restricted corpus. The probabilities must sum to 1.0).*

**Question 4**: Calculate the total probability of the sentence "I am" using a Bigram model.
- $P(\text{"I am"}) = P(\text{"I"}) \times P(\text{"am"} \mid \text{"I"})$
- $P(\text{"I am"}) = (3 / 14) \times (2 / 3) = 6 / 42 \approx 0.142$.

---

## 4. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: Using the corpus provided above, calculate the probability of the sentence "Sam I do" using a Bigram Model. Show your work.
> **Answer**: 
> $P(\text{"Sam I do"}) \approx P(\text{"Sam"}) \times P(\text{"I"} \mid \text{"Sam"}) \times P(\text{"do"} \mid \text{"I"})$
> 
> 1. $P(\text{"Sam"}) = \text{Count}(\text{"Sam"}) / \text{Total Words} = 2 / 14$
> 2. $P(\text{"I"} \mid \text{"Sam"}) = \text{Count}(\text{"Sam I"}) / \text{Count}(\text{"Sam"}) = 1 / 2$
> 3. $P(\text{"do"} \mid \text{"I"}) = \text{Count}(\text{"I do"}) / \text{Count}(\text{"I"}) = 1 / 3$
> 
> $P(\text{"Sam I do"}) = (2/14) \times (1/2) \times (1/3) = 2/84 \approx 0.0238$

**2-Mark Question**: Write the mathematical formula for the MLE Trigram probability of the word "apples" given the context "I like".
> **Answer**: 
> $$ P_{MLE}(\text{"apples"} \mid \text{"I", "like"}) = \frac{\text{Count}(\text{"I like apples"})}{\text{Count}(\text{"I like"})} $$

---

### Can You Explain This?
- [ ] I can write the formulas for Unigram, Bigram, and Trigram MLE probabilities.
- [ ] I understand why the denominator of a Bigram probability is the count of a Unigram.
- [ ] I can manually calculate the probability of a sentence using a toy corpus and the Chain Rule.

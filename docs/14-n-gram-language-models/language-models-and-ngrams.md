# Language Models and N-grams

## 1. What is a Language Model?
A **Language Model (LM)** is a statistical model that estimates the mathematical probability of a sequence of words. 
It answers the fundamental question: *"How mathematically likely is it that someone would actually say this exact sentence in this specific language?"*

- $P(\text{"I like apples"}) = 0.05$ *(High probability, normal English sentence)*
- $P(\text{"Apples I like"}) = 0.0001$ *(Low probability, weird syntax)*
- $P(\text{"I xylophone apples"}) \approx 0.0$ *(Extremely low probability, grammatically invalid)*

By extension, because of the Chain Rule of probability, an LM can also calculate the probability of the **next token** given all the previous tokens: $P(w_{n} \mid w_1, ..., w_{n-1})$.

---

## 2. The N-Gram Assumption

As we learned in the Probability Foundations module, the strict, true mathematical probability of a sentence relies on the Chain Rule:
$$ P(w_1, w_2, w_3) = P(w_1) \times P(w_2 \mid w_1) \times P(w_3 \mid w_1, w_2) $$

If the sentence has 20 words, the final term in the equation is $P(w_{20} \mid w_1, w_2, ..., w_{19})$. 
To estimate this final term using Maximum Likelihood Estimation (MLE), we would need to count how many times that exact, specific 19-word sequence occurred in our training data. Unless our training data is infinitely large, that count will almost certainly be 0, crashing the equation.

To solve this, we make the **Markov Assumption**: We assume that the probability of a word *only* depends on the immediately preceding $n-1$ words, discarding the rest of the history. This defines an **N-gram Language Model**.

---

## 3. Types of N-gram Models

### Unigram Model ($n=1$)
Assumes the probability of a word depends on **absolutely nothing**. Words are drawn independently from a bag. It completely destroys word order.
$$ P(w_1, w_2, w_3) \approx P(w_1) \times P(w_2) \times P(w_3) $$
- *Generated Text*: `"the the cat a run to"` (Total gibberish).

### Bigram Model ($n=2$)
Assumes the probability of a word depends **only on the exactly 1 immediately preceding word**.
$$ P(w_1, w_2, w_3) \approx P(w_1) \times P(w_2 \mid w_1) \times P(w_3 \mid w_2) $$
- *Generated Text*: `"I want to the store."` (Locally grammatical because "to the" and "the store" make sense, but globally incoherent).

### Trigram Model ($n=3$)
Assumes the probability of a word depends on the **2 preceding words**.
$$ P(w_1, w_2, w_3, w_4) \approx P(w_1, w_2) \times P(w_3 \mid w_1, w_2) \times P(w_4 \mid w_2, w_3) $$
- *Generated Text*: `"I want to go to the store."` (Much more globally coherent).

---

## 4. The Curse of Dimensionality

If Trigrams are better than Bigrams, why don't we use 10-gram models to generate perfect text? 

As $n$ increases, the model generates more fluent text because it has more context. However, as $n$ increases, the number of possible n-grams explodes mathematically (Vocabulary Size $|V|^n$). 

If your vocabulary has just 10,000 words, there are $10,000^{10}$ possible 10-grams. Storing the counts for these would require more RAM memory than physically exists on Earth, and almost all of those counts would be exactly 0 anyway, resulting in massive data sparsity. Historically, classical NLP models rarely exceeded Trigrams or 4-grams for this exact reason.

---

## 5. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: Define the Markov Assumption in the context of Language Modeling. Write out the Chain Rule approximation for the sentence "The cat sat" using a Trigram model.
> **Answer**: 
> The Markov Assumption states that the probability of predicting the next word in a sequence does not depend on the entire history of the sentence, but only on a fixed window of the preceding $n-1$ words. This simplifies the Chain Rule and prevents data sparsity.
> 
> **Trigram Approximation** ($n=3$, looking back 2 words):
> $P(\text{The, cat, sat}) \approx P(\text{The}) \times P(\text{cat} \mid \text{The}) \times P(\text{sat} \mid \text{The, cat})$

**2-Mark Question**: What is the formula for calculating the total number of distinct n-grams that can be extracted from a sentence of length $N$? How many bigrams are in a 10-word sentence?
> **Answer**: 
> The formula is $N - n + 1$.
> For a 10-word sentence ($N=10$) extracting bigrams ($n=2$): $10 - 2 + 1 = 9$ bigrams.

---

### Can You Explain This?
- [ ] I can formally define what a Language Model is mathematically trying to compute.
- [ ] I can explain what the Markov Assumption is and why it mathematically prevents probability equations from returning 0.0.
- [ ] I can explain why a Bigram model only looks back at exactly 1 previous word, not 2.
- [ ] I understand the "Curse of Dimensionality" regarding huge values of $n$.

# Language Models and N-grams

## 1. What is a Language Model?
A **Language Model (LM)** is a statistical model that estimates the probability of a sequence of words. 
It answers the question: "How likely is it that someone would actually say this sentence in this language?"

- $P(\text{"I like apples"}) = 0.05$ (High probability)
- $P(\text{"Apples I like"}) = 0.0001$ (Low probability)
- $P(\text{"I xylophone apples"}) = 0.0000000001$ (Extremely low probability)

By extension, because of the Chain Rule, an LM can also calculate the probability of the **next token** given the previous tokens: $P(w_{n} | w_1, ..., w_{n-1})$.

## 2. The N-Gram Assumption
As we learned in the Probability Foundations module, the strict probability of a sentence is:
$$ P(w_1, w_2, w_3) = P(w_1) \times P(w_2|w_1) \times P(w_3|w_1, w_2) $$

If the sentence has 20 words, the final term is $P(w_{20} | w_1, w_2, ..., w_{19})$. 
To estimate this using MLE, we would need to count how many times that exact 19-word sequence occurred in our training data. Unless our training data is infinitely large, that count will almost certainly be 0.

To solve this, we make the **Markov Assumption**: We assume that the probability of a word only depends on the previous $n-1$ words. This defines an **N-gram Language Model**.

## 3. Types of N-gram Models

### Unigram Model ($n=1$)
Assumes the probability of a word depends on **nothing**. Words are drawn independently from a bag.
$$ P(w_1, w_2, w_3) \approx P(w_1) \times P(w_2) \times P(w_3) $$
- *Generated Text*: "the the cat a run to" (Total gibberish).

### Bigram Model ($n=2$)
Assumes the probability of a word depends **only on the immediately preceding word**.
$$ P(w_1, w_2, w_3) \approx P(w_1) \times P(w_2|w_1) \times P(w_3|w_2) $$
- *Generated Text*: "I want to the store." (Locally grammatical, but globally incoherent).

### Trigram Model ($n=3$)
Assumes the probability of a word depends on the **two preceding words**.
$$ P(w_1, w_2, w_3, w_4) \approx P(w_1, w_2) \times P(w_3|w_1, w_2) \times P(w_4|w_2, w_3) $$
- *Generated Text*: "I want to go to the store." (Much more coherent).

### 4-gram and Beyond
As $n$ increases, the model generates more fluent text because it has more context. However, as $n$ increases, the number of possible n-grams explodes (Vocabulary Size $|V|^n$), requiring exponentially more RAM and causing massive data sparsity issues (which we will cover in the next module). 

## 4. Word vs Character N-grams
- **Word N-grams**: The standard for Language Modeling and text generation (e.g., predicting the next word).
- **Character N-grams**: Predicting the next character. Used for Language Identification (as seen in Module 10) and spelling correction.

## 5. Exam Preparation
### Must Memorize
- The definition of the Markov Assumption: The probability of a word depends only on a limited history of preceding words, not the entire sentence.
- Number of n-grams formula: For a sequence of length $N$, there are $N - n + 1$ n-grams.

### Likely Theory Question
**Question**: Why don't we use 10-gram models in classical NLP if they produce better text?
**Answer**: Because of the "Curse of Dimensionality." If your vocabulary has 10,000 words, there are $10,000^{10}$ possible 10-grams. Storing the counts for these would require more memory than exists on Earth, and almost all of those counts would be exactly 0 anyway, resulting in massive data sparsity.

# Probability Basics

## 1. What is Probability?
Probability is the rigorous mathematical measure of how likely a specific event is to occur. In NLP, "events" are usually the occurrence of specific words, sequences of words, or grammatical tags.
- Probabilities always mathematically range from $0.0$ (absolutely impossible) to $1.0$ (absolutely certain).
- $P(A)$ denotes the probability of event $A$ occurring.

---

## 2. Joint Probability
The probability that two events $A$ and $B$ occur together simultaneously.
- Denoted mathematically as $P(A, B)$ or $P(A \cap B)$.
- *Example*: The probability that a word is a NOUN **and** it is the specific word "bank".
- *Visual*: The intersection of two circles in a Venn diagram.

---

## 3. Conditional Probability
The probability that event $A$ occurs, **given** the mathematical certainty that event $B$ has already occurred.
- Denoted as $P(A \mid B)$.
- *Formula*: $P(A \mid B) = \frac{P(A, B)}{P(B)}$
- *Example*: Given that the previous word was already observed to be "the", what is the probability that the next word is "cat"? This is written as $P(\text{"cat"} \mid \text{"the"})$.

> [!WARNING]
> **A Very Common Mistake**
> Do not confuse $P(A, B)$ with $P(A \mid B)$. 
> - $P(\text{"cat"}, \text{"the"})$ asks: "Out of ALL two-word sequences in the entire English language, how many of them are exactly 'the cat'?" (A very small number).
> - $P(\text{"cat"} \mid \text{"the"})$ asks: "Look *only* at the sequences that start with 'the'. Out of just those, how many are followed by 'cat'?" (A much larger number).

---

## 4. Marginal Probability
If you know the joint probabilities of $A$ and $B$, but you only care about isolating the total probability of $A$, you can "marginalize out" $B$ by summing over all possible states of $B$.
- *Formula*: $P(A) = \sum_{b} P(A, B=b)$
- *Example*: The total probability of the word "bank" appearing in a text is the mathematical sum of the joint probability of it appearing as a Noun and the joint probability of it appearing as a Verb. 
  $P(\text{bank}) = P(\text{bank, NOUN}) + P(\text{bank, VERB})$.

---

## 5. Probability Normalization
For a set of mutually exclusive and exhaustive events (e.g., trying to guess what the single next word will be out of an entire vocabulary $V$), their probabilities must mathematically sum to exactly $1.0$.

$$ \sum_{w \in V} P(w) = 1.0 $$

If you calculate raw occurrence scores for events (like simple word counts), you must **normalize** them into valid mathematical probabilities by dividing each individual score by the sum of all scores.

---

## 6. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: You are building a predictive keyboard. You observe the following raw frequency counts for the next word typed after the phrase "I like": `apples: 5`, `bananas: 3`, `cars: 2`. Convert these raw counts into a normalized probability distribution. Show your work and prove that it is a valid distribution.
> **Answer**:
> 1. Find the total sum of the occurrences: $5 + 3 + 2 = 10$.
> 2. Divide each individual count by the total sum to normalize.
>    - $P(\text{apples} \mid \text{"I like"}) = 5 / 10 = 0.5$
>    - $P(\text{bananas} \mid \text{"I like"}) = 3 / 10 = 0.3$
>    - $P(\text{cars} \mid \text{"I like"}) = 2 / 10 = 0.2$
> 3. To prove it is a valid distribution, the sum of all probabilities in the mutually exclusive set must equal $1.0$.
>    - $0.5 + 0.3 + 0.2 = 1.0$.

**2-Mark Question**: Write the mathematical formula for Conditional Probability $P(A \mid B)$.
> **Answer**: $P(A \mid B) = \frac{P(A, B)}{P(B)}$

---

### Can You Explain This?
- [ ] I can explain the difference between Joint and Conditional probability.
- [ ] I can write the formula for Conditional Probability.
- [ ] I know how to normalize a set of raw counts into valid probabilities.

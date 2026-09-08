# Probability Basics

## 1. What is Probability?
Probability is the mathematical measure of how likely an event is to occur. In NLP, events are usually the occurrence of specific words, sequences of words, or grammatical tags.
- Probabilities always range from $0.0$ (impossible) to $1.0$ (certain).
- $P(A)$ denotes the probability of event $A$.

## 2. Joint Probability
The probability that two events $A$ and $B$ occur together.
- Denoted as $P(A, B)$ or $P(A \cap B)$.
- *Example*: The probability that a word is a NOUN **and** it is the word "bank".

## 3. Conditional Probability
The probability that event $A$ occurs, **given** that event $B$ has already occurred.
- Denoted as $P(A | B)$.
- *Formula*: $P(A | B) = \frac{P(A, B)}{P(B)}$
- *Example*: Given that the previous word was "the", what is the probability that the next word is "cat"? $P(\text{"cat"} | \text{"the"})$.

## 4. Marginal Probability
If you know the joint probabilities of $A$ and $B$, but you only care about $A$, you can "marginalize out" $B$ by summing over all possible states of $B$.
- *Formula*: $P(A) = \sum_{b} P(A, B=b)$
- *Example*: The probability of the word "bank" appearing is the sum of the joint probabilities of it appearing as a Noun and appearing as a Verb. $P(\text{bank}) = P(\text{bank, NOUN}) + P(\text{bank, VERB})$.

## 5. Probability Normalization
For a set of mutually exclusive and exhaustive events (e.g., all words in a vocabulary $V$), their probabilities must sum to exactly $1.0$.
$$ \sum_{w \in V} P(w) = 1.0 $$

If you calculate raw scores for events, you **normalize** them into valid probabilities by dividing each score by the sum of all scores.

## 6. Exam Preparation
### Must Memorize
- The definition and formula for Conditional Probability: $P(A | B) = P(A, B) / P(B)$.
- Probabilities must always sum to 1.0.

### Likely Practical Question
**Question**: You are given the following raw counts for the next word after "I like": `apples: 5`, `bananas: 3`, `cars: 2`. Convert these counts into normalized probabilities.
**Answer**:
1. Find the sum: $5 + 3 + 2 = 10$.
2. Divide each count by the sum.
   - $P(\text{apples} | \text{"I like"}) = 5 / 10 = 0.5$
   - $P(\text{bananas} | \text{"I like"}) = 3 / 10 = 0.3$
   - $P(\text{cars} | \text{"I like"}) = 2 / 10 = 0.2$
(Notice how $0.5 + 0.3 + 0.2 = 1.0$).

# Bayes Theorem and The Chain Rule

## 1. Bayes' Theorem
Bayes' Theorem provides a way to reverse conditional probabilities. It allows us to calculate $P(A|B)$ if we only know $P(B|A)$.

$$ P(A|B) = \frac{P(B|A) \times P(A)}{P(B)} $$

### Terminology
- **$P(A)$**: The **Prior** probability (what we believed before seeing evidence B).
- **$P(B|A)$**: The **Likelihood** (the probability of the evidence B given that A is true).
- **$P(A|B)$**: The **Posterior** probability (our new belief after seeing evidence B).
- **$P(B)$**: The **Evidence** (often ignored in classification tasks because it is the same for all classes).

### Application in NLP (Naive Bayes)
If we want to classify a document $D$ as Spam or Not Spam ($C$):
$$ P(C|D) \propto P(D|C) \times P(C) $$
We find the probability of the class given the document by multiplying the likelihood of the document given the class by the prior probability of that class.

## 2. The Chain Rule of Probability
The Chain Rule allows us to calculate the joint probability of a sequence of events by multiplying their conditional probabilities.

For two events:
$$ P(A, B) = P(A) \times P(B|A) $$

For a sequence of $n$ events (like words in a sentence $w_1, w_2, ..., w_n$):
$$ P(w_1, w_2, ..., w_n) = P(w_1) \times P(w_2|w_1) \times P(w_3|w_1, w_2) \dots \times P(w_n|w_1, ..., w_{n-1}) $$

### Why this matters
To calculate the probability of the sentence "The cat sat", we use the chain rule:
$P(\text{The, cat, sat}) = P(\text{The}) \times P(\text{cat | The}) \times P(\text{sat | The cat})$

This exact equation is the mathematical foundation of all Language Models (including ChatGPT).

## 3. Exam Preparation
### Must Memorize
- Bayes Theorem: $P(A|B) = \frac{P(B|A)P(A)}{P(B)}$
- The Chain Rule formula.

### Likely Practical Question
**Question**: Using the Chain Rule of Probability, write the expansion for the joint probability $P(X_1, X_2, X_3)$.
**Answer**: $P(X_1, X_2, X_3) = P(X_1) \times P(X_2|X_1) \times P(X_3|X_1, X_2)$

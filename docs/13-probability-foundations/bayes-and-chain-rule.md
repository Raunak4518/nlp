# Bayes Theorem and The Chain Rule

## 1. Bayes' Theorem
Bayes' Theorem provides a mathematical way to reverse conditional probabilities. It allows us to calculate $P(A \mid B)$ if we only know $P(B \mid A)$.

$$ P(A \mid B) = \frac{P(B \mid A) \times P(A)}{P(B)} $$

### Terminology
In machine learning, we often use specific terminology for the components of Bayes' Theorem:
- **$P(A)$**: The **Prior** probability (what we believed about event $A$ *before* seeing any new evidence).
- **$P(B \mid A)$**: The **Likelihood** (the probability of observing the evidence $B$ given that $A$ is true).
- **$P(A \mid B)$**: The **Posterior** probability (our new, updated belief about $A$ *after* seeing the evidence $B$).
- **$P(B)$**: The **Evidence** (often ignored in classification math because it remains a constant denominator for all classes being compared).

### Application in NLP (Naive Bayes)
If we want to classify a document $D$ as Spam or Not Spam ($C$):
$$ P(C \mid D) \propto P(D \mid C) \times P(C) $$
We find the probability of the class given the document by multiplying the Likelihood of the document given the class by the Prior probability of that class existing in the wild.

---

## 2. The Chain Rule of Probability
The Chain Rule is arguably the most important statistical law in NLP. It allows us to calculate the **joint probability** of an entire sequence of events by multiplying their **conditional probabilities** together sequentially.

For two events:
$$ P(A, B) = P(A) \times P(B \mid A) $$

For a sequence of $n$ events (like words in a sentence $w_1, w_2, ..., w_n$):
$$ P(w_1, w_2, ..., w_n) = P(w_1) \times P(w_2 \mid w_1) \times P(w_3 \mid w_1, w_2) \dots \times P(w_n \mid w_1, ..., w_{n-1}) $$

### Why this matters
To calculate the total probability of a user typing the sentence *"The cat sat"*, we use the chain rule:
$$ P(\text{The, cat, sat}) = P(\text{The}) \times P(\text{cat} \mid \text{The}) \times P(\text{sat} \mid \text{The cat}) $$

> [!IMPORTANT]
> This exact mathematical equation is the absolute foundation of all Language Models (including modern LLMs like ChatGPT). Language Generation is simply calculating the Chain Rule over and over again to find the most probable next word given the entire sequence of previous words.

---

## 3. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: Using the Chain Rule of Probability, write out the full mathematical expansion for calculating the joint probability of the 4-word sequence `[w1, w2, w3, w4]`.
> **Answer**: 
> $$ P(w_1, w_2, w_3, w_4) = P(w_1) \times P(w_2 \mid w_1) \times P(w_3 \mid w_1, w_2) \times P(w_4 \mid w_1, w_2, w_3) $$

**3-Mark Question**: Write the formula for Bayes' Theorem and label the Prior, Likelihood, and Posterior.
> **Answer**: 
> $$ P(A \mid B) = \frac{P(B \mid A) \times P(A)}{P(B)} $$
> - **Posterior**: $P(A \mid B)$
> - **Likelihood**: $P(B \mid A)$
> - **Prior**: $P(A)$

---

### Can You Explain This?
- [ ] I can write Bayes' Theorem from memory.
- [ ] I can write the Chain Rule expansion for 3 variables from memory.
- [ ] I can explain how the Chain Rule applies to predicting the next word in a sentence.

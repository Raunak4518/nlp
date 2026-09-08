# Text Classification and Naive Bayes

## 1. What is Text Classification?
Text Classification is the fundamental Supervised NLP task of algorithmic assigning a predefined category (or label) to a given document based on its contents.
- **Spam Filtering**: Assigning an incoming email to the `SPAM` or `NOT SPAM` bucket.
- **Topic Modeling**: Automatically assigning a news article to `SPORTS`, `POLITICS`, or `TECH`.
- **Sentiment Analysis**: Assigning an IMDB movie review to `POSITIVE` or `NEGATIVE`.

---

## 2. Feature Extraction
Mathematical algorithms cannot read raw text directly. Before classifying any document, we must mathematically convert the text into a numerical vector representation (as extensively covered in Module 12).
1. **Bag of Words (BoW) / Count Features**: We represent the document as a sparse vector of raw word frequencies.
2. **TF-IDF Features**: We represent the document as a vector of TF-IDF scores, mathematically down-weighting overly common stop-words.

---

## 3. Naive Bayes Classification
**Naive Bayes** is a classical, highly efficient, generative statistical algorithm universally used for baseline text classification. It is based directly on Bayes' Theorem (Module 13).

$$ P(C \mid D) = \frac{P(D \mid C) \times P(C)}{P(D)} $$

Where:
- **$P(C \mid D)$**: The Posterior probability that the specific document $D$ belongs to Class $C$. (This is what we want to calculate).
- **$P(D \mid C)$**: The Likelihood of seeing the exact words in document $D$ given that it is definitely in Class $C$.
- **$P(C)$**: The Prior probability of Class $C$ existing in the wild (e.g., are 80% of all emails historically spam?).
- **$P(D)$**: The Evidence (We permanently drop this denominator in classification because it is exactly the same mathematically for all classes we are comparing).

### Why is it called "Naive"?
To rigorously calculate the Likelihood $P(D \mid C)$ for a document containing $N$ words, we would normally use the Chain Rule: $P(w_1, w_2, \dots, w_N \mid C)$. 

However, calculating exact N-gram probabilities for entire documents suffers from extreme, fatal Data Sparsity. The algorithm is famously called "Naive" because it makes a wildly incorrect, brute-force assumption to solve this: **it mathematically assumes that every single word in the document is completely independent of every other word, completely ignoring grammar and word order.**

Because of this "naive" independence assumption, the complex Likelihood simplifies beautifully into simply multiplying the individual unigram probabilities together:

> [!IMPORTANT]
> **The Naive Independence Assumption**
> $$ P(D \mid C) \approx P(w_1 \mid C) \times P(w_2 \mid C) \times \dots \times P(w_N \mid C) $$

---

## 4. Multinomial Naive Bayes & Laplace Smoothing
When classifying text, we specifically use the **Multinomial** variant of Naive Bayes, which calculates the probability $P(w_i \mid C)$ using the raw frequency counts of words found inside the training documents for that specific class.

$$ P_{MLE}(w_i \mid C) = \frac{\text{Count of } w_i \text{ in all documents of Class } C}{\text{Total words in all documents of Class } C} $$

**The Fatal Zero-Probability Problem**: If the word "Rolex" never physically appeared in the `NOT SPAM` training emails, then $P(\text{"Rolex"} \mid \text{NOT SPAM}) = 0.0$. If a brand new, legitimate work email arrives containing the word "Rolex", the Naive Bayes chain multiplication will instantly evaluate to exactly $0.0$, making it mathematically impossible to classify the email correctly.

**The Absolute Solution**: We MUST forcefully apply **Laplace Smoothing (+1)** when calculating the likelihoods.
$$ P(w_i \mid C) = \frac{\text{Count}(w_i \text{ in } C) + 1}{\text{Total Words in } C + |V|} $$

---

## 5. Scratch Implementation (Naive Bayes in Log Space)
As covered in Module 23, multiplying thousands of probabilities causes hardware Underflow. A real Naive Bayes implementation **must** add Log Probabilities.

```python
import math
from collections import defaultdict

class NaiveBayesClassifier:
    def __init__(self):
        self.vocab = set()
        self.class_word_counts = defaultdict(lambda: defaultdict(int))
        self.class_total_words = defaultdict(int)
        self.class_doc_counts = defaultdict(int)
        self.total_docs = 0

    def train(self, documents: list[str], labels: list[str]):
        """Trains the classifier by counting frequencies."""
        self.total_docs = len(documents)
        for doc, label in zip(documents, labels):
            self.class_doc_counts[label] += 1
            for word in doc.lower().split():
                self.vocab.add(word)
                self.class_word_counts[label][word] += 1
                self.class_total_words[label] += 1

    def predict(self, document: str) -> str:
        """Predicts the class using Log Probabilities and Laplace Smoothing."""
        best_class = None
        highest_prob = float('-inf')

        # To mathematically prevent underflow, use Log Probabilities (adding instead of multiplying)
        for label in self.class_doc_counts.keys():
            # 1. Log Prior P(C)
            prior = math.log(self.class_doc_counts[label] / self.total_docs)
            
            # 2. Log Likelihood P(D|C) with Laplace (+1) Smoothing
            likelihood = 0.0
            for word in document.lower().split():
                if word in self.vocab: # Ignore completely OOV words
                    count = self.class_word_counts[label][word]
                    total = self.class_total_words[label]
                    # Apply Laplace +1 and +V
                    prob = (count + 1) / (total + len(self.vocab))
                    likelihood += math.log(prob)
            
            # 3. P(C|D) is proportional to Prior + Likelihood
            total_prob = prior + likelihood
            
            if total_prob > highest_prob:
                highest_prob = total_prob
                best_class = label
                
        return best_class

# --- Usage ---
# nb = NaiveBayesClassifier()
# nb.train(training_docs, training_labels)
# print(nb.predict("free money for noon meeting")) 
```

---

## 6. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: You are building a Naive Bayes Spam filter. Why is it mathematically catastrophic if a completely valid, non-spam email contains a typo (e.g., "helloo") that never appeared in your training data? Name and define the specific mathematical technique used to permanently fix this.
> **Answer**: 
> If the word "helloo" never appeared in the training data for the Non-Spam class, its Maximum Likelihood probability $P(\text{"helloo"} \mid \text{Non-Spam})$ will be exactly $0.0$. Because the "Naive" assumption calculates the final document probability by mathematically multiplying all individual word probabilities together ($P(w_1) \times P(w_2) \dots$), a single $0.0$ will cause the entire equation to collapse to $0.0$. The model will incorrectly conclude that there is a 0% chance the email is Non-Spam.
> 
> This is permanently fixed by applying **Laplace Smoothing**. This technique mathematically adds an artificial $+1$ to the count of every single word (and adds the total Vocabulary size $|V|$ to the denominator) to rigorously ensure no probability can ever physically equal zero.

**2-Mark Question**: Explicitly define the "Naive" assumption in the Naive Bayes classification algorithm.
> **Answer**: The Naive assumption mathematically assumes that the probability of every individual word in a document is completely, statistically independent of the presence or absence of every other word in that document. It intentionally ignores grammar, word order, and context to completely eliminate the Data Sparsity problem when calculating likelihoods.

---

### Can You Explain This?
- [ ] I can write the core Bayes' Theorem equation used in classification.
- [ ] I can explicitly state why we ignore the Denominator $P(D)$ when picking a class.
- [ ] I can explain why real-world Naive Bayes must be implemented in Log Space.
- [ ] I can trace the Python dictionary lookups required to calculate a Laplace smoothed probability.

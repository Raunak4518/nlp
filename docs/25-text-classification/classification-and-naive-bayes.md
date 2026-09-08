# Text Classification and Naive Bayes

## 1. What is Text Classification?
Text Classification is the NLP task of assigning a predefined category (or label) to a given document.
- **Spam Filtering**: Assigning an email to `SPAM` or `NOT SPAM`.
- **Topic Modeling**: Assigning a news article to `SPORTS`, `POLITICS`, or `TECH`.
- **Sentiment Analysis**: Assigning a movie review to `POSITIVE` or `NEGATIVE`.

## 2. Feature Extraction
Algorithms cannot read text directly. Before classifying a document, we must convert it into a numerical vector (as covered in Module 12).
1. **Bag of Words (BoW) / Count Features**: We represent the document as a vector of word counts.
2. **TF-IDF Features**: We represent the document as a vector of TF-IDF scores, down-weighting overly common words.

## 3. Naive Bayes Classification
**Naive Bayes** is a classical statistical algorithm used for text classification. It is based directly on Bayes' Theorem (Module 13).

$$ P(C|D) = \frac{P(D|C) \times P(C)}{P(D)} $$
Where:
- $P(C|D)$: The probability that the document $D$ belongs to Class $C$.
- $P(D|C)$: The Likelihood of seeing the words in document $D$ given that it is in Class $C$.
- $P(C)$: The Prior probability of Class $C$ (e.g., are 80% of all emails spam?).
- $P(D)$: The Evidence (we drop this in classification because it is the same for all classes).

### Why is it "Naive"?
To calculate the Likelihood $P(D|C)$ for a document containing $N$ words, we use the Chain Rule: $P(w_1, w_2, ..., w_N | C)$. 
This would suffer from extreme Data Sparsity. The algorithm is called "Naive" because it makes the wildly incorrect assumption that **every word in the document is completely independent of every other word**.

Therefore, the likelihood simplifies to multiplying the individual unigram probabilities:
$$ P(D|C) \approx P(w_1|C) \times P(w_2|C) \times ... \times P(w_N|C) $$

## 4. Multinomial Naive Bayes & Laplace Smoothing
When classifying text, we specifically use the **Multinomial** variant of Naive Bayes, which calculates $P(w_i|C)$ using the frequency counts of words in the training documents for that class.

$$ P_{MLE}(w_i|C) = \frac{\text{Count of } w_i \text{ in all documents of Class } C}{\text{Total words in all documents of Class } C} $$

**The Zero-Probability Problem**: If the word "Rolex" never appeared in the `NOT SPAM` training emails, then $P(\text{"Rolex"} | \text{NOT SPAM}) = 0.0$. If a new, legitimate email contains the word "Rolex", the Naive Bayes chain multiplication will evaluate to exactly $0.0$, making it impossible to classify the email correctly.

**The Solution**: We MUST use Laplace Smoothing (+1) when calculating the likelihoods.
$$ P(w_i|C) = \frac{\text{Count}(w_i \text{ in } C) + 1}{\text{Total Words in } C + |V|} $$

## 5. Logistic Regression Concept
While Naive Bayes is a *Generative* model (it models the underlying probability distributions), **Logistic Regression** is a *Discriminative* model. It doesn't care about Bayes' Theorem. Instead, it learns a weight $w_i$ for every word in the vocabulary, multiplies the document's feature vector by those weights, and passes the sum through a Sigmoid function to output a probability between 0 and 1. 

Logistic Regression generally performs better than Naive Bayes on large datasets because it does not make the "naive" independence assumption, but it takes much longer to train.

## 6. Scratch Implementation (Naive Bayes)
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
        self.total_docs = len(documents)
        for doc, label in zip(documents, labels):
            self.class_doc_counts[label] += 1
            for word in doc.lower().split():
                self.vocab.add(word)
                self.class_word_counts[label][word] += 1
                self.class_total_words[label] += 1

    def predict(self, document: str) -> str:
        best_class = None
        highest_prob = float('-inf')

        # To prevent underflow, we use Log Probabilities (adding instead of multiplying)
        for label in self.class_doc_counts.keys():
            # 1. Log Prior P(C)
            prior = math.log(self.class_doc_counts[label] / self.total_docs)
            
            # 2. Log Likelihood P(D|C) with Laplace Smoothing
            likelihood = 0.0
            for word in document.lower().split():
                if word in self.vocab: # Ignore completely OOV words
                    count = self.class_word_counts[label][word]
                    total = self.class_total_words[label]
                    # Laplace +1 and +V
                    prob = (count + 1) / (total + len(self.vocab))
                    likelihood += math.log(prob)
            
            # 3. P(C|D) proportional to Prior + Likelihood
            total_prob = prior + likelihood
            
            if total_prob > highest_prob:
                highest_prob = total_prob
                best_class = label
                
        return best_class

# --- Trace ---
docs = [
    "win free money",        # SPAM
    "free viagra now",       # SPAM
    "meeting at noon",       # NOT SPAM
    "bring money for lunch"  # NOT SPAM
]
labels = ["SPAM", "SPAM", "NOT_SPAM", "NOT_SPAM"]

nb = NaiveBayesClassifier()
nb.train(docs, labels)
print(nb.predict("free money for noon meeting")) # Output: NOT_SPAM (or SPAM depending on counts, let's trace: 'free', 'money' are spammy. 'for', 'noon', 'meeting' are not spammy. It will calculate exact log probabilities to decide).
```

## 7. Exam Preparation
### Must Memorize
- Naive Bayes relies on the "naive" assumption of conditional independence between words.
- Laplace smoothing is mandatory to prevent zero-probability collapse.

### Likely Theory Question
**Question**: Why is it necessary to operate in Log Space when implementing Naive Bayes for text classification?
**Answer**: A document might contain 1,000 words. Naive Bayes calculates the likelihood by multiplying 1,000 small probabilities together (e.g., $0.01 \times 0.05 \times 0.002 ...$). This quickly results in a number so infinitesimally small that the computer's floating-point architecture rounds it to exactly $0.0$ (Underflow). Taking the logarithm allows us to *add* negative numbers instead of multiplying fractions, preserving mathematical precision.

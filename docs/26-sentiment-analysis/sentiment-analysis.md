# Sentiment Analysis

## 1. What is Sentiment Analysis?
Sentiment Analysis (formally known as Opinion Mining) is a highly lucrative, specific commercial application of Text Classification where the primary goal is to algorithmically determine the emotional tone or attitude physically expressed in a piece of text.
The most common formulation is binary mathematical classification: assigning a text block to the **POSITIVE** or **NEGATIVE** class.

---

## 2. Lexicon-Based Sentiment Classification
Before statistical machine learning algorithms (like Naive Bayes) became the industry standard, sentiment analysis was performed using **Lexicons**.

A **Sentiment Lexicon** is a massive, static, pre-compiled dictionary mapping specific words to hardcoded sentiment scores, manually created by linguists.
- "happy" $\rightarrow$ +1.0
- "terrible" $\rightarrow$ -1.5
- "okay" $\rightarrow$ +0.1

### The Algorithm
To algorithmically classify a sentence using a Lexicon:
1. Tokenize the sentence into unigrams.
2. Mathematically look up every single token in the lexicon dictionary.
3. Sum the scores together.
4. If the final sum is mathematically $>0$, predict `POSITIVE`. If $<0$, predict `NEGATIVE`.

### The Fatal Linguistic Limitation of Lexicons
Lexicons fail completely and catastrophically when dealing with linguistic context, sarcasm, and primarily **negation**.
- *"The movie was not terrible."*
  - The static lexicon dictionary sees the word "terrible" (score -1.5) and immediately outputs a `NEGATIVE` prediction. It has no structural mechanism to understand that "not" logically reverses the polarity of the next word.

---

## 3. Naive Bayes Sentiment Classifier
Sentiment analysis is perfectly structurally suited for the **Multinomial Naive Bayes algorithm** (covered in Module 25).

Unlike static lexicons, Naive Bayes learns dynamically from real-world data. During training, the algorithm mathematically calculates the statistical likelihood $P(w_i \mid C)$ for every word in the vocabulary for both the `POSITIVE` and `NEGATIVE` document classes.
- Words like "love", "amazing", and "recommend" will naturally have highly skewed probability mass toward the `POSITIVE` class.
- Words like "awful", "boring", and "waste" will have massively skewed probability mass toward the `NEGATIVE` class.

When structurally evaluating a brand new test sentence, Naive Bayes mathematically multiplies the prior probability $P(C)$ by the likelihood of every individual word in the sentence. Whichever class mathematically yields the highest final log-probability is the predicted sentiment.

### Solving Negation with Bigram Features
By upgrading the Naive Bayes feature extractor from Unigrams (Bag of Words) to **Bigrams**, Naive Bayes cleanly solves the lexicon negation problem. A Bigram model treats the sequence `"not terrible"` as a single mathematical token. During training, the bigram `"not terrible"` will logically appear almost exclusively in POSITIVE movie reviews, so the mathematical probability $P(\text{"not terrible"} \mid \text{POSITIVE})$ will be extremely high.

---

## 4. Sentiment Evaluation Metrics
Because real-world sentiment datasets are almost always highly imbalanced (e.g., on Amazon, 80% of all product reviews are 5-star positive reviews), **Accuracy** is a mathematically terrible, dangerous metric for evaluating sentiment classifiers.

If an Amazon dataset is exactly 80% positive, a mathematically broken classifier that blindly hardcodes its output to `POSITIVE` for every single review will achieve an 80% Accuracy score, completely masking the devastating fact that it failed to identify a single negative review.

> [!WARNING]
> Always evaluate highly imbalanced sentiment models strictly using **Precision, Recall, and the Macro-F1 Score**.

---

## 5. Scratch Implementation (Lexicon Classifier)

Here is a simple Python implementation of a Lexicon classifier. Notice how the logic completely fails on negation.

```python
class LexiconSentimentClassifier:
    def __init__(self, lexicon: dict[str, float]):
        self.lexicon = lexicon
        
    def predict(self, text: str) -> str:
        score = 0.0
        for word in text.lower().split():
            # If word is in lexicon, mathematically add its score. Else add 0.0
            score += self.lexicon.get(word, 0.0)
            
        if score > 0:
            return "POSITIVE"
        elif score < 0:
            return "NEGATIVE"
        else:
            return "NEUTRAL"

# --- Code Trace ---
my_lexicon = {
    "good": 1.0,
    "great": 2.0,
    "bad": -1.0,
    "terrible": -2.0,
    "not": -0.5 # Negation is mathematically impossible for simple lexicons to handle well
}

classifier = LexiconSentimentClassifier(my_lexicon)

print(classifier.predict("the movie was great and good")) 
# Score: 2.0 + 1.0 = 3.0 -> POSITIVE

print(classifier.predict("the actor was bad but the movie was great"))
# Score: -1.0 + 2.0 = 1.0 -> POSITIVE

print(classifier.predict("the movie was not good"))
# Score: -0.5 + 1.0 = 0.5 -> POSITIVE (This is a classic, catastrophic Lexicon failure!)
```

---

## 6. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: Provide a specific example of an English sentence where a standard unigram Lexicon-based sentiment classifier will definitively fail, but a Bigram Naive Bayes classifier will succeed. Mathematically explain the structural reason why the Naive Bayes classifier succeeds.
> **Answer**: The sentence "The battery life is not good." 
> A standard unigram lexicon classifier will mathematically sum the hardcoded scores of "not" (slightly negative) and "good" (highly positive) and will incorrectly output a POSITIVE prediction, because it structurally ignores syntactic word order.
> 
> A Bigram Naive Bayes classifier succeeds because it extracts the two-word sequence "not good" as a single, unified mathematical token. During training on labeled data, the token "not good" will appear almost exclusively in negative documents, meaning the likelihood probability $P(\text{"not good"} \mid \text{NEGATIVE})$ will be calculated as extremely high. When multiplying the probabilities for the test sentence, the high negative likelihood will easily outweigh the other words, allowing the model to correctly classify the sentence as negative.

**2-Mark Question**: Why is Accuracy a misleading metric for evaluating a sentiment classifier trained on Yelp reviews?
> **Answer**: Yelp reviews are naturally heavily imbalanced toward positive ratings (e.g., 85% positive). If a model is evaluated using Accuracy, it could simply predict "Positive" for every single review and achieve an artificially high 85% score, despite having zero predictive power for identifying negative reviews. F1-score must be used instead.

---

### Can You Explain This?
- [ ] I can explicitly define what a Lexicon is.
- [ ] I can trace the Python loop that calculates a Lexicon score.
- [ ] I can explain why Bigram Naive Bayes is structurally superior to Unigram Lexicons for sentiment analysis.

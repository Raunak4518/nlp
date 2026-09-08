# Sentiment Analysis

## 1. What is Sentiment Analysis?
Sentiment Analysis (also known as Opinion Mining) is a specific type of Text Classification where the goal is to determine the emotional tone or attitude expressed in a piece of text.
The most common formulation is binary classification: assigning a text as **POSITIVE** or **NEGATIVE**.

## 2. Lexicon-Based Sentiment Classification
Before machine learning algorithms like Naive Bayes became standard, sentiment analysis was performed using **Lexicons**.

A **Sentiment Lexicon** is a pre-compiled dictionary of words mapping to sentiment scores.
- "happy" $\rightarrow$ +1.0
- "terrible" $\rightarrow$ -1.5
- "okay" $\rightarrow$ +0.1

### The Algorithm
To classify a sentence using a lexicon:
1. Tokenize the sentence.
2. Look up every token in the lexicon.
3. Sum the scores.
4. If the sum is $>0$, predict `POSITIVE`. If $<0$, predict `NEGATIVE`.

### Limitations of Lexicons
Lexicons fail completely when dealing with context, sarcasm, and negation.
- "The movie was not terrible."
  - The lexicon sees "terrible" (-1.5) and outputs `NEGATIVE`. A machine learning classifier trained on Bigrams ("not terrible") would easily learn to classify this as `POSITIVE`.

## 3. Naive Bayes Sentiment Classifier
Sentiment analysis is perfectly suited for the Multinomial Naive Bayes algorithm (covered in Module 25).

During training, the algorithm calculates the likelihood $P(w_i | C)$ for every word in the vocabulary for both the `POSITIVE` and `NEGATIVE` classes.
- Words like "love", "amazing", and "recommend" will have highly skewed probabilities toward the `POSITIVE` class.
- Words like "awful", "boring", and "waste" will have skewed probabilities toward the `NEGATIVE` class.

When evaluating a new sentence, Naive Bayes multiplies the prior probability $P(C)$ by the likelihood of every word in the sentence. Whichever class yields the highest log-probability is the predicted sentiment.

## 4. Sentiment Evaluation
Because sentiment datasets are often highly imbalanced (e.g., on Amazon, 80% of reviews are 5-star positive reviews), **Accuracy** is a very poor metric for evaluating sentiment classifiers.

If a dataset is 80% positive, a broken classifier that blindly guesses `POSITIVE` for every single review will achieve an 80% Accuracy score, completely masking the fact that it failed to identify a single negative review.

Always evaluate sentiment models using **Precision, Recall, and the Macro-F1 Score**.

## 5. Scratch Implementation (Lexicon Classifier)
```python
class LexiconSentimentClassifier:
    def __init__(self, lexicon: dict[str, float]):
        self.lexicon = lexicon
        
    def predict(self, text: str) -> str:
        score = 0.0
        for word in text.lower().split():
            # If word is in lexicon, add its score. Else add 0.0
            score += self.lexicon.get(word, 0.0)
            
        if score > 0:
            return "POSITIVE"
        elif score < 0:
            return "NEGATIVE"
        else:
            return "NEUTRAL"

# --- Trace ---
my_lexicon = {
    "good": 1.0,
    "great": 2.0,
    "bad": -1.0,
    "terrible": -2.0,
    "not": -0.5 # Negation is hard for lexicons!
}

classifier = LexiconSentimentClassifier(my_lexicon)

print(classifier.predict("the movie was great and good")) 
# Score: 2.0 + 1.0 = 3.0 -> POSITIVE

print(classifier.predict("the actor was bad but the movie was great"))
# Score: -1.0 + 2.0 = 1.0 -> POSITIVE

print(classifier.predict("the movie was not good"))
# Score: -0.5 + 1.0 = 0.5 -> POSITIVE (This is a classic Lexicon failure!)
```

## 6. Exam Preparation
### Must Know
- Lexicon-based sentiment relies on static dictionaries and struggles with negation and sarcasm.
- Naive Bayes handles sentiment natively by learning word distributions directly from labeled training data.

### Likely Theory Question
**Question**: Give an example of a sentence that a Lexicon-based sentiment classifier would fail on, and explain why a Bigram Naive Bayes classifier would succeed on the same sentence.
**Answer**: "The battery life is not good." A lexicon classifier will sum the scores of "not" (slightly negative) and "good" (highly positive) and likely output a POSITIVE prediction, ignoring the syntactic negation. A Bigram Naive Bayes classifier treats "not good" as a single token. During training, the bigram "not good" will appear almost exclusively in NEGATIVE documents, so $P(\text{"not good"} | \text{NEGATIVE})$ will be extremely high, allowing the model to correctly classify the sentence.

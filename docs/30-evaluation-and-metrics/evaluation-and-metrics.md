# Evaluation & Metrics

## 1. Summary of NLP Evaluation Metrics
Throughout this course, we have introduced various metrics tailored to specific NLP tasks. This module serves as a comprehensive review and introduces BLEU and ROUGE for generation tasks.

## 2. Language Model Evaluation (Perplexity)
**Metric**: Perplexity ($PP$)
**Task**: Language Modeling, Next-Word Prediction.
**Definition**: $PP(W) = P(w_1, ..., w_N)^{-\frac{1}{N}}$. The weighted average branching factor.
**Rule**: Lower is better.

## 3. Classification Evaluation (Precision, Recall, F1)
**Metric**: Precision, Recall, Macro/Micro-F1, Accuracy.
**Task**: Text Classification, Sentiment Analysis, Spam Filtering.
**Definitions**:
- *Precision*: $TP / (TP + FP)$. (How many predicted positives were actually positive?)
- *Recall*: $TP / (TP + FN)$. (How many actual positives did we successfully find?)
- *F1 Score*: Harmonic mean of Precision and Recall.
**Rule**: Higher is better. Accuracy should ONLY be used if the dataset is perfectly balanced.

## 4. Sequence Labeling Evaluation (NER & POS)
**Task**: Part-of-Speech Tagging, Named Entity Recognition.

### Token-Level Accuracy
For simple tasks like POS tagging, we often just use Token-Level Accuracy: what percentage of words in the sentence were assigned the correct tag?

### Entity-Level Precision/Recall/F1
For NER, Token-Level Accuracy is highly misleading because $95\%$ of tokens are usually the `O` (Outside) tag. A broken model that just guesses `O` for everything will get $95\%$ accuracy.

Instead, we use **Entity-Level** evaluation. A prediction is only a True Positive (TP) if the model correctly identified the *exact start boundary*, the *exact end boundary*, AND the *correct entity type*.
- If the text is "President [George Washington] visited...", and the model predicts "President George [Washington] visited...", that is a False Positive for the predicted entity, and a False Negative for the true entity. It gets zero partial credit.
- We then calculate Precision, Recall, and F1 on these strict Entity-Level counts.

## 5. Machine Translation Evaluation (BLEU)
**Metric**: BLEU (Bilingual Evaluation Understudy)
**Task**: Machine Translation.
**Definition**: How do you grade a translation? There are many valid ways to translate a sentence. BLEU compares the machine's translation against one or more human reference translations.
- It calculates the **N-gram precision**: how many unigrams, bigrams, and trigrams in the machine's output appeared anywhere in the human references?
- It includes a **Brevity Penalty**: to prevent the machine from just outputting one highly-confident word (e.g., "The") and claiming 100% precision, BLEU heavily penalizes outputs that are shorter than the reference.
**Rule**: Higher is better (usually on a scale of 0 to 100).

## 6. Summarization Evaluation (ROUGE)
**Metric**: ROUGE (Recall-Oriented Understudy for Gisting Evaluation)
**Task**: Summarization (Extractive and Abstractive).
**Definition**: ROUGE is the inverse of BLEU. While BLEU focuses on Precision (did the machine's words appear in the human text?), ROUGE focuses on **Recall** (did the machine successfully capture all the important N-grams from the human's reference summary?).
- *ROUGE-N*: Measures N-gram recall.
- *ROUGE-L*: Measures the Longest Common Subsequence between the machine summary and the human summary.
**Rule**: Higher is better.

## 7. Exam Preparation
### Must Memorize
- **Perplexity**: Language Modeling. Lower is better.
- **F1 Score**: Classification and NER. Higher is better.
- **BLEU**: Machine Translation. Focuses on N-gram *Precision* + Brevity Penalty.
- **ROUGE**: Summarization. Focuses on N-gram *Recall*.

### Likely Theory Question
**Question**: Why is Token-Level Accuracy an inappropriate metric for evaluating Named Entity Recognition (NER)?
**Answer**: NER datasets are heavily imbalanced. In BIO tagging, the vast majority of tokens in a standard text will be tagged as `O` (Outside any entity). A baseline model that blindly predicts `O` for every single token might achieve 90% or 95% Token-Level Accuracy while failing to extract a single named entity. NER must be evaluated using Entity-Level Precision, Recall, and F1 to ensure the model is actually detecting the rare, valuable entity boundaries.

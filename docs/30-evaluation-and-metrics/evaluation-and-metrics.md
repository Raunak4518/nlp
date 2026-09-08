# Evaluation & Metrics

## 1. Summary of NLP Evaluation Metrics
Throughout this course, we have introduced various distinct mathematical metrics tailored to entirely different NLP tasks. This module serves as a comprehensive, centralized review and formally introduces BLEU and ROUGE for evaluating generation tasks.

Using the wrong mathematical metric for a task will cause you to deploy a fundamentally broken, useless model to production.

---

## 2. Language Model Evaluation
- **Metric**: Perplexity ($PP$)
- **Task**: Language Modeling, Next-Word Prediction.
- **Definition**: $PP(W) = P(w_1, \dots, w_N)^{-\frac{1}{N}}$. It represents the weighted average branching factor of the model's predictive distribution.
- **Rule**: **Lower is better**.

---

## 3. Classification Evaluation
- **Metric**: Precision, Recall, Macro/Micro-F1, Accuracy.
- **Task**: Text Classification, Sentiment Analysis, Spam Filtering.
- **Definitions**:
  - *Precision*: $TP / (TP + FP)$. (How many mathematically predicted positives were actually positive?)
  - *Recall*: $TP / (TP + FN)$. (How many actual real-world positives did we successfully capture?)
  - *F1 Score*: The Harmonic mean of Precision and Recall.
- **Rule**: **Higher is better**. 
  *(WARNING: Accuracy should ONLY be used if the dataset is perfectly, mathematically balanced. Otherwise, it is extremely dangerous and misleading).*

---

## 4. Sequence Labeling Evaluation (NER & POS)
- **Task**: Part-of-Speech (POS) Tagging, Named Entity Recognition (NER).

### Token-Level Accuracy (Fails for NER)
For simple, balanced tasks like POS tagging (where every word gets exactly one tag), we often just use basic Token-Level Accuracy: what percentage of words in the sentence were assigned the correct POS tag?

### Entity-Level Precision/Recall/F1 (Required for NER)
For NER, Token-Level Accuracy is highly misleading because up to $95\%$ of tokens are usually the `O` (Outside) tag. A completely broken model that just blindly guesses `O` for every single token will artificially get $95\%$ accuracy.

Instead, we mathematically enforce **Entity-Level** evaluation. A prediction is only granted a True Positive (TP) if the model correctly identified the *exact start boundary*, the *exact end boundary*, AND the *correct entity type* simultaneously.
- If the ground truth text is "President `[George Washington]` visited...", and the model predicts "President George `[Washington]` visited...", that is mathematically scored as a False Positive for the predicted entity, and a False Negative for the true entity. It gets absolutely zero partial credit.
- We then systematically calculate Precision, Recall, and F1 exclusively on these strict Entity-Level counts.

---

## 5. Machine Translation Evaluation (BLEU)
- **Metric**: **BLEU** (Bilingual Evaluation Understudy)
- **Task**: Machine Translation.
- **Definition**: How do you algorithmically grade a translation without a human? There are many perfectly valid ways to translate a sentence. BLEU mathematically compares the machine's translation against one or more human-written reference translations.
  - It calculates the **N-gram precision**: how many unigrams, bigrams, and trigrams in the machine's generated output appeared *anywhere* in the human references?
  - It physically enforces a **Brevity Penalty**: to prevent the machine from just outputting one highly-confident, safe word (e.g., "The") and falsely claiming 100% precision, BLEU heavily penalizes outputs that are mathematically shorter than the reference translation.
- **Rule**: **Higher is better** (usually reported on a scale of 0 to 100).

---

## 6. Summarization Evaluation (ROUGE)
- **Metric**: **ROUGE** (Recall-Oriented Understudy for Gisting Evaluation)
- **Task**: Summarization (Extractive and Abstractive).
- **Definition**: ROUGE is effectively the mathematical inverse of BLEU. While BLEU focuses heavily on Precision (did the machine's words appear in the human text?), ROUGE focuses heavily on **Recall** (did the machine successfully mathematically capture and include all the important N-grams from the human's reference summary?).
  - *ROUGE-N*: Measures strict N-gram recall.
  - *ROUGE-L*: Measures the Longest Common Subsequence mathematically shared between the machine summary and the human summary, ignoring rigid word order.
- **Rule**: **Higher is better**.

---

## 7. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: You are an AI Engineer. Your junior developer evaluated your new Named Entity Recognition (NER) model and proudly reported it achieved 93% Token-Level Accuracy. Explain to them why this metric is completely invalid for NER, and explain the exact criteria required to score a True Positive under the correct evaluation framework.
> **Answer**: Token-Level Accuracy is completely invalid for NER because NER datasets are massively imbalanced. In the standard BIO tagging format, the vast majority of tokens (often over 90%) will simply be tagged as `O` (Outside any entity). A baseline model that blindly predicts `O` for every single token will achieve over 90% accuracy while failing to extract a single named entity. 
> 
> NER must exclusively be evaluated using **Entity-Level F1**. To score a True Positive under Entity-Level evaluation, the model must simultaneously predict three exact criteria: 1) the exact start boundary of the entity, 2) the exact end boundary of the entity, and 3) the correct entity label (e.g., ORG or PER). Any partial overlap is strictly scored as a False Positive and a False Negative.

**3-Mark Question**: Compare the mathematical priorities of the BLEU score versus the ROUGE score, and list the NLP task each was specifically designed to evaluate.
> **Answer**: 
> - **BLEU** was specifically designed to evaluate **Machine Translation**. It heavily prioritizes N-gram **Precision** (ensuring the words the machine generated are highly accurate and fluent based on the reference) and enforces a Brevity Penalty to prevent overly short outputs.
> - **ROUGE** was specifically designed to evaluate **Summarization**. It heavily prioritizes N-gram **Recall** (ensuring the machine successfully captured and included all the critical concepts present in the human reference summary).

---

### Can You Explain This?
- [ ] I can explicitly state why Token-Level Accuracy completely fails for evaluating NER systems.
- [ ] I can explicitly state the 3 conditions required for an Entity-Level True Positive.
- [ ] I can explain the structural difference between how BLEU evaluates text (Precision) and how ROUGE evaluates text (Recall).
- [ ] I can perfectly map the 5 major NLP tasks (LM, Classification, NER, MT, Summarization) to their primary evaluation metrics from memory.

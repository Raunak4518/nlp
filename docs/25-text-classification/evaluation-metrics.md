# Evaluation Metrics: Precision, Recall, and F1

## 1. The Problem with Accuracy
**Accuracy** is the simplest evaluation metric:
$$ \text{Accuracy} = \frac{\text{Correct Predictions}}{\text{Total Predictions}} $$

However, Accuracy is completely misleading when the dataset is **imbalanced**.
If $99\%$ of your emails are `NOT SPAM`, and $1\%$ are `SPAM`, a broken model that just outputs `NOT SPAM` every single time will achieve a $99\%$ Accuracy score! But the model is useless because it missed $100\%$ of the actual spam.

To properly evaluate classifiers, we use a Confusion Matrix.

## 2. The Confusion Matrix
A confusion matrix categorizes predictions into four buckets. Let's assume we are detecting SPAM (the Positive class).

| | Actual SPAM (Positive) | Actual NOT SPAM (Negative) |
|---|---|---|
| **Predicted SPAM** | True Positive (TP) | False Positive (FP) |
| **Predicted NOT SPAM** | False Negative (FN) | True Negative (TN) |

- **True Positive (TP)**: It is spam, and we correctly caught it.
- **True Negative (TN)**: It is a normal email, and we correctly let it through.
- **False Positive (FP)**: It is a normal email, but we incorrectly sent it to the Spam folder (Very annoying for the user!).
- **False Negative (FN)**: It is spam, but we incorrectly let it into the inbox.

## 3. Precision and Recall
To solve the Accuracy problem, we calculate two separate metrics:

### Precision
"Out of all the emails the model *claimed* were spam, how many were *actually* spam?"
$$ \text{Precision} = \frac{TP}{TP + FP} $$
- High precision means you have very few False Positives. (You rarely put normal emails in the spam folder).

### Recall
"Out of all the *actual* spam in the universe, how many did the model successfully *find*?"
$$ \text{Recall} = \frac{TP}{TP + FN} $$
- High recall means you have very few False Negatives. (You rarely let spam into the inbox).

*Note: There is always a trade-off. If you flag everything as spam, your Recall is 100%, but your Precision drops to near 0%.*

## 4. The F1 Score
Because evaluating two metrics is difficult, we combine them into a single number called the **F1 Score**. It is the harmonic mean of Precision and Recall.

$$ F1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} $$

The harmonic mean heavily penalizes extreme values. If Precision is $1.0$ and Recall is $0.01$, the arithmetic average is $0.5$, but the F1 score will be very close to $0.0$, correctly identifying that the model is broken.

## 5. Multi-Class Evaluation (Macro vs Micro)
If you have 3 classes (e.g., `SPORTS`, `TECH`, `POLITICS`), you calculate the F1 score for each class separately. How do you combine them into one final score?

- **Macro-F1**: Calculate the F1 for each class, and take the unweighted average. 
  *(Use this if you care about performance on rare classes equally).*
- **Micro-F1**: Sum up all the TPs, FPs, and FNs across all classes first, then calculate one massive F1 score. 
  *(Use this if you care about overall performance and want to weight the score by class frequency).*

## 6. Exam Preparation
### Must Memorize
- Precision = $TP / (TP + FP)$. (Denominator is all *predictions*).
- Recall = $TP / (TP + FN)$. (Denominator is all *actual truth*).
- F1 Score = $2PR / (P+R)$.

### Likely Practical Question
**Question**: An NLP system classifies 100 emails. It predicts 20 are Spam. Out of those 20, 15 are actually Spam, and 5 are normal emails. In reality, there were 30 total Spam emails in the dataset. Calculate Precision, Recall, and F1.
**Answer**:
1. $TP = 15$ (Predicted Spam, Actually Spam).
2. $FP = 5$ (Predicted Spam, Actually Normal).
3. $FN = 15$ (Predicted Normal, Actually Spam. 30 total - 15 found = 15 missed).
4. $\text{Precision} = 15 / (15 + 5) = 15 / 20 = 0.75$.
5. $\text{Recall} = 15 / (15 + 15) = 15 / 30 = 0.50$.
6. $\text{F1} = 2 \times (0.75 \times 0.50) / (0.75 + 0.50) = 2 \times (0.375) / 1.25 = 0.75 / 1.25 = 0.60$.

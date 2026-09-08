# Evaluation Metrics: Precision, Recall, and F1

## 1. The Catastrophic Problem with Accuracy
**Accuracy** is the simplest and most intuitive evaluation metric:
$$ \text{Accuracy} = \frac{\text{Correct Predictions}}{\text{Total Predictions}} $$

However, in the real world, Accuracy is a completely misleading and dangerous metric whenever the dataset is **highly imbalanced** (which is almost always).

If $99\%$ of incoming emails are `NOT SPAM`, and $1\%$ are `SPAM`, a mathematically broken model that simply hardcodes its output to `NOT SPAM` every single time will achieve a massive $99\%$ Accuracy score! The metric makes the model look like a masterpiece, but the model is utterly useless because it missed $100\%$ of the actual spam.

To properly and safely evaluate classifiers, data scientists completely ignore Accuracy and use a Confusion Matrix instead.

---

## 2. The Confusion Matrix
A confusion matrix is a grid that strictly categorizes all predictions into four buckets. Let's assume we are actively trying to detect SPAM (meaning SPAM is the "Positive" class).

| | Actual SPAM (Positive) | Actual NOT SPAM (Negative) |
|---|---|---|
| **Predicted SPAM** | True Positive (TP) | False Positive (FP) |
| **Predicted NOT SPAM** | False Negative (FN) | True Negative (TN) |

- **True Positive (TP)**: It is real spam, and our model correctly caught it.
- **True Negative (TN)**: It is a normal work email, and our model correctly let it through to the inbox.
- **False Positive (FP)**: It is a normal work email, but our model incorrectly sent it to the Spam folder (Extremely annoying for the user! Could cause them to miss a job offer).
- **False Negative (FN)**: It is real spam, but our model incorrectly let it into the inbox (Annoying, but usually harmless).

---

## 3. Precision and Recall
To permanently solve the Accuracy problem, we calculate two distinct, competing metrics:

### Precision (The "Quality" Metric)
*"Out of all the emails the model formally **claimed** were spam, how many were **actually** spam?"*
$$ \text{Precision} = \frac{TP}{TP + FP} $$
- High precision mathematically means you have very few False Positives. (You rarely put normal work emails in the spam folder).

### Recall (The "Capture Rate" Metric)
*"Out of all the **actual** spam in the universe, how many did the model successfully **find**?"*
$$ \text{Recall} = \frac{TP}{TP + FN} $$
- High recall mathematically means you have very few False Negatives. (You rarely let spam slip through into the inbox).

> [!WARNING]
> **The Precision/Recall Trade-off**: There is mathematically almost always a trade-off between the two. If you configure your algorithm to flag *every single email* as spam, your Recall will be a perfect 100% (you caught all the spam!), but your Precision will drop to near 0% (because you flagged thousands of normal emails too).

---

## 4. The F1-Score
Because evaluating two competing metrics simultaneously is difficult when comparing models, we mathematically combine them into a single, unified number called the **F1-Score**. 

The F1-Score is specifically the **Harmonic Mean** of Precision and Recall.

$$ F1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} $$

**Why use the Harmonic Mean instead of a normal average?**
The harmonic mean heavily penalizes extreme, unbalanced values. If a broken model has a Precision of $1.0$ and a Recall of $0.01$, the standard arithmetic average is roughly $0.5$. However, the harmonic F1 score will be very close to $0.0$, correctly mathematically identifying that the model is broken and useless.

---

## 5. Multi-Class Evaluation (Macro vs Micro)
If you have 3 or more classes (e.g., classifying news as `SPORTS`, `TECH`, `POLITICS`), you calculate the F1 score for each class entirely separately. But how do you combine them into one final, global score for the model?

- **Macro-F1**: Calculate the F1 for each class independently, and take the raw, unweighted arithmetic average of those scores. 
  *(Use this if you care about performance on rare minority classes equally as much as majority classes).*
- **Micro-F1**: Sum up all the global TPs, FPs, and FNs across every single class *first*, then mathematically calculate one massive, global F1 score. 
  *(Use this if you primarily care about overall global performance and want the final score to be weighted by class frequency).*

---

## 6. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: A new NLP system classifies 100 emails. It predicts that exactly 20 emails are Spam. Out of those 20 predicted emails, 15 are actually Spam, and 5 are normal emails. In reality, there were exactly 30 total Spam emails in the dataset. Calculate Precision, Recall, and the F1-Score.
> **Answer**:
> 1. Determine the Confusion Matrix values:
>    - $TP = \mathbf{15}$ (Predicted Spam, Actually Spam).
>    - $FP = \mathbf{5}$ (Predicted Spam, Actually Normal).
>    - $FN = \mathbf{15}$ (Predicted Normal, Actually Spam. Calculation: 30 total in reality - 15 found = 15 missed).
> 2. Calculate Precision: 
>    $\text{Precision} = \frac{TP}{TP + FP} = \frac{15}{15 + 5} = \frac{15}{20} = \mathbf{0.75}$.
> 3. Calculate Recall: 
>    $\text{Recall} = \frac{TP}{TP + FN} = \frac{15}{15 + 15} = \frac{15}{30} = \mathbf{0.50}$.
> 4. Calculate F1-Score: 
>    $F1 = 2 \times \frac{0.75 \times 0.50}{0.75 + 0.50} = 2 \times \frac{0.375}{1.25} = \frac{0.75}{1.25} = \mathbf{0.60}$.

**2-Mark Question**: Explain mathematically why F1 is calculated using the Harmonic Mean rather than the Arithmetic Mean.
> **Answer**: The arithmetic mean can artificially inflate the score of a poorly tuned model. For example, a model that classifies everything as Positive will have a Recall of 1.0 and a Precision near 0.0, yielding a respectable arithmetic mean of 0.5. The Harmonic Mean severely penalizes models where one metric is extremely low, pulling the F1 score down to near 0.0, correctly reflecting that the model's predictive power is broken.

---

### Can You Explain This?
- [ ] I can explicitly define True Positives and False Positives.
- [ ] I can write the formulas for Precision and Recall.
- [ ] I can write the formula for the F1-Score.
- [ ] I can explain the structural difference between Macro-F1 and Micro-F1.

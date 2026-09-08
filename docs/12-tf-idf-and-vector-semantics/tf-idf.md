# Term Frequency-Inverse Document Frequency (TF-IDF)

## 1. Fixing the Frequency Bias
Count vectors weight words based purely on how often they physically appear in a document. This means grammatical function words like "the" will always dominate the vector, masking the true semantic meaning of the text. 

**TF-IDF** solves this by balancing two opposing metrics: 
1. **TF**: How frequent the word is in the *current document* (a measure of local importance).
2. **IDF**: How rare the word is across the *entire corpus* (a measure of global uniqueness).

---

## 2. Term Frequency (TF)
$TF(t, d)$ measures how frequently a term $t$ occurs in a specific document $d$. In its most basic form:

$$ TF(t, d) = \text{count of } t \text{ in } d $$

*(Note: Advanced implementations often use $\log_{10}(\text{count} + 1)$ to dampen the mathematical effect of extreme repetition, or they normalize the count by dividing by the total number of words in the document).*

## 3. Document Frequency (DF)
$DF(t)$ is simply the number of documents in the entire training corpus that contain the term $t$ at least once.
- If we have a dataset of 1,000 Wikipedia articles, and the word "the" appears in all 1,000 of them, $DF(\text{"the"}) = 1000$.

---

## 4. Inverse Document Frequency (IDF)
$IDF$ mathematically penalizes words that are too common across the dataset. It is calculated as the base-10 logarithm of the total number of documents $N$ divided by $DF(t)$.

$$ IDF(t) = \log_{10}\left(\frac{N}{DF(t)}\right) $$

Let's calculate IDF for a corpus where $N = 1000$:

| Term | DF (Documents containing term) | IDF Calculation | IDF Score |
| :--- | :--- | :--- | :--- |
| **the** | 1000 | $\log_{10}(1000/1000) = \log_{10}(1)$ | **0** |
| **NLP** | 10 | $\log_{10}(1000/10) = \log_{10}(100)$ | **2** |
| **zygote** | 1 | $\log_{10}(1000/1) = \log_{10}(1000)$ | **3** |

> [!TIP]
> Notice how the IDF of the word "the" becomes exactly zero. This is the magic of TF-IDF: it mathematically neutralizes stop-words without requiring a hard-coded dictionary of words to ignore.

---

## 5. The Final TF-IDF Calculation
The final weight for term $t$ in document $d$ is simply the product of its TF and IDF.

$$ \text{TF-IDF}(t, d) = TF(t, d) \times IDF(t) $$

### Example Numerical Calculation
Assume our dataset has $N = 100$ total documents.
We are processing Document $d$: *"the cat saw a cat"*
We want the TF-IDF weight for the word **"cat"**.
- "cat" appears 2 times in $d$. So, **$TF = 2$**.
- "cat" appears in 10 documents total across the corpus. So, **$DF = 10$**.
- $IDF = \log_{10}(100 / 10) = \log_{10}(10) = 1$.
- **$\text{TF-IDF}(\text{cat}, d) = 2 \times 1 = 2$**.

Now we calculate the TF-IDF weight for the word **"the"**.
- "the" appears 1 time in $d$. **$TF = 1$**.
- "the" appears in all 100 documents. **$DF = 100$**.
- $IDF = \log_{10}(100 / 100) = \log_{10}(1) = 0$.
- **$\text{TF-IDF}(\text{the}, d) = 1 \times 0 = 0$**.

---

## 6. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: You are given a corpus of 10,000 documents. The word "Python" appears in 100 of these documents. In Document $X$, the word "Python" appears 5 times. Calculate the TF-IDF score for "Python" in Document $X$. Show all formulas and work (Assume base-10 log).
> **Answer**: 
> 1. $TF(t, d) = \text{count of } t \text{ in } d$
>    $TF(\text{"Python"}, X) = 5$
> 2. $IDF(t) = \log_{10}(\frac{N}{DF(t)})$
>    $N = 10,000$
>    $DF(\text{"Python"}) = 100$
>    $IDF = \log_{10}(\frac{10,000}{100}) = \log_{10}(100) = 2$
> 3. $\text{TF-IDF} = TF \times IDF$
>    $\text{TF-IDF} = 5 \times 2 = 10$
> 
> The final score is 10.

**3-Mark Question**: Why do we use the logarithm in the IDF formula? What would happen if we omitted it?
> **Answer**: Without the logarithm, the IDF score for extremely rare words would explode to unmanageable numbers (e.g., $1,000,000 / 1 = 1,000,000$). This would cause rare words to completely dominate the vector space, overpowering the rest of the text. The logarithm strictly dampens this effect, allowing rare words to be weighted higher than common words without destroying the mathematical stability of the model.

---

### Can You Explain This?
- [ ] I can write the formulas for TF, IDF, and TF-IDF from memory.
- [ ] I can define what the variable $N$ stands for.
- [ ] I understand how TF-IDF automatically acts as a stop-word filter.

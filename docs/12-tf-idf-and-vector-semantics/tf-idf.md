# Term Frequency-Inverse Document Frequency (TF-IDF)

## 1. Fixing the Frequency Bias
Count vectors weight words based purely on how often they appear in a document. This means "the" will always dominate the vector. **TF-IDF** solves this by balancing two metrics: how frequent the word is in the *document*, versus how rare the word is across the *entire corpus*.

## 2. Term Frequency (TF)
$TF(t, d)$ measures how frequently a term $t$ occurs in a document $d$.
$$ TF(t, d) = \text{count of } t \text{ in } d $$

*(Note: Some variants use $\log_{10}(count + 1)$ to dampen the effect of extreme repetition, or normalize it by the total words in the document).*

## 3. Document Frequency (DF)
$DF(t)$ is the number of documents in the entire corpus that contain the term $t$.
If we have 1,000 documents, and the word "the" appears in all of them, $DF(\text{"the"}) = 1000$.

## 4. Inverse Document Frequency (IDF)
$IDF$ penalizes words that are too common. It is calculated as the logarithm of the total number of documents $N$ divided by $DF(t)$.

$$ IDF(t) = \log_{10}\left(\frac{N}{DF(t)}\right) $$

Let $N = 1000$:
- "the" is in 1000 docs. $IDF = \log_{10}(1000/1000) = \log_{10}(1) = 0$.
- "NLP" is in 10 docs. $IDF = \log_{10}(1000/10) = \log_{10}(100) = 2$.
- "zygote" is in 1 doc. $IDF = \log_{10}(1000/1) = \log_{10}(1000) = 3$.

*Notice how the IDF of "the" becomes exactly zero, completely neutralizing it.*

## 5. The TF-IDF Calculation
The final weight for term $t$ in document $d$ is simply the product of its TF and IDF.

$$ \text{TF-IDF}(t, d) = TF(t, d) \times IDF(t) $$

### Example Numerical Calculation
Assume $N = 100$ total documents.
Document $d$ is: "the cat saw a cat"
We want the TF-IDF for "cat".
- "cat" appears 2 times in $d$. So, $TF = 2$.
- "cat" appears in 10 documents total across the corpus. So, $DF = 10$.
- $IDF = \log_{10}(100 / 10) = \log_{10}(10) = 1$.
- $\text{TF-IDF}(\text{cat}, d) = 2 \times 1 = 2$.

Now we calculate TF-IDF for "the".
- "the" appears 1 time in $d$. $TF = 1$.
- "the" appears in all 100 documents. $DF = 100$.
- $IDF = \log_{10}(100 / 100) = \log_{10}(1) = 0$.
- $\text{TF-IDF}(\text{the}, d) = 1 \times 0 = 0$.

## 6. Exam Preparation
### Must Memorize
- The formulas for TF, IDF, and TF-IDF. (Assume base 10 for logs unless specified otherwise by your professor).
- What $N$ stands for (Total number of documents in the training corpus).

### Likely Theory Question
**Question**: Why do we use the logarithm in the IDF formula?
**Answer**: Without the logarithm, the IDF score for rare words would explode to massive numbers (e.g., $1,000,000 / 1 = 1,000,000$), completely dominating the vector. The logarithm dampens this effect, allowing rare words to be weighted higher than common words without overpowering the entire model.

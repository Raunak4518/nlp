# The Zero-Probability Problem

## 1. Unseen N-grams and Zero Probability
As established in the previous section, the vast majority of possible N-grams will never appear in our training data. Therefore, their Maximum Likelihood Estimate (MLE) count is 0.

If the count is 0, the estimated probability is exactly $0.0$.

$$ P_{MLE}(\text{"elephant"} | \text{"the purple"}) = \frac{0}{\text{Count("the purple")}} = 0.0 $$

## 2. Destroying Sentence Probability
Remember that Language Models calculate the probability of a full sentence using the Chain Rule (multiplying the probabilities of the constituent n-grams).

$$ P(w_1, w_2, w_3, w_4) = P(w_1) \times P(w_2|w_1) \times P(w_3|w_2) \times P(w_4|w_3) $$

If even a **single** bigram in a 100-word sentence has a probability of $0.0$, the entire multiplication chain collapses to exactly $0.0$.

For example, if you ask the model the probability of "I am eating a delicious apple", but the bigram "delicious apple" never appeared in the training data, the model will confidently declare that the probability of someone saying "I am eating a delicious apple" is absolutely impossible ($0.0$). 

This is catastrophic. The model cannot generalize to perfectly valid, normal sentences just because it didn't see that exact word combination in training.

## 3. Unknown Words vs Unseen N-grams
It is important to distinguish between two different zero-probability problems:

1. **Unknown Words (Out of Vocabulary - OOV)**: A completely new word that the model has never seen before (e.g., a new slang term like "rizz").
   - *Solution*: As covered in Tokenization, we handle this by mapping rare words to an `<UNK>` token during training, so the model learns a probability distribution for unknown words.
2. **Unseen N-grams**: Both words are in the vocabulary, but they have never appeared *next to each other* (e.g., "delicious" and "apple").
   - *Solution*: We cannot use `<UNK>` here, because both words are known. We must use **Smoothing**.

## 4. Why Smoothing is Necessary
To prevent the Chain Rule from collapsing to zero, we must guarantee that no valid n-gram ever has a probability of exactly $0.0$.

**Smoothing** (or Discounting) is the mathematical process of "stealing" a tiny bit of probability mass from the n-grams we *did* see, and redistributing it to all the n-grams we *didn't* see.

This ensures that "delicious apple" gets a very small, non-zero probability (e.g., $0.00001$), allowing the sentence probability calculation to survive. We will cover the specific mathematical formulas for smoothing in the next module.

## 5. Exam Preparation
### Must Know
- A single $0.0$ probability in an n-gram chain forces the entire sentence probability to $0.0$.
- Unknown words are handled by `<UNK>`. Unseen sequences of known words are handled by Smoothing.

### Likely Theory Question
**Question**: A Bigram language model is trained on the works of Shakespeare. When asked to evaluate the sentence "The king texted the queen", the model returns a probability of 0.0. Explain exactly why this happens, distinguishing between OOV words and unseen n-grams.
**Answer**: The word "texted" never appears in Shakespeare, so it is an Out-Of-Vocabulary (OOV) word. If the system does not implement an `<UNK>` token fallback, the unigram probability of "texted" is 0.0, causing the sentence probability to become 0.0. Even if "texted" was in the vocabulary, the bigram "king texted" never appears in the text. This is an unseen n-gram, which will also yield a 0.0 probability under basic MLE unless a Smoothing algorithm is applied.

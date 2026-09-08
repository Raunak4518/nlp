# Formula Sheet

This page collects all the critical mathematical formulas introduced across the NLP syllabus. 

---

### TF-IDF

!!! abstract "Term Frequency"
    $$ TF(t, d) = \log_{10}(\text{count}(t, d) + 1) $$
    
    * **$t$**: The specific term.
    * **$d$**: The specific document.
    * *Purpose*: Measures how frequently a term appears in a document, scaled logarithmically to dampen the effect of highly repetitive words.

!!! abstract "Inverse Document Frequency"
    $$ IDF(t) = \log_{10}\left(\frac{N}{DF(t)}\right) $$
    
    * **$N$**: Total number of documents in the corpus.
    * **$DF(t)$**: Number of documents that contain term $t$.
    * *Purpose*: Measures how rare and informative a term is across the entire corpus.

!!! abstract "TF-IDF Weight"
    $$ W(t, d) = TF(t, d) \times IDF(t) $$

---

### Vector Semantics

!!! abstract "Cosine Similarity"
    $$ \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\|\|\mathbf{B}\|} = \frac{\sum_{i=1}^{n} A_i B_i}{\sqrt{\sum_{i=1}^{n} A_i^2} \sqrt{\sum_{i=1}^{n} B_i^2}} $$
    
    * **$\mathbf{A}, \mathbf{B}$**: Two text vectors.
    * *Purpose*: Measures the similarity in direction between two vectors, ranging from -1 (opposite) to 1 (identical direction), ignoring magnitude.

---

### Probability & Language Models

!!! abstract "Bayes' Theorem"
    $$ P(A|B) = \frac{P(B|A) P(A)}{P(B)} $$

!!! abstract "Chain Rule of Probability"
    $$ P(w_1, w_2, \ldots, w_n) = \prod_{i=1}^{n} P(w_i | w_1, \ldots, w_{i-1}) $$
    
    * *Purpose*: Decomposes the probability of an entire sentence into a sequence of conditional next-word probabilities.

!!! abstract "Markov Assumption (Bigram Model)"
    $$ P(w_i | w_1, \ldots, w_{i-1}) \approx P(w_i | w_{i-1}) $$
    
    * *Purpose*: Approximates history by assuming the probability of a word depends *only* on the single preceding word.

!!! abstract "Maximum Likelihood Estimation (Bigram)"
    $$ P(w_i | w_{i-1}) = \frac{C(w_{i-1}, w_i)}{C(w_{i-1})} $$
    
    * **$C(x)$**: The exact raw count of sequence $x$ in the training corpus.

---

### Smoothing

!!! abstract "Laplace (Add-1) Smoothing"
    $$ P_{Laplace}(w_i | w_{i-1}) = \frac{C(w_{i-1}, w_i) + 1}{C(w_{i-1}) + V} $$
    
    * **$V$**: Vocabulary size (total unique words in the corpus).

!!! abstract "Add-k Smoothing"
    $$ P_{Add-k}(w_i | w_{i-1}) = \frac{C(w_{i-1}, w_i) + k}{C(w_{i-1}) + k \cdot V} $$

!!! abstract "Good-Turing Adjusted Count"
    $$ c^* = (c + 1) \frac{N_{c+1}}{N_c} $$
    
    * **$c$**: The original raw count of an n-gram.
    * **$N_c$**: The "count of counts" (how many unique n-grams appeared exactly $c$ times).

!!! abstract "Linear Interpolation"
    $$ \hat{P}(w_i|w_{i-2}, w_{i-1}) = \lambda_1 P_3(w_i|w_{i-2},w_{i-1}) + \lambda_2 P_2(w_i|w_{i-1}) + \lambda_3 P_1(w_i) $$
    
    * **Requirement**: $\lambda_1 + \lambda_2 + \lambda_3 = 1$.

---

### Evaluation Metrics

!!! abstract "Perplexity"
    $$ PP(W) = P(w_1, \ldots, w_N)^{-\frac{1}{N}} $$
    *or*
    $$ PP(W) = 2^{\text{Cross-Entropy}} $$
    
    * *Purpose*: Evaluates language models. **Lower is better**.

!!! abstract "Precision, Recall, and F1"
    $$ \text{Precision} = \frac{TP}{TP + FP} $$
    
    $$ \text{Recall} = \frac{TP}{TP + FN} $$
    
    $$ F_1 = \frac{2 \times \text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} $$
    
    * *Purpose*: Evaluates Classification and NER models. **Higher is better**.

---

### Zipf's Law

!!! abstract "Zipf's Law"
    $$ f \propto \frac{1}{r} \implies f \times r = k $$
    
    * **$f$**: Frequency of the word.
    * **$r$**: Rank of the word.
    * **$k$**: A constant for the specific corpus.
    * *Purpose*: Empirically models the highly skewed distribution of word frequencies in natural language.

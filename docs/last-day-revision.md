# Last-Day Revision

This page is the ultimate, dense, high-speed revision layer. It strips away all intuitions and examples, leaving only the raw facts, formulas, and classifications required for the exam.

---

## 1. Text Processing
- **Regex**: Defines regular languages. Equivalent to FSAs.
- **Normalization**: Lowercasing, removing punctuation.
- **Stemming vs Lemmatization**:
  - *Stemming*: Heuristic, fast, chops endings, can produce non-words (e.g., `better` $\rightarrow$ `bet`).
  - *Lemmatization*: Dictionary-based, slower, produces valid roots (e.g., `better` $\rightarrow$ `good`).
- **BPE**: Subword tokenization. Merges most frequent character pairs. Solves OOV problem.
- **Edit Distance**: Minimum insertions, deletions, substitutions. Matrix dimensions: $(|A|+1) \times (|B|+1)$.

## 2. Sequence Labeling
- **POS Tagging**: Identifying noun, verb, adjective. Ambiguity is the main challenge.
- **NER**: Identifying Person, Org, Location. Uses BIO tagging (Begin, Inside, Outside).
- **HMM**: $P(\text{State}|\text{Previous State})$ [Transitions] and $P(\text{Word}|\text{State})$ [Emissions].
- **Viterbi**: Dynamic programming for HMMs. Avoids exponential paths. $O(T K^2)$. Requires backpointers.

## 3. Parsing
- **CFG**: Context-Free Grammar. Rules like $S \rightarrow NP \ VP$.
- **CKY Algorithm**: Bottom-up parsing. Requires Chomsky Normal Form ($A \rightarrow B C$ or $A \rightarrow x$).
- **Dependency Parsing**: Connects words with directed arrows. Head-dependent relationships. No non-terminals (no NP, VP).

## 4. Vector Semantics
- **Bag of Words**: Counts frequencies. Ignores order.
- **TF-IDF**: $TF \times \log(N/DF)$. High weight = frequent in this document, rare globally.
- **Cosine Similarity**: $\mathbf{A} \cdot \mathbf{B} / (\|\mathbf{A}\| \|\mathbf{B}\|)$. Normalizes length. 1 = identical angle. 0 = orthogonal.

## 5. Language Models
- **Markov Assumption**: Bigram model assumes word only depends on the *one* previous word.
- **Perplexity**: Inverse probability. Lower = better.
- **Laplace Smoothing**: Add 1 to all counts. Shifts too much probability mass.
- **Add-k Smoothing**: Add fraction $k$. Better than Laplace.
- **Good-Turing**: Adjusts counts based on $N_c$ (how many things occurred $c$ times). $P_{unseen} = N_1 / N$.
- **Interpolation**: Combining Unigram, Bigram, Trigram with $\lambda$ weights ($\lambda_1+\lambda_2+\lambda_3=1$).
- **Stupid Backoff**: If trigram missing, use bigram and multiply by penalty (e.g., 0.4).
- **Kneser-Ney**: Subtract $d$ (Absolute Discounting). Backoff uses *continuation probability* (how many different contexts the word follows).

## 6. Classification & Applications
- **Naive Bayes**: Multiplies Prior $P(C)$ by Likelihoods $P(w_i|C)$. Assumes features (words) are conditionally independent given the class. Uses log probabilities to prevent underflow.
- **Sentiment Analysis**: Evaluated with F1, not Accuracy (due to imbalanced data). Lexicons fail on negation.
- **Generative Decoding**:
  - *Greedy*: Pick best next word.
  - *Beam Search*: Keep top $K$ paths.
  - *Temperature*: $T < 1$ = greedy/repetitive. $T > 1$ = random/creative.
- **Machine Translation (MT)**: SMT used Noisy Channel. NMT uses Seq2Seq. Evaluated via BLEU (Precision + Brevity Penalty).
- **Summarization**: Extractive (highlights sentences) vs Abstractive (generates new text). Evaluated via ROUGE (Recall).
- **Information Extraction**: Entity Linking (maps to database ID). Relation Extraction (creates Subject-Predicate-Object triples for Knowledge Graphs).

## 7. Evaluation Metrics Cheat-Table

| Task | Primary Metric | Rule | Key Feature |
| :--- | :--- | :--- | :--- |
| **Language Modeling** | Perplexity | Lower is better | Uses Cross-Entropy |
| **Classification** | F1-Score | Higher is better | Harmonic mean of Precision & Recall |
| **NER** | Entity-Level F1 | Higher is better | Token-level accuracy is misleading |
| **Machine Translation** | BLEU | Higher is better | N-gram Precision + Brevity Penalty |
| **Summarization** | ROUGE | Higher is better | N-gram Recall |

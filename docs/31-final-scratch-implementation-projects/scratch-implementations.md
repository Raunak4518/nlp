# Final Scratch-Implementation Projects

## 1. The Capstone Codebase
Throughout this rigorously mathematical course, we have heavily emphasized the fundamental importance of building NLP algorithms entirely from scratch without ever relying on black-box libraries like NLTK, SpaCy, or HuggingFace. 

If you cannot manually translate mathematical equations into performant Python code, you do not truly understand the algorithm. Below is an index and unified collection of the most mathematically critical scratch implementations required for mastery.

> [!TIP]
> **Study Method**
> Do not simply read this code. Open a completely blank Jupyter Notebook, hide this page, and attempt to write these algorithms strictly from memory based on the mathematical equations you learned in previous modules.

---

## 2. Tokenization and Parsing (Modules 3-11)

### Regex Tokenizer
```python
import re

def tokenize(text: str) -> list[str]:
    """
    A foundational Regular Expression tokenizer.
    Mathematically matches consecutive word characters (\w+) OR non-word/non-space characters.
    """
    pattern = r"\w+|[^\w\s]"
    return re.findall(pattern, text)
```

### Viterbi Algorithm (HMM POS Tagger)
The Viterbi algorithm is a brilliant Dynamic Programming algorithm used to find the mathematically most likely sequence of hidden states (e.g., POS Tags) given a sequence of observed events (words).

```python
def viterbi(obs: list[str], states: list[str], start_p: dict, trans_p: dict, emit_p: dict) -> list[str]:
    """
    Viterbi Dynamic Programming Decoding.
    Time Complexity: O(N * S^2) where N is observation length and S is number of states.
    """
    V = [{}]
    path = {}

    # 1. Initialize base cases (time t == 0) using Start Probabilities
    for y in states:
        V[0][y] = start_p.get(y, 0.0) * emit_p[y].get(obs[0], 0.0)
        path[y] = [y]

    # 2. Run the dynamic programming recursive step for t > 0
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}

        for y in states:
            # Find the MAXIMUM probability to arrive at state y at time t
            # by checking every possible previous state y0 at time t-1
            (prob, state) = max(
                (V[t-1][y0] * trans_p[y0].get(y, 0.0) * emit_p[y].get(obs[t], 0.0), y0) 
                for y0 in states
            )
            V[t][y] = prob
            # Save the backpointer path
            newpath[y] = path[state] + [y]

        path = newpath

    # 3. Return the fully reconstructed path of the highest probability final state
    n = len(obs) - 1
    (prob, state) = max((V[n][y], y) for y in states)
    return path[state]
```

---

## 3. Language Modeling and Smoothing (Modules 14-21)

### Add-k Smoothing
```python
def add_k_smoothing(bigram_count: int, context_count: int, vocab_size: int, k: float) -> float:
    """
    Solves the zero-probability problem by mathematically adding 'k' 
    to all numerator counts and 'k*V' to the denominator.
    """
    return (bigram_count + k) / (context_count + (k * vocab_size))
```

### Stupid Backoff
```python
def stupid_backoff(w1: str, w2: str, w3: str, trigrams: dict, bigrams: dict, unigrams: dict, total_words: int, penalty: float = 0.4) -> float:
    """
    Backs off to lower-order N-grams if higher-order counts are 0,
    multiplying by a static alpha penalty (0.4) at each backoff step.
    """
    if trigrams.get((w1, w2, w3), 0) > 0:
        return trigrams[(w1, w2, w3)] / bigrams[(w1, w2)]
    
    elif bigrams.get((w2, w3), 0) > 0:
        return penalty * (bigrams[(w2, w3)] / unigrams[w2])
    
    elif unigrams.get(w3, 0) > 0:
        return (penalty * penalty) * (unigrams[w3] / total_words)
    
    return 0.0
```

### Interpolated Kneser-Ney (Bigram)
The mathematically optimal classical smoothing algorithm. It uses Absolute Discounting to steal probability mass, and Continuation Probabilities to redistribute it intelligently.

```python
def kneser_ney_bigram(w1: str, w2: str, bigrams: dict, unigrams: dict, total_bigram_types: int, d: float = 0.75) -> float:
    # 1. Absolute Discounting
    c_w1_w2 = bigrams.get((w1, w2), 0)
    discounted_term = max(c_w1_w2 - d, 0) / unigrams[w1]
    
    # 2. Calculate Lambda (The normalization constant for the stolen mass)
    types_following_w1 = sum(1 for (a, b) in bigrams.keys() if a == w1)
    lambda_w1 = (d / unigrams[w1]) * types_following_w1
    
    # 3. Calculate Continuation Probability P_cont(w2)
    types_preceding_w2 = sum(1 for (a, b) in bigrams.keys() if b == w2)
    p_continuation = types_preceding_w2 / total_bigram_types
    
    # 4. Interpolate
    return discounted_term + (lambda_w1 * p_continuation)
```

---

## 4. Evaluation (Modules 23-25)

### Perplexity Calculator
```python
import math

def calculate_perplexity(sentence: list[str], lm_prob_func) -> float:
    """
    Calculates the mathematically rigorous Perplexity of a sentence.
    PP(W) = 2^(-(1/N) * sum(log2(P(w_i | w_i-1))))
    """
    N = len(sentence)
    log_prob_sum = 0.0
    
    for i in range(1, N):
        prob = lm_prob_func(sentence[i-1], sentence[i])
        if prob == 0.0:
            return float('inf') # Zero probability instantly breaks perplexity
        log_prob_sum += math.log2(prob)
        
    cross_entropy = - (1 / N) * log_prob_sum
    return 2 ** cross_entropy
```

### F1-Score Calculator
```python
def calculate_f1(tp: int, fp: int, fn: int) -> float:
    """
    Calculates the Harmonic Mean of Precision and Recall.
    """
    if tp == 0:
        return 0.0
        
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    
    # Harmonic Mean
    return 2 * (precision * recall) / (precision + recall)
```

---

## 5. Tokenization Trainers (Module 24)

### BPE Subword Merger
```python
def bpe_merge(pair: tuple, vocab: dict) -> dict:
    """
    Performs a single frequency-based Byte-Pair Encoding merge step.
    Replaces all instances of the space-separated bigram with the merged token.
    """
    v_out = {}
    bigram = " ".join(pair)        # e.g., "l o"
    replacement = "".join(pair)    # e.g., "lo"
    
    for word in vocab:
        # String replacement logic
        w_out = word.replace(bigram, replacement)
        v_out[w_out] = vocab[word]
        
    return v_out
```

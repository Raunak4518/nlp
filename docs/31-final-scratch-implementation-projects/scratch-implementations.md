# Final Scratch-Implementation Projects

## 1. The Capstone Codebase
Throughout this course, we have emphasized the importance of building NLP algorithms from scratch without relying on libraries like NLTK or SpaCy. Below is an index and unified collection of the most critical scratch implementations required for mastery.

*Note: For the detailed step-by-step trace of each algorithm, refer back to the specific module.*

## 2. Tokenization and Parsing (Modules 3-11)
### Regex Tokenizer
```python
import re
def tokenize(text: str) -> list[str]:
    # Matches words, numbers, and basic punctuation
    pattern = r"\w+|[^\w\s]"
    return re.findall(pattern, text)
```

### Viterbi Algorithm (HMM POS Tagger)
```python
def viterbi(obs: list[str], states: list[str], start_p: dict, trans_p: dict, emit_p: dict) -> list[str]:
    V = [{}]
    path = {}

    # Initialize base cases (t == 0)
    for y in states:
        V[0][y] = start_p.get(y, 0.0) * emit_p[y].get(obs[0], 0.0)
        path[y] = [y]

    # Run Viterbi for t > 0
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}

        for y in states:
            # Find the maximum probability to arrive at state y at time t
            (prob, state) = max(
                (V[t-1][y0] * trans_p[y0].get(y, 0.0) * emit_p[y].get(obs[t], 0.0), y0) 
                for y0 in states
            )
            V[t][y] = prob
            newpath[y] = path[state] + [y]

        path = newpath

    # Return the path of the highest probability final state
    n = len(obs) - 1
    (prob, state) = max((V[n][y], y) for y in states)
    return path[state]
```

## 3. Language Modeling and Smoothing (Modules 14-21)
### Add-k Smoothing
```python
def add_k_smoothing(bigram_count: int, context_count: int, vocab_size: int, k: float) -> float:
    return (bigram_count + k) / (context_count + (k * vocab_size))
```

### Stupid Backoff
```python
def stupid_backoff(w1, w2, w3, trigrams, bigrams, unigrams, total_words, penalty=0.4):
    if trigrams.get((w1, w2, w3), 0) > 0:
        return trigrams[(w1, w2, w3)] / bigrams[(w1, w2)]
    elif bigrams.get((w2, w3), 0) > 0:
        return penalty * (bigrams[(w2, w3)] / unigrams[w2])
    elif unigrams.get(w3, 0) > 0:
        return (penalty * penalty) * (unigrams[w3] / total_words)
    return 0.0
```

### Interpolated Kneser-Ney (Bigram)
```python
def kneser_ney_bigram(w1, w2, bigrams, unigrams, total_bigram_types, d=0.75):
    c_w1_w2 = bigrams.get((w1, w2), 0)
    discounted_term = max(c_w1_w2 - d, 0) / unigrams[w1]
    
    types_following_w1 = sum(1 for (a, b) in bigrams.keys() if a == w1)
    lambda_w1 = (d / unigrams[w1]) * types_following_w1
    
    types_preceding_w2 = sum(1 for (a, b) in bigrams.keys() if b == w2)
    p_continuation = types_preceding_w2 / total_bigram_types
    
    return discounted_term + (lambda_w1 * p_continuation)
```

## 4. Evaluation (Modules 23-25)
### Perplexity Calculator
```python
import math

def calculate_perplexity(sentence: list[str], lm_prob_func) -> float:
    N = len(sentence)
    log_prob_sum = 0.0
    
    for i in range(1, N):
        # Calculate P(w_i | w_i-1)
        prob = lm_prob_func(sentence[i-1], sentence[i])
        if prob == 0.0:
            return float('inf') # Zero probability breaks perplexity
        log_prob_sum += math.log2(prob)
        
    cross_entropy = - (1 / N) * log_prob_sum
    return 2 ** cross_entropy
```

### F1 Score Calculator
```python
def calculate_f1(tp: int, fp: int, fn: int) -> float:
    if tp == 0:
        return 0.0
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    return 2 * (precision * recall) / (precision + recall)
```

## 5. Tokenization Trainers (Module 24)
### BPE Subword Merger
```python
def bpe_merge(pair: tuple, vocab: dict) -> dict:
    v_out = {}
    bigram = " ".join(pair)
    replacement = "".join(pair)
    
    for word in vocab:
        w_out = word.replace(bigram, replacement)
        v_out[w_out] = vocab[word]
    return v_out
```

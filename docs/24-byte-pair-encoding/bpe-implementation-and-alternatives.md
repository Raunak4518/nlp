# BPE Implementation and Alternatives

## 1. Scratch Implementation (BPE Trainer)
To fully understand BPE, you must be able to write the loop that counts and merges pairs.

```python
import collections

def get_stats(vocab):
    """Count the frequency of adjacent pairs of symbols."""
    pairs = collections.defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols)-1):
            pairs[symbols[i], symbols[i+1]] += freq
    return pairs

def merge_vocab(pair, v_in):
    """Merge the most frequent pair in all words."""
    v_out = {}
    bigram = " ".join(pair)       # e.g., "e r"
    replacement = "".join(pair)   # e.g., "er"
    
    for word in v_in:
        # Replace the space-separated bigram with the merged string
        w_out = word.replace(bigram, replacement)
        v_out[w_out] = v_in[word]
    return v_out

# --- Trace ---
# Initial vocabulary (words split into characters with </w> at the end)
vocab = {
    'l o w </w>': 5,
    'l o w e s t </w>': 2,
    'n e w e r </w>': 6,
    'w i d e r </w>': 3
}

num_merges = 3

for i in range(num_merges):
    pairs = get_stats(vocab)
    if not pairs:
        break
        
    # Find the most frequent pair
    best = max(pairs, key=pairs.get)
    print(f"Merge #{i+1}: {best} (Freq: {pairs[best]})")
    
    # Execute the merge
    vocab = merge_vocab(best, vocab)

print("\nFinal Vocab:")
for k, v in vocab.items():
    print(f"{k}: {v}")

# Output:
# Merge #1: ('e', 'r') (Freq: 9)
# Merge #2: ('er', '</w>') (Freq: 9)
# Merge #3: ('l', 'o') (Freq: 7)
#
# Final Vocab:
# lo w </w>: 5
# lo w e s t </w>: 2
# n e w er</w>: 6
# w i d er</w>: 3
```

## 2. BPE Numerical Problem Walkthrough
**Problem**: Given the dictionary `{'f a s t </w>': 4, 'f a t e </w>': 3}`, what is the very first merge operation BPE will perform?

**Solution**:
1. Count all pairs.
   - `f a`: occurs 4 (fast) + 3 (fate) = 7 times.
   - `a s`: occurs 4 times.
   - `s t`: occurs 4 times.
   - `t </w>`: occurs 4 times.
   - `a t`: occurs 3 times.
   - `t e`: occurs 3 times.
   - `e </w>`: occurs 3 times.
2. The most frequent pair is `f a` (7 times).
3. The first merge operation will be merging `f` and `a` into `fa`.

## 3. Subword Tokenization Alternatives

### WordPiece
Used by **BERT**. It is very similar to BPE. Both start with characters and merge them. 
- *Difference*: BPE merges the pair that is the *most frequent*. WordPiece merges the pair that *maximizes the likelihood* of the training data. It evaluates pairs using a language model score rather than raw frequency.

### Unigram LM Tokenization
Used by **SentencePiece** (and Albert/T5). 
- *Difference*: It operates in reverse. It starts with a massive vocabulary of all possible subwords, and iteratively *removes* the least useful ones until it hits the target vocabulary size. It uses a unigram language model to determine which subwords cause the smallest drop in likelihood when removed.

## 4. Exam Preparation
### Must Memorize
- `get_stats()` counts adjacent pairs.
- `merge_vocab()` concatenates the most frequent pair.
- WordPiece maximizes likelihood; BPE maximizes raw frequency.

### Likely Practical Question
**Question**: Perform 2 BPE merges on the corpus `{'b o o k </w>': 2, 'l o o k </w>': 1}`.
**Answer**:
1. Pair counts: `b o`: 2, `o o`: 3, `o k`: 3, `k </w>`: 3, `l o`: 1.
2. There is a 3-way tie for the highest frequency (`o o`, `o k`, `k </w>`). (Assume alphabetical tie-breaking or first-encountered). Let's merge `o o` into `oo`.
3. New Corpus: `{'b oo k </w>': 2, 'l oo k </w>': 1}`.
4. Next pair counts: `b oo`: 2, `oo k`: 3, `k </w>`: 3, `l oo`: 1.
5. Merge `oo k` into `ook`.
6. Final Corpus: `{'b ook </w>': 2, 'l ook </w>': 1}`.

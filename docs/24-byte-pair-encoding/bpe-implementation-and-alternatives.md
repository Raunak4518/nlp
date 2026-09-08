# BPE Implementation and Alternatives

## 1. Scratch Implementation (BPE Trainer)
To fully mathematically understand Byte Pair Encoding, you must be able to trace the Python loop that algorithmically counts and merges the character pairs.

```python
import collections

def get_stats(vocab: dict) -> dict:
    """Algorithmically scan the vocabulary and count adjacent pairs of symbols."""
    pairs = collections.defaultdict(int)
    for word, freq in vocab.items():
        # Words are stored as space-separated strings (e.g. "l o w </w>")
        symbols = word.split()
        
        # Iterate through the symbols to find all adjacent pairs
        for i in range(len(symbols)-1):
            pairs[symbols[i], symbols[i+1]] += freq
            
    return pairs

def merge_vocab(pair: tuple, v_in: dict) -> dict:
    """Merge the most frequent pair in all words across the entire vocabulary."""
    v_out = {}
    
    # We must be extremely careful with spaces during replacement
    bigram = " ".join(pair)       # The target to find (e.g., "e r")
    replacement = "".join(pair)   # The new merged symbol (e.g., "er")
    
    for word in v_in:
        # Replace the space-separated bigram with the single merged string
        w_out = word.replace(bigram, replacement)
        v_out[w_out] = v_in[word]
        
    return v_out
```

### Try It Yourself

??? question "Trace the BPE Loop"
    ```python
    # Initial vocabulary (Words physically split into characters with </w> appended)
    vocab = {
        'l o w </w>': 5,
        'l o w e s t </w>': 2,
        'n e w e r </w>': 6,
        'w i d e r </w>': 3
    }
    
    num_merges = 3
    
    for i in range(num_merges):
        # Step 1: Count
        pairs = get_stats(vocab)
        if not pairs:
            break
            
        # Step 2: Find the mathematical maximum
        best = max(pairs, key=pairs.get)
        print(f"Merge #{i+1}: {best} (Freq: {pairs[best]})")
        
        # Step 3: Execute the merge
        vocab = merge_vocab(best, vocab)
    
    print("\nFinal Vocab State:")
    for k, v in vocab.items():
        print(f"{k}: {v}")
    
    # OUTPUT TRACE:
    # Merge #1: ('e', 'r') (Freq: 9)
    # Merge #2: ('er', '</w>') (Freq: 9)
    # Merge #3: ('l', 'o') (Freq: 7)
    #
    # Final Vocab State:
    # lo w </w>: 5
    # lo w e s t </w>: 2
    # n e w er</w>: 6
    # w i d er</w>: 3
    ```

---

## 2. BPE Numerical Problem Walkthrough

**Problem**: You are executing a manual BPE training loop. Given the initial dictionary state `{'f a s t </w>': 4, 'f a t e </w>': 3}`, what is the mathematically exact first merge operation BPE will perform? Show your counts.

**Solution**:
1. Count all adjacent pairs mathematically:
   - `f a`: occurs 4 (from fast) + 3 (from fate) = **7 times**.
   - `a s`: occurs **4 times**.
   - `s t`: occurs **4 times**.
   - `t </w>`: occurs **4 times**.
   - `a t`: occurs **3 times**.
   - `t e`: occurs **3 times**.
   - `e </w>`: occurs **3 times**.
2. The maximum frequency pair is clearly `f a` (7 times).
3. The very first algorithmic merge operation will be merging `f` and `a` into the new single token `fa`.

---

## 3. Subword Tokenization Alternatives
While BPE is the most famous, there are two other highly popular subword algorithms used in modern Large Language Models:

### WordPiece (Used by BERT)
WordPiece was explicitly developed by Google and is the core tokenization algorithm inside BERT. It is algorithmically incredibly similar to BPE: both are bottom-up algorithms that start with base characters and iteratively merge them. 
- **The Core Difference**: BPE mathematically merges the pair that possesses the *highest raw frequency*. WordPiece evaluates pairs using a language model and merges the specific pair that *maximizes the likelihood* of the training data. (It asks: "Does combining these two symbols make the statistical probability of the training corpus higher?").

### Unigram LM Tokenization (Used by SentencePiece / T5)
Unigram Tokenization fundamentally operates in mathematical reverse compared to BPE. 
- **The Core Difference**: It is a top-down algorithm. It starts by aggressively initializing a massive, bloated vocabulary containing all possible substrings and subwords. Then, it iteratively *removes* (prunes) the mathematically least useful symbols until it cleanly hits the target hyperparameter vocabulary size. It uses a unigram language model to evaluate which subwords cause the smallest drop in total corpus likelihood when deleted.

---

## 4. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: Perform exactly 2 BPE merge iterations on the following toy corpus: `{'b o o k </w>': 2, 'l o o k </w>': 1}`. Show the state of the corpus after each step. In the event of a frequency tie, explicitly state your tie-breaking rule (e.g., alphabetical).
> **Answer**:
> **Iteration 1**:
> 1. Pair counts: `b o`: 2, `o o`: 3, `o k`: 3, `k </w>`: 3, `l o`: 1.
> 2. There is a 3-way mathematical tie for the highest frequency (`o o`, `o k`, `k </w>`). I will use alphabetical tie-breaking, so `k </w>` is chosen first.
> 3. We merge `k` and `</w>` into `k</w>`.
> 4. State of Corpus 1: `{'b o o k</w>': 2, 'l o o k</w>': 1}`.
> 
> **Iteration 2**:
> 1. New Pair counts: `b o`: 2, `o o`: 3, `o k</w>`: 3, `l o`: 1.
> 2. There is a 2-way tie (`o o`, `o k</w>`). Alphabetically, `o k</w>` wins.
> 3. We merge `o` and `k</w>` into `ok</w>`.
> 4. Final State of Corpus 2: `{'b o ok</w>': 2, 'l o ok</w>': 1}`.

**2-Mark Question**: Explain the fundamental algorithmic difference between Byte Pair Encoding (BPE) and Unigram LM Tokenization regarding how they construct their final vocabularies.
> **Answer**: BPE is a bottom-up algorithm; it initializes its vocabulary with individual base characters and incrementally *builds* the vocabulary by merging pairs until it hits the target size. Unigram Tokenization is a top-down algorithm; it initializes its vocabulary with a massive set of all possible subwords and incrementally *prunes* (removes) the least useful subwords until it hits the target size.

---

### Can You Explain This?
- [ ] I can write out the Python string logic used to replace bigrams.
- [ ] I can mathematically identify the correct pair to merge given a small dictionary of words and frequencies.
- [ ] I can state which algorithm BERT uses for tokenization.

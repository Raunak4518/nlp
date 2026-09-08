# Byte Pair Encoding (BPE) Fundamentals

## 1. Why Subword Tokenization is Needed
In Module 3, we discussed the classical approach of Word-level Tokenization. Word tokenization suffers from two fatal, mathematically unsolvable flaws:
1. **Infinite Vocabulary**: The English language structurally adds thousands of new words every year. Because of Zipf's Law, no fixed vocabulary table can ever contain every possible word.
2. **The `<UNK>` Problem**: When a classical Language Model encounters a word not in its exact vocabulary table (e.g., the novel word "un-friend-able"), it instantly replaces it with an `<UNK>` token. This completely destroys the semantic meaning. "un-friend-able" is made of three perfectly understandable morphemes (un + friend + able), but the LM treats it as total garbage.

We *could* theoretically use **Character-level Tokenization** (where the vocabulary is strictly just the 26 letters of the alphabet). This guarantees no `<UNK>` tokens, but then the LM has to mathematically learn from scratch that the raw letters 'c', 'a', 't' sequentially mean a feline. The context sequences become far too long and the model loses semantic meaning.

The modern solution is **Subword Tokenization**, which creates a dynamic, data-driven vocabulary of common sub-pieces of words. The most computationally popular subword algorithm is Byte Pair Encoding (BPE), used universally in GPT-3, GPT-4, and LLaMA.

---

## 2. The BPE Algorithm
Byte Pair Encoding (BPE) is historically a data compression algorithm that was brilliantly adapted for NLP. It starts with individual characters and iteratively merges the most highly frequent adjacent pairs into brand new, single mathematical symbols.

### Step 1: Character-level Initialization
Initialize the vocabulary with all the unique individual characters present in the training data, plus a critically special end-of-word symbol (usually `</w>`).
Physically split all words in the training data into space-separated characters.

*Example Corpus:*
- "low" (appears 5 times) $\rightarrow$ `l o w </w>`
- "lowest" (appears 2 times) $\rightarrow$ `l o w e s t </w>`
- "newer" (appears 6 times) $\rightarrow$ `n e w e r </w>`
- "wider" (appears 3 times) $\rightarrow$ `w i d e r </w>`

### Step 2: Count Adjacent Symbol Pairs
Algorithmically scan the entire corpus and explicitly count how many times every pair of adjacent symbols occurs.
- `l o`: 7 times *(5 from "low", 2 from "lowest")*
- `o w`: 7 times
- `e r`: 9 times *(6 from "newer", 3 from "wider")*

### Step 3: Merge the Most Frequent Pair
The specific pair `e r` is mathematically the most frequent (9 times). We add the brand new symbol `er` to our formal vocabulary table, and we replace all physical instances of `e` directly followed by `r` in the corpus with the new single symbol `er`.

*Updated Corpus:*
- "newer": `n e w er </w>`
- "wider": `w i d er </w>`

### Step 4: Repeat
We loop back and repeat Step 2 and Step 3 on the updated corpus. 
Next, `e r` might structurally merge with `</w>` to form the token `er</w>`. 
Next, `l o` might merge into the single token `lo`.

### Step 5: Stopping Condition
We strictly repeat this loop until we hit a predefined **target vocabulary size** hyperparameter (e.g., exactly 50,000 tokens) or a predefined **number of merge operations** (e.g., 30,000 merges).

---

## 3. Applying the BPE Vocabulary
Once the training loop is done, we have a fixed, ordered list of merge rules. 

When a brand new, unseen test word comes in (e.g., "lowest"), we do *not* run the count algorithm again. We simply split it into characters `l o w e s t </w>` and algorithmically apply the exact same ordered merge rules we learned during training.

If the test word is "lower" (which absolutely wasn't in our training data), the algorithm will still successfully merge it into the known subword tokens `low` and `er</w>`. The language model will process it perfectly without ever seeing it in training, permanently solving the OOV problem!

---

## 4. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: You are running the BPE algorithm. Your current corpus state is:
"f a s t </w>" (Count: 3)
"f a s t e r </w>" (Count: 2)
Identify the most frequent adjacent symbol pair. What will the exact string state of the corpus be after you perform the merge operation for that pair?
> **Answer**: 
> 1. The most frequent adjacent pair is `s t`. (It occurs 3 times in "fast" and 2 times in "faster", for a total of 5 times).
> 2. We merge `s` and `t` into the new symbol `st`.
> 3. The new corpus state is:
>    "f a st </w>" (Count: 3)
>    "f a st e r </w>" (Count: 2)

**2-Mark Question**: Conceptually, how does BPE guarantee that an LLM will never be forced to generate a completely meaningless `<UNK>` token?
> **Answer**: Because BPE explicitly initializes its vocabulary with every individual base character (or byte) present in the text before beginning the merge process. If a completely bizarre, unseen word is passed into the model, the BPE tokenizer will simply fall back to representing that word as a sequence of its individual known characters, completely avoiding the `<UNK>` token while preserving the spelling information.

---

### Can You Explain This?
- [ ] I can explicitly define the fatal flaws of both pure word-level tokenization and pure character-level tokenization.
- [ ] I can list the 5 structural steps of the BPE training algorithm.
- [ ] I can explain why the algorithm applies learned merge rules to new text rather than recalculating counts.

# Byte Pair Encoding (BPE) Fundamentals

## 1. Why Subword Tokenization is Needed
In Module 3, we discussed Word-level Tokenization. Word tokenization suffers from two fatal flaws:
1. **Infinite Vocabulary**: The English language adds thousands of new words every year. No fixed vocabulary can contain every word.
2. **The `<UNK>` Problem**: When a Language Model encounters a word not in its vocabulary (e.g., "un-friend-able"), it replaces it with `<UNK>`. This destroys the meaning. "un-friend-able" is made of three perfectly understandable morphemes (un + friend + able), but the LM treats it as total garbage.

We could use **Character-level Tokenization** (where the vocabulary is just the 26 letters of the alphabet), but then the LM has to learn from scratch that 'c', 'a', 't' means a feline. The sequences become too long and the model loses semantic meaning.

The solution is **Subword Tokenization**, which creates a vocabulary of common sub-pieces of words. The most popular subword algorithm is Byte Pair Encoding (BPE), used in GPT-3, GPT-4, and LLaMA.

## 2. The BPE Algorithm
BPE is a data compression algorithm that was adapted for NLP. It starts with characters and iteratively merges the most frequent pairs into new symbols.

### Step 1: Character-level starting representation
Initialize the vocabulary with all the unique individual characters in the training data, plus a special end-of-word symbol (usually `</w>`).
Split all words in the training data into characters.

*Example Corpus:*
- "low" (5 times) $\rightarrow$ `l o w </w>`
- "lowest" (2 times) $\rightarrow$ `l o w e s t </w>`
- "newer" (6 times) $\rightarrow$ `n e w e r </w>`
- "wider" (3 times) $\rightarrow$ `w i d e r </w>`

### Step 2: Count adjacent symbol pairs
Scan the corpus and count how many times every pair of adjacent symbols occurs.
- `l o`: 7 times (5 from "low", 2 from "lowest")
- `o w`: 7 times
- `e r`: 9 times (6 from "newer", 3 from "wider")

### Step 3: Merge the most frequent pair
The pair `e r` is the most frequent (9 times). We add the new symbol `er` to our vocabulary, and we replace all instances of `e` followed by `r` in the corpus with the new single symbol `er`.

*Updated Corpus:*
- "newer": `n e w er </w>`
- "wider": `w i d er </w>`

### Step 4: Repeat
We repeat Step 2 and Step 3. 
Next, `e r` might be merged with `</w>` to form `er</w>`. 
Next, `l o` might merge into `lo`.

### Step 5: Stopping Condition
We repeat this loop until we hit a predefined **target vocabulary size** (e.g., 50,000 tokens) or a predefined **number of merge operations** (e.g., 30,000 merges).

## 3. Applying the BPE Vocabulary
Once training is done, we have a fixed list of ordered merge rules. 
When a new, unseen word comes in (e.g., "lowest"), we split it into characters `l o w e s t </w>` and apply the exact same merge rules we learned during training, in the exact same order.

If the word is "lower" (which wasn't in our training data), it might successfully merge into `low` and `er</w>`. The model will understand it perfectly without ever seeing it in training, solving the OOV problem entirely!

## 4. Exam Preparation
### Must Memorize
- BPE starts with individual characters and merges the most frequent adjacent pairs.
- BPE perfectly solves the OOV (Out of Vocabulary) problem by ensuring that any unknown word can fall back to being represented as smaller known subwords, down to individual characters.

### Likely Theory Question
**Question**: Explain how BPE prevents a language model from generating an `<UNK>` token for an unseen word like "unhappiness".
**Answer**: BPE uses a vocabulary built from merging frequent subwords. During tokenization, if the full word "unhappiness" is not in the vocabulary, the BPE tokenizer will break it down using its learned merge rules. It will likely find the known subwords "un", "happi", and "ness" in its vocabulary. The model processes these three subword tokens instead of a single `<UNK>` token, preserving the semantic meaning of the unseen word.

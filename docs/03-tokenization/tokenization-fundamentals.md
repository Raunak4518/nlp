# Tokenization Fundamentals

## 1. What Is It?
Tokenization is the process of breaking down a continuous stream of text into smaller, discrete units called **tokens**. These tokens act as the fundamental atomic units that an NLP model processes.

## 2. Why Does It Exist?
Machine learning models (like Neural Networks) cannot read continuous text. They require distinct inputs that can be mapped to a vocabulary index and converted into mathematical vectors. Tokenization defines what those distinct inputs are.

## 3. Levels of Tokenization

### Character Units
Treating every single character (including spaces) as a token.
- **Pros**: Tiny vocabulary size (e.g., ~100 in English). No Unknown (`<UNK>`) tokens because any word can be spelled from characters.
- **Cons**: Characters themselves have almost no semantic meaning. The sequence length becomes huge, making it computationally expensive for models like Transformers to process.

### Word Units
Treating text bounded by spaces/punctuation as tokens.
- **Pros**: Words naturally carry semantic meaning.
- **Cons**: Massive vocabulary size. High number of `<UNK>` tokens for rare words or typos. Cannot handle morphologically rich languages well (e.g., Turkish or Finnish).

### Subword Units
Breaking rare words into meaningful sub-units (e.g., "unhappiness" -> "un", "happi", "ness") while keeping common words whole (e.g., "the").
- **Pros**: The industry standard (used in BERT, GPT). Balances vocabulary size and semantic meaning. Solves the `<UNK>` problem.
- **Cons**: More complex to train and implement (e.g., BPE, WordPiece).

### Sentence, Paragraph, and Document Units
Sometimes, the fundamental unit of processing isn't a word, but a higher-level structure.
- **Sentence Units**: Useful for machine translation (translating sentence by sentence).
- **Paragraph/Document**: Useful for information retrieval and long-context summarization.

## 4. Unknown-Token Handling (`<UNK>`)
When using Word Tokenization, any word in the test set that was not seen during training is mapped to a special `<UNK>` token. 
If a sentence has too many `<UNK>` tokens, the model loses all context. This is the primary reason modern NLP uses Subword Tokenization.

## 5. Exam Preparation
### Must Memorize
- The tradeoffs between Character, Word, and Subword tokenization.

### Likely Theory Question
**Question**: Why do modern Large Language Models (like GPT-4) use subword tokenization instead of word tokenization?
**Answer**: Word tokenization requires an impractically large vocabulary to cover all possible words, derivations, and misspellings, and inevitably results in `<UNK>` tokens for unseen words. Subword tokenization limits the vocabulary size (e.g., to 50,000 tokens) while ensuring that *any* unseen word can still be represented as a sequence of known subword chunks or characters, completely eliminating the `<UNK>` problem.

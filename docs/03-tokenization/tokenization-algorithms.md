# Tokenization Algorithms & Scratch Implementations

## 1. Whitespace Tokenization
The absolute simplest form of tokenization. It splits text purely on spaces, tabs, and newlines.

### Scratch Implementation
```python
def whitespace_tokenize(text: str) -> list[str]:
    # Python's built-in .split() with no arguments splits on all whitespace
    return text.split()
```

### Try It Yourself
??? question "Trace the code on this input"
    **Input:** `"The cat, sat on the mat!"`
    
    **Output:** `['The', 'cat,', 'sat', 'on', 'the', 'mat!']`
    
    *Notice how the punctuation is glued to the words (`cat,`, `mat!`). This inflates the vocabulary unnecessarily because the model will treat `mat` and `mat!` as two completely unrelated words.*

---

## 2. Punctuation Tokenization
To fix the vocabulary inflation issue, we can separate punctuation from the alphabetic words.

### Scratch Implementation
```python
import string

def punctuation_tokenize(text: str) -> list[str]:
    # Add spaces around punctuation, then split on whitespace
    for p in string.punctuation:
        text = text.replace(p, f" {p} ")
    
    # Clean up double spaces and split
    return text.split()
```

### Try It Yourself
??? question "Trace the code on this input"
    **Input:** `"I bought it for $100.00 in the U.S.A."`
    
    **Output:** `['I', 'bought', 'it', 'for', '$', '100', '.', '00', 'in', 'the', 'U', '.', 'S', '.', 'A', '.']`
    
    *While this solves the vocabulary inflation for simple words, it destroys complex concepts. Ripping the periods out of `U.S.A.` or `100.00` destroys the semantic meaning of the acronym and the decimal.*

---

## 3. Regex-Based Tokenization
To handle the edge cases of simple punctuation splitting, we define complex Regular Expressions that declare exactly what constitutes a valid token (e.g., words, decimals, money, URLs).

### Scratch Implementation
```python
import re

def regex_tokenize(text: str) -> list[str]:
    # Define a regex pattern for valid tokens:
    # 1. Words with optional internal apostrophes (e.g., don't, it's)
    # 2. Numbers with optional decimals (e.g., 99.99)
    # 3. Standalone punctuation
    pattern = r"[a-zA-Z]+'[a-zA-Z]+|[a-zA-Z]+|\d+\.\d+|\d+|[^\w\s]"
    
    return re.findall(pattern, text)
```

### Try It Yourself
??? question "Trace the code on this input"
    **Input:** `"I can't believe it's $99.99!"`
    
    **Output:** `['I', "can't", 'believe', "it's", '$', '99.99', '!']`

---

## 4. N-gram Tokenization
Sometimes, treating single words as tokens removes too much context. An **n-gram** is a contiguous sequence of *n* items from a given text sequence.

- **1-gram (unigram)**: `["the", "cat", "sat"]`
- **2-gram (bigram)**: `["the cat", "cat sat"]`
- **3-gram (trigram)**: `["the cat sat"]`

### The N-gram Mathematics
If you have a sequence of $N$ tokens, how many $n$-grams will it produce?
!!! abstract "N-gram Count Formula"
    $$ \text{Total N-grams} = N - n + 1 $$

### Scratch Implementation
```python
def ngram_tokenize(tokens: list[str], n: int) -> list[str]:
    ngrams = []
    # Loop from 0 to (Total length - n + 1)
    for i in range(len(tokens) - n + 1):
        # Slice n elements and join them with a space
        ngram = " ".join(tokens[i : i+n])
        ngrams.append(ngram)
    return ngrams
```

---

## 5. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: Write a Python function from scratch that takes a list of string tokens and an integer $n$, and returns a list of all $n$-grams. Do not use external libraries.
> **Answer**:
> ```python
> def get_ngrams(tokens, n):
>     ngrams = []
>     for i in range(len(tokens) - n + 1):
>         ngrams.append(tokens[i:i+n])
>     return ngrams
> ```

**2-Mark Question**: A sentence contains 15 words. If you tokenize it into trigrams ($n=3$), how many trigrams will be produced?
> **Answer**: Using the formula $N - n + 1$, the calculation is $15 - 3 + 1 = 13$ trigrams.

**3-Mark Question**: Given the sentence `"It's raining cats & dogs."`, state the exact output of a pure whitespace tokenizer versus a pure punctuation-splitting tokenizer.
> **Answer**:
> - **Whitespace**: `["It's", "raining", "cats", "&", "dogs."]`.
> - **Punctuation**: `["It", "'", "s", "raining", "cats", "&", "dogs", "."]`.

---

### Can You Explain This?
- [ ] I can write a whitespace tokenizer in one line of Python.
- [ ] I can explain why pure punctuation-splitting breaks decimals and acronyms.
- [ ] I can write an n-gram extractor from scratch.
- [ ] I can calculate the exact number of n-grams produced by a sequence of length $N$.

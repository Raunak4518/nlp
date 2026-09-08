# Tokenization Algorithms & Scratch Implementations

## 1. Whitespace Tokenization
The absolute simplest form of tokenization. It splits text purely on spaces, tabs, and newlines.

### Scratch Implementation
```python
def whitespace_tokenize(text: str) -> list[str]:
    # Python's built in .split() with no arguments splits on all whitespace
    return text.split()

# Example
print(whitespace_tokenize("The cat, sat on the mat!"))
# Output: ['The', 'cat,', 'sat', 'on', 'the', 'mat!']
```
*Notice how the punctuation is glued to the words ("cat,", "mat!"). This inflates the vocabulary unnecessarily.*

## 2. Punctuation Tokenization
To fix the issue above, we can separate punctuation from words.

### Scratch Implementation
```python
import string

def punctuation_tokenize(text: str) -> list[str]:
    # Add spaces around punctuation, then split on whitespace
    for p in string.punctuation:
        text = text.replace(p, f" {p} ")
    
    # Clean up double spaces and split
    return text.split()

# Example
print(punctuation_tokenize("The cat, sat on the mat!"))
# Output: ['The', 'cat', ',', 'sat', 'on', 'the', 'mat', '!']
```
*This is much better for vocabulary size, but it destroys concepts like "U.S.A." or "$100.00" by ripping the punctuation out of them.*

## 3. Regex-Based Tokenization
To handle the edge cases of punctuation tokenization, we define complex Regular Expressions that define exactly what constitutes a valid token (e.g., words, numbers, money, URLs).

### Scratch Implementation
```python
import re

def regex_tokenize(text: str) -> list[str]:
    # Define a regex pattern for valid tokens:
    # 1. Words with optional internal apostrophes (e.g., don't, it's)
    # 2. Numbers with optional decimals
    # 3. Standalone punctuation
    pattern = r"[a-zA-Z]+'[a-zA-Z]+|[a-zA-Z]+|\d+\.\d+|\d+|[^\w\s]"
    
    return re.findall(pattern, text)

# Example
print(regex_tokenize("I can't believe it's $99.99!"))
# Output: ['I', "can't", 'believe', "it's", '$', '99.99', '!']
```

## 4. N-gram Tokenization
Sometimes, treating single words as tokens removes too much context. An **n-gram** is a contiguous sequence of *n* items from a given text.
- 1-gram (unigram): ["the", "cat", "sat"]
- 2-gram (bigram): ["the cat", "cat sat"]
- 3-gram (trigram): ["the cat sat"]

### Scratch Implementation
```python
def ngram_tokenize(tokens: list[str], n: int) -> list[str]:
    ngrams = []
    # Loop from 0 to length - n + 1
    for i in range(len(tokens) - n + 1):
        # Slice n elements and join them
        ngram = " ".join(tokens[i : i+n])
        ngrams.append(ngram)
    return ngrams

# Example
words = ["the", "quick", "brown", "fox"]
print(ngram_tokenize(words, n=2))
# Output: ['the quick', 'quick brown', 'brown fox']
```

## 5. Exam Preparation
### Must Be Able To Implement
You must be able to write the `ngram_tokenize` and `whitespace_tokenize` functions from scratch on an exam using only standard Python.

### Likely Practical Question
**Question**: Given the sentence "It's raining cats & dogs.", what is the output of a pure whitespace tokenizer vs a punctuation-splitting tokenizer?
**Answer**:
- **Whitespace**: `["It's", "raining", "cats", "&", "dogs."]`.
- **Punctuation**: `["It", "'", "s", "raining", "cats", "&", "dogs", "."]`.

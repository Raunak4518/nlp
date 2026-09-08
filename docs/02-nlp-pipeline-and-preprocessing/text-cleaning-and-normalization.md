# Text Cleaning and Normalization

## 1. What Is It?
Raw text is noisy. It contains HTML tags, inconsistent capitalization, emojis, URLs, and bizarre punctuation. Text cleaning is the process of removing unwanted noise, while normalization is the process of converting text into a standard, uniform format.

## 2. Text Cleaning
Before looking at words, we clean the characters.
- **HTML Stripping**: Removing `<p>`, `<a>`, etc., usually via libraries like BeautifulSoup.
- **URL/Email/Mention Removal**: Replacing these with generic placeholder tokens (e.g., `<URL>`, `<EMAIL>`, `<USER>`) using Regular Expressions.
- **Special Character Handling**: Removing non-ASCII characters if they are irrelevant to the task, or specifically retaining them (like emojis in sentiment analysis).

## 3. Normalization Techniques
Normalization reduces the dimensionality of the vocabulary by mapping different strings to the same underlying token.

### Lowercasing / Uppercasing
- "Apple", "APPLE", and "apple" are converted to "apple".
- *Warning*: This can destroy information. "Apple" (company) vs "apple" (fruit), or "US" (United States) vs "us" (pronoun).

### Whitespace Normalization
- Converting tabs `\t`, newlines `\n`, and multiple spaces `   ` into a single space ` `.

### Punctuation Normalization
- Removing punctuation completely: `Hello, world!` -> `Hello world`
- Or standardizing it: Converting different quotes (`'`, `‘`, `’`) into a single standard quote `'`.

### Unicode Normalization
Text can be visually identical but computationally different. 
- "é" can be represented as a single character (U+00E9) or as an "e" followed by an accent mark (U+0065 U+0301).
- Unicode normalization (like NFKC or NFC in Python) ensures these are identical bytes.

## 4. Scratch Implementation

```python
import re
import unicodedata

def clean_and_normalize(text: str) -> str:
    # 1. Unicode Normalization (NFC)
    text = unicodedata.normalize('NFC', text)
    
    # 2. Lowercase
    text = text.lower()
    
    # 3. Replace URLs and Emails
    text = re.sub(r'http\S+', '<URL>', text)
    text = re.sub(r'\S+@\S+', '<EMAIL>', text)
    
    # 4. Remove punctuation (excluding the < > for placeholders)
    text = re.sub(r'[^\w\s<>]', '', text)
    
    # 5. Whitespace normalization
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

# Manual Trace
sample = "Check out my new website https://example.com!! Email me at test@test.com.      It's GREAT."
print(clean_and_normalize(sample))
# Output: "check out my new website <URL> email me at <EMAIL> its great"
```

## 5. Exam Preparation
### Must Know
- The difference between cleaning (removing noise) and normalization (standardizing format).
- Why lowercasing can sometimes hurt model performance (e.g., in Named Entity Recognition).

### Likely Practical Question
**Question**: Write a regular expression to normalize all whitespace (including tabs and newlines) into a single space.
**Answer**: `re.sub(r'\s+', ' ', text)`

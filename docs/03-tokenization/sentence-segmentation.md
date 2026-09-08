# Sentence Segmentation

## 1. What Is It?
Sentence segmentation (also known as sentence boundary disambiguation) is the process of determining where one sentence ends and another begins within a continuous block of text.

## 2. Why is it difficult?
In English, sentences usually end with a period (`.`), exclamation mark (`!`), or question mark (`?`). However, the period is highly ambiguous. It is used for:
- End of sentence boundary markers.
- Abbreviations (Dr., Mr., Mrs., Inc.).
- Decimal points (3.14).
- Ellipses (...).
- Acronyms (U.S.A.).

## 3. Handling Abbreviations
The core challenge in sentence segmentation is distinguishing a period used in an abbreviation from a period used to terminate a sentence.

### Rule-based Approaches
Early NLP systems used hand-crafted lists of common abbreviations.
If the token before the period is in the list `["Dr", "Mr", "Mrs", "Prof", "Inc"]`, the period is NOT a sentence boundary.

*Edge Case*: "I saw the Dr. He was walking." Here, "Dr." ends the sentence because "He" is capitalized. Rule-based systems become incredibly complex when handling these edge cases.

### Statistical Approaches
Modern systems use statistical models or decision trees to classify whether a period is an End-Of-Sentence (EOS) marker based on features like:
- Is the word before the period capitalized?
- Is the word after the period capitalized?
- How long is the word before the period?
- Is the word before the period a known abbreviation?

## 4. Scratch Implementation (Rule-Based Sentence Segmenter)

```python
import re

def segment_sentences(text: str) -> list[str]:
    # List of common abbreviations that shouldn't break a sentence
    abbreviations = {"Dr", "Mr", "Mrs", "Ms", "Prof", "Inc", "Ltd", "Jr", "Sr"}
    
    # 1. Normalize spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    sentences = []
    current_sentence = []
    
    words = text.split(' ')
    for i, word in enumerate(words):
        current_sentence.append(word)
        
        # Check if word ends with punctuation
        if re.search(r'[.!?]$', word):
            # Check for abbreviations
            clean_word = re.sub(r'[.!?]', '', word)
            if clean_word in abbreviations:
                continue # It's an abbreviation, don't split
                
            # Otherwise, it's a boundary
            sentences.append(" ".join(current_sentence))
            current_sentence = []
            
    # Catch any remaining text
    if current_sentence:
        sentences.append(" ".join(current_sentence))
        
    return sentences

# Manual Trace
sample = "Hello Dr. Smith! How are you doing today? I bought a computer from Apple Inc. for $3.14."
for s in segment_sentences(sample):
    print(f"- {s}")
    
# Output:
# - Hello Dr. Smith!
# - How are you doing today?
# - I bought a computer from Apple Inc. for $3.14.
```

## 5. Exam Preparation
### Must Know
- Why the period (`.`) is the most ambiguous punctuation mark in English NLP.
- How to resolve the abbreviation vs. sentence-boundary conflict.

### Likely Practical Question
**Question**: Design a feature set for a machine learning model tasked with classifying whether a period is a sentence boundary.
**Answer**:
1. Length of the word preceding the period.
2. Case (capitalized/lowercase) of the word preceding the period.
3. Case of the word following the period.
4. Whether the preceding word is present in an abbreviation dictionary.
5. Distance to the next punctuation mark.

# Sentence Segmentation

## 1. What Is It?
Sentence segmentation (also known as sentence boundary disambiguation) is the process of determining where one sentence ends and another begins within a continuous block of text.

## 2. The Core Problem: Period Ambiguity
In English, sentences usually end with a period (`.`), exclamation mark (`!`), or question mark (`?`). Exclamation and question marks are usually unambiguous. The **period**, however, is highly ambiguous because it serves multiple linguistic and formatting functions simultaneously.

### The Multiple Roles of the Period
| Role | Example | Is it a boundary? |
| :--- | :--- | :--- |
| End of sentence | "The dog barked`.`" | YES |
| Abbreviation | "He saw `Dr.` Smith." | NO |
| Decimal Point | "Pi is `3.14`." | NO |
| Acronym | "The `U.S.A.` is large." | NO |
| Ellipses | "Wait `...` what?" | NO |

---

## 3. Resolving the Ambiguity

How does a machine know if a period is an End-Of-Sentence (EOS) marker or just an abbreviation?

### 1. Rule-based Approaches
Early NLP systems used hand-crafted lists of common abbreviations.
> **Rule**: If the token before the period is in the set `{Dr, Mr, Mrs, Prof, Inc, Ltd}`, the period is NOT a sentence boundary.

**The Edge Case Failure**:
Look at this string: `"I saw the Dr. He was walking."`
Under the simple rule above, the machine assumes "Dr." is not a boundary. But here, "Dr." *is* the end of the sentence. Rule-based systems become incredibly complex when handling these edge cases (e.g., checking if the next word is capitalized, but wait, proper nouns are also capitalized!).

### 2. Machine Learning Approaches
Modern systems use statistical models (like Decision Trees or Logistic Regression) to classify whether a period is an EOS marker based on surrounding contextual features.

**Common ML Features**:
- Is the word before the period capitalized?
- Is the word *after* the period capitalized?
- How many letters are in the word before the period? (Abbreviations are usually short).
- Is the word before the period found in a known dictionary of abbreviations?

---

## 4. Scratch Implementation: Rule-Based Segmenter

Here is a basic Python script that demonstrates how you might attempt to segment sentences using rules. Notice how brittle it is regarding decimals.

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
            # Strip the punctuation to check if it's an abbreviation
            clean_word = re.sub(r'[.!?]', '', word)
            if clean_word in abbreviations:
                continue # It's an abbreviation, keep appending to current sentence
                
            # Otherwise, we assume it's a boundary
            sentences.append(" ".join(current_sentence))
            current_sentence = []
            
    # Catch any remaining text
    if current_sentence:
        sentences.append(" ".join(current_sentence))
        
    return sentences
```

### Try It Yourself

??? question "Trace the code on this input"
    **Input:** `"Hello Dr. Smith! How are you doing today? I bought a computer from Apple Inc. for $3.14."`
    
    **Output:**
    ```python
    [
      "Hello Dr. Smith!",
      "How are you doing today?",
      "I bought a computer from Apple Inc. for $3.14."
    ]
    ```
    *Notice how the rule successfully skipped splitting after `Dr.` and `Inc.`, and how the regex successfully matched the `!` and `?` as boundaries.*

---

## 5. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: Design a feature set for a machine learning model tasked with classifying whether a period is a sentence boundary. Justify why each feature is necessary.
> **Answer**:
> 1. **Length of the word preceding the period**: Abbreviations (like Dr., Mr.) are typically very short (1-4 characters).
> 2. **Case of the word preceding the period**: Capitalization often hints at an acronym or title.
> 3. **Case of the word following the period**: In English, the first word of a new sentence is strictly capitalized. If the following word is lowercase, the period is almost certainly not a boundary.
> 4. **Presence in abbreviation dictionary**: A boolean feature checking if the preceding word exists in a predefined list of common abbreviations.
> 5. **Distance to the next punctuation mark**: Can help identify acronyms (like U.S.A.) where periods occur tightly clustered together.

---

### Can You Explain This?
- [ ] I can explain why sentence segmentation in English is non-trivial.
- [ ] I can list at least 3 distinct linguistic uses for the period character.
- [ ] I can explain why a simple rule-based abbreviation dictionary fails on edge cases.
- [ ] I can list 4 machine learning features used to classify a period as an EOS marker.

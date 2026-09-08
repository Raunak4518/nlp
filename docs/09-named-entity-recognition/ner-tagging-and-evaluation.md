# NER Tagging and Evaluation

## 1. BIO Tagging for NER
As covered in the Sequence Labeling module, NER entities frequently span multiple tokens (e.g., "New York City"). To train machine learning models to identify these spans, we use **BIO encoding** (Begin, Inside, Outside).

If our text is: "Tim Cook is the CEO of Apple Inc."
| Token | BIO Tag |
|---|---|
| Tim | `B-PER` |
| Cook | `I-PER` |
| is | `O` |
| the | `O` |
| CEO | `O` |
| of | `O` |
| Apple | `B-ORG` |
| Inc. | `I-ORG` |

## 2. Rule-Based NER
Before statistical models, NER was done using complex rule engines (like the famous GATE system).
A rule-based NER relies on:
1. **Gazetteers**: Massive dictionaries of known names, cities, and companies.
2. **Regex Patterns**: For finding predictable entities like Emails, Dates, and Money.
3. **Contextual Rules**: E.g., "If a capitalized word is preceded by 'Mr.', it is a PERSON."

*Drawback*: They cannot easily generalize to new, unseen entities. If a new company called "Zorplox" is founded tomorrow, a dictionary-based NER will miss it, but a statistical/deep-learning NER will recognize it as an ORG based on sentence context ("Zorplox announced its Q3 earnings").

## 3. NER Evaluation (Strict vs Partial)
Evaluating NER is much more complex than evaluating simple classification. We use Precision, Recall, and F1-Score, but we have to decide *what counts as a match*.

Assume the true entity in the text is `[United States of America]`.
Assume the model predicted `[United States]`.

### Strict Match (Exact Match)
The predicted span must match the true span's boundaries **exactly**, and the predicted category must match the true category exactly.
- In the example above, the model gets a **False Negative** (it missed the full entity) and a **False Positive** (it predicted an entity that doesn't exactly exist).
- *Score*: 0.

### Partial Match
Credit is given if the predicted span overlaps with the true span.
- In the example above, the model gets partial credit because "United States" overlaps with "United States of America".
- Much more forgiving, often used in exploratory research.

## 4. Scratch Implementation (BIO Extractor)
Converting a list of BIO tags back into distinct string entities.

```python
def extract_entities(tokens: list[str], bio_tags: list[str]) -> list[tuple[str, str]]:
    """Extracts entities from parallel lists of tokens and BIO tags."""
    entities = []
    current_entity_tokens = []
    current_entity_type = None

    for token, tag in zip(tokens, bio_tags):
        if tag.startswith('B-'):
            # If we were tracking an entity, save it
            if current_entity_tokens:
                entities.append((" ".join(current_entity_tokens), current_entity_type))
            
            # Start tracking a new entity
            current_entity_type = tag.split('-')[1]
            current_entity_tokens = [token]
            
        elif tag.startswith('I-'):
            # Continue tracking the current entity
            if current_entity_tokens and tag.split('-')[1] == current_entity_type:
                current_entity_tokens.append(token)
            else:
                # Malformed BIO sequence (I without B)
                pass 
                
        elif tag == 'O':
            # End of entity
            if current_entity_tokens:
                entities.append((" ".join(current_entity_tokens), current_entity_type))
                current_entity_tokens = []
                current_entity_type = None

    # Catch the last entity if the sequence ended on it
    if current_entity_tokens:
        entities.append((" ".join(current_entity_tokens), current_entity_type))

    return entities

# Trace
t = ["Barack", "Obama", "visited", "New", "York"]
tags = ["B-PER", "I-PER", "O", "B-LOC", "I-LOC"]
print(extract_entities(t, tags))
# Output: [('Barack Obama', 'PER'), ('New York', 'LOC')]
```

## 5. Exam Preparation
### Must Know
- In strict evaluation, getting the boundary wrong by even one word counts as a complete failure (False Positive + False Negative).

### Likely Practical Question
**Question**: Given the sentence "The Bank of England raised rates", and the tags `['O', 'B-ORG', 'O', 'B-LOC', 'O', 'O']`, explain why the BIO sequence is structurally valid but semantically incorrect.
**Answer**: It is structurally valid because every `B-` tag can legally follow an `O` tag. However, it is semantically incorrect because "Bank of England" is a single organization. The correct tagging should be `['O', 'B-ORG', 'I-ORG', 'I-ORG', 'O', 'O']`.

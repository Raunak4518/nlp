# NER Tagging and Evaluation

## 1. BIO Tagging for NER
As covered in the Sequence Labeling module, Named Entities almost always span multiple tokens (e.g., "New York City"). To train machine learning models to identify these boundaries properly without treating "New", "York", and "City" as three separate entities, we use **BIO encoding**.

If our text is: *"Tim Cook is the CEO of Apple Inc."*

| Token | BIO Tag | Explanation |
| :--- | :--- | :--- |
| Tim | `B-PER` | Start of a Person entity |
| Cook | `I-PER` | Continuation of a Person entity |
| is | `O` | Outside any entity |
| the | `O` | Outside any entity |
| CEO | `O` | Outside any entity (titles are not usually tagged) |
| of | `O` | Outside any entity |
| Apple | `B-ORG` | Start of an Organization entity |
| Inc. | `I-ORG` | Continuation of an Organization entity |

---

## 2. Rule-Based vs. Statistical NER

Before modern machine learning, NER was done using complex rule engines (like the famous GATE system).

### Rule-Based NER
A rule-based NER relies on three components:
1. **Gazetteers**: Massive dictionaries of known names, cities, and companies.
2. **Regex Patterns**: For finding highly predictable entities like Emails, Dates, and Money.
3. **Contextual Rules**: Hand-written logic (e.g., "If a capitalized word is preceded by 'Mr.', it is a PERSON.")

*Drawback*: They cannot generalize to new, unseen entities. If a brand new startup called "Zorplox" is founded tomorrow, a dictionary-based NER will miss it entirely. 

### Statistical/Deep-Learning NER
A statistical NER (like a BiLSTM or Transformer) learns to identify entities based on surrounding context. It will recognize "Zorplox" as an `ORG` because it occurs in the sentence *"Zorplox announced its Q3 earnings"*, a grammatical structure usually reserved for companies.

---

## 3. NER Evaluation (Strict vs Partial)
Evaluating NER is much more complex than evaluating simple classification. We still use Precision, Recall, and F1-Score, but we have to decide *what physically counts as a match*.

Assume the True Entity in the text is `[United States of America]`.
Assume the Model Predicted `[United States]`.

### Strict Match (Exact Match)
The predicted span must match the true span's boundaries **exactly**, and the predicted category must match the true category exactly.
- In the example above, the model gets a **False Negative** (it completely missed the true full entity) and a **False Positive** (it predicted an entity that doesn't exactly exist).
- *Score*: 0. This is the industry standard for production systems.

### Partial Match
Credit is given if the predicted span merely *overlaps* with the true span.
- In the example above, the model gets partial credit because "United States" overlaps with "United States of America".
- Much more forgiving; often used in exploratory research to see if the model is at least "close".

---

## 4. Scratch Implementation (BIO Extractor)
Converting a raw list of BIO tags back into distinct, readable string entities requires careful loop tracking.

```python
def extract_entities(tokens: list[str], bio_tags: list[str]) -> list[tuple[str, str]]:
    """Extracts entities from parallel lists of tokens and BIO tags."""
    entities = []
    current_entity_tokens = []
    current_entity_type = None

    for token, tag in zip(tokens, bio_tags):
        if tag.startswith('B-'):
            # If we were already tracking an entity, save it before starting the new one
            if current_entity_tokens:
                entities.append((" ".join(current_entity_tokens), current_entity_type))
            
            # Start tracking the new entity
            current_entity_type = tag.split('-')[1]
            current_entity_tokens = [token]
            
        elif tag.startswith('I-'):
            # Continue tracking the current entity
            if current_entity_tokens and tag.split('-')[1] == current_entity_type:
                current_entity_tokens.append(token)
            else:
                # Malformed BIO sequence (I without B). Ignore or handle error.
                pass 
                
        elif tag == 'O':
            # End of entity
            if current_entity_tokens:
                entities.append((" ".join(current_entity_tokens), current_entity_type))
                current_entity_tokens = []
                current_entity_type = None

    # Catch the very last entity if the sequence ended on it
    if current_entity_tokens:
        entities.append((" ".join(current_entity_tokens), current_entity_type))

    return entities
```

### Try It Yourself

??? question "Trace the code on this input"
    **Input:**
    ```python
    t = ["Barack", "Obama", "visited", "New", "York"]
    tags = ["B-PER", "I-PER", "O", "B-LOC", "I-LOC"]
    print(extract_entities(t, tags))
    ```
    
    **Output:** `[('Barack Obama', 'PER'), ('New York', 'LOC')]`

---

## 5. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: Given the sentence "The Bank of England raised rates", and the model prediction tags `['O', 'B-ORG', 'O', 'B-LOC', 'O', 'O']`, explain why the BIO sequence is structurally valid but semantically incorrect.
> **Answer**: It is *structurally valid* because every `B-` tag can legally follow an `O` tag (it does not violate the rules of BIO formatting). However, it is *semantically incorrect* because "Bank of England" is a single unified organization. The model incorrectly split it into an Organization and a Location. The correct tagging should be `['O', 'B-ORG', 'I-ORG', 'I-ORG', 'O', 'O']`.

**3-Mark Question**: Define Strict Evaluation in the context of Named Entity Recognition.
> **Answer**: In Strict Evaluation, a prediction is only counted as a True Positive if both the physical boundaries of the entity span AND the predicted entity class match the ground truth exactly. An overlap of 3 out of 4 words is considered both a False Positive and a False Negative.

---

### Can You Explain This?
- [ ] I can write out the BIO tags for the sentence "Steve Jobs founded Apple".
- [ ] I can define what a Gazetteer is.
- [ ] I can explain why an "almost perfect" prediction in Strict Evaluation results in a score of 0.

# Sequence Labeling

## 1. Sequence Classification vs Sequence Labeling
It is critical to distinguish between these two fundamental NLP tasks.

### Sequence Classification
- **Input**: A sequence of tokens $[x_1, x_2, ..., x_n]$.
- **Output**: A **single** class label $y$.
- **Example**: Sentiment Analysis. "The movie was terrible" $\rightarrow$ `NEGATIVE`.

### Sequence Labeling (Sequence Tagging)
- **Input**: A sequence of tokens $[x_1, x_2, ..., x_n]$.
- **Output**: A sequence of labels $[y_1, y_2, ..., y_n]$, where the length of the input equals the length of the output.
- **Example**: POS Tagging. ["The", "movie", "was", "terrible"] $\rightarrow$ `[DET, NOUN, VERB, ADJ]`.

## 2. The Problem with Multi-Token Entities
Sequence labeling works perfectly for POS tagging because every single token gets exactly one tag. But what happens in Named Entity Recognition (NER) when an entity spans multiple tokens?

- Text: "Barack Obama visited New York."
- Tags: "Barack" = PERSON, "Obama" = PERSON, "New" = LOCATION, "York" = LOCATION.

How does the machine know if "New York" is one location or two separate locations next to each other? We solve this using specialized encoding schemes.

## 3. BIO Encoding (IOB Encoding)
BIO stands for **Begin, Inside, Outside**. It is the most common tagging scheme for multi-token entities.

- **B-**: Marks the **Beginning** of an entity.
- **I-**: Marks the **Inside** of an entity (any token after the first one).
- **O**: Marks a token that is **Outside** any entity.

### Example
| Token | BIO Tag |
|---|---|
| Barack | `B-PER` |
| Obama | `I-PER` |
| visited | `O` |
| New | `B-LOC` |
| York | `I-LOC` |
| and | `O` |
| Washington | `B-LOC` |

Notice that "New York" is clearly one entity (`B-LOC`, `I-LOC`), while "Washington" is a separate entity that happens to be nearby (`B-LOC`).

## 4. BILOU Encoding
A more fine-grained extension of BIO encoding that provides the model with more specific boundary information.

- **B-**: **Beginning** of a multi-token entity.
- **I-**: **Inside** of a multi-token entity.
- **L-**: **Last** token of a multi-token entity.
- **O**: **Outside** any entity.
- **U-**: **Unit** token (an entity consisting of exactly one token).

### Example
| Token | BILOU Tag |
|---|---|
| Barack | `B-PER` |
| Obama | `L-PER` |
| visited | `O` |
| New | `B-LOC` |
| York | `L-LOC` |
| and | `O` |
| Washington | `U-LOC` |

While BILOU gives the machine learning model stronger signals about where entities end, it significantly increases the total number of labels the model has to predict.

## 5. Exam Preparation
### Must Be Able To Calculate
Given a sentence and a list of entities, correctly tag every word using both the BIO and BILOU schemes.

### Common Mistake
> [!CAUTION]
> In BIO encoding, a tag of `I-LOC` can **only** follow a `B-LOC` or another `I-LOC`. It is grammatically invalid in BIO encoding to have an `I-LOC` immediately following an `O` or a `B-PER`.

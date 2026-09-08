# Sequence Labeling

## 1. Sequence Classification vs Sequence Labeling
It is critical to distinguish between these two fundamental NLP architectures.

### Sequence Classification
- **Input**: A sequence of tokens $[x_1, x_2, ..., x_n]$.
- **Output**: A **single** class label $y$ that applies to the entire sequence.
- **Example**: Sentiment Analysis. `["The", "movie", "was", "terrible"]` $\rightarrow$ `NEGATIVE`.

### Sequence Labeling (Sequence Tagging)
- **Input**: A sequence of tokens $[x_1, x_2, ..., x_n]$.
- **Output**: A sequence of labels $[y_1, y_2, ..., y_n]$, where the length of the input exactly equals the length of the output.
- **Example**: POS Tagging. `["The", "movie", "was", "terrible"]` $\rightarrow$ `[DET, NOUN, VERB, ADJ]`.

---

## 2. The Multi-Token Entity Problem
Sequence labeling works perfectly for POS tagging because every single token inherently gets exactly one linguistic tag. 

But what happens in Named Entity Recognition (NER) when a single logical entity spans multiple physical tokens?
- **Text**: `"Barack Obama visited New York."`
- **Naive Tags**: `"Barack" = PERSON, "Obama" = PERSON, "visited" = O, "New" = LOCATION, "York" = LOCATION.`

**The Problem**: How does the machine parsing these tags know if "New York" is one single city, or two separate locations situated next to each other? We solve this using specialized structural encoding schemes.

---

## 3. BIO Encoding (IOB Encoding)
BIO stands for **Begin, Inside, Outside**. It is the absolute industry standard tagging scheme for multi-token entities.

- **B-**: Marks the **Beginning** token of an entity.
- **I-**: Marks the **Inside** of an entity (any token belonging to the entity after the first one).
- **O**: Marks a token that is **Outside** any entity.

### Example
| Token | BIO Tag | Explanation |
| :--- | :--- | :--- |
| Barack | `B-PER` | Starts a Person entity. |
| Obama | `I-PER` | Continues the Person entity. |
| visited | `O` | Not an entity. |
| New | `B-LOC` | Starts a Location entity. |
| York | `I-LOC` | Continues the Location entity. |
| and | `O` | Not an entity. |
| Washington | `B-LOC` | Starts a *new* separate Location entity. |

Notice that "New York" is clearly identified as one entity (`B-LOC`, `I-LOC`), while "Washington" is correctly identified as a separate entity that happens to be nearby (`B-LOC`).

> [!CAUTION]
> **The Golden Rule of BIO**
> In BIO encoding, an `I-X` tag can **only** legally follow a `B-X` or another `I-X`. It is structurally invalid to have an `I-LOC` immediately following an `O` or a `B-PER`.

---

## 4. BILOU Encoding
BILOU is a more fine-grained extension of BIO encoding. It provides the machine learning model with stronger, more specific boundary information, which can improve accuracy at the cost of expanding the tag vocabulary.

- **B-**: **Beginning** of a multi-token entity.
- **I-**: **Inside** of a multi-token entity.
- **L-**: **Last** token of a multi-token entity.
- **O**: **Outside** any entity.
- **U-**: **Unit** token (an entity consisting of exactly one single token).

### Example
| Token | BILOU Tag |
| :--- | :--- |
| Barack | `B-PER` |
| Obama | `L-PER` |
| visited | `O` |
| New | `B-LOC` |
| York | `L-LOC` |
| and | `O` |
| Washington | `U-LOC` |

---

## 5. Exam Preparation

### How to Write This in an Exam

**10-Mark Question**: Given the sentence `"Tim Cook is the CEO of Apple Inc in Cupertino"`, define the entities `Tim Cook` (PERSON), `Apple Inc` (ORG), and `Cupertino` (LOC). Write out the token-by-token tagging for this sentence using both the BIO and BILOU encoding schemes.
> **Answer**:
> | Token | BIO Tag | BILOU Tag |
> | :--- | :--- | :--- |
> | Tim | B-PER | B-PER |
> | Cook | I-PER | L-PER |
> | is | O | O |
> | the | O | O |
> | CEO | O | O |
> | of | O | O |
> | Apple | B-ORG | B-ORG |
> | Inc | I-ORG | L-ORG |
> | in | O | O |
> | Cupertino | B-LOC | U-LOC |

---

### Can You Explain This?
- [ ] I can explain the difference between Sequence Classification and Sequence Labeling.
- [ ] I can explain why simple sequence labeling fails for Named Entities without an encoding scheme.
- [ ] I can write out what the acronyms BIO and BILOU stand for.
- [ ] I know the Golden Rule regarding where an `I-` tag is legally allowed to appear.

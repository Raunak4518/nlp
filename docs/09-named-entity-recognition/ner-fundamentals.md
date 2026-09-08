# Named Entity Recognition Fundamentals

## 1. What is NER?
Named Entity Recognition (NER) is a core subtask of Information Extraction. It seeks to locate and classify "named entities" mentioned in unstructured text into pre-defined categories.

While Part-of-Speech tagging identifies the *grammatical role* of a word (e.g., "Apple" is a Noun), NER identifies the *semantic real-world category* of the word (e.g., "Apple" is an Organization).

---

## 2. Standard Entity Categories
The exact set of categories depends entirely on the dataset the model was trained on. 

### The CoNLL-2003 Standard
The most famous NER dataset is CoNLL-2003, which defines four core tags:
- **PER (Person)**: "Barack Obama", "Harry Potter"
- **LOC (Location)**: "New York", "Mount Everest"
- **ORG (Organization)**: "Google", "United Nations"
- **MISC (Miscellaneous)**: Entities that don't fit the above (e.g., Nationalities like "French", Events like "World War II")

### The OntoNotes 5 Standard
Modern systems often use the OntoNotes 5 tagset, which is much richer (18 categories). It splits CoNLL's LOC tag into `LOC` (physical locations) and `GPE` (Geo-Political Entities).

| OntoNotes Tag | Definition | Examples |
| :--- | :--- | :--- |
| **PERSON** | People, including fictional. | "Mr. Smith", "Batman" |
| **GPE** | Countries, cities, states. | "France", "New York" |
| **LOC** | Physical locations (mountains, rivers). | "the Alps", "the Nile" |
| **ORG** | Companies, agencies, institutions. | "Manchester United" |
| **DATE / TIME** | Temporal expressions. | "January 1st", "last Tuesday" |
| **MONEY** | Monetary values. | "$100", "50 euros" |
| **PRODUCT** | Objects, vehicles, foods. | "iPhone", "Honda Civic" |
| **EVENT** | Wars, sports events, hurricanes. | "Hurricane Katrina" |

---

## 3. The Challenge of Ambiguity
Just like POS tagging, NER faces massive ambiguity. Consider the string **"Washington"**:

| Context | Semantic Meaning | Correct NER Tag |
| :--- | :--- | :--- |
| "George **Washington** was president." | The man | `PERSON` |
| "I drove to **Washington**." | The state/city | `GPE` |
| "**Washington** passed the new tax law." | The U.S. Government | `ORG` |
| "I read it in the **Washington** Post." | The company | `ORG` |

Resolving this requires the model to analyze the surrounding context (the sequence), which is why NER is treated as a Sequence Labeling task exactly like POS tagging.

---

## 4. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: How does Named Entity Recognition (NER) fundamentally differ from Part-of-Speech (POS) tagging? Compare their outputs on the sentence: `"Tim Cook loves Apple."`
> **Answer**: 
> POS tagging assigns a grammatical syntactic category (Noun, Verb, Adjective) to *every single word* in a sentence. 
> NER assigns semantic real-world categories (Person, Organization, Location) *only to specific substrings* that represent named entities, leaving the rest of the text untagged (or tagged as 'O' for outside).
> 
> **POS Output**: `Tim (PROPN), Cook (PROPN), loves (VERB), Apple (PROPN), . (PUNCT)`
> **NER Output**: `[Tim Cook] (PERSON) loves [Apple] (ORGANIZATION).`

**2-Mark Question**: In the OntoNotes 5 dataset, what is the difference between a `LOC` and a `GPE`? Give an example of each.
> **Answer**: A `GPE` (Geo-Political Entity) refers to locations with human-defined borders and governments, such as countries or cities (e.g., "Germany", "Chicago"). A `LOC` refers to physical, natural geographical features (e.g., "the Sahara Desert", "the Pacific Ocean").

---

### Can You Explain This?
- [ ] I can list the four tags used in the CoNLL-2003 dataset.
- [ ] I can define what GPE stands for and how it differs from LOC.
- [ ] I can explain why "Washington" is an ambiguous entity.

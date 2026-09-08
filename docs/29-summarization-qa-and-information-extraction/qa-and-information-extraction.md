# QA and Information Extraction

## 1. Question Answering (QA)
Question Answering is the task of automatically answering a user's question posed in natural language. There are two primary paradigms:

### Retrieval-Based QA (Extractive QA)
In this paradigm, the system does not generate new text. 
1. The user asks a question: "When was the Eiffel Tower built?"
2. The system searches a database (e.g., Wikipedia) and retrieves the most relevant article ("Eiffel Tower").
3. A machine learning model reads the article and **extracts** the specific span of text that contains the answer (e.g., "1889").

*Models used*: BERT (Bidirectional Encoder Representations from Transformers) is the classic model for this, trained specifically to output the start and end index of the answer span within the document.

### Generative QA
In this paradigm, the system uses an Autoregressive Language Model to freely generate an answer.
- *Open-Book (RAG)*: The model retrieves an article from a database, reads it, and generates a conversational summary answer. (Retrieval-Augmented Generation).
- *Closed-Book*: The model relies purely on its internal, pre-trained neural network weights to remember the answer, without looking up any external documents (e.g., standard ChatGPT).

## 2. Information Extraction (IE)
Information Extraction is the task of reading unstructured text (like news articles or medical reports) and automatically populating a structured database (like a SQL table).

### Entity Linking
In Module 9, we discussed Named Entity Recognition (NER), which identifies that "Washington" is an Organization or a Location. 
**Entity Linking** (or Named Entity Disambiguation) goes one step further: it links the word "Washington" in the text to a specific unique ID in a database (e.g., mapping it to the Wikipedia page for `George_Washington` rather than `Washington_(state)`).

### Relation Extraction
Once entities are identified, **Relation Extraction** determines how they are connected.
- *Text*: "Elon Musk is the CEO of Tesla."
- *Extracted Entities*: `[Elon Musk]` (Person), `[Tesla]` (Organization).
- *Extracted Relation*: `(Elon Musk, CEO_OF, Tesla)`.

These extracted relations are used to build vast **Knowledge Graphs**, which power the "info boxes" you see on the right side of Google Search results.

## 3. Exam Preparation
### Must Memorize
- Retrieval-based QA extracts a span of text from an existing document.
- Relation Extraction turns unstructured text into structured triples: `(Subject, Predicate, Object)`.

### Likely Theory Question
**Question**: How does Entity Linking differ from standard Named Entity Recognition (NER)?
**Answer**: NER only identifies the boundary and category of an entity (e.g., identifying "Apple" as an Organization). It does not know *which* specific organization it is. Entity Linking takes the NER output and disambiguates it by mapping it to a unique, specific entry in a knowledge base (e.g., distinguishing between Apple Inc. the tech company and Apple the fruit, and linking to the correct database ID).

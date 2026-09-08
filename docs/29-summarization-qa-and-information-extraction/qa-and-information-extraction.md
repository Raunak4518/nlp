# QA and Information Extraction

## 1. Question Answering (QA)
Question Answering is the massive commercial NLP task of automatically answering a user's question posed in natural human language. There are two primary architectural paradigms:

### Retrieval-Based QA (Extractive QA)
In this highly reliable paradigm, the system **never** mathematically generates new text. 
1. The user asks a question: *"When was the Eiffel Tower built?"*
2. The system searches a massive database (e.g., Wikipedia) using Information Retrieval (TF-IDF or Dense Embeddings) and retrieves the most highly relevant article ("Eiffel Tower").
3. A machine learning model reads the physical article and physically **extracts** the specific string span of text that contains the answer (e.g., "1889") and displays it to the user.

*Models used*: **BERT** (Bidirectional Encoder Representations from Transformers) is the classic industry-standard model for this. It is trained specifically to mathematically output the integer start index and end index of the answer span within the physical document.

### Generative QA
In this paradigm, the system uses an Autoregressive Language Model (like GPT-4) to dynamically generate an entirely new answer.
- **Open-Book (RAG)**: Retrieval-Augmented Generation. The model retrieves a factual article from a database, reads it, and generates a conversational summary answer based *strictly* on that retrieved text. This highly limits hallucinations.
- **Closed-Book**: The model relies purely on its internal, pre-trained neural network weights to mathematically "remember" the answer, without looking up any external documents. (This is how standard ChatGPT works, and why it frequently hallucinates false facts).

---

## 2. Information Extraction (IE)
Information Extraction is the incredibly lucrative enterprise task of reading vast amounts of unstructured text (like millions of financial news articles or medical research reports) and automatically populating a structured relational database (like a SQL table) with the facts.

### Entity Linking
In Module 9, we discussed classical Named Entity Recognition (NER), which simply identifies that the string "Washington" is an Organization or a Location. 

**Entity Linking** (or Named Entity Disambiguation) goes one massive step further: it mathematically links the word "Washington" in the text to a specific, unique database ID (e.g., actively mapping it to the Wikipedia Knowledge Base page for `George_Washington` rather than `Washington_(state)`).

### Relation Extraction
Once entities are identified and linked, **Relation Extraction** determines exactly how they are connected.
- **Text**: *"Elon Musk is the CEO of Tesla."*
- **Extracted Entities**: `[Elon Musk]` (Person), `[Tesla]` (Organization).
- **Extracted Relation Triple**: `(Elon Musk, CEO_OF, Tesla)`.

These extracted relational triples are used to build vast, interconnected **Knowledge Graphs**, which natively power the factual "info boxes" you see on the right side of Google Search results.

---

## 3. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: How does Entity Linking fundamentally differ from standard Named Entity Recognition (NER), and why is it necessary for building a Knowledge Graph?
> **Answer**: NER only identifies the boundary and broad category of an entity in text (e.g., identifying "Apple" as an Organization). It does not computationally know *which* specific organization it is. 
> 
> Entity Linking takes the raw NER output and disambiguates it by mapping it to a unique, specific mathematical entry in a structured database (e.g., distinguishing between Apple Inc. the tech company and Apple the fruit, and linking to the correct database ID). This is absolutely necessary for building a Knowledge Graph, because a graph requires unique, distinct nodes to attach relational edges to; without Entity Linking, facts about Apple the company and Apple the fruit would be incorrectly merged into the same node.

**2-Mark Question**: Define the structural difference between Extractive QA and Generative QA.
> **Answer**: Extractive QA systems never generate new text; they mathematically identify and output the specific start and end indices of a text span within an existing, retrieved document that answers the question. Generative QA systems use autoregressive language models to generate an entirely new, conversational text response from scratch.

---

### Can You Explain This?
- [ ] I can explicitly describe the 3 steps of Extractive QA.
- [ ] I can explicitly define what RAG (Retrieval-Augmented Generation) is.
- [ ] I can explicitly state the 3 components of a Relation Extraction triple (Subject, Predicate, Object).

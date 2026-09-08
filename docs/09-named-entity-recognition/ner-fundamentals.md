# Named Entity Recognition Fundamentals

## 1. What is NER?
Named Entity Recognition (NER) is a subtask of information extraction that seeks to locate and classify named entities mentioned in unstructured text into pre-defined categories.

While POS tagging identifies the grammatical role of a word (e.g., "Apple" is a Noun), NER identifies the semantic real-world category of the word (e.g., "Apple" is an Organization).

## 2. Standard Entity Categories
The exact set of categories depends on the dataset being used (e.g., CoNLL-2003, OntoNotes 5). However, almost all standard NER systems recognize the following core entities:

### PERSON (PER)
- People, including fictional characters.
- *Examples*: "Barack Obama", "Harry Potter", "Mr. Smith".

### LOCATION (LOC) / GPE (Geo-Political Entity)
- Some datasets distinguish between physical locations (mountains, rivers) and geopolitical entities (countries, cities, states).
- *Examples*: "Mount Everest" (LOC), "New York" (GPE), "France" (GPE).

### ORGANIZATION (ORG)
- Companies, agencies, institutions, sports teams.
- *Examples*: "Google", "United Nations", "Manchester United".

### DATE and TIME
- Absolute or relative temporal expressions.
- *Examples*: "January 1st", "last Tuesday", "the 1990s".

### MONEY
- Monetary values, including the currency symbol or word.
- *Examples*: "$100", "50 euros", "a million dollars".

### PRODUCT
- Objects, vehicles, foods, etc. (Not services).
- *Examples*: "iPhone", "Honda Civic".

### EVENT
- Named hurricanes, battles, wars, sports events.
- *Examples*: "World War II", "Hurricane Katrina", "the Olympics".

## 3. The Challenge of Ambiguity
Just like POS tagging, NER faces massive ambiguity.
- "Washington" could be:
  - **PERSON**: George Washington.
  - **LOC/GPE**: Washington State, or Washington D.C.
  - **ORG**: The Washington Post (sometimes metonymically referred to as just "Washington").

Resolving this requires surrounding context. "Washington threw the ball" implies PERSON. "Washington passed the new law" implies ORG (the government). "I drove to Washington" implies LOC.

## 4. Exam Preparation
### Must Memorize
- The standard CoNLL-2003 entity types: PER, LOC, ORG, MISC.

### Likely Theory Question
**Question**: How does NER differ from POS tagging?
**Answer**: POS tagging assigns grammatical syntactic categories (Noun, Verb, Adjective) to every single word in a sentence. NER assigns semantic real-world categories (Person, Organization, Location) only to specific substrings of the text that represent named entities, leaving the rest of the text untagged (or tagged as 'O').

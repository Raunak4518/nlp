# Entity Linking

## 1. The Limitation of NER
Named Entity Recognition is only the first step in understanding text. NER tells the computer: *"The span 'Washington' is a Person."*

But *which* Washington? George Washington? Denzel Washington? The computer doesn't know. To the computer, 'Washington' is just a string of characters tagged with `PER`.

## 2. What is Entity Linking?
Entity Linking (also known as Named Entity Disambiguation or NED) is the task of mapping an entity mention in text to a specific unique identifier in a Knowledge Base (like Wikipedia, Wikidata, or a corporate database).

- **Input**: "Washington crossed the Delaware." (with "Washington" identified as a `PER` entity).
- **Knowledge Base Lookup**: The system searches Wikipedia for "Washington (Person)".
- **Disambiguation**: The system evaluates context. "Delaware" strongly correlates with "George Washington".
- **Output**: The system links the string "Washington" to the unique URI: `https://en.wikipedia.org/wiki/George_Washington`.

## 3. Why it matters
Entity linking turns raw text into a graph of connected knowledge. 
If an NLP pipeline processes thousands of news articles, Entity Linking allows the system to realize that mentions of "The President", "Barack Obama", and "Obama" all refer to the exact same underlying Knowledge Graph node, allowing for deep data mining and question answering.

## 4. Exam Preparation
### Must Know
- NER identifies *what type* of thing a word is. Entity Linking identifies *exactly which specific thing* in the real world it is.

### Likely Theory Question
**Question**: An NLP system reads "Apple announced a new phone." The NER module tags "Apple" as an ORG. What is the role of the Entity Linking module in the next step?
**Answer**: The Entity Linking module will take the mention "Apple" (ORG) and map it to a specific, unique record in a database (e.g., the Wikidata Q-identifier `Q312` for Apple Inc.), distinguishing it from Apple Records (the Beatles' record label) or Apple Bank.

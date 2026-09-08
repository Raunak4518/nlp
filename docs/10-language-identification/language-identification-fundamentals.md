# Language Identification

## 1. What is Language Identification?
Language Identification (LangID) is the NLP task of determining the natural language (e.g., English, French, Mandarin, Swahili) that a given document is written in. 

It is often the "Step 0" in an NLP pipeline. If you have a French POS-tagger and you feed it an English sentence, it will produce garbage. You must classify the language first to route the text to the correct language-specific models.

## 2. Why it is conceptually easy
Unlike tasks like translation or sentiment analysis, LangID is considered a solved problem for long texts. 
- You do not need to understand grammar.
- You do not need to understand semantics.
- You only need to look at the statistical distribution of characters.

## 3. Unknown Language Handling
No LangID model supports all 7,000+ human languages. Models are typically trained on 50 to 100 high-resource languages. 
When a model encounters a language it wasn't trained on (e.g., an obscure indigenous dialect), it will confidently (but incorrectly) classify it as the language in its training set that it shares the most character distributions with.

To handle this, systems must implement a **confidence threshold**.
- If the model predicts `English` with a confidence of $99\%$, accept it.
- If the model predicts `Spanish` with a confidence of $14\%$, reject it and classify the text as `UNKNOWN`.

## 4. Short Text Difficulties
While LangID is easy for paragraphs, it is extremely difficult for short text (like a 3-word tweet).
- "C'est la vie" (French)
- "I like pizza" (English)
- "No" (Valid in English, Spanish, Italian, and many others).

For very short texts, character statistics fail, and systems often fall back to metadata (e.g., the user's location, default browser language) or dictionary lookups.

## 5. Exam Preparation
### Must Know
- LangID is a prerequisite routing step for multilingual NLP pipelines.
- It relies on statistical character distributions, not grammatical parsing.

### Likely Theory Question
**Question**: Why do LangID systems struggle to classify a 2-word sentence, and how do they fail?
**Answer**: Two words do not provide a large enough statistical sample of characters to match a language profile accurately. A sentence like "No parking" might share n-grams with multiple European languages. If the system lacks an `UNKNOWN` threshold, it will arbitrarily force the text into one of its known language categories based on minor statistical noise.

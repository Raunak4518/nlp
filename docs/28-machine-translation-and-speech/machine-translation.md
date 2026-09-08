# Machine Translation

## 1. What is Machine Translation?
Machine Translation (MT) is the task of automatically translating text from one language (the **Source Language**) into another language (the **Target Language**). 

## 2. The Evolution of MT

### Rule-Based Machine Translation (RBMT)
In the 1970s and 1980s, linguists tried to build translation systems by manually writing thousands of grammatical rules and mapping dictionaries. 
- *How it worked*: "If the sentence is English, identify the Subject, Verb, and Object. Map the English words to Russian words using a dictionary. Apply Russian grammatical rules to rearrange the SVO order into Russian order."
- *Why it failed*: Human language is too complex and full of exceptions. The rules became impossibly tangled, and the translations sounded incredibly robotic.

### Statistical Machine Translation (SMT)
In the 1990s and 2000s, companies like IBM and Google abandoned linguistics and turned to pure statistics. SMT relies on massive parallel corpora (e.g., millions of documents translated by the United Nations into both English and French).
- *How it worked*: The system uses a **Translation Model** to learn the probability that the English word "house" aligns with the French word "maison". It then uses a **Language Model** (like Interpolated Kneser-Ney) on the target language to ensure the output French sentence is fluent and grammatically probable.
- *Why it was replaced*: It handled grammar poorly for languages with radically different word orders (like English to Japanese) because it translated in small chunks (phrases) rather than looking at the holistic meaning of the entire sentence.

### Neural Machine Translation (NMT)
Starting around 2014, Deep Learning took over. NMT models treat translation as a **Sequence-to-Sequence (Seq2Seq)** problem.
- *How it works*: An **Encoder** neural network reads the entire source sentence and compresses its meaning into a dense mathematical vector. A **Decoder** neural network takes that vector and autoregressively generates the target sentence one word at a time, usually using **Beam Search** to find the most probable sequence.
- *Why it won*: NMT models (especially Transformers) capture long-range dependencies perfectly, translating highly idiomatic language flawlessly.

## 3. Exam Preparation
### Must Memorize
- SMT relies on the Noisy Channel Model: $P(\text{Target}|\text{Source}) \propto P(\text{Source}|\text{Target}) \times P(\text{Target})$. The Translation Model handles $P(S|T)$, and the Language Model handles $P(T)$.
- NMT uses a Sequence-to-Sequence (Encoder-Decoder) architecture.

### Likely Theory Question
**Question**: Explain why Statistical Machine Translation struggles with language pairs that have different structural typologies (e.g., SVO vs SOV).
**Answer**: SMT translates text by aligning and translating small "phrases" (chunks of 2-3 words). If the source language is Subject-Verb-Object (English) and the target language is Subject-Object-Verb (Japanese), the verb in the target language must be placed at the very end of the sentence. Because SMT only looks at local phrase alignments, it struggles to move a translated verb across a gap of 10 or 15 words, resulting in poor grammatical structure. Neural Seq2Seq models solve this by encoding the entire sentence meaning into a single vector before beginning to generate the output.

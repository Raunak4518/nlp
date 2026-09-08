# Machine Translation

## 1. What is Machine Translation?
Machine Translation (MT) is the computationally massive NLP task of automatically translating text from one language (the **Source Language**) into another language (the **Target Language**). It is considered an "AI-Complete" problem, meaning that perfectly solving Machine Translation practically requires solving Artificial General Intelligence, as it demands deep contextual knowledge of the world, culture, and human intent.

---

## 2. The Evolution of MT

### Era 1: Rule-Based Machine Translation (RBMT)
In the 1970s and 1980s, computer scientists and linguists attempted to build translation systems by manually hardcoding thousands of explicit grammatical rules and mapping massive dictionaries.
- **How it worked**: *"If the sentence is English, parse the Syntax Tree to identify the Subject, Verb, and Object. Map the English words to Russian words using a bilingual dictionary. Apply Russian grammatical rules to algorithmically rearrange the English SVO order into Russian order."*
- **Why it failed**: Human language is infinitely complex and filled with millions of cultural idioms and exceptions. The hardcoded rulebases became impossibly tangled, and the literal translations sounded incredibly robotic and broken.

### Era 2: Statistical Machine Translation (SMT)
In the 1990s and 2000s, companies like IBM and Google explicitly abandoned linguistics and turned to pure mathematical statistics. SMT relies on massive **parallel corpora** (e.g., millions of legal documents professionally translated by the United Nations into both English and French).
- **How it worked**: The system statistically learns from the data. It mathematically uses a **Translation Model** to learn the raw probability that the English word "house" aligns with the French word "maison". It simultaneously uses a **Language Model** (like Interpolated Kneser-Ney) on the target language to strictly ensure the output French sentence is fluent and mathematically probable.
- **Why it was replaced**: It handled grammar very poorly for languages with radically different structural word orders (like English to Japanese). Because it translated in small, isolated chunks ("phrases") rather than looking at the holistic semantic meaning of the entire sentence, it failed to gracefully reorder words across long distances.

### Era 3: Neural Machine Translation (NMT)
Starting around 2014, Deep Learning completely took over the industry. NMT models definitively treat translation as a mathematical **Sequence-to-Sequence (Seq2Seq)** problem.
- **How it works**: An **Encoder** neural network reads the entire source sentence and compresses its deep semantic meaning into a dense mathematical vector. A **Decoder** neural network takes that vector and autoregressively generates the target sentence one word at a time, universally using **Beam Search** to find the most mathematically probable sequence.
- **Why it won**: Modern NMT models (specifically Transformers) capture long-range linguistic dependencies perfectly. They translate highly idiomatic language, sarcasm, and complex grammar flawlessly because they process the entire sentence holistically.

---

## 3. Exam Preparation

### How to Write This in an Exam

**5-Mark Question**: Explicitly explain the mathematical Noisy Channel Model formulation used in Classical Statistical Machine Translation. Identify the two distinct probabilistic models used and explain their specific roles in generating a fluent translation.
> **Answer**: 
> SMT fundamentally relies on Bayes' Theorem via the Noisy Channel Model: $P(\text{Target} \mid \text{Source}) \propto P(\text{Source} \mid \text{Target}) \times P(\text{Target})$.
> 
> 1. **$P(\text{Source} \mid \text{Target})$ is the Translation Model**: This model calculates the statistical probability that the words in the target language mathematically align to the words in the source language, ensuring the translation maintains factual fidelity and vocabulary correctness.
> 2. **$P(\text{Target})$ is the Language Model**: This is an N-gram model trained exclusively on the target language. Its explicit role is to evaluate the grammatical fluency of the generated text, ensuring the output sounds like a native speaker wrote it, regardless of the translation fidelity.

**2-Mark Question**: Explain the structural reason why Statistical Machine Translation struggles with language pairs that have different typologies (e.g., English SVO vs Japanese SOV), and how Neural Seq2Seq models solve this.
> **Answer**: SMT translates text by statistically aligning and translating small "phrases" (chunks of 2-3 words). If translating English (SVO) to Japanese (SOV), the English verb must be physically moved to the very end of the Japanese sentence. Because SMT only looks at local phrase alignments, it struggles to mathematically move a translated verb across a gap of 10 or 15 words. Neural Seq2Seq models perfectly solve this because the Encoder network compresses the entire holistic meaning of the sentence into a single vector before the Decoder begins generating the output, completely decoupling the generation from local alignment chunks.

---

### Can You Explain This?
- [ ] I can explicitly state why Rule-Based MT failed.
- [ ] I can define what a "Parallel Corpus" is and why SMT requires it.
- [ ] I can describe the structural components of an Encoder-Decoder (Seq2Seq) architecture.

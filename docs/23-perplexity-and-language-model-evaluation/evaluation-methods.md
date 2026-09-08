# Intrinsic vs Extrinsic Evaluation

## 1. Intrinsic Evaluation
Intrinsic Evaluation measures the quality of an NLP model *in isolation*, independent of any specific downstream task. It evaluates the model based entirely on its mathematical properties.

**Perplexity** is the primary metric for the intrinsic evaluation of a Language Model.
- *Process*: Train the model on Dataset A. Test the model's perplexity on Dataset B. Compare it to another model.
- *Pros*: Very fast. Requires no user studies or complex software engineering.
- *Cons*: Lower perplexity does not guarantee that the model will actually be useful for a real-world task. For example, a model might achieve lower perplexity by simply memorizing common sentence structures, but fail completely at understanding the meaning of a sentence.

## 2. Extrinsic Evaluation
Extrinsic Evaluation (or In Vivo evaluation) measures the quality of an NLP model by embedding it into a larger, real-world downstream application and observing how much the application improves.

- *Process*: Take Model A and plug it into a Speech Recognition system. Measure the system's Word Error Rate (WER). Then plug in Model B and measure the WER again. Whichever model results in lower WER is the better model.
- *Examples of Downstream Tasks*: Speech Recognition, Machine Translation, Spell Checking, Search Ranking.
- *Pros*: Proves the actual business value of the model. 
- *Cons*: Extremely slow, computationally expensive, and difficult to isolate variables (e.g., did Model B fail because it's a bad language model, or because it wasn't integrated well with the acoustic model?).

## 3. The Standard Workflow
In modern NLP (and machine learning in general), engineers follow a standard workflow combining both:
1. **Develop** dozens of new model architectures and hyperparameters.
2. **Filter** them rapidly using *Intrinsic Evaluation* (Perplexity). Discard the models with high perplexity.
3. **Select** the top 2 or 3 best-performing models from the intrinsic tests.
4. **Deploy** them to a test environment and run an *Extrinsic Evaluation* (e.g., A/B testing on real users, or running them through a Machine Translation benchmark) to find the final winner.

## 4. Exam Preparation
### Must Memorize
- Intrinsic = Evaluating the model by itself (Perplexity).
- Extrinsic = Evaluating the model inside a larger application (Word Error Rate, Translation BLEU score).

### Likely Theory Question
**Question**: Why is it dangerous to rely solely on Intrinsic Evaluation when deploying a new Language Model to production?
**Answer**: Intrinsic evaluation metrics like perplexity only measure how well the model predicts the test set data distribution. A model might achieve an artificially low perplexity by over-indexing on frequent syntactic structures while failing to capture deep semantic meaning. Extrinsic evaluation is required to prove that the language model actually improves the performance of the end-user application, such as reducing translation errors or improving autocomplete accuracy.

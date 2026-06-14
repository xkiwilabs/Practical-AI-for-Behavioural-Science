# Course Review — Short-Answer Example Questions

These are **9 example short-answer questions** for self-practice. They span the major method families covered in the course, so working through them is a good way to check you can reason about which method fits a given research scenario.

> **A note on the bar — read this first.** These questions are about your **general understanding** of the methods, **not** PhD-level technical depth. The aim is to check that you've engaged with the material, can pick a reasonable approach for a given scenario, and can talk through what you'd do and what you'd be cautious about. Reasonable choices, reasonable caveats, in your own words — that's the whole point. You do not need to memorise formulas, recite every metric, or be perfect. This is meant to be approachable, not stressful.

Each entry below shows:

- The **question prompt**.

- An **example narrative response** — what a strong ~60-second spoken answer might sound like for someone who has just learned these methods. Use it to calibrate **length and structure**; you do not need to memorise the wording, and your own answer should reflect your own thinking. If your answer hits the same main points in your own voice, you're in good shape.

**Suggested format for self-practice:** give yourself 30 seconds to plan, then up to 60 seconds to answer aloud, with a timer.

**Supporting terminology** is in Part 2 of [`concept-list.md`](concept-list.md) — review it before practising so the vocabulary is comfortable.


---

## Regression


### Example 1

**Question:**

> A researcher wants to predict DASS Depression scores from Big Five personality traits in a large student sample. Which ML regression approach would you use, and how would you check it's trustworthy?

**Example narrative response (~1 minute spoken):**

> I'd start with linear regression since the target is continuous and we don't have many predictors. First I'd split the data into train and test — say 80/20 — and standardise the features. Then I'd fit the model on the training set and report R-squared and mean absolute error on the test set. To check it's trustworthy I'd compare test performance against training: if they're close, the model generalises; if test drops a lot, we're overfitting. I'd also run cross-validation for a more stable estimate. If we had a lot more features I'd switch to Ridge or Lasso, but for the Big Five plain linear regression is fine.


### Example 2

**Question:**

> You have 60 self-report items and only 250 participants, and you want to predict perceived stress. Should you use Ridge or Lasso, and why?

**Example narrative response (~1 minute spoken):**

> With 60 items and only 250 people, plain linear regression would overfit — too many predictors for the sample. Both Ridge and Lasso help by shrinking coefficients. Ridge keeps all features but shrinks them toward zero; Lasso zeroes out the less useful ones, giving a sparser, more interpretable model. If I think only a few items matter and I want a cleaner answer, I'd use Lasso. If I think all 60 contribute a little, Ridge is better. Honestly I'd run both, use cross-validation to tune the regularisation strength, and pick whichever gives lower test error. Lasso also doubles as automatic feature selection, which I'd find useful for reporting.


### Example 3

**Question:**

> A colleague reports R² = 0.85 predicting wellbeing from lifestyle variables in their training data, but the model performs poorly on a new cohort. What's gone wrong, and what would you do differently?

**Example narrative response (~1 minute spoken):**

> What's gone wrong is overfitting — the model fit patterns specific to the training data, not patterns that generalise. R-squared of 0.85 on the training data alone is meaningless because we have no idea how the model handles unseen people. The fix is to use a proper train/test split from the start, fit on training, and report on test. Cross-validation gives an even more stable estimate. If the dataset has lots of predictors, I'd also try Ridge or Lasso to prevent the model fitting noise. The rule is: never trust a model that's only been evaluated on the data it was trained on. Test performance is what generalises.


---

## Classification


### Example 4

**Question:**

> A university counselling service wants to flag students likely to be experiencing elevated depression (PHQ-9 ≥ 5) from a short survey. Which ML classification approach would you use, and which metric matters most?

**Example narrative response (~1 minute spoken):**

> This is a binary classification problem. I'd start with logistic regression because it's simple and interpretable — useful if the service wants to know which features matter. I'd do a stratified split to keep the proportion of elevated cases the same in train and test. Then I'd compare to a random forest as a stronger baseline. The most important metric here is recall — false negatives mean missing students who need support, which is worse than flagging some who turn out fine. I'd also look at AUC and the precision-recall curve, and tune the classification threshold below 0.5 since recall matters more than precision in screening.


### Example 5

**Question:**

> Your classifier detects a rare clinical condition (~8% prevalence) and hits 92% accuracy. Why might you be more cautious than your supervisor?

**Example narrative response (~1 minute spoken):**

> 92% accuracy sounds great, but the condition is only 8% prevalent — so a model that just predicts 'no' for every single person would also get 92% accuracy. That's a useless model for screening. Accuracy is the wrong metric here. I'd switch to recall and precision, or AUC, because we care about catching the positive cases. I'd check the confusion matrix to see if the model actually identifies anyone with the condition. If it doesn't, I'd try class-weight balancing during training, tune the threshold to favour recall, or oversample the positive class. With imbalanced data, accuracy is misleading — we need metrics that reflect the cost of missing a positive case.


---

## Dimensionality reduction


### Example 6

**Question:**

> You want a 2D visualisation of participants in a high-dimensional symptom dataset to see whether clinical and non-clinical groups separate. Would you use PCA or UMAP, and why?

**Example narrative response (~1 minute spoken):**

> I'd probably try both, but I'd lean toward UMAP for this. PCA is linear — it preserves global structure and the components are interpretable, but it often doesn't separate non-linear groupings cleanly in 2D. UMAP is non-linear and tends to give clearer visual separation between groups, which is what we want here. The catch is that distances on a UMAP plot don't mean what they look like — two points being close doesn't mean they're literally similar, only that they're related in some sense. So I'd use UMAP for the picture but be careful about the interpretation: I'd colour points by clinical status, see whether they visibly separate, but not make strong claims about cluster sizes or gaps.


---

## Neural networks


### Example 7

**Question:**

> A colleague has 200 participants with personality questionnaire data and wants to use a deep neural network to predict wellbeing because 'deep learning is more powerful'. What would you recommend?

**Example narrative response (~1 minute spoken):**

> 200 participants is small for deep learning. Neural networks shine when you have a lot of data, complex features, or unstructured inputs like images or audio. With 200 participants and tabular questionnaire data, a deep network will probably overfit, and a simpler model will be just as good or better. I'd start with linear regression as a baseline, then try a random forest. If those work well, the neural network probably isn't worth the added complexity. To convince my colleague, I'd train all three on the same train/test split and compare honestly. Only if the neural network clearly beats the simpler models on the test set would I recommend it.


---

## Embeddings & LLM-assisted workflows


### Example 8

**Question:**

> You have 400 interview transcripts about coping during the pandemic. How would you use embeddings to find recurring themes, and how would you check the themes are real?

**Example narrative response (~1 minute spoken):**

> I'd embed each transcript using a pretrained sentence-embedding model — that turns each transcript into a vector capturing its meaning. Then I'd cluster the embeddings, probably with k-means or hierarchical clustering, to find groups of similar transcripts. To label them, I'd read a few transcripts from each cluster and use an LLM to help summarise the common theme. The key check is whether the clusters are real or just noise — I'd vary the number of clusters and the random seed and see if the same groupings come back. I'd also manually code a subset of transcripts myself to compare. I'd never trust the themes without reading enough transcripts to confirm them.


### Example 9

**Question:**

> A colleague used ChatGPT to do a 'thematic analysis' of their interview transcripts and pasted the output straight into their results section. What concerns would you raise, and how should they have done it instead?

**Example narrative response (~1 minute spoken):**

> I'd raise a few concerns. First, reproducibility — LLMs are non-deterministic, so running it again could give different themes, which is a problem for scientific reporting. Second, hallucination — the model might invent themes that aren't really in the transcripts, especially with long inputs. Third, there's no validation — themes should be grounded in the data, and the colleague hasn't checked that. A better approach is to embed each transcript using a sentence-embedding model, cluster the embeddings, then use the LLM to help summarise each cluster. The researcher reads a sample of transcripts from each cluster to confirm the theme. That keeps the LLM as an assistant, not the authoritative source.


---

*[Back to the Week 12 study guide](README.md)*
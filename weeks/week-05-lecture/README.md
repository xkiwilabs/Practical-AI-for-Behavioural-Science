# Week 5: Prediction with Accountability — Classification, Uncertainty, and Evaluation

> **Companion reading for the Week 5 lecture.** Read this before or after the lecture — it covers the same ideas in more depth, with examples you can revisit at your own pace.

---

## Overview

Last week you predicted a *number* — a depression score. This week, we predict a *category*: does this person have elevated depression, or not? That single shift — from regression to classification — changes everything about how we evaluate our models, because now the *type* of mistake matters as much as how many mistakes we make.

## From Regression to Classification

In regression, your model outputs a number (like a depression score from 0 to 42), and you measure how far off it is. In classification, your model outputs a *label* — "elevated" or "not elevated," "at risk" or "low risk," "respond to treatment" or "unlikely to respond."

This should feel familiar from statistics. Logistic regression has been a workhorse of behavioural research for decades — any time you've seen a study predicting a binary outcome (dropout vs. retention, diagnosis vs. no diagnosis), that's classification. The difference in ML is the focus: rather than asking "is this predictor significant?", we ask "how accurately can the model identify who belongs to each group in new data it hasn't seen?"

Binary classification (two categories) is the most common type, and it's what we'll focus on. The target variable has exactly two values — often coded as 0 and 1. In Week 6, you'll classify participants as having elevated depression (PHQ-9 score ≥ 5) or minimal symptoms (< 5) using real COVID-era survey data.

## Logistic Regression

Logistic regression is the most natural bridge from what you already know. Instead of fitting a straight line through the data (linear regression), it fits an S-shaped curve called a **sigmoid function**. This curve squashes any input into a value between 0 and 1 — which we interpret as a *probability*.

![Confusion Matrix](figures/confusion-matrix.svg)

So a logistic regression model doesn't just say "elevated" or "not elevated." It says "there's a 73% probability this person has elevated depression." We then choose a **decision boundary** — typically 0.5 — and classify anyone above that threshold as "elevated" and anyone below as "not elevated."

This probability output is powerful. It lets us adjust *how cautious* the model is, as we'll see when we discuss decision thresholds below.

You don't need to understand the mathematics of the sigmoid function for this course. The key intuition is: logistic regression converts a linear combination of features into a probability, and that probability determines the predicted class.

## The Confusion Matrix

When a classifier makes predictions, every prediction falls into one of four categories:

| | **Actually Elevated** | **Actually Minimal** |
|---|---|---|
| **Predicted Elevated** | True Positive (TP) | False Positive (FP) |
| **Predicted Minimal** | False Negative (FN) | True Negative (TN) |

These four cells tell you everything about how a classifier performs — and *where* it goes wrong.

Consider a depression screening tool used at a university counselling centre. If the model predicts "elevated" for a student who genuinely has elevated symptoms, that's a **true positive** — the system correctly identified someone who needs support. If it flags a student who's actually fine, that's a **false positive** — an unnecessary follow-up, perhaps some worry, but relatively low cost.

But what about a **false negative**? The model says "minimal" for someone who actually has elevated depression. That student might not get referred for support. In a screening context, this is the more dangerous error.

> **Think about it #1:** Imagine two depression screening tools for a university. Tool A catches 95% of students with elevated depression, but also flags 40% of students who are fine (high false positive rate). Tool B catches only 70% of those with elevated depression, but rarely flags anyone incorrectly. Which would you choose for a walk-in counselling service? What about for an emergency crisis detection system? Why might the answer be different?

## Classification Metrics

**Accuracy** is the most intuitive metric: what proportion of predictions were correct? But accuracy has a fatal flaw called the **accuracy trap**. Imagine 95% of your sample does *not* have elevated depression. A model that predicts "not elevated" for everyone achieves 95% accuracy — without learning anything at all.

This is why we need several metrics, each capturing a different aspect of performance:

- **Precision:** Of everyone the model *flagged as elevated*, how many actually were? High precision means few false alarms.
- **Recall (sensitivity):** Of everyone who *actually had elevated depression*, how many did the model catch? High recall means few missed cases.
- **F1 score:** The harmonic mean of precision and recall — a single number that balances both. Useful when you want one summary metric but accuracy is misleading.
- **Specificity:** Of everyone who was *actually minimal*, how many did the model correctly identify? The mirror image of recall, focused on the "negative" class.

There's always a tension between precision and recall. Making the model more aggressive at flagging cases (higher recall) inevitably means more false alarms (lower precision). The F1 score captures this trade-off in a single number.

**ROC-AUC** (Area Under the Receiver Operating Characteristic curve) evaluates the model *across all possible thresholds*. The ROC curve plots recall against false positive rate at every threshold. A perfect model has AUC = 1.0; random guessing gives 0.5. AUC answers: "If I pick one elevated and one minimal person at random, how often does the model rank the elevated person higher?"

![ROC Curve](figures/roc-curve.png)

## Decision Thresholds

Most classifiers don't just output a label — they output a *probability*. The threshold for converting that probability into a label is a **choice you make**, not a law of nature.

The default threshold is 0.5: if the model says there's more than a 50% chance of elevated depression, classify as elevated. But you can adjust this:

- **Lower the threshold** (e.g., 0.3): cast a wider net, catch more true cases, but also more false alarms. Good for screening where missing someone is costly.
- **Raise the threshold** (e.g., 0.7): be more conservative, fewer false alarms, but miss more true cases. Good when the intervention is expensive or invasive.

![Threshold Trade-off](figures/threshold-tradeoff.svg)

The right threshold depends on the **costs of different errors**. In a depression screening programme, a false negative (missing someone who needs help) is arguably worse than a false positive (flagging someone for a follow-up conversation). So you might lower the threshold. In a study selecting participants for an expensive clinical trial, false positives waste resources — you might raise it.

> **Think about it #2:** You've built a classifier that predicts which first-year students are likely to drop out of university. The model outputs a probability for each student. If you set a low threshold (say 0.3), many students get flagged and receive extra support — but resources are spread thin. If you set a high threshold (0.7), only the most at-risk students get support — but some who needed help are missed. What factors should guide your choice?

## Class Imbalance

Class imbalance occurs when one category is much more common than the other — for example, if only 5% of participants have a clinical diagnosis. In these situations, accuracy becomes nearly useless (the "predict everyone as healthy" model gets 95%), and you need to rely on precision, recall, F1, and AUC instead.

Strategies for handling imbalance include oversampling the minority class, undersampling the majority, adjusting class weights in the model, or using metrics that don't reward simply guessing the majority class. The good news for Week 6: our dataset is nearly balanced (54.5% elevated, 45.5% minimal), so imbalance won't be a major concern.

## Decision Trees

A decision tree makes predictions through a series of if-then questions about your features, creating a flowchart-like structure. For example:

> If sleep latency > 25 minutes → check stress coping...
> If stress coping < 3 → predict "elevated"
> Otherwise → check negative affect...

![Decision Tree Example](figures/decision-tree-example.svg)

The beauty of decision trees is their **interpretability**. You can trace exactly *why* the model made a particular prediction by following the branches. This matters in psychology and healthcare, where "the model said so" isn't a satisfying explanation.

The downside? Decision trees are prone to **overfitting**. An unrestricted tree will keep splitting until it perfectly memorises the training data, creating branches for noise rather than genuine patterns. Think of it like a clinician who builds an increasingly elaborate diagnostic checklist — at some point, the checklist starts encoding quirks of the specific patients they've seen rather than general patterns that apply to new patients.

We control overfitting in trees using several parameters:

- **Maximum depth** (`max_depth`): Limits how many levels of questions the tree can ask. A depth of 3 means the tree can ask at most three questions in sequence before making a prediction. Shallow trees are simpler and less likely to overfit, but might miss genuine patterns. In Week 6, we'll use `max_depth=5` for single trees and `max_depth=10` for random forests.
- **Minimum samples per leaf** (`min_samples_leaf`): Requires that every terminal node (the endpoints where predictions are made) contains at least a certain number of observations. Setting this to 10, for example, prevents the tree from creating a branch that applies to just one or two unusual participants. This is like saying "don't draw a conclusion from fewer than 10 cases."
- **Minimum samples to split** (`min_samples_split`): The minimum number of observations required before a node can be split further. If a node has fewer than this many observations, the tree stops splitting there regardless of whether a split would improve performance.
- **Pruning**: Instead of restricting the tree while it grows, you let it grow fully and then remove branches that don't improve performance enough to justify their complexity. This is like writing a first draft and then editing out tangential paragraphs. In scikit-learn, the `ccp_alpha` parameter controls cost-complexity pruning — higher values prune more aggressively.

These parameters all make the same fundamental trade-off: a simpler tree generalises better to new data but might miss some real patterns in the training data. In practice, `max_depth` and `min_samples_leaf` are the most commonly tuned parameters.

## Ensembles and Random Forests

If one decision tree is good but prone to overfitting, what about *many* trees? That's the idea behind **ensemble methods** — combining multiple models to get better predictions than any single model alone.

A **Random Forest** builds dozens or hundreds of decision trees, each trained on a random subset of the data and a random subset of features. Each tree makes its own prediction, and the forest takes a vote — the majority wins. This is like asking 100 slightly different experts for their opinion and going with the consensus.

![Random Forest Concept](figures/random-forest-concept.svg)

Why does this work? Individual trees might overfit to quirks in their particular data subset, but those quirks are different for each tree. When you average across many trees, the idiosyncratic errors cancel out, leaving only the genuine patterns. This is the bias-variance trade-off from Week 3 in action: each tree has low bias but high variance; the ensemble keeps the low bias while dramatically reducing variance.

Random forests also provide **feature importance** — a ranking of which features contributed most to the predictions across all the trees. The figure below shows an example from a depression classification task: mood and anxiety measures (negative affect, GAD-7 anxiety, stress coping) dominate, while personality traits and demographics contribute less. This kind of ranking helps researchers understand *what the model relies on* — and whether those features make psychological sense.

![Feature Importance Example](figures/feature-importance-example.png)

> **Think about it #4:** Suppose your logistic regression achieves 82% accuracy on a depression classification task, while a decision tree achieves only 76%. A colleague suggests you should use the logistic regression because it's more accurate. Can you think of a situation where you might prefer the less accurate decision tree? What does the tree give you that logistic regression doesn't?

## Tuning and Optimising Your Models

So far we've treated models as off-the-shelf tools: pick a model, fit it, evaluate it. But most models have **hyperparameters** — settings you choose *before* training that control how the model learns. We already saw some: `max_depth` and `min_samples_leaf` for decision trees, the number of trees in a random forest, or the regularisation strength (`alpha`) from Week 4's Ridge and Lasso models.

How do you find the best hyperparameters? You could try a few values by hand, but there are more systematic approaches:

- **Grid search** tests every combination from a predefined set of values. For example, try `max_depth` = 3, 5, 7, 10 and `min_samples_leaf` = 1, 5, 10 — that's 12 combinations. For each, run cross-validation and pick the combination with the best performance. This is thorough but can be slow when you have many hyperparameters.
- **Random search** samples combinations randomly rather than testing all of them. Surprisingly, this often finds good settings faster than grid search, because not all hyperparameters matter equally — random search spends less time exhaustively varying the ones that don't make much difference.

The key principle: always evaluate hyperparameter choices using **cross-validation on the training set**, never on the test set. If you use the test set to pick hyperparameters, you're effectively training on it — and your final performance estimate will be overly optimistic. This is the same logic as the "never peek at the test set" rule from Week 3, applied to model settings rather than model weights.

### Feature Selection

Choosing *which features to include* is another form of optimisation. More features aren't always better — irrelevant features add noise, slow down training, and can reduce performance. There are two classic strategies:

- **Forward selection** starts with no features and adds them one at a time. At each step, try adding each remaining feature, keep the one that improves performance the most, and repeat. Stop when adding more features doesn't help. This is like building a research questionnaire by starting with nothing and adding items that each improve prediction.
- **Backward elimination** starts with *all* features and removes them one at a time. At each step, drop the feature whose removal hurts performance the least, and repeat. Stop when removing anything makes the model noticeably worse. This is like editing a long questionnaire by cutting items that aren't contributing.

Tree-based models offer a shortcut: you can use the **feature importance** scores (like the ones shown above) to identify and drop low-importance features. This isn't as rigorous as forward or backward selection, but it's fast and often effective.

There are also more advanced techniques you may encounter:

- **Gradient boosting** (XGBoost, LightGBM) builds trees *sequentially*, where each new tree focuses on correcting the mistakes of the previous ones. This often outperforms random forests but requires more careful tuning.
- **Stacking** combines predictions from multiple different model types (e.g., logistic regression + random forest + gradient boosting) by training a second model to learn the best way to blend their outputs.

We'll return to hyperparameter tuning and model optimisation in more depth in later weeks. For now, the important takeaway is that "fit a model and report the results" is rarely the whole story — there's a principled process of tuning settings and selecting features that can substantially improve performance, as long as you always evaluate honestly using held-out data.

## Fairness and Ethics

Classification models that affect people's lives raise serious ethical questions. Two landmark examples:

**COMPAS** (Correctional Offender Management Profiling for Alternative Sanctions) is an algorithm used in the US criminal justice system to predict recidivism — whether a defendant will reoffend. A ProPublica investigation found that Black defendants were almost twice as likely to be incorrectly labelled as high risk (false positives) compared to white defendants, even when controlling for prior criminal history.

**Obermeyer et al. (2019)** examined a widely-used healthcare algorithm that was supposed to identify patients who would benefit from extra care. The algorithm used healthcare *costs* as a proxy for health *needs* — but because Black patients historically had less access to healthcare (and therefore lower costs), the algorithm systematically under-identified Black patients who needed care.

A mathematical result called the **impossibility theorem** (Chouldechova, 2017) shows that you cannot simultaneously satisfy all common definitions of fairness when base rates differ between groups. If depression rates genuinely differ across demographic groups, you cannot simultaneously achieve equal false positive rates, equal false negative rates, and equal predictive values across all groups. This isn't a technical problem to solve — it's a *values* question about which type of fairness matters most in each context.

> **Think about it #3:** You've built a depression classifier that achieves 85% accuracy overall. When you check performance across demographic groups, you find it's 90% accurate for one group but only 72% for another. Should you deploy this model? What questions would you want to ask before making that decision?

## Common Misconceptions

- **"Higher accuracy always means a better model."** No — accuracy can be misleading when classes are imbalanced. Always check precision, recall, and AUC alongside accuracy.
- **"Random forests are always better than logistic regression."** Not necessarily. When relationships are roughly linear and the dataset is moderate-sized, logistic regression often performs just as well — and it's more interpretable.
- **"The model's output is the final answer."** The model outputs a *probability*. Converting that to a label requires choosing a threshold, which is a *human* decision guided by the costs of different errors.

## Getting Ready for Week 6

Next week, you'll build classifiers on real mental health survey data from the Boston College COVID-19 Sleep and Well-Being study. This dataset includes daily surveys (sleep, mood, social contact) and assessments (personality, anxiety, depression) from over 800 participants during the early months of the pandemic.

**Before class, download the data:**
```
conda activate ai-behsci
cd weeks/week-06-lab/data
python download_data.py
```

**New LLM skill — Refactoring:** In Week 2 you learned prompting, in Week 4 you learned debugging. This week's skill is **refactoring** — asking your AI assistant to take working-but-messy code and make it cleaner, more modular, and easier to understand *without changing what it does*. Refactoring isn't just about code structure — good documentation and clear comments are just as important as the code itself. In research, someone else (or future you) needs to understand not just *what* the code does, but *why* each step was chosen. It is almost always better to write code that is transparent and easy to follow than to write clever, optimised code that saves a millisecond but nobody can understand.

---

*[Back to course overview](../../README.md)*

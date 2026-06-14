# Course Review — Concept Reference

This is your review reference for the course. It has two parts:

- **Part 1** lists **40 core concepts** to self-quiz on. Definitions are not shown here; practise giving each definition aloud in about 20 seconds to check you can explain it crisply.
- **Part 2** lists **additional course concepts** (method names, metrics, and tools used throughout the course). Definitions are provided so you can use this as a reading reference and feel comfortable using these terms when you talk about the methods you've learned.

---

# Part 1 — Core Concept List (40 terms)

A good self-quiz: pick terms at random and explain each one aloud. Grouped by the week of the course that introduced each concept.

## Week 1 — ML in Psychological Science

- Artificial Intelligence (AI)
- Machine Learning (ML)
- Generalisation

## Week 2 — Setup + LLM Problem-Solving Loop

- Prompt Engineering
- Context Engineering
- LLM Problem-Solving Loop

## Week 3 — Generalisation & Overfitting

- Overfitting
- Underfitting
- Bias-Variance Tradeoff
- Cross-Validation
- Hyperparameter

## Week 4 — Regression Pipeline

- Linear Regression
- Regularisation
- Lasso Regression (L1)
- Mean Absolute Error (MAE)

## Week 5 — Classification & Evaluation

- Classification
- Decision Tree
- Random Forest
- Confusion Matrix
- ROC Curve / AUC (Receiver Operating Characteristic / Area Under the Curve)

## Week 6 — Trees & Ensembles

- Ensemble Learning
- Feature Importance
- Classification Threshold

## Week 7 — Clustering & Dimensionality Reduction

- Clustering
- K-Means
- Principal Component Analysis (PCA)

## Week 8 — PCA / UMAP & Clustering

- Cluster Stability
- Silhouette Score

## Week 9 — Neural Networks

- Neural Network (Artificial)
- Perceptron
- Activation Function
- Backpropagation
- Dropout

## Week 10 — Neural Network Training

- Training Loop (Epoch and Batch)
- Loss Function

## Week 11 — Deep Learning, LLMs, GenAI

- Convolutional Neural Network (CNN)
- Transformer
- Embedding
- Self-Attention
- Hallucination (LLM)

---

# Part 2 — Additional Course Concepts (with definitions)

These are method names, metrics, and tools used throughout the course. You should be comfortable using them when you talk about the methods you've learned. Read them as a reading reference; you do not need to memorise the wording.

## Regression & general modelling

**R-squared (R²) — Coefficient of Determination**
The proportion of variance in the outcome explained by the model (0 to 1). Commonly reported alongside MAE for regression. A high R² on training data alone is meaningless without a held-out test estimate.

**Logistic Regression**
A classification model that outputs the probability of a binary outcome via a sigmoid over a weighted sum of features. The standard linear baseline before trying more complex classifiers.

**Standardisation (Z-score scaling)**
Rescaling each feature to mean 0 and standard deviation 1. Used before regression, clustering, dimensionality reduction, or neural networks to put features on a comparable scale.

**Held-out Test Set**
A portion of the data set aside before training and used only to estimate how the model performs on unseen data. The test score is what you report — not the training score.

**Stratified Train/Test Split**
A way of splitting the data so that class proportions are preserved in both training and test sets. Important for classification with imbalanced classes.

## Classification metrics & imbalance

**Recall (Sensitivity)**
Of all actual positives, the fraction the classifier correctly identifies. Emphasised when false negatives are costly — e.g., clinical screening, where missing a case is worse than a false alarm.

**Precision**
Of all positives the classifier predicts, the fraction that are correct. Emphasised when false positives are costly.

**F1 Score**
The harmonic mean of precision and recall. A single number that balances the two; useful when classes are imbalanced.

**Class Imbalance**
When one class is much more common than another. Accuracy becomes a misleading metric, and methods like **class-weight balancing** (telling the model to penalise mistakes on the rare class more) or **oversampling** (generating more examples of the rare class) are used to address it.

## Clustering & dimensionality reduction

**Hierarchical Clustering**
A clustering method that builds a tree (dendrogram) of nested groupings, from individual points up to one big cluster. Cutting the tree at different heights gives different numbers of clusters.

**Elbow Method**
A way to choose the number of clusters (k) by plotting within-cluster variance against k and looking for the "elbow" — the point where adding more clusters stops yielding much improvement.

**Adjusted Rand Index (ARI)**
A metric that compares two clusterings of the same data and corrects for chance. Useful for checking whether clusters are stable across runs (closer to 1 = more agreement, 0 = chance, negative = worse than chance).

**Scree Plot**
A plot of variance explained by each PCA component in descending order. Used to choose how many components to keep — typically where the curve flattens out.

**Variance Explained**
The proportion of total variance captured by a PCA component, or by the first *k* components combined. A typical target is 70–90% cumulative variance retained.

**UMAP (Uniform Manifold Approximation and Projection)**
A non-linear dimensionality-reduction algorithm that produces 2D or 3D visualisations preserving local neighbourhood structure. Great for visually exploring whether groups separate, but distances on the plot do not have a strict quantitative meaning.

## Embeddings

**Sentence-embedding Model**
A pretrained model (e.g., SBERT, OpenAI text-embedding models) that converts a sentence or document into a fixed-length vector capturing its meaning. The basis of semantic search and clustering of text.

**Cosine Similarity**
A measure of similarity between two vectors based on the angle between them (ranges from −1 to 1, typically 0 to 1 for embeddings). The standard distance metric for comparing embeddings.

## Pose & video-based ML

**MediaPipe / DeepLabCut / OpenPose**
Marker-less pose-estimation tools that use CNNs to extract joint keypoints from video without physical markers. **MediaPipe** runs on a phone or browser; **DeepLabCut** is standard in animal behaviour research; **OpenPose** is widely used for human motion.

**Kinematic Features**
Movement-derived features computed from raw pose keypoints — e.g., velocity, smoothness, postural sway, head rotation. These summarise behaviour for a downstream classical-ML classifier.

## Evaluation & training

**Inter-rater Reliability**
The degree to which two or more raters (human or machine) agree when scoring the same items. Commonly reported as Cohen's kappa or ICC. Required evidence before trusting an automated coder against human raters.

**Learning Rate**
A hyperparameter that controls how big a step the optimiser takes when updating a neural network's weights. Too small → training is slow or stuck; too large → training is unstable or diverges.

---

*[Back to the Week 12 study guide](README.md)*

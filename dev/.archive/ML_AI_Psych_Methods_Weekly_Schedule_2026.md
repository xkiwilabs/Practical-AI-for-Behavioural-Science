# Current Advances in Psychological Methods and Analyses

**Class time:** Mondays, 3:00–5:00pm

**Teaching dates:** 23 Feb 2026 – 01 Jun 2026

**Mid-semester break (no classes):** 06 Apr 2026 – 19 Apr 2026

## Course Description

This unit introduces modern computational methods now shaping psychological and cognitive science research, with a focus on machine learning and contemporary AI tools, including large language models (LLMs). Students learn how to frame research questions for supervised and unsupervised learning, evaluate models responsibly, and use LLM-based assistants to support coding, analysis, visualisation, and research workflows. No technical or mathematical background is assumed; emphasis is placed on practical, student-guided experimentation and sound scientific interpretation.

## Weekly Schedule

### Week 1 — Mon 23 Feb 2026 — *Lecture*

**From Mind to Model: Why ML Belongs in Psychological Science**

Introduce the course goals, core ML concepts, and how AI tools change psychological research. Clarify prediction versus explanation, generalisation, and common threats like confounds and data leakage. Establish the "LLM problem-solving loop" students will use all semester: plan, prompt, verify, refine, and document.

*Key concepts:* Prediction vs. explanation, generalisation, overfitting (preview), data leakage, the LLM problem-solving loop

---

### Week 2 — Mon 02 Mar 2026 — *Lab + student presentations*

**Coding Lab 1: Setup, Plotting, and the LLM Problem-Solving Loop**

Lab setup: Python/Jupyter, core libraries, and a reproducible workflow. Students work with scaffolded notebooks (fill-in-the-blanks) to reduce friction for beginners. Practice prompting an LLM for code generation, verifying outputs with plots and shape checks.

*LLM skill focus:* Basic prompting — "Write code that does X"

**Group Challenge: Reproduce a Figure**
Given a dataset and a published figure, recreate the visualisation using LLM-assisted coding. Success = visual match + clean, documented code.

---

### Week 3 — Mon 09 Mar 2026 — *Lecture*

**Models, Not Magic: Generalisation, Overfitting, and How ML Misleads**

Deepen foundations of supervised learning: targets, features, preprocessing, baselines, and evaluation. Cover train/test splits, cross-validation, bias–variance trade-offs, and how overfitting appears in behavioural datasets. Students learn to choose metrics that match research questions and to interpret performance as evidence, not truth.

*Key concepts:* Training vs. test data, cross-validation, bias-variance trade-off, overfitting, baseline models, evaluation metrics

---

### Week 4 — Mon 16 Mar 2026 — *Lab + student presentations*

**Coding Lab 2: Regression Pipeline, Cross-Validation, and Interpretation**

Build end-to-end pipelines for linear and regularised models (Ridge/Lasso). Use cross-validation, learning curves, and residual diagnostics to detect misfit. Practice LLM-assisted debugging on preprocessing and modelling code.

*LLM skill focus:* Debugging — "Here's my error, help me fix it"

**Group Challenge: Predict & Explain**
Predict a psychological outcome (e.g., test anxiety from survey items). Groups compete on held-out test performance but must also write a 1-paragraph interpretation linking coefficients to psychological meaning.

---

### Week 5 — Mon 23 Mar 2026 — *Lecture*

**Prediction with Accountability: Classification, Uncertainty, and Evaluation**

Introduce classification for psychological prediction tasks: logistic regression, decision thresholds, and class imbalance. Compare metrics (accuracy, F1, ROC-AUC, PR-AUC) and emphasise calibration and uncertainty. Discuss interpretability and ethical risks of categorising people.

*Key concepts:* Classification, decision thresholds, precision/recall trade-off, class imbalance, calibration, fairness considerations

---

### Week 6 — Mon 30 Mar 2026 — *Lab + student presentations*

**Coding Lab 3: Trees, Ensembles, Feature Importance, and Error Analysis**

Implement decision trees and ensembles (random forests; optional boosting). Focus on practical tuning, cross-validation, and diagnosing failure modes via error analysis and subgroup checks. Use feature importance and partial dependence carefully, noting their assumptions.

*LLM skill focus:* Refactoring — "Make this code cleaner and add verification checks"

**Group Challenge: Build a Defensible Classifier**
Classify a meaningful outcome (e.g., dropout risk, treatment response). Groups must justify their threshold choice, report appropriate metrics, and discuss one ethical concern with deployment.

---

### Mid-Semester Break — 06 Apr 2026 – 19 Apr 2026

---

### Week 7 — Mon 20 Apr 2026 — *Lecture*

**Discovering Structure: Clustering and Dimensionality Reduction Without Self-Deception**

Unsupervised learning for behavioural and cognitive data: clustering (k-means, hierarchical, DBSCAN) and dimensionality reduction (PCA versus UMAP/t-SNE). Emphasise stability, sensitivity to preprocessing, and the danger of reifying "types." Students learn to separate visualisation from inference.

*Key concepts:* Clustering algorithms, dimensionality reduction, stability analysis, visualisation vs. inference, the problem of "discovering" imposed structure

---

### Week 8 — Mon 27 Apr 2026 — *Lab + student presentations*

**Coding Lab 4: PCA/UMAP, Clustering, and Stability Checks**

Apply PCA/UMAP and clustering to a psychology-relevant dataset. Evaluate cluster solutions using silhouette scores, resampling stability, and qualitative sanity checks. Practice LLM-assisted coding for clean visualisations and reproducible notebooks.

*LLM skill focus:* Documentation — "Explain this analysis for a methods section"

**Group Challenge: Find Structure, Don't Fabricate It**
Cluster a messy behavioural dataset. Groups must run stability checks (bootstrap, different initialisations) and present what they found AND what they're uncertain about. No overclaiming "types."

**Written assignment due**

---

### Week 9 — Mon 04 May 2026 — *Lecture*

**Learning Representations: Neural Networks as Psychological Tools (and Limits)**

Neural networks as flexible function approximators: perceptrons to multilayer networks, losses, optimisation, and regularisation. Discuss when deep learning helps in psychology/cognitive science (data scale, signal-to-noise, representation needs) and when simpler models are better. Introduce training diagnostics and the importance of baseline comparisons.

*Key concepts:* Neurons, layers, activation functions, loss functions, gradient descent, overfitting in neural nets, when complexity is warranted

---

### Week 10 — Mon 11 May 2026 — *Lab + student presentations*

**Coding Lab 5: Simple Neural Network, Training Diagnostics, and Baseline Comparison**

Build and train a small neural network (MLP) in PyTorch on a behavioural dataset. Compare performance to classical baselines, tune hyperparameters, and troubleshoot instability (scaling, learning rate, overfitting).

*LLM skill focus:* Complex debugging — "My loss isn't decreasing, here's my code..."

**Group Challenge: Beat the Baseline**
Train a neural network that outperforms a logistic regression baseline. Document what worked, what failed, and honestly assess: was the added complexity worth it?

---

### Week 11 — Mon 18 May 2026 — *Lecture*

**Meaning in Vectors: Embeddings and LLMs for Research Workflows**

Introduce embeddings and LLMs as research infrastructure: semantic similarity, clustering text, retrieval, and assisted coding. Explain prompting versus retrieval-augmented generation and evaluation strategies (human checks, gold labels, robustness tests). Now that students have used LLMs all semester, explain what's happening under the hood.

*Key concepts:* Word/sentence embeddings, semantic similarity, how LLMs generate text, prompt engineering principles, evaluation and verification

---

### Week 12 — Mon 25 May 2026 — *Viva review session*

**Viva Review: Consolidation, Q&A, and Practice Defenses**

No new content. Students rehearse short defenses of their written work and methods choices, practice explaining model evaluation and limitations, and answer targeted questions about leakage, overfitting, and interpretation. Time reserved for Q&A and exam format guidance.

---

### Week 13 — Mon 01 Jun 2026 — *Lecture + group discussion*

**What You Can Claim: Limits, Ethics, Reproducibility, and Reasoned Conclusions**

Wrap-up lecture and discussion on the boundaries of ML and AI in psychological science. Cover reproducibility, documentation, data governance, privacy, bias, and responsible communication of uncertainty. Students critique example claims, identify what evidence supports, and practice writing reasoned conclusions that separate prediction from explanation.

*Key takeaways:* Prediction ≠ explanation; uncertainty is honesty, not weakness; LLMs are tools, not oracles

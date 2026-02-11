# PSYC4411: Current Advances in Psychological Methods and Analyses

## Course Information

**Class time:** Mondays, 3:00–5:00pm
**Teaching dates:** 23 Feb 2026 – 01 Jun 2026
**Mid-semester break (no classes):** 06 Apr 2026 – 19 Apr 2026

---

## Course Description

This unit introduces modern computational methods now shaping psychological and cognitive science research, with a focus on machine learning and contemporary AI tools, including large language models (LLMs). Students learn how to frame research questions for supervised and unsupervised learning, evaluate models responsibly, and use LLM-based assistants to support coding, analysis, visualisation, and research workflows.

**No technical or mathematical background is assumed.** Emphasis is placed on practical, student-guided experimentation and sound scientific interpretation. Students will learn to use modern LLM tools (e.g., ChatGPT, Claude, Copilot) as coding assistants and problem-solving partners throughout the course.

---

## Learning Objectives

By the end of this course, students will be able to:

1. **Frame research questions** appropriately for supervised and unsupervised machine learning
2. **Build and evaluate** regression, classification, clustering, and simple neural network models
3. **Use LLM coding assistants** effectively to write, debug, refactor, and document code
4. **Interpret model outputs** with appropriate uncertainty and connect findings to psychological constructs
5. **Identify common pitfalls** including overfitting, data leakage, and spurious structure
6. **Communicate findings** clearly, distinguishing prediction from explanation and acknowledging limitations
7. **Evaluate ethical implications** of ML-based categorisation and prediction in psychological research

---

## Pre-Class Preparation

Since 80% of students have no prior coding experience, **all students must complete the following before Week 2:**

- [ ] Install Python and Jupyter (instructions provided on iLearn)
- [ ] Complete the "Zero to Jupyter" video walkthrough (30 min)
- [ ] Run the test notebook to verify your setup works
- [ ] Create accounts for your chosen LLM assistant (ChatGPT, Claude, or similar)

This preparation ensures Week 2 lab time focuses on learning, not troubleshooting installations.

---

## Assessment

### Written Assignment (100%)

**Due:** Week 8 (Monday 27 Apr 2026, 5:00pm)

A short methods-and-results report (1500–2000 words) demonstrating:
- A complete analysis pipeline (preprocessing → modelling → evaluation)
- Justified methodological choices with reference to course concepts
- Appropriate interpretation with clearly stated limitations
- Evidence of LLM-assisted coding with documentation of your process

The assignment will use a provided dataset. Students may work on the technical implementation in their groups but must write the report individually.

### Viva Examination

**Week 12–13** (scheduled individually)

A 15-minute oral examination where you:
- Defend your written assignment choices
- Explain your code and modelling decisions
- Answer questions about course concepts (overfitting, leakage, interpretation, etc.)
- Demonstrate understanding of what your results do and do not show

---

## Weekly Structure

Each week follows one of two formats:

### Lecture Weeks (Weeks 1, 3, 5, 7, 9, 11, 13)
- 90 min: Lecture with discussion
- 30 min: Q&A and concept consolidation

### Lab Weeks (Weeks 2, 4, 6, 8, 10)
- 15 min: Brief recap and challenge introduction
- 75 min: Group challenge work (groups of 4–5 students)
- 20 min: Group presentations and peer discussion
- 10 min: "Prompting Wins & Fails" — one group shares an LLM interaction that helped or hindered

### Week 12 (Viva Review)
- Practice defenses and Q&A

---

## Group Challenges

Lab weeks feature structured challenges completed in groups of 4–5 students. Groups are assigned in Week 2 and remain stable throughout the semester.

### Challenge Format

Each challenge includes:
- **A clear problem** with provided data and success criteria
- **A deliverable:** Jupyter notebook + brief written summary (300–500 words)
- **A 5-minute presentation** to the class
- **Peer feedback** using a structured rubric

### Challenge Rubric

| Criterion | Excellent | Satisfactory | Needs Work |
|-----------|-----------|--------------|------------|
| **Code runs** | Fully reproducible, no errors | Runs with minor fixes | Does not run |
| **Approach** | Well-justified, appropriate for problem | Reasonable but not fully justified | Inappropriate or unjustified |
| **Interpretation** | Clear, appropriately cautious, connected to constructs | Mostly clear, some overreach | Overconfident or disconnected |
| **LLM use** | Documented, verified, critically evaluated | Used but not well documented | No evidence of verification |
| **Presentation** | Clear, within time, addresses limitations | Mostly clear, minor issues | Unclear or over time |

### Challenge Schedule

| Week | Challenge | Key Skills |
|------|-----------|------------|
| 2 | **Reproduce a Figure** | Prompting, plotting, verification |
| 4 | **Predict & Explain** | Regression, cross-validation, interpretation |
| 6 | **Build a Defensible Classifier** | Classification, thresholds, ethics |
| 8 | **Find Structure, Don't Fabricate It** | Clustering, stability, uncertainty |
| 10 | **Beat the Baseline** | Neural nets, comparison, debugging |

---

## LLM Skill Progression

A core course goal is learning to use LLMs as effective research tools. Each lab builds specific prompting skills:

| Week | LLM Skill Focus | Example Prompts |
|------|-----------------|-----------------|
| 2 | **Basic code generation** | "Write Python code that loads a CSV and creates a scatter plot of X vs Y" |
| 4 | **Debugging** | "Here's my error message and code. What's wrong and how do I fix it?" |
| 6 | **Refactoring & testing** | "Make this code cleaner and add a check that the output shape is correct" |
| 8 | **Documentation** | "Explain this analysis pipeline for a methods section" |
| 10 | **Complex debugging** | "My neural network loss isn't decreasing. Here's my training loop..." |

### The LLM Problem-Solving Loop

Throughout the course, students practice this cycle:

```
1. PLAN    → What am I trying to do? What do I need?
2. PROMPT  → Ask the LLM for code/help
3. VERIFY  → Does it run? Is the output sensible? Check shapes, plots, edge cases
4. REFINE  → Fix errors, improve code, re-prompt if needed
5. DOCUMENT → Record what you did and why
```

**Critical rule:** Never trust LLM output without verification. Always check that code runs, outputs make sense, and results align with expectations.

---

## Student Paper Presentations

Each lab week includes short student presentations on relevant research papers.

### Format
- **Duration:** 5 minutes (strict)
- **Content:** Summarise the paper's question, methods, findings, and one limitation
- **Discussion:** 2–3 minutes of class questions

### Schedule
- Papers are assigned in Week 1
- 3–4 presentations per lab week
- All students present once during the semester

### Presentation Rubric

| Criterion | Points |
|-----------|--------|
| Clear summary of research question | /2 |
| Accurate description of methods | /3 |
| Key findings communicated | /2 |
| Limitation or critique identified | /2 |
| Within time limit | /1 |
| **Total** | **/10** |

---

## Course Datasets

To reduce cognitive load and build familiarity, the course uses recurring datasets:

1. **Survey dataset** — Questionnaire data with psychological scales (used in Weeks 2, 4, 6)
2. **Behavioural dataset** — Response times and accuracy from a cognitive task (used in Weeks 4, 8, 10)
3. **Text dataset** — Open-ended responses for embedding and clustering (used in Week 11)

Using consistent data helps you see how different methods reveal different aspects of the same phenomena.

---

## Weekly Schedule

### Week 1 — Mon 23 Feb 2026 — *Lecture*

**From Mind to Model: Why ML Belongs in Psychological Science**

Introduce the course goals, core ML concepts, and how AI tools change psychological research. Clarify prediction versus explanation, generalisation, and common threats like confounds and data leakage. Establish the "LLM problem-solving loop" students will use all semester to plan, code, verify, and document analyses responsibly.

**Key concepts:** Prediction vs. explanation, generalisation, overfitting (preview), data leakage, the LLM problem-solving loop

**Before next week:** Complete pre-class setup (Python, Jupyter, LLM accounts). Run the test notebook.

---

### Week 2 — Mon 02 Mar 2026 — *Lab + presentations*

**Coding Lab 1: Setup, Plotting, and the LLM Problem-Solving Loop**

Verify setups, introduce Jupyter workflow, and practice the core loop: prompt an LLM for code → run it → verify output → refine. Students work with heavily scaffolded notebooks (fill-in-the-blanks style) to reduce initial friction.

**Group Challenge: Reproduce a Figure**

Given a dataset and a target figure from a published paper, recreate the visualisation using LLM-assisted coding.

*Success criteria:*
- Figure visually matches the target
- Code is clean and commented
- Process is documented (what prompts worked, what didn't)

**LLM skill focus:** Basic prompting — "Write code that does X"

**Student presentations:** 3–4 papers on ML applications in psychology

---

### Week 3 — Mon 09 Mar 2026 — *Lecture*

**Models, Not Magic: Generalisation, Overfitting, and How ML Misleads**

Deepen foundations of supervised learning: targets, features, preprocessing, baselines, and evaluation. Cover train/test splits, cross-validation, bias–variance trade-offs, and how overfitting appears in behavioural datasets. Students learn to choose metrics that match research questions and to interpret performance as evidence, not truth.

**Key concepts:** Training vs. test data, cross-validation, bias-variance trade-off, overfitting, baseline models, evaluation metrics

---

### Week 4 — Mon 16 Mar 2026 — *Lab + presentations*

**Coding Lab 2: Regression Pipeline, Cross-Validation, and Interpretation**

Build end-to-end regression pipelines for linear and regularised models (Ridge/Lasso). Use cross-validation, learning curves, and residual diagnostics to detect misfit. Practice LLM-assisted debugging.

**Group Challenge: Predict & Explain**

Predict a psychological outcome (e.g., test anxiety from survey items) using regression. Groups compete on held-out test performance but must also write a 1-paragraph interpretation connecting coefficients to psychological meaning.

*Success criteria:*
- Working pipeline with cross-validation
- Reasonable predictive performance (compared to baseline)
- Interpretation links statistics to psychological constructs
- Limitations acknowledged

**LLM skill focus:** Debugging — "Here's my error, help me fix it"

**Student presentations:** 3–4 papers on prediction in clinical/educational psychology

---

### Week 5 — Mon 23 Mar 2026 — *Lecture*

**Prediction with Accountability: Classification, Uncertainty, and Evaluation**

Introduce classification for psychological prediction tasks: logistic regression, decision thresholds, and class imbalance. Compare metrics (accuracy, F1, ROC-AUC, PR-AUC) and emphasise calibration and uncertainty. Discuss interpretability and ethical risks of categorising people.

**Key concepts:** Classification, decision thresholds, precision/recall trade-off, class imbalance, calibration, fairness considerations

---

### Week 6 — Mon 30 Mar 2026 — *Lab + presentations*

**Coding Lab 3: Trees, Ensembles, Feature Importance, and Error Analysis**

Implement decision trees and random forests. Focus on practical tuning, cross-validation, and diagnosing failure modes via error analysis and subgroup checks. Use feature importance carefully, noting assumptions.

**Group Challenge: Build a Defensible Classifier**

Classify a meaningful psychological outcome (e.g., treatment response, dropout risk). Groups must:
- Justify their threshold choice with reference to costs of errors
- Report appropriate metrics for imbalanced data
- Discuss one ethical concern with deploying this classifier

*Success criteria:*
- Working classifier with appropriate evaluation
- Threshold choice justified (not just default 0.5)
- Ethical consideration is substantive, not token

**LLM skill focus:** Refactoring — "Make this code cleaner and add verification checks"

**Student presentations:** 3–4 papers on algorithmic fairness or clinical prediction

---

### Mid-Semester Break — 06 Apr 2026 – 19 Apr 2026

No classes. Use this time to consolidate learning and begin working on the written assignment.

---

### Week 7 — Mon 20 Apr 2026 — *Lecture*

**Discovering Structure: Clustering and Dimensionality Reduction Without Self-Deception**

Unsupervised learning for behavioural and cognitive data: clustering (k-means, hierarchical, DBSCAN) and dimensionality reduction (PCA vs. UMAP/t-SNE). Emphasise stability, sensitivity to preprocessing, and the danger of reifying "types."

**Key concepts:** Clustering algorithms, dimensionality reduction, stability analysis, the problem of "discovering" structure you imposed, visualisation vs. inference

**Preview:** Introduce the written assignment dataset and requirements.

---

### Week 8 — Mon 27 Apr 2026 — *Lab + presentations*

**Coding Lab 4: PCA/UMAP, Clustering, and Stability Checks**

Apply dimensionality reduction and clustering to a psychology-relevant dataset. Evaluate cluster solutions using silhouette scores, resampling stability, and qualitative sanity checks.

**Group Challenge: Find Structure, Don't Fabricate It**

Cluster a messy behavioural dataset. Groups must:
- Try multiple approaches and justify their final choice
- Run stability checks (bootstrap resampling, different initialisations)
- Present what they found AND what they're uncertain about

*Success criteria:*
- Multiple methods compared
- Stability assessed quantitatively
- Uncertainty clearly communicated
- No overclaiming of "types" or "subtypes"

**LLM skill focus:** Documentation — "Explain this analysis for a methods section"

**Student presentations:** 3–4 papers on clustering/latent structure in psychopathology or cognition

**WRITTEN ASSIGNMENT DUE: 5:00pm**

---

### Week 9 — Mon 04 May 2026 — *Lecture*

**Learning Representations: Neural Networks as Psychological Tools (and Limits)**

Neural networks as flexible function approximators: perceptrons to multilayer networks, losses, optimisation, and regularisation. Discuss when deep learning helps in psychology/cognitive science (data scale, signal-to-noise) and when simpler models are better. Introduce training diagnostics.

**Key concepts:** Neurons, layers, activation functions, loss functions, gradient descent, overfitting in neural nets, when complexity is warranted

**Preview:** Words as vectors — brief introduction to embeddings as motivation for Week 11

---

### Week 10 — Mon 11 May 2026 — *Lab + presentations*

**Coding Lab 5: Simple Neural Network, Training Diagnostics, and Baseline Comparison**

Build and train a small neural network (MLP) in PyTorch on a behavioural dataset. Compare to classical baselines, tune hyperparameters, and troubleshoot common problems.

**Group Challenge: Beat the Baseline**

Train a neural network that outperforms a logistic regression baseline on a prediction task.

*Success criteria:*
- Neural network trains without crashing
- Fair comparison to baseline (same splits, same metrics)
- Documented what worked and what failed
- Honest assessment: was the complexity worth it?

**LLM skill focus:** Complex debugging — "My loss isn't decreasing, here's my code..."

**Student presentations:** 3–4 papers on deep learning in cognitive modelling or neuroimaging

---

### Week 11 — Mon 18 May 2026 — *Lecture*

**Meaning in Vectors: Embeddings and LLMs for Research Workflows**

Now that students have used LLMs all semester, explain how they work: embeddings, semantic similarity, attention (conceptually), and generation. Cover practical research applications: text clustering, retrieval-augmented search, coding assistance, and literature review. Discuss evaluation strategies and failure modes.

**Key concepts:** Word/sentence embeddings, semantic similarity, how LLMs generate text, retrieval-augmented generation, prompt engineering principles, evaluation and verification

**Reflection:** How has your use of LLM tools evolved over the semester? What have you learned about effective prompting?

---

### Week 12 — Mon 25 May 2026 — *Viva review session*

**Viva Review: Consolidation, Q&A, and Practice Defenses**

No new content. Students rehearse short defenses of their written work:
- Explain your analysis choices
- Justify your model evaluation approach
- Discuss limitations honestly
- Answer targeted questions about leakage, overfitting, interpretation

**Activities:**
- Practice viva questions in pairs
- Common mistakes and how to avoid them
- Q&A on any course concepts
- Exam format guidance

---

### Week 13 — Mon 01 Jun 2026 — *Lecture + discussion*

**What You Can Claim: Limits, Ethics, Reproducibility, and Reasoned Conclusions**

Wrap-up lecture on the boundaries of ML and AI in psychological science. Cover reproducibility, documentation, data governance, privacy, bias, and responsible communication of uncertainty.

**Activities:**
- Critique example claims from published papers
- Identify what evidence actually supports
- Practice writing conclusions that separate prediction from explanation
- Discussion: Where is this field going? What role will you play?

**Key takeaways:**
- Prediction ≠ explanation
- All models are wrong; some are useful
- Uncertainty is not weakness—it's honesty
- LLMs are tools, not oracles
- Your job is to think; the tools help you do it faster

---

## Required Software and Tools

- **Python 3.10+** via Anaconda or similar
- **Jupyter Notebook/Lab**
- **Core libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn, pytorch
- **LLM access:** ChatGPT, Claude, GitHub Copilot, or similar (free tiers are sufficient)

Detailed installation instructions provided on iLearn.

---

## Academic Integrity

Using LLM tools for coding assistance is **encouraged and required** in this course. However:

1. **Document your process** — Note when you used LLM assistance and what prompts worked
2. **Verify all outputs** — You are responsible for code correctness, not the LLM
3. **Write interpretations yourself** — LLMs can help with code; your scientific reasoning must be your own
4. **Individual work is individual** — Group challenges are collaborative; the written assignment interpretation must be yours

Using LLMs to generate your written analysis or interpretation without substantial original thought constitutes academic misconduct.

---

## Support and Resources

- **iLearn:** All materials, datasets, and submission links
- **Discussion forum:** Post questions; help each other
- **Office hours:** [TBD]
- **Technical help:** LLM tools can often debug your code faster than waiting for office hours—try them first!

---

## Weekly Checklist for Students

### Before each lecture week:
- [ ] Review previous week's concepts
- [ ] Complete any assigned readings

### Before each lab week:
- [ ] Ensure your coding environment works
- [ ] Review the challenge brief (posted 48 hours before)
- [ ] Prepare for your presentation (if scheduled)

### After each lab week:
- [ ] Submit group challenge notebook
- [ ] Reflect: What LLM prompts worked? What didn't?
- [ ] Note any concepts to review

---

*Last updated: February 2026*

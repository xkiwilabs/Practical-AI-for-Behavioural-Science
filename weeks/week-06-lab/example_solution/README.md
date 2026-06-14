# Week 6 Example Solution

This folder contains a worked example showing how the Week 6 challenge lab could be completed, including the full classification pipeline from data merging through to threshold analysis and interpretation.

> **Note:** This is an *example* solution, not the only correct one. Students' work will look different — different feature choices, different thresholds, different ethical considerations. The point is to demonstrate the process: plan your approach, build multiple classifiers, compare them properly, justify your decisions, and consider the real-world implications.

## Folder Structure

```
example_solution/
├── README.md                      ← you are here
├── plan.md                        ← initial analysis plan (before coding)
├── plan_final.md                  ← updated plan reflecting what was actually built
├── example_solution.ipynb         ← full notebook workflow (merge → classify → evaluate → interpret)
├── explore_data.py                ← script 1: data loading, merging, and exploration
├── classify_depression.py         ← script 2: full classification pipeline
├── slide.html                     ← example presentation slide (reveal.js)
├── css/
│   └── mq-theme.css               ← slide styling
└── images/
    ├── model_comparison.png       ← bar chart comparing model performance
    ├── feature_importance.png     ← Random Forest feature importances
    ├── roc_curves.png             ← ROC curves for all classifiers
    ├── threshold_analysis.png     ← precision/recall/F1 across thresholds
    ├── confusion_matrices.png     ← confusion matrices at two thresholds
    └── class_distribution.png     ← class balance visualisation
```

## Key Results

Using sleep, mood, personality (Big Five), anxiety (GAD-7), and demographics as features to classify elevated depression (PHQ-9 >= 5):

| Model | Accuracy | F1 | AUC |
|-------|----------|-----|-----|
| Baseline (majority class) | 0.545 | — | — |
| Logistic Regression | 0.815 | 0.827 | 0.911 |
| Decision Tree (depth=5) | 0.804 | 0.811 | 0.871 |
| Random Forest (100 trees) | 0.815 | 0.821 | 0.920 |

The strongest predictors of elevated depression were **PANAS negative affect**, **GAD-7 anxiety**, **stress coping**, **sadness**, and **isolation**. Logistic regression and Random Forest performed similarly, but Random Forest achieved the highest AUC (0.920).

## Running the Code

```bash
conda activate ai-behsci
cd weeks/week-06-lab/example_solution

# Script workflow
python explore_data.py
python classify_depression.py

# View the slide
open slide.html    # macOS
```

The notebook can be opened and run cell-by-cell in VS Code or Jupyter.

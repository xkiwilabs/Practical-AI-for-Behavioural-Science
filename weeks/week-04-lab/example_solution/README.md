# Week 4 Example Solution

This folder contains a worked example showing how the Week 4 challenge lab could be completed, including the full modelling pipeline from data cleaning through to interpretation.

> **Note:** This is an *example* solution, not the only correct one. Students' work will look different — different feature choices, different cleaning decisions, different interpretations. The point is to demonstrate the process: plan your approach, score the variables, build models, compare them, and interpret the results.

## Folder Structure

```
example_solution/
├── README.md                      ← you are here
├── plan.md                        ← initial analysis plan (before coding)
├── plan_final.md                  ← updated plan reflecting what was actually built
├── example_solution.ipynb         ← full notebook workflow (clean → score → model → interpret)
├── explore_data.py                ← script 1: data exploration and summary stats
├── model_and_predict.py           ← script 2: full modelling pipeline
├── slide.html                     ← example presentation slide (reveal.js)
├── css/
│   └── mq-theme.css               ← slide styling
└── images/
    ├── model_comparison.png       ← bar chart comparing model performance
    ├── coefficients.png           ← coefficient plot (which features matter)
    ├── residuals.png              ← residual diagnostic plots
    ├── learning_curves.png        ← bonus: learning curve plot
    └── lasso_path.png             ← bonus: regularisation path
```

## Key Results

Using Big Five personality traits + demographics (age, gender, education, urban, married, familysize) as features:

| Model | CV MAE | CV R² |
|-------|--------|-------|
| Baseline (mean) | 10.59 | ~0.00 |
| Linear Regression | 8.19 | 0.339 |
| Ridge (alpha=1.0) | 8.19 | 0.339 |
| Lasso (alpha=0.1) | 8.20 | 0.339 |

The strongest predictor of depression was **Emotional Stability** (coefficient ≈ −3.4), followed by Extraversion (−1.4) and Conscientiousness (−1.1). This aligns well with decades of personality–psychopathology research.

## Running the Code

```bash
conda activate ai-behsci
cd weeks/week-04-lab/example_solution

# Script workflow
python explore_data.py
python model_and_predict.py

# View the slide
open slide.html    # macOS
```

The notebook can be opened and run cell-by-cell in VS Code or Jupyter.

# Week 2 Example Solution

This folder contains a worked example showing how the Week 2 challenge lab could be completed using both workflows (notebook and scripts), including the exploration-first approach.

> **Note:** This is an *example* solution, not the only correct one. Students' work will look different — different variable choices, different plot types, different findings. The point is to demonstrate the process: explore the data, plan your approach, write focused prompts, and document what you find.

## Folder Structure

```
example_solution/
├── README.md                       ← you are here
├── plan.md                         ← initial analysis plan (before coding)
├── plan_final.md                   ← updated plan reflecting what was actually built
├── example_solution.ipynb          ← notebook workflow (explore → plan → visualise → bonus)
├── explore_data.py                 ← script workflow step 1: explore the data
├── visualise_key_variables.py      ← script workflow step 2: focused visualisation
├── slide.html                      ← example presentation slide (reveal.js)
├── css/
│   └── mq-theme.css                ← slide styling
└── images/
    ├── correlation_heatmap.png     ← exploration: correlation matrix
    ├── pairplot.png                ← exploration: pairwise scatter grid
    ├── our_visualisation.png       ← notebook output: 2×2 scatter plots
    ├── depression_by_gender.png    ← script output: 2×3 gender-split figure
    ├── bonus_group_comparison.png  ← bonus: depression by occupation
    └── bonus_annotated.png         ← bonus: annotated scatter plots
```

## Dataset

The example uses `lifestyle_mental_health.csv` (3,000 participants × 44 variables) which includes:
- Demographics (age, gender, occupation, income, relationship status)
- Lifestyle factors (sleep, exercise, social media, screen time, caffeine, alcohol, study hours)
- DASS-21 scores (Depression, Anxiety, Stress subscales, each 0–42)
- Wellbeing measures (life satisfaction, social support)

## What's Demonstrated

### The exploration-first approach

Both workflows start by **exploring the data before planning** — computing summary statistics, a correlation matrix, and a pairplot. This data-driven exploration reveals which variables are most strongly related to depression, so the visualisation choices are informed rather than guessed.

### Notebook workflow (`example_solution.ipynb`)

Follows the full loop: **Explore → Plan → Engineer prompt → Execute → Verify → Document**, with bonus challenges at the end. All steps are shown as markdown + code cells, modelling how students should structure their notebooks.

### Script workflow (`explore_data.py` + `visualise_key_variables.py`)

Demonstrates the two-script pattern common in data science:
1. `explore_data.py` — run first, produces summary stats and exploration figures
2. `visualise_key_variables.py` — run second, creates the polished visualisation

The plan files (`plan.md` → `plan_final.md`) show how the design evolved.

### Example slide (`slide.html`)

A reveal.js presentation slide with toggle buttons to switch between all outputs (notebook, script, exploration, bonus). Demonstrates how students can present their work using HTML slides.

## Running the Code

```bash
conda activate psyc4411-env
cd weeks/week-02-lab/example_solution

# Script workflow
python explore_data.py
python visualise_key_variables.py

# View the slide
open slide.html    # macOS
# or just double-click slide.html in your file manager
```

The notebook can be opened and run cell-by-cell in VS Code or Jupyter.

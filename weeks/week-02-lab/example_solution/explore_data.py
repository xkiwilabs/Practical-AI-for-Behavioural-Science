"""
Week 2 Example Solution — Explore the Data (Script Workflow)
=============================================================

Step 1 of the script workflow. Before creating a visualisation, we need
to understand the data: what variables are there, what do the distributions
look like, and which variables are most strongly related to depression?

This script produces:
  1. Summary statistics printed to the terminal
  2. A correlation heatmap saved as 'correlation_heatmap.png'
  3. A pairplot of key variables saved as 'pairplot.png'

Run this BEFORE visualise_key_variables.py — the exploration informs
which variables are worth visualising in detail.

Usage:
    conda activate psyc4411-env
    cd weeks/week-02-lab/example_solution
    python explore_data.py
"""

import os
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")  # non-interactive backend for saving files
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("images", exist_ok=True)

# -- Setup -----------------------------------------------------------------
sns.set_theme(style="whitegrid", font_scale=1.1)

# -- Load data -------------------------------------------------------------
data = pd.read_csv("../data/lifestyle_mental_health.csv")
print(f"Loaded {data.shape[0]} participants, {data.shape[1]} variables")
print(f"Columns: {', '.join(data.columns)}\n")

# -- Summary statistics ----------------------------------------------------
print("=" * 60)
print("SUMMARY STATISTICS")
print("=" * 60)
print(data.describe().round(2).to_string())
print()

# Check for missing values
missing = data.isnull().sum()
has_missing = missing[missing > 0]
if len(has_missing) == 0:
    print("No missing values found.")
else:
    print(f"Missing values ({len(has_missing)} columns affected):")
    print(has_missing.to_string())
print()

# -- Correlation analysis --------------------------------------------------
print("=" * 60)
print("CORRELATIONS WITH DASS_DEPRESSION (sorted by strength)")
print("=" * 60)

# Select only lifestyle/demographic variables (not individual DASS items
# or other DASS subscales, which would be circular)
exclude_cols = [c for c in data.columns if c.startswith("DASS_")]
analysis_vars = [c for c in data.select_dtypes(include=[np.number]).columns
                 if c not in exclude_cols]
analysis_vars.append("DASS_Depression")

numeric_subset = data[analysis_vars].dropna()
corr_matrix = numeric_subset.corr().round(3)

# Print correlations with DASS_Depression, sorted by absolute value
dep_corr = corr_matrix["DASS_Depression"].drop("DASS_Depression")
dep_corr_sorted = dep_corr.abs().sort_values(ascending=False)
for var in dep_corr_sorted.index:
    r = dep_corr[var]
    strength = "strong" if abs(r) > 0.3 else "moderate" if abs(r) > 0.15 else "weak"
    print(f"  {var:.<35s} r = {r:+.3f}  ({strength})")

print()
print("Takeaway: Life satisfaction, sleep, and study hours show the strongest")
print("linear correlations with depression. Exercise and social support are")
print("moderate. Some variables (height, weight, siblings) show almost no")
print("association — the data tells us where to focus.")
print()

# -- Figure 1: Correlation heatmap ----------------------------------------
print("Creating correlation heatmap...")

# Use a subset of the most interesting variables for readability
key_analysis_vars = [
    "Sleep_hrs_night", "Exercise_hrs_week", "SocialMedia_hrs_week",
    "Screen_time_hrs_day", "Caffeine_cups_day", "Alcohol_drinks_week",
    "Study_hrs_week", "Social_Support_score", "Income_AUD",
    "Life_satisfaction", "DASS_Depression"
]
key_corr = data[key_analysis_vars].dropna().corr().round(3)

fig_corr, ax_corr = plt.subplots(figsize=(10, 8))
sns.heatmap(
    key_corr, annot=True, fmt=".2f", cmap="RdBu_r", center=0,
    vmin=-1, vmax=1, square=True, linewidths=0.5,
    annot_kws={"size": 9}, ax=ax_corr
)
ax_corr.set_title("Correlation Matrix: Lifestyle Variables and Depression",
                   fontsize=14, fontweight="bold", pad=12)
plt.tight_layout()
fig_corr.savefig("images/correlation_heatmap.png", dpi=300, bbox_inches="tight")
print("  Saved 'images/correlation_heatmap.png'")

# -- Figure 2: Pairplot of key variables ----------------------------------
print("Creating pairplot (this may take a moment)...")

pairplot_vars = ["Sleep_hrs_night", "Exercise_hrs_week", "SocialMedia_hrs_week",
                 "Study_hrs_week", "DASS_Depression"]

pair_grid = sns.pairplot(
    data[pairplot_vars].dropna(), diag_kind="kde",
    plot_kws={"alpha": 0.15, "s": 8},
    height=2.2, aspect=1
)
pair_grid.figure.suptitle("Pairwise Relationships: Key Lifestyle Variables and Depression",
                          fontsize=14, fontweight="bold", y=1.02)
pair_grid.savefig("images/pairplot.png", dpi=300, bbox_inches="tight")
print("  Saved 'images/pairplot.png'")

print()
print("Exploration complete! Review the outputs, then run:")
print("  python visualise_key_variables.py")

"""
Week 2 Example Solution — Script Workflow
==========================================

Step 2 of the script workflow. This script creates a 2x3 figure exploring
how depression scores relate to lifestyle factors, split by gender.

Run explore_data.py first to understand the data, then run this script
to create the focused visualisation based on what the exploration revealed.

Usage:
    conda activate psyc4411-env
    cd weeks/week-02-lab/example_solution
    python explore_data.py              # Step 1: explore
    python visualise_key_variables.py   # Step 2: visualise

Output:
    Saves 'images/depression_by_gender.png'.
"""

import os
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("images", exist_ok=True)

# -- Setup -----------------------------------------------------------------
sns.set_theme(style="whitegrid", font_scale=1.1)

# -- Load data -------------------------------------------------------------
data = pd.read_csv("../data/lifestyle_mental_health.csv")
print(f"Loaded {data.shape[0]} participants, {data.shape[1]} variables")

# Drop rows with missing values in the variables we'll use
plot_vars = ["Sleep_hrs_night", "Exercise_hrs_week", "SocialMedia_hrs_week",
             "DASS_Depression", "Gender"]
data_clean = data.dropna(subset=plot_vars).copy()
print(f"After dropping missing values: {len(data_clean)} participants")

# -- Create the figure -----------------------------------------------------
# A 2x3 grid: top row = scatter plots by gender (sleep, exercise, social media)
#              bottom row = distribution plots (violin + box plots)

fig, axes = plt.subplots(2, 3, figsize=(16, 10))

# Define the three lifestyle variables we're comparing
lifestyle_vars = [
    ("Sleep_hrs_night", "Sleep (hrs/night)"),
    ("Exercise_hrs_week", "Exercise (hrs/week)"),
    ("SocialMedia_hrs_week", "Social Media (hrs/week)"),
]

# -- Top row: Scatter plots coloured by gender -----------------------------
for i, (col, label) in enumerate(lifestyle_vars):
    ax = axes[0, i]
    sns.scatterplot(
        data=data_clean, x=col, y="DASS_Depression", hue="Gender",
        palette={"Male": "#4C72B0", "Female": "#DD8452", "Non-binary": "#55A868"},
        alpha=0.25, s=15, ax=ax, legend=(i == 2)  # legend on last panel only
    )

    # Add separate trend lines for each gender
    for gender, colour in [("Male", "#4C72B0"), ("Female", "#DD8452"),
                           ("Non-binary", "#55A868")]:
        subset = data_clean[data_clean["Gender"] == gender]
        if len(subset) > 10:  # only plot trend line if enough data
            z = np.polyfit(subset[col], subset["DASS_Depression"], 1)
            p = np.poly1d(z)
            x_line = np.linspace(subset[col].min(), subset[col].max(), 100)
            ax.plot(x_line, p(x_line), color=colour, linewidth=2, alpha=0.8)

    ax.set_xlabel(label, fontsize=12)
    ax.set_ylabel("DASS Depression Score" if i == 0 else "", fontsize=12)
    ax.set_title(f"{label} vs Depression", fontsize=14, fontweight="bold")

# Move legend outside the last scatter plot
axes[0, 2].legend(title="Gender", bbox_to_anchor=(1.02, 1), loc="upper left")

# -- Bottom row: Violin plots split by gender ------------------------------
for i, (col, label) in enumerate(lifestyle_vars):
    ax = axes[1, i]

    # Create high/low groups based on median split
    median_val = data_clean[col].median()
    short_label = label.split("(")[0].strip()
    data_clean[f"{col}_group"] = data_clean[col].apply(
        lambda x, lbl=short_label, med=median_val:
            f"High {lbl}" if x >= med else f"Low {lbl}"
    )

    sns.violinplot(
        data=data_clean, x=f"{col}_group", y="DASS_Depression", hue="Gender",
        palette={"Male": "#4C72B0", "Female": "#DD8452", "Non-binary": "#55A868"},
        inner="quart", ax=ax, legend=(i == 2), density_norm="width"
    )

    ax.set_xlabel("", fontsize=12)
    ax.set_ylabel("DASS Depression Score" if i == 0 else "", fontsize=12)
    ax.set_title(f"Depression by {short_label} Level & Gender",
                 fontsize=14, fontweight="bold")

# Move legend outside the last violin plot
axes[1, 2].legend(title="Gender", bbox_to_anchor=(1.02, 1), loc="upper left")

# -- Final touches ---------------------------------------------------------
fig.suptitle(
    "Depression and Lifestyle Factors by Gender",
    fontsize=18, fontweight="bold", y=1.01
)
sns.despine()
plt.tight_layout()

# -- Save ------------------------------------------------------------------
fig.savefig("images/depression_by_gender.png", dpi=300, bbox_inches="tight")
print("Figure saved as 'images/depression_by_gender.png'")

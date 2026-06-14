"""
Week 2 — Starter Script: Visualising Lifestyle and Mental Health
================================================================

This is a starter template for the SCRIPT workflow (Part 2 of the lab).
The imports and data loading are done for you — your AI coding assistant
will help you write the visualisation code.

How to use this file:
    1. First, have your AI create a plan.md file (see README.md for details)
    2. Review and revise the plan until you're happy with it
    3. Have the AI edit THIS file (or create a new .py file) with the code
    4. Run from the terminal:
         conda activate ai-behsci
         python starter.py

Your AI assistant can edit this file directly, create new files alongside it,
or do both — build up your project piece by piece.

Dataset: data/lifestyle_mental_health.csv
    3,000 participants, 44 variables including demographics, lifestyle factors,
    DASS-21 items (Depression, Anxiety, Stress subscales), and life satisfaction.
    There are ~2-3% missing values in the lifestyle columns.
"""

# === IMPORTS ===
# These are the same libraries used in the notebook.
# pandas: for loading and working with data tables
# numpy: for numerical operations (like calculating trend lines)
# matplotlib: for creating plots and figures
# seaborn: for making statistical plots look great with less code

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set some defaults so our plots look nice
sns.set_theme(style="whitegrid", font_scale=1.1)


# === LOAD THE DATA ===
# This reads the CSV file into a pandas DataFrame called 'data'.
# A DataFrame is like a spreadsheet — rows are participants, columns are variables.

data = pd.read_csv("data/lifestyle_mental_health.csv")

print(f"Dataset loaded: {data.shape[0]} participants, {data.shape[1]} variables")
print(f"Columns: {', '.join(data.columns)}")
print()


# === YOUR VISUALISATION CODE GOES BELOW ===
# Have your AI assistant write the visualisation code based on your plan.
# The code should:
#   - Create a figure (e.g., multi-panel scatter plots, box plots, etc.)
#   - Add titles, labels, and any styling
#   - Save the figure as a PNG file
#
# Key variables to explore:
#   Lifestyle: Sleep_hrs_night, Exercise_hrs_week, SocialMedia_hrs_week,
#              Screen_time_hrs_day, Caffeine_cups_day, Alcohol_drinks_week
#   Mental health: DASS_Depression, DASS_Anxiety, DASS_Stress (each 0-42)
#   Wellbeing: Life_satisfaction (1-10), Social_Support_score (1-10)
#   Demographics: Age, Gender, Occupation, Income_AUD
#
# Tip: Ask the AI to implement your plan one step at a time rather than
# all at once. You can always ask it to edit this file again to add more.


# === SAVE THE FIGURE ===
# Uncomment and modify these lines once your figure code is ready:
#
# fig.savefig("our_visualisation.png", dpi=300, bbox_inches="tight")
# print("Figure saved as 'our_visualisation.png'")

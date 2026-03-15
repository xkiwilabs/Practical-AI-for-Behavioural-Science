"""
Week 4 — Starter Script: Predict & Explain — Regression on Real DASS Data
==========================================================================

This is a starter template for the script workflow.
The imports and data loading are done for you — your AI coding assistant
will help you write the modelling code.

How to use this file:
    1. First, have your AI create a plan.md file (see README.md for details)
    2. Review and revise the plan until you're happy with it
    3. Have the AI edit THIS file (or create a new .py file) with the code
    4. Run from the terminal:
         conda activate psyc4411-env
         python starter.py

Your AI assistant can edit this file directly, create new files alongside it,
or do both — build up your project piece by piece.

Dataset: data/dass42_data.csv (tab-separated)
    39,775 respondents, 172 variables including DASS-42 items (Q1A-Q42A),
    Big Five personality (TIPI1-TIPI10), demographics, vocabulary check,
    and item response times. See README.md for full details.
"""

# === IMPORTS ===
# pandas: for loading and working with data tables
# numpy: for numerical operations
# matplotlib + seaborn: for creating plots
# sklearn: for building and evaluating regression models

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.dummy import DummyRegressor

# Set some defaults so our plots look nice
sns.set_theme(style="whitegrid", font_scale=1.1)


# === LOAD THE DATA ===
# This file is tab-separated (not comma-separated), so we need sep="\t"
data = pd.read_csv("data/dass42_data.csv", sep="\t")

print(f"Dataset loaded: {data.shape[0]} respondents, {data.shape[1]} variables")
print(f"First few columns: {list(data.columns[:10])}")
print()


# === BASIC CLEANING ===
# Some ages are clearly wrong (e.g., 1998 — probably a birth year)
# Filter to keep only reasonable ages
data = data[(data["age"] >= 10) & (data["age"] <= 100)]
print(f"After age filter: {len(data)} rows")

# Check for missing values in key columns
dass_cols = [f"Q{i}A" for i in range(1, 43)]
tipi_cols = [f"TIPI{i}" for i in range(1, 11)]
print(f"Missing DASS items: {data[dass_cols].isnull().sum().sum()}")
print(f"Missing TIPI items: {data[tipi_cols].isnull().sum().sum()}")
print()


# === YOUR CODE GOES BELOW ===
# Have your AI assistant help you with the following steps.
# Each step builds on the previous one.

# Step 1: Score the DASS Depression subscale
# The 14 Depression items are: Q3, Q5, Q10, Q13, Q16, Q17, Q21, Q24, Q26, Q31, Q34, Q37, Q38, Q42
# Raw items are coded 1-4; recode to 0-3 (subtract 1) and sum.
# Ask your AI: "How do I recode these DASS items from 1-4 to 0-3 and sum them into a Depression score?"

# dep_items = [f'Q{i}A' for i in [3, 5, 10, 13, 16, 17, 21, 24, 26, 31, 34, 37, 38, 42]]
# data['DASS_Depression'] = ...


# Step 2: Score the Big Five personality traits from the TIPI
# Reverse-score items 2, 4, 6, 8, 10 (reverse = 8 - original)
# Then compute each trait as the average of its two items.
# Ask your AI: "How do I reverse-score TIPI items and compute Big Five scales?"

# Extraversion = (TIPI1 + TIPI6R) / 2
# Agreeableness = (TIPI2R + TIPI7) / 2
# Conscientiousness = (TIPI3 + TIPI8R) / 2
# EmotionalStability = (TIPI4R + TIPI9) / 2
# Openness = (TIPI5 + TIPI10R) / 2


# Step 3: Choose your features and target
# target = "DASS_Depression"
# features = [...]  # start with Big Five, add demographics if you want


# Step 4: Train/test split (80/20)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Step 5: Baseline — predict the mean for everyone
# This is the "dumbest possible model." Any real model should beat this.
# Ask your AI: "How do I calculate baseline MAE and R² when predicting the mean?"


# Step 6: Build models — LinearRegression, Ridge, Lasso
# Use 5-fold cross-validation to evaluate each model.
# Ask your AI: "Show me how to fit and cross-validate Ridge regression with sklearn"


# Step 7: Compare models
# Create a bar chart or table comparing CV MAE and R² across all models.


# Step 8: Interpret coefficients
# Which features have the largest coefficients? What does this mean psychologically?
# Ask your AI: "How do I plot regression coefficients as a horizontal bar chart?"


# Step 9: Final test set evaluation
# Now (and ONLY now) evaluate your best model on the held-out test set.
# Compare test performance to CV performance — a big gap means overfitting.


# Step 10: Save your results
# Uncomment and modify these lines when you're ready:
# fig.savefig("model_comparison.png", dpi=300, bbox_inches="tight")
# print("Figure saved as 'model_comparison.png'")

"""
Week 6 — Starter Script: Build a Defensible Classifier
=======================================================

This is a starter template for the script workflow.
The imports, data loading, aggregation, merging, and target creation
are done for you — your AI coding assistant will help you write the
classification code.

How to use this file:
    1. First, have your AI create a plan.md file (see README.md for details)
    2. Review and revise the plan until you're happy with it
    3. Have the AI edit THIS file (or create a new .py file) with the code
    4. Run from the terminal:
         conda activate ai-behsci
         python starter.py

Dataset: Boston College COVID-19 Sleep & Well-Being Study
    3 CSV files merged into ~836 participants with 21 features.
    Target: elevated depression (PHQ-9 >= 5) vs minimal (< 5).
    See README.md for full details.
"""

# === IMPORTS ===
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (accuracy_score, f1_score, roc_auc_score,
                             precision_score, recall_score, confusion_matrix,
                             classification_report, roc_curve)
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

warnings.filterwarnings('ignore')
sns.set_theme(style="whitegrid", font_scale=1.1)


# === LOAD THE DATA ===
# Three CSV files in the data/boston_college/ folder
data_dir = "data/boston_college"

print("Loading data files...")
daily = pd.read_csv(f"{data_dir}/daily_survey.csv")
demo = pd.read_csv(f"{data_dir}/demographics.csv")
r1 = pd.read_csv(f"{data_dir}/round1_assessment.csv")

print(f"  Daily survey: {daily.shape[0]} entries from {daily.sub_id.nunique()} participants")
print(f"  Demographics: {demo.shape[0]} participants")
print(f"  Round 1:      {r1.shape[0]} entries from {r1.sub_id.nunique()} unique participants")
print()


# === AGGREGATE DAILY SURVEY ===
# Each participant has multiple daily entries. Average them per participant.
agg_cols = ['PHQ9', 'PANAS_PA', 'PANAS_NA', 'TST', 'SE',
            'sleepdiary_sleeplatency', 'sleepdiary_wakes',
            'exercise', 'alcohol_bev', 'isolation', 'stress',
            'worry_scale', 'panas_sad3', 'panas_happy3', 'people_contact']

daily_with_phq = daily[daily['PHQ9'].notna()]
daily_agg = daily_with_phq.groupby('sub_id')[agg_cols].mean()

print(f"After aggregation: {daily_agg.shape[0]} participants with PHQ-9 data")
print()


# === SCORE BIG FIVE PERSONALITY ===
# BFI-2: 30 items, 6 per trait, 1-5 scale
# Some items are reverse-scored (6 - original)
r1_dedup = r1.drop_duplicates(subset='sub_id', keep='first')
print(f"Round 1 after dedup: {r1_dedup.shape[0]} (removed {len(r1) - len(r1_dedup)} duplicates)")


def score_trait(df, pos_items, neg_items):
    """Score a Big Five trait from positive and reverse-scored items."""
    pos = df[[f'big5_{i}' for i in pos_items]].values
    neg = 6 - df[[f'big5_{i}' for i in neg_items]].values
    all_items = np.concatenate([pos, neg], axis=1)
    return np.nanmean(all_items, axis=1)


r1_dedup = r1_dedup.copy()
r1_dedup['Extraversion'] = score_trait(r1_dedup, [1, 11, 21], [6, 16, 26])
r1_dedup['Agreeableness'] = score_trait(r1_dedup, [7, 17, 27], [2, 12, 22])
r1_dedup['Conscientiousness'] = score_trait(r1_dedup, [3, 13, 23], [8, 18, 28])
r1_dedup['Neuroticism'] = score_trait(r1_dedup, [4, 14, 24], [9, 19, 29])
r1_dedup['Openness'] = score_trait(r1_dedup, [5, 15, 25], [10, 20, 30])

# GAD-7 total
gad_cols = [f'gad_{i}' for i in range(1, 8)]
r1_dedup['GAD7_total'] = r1_dedup[gad_cols].sum(axis=1)


# === MERGE DATAFRAMES ===
merged = daily_agg.merge(
    demo[['sub_id', 'age1', 'bio_sex']],
    left_index=True, right_on='sub_id', how='inner'
)
print(f"After merge with demographics: {merged.shape}")

merged = merged.merge(
    r1_dedup[['sub_id', 'Extraversion', 'Agreeableness', 'Conscientiousness',
              'Neuroticism', 'Openness', 'GAD7_total']],
    on='sub_id', how='inner'
)
merged = merged.drop_duplicates(subset='sub_id')
print(f"After merge with Round 1: {merged.shape}")
print()


# === CREATE BINARY TARGET ===
merged['depression_elevated'] = (merged['PHQ9'] >= 5).astype(int)
print("Class balance:")
print(merged['depression_elevated'].value_counts())
print(merged['depression_elevated'].value_counts(normalize=True).round(3))
print()


# === DEFINE FEATURES AND TARGET ===
feature_cols = ['PANAS_PA', 'PANAS_NA', 'TST', 'SE',
                'sleepdiary_sleeplatency', 'sleepdiary_wakes',
                'exercise', 'alcohol_bev', 'isolation', 'stress',
                'worry_scale', 'panas_sad3', 'panas_happy3',
                'age1', 'bio_sex',
                'Extraversion', 'Agreeableness', 'Conscientiousness',
                'Neuroticism', 'Openness', 'GAD7_total']

X = merged[feature_cols].copy()
y = merged['depression_elevated'].copy()

# Handle missing values
imputer = SimpleImputer(strategy='median')
X = pd.DataFrame(imputer.fit_transform(X), columns=feature_cols, index=X.index)

print(f"Features: {len(feature_cols)} columns")
print(f"Samples: {len(X)}")
print(f"Target: {y.value_counts().to_dict()}")
print()


# === YOUR CODE GOES BELOW ===
# Have your AI assistant help you with the following steps.
# Each step builds on the previous one.

# Step 1: Train/test split (80/20, stratified)
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42, stratify=y)


# Step 2: Scale features for logistic regression
# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)


# Step 3: Baseline — always predict the majority class
# Ask your AI: "How do I create a majority-class baseline with DummyClassifier?"


# Step 4: Logistic Regression
# Ask your AI: "How do I fit a LogisticRegression and report accuracy, F1, and AUC?"


# Step 5: Decision Tree (max_depth=5 to prevent overfitting)
# Ask your AI: "How do I fit a DecisionTreeClassifier and plot its confusion matrix?"


# Step 6: Random Forest (100 trees, max_depth=10)
# Ask your AI: "How do I fit a RandomForestClassifier and extract feature importances?"


# Step 7: Compare models
# Create a bar chart or table comparing accuracy, F1, and AUC across all models.


# Step 8: Feature importance
# Plot the top 10 features by Random Forest importance.


# Step 9: Threshold analysis
# Try different thresholds (0.3, 0.4, 0.5, 0.6, 0.7) and see how metrics change.
# Ask your AI: "How do I plot precision and recall as a function of threshold?"


# Step 10: Confusion matrices
# Plot confusion matrices for your best model at different thresholds.


# Step 11: Save your results
# Uncomment when ready:
# fig.savefig("model_comparison.png", dpi=300, bbox_inches="tight")
# print("Figure saved!")

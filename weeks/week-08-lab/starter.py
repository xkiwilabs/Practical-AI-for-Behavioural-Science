"""
Week 8 — Starter Script: Find Structure, Don't Fabricate It
============================================================

This is a starter template for the script workflow.
The imports, data loading, cleaning, and scoring are done for you —
your AI coding assistant will help you write the PCA and clustering code.

How to use this file:
    1. First, have your AI create a plan.md file (see README.md for details)
    2. Review and revise the plan until you're happy with it
    3. Have the AI edit THIS file (or create a new .py file) with the code
    4. Run from the terminal:
         conda activate ai-behsci
         python starter.py

Dataset: data/dass42_data.csv (tab-separated)
    39,775 respondents, 172 variables including DASS-42 items (Q1A-Q42A),
    Big Five personality (TIPI1-TIPI10), demographics, vocabulary check.
    Same data as Week 4 — different question this time.
"""

# === IMPORTS ===
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

warnings.filterwarnings('ignore')
sns.set_theme(style="whitegrid", font_scale=1.1)


# === LOAD THE DATA ===
# Same dataset as Week 4 — tab-separated
data = pd.read_csv("data/dass42_data.csv", sep="\t")

print(f"Dataset loaded: {data.shape[0]:,} respondents, {data.shape[1]} variables")
print()


# === DATA QUALITY FILTERING ===
# 1. Remove unrealistic ages (some are birth years like 1998)
data = data[(data["age"] >= 10) & (data["age"] <= 100)]
print(f"After age filter (10-100): {len(data):,} rows")

# 2. Remove careless responders using vocabulary check items.
# VCL6, VCL9, VCL12 are fake words that don't exist.
# If someone claims to know them (value = 1), they weren't paying attention.
data = data[(data["VCL6"] == 0) & (data["VCL9"] == 0) & (data["VCL12"] == 0)]
print(f"After removing careless responders: {len(data):,} rows")
print()


# === SCORE DASS SUBSCALES ===
# DASS-42: 42 items coded 1-4. Recode to 0-3 (subtract 1), then sum per subscale.
dass_cols = [f"Q{i}A" for i in range(1, 43)]
for col in dass_cols:
    data[col] = data[col] - 1  # Recode 1-4 to 0-3

# Depression: 14 items
dep_items = [f"Q{i}A" for i in [3, 5, 10, 13, 16, 17, 21, 24, 26, 31, 34, 37, 38, 42]]
data["DASS_Depression"] = data[dep_items].sum(axis=1)

# Anxiety: 14 items
anx_items = [f"Q{i}A" for i in [2, 4, 7, 9, 15, 19, 20, 23, 25, 28, 30, 36, 40, 41]]
data["DASS_Anxiety"] = data[anx_items].sum(axis=1)

# Stress: 14 items
str_items = [f"Q{i}A" for i in [1, 6, 8, 11, 12, 14, 18, 22, 27, 29, 32, 33, 35, 39]]
data["DASS_Stress"] = data[str_items].sum(axis=1)

print("DASS subscales scored:")
print(f"  Depression: M={data['DASS_Depression'].mean():.1f}, SD={data['DASS_Depression'].std():.1f}")
print(f"  Anxiety:    M={data['DASS_Anxiety'].mean():.1f}, SD={data['DASS_Anxiety'].std():.1f}")
print(f"  Stress:     M={data['DASS_Stress'].mean():.1f}, SD={data['DASS_Stress'].std():.1f}")
print()


# === SCORE BIG FIVE FROM TIPI ===
# TIPI: 10 items, 2 per trait. Reverse-score items 2, 4, 6, 8, 10.
# Same scoring approach as Week 4: reverse = 8 - original
for i in [2, 4, 6, 8, 10]:
    data[f"TIPI{i}R"] = 8 - data[f"TIPI{i}"]

data["Extraversion"] = (data["TIPI1"] + data["TIPI6R"]) / 2
data["Agreeableness"] = (data["TIPI2R"] + data["TIPI7"]) / 2
data["Conscientiousness"] = (data["TIPI3"] + data["TIPI8R"]) / 2
data["EmotionalStability"] = (data["TIPI4R"] + data["TIPI9"]) / 2
data["Openness"] = (data["TIPI5"] + data["TIPI10R"]) / 2

big5_traits = ["Extraversion", "Agreeableness", "Conscientiousness",
               "EmotionalStability", "Openness"]

print("Big Five scored:")
for trait in big5_traits:
    print(f"  {trait}: M={data[trait].mean():.2f}, SD={data[trait].std():.2f}")
print()


# === SUMMARY ===
print("=" * 60)
print("Your data is ready!")
print(f"  Respondents: {len(data):,}")
print(f"  DASS items (for PCA): {len(dass_cols)} columns")
print(f"  Clustering features: 5 Big Five + 3 DASS subscales = 8")
print("=" * 60)
print()


# === YOUR CODE GOES BELOW ===
# Have your AI assistant help you with the following steps.
# Each step builds on the previous one.

# Step 1: PCA on 42 DASS items
# Standardise the 42 items, fit PCA, create a scree plot.
# Ask your AI: "How do I standardise data and fit PCA with sklearn?"


# Step 2: Examine PCA loadings
# What do the top components represent? Which items load highest?
# Ask your AI: "Show me the top 5 loadings for the first 3 PCA components."


# Step 3: UMAP visualisation
# Create a 2D projection coloured by depression severity.
# Note: install umap-learn first if needed: pip install umap-learn
# Ask your AI: "How do I fit UMAP and create a scatter plot coloured by a variable?"


# Step 4: Cluster participants
# Try k-means with k=2,3,4,5 on standardised Big Five + DASS subscales.
# Plot silhouette scores to choose the best k.
# Ask your AI: "Run k-means for multiple k values and plot silhouette scores."


# Step 5: Profile your clusters
# What does each cluster look like? Plot mean feature values per cluster.
# Ask your AI: "Create a bar chart showing the mean of each feature per cluster."


# Step 6: Stability checks
# Rerun k-means with different random seeds. Do the same people stay together?
# Ask your AI: "How do I check cluster stability across different random seeds?"


# Step 7: Write a methods paragraph
# Ask your AI to draft a methods paragraph for a psychology journal.
# Then verify every detail matches your actual analysis.
# See README.md for the documentation prompt.


# Step 8: Save your results
# Uncomment when ready:
# fig.savefig("scree_plot.png", dpi=300, bbox_inches="tight")
# print("Figure saved!")

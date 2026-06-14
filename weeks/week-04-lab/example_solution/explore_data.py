"""
Week 4 Example Solution — Script 1: Data Exploration
=====================================================

This script loads the OpenPsychometrics DASS-42 dataset, performs basic
cleaning, scores the DASS subscales and TIPI Big Five, and prints summary
statistics. Run this first to understand the data before modelling.

Usage:
    conda activate ai-behsci
    cd weeks/week-04-lab/example_solution
    python explore_data.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", font_scale=1.1)

# ── Load data ────────────────────────────────────────────────────────────────
data = pd.read_csv("../data/dass42_data.csv", sep="\t")
print(f"Raw dataset: {data.shape[0]} rows × {data.shape[1]} columns")
print()

# ── Basic cleaning ───────────────────────────────────────────────────────────
# Filter unreasonable ages
data = data[(data["age"] >= 10) & (data["age"] <= 100)]
print(f"After age filter (10-100): {len(data)} rows")

# Remove careless responders using vocabulary check fake words
fake_words = ["VCL6", "VCL9", "VCL12"]
data["vcl_fake_count"] = data[fake_words].sum(axis=1)
n_careless = (data["vcl_fake_count"] >= 2).sum()
data = data[data["vcl_fake_count"] < 2]
print(f"Removed {n_careless} careless responders (2+ fake words endorsed)")
print(f"Clean dataset: {len(data)} rows")
print()

# ── Score DASS subscales ─────────────────────────────────────────────────────
dep_items = [f"Q{i}A" for i in [3, 5, 10, 13, 16, 17, 21, 24, 26, 31, 34, 37, 38, 42]]
anx_items = [f"Q{i}A" for i in [2, 4, 7, 9, 15, 19, 20, 23, 25, 29, 30, 33, 36, 40]]
stress_items = [f"Q{i}A" for i in [1, 6, 8, 11, 12, 14, 18, 22, 27, 28, 32, 35, 39, 41]]

# Recode 1-4 → 0-3 and sum
data["DASS_Depression"] = data[dep_items].sub(1).sum(axis=1)
data["DASS_Anxiety"] = data[anx_items].sub(1).sum(axis=1)
data["DASS_Stress"] = data[stress_items].sub(1).sum(axis=1)

print("=== DASS Subscale Statistics ===")
for subscale in ["DASS_Depression", "DASS_Anxiety", "DASS_Stress"]:
    print(f"  {subscale}: M={data[subscale].mean():.1f}, SD={data[subscale].std():.1f}, "
          f"Median={data[subscale].median():.0f}, Range=[{data[subscale].min():.0f}, {data[subscale].max():.0f}]")
print()

# ── Score Big Five (TIPI) ────────────────────────────────────────────────────
for i in [2, 4, 6, 8, 10]:
    data[f"TIPI{i}R"] = 8 - data[f"TIPI{i}"]

data["Extraversion"] = (data["TIPI1"] + data["TIPI6R"]) / 2
data["Agreeableness"] = (data["TIPI2R"] + data["TIPI7"]) / 2
data["Conscientiousness"] = (data["TIPI3"] + data["TIPI8R"]) / 2
data["EmotionalStability"] = (data["TIPI4R"] + data["TIPI9"]) / 2
data["Openness"] = (data["TIPI5"] + data["TIPI10R"]) / 2

big5 = ["Extraversion", "Agreeableness", "Conscientiousness", "EmotionalStability", "Openness"]

print("=== Big Five Personality Statistics ===")
for trait in big5:
    print(f"  {trait}: M={data[trait].mean():.2f}, SD={data[trait].std():.2f}")
print()

# ── Correlations with DASS Depression ─────────────────────────────────────────
print("=== Correlations with DASS Depression ===")
all_predictors = big5 + ["age", "gender", "education", "urban", "married", "familysize"]
corrs = data[["DASS_Depression"] + all_predictors].corr()["DASS_Depression"].drop("DASS_Depression")
corrs_sorted = corrs.abs().sort_values(ascending=False)

for var in corrs_sorted.index:
    print(f"  {var:25s}  r = {corrs[var]:+.3f}")
print()

# ── Demographics ──────────────────────────────────────────────────────────────
print("=== Sample Demographics ===")
print(f"  Age: M={data['age'].mean():.1f}, SD={data['age'].std():.1f}, Range=[{data['age'].min()}, {data['age'].max()}]")
gender_map = {1: "Male", 2: "Female", 3: "Other", 0: "Missed"}
print(f"  Gender: {data['gender'].map(gender_map).value_counts().to_dict()}")
print(f"  English native: {(data['engnat'] == 1).sum()} ({(data['engnat'] == 1).mean()*100:.1f}%)")
if "country" in data.columns:
    top_countries = data["country"].value_counts().head(5)
    print(f"  Top countries: {dict(top_countries)}")
print()

# ── Correlation heatmap ──────────────────────────────────────────────────────
print("Generating correlation heatmap...")
fig, ax = plt.subplots(figsize=(10, 8))
corr_vars = big5 + ["age", "education", "DASS_Depression", "DASS_Anxiety", "DASS_Stress"]
corr_matrix = data[corr_vars].corr()
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="RdBu_r", center=0,
            vmin=-1, vmax=1, square=True, ax=ax,
            xticklabels=[v.replace("EmotionalStability", "Emot. Stab.").replace("Conscientiousness", "Conscient.") for v in corr_vars],
            yticklabels=[v.replace("EmotionalStability", "Emot. Stab.").replace("Conscientiousness", "Conscient.") for v in corr_vars])
ax.set_title("Correlation Matrix: Personality, Demographics, and DASS Subscales", fontsize=14, fontweight="bold")
plt.tight_layout()
fig.savefig("images/correlation_heatmap.png", dpi=200, bbox_inches="tight")
plt.close()
print("  Saved: images/correlation_heatmap.png")
print()
print("Exploration complete.")

"""
Week 8 Example Solution — Script 1: PCA & UMAP Exploration
============================================================

This script loads the DASS-42 data, cleans it, scores subscales and
personality, then runs PCA and UMAP to explore the structure of distress.
Generates scree plot, loadings heatmap, and UMAP visualisation.

Usage:
    conda activate psyc4411-env
    cd weeks/week-08-lab/example_solution
    python explore_structure.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import umap

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

sns.set_theme(style="whitegrid", font_scale=1.1)


# ── Load and clean ────────────────────────────────────────────────────────────
data = pd.read_csv("../data/dass42_data.csv", sep="\t")
print(f"Raw dataset: {data.shape[0]:,} respondents")

# Age filter
data = data[(data["age"] >= 10) & (data["age"] <= 100)]
print(f"After age filter (10-100): {len(data):,}")

# Careless responder filter (VCL fake words)
data = data[(data["VCL6"] == 0) & (data["VCL9"] == 0) & (data["VCL12"] == 0)]
print(f"After VCL filter: {len(data):,}")
print()


# ── Score DASS subscales ──────────────────────────────────────────────────────
dass_cols = [f"Q{i}A" for i in range(1, 43)]
for col in dass_cols:
    data[col] = data[col] - 1  # Recode 1-4 to 0-3

dep_items = [f"Q{i}A" for i in [3, 5, 10, 13, 16, 17, 21, 24, 26, 31, 34, 37, 38, 42]]
anx_items = [f"Q{i}A" for i in [2, 4, 7, 9, 15, 19, 20, 23, 25, 28, 30, 36, 40, 41]]
str_items = [f"Q{i}A" for i in [1, 6, 8, 11, 12, 14, 18, 22, 27, 29, 32, 33, 35, 39]]

data["DASS_Depression"] = data[dep_items].sum(axis=1)
data["DASS_Anxiety"] = data[anx_items].sum(axis=1)
data["DASS_Stress"] = data[str_items].sum(axis=1)

print("=== DASS Subscale Statistics ===")
for sub in ["DASS_Depression", "DASS_Anxiety", "DASS_Stress"]:
    print(f"  {sub}: M={data[sub].mean():.1f}, SD={data[sub].std():.1f}")
print()


# ── Score Big Five from TIPI ──────────────────────────────────────────────────
for i in [2, 4, 6, 8, 10]:
    data[f"TIPI{i}R"] = 8 - data[f"TIPI{i}"]

data["Extraversion"] = (data["TIPI1"] + data["TIPI6R"]) / 2
data["Agreeableness"] = (data["TIPI2R"] + data["TIPI7"]) / 2
data["Conscientiousness"] = (data["TIPI3"] + data["TIPI8R"]) / 2
data["EmotionalStability"] = (data["TIPI4R"] + data["TIPI9"]) / 2
data["Openness"] = (data["TIPI5"] + data["TIPI10R"]) / 2

big5 = ["Extraversion", "Agreeableness", "Conscientiousness",
        "EmotionalStability", "Openness"]

print("=== Big Five Statistics ===")
for trait in big5:
    print(f"  {trait}: M={data[trait].mean():.2f}, SD={data[trait].std():.2f}")
print()

print(f"Final dataset: {len(data):,} respondents")
print()


# ═══════════════════════════════════════════════════════════════════════════════
# PCA ON 42 DASS ITEMS
# ═══════════════════════════════════════════════════════════════════════════════

print("=== PCA on 42 DASS Items ===")

# Standardise
scaler = StandardScaler()
X_dass = scaler.fit_transform(data[dass_cols])

# Fit PCA (all 42 components)
pca = PCA(random_state=42)
pca.fit(X_dass)

# Variance explained
var_explained = pca.explained_variance_ratio_
cumulative_var = np.cumsum(var_explained)

print(f"  PC1: {var_explained[0]*100:.2f}%")
print(f"  PC2: {var_explained[1]*100:.2f}%")
print(f"  PC3: {var_explained[2]*100:.2f}%")
print(f"  Cumulative (3 PCs): {cumulative_var[2]*100:.2f}%")
print(f"  Components with eigenvalue > 1: {sum(pca.explained_variance_ > 1)}")
print()


# ── Scree plot ────────────────────────────────────────────────────────────────
print("Generating scree plot...")
fig, ax1 = plt.subplots(figsize=(12, 6))

# Bar chart of individual variance
x = range(1, 16)
ax1.bar(x, var_explained[:15] * 100, color="#4A90D9", edgecolor="white",
        alpha=0.8, label="Individual variance")
ax1.set_xlabel("Principal Component", fontsize=13)
ax1.set_ylabel("Variance Explained (%)", fontsize=13, color="#4A90D9")
ax1.tick_params(axis="y", labelcolor="#4A90D9")
ax1.set_xticks(x)

# Cumulative line on secondary axis
ax2 = ax1.twinx()
ax2.plot(x, cumulative_var[:15] * 100, "o-", color="#A71930", linewidth=2,
         markersize=6, label="Cumulative")
ax2.set_ylabel("Cumulative Variance (%)", fontsize=13, color="#A71930")
ax2.tick_params(axis="y", labelcolor="#A71930")
ax2.set_ylim(0, 100)

# Elbow annotation
ax1.annotate("Elbow: 3 components\ncapture 55% of variance",
             xy=(3, var_explained[2] * 100), xytext=(7, var_explained[0] * 100 - 5),
             fontsize=11, fontweight="bold",
             arrowprops=dict(arrowstyle="->", color="#2D2D2D", lw=1.5))

ax1.set_title("PCA Scree Plot — 42 DASS Items", fontsize=15, fontweight="bold", pad=15)

# Combined legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="center right", fontsize=11)

plt.tight_layout()
fig.savefig("images/scree_plot.png", dpi=200, bbox_inches="tight")
plt.close()
print("  Saved: images/scree_plot.png")
print()


# ── PCA Loadings heatmap ─────────────────────────────────────────────────────
print("Generating loadings heatmap...")

# Get loadings for first 3 components
loadings = pd.DataFrame(
    pca.components_[:3].T,
    columns=["PC1", "PC2", "PC3"],
    index=dass_cols
)

# Create subscale labels for colouring
subscale_map = {}
for item in dep_items:
    subscale_map[item] = "Depression"
for item in anx_items:
    subscale_map[item] = "Anxiety"
for item in str_items:
    subscale_map[item] = "Stress"

# Top loadings for each component
print("\n  Top 5 loadings by component:")
for pc in ["PC1", "PC2", "PC3"]:
    top = loadings[pc].abs().nlargest(5)
    print(f"\n  {pc}:")
    for item, val in top.items():
        actual = loadings.loc[item, pc]
        sub = subscale_map[item]
        print(f"    {item} ({sub}): {actual:+.3f}")

# Heatmap — sort items by subscale for clearer visualisation
item_order = dep_items + anx_items + str_items
loadings_sorted = loadings.loc[item_order]

# Create row colours by subscale
row_colours = [subscale_map[item] for item in item_order]
colour_map = {"Depression": "#A71930", "Anxiety": "#4A90D9", "Stress": "#5BA55B"}
row_colour_values = [colour_map[s] for s in row_colours]

fig, ax = plt.subplots(figsize=(8, 14))
sns.heatmap(loadings_sorted, annot=False, cmap="RdBu_r", center=0,
            xticklabels=True, yticklabels=True, ax=ax,
            cbar_kws={"shrink": 0.5, "label": "Loading"})

# Colour y-axis labels by subscale
for label in ax.get_yticklabels():
    item = label.get_text()
    if item in subscale_map:
        label.set_color(colour_map[subscale_map[item]])
        label.set_fontweight("bold")

ax.set_title("PCA Loadings — First 3 Components\n(items sorted by DASS subscale)",
             fontsize=14, fontweight="bold", pad=10)
ax.set_ylabel("")

# Legend for subscales
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor="#A71930", label="Depression"),
                   Patch(facecolor="#4A90D9", label="Anxiety"),
                   Patch(facecolor="#5BA55B", label="Stress")]
ax.legend(handles=legend_elements, loc="lower right", fontsize=10)

plt.tight_layout()
fig.savefig("images/pca_loadings.png", dpi=200, bbox_inches="tight")
plt.close()
print("\n  Saved: images/pca_loadings.png")
print()


# ═══════════════════════════════════════════════════════════════════════════════
# UMAP VISUALISATION
# ═══════════════════════════════════════════════════════════════════════════════

print("=== UMAP Visualisation ===")
print("  Fitting UMAP (this may take a minute)...")

reducer = umap.UMAP(n_components=2, random_state=42, n_neighbors=15, min_dist=0.1)
embedding = reducer.fit_transform(X_dass)

print(f"  UMAP embedding shape: {embedding.shape}")

fig, ax = plt.subplots(figsize=(12, 8))
scatter = ax.scatter(embedding[:, 0], embedding[:, 1],
                     c=data["DASS_Depression"].values,
                     cmap="RdYlGn_r", s=2, alpha=0.4)
cbar = plt.colorbar(scatter, ax=ax, shrink=0.8)
cbar.set_label("DASS Depression Score (0–42)", fontsize=12)

ax.set_xlabel("UMAP 1", fontsize=13)
ax.set_ylabel("UMAP 2", fontsize=13)
ax.set_title("UMAP Projection of 42 DASS Items — Coloured by Depression Severity",
             fontsize=14, fontweight="bold")

# Warning annotation
ax.text(0.02, 0.02,
        "Warning: distances between clusters are NOT meaningful.\n"
        "Only local structure (nearby points) is trustworthy.",
        transform=ax.transAxes, fontsize=9, fontstyle="italic",
        color="#8C8C8C", verticalalignment="bottom",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

plt.tight_layout()
fig.savefig("images/umap_depression.png", dpi=200, bbox_inches="tight")
plt.close()
print("  Saved: images/umap_depression.png")
print()

print("Exploration complete.")

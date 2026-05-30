"""
Week 8 Example Solution — Script 2: Clustering & Stability
============================================================

This script clusters participants by their Big Five personality and
DASS subscale profiles (8 features), evaluates cluster quality, profiles
the best solution, and checks stability across random seeds.

Usage:
    conda activate psyc4411-env
    cd weeks/week-08-lab/example_solution
    python cluster_profiles.py

Run explore_structure.py first to understand the PCA/UMAP results.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

sns.set_theme(style="whitegrid", font_scale=1.1)


# ═══════════════════════════════════════════════════════════════════════════════
# 1. DATA LOADING AND PREPARATION
# ═══════════════════════════════════════════════════════════════════════════════

data = pd.read_csv("../data/dass42_data.csv", sep="\t")

# Clean
data = data[(data["age"] >= 10) & (data["age"] <= 100)]
data = data[(data["VCL6"] == 0) & (data["VCL9"] == 0) & (data["VCL12"] == 0)]

# Score DASS subscales
dass_cols = [f"Q{i}A" for i in range(1, 43)]
for col in dass_cols:
    data[col] = data[col] - 1

dep_items = [f"Q{i}A" for i in [3, 5, 10, 13, 16, 17, 21, 24, 26, 31, 34, 37, 38, 42]]
anx_items = [f"Q{i}A" for i in [2, 4, 7, 9, 15, 19, 20, 23, 25, 28, 30, 36, 40, 41]]
str_items = [f"Q{i}A" for i in [1, 6, 8, 11, 12, 14, 18, 22, 27, 29, 32, 33, 35, 39]]

data["DASS_Depression"] = data[dep_items].sum(axis=1)
data["DASS_Anxiety"] = data[anx_items].sum(axis=1)
data["DASS_Stress"] = data[str_items].sum(axis=1)

# Score Big Five
for i in [2, 4, 6, 8, 10]:
    data[f"TIPI{i}R"] = 8 - data[f"TIPI{i}"]

data["Extraversion"] = (data["TIPI1"] + data["TIPI6R"]) / 2
data["Agreeableness"] = (data["TIPI2R"] + data["TIPI7"]) / 2
data["Conscientiousness"] = (data["TIPI3"] + data["TIPI8R"]) / 2
data["EmotionalStability"] = (data["TIPI4R"] + data["TIPI9"]) / 2
data["Openness"] = (data["TIPI5"] + data["TIPI10R"]) / 2

print(f"Dataset: {len(data):,} respondents")
print()


# ═══════════════════════════════════════════════════════════════════════════════
# 2. PREPARE CLUSTERING FEATURES
# ═══════════════════════════════════════════════════════════════════════════════

feature_cols = ["Extraversion", "Agreeableness", "Conscientiousness",
                "EmotionalStability", "Openness",
                "DASS_Depression", "DASS_Anxiety", "DASS_Stress"]

X = data[feature_cols].copy()

# Standardise (important for k-means — all features on same scale)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(f"Clustering features: {len(feature_cols)}")
print(f"  Big Five: Extraversion, Agreeableness, Conscientiousness, EmotionalStability, Openness")
print(f"  DASS:     Depression, Anxiety, Stress")
print()


# ═══════════════════════════════════════════════════════════════════════════════
# 3. K-MEANS: EVALUATE MULTIPLE k VALUES
# ═══════════════════════════════════════════════════════════════════════════════

print("=== k-Means Evaluation ===")

k_values = [2, 3, 4, 5, 6]
inertias = []
silhouettes = []

for k in k_values:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(X_scaled)
    inertia = km.inertia_
    sil = silhouette_score(X_scaled, labels)
    inertias.append(inertia)
    silhouettes.append(sil)
    print(f"  k={k}: inertia={inertia:,.0f}, silhouette={sil:.3f}")

print()


# ── Elbow and silhouette plots ───────────────────────────────────────────────
print("Generating elbow and silhouette plots...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Elbow plot
ax1.plot(k_values, inertias, "o-", color="#4A90D9", linewidth=2, markersize=8)
ax1.set_xlabel("Number of Clusters (k)", fontsize=13)
ax1.set_ylabel("Inertia (within-cluster sum of squares)", fontsize=12)
ax1.set_title("Elbow Plot", fontsize=14, fontweight="bold")
ax1.set_xticks(k_values)

# Silhouette plot
colours = ["#5BA55B" if s == max(silhouettes) else "#4A90D9" for s in silhouettes]
bars = ax2.bar(k_values, silhouettes, color=colours, edgecolor="white", linewidth=0.5)
ax2.set_xlabel("Number of Clusters (k)", fontsize=13)
ax2.set_ylabel("Silhouette Score", fontsize=13)
ax2.set_title("Silhouette Score by k", fontsize=14, fontweight="bold")
ax2.set_xticks(k_values)

# Annotate best k
best_idx = silhouettes.index(max(silhouettes))
best_k = k_values[best_idx]
ax2.annotate(f"Best: k={best_k}\n(silhouette={max(silhouettes):.3f})",
             xy=(best_k, max(silhouettes)), xytext=(best_k + 1.2, max(silhouettes)),
             fontsize=11, fontweight="bold",
             arrowprops=dict(arrowstyle="->", color="#2D2D2D", lw=1.5))

plt.tight_layout()
fig.savefig("images/elbow_silhouette.png", dpi=200, bbox_inches="tight")
plt.close()
print("  Saved: images/elbow_silhouette.png")
print()


# ═══════════════════════════════════════════════════════════════════════════════
# 4. PROFILE THE BEST CLUSTER SOLUTION (k=2)
# ═══════════════════════════════════════════════════════════════════════════════

print(f"=== Cluster Profiles (k={best_k}) ===")

km_best = KMeans(n_clusters=best_k, random_state=42, n_init=10)
data["cluster"] = km_best.fit_predict(X_scaled)

# Profile: mean raw values per cluster
profile = data.groupby("cluster")[feature_cols].mean()
print("\nCluster means (raw values):")
print(profile.round(2).to_string())
print()

# Cluster sizes
for c in range(best_k):
    n = (data["cluster"] == c).sum()
    pct = n / len(data) * 100
    print(f"  Cluster {c}: N={n:,} ({pct:.1f}%)")
print()


# ── Cluster profile bar chart ────────────────────────────────────────────────
print("Generating cluster profiles chart...")

# Use standardised means for better visualisation
profile_std = pd.DataFrame(
    scaler.inverse_transform(
        pd.DataFrame(
            [X_scaled[data["cluster"] == c].mean(axis=0) for c in range(best_k)],
            columns=feature_cols
        ).values
    ),
    columns=feature_cols
)
# Actually, let's just use z-scores for the chart
profile_z = pd.DataFrame(
    [X_scaled[data["cluster"] == c].mean(axis=0) for c in range(best_k)],
    columns=feature_cols
)

# Determine labels based on distress levels
cluster_labels = []
for c in range(best_k):
    dep_mean = profile.loc[c, "DASS_Depression"]
    if dep_mean < 15:
        cluster_labels.append(f"Cluster {c}: Low Distress")
    else:
        cluster_labels.append(f"Cluster {c}: High Distress")

fig, ax = plt.subplots(figsize=(14, 6))
x = np.arange(len(feature_cols))
width = 0.35

colours = ["#5BA55B", "#A71930", "#4A90D9", "#C8972C"]
for c in range(best_k):
    offset = (c - (best_k - 1) / 2) * width
    ax.bar(x + offset, profile_z.iloc[c], width,
           label=cluster_labels[c], color=colours[c], edgecolor="white",
           alpha=0.85)

ax.set_xlabel("Feature", fontsize=13)
ax.set_ylabel("Standardised Mean (z-score)", fontsize=13)
ax.set_title(f"Cluster Profiles (k={best_k}) — Standardised Feature Means",
             fontsize=14, fontweight="bold")
ax.set_xticks(x)
ax.set_xticklabels([c.replace("DASS_", "") for c in feature_cols],
                   rotation=30, ha="right", fontsize=11)
ax.axhline(y=0, color="grey", linewidth=0.8, linestyle="--")
ax.legend(fontsize=11)

plt.tight_layout()
fig.savefig("images/cluster_profiles.png", dpi=200, bbox_inches="tight")
plt.close()
print("  Saved: images/cluster_profiles.png")
print()


# ═══════════════════════════════════════════════════════════════════════════════
# 5. STABILITY CHECKS
# ═══════════════════════════════════════════════════════════════════════════════

print("=== Stability Checks ===")

# Reference: seed=42 labels
ref_labels = data["cluster"].values

seeds = [0, 123, 456, 789, 2026]
stability_results = []

for seed in seeds:
    km_test = KMeans(n_clusters=best_k, random_state=seed, n_init=10)
    test_labels = km_test.fit_predict(X_scaled)

    # Since cluster labels can be permuted, find the best alignment
    # by checking if flipping gives better agreement
    match_same = np.sum(ref_labels == test_labels)
    match_flip = np.sum(ref_labels != test_labels)
    best_match = max(match_same, match_flip)
    agreement = best_match / len(ref_labels) * 100
    changed = 100 - agreement

    stability_results.append({
        "seed": seed,
        "agreement": agreement,
        "changed_pct": changed
    })
    print(f"  Seed {seed:4d}: {agreement:.2f}% agreement ({changed:.2f}% changed cluster)")

stability_df = pd.DataFrame(stability_results)
avg_agreement = stability_df["agreement"].mean()
print(f"\n  Average agreement: {avg_agreement:.2f}%")
print()


# ── Stability bar chart ──────────────────────────────────────────────────────
print("Generating stability chart...")

fig, ax = plt.subplots(figsize=(10, 5))

bars = ax.bar([f"Seed {s['seed']}" for s in stability_results],
              [s["agreement"] for s in stability_results],
              color="#5BA55B", edgecolor="white", alpha=0.85)

ax.set_ylabel("Agreement with Reference (%)", fontsize=13)
ax.set_title(f"Cluster Stability — k={best_k} across Different Random Seeds",
             fontsize=14, fontweight="bold")
ax.set_ylim(95, 100.5)

# Annotate each bar
for bar, result in zip(bars, stability_results):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1,
            f"{result['agreement']:.1f}%", ha="center", fontsize=11, fontweight="bold")

# Verdict box
verdict = "Very stable" if avg_agreement > 99 else "Moderately stable"
ax.text(0.98, 0.05, f"Verdict: {verdict}\nAvg agreement: {avg_agreement:.1f}%",
        transform=ax.transAxes, fontsize=11, ha="right", va="bottom",
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#5BA55B", alpha=0.15))

plt.tight_layout()
fig.savefig("images/stability_check.png", dpi=200, bbox_inches="tight")
plt.close()
print("  Saved: images/stability_check.png")
print()


# ═══════════════════════════════════════════════════════════════════════════════
# 6. SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"  Respondents: {len(data):,}")
print(f"  Features: {len(feature_cols)} (5 Big Five + 3 DASS subscales)")
print(f"  Best k: {best_k} (silhouette = {max(silhouettes):.3f})")
for c in range(best_k):
    n = (data["cluster"] == c).sum()
    dep = profile.loc[c, "DASS_Depression"]
    anx = profile.loc[c, "DASS_Anxiety"]
    stress = profile.loc[c, "DASS_Stress"]
    print(f"  Cluster {c} (N={n:,}): Depression={dep:.1f}, Anxiety={anx:.1f}, Stress={stress:.1f}")
print(f"  Stability: {avg_agreement:.1f}% average agreement across {len(seeds)} seeds")
print("=" * 60)
print()
print("Clustering complete.")

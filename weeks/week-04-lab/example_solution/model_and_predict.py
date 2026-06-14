"""
Week 4 Example Solution — Script 2: Modelling Pipeline
=======================================================

This script builds and compares regression models for predicting DASS
Depression from Big Five personality and demographics. Generates all
visualisations for the example solution.

Usage:
    conda activate ai-behsci
    cd weeks/week-04-lab/example_solution
    python model_and_predict.py

Run explore_data.py first to understand the dataset.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, cross_val_score, learning_curve
from sklearn.linear_model import LinearRegression, Ridge, Lasso, lasso_path
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.dummy import DummyRegressor

sns.set_theme(style="whitegrid", font_scale=1.1)


# ═══════════════════════════════════════════════════════════════════════════════
# 1. DATA LOADING AND PREPARATION
# ═══════════════════════════════════════════════════════════════════════════════

data = pd.read_csv("../data/dass42_data.csv", sep="\t")

# Clean: filter ages and careless responders
data = data[(data["age"] >= 10) & (data["age"] <= 100)]
fake_words = ["VCL6", "VCL9", "VCL12"]
data["vcl_fake_count"] = data[fake_words].sum(axis=1)
data = data[data["vcl_fake_count"] < 2]

# Score DASS Depression (14 items, recode 1-4 → 0-3, sum)
dep_items = [f"Q{i}A" for i in [3, 5, 10, 13, 16, 17, 21, 24, 26, 31, 34, 37, 38, 42]]
data["DASS_Depression"] = data[dep_items].sub(1).sum(axis=1)

# Score Big Five personality (TIPI)
for i in [2, 4, 6, 8, 10]:
    data[f"TIPI{i}R"] = 8 - data[f"TIPI{i}"]

data["Extraversion"] = (data["TIPI1"] + data["TIPI6R"]) / 2
data["Agreeableness"] = (data["TIPI2R"] + data["TIPI7"]) / 2
data["Conscientiousness"] = (data["TIPI3"] + data["TIPI8R"]) / 2
data["EmotionalStability"] = (data["TIPI4R"] + data["TIPI9"]) / 2
data["Openness"] = (data["TIPI5"] + data["TIPI10R"]) / 2

print(f"Clean dataset: {len(data)} rows")
print(f"DASS Depression: M={data['DASS_Depression'].mean():.2f}, SD={data['DASS_Depression'].std():.2f}")
print()


# ═══════════════════════════════════════════════════════════════════════════════
# 2. FEATURE SELECTION AND SPLITTING
# ═══════════════════════════════════════════════════════════════════════════════

big5 = ["Extraversion", "Agreeableness", "Conscientiousness", "EmotionalStability", "Openness"]
demographics = ["age", "gender", "education", "urban", "married", "familysize"]
features = big5 + demographics

# Drop any rows with missing values in features or target
model_data = data[features + ["DASS_Depression"]].dropna()
X = model_data[features]
y = model_data["DASS_Depression"]

# 80/20 train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Features: {features}")
print(f"Training set: {len(X_train)} rows")
print(f"Test set: {len(X_test)} rows")
print()


# ═══════════════════════════════════════════════════════════════════════════════
# 3. BASELINE MODEL
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("MODEL COMPARISON (5-fold cross-validation)")
print("=" * 60)

# Baseline: predict the mean
baseline = DummyRegressor(strategy="mean")
baseline_cv_mae = -cross_val_score(baseline, X_train, y_train, cv=5, scoring="neg_mean_absolute_error")
baseline_cv_r2 = cross_val_score(baseline, X_train, y_train, cv=5, scoring="r2")
baseline.fit(X_train, y_train)

print(f"\nBaseline (mean prediction):")
print(f"  Train mean: {y_train.mean():.2f}")
print(f"  CV MAE: {baseline_cv_mae.mean():.2f} ± {baseline_cv_mae.std():.2f}")
print(f"  CV R²:  {baseline_cv_r2.mean():.4f}")


# ═══════════════════════════════════════════════════════════════════════════════
# 4. BUILD AND EVALUATE MODELS
# ═══════════════════════════════════════════════════════════════════════════════

models = {
    "Linear Regression": LinearRegression(),
    "Ridge (alpha=1.0)": Ridge(alpha=1.0),
    "Lasso (alpha=0.1)": Lasso(alpha=0.1, max_iter=10000),
}

results = {
    "Model": ["Baseline (mean)"],
    "CV MAE": [baseline_cv_mae.mean()],
    "CV R²": [baseline_cv_r2.mean()],
    "Train R²": [baseline.score(X_train, y_train)],
}

for name, model in models.items():
    cv_mae = -cross_val_score(model, X_train, y_train, cv=5, scoring="neg_mean_absolute_error")
    cv_r2 = cross_val_score(model, X_train, y_train, cv=5, scoring="r2")
    model.fit(X_train, y_train)
    train_r2 = model.score(X_train, y_train)

    results["Model"].append(name)
    results["CV MAE"].append(cv_mae.mean())
    results["CV R²"].append(cv_r2.mean())
    results["Train R²"].append(train_r2)

    print(f"\n{name}:")
    print(f"  CV MAE: {cv_mae.mean():.2f} ± {cv_mae.std():.2f}")
    print(f"  CV R²:  {cv_r2.mean():.4f} ± {cv_r2.std():.4f}")
    print(f"  Train R²: {train_r2:.4f}")

results_df = pd.DataFrame(results)
print("\n" + results_df.to_string(index=False))


# ═══════════════════════════════════════════════════════════════════════════════
# 5. MODEL COMPARISON PLOT
# ═══════════════════════════════════════════════════════════════════════════════

print("\nGenerating model comparison plot...")
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

colours = ["#8C8C8C", "#4A90D9", "#5BA55B", "#E8873D"]

# MAE comparison
axes[0].bar(results_df["Model"], results_df["CV MAE"], color=colours, edgecolor="white", linewidth=0.5)
axes[0].set_ylabel("Cross-Validated MAE", fontsize=12)
axes[0].set_title("Model Comparison: Mean Absolute Error", fontsize=14, fontweight="bold")
axes[0].tick_params(axis="x", rotation=20)
for i, v in enumerate(results_df["CV MAE"]):
    axes[0].text(i, v + 0.1, f"{v:.2f}", ha="center", fontsize=10, fontweight="bold")

# R² comparison
axes[1].bar(results_df["Model"], results_df["CV R²"], color=colours, edgecolor="white", linewidth=0.5)
axes[1].set_ylabel("Cross-Validated R²", fontsize=12)
axes[1].set_title("Model Comparison: R² (Variance Explained)", fontsize=14, fontweight="bold")
axes[1].tick_params(axis="x", rotation=20)
for i, v in enumerate(results_df["CV R²"]):
    axes[1].text(i, v + 0.005, f"{v:.3f}", ha="center", fontsize=10, fontweight="bold")

plt.tight_layout()
fig.savefig("images/model_comparison.png", dpi=200, bbox_inches="tight")
plt.close()
print("  Saved: images/model_comparison.png")


# ═══════════════════════════════════════════════════════════════════════════════
# 6. COEFFICIENT ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════

print("\nGenerating coefficient plot...")
lr_model = models["Linear Regression"]
coefs = pd.Series(lr_model.coef_, index=features)
coefs_sorted = coefs.sort_values()

fig, ax = plt.subplots(figsize=(10, 6))
bar_colours = ["#A71930" if c < 0 else "#4A90D9" for c in coefs_sorted]
coefs_sorted.plot(kind="barh", ax=ax, color=bar_colours, edgecolor="white", linewidth=0.5)
ax.set_xlabel("Coefficient Value", fontsize=12)
ax.set_title("Regression Coefficients: What Predicts Depression?", fontsize=14, fontweight="bold")
ax.axvline(x=0, color="black", linewidth=0.8, linestyle="-")

# Add value labels
for i, (val, name) in enumerate(zip(coefs_sorted, coefs_sorted.index)):
    offset = -0.15 if val < 0 else 0.05
    ax.text(val + offset, i, f"{val:.2f}", va="center", fontsize=9, fontweight="bold")

plt.tight_layout()
fig.savefig("images/coefficients.png", dpi=200, bbox_inches="tight")
plt.close()
print("  Saved: images/coefficients.png")

print("\nCoefficients (Linear Regression):")
for feat, coef in sorted(zip(features, lr_model.coef_), key=lambda x: abs(x[1]), reverse=True):
    print(f"  {feat:25s} {coef:+.3f}")


# ═══════════════════════════════════════════════════════════════════════════════
# 7. FINAL TEST SET EVALUATION
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("FINAL TEST SET EVALUATION")
print("=" * 60)

best_model = models["Linear Regression"]  # All models are nearly identical
y_pred = best_model.predict(X_test)
test_mae = mean_absolute_error(y_test, y_pred)
test_r2 = r2_score(y_test, y_pred)

print(f"\nBest model: Linear Regression")
print(f"  Test MAE: {test_mae:.2f}")
print(f"  Test R²:  {test_r2:.4f}")
print(f"  (CV R² was {results_df.loc[results_df['Model'] == 'Linear Regression', 'CV R²'].values[0]:.4f})")
print(f"  Gap: {abs(results_df.loc[results_df['Model'] == 'Linear Regression', 'CV R²'].values[0] - test_r2):.4f}")
print(f"  → Minimal gap = no overfitting")


# ═══════════════════════════════════════════════════════════════════════════════
# 8. RESIDUAL PLOTS
# ═══════════════════════════════════════════════════════════════════════════════

print("\nGenerating residual plots...")
residuals = y_test - y_pred

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Predicted vs Actual
axes[0].scatter(y_pred, y_test, alpha=0.1, s=5, color="#4A90D9")
axes[0].plot([0, 42], [0, 42], "r--", linewidth=2, label="Perfect prediction")
axes[0].set_xlabel("Predicted Depression Score", fontsize=12)
axes[0].set_ylabel("Actual Depression Score", fontsize=12)
axes[0].set_title("Predicted vs Actual", fontsize=14, fontweight="bold")
axes[0].legend()

# Residuals vs Predicted
axes[1].scatter(y_pred, residuals, alpha=0.1, s=5, color="#E8873D")
axes[1].axhline(y=0, color="red", linewidth=2, linestyle="--")
axes[1].set_xlabel("Predicted Depression Score", fontsize=12)
axes[1].set_ylabel("Residual (Actual - Predicted)", fontsize=12)
axes[1].set_title("Residuals vs Predicted", fontsize=14, fontweight="bold")

plt.tight_layout()
fig.savefig("images/residuals.png", dpi=200, bbox_inches="tight")
plt.close()
print("  Saved: images/residuals.png")


# ═══════════════════════════════════════════════════════════════════════════════
# 9. BONUS: LEARNING CURVES
# ═══════════════════════════════════════════════════════════════════════════════

print("\nGenerating learning curves...")
train_sizes, train_scores, val_scores = learning_curve(
    LinearRegression(), X_train, y_train,
    train_sizes=np.linspace(0.1, 1.0, 10),
    cv=5, scoring="neg_mean_absolute_error",
    n_jobs=-1
)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(train_sizes, -train_scores.mean(axis=1), "o-", color="#4A90D9", label="Training MAE")
ax.fill_between(train_sizes,
                -train_scores.mean(axis=1) - train_scores.std(axis=1),
                -train_scores.mean(axis=1) + train_scores.std(axis=1),
                alpha=0.1, color="#4A90D9")
ax.plot(train_sizes, -val_scores.mean(axis=1), "o-", color="#A71930", label="Validation MAE")
ax.fill_between(train_sizes,
                -val_scores.mean(axis=1) - val_scores.std(axis=1),
                -val_scores.mean(axis=1) + val_scores.std(axis=1),
                alpha=0.1, color="#A71930")
ax.set_xlabel("Training Set Size", fontsize=12)
ax.set_ylabel("Mean Absolute Error", fontsize=12)
ax.set_title("Learning Curves: Linear Regression", fontsize=14, fontweight="bold")
ax.legend(fontsize=11)
plt.tight_layout()
fig.savefig("images/learning_curves.png", dpi=200, bbox_inches="tight")
plt.close()
print("  Saved: images/learning_curves.png")


# ═══════════════════════════════════════════════════════════════════════════════
# 10. BONUS: LASSO REGULARISATION PATH
# ═══════════════════════════════════════════════════════════════════════════════

print("\nGenerating Lasso regularisation path...")
alphas_lasso, coefs_path, _ = lasso_path(X_train, y_train, alphas=np.logspace(-2, 1, 50))

fig, ax = plt.subplots(figsize=(10, 6))
feature_colours = ["#4A90D9", "#5BA55B", "#E8873D", "#A71930", "#7B68A8",
                    "#8C8C8C", "#C8972C", "#2D2D2D", "#D4533B", "#4A90D9", "#5BA55B"]
for i, feat in enumerate(features):
    ax.plot(alphas_lasso, coefs_path[i], label=feat, color=feature_colours[i % len(feature_colours)], linewidth=2)

ax.set_xscale("log")
ax.set_xlabel("Lasso Alpha (regularisation strength)", fontsize=12)
ax.set_ylabel("Coefficient Value", fontsize=12)
ax.set_title("Lasso Path: How Coefficients Change with Regularisation", fontsize=14, fontweight="bold")
ax.axhline(y=0, color="black", linewidth=0.5, linestyle=":")
ax.legend(fontsize=8, loc="upper right", ncol=2)
plt.tight_layout()
fig.savefig("images/lasso_path.png", dpi=200, bbox_inches="tight")
plt.close()
print("  Saved: images/lasso_path.png")

print("\nAll plots saved to images/")
print("Done.")

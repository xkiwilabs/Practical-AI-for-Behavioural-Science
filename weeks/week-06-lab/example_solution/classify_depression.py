"""
Week 6 Example Solution — Script 2: Classification Pipeline
============================================================

This script builds and compares classifiers for predicting elevated
depression (PHQ-9 >= 5) from sleep, mood, personality, and demographics.
Generates all visualisations for the example solution.

Usage:
    conda activate ai-behsci
    cd weeks/week-06-lab/example_solution
    python classify_depression.py

Run explore_data.py first to understand the dataset.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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

sns.set_theme(style="whitegrid", font_scale=1.1)


# ═══════════════════════════════════════════════════════════════════════════════
# 1. DATA LOADING AND PREPARATION
# ═══════════════════════════════════════════════════════════════════════════════

data_dir = "../data/boston_college"

# Load
daily = pd.read_csv(f"{data_dir}/daily_survey.csv")
demo = pd.read_csv(f"{data_dir}/demographics.csv")
r1 = pd.read_csv(f"{data_dir}/round1_assessment.csv")

# Aggregate daily survey per participant
agg_cols = ['PHQ9', 'PANAS_PA', 'PANAS_NA', 'TST', 'SE',
            'sleepdiary_sleeplatency', 'sleepdiary_wakes',
            'exercise', 'alcohol_bev', 'isolation', 'stress',
            'worry_scale', 'panas_sad3', 'panas_happy3', 'people_contact']

daily_with_phq = daily[daily['PHQ9'].notna()]
daily_agg = daily_with_phq.groupby('sub_id')[agg_cols].mean()

# Score Big Five personality
r1_dedup = r1.drop_duplicates(subset='sub_id', keep='first').copy()


def score_trait(df, pos_items, neg_items):
    """Score a Big Five trait from positive and reverse-scored items."""
    pos = df[[f'big5_{i}' for i in pos_items]].values
    neg = 6 - df[[f'big5_{i}' for i in neg_items]].values
    all_items = np.concatenate([pos, neg], axis=1)
    return np.nanmean(all_items, axis=1)


r1_dedup['Extraversion'] = score_trait(r1_dedup, [1, 11, 21], [6, 16, 26])
r1_dedup['Agreeableness'] = score_trait(r1_dedup, [7, 17, 27], [2, 12, 22])
r1_dedup['Conscientiousness'] = score_trait(r1_dedup, [3, 13, 23], [8, 18, 28])
r1_dedup['Neuroticism'] = score_trait(r1_dedup, [4, 14, 24], [9, 19, 29])
r1_dedup['Openness'] = score_trait(r1_dedup, [5, 15, 25], [10, 20, 30])

gad_cols = [f'gad_{i}' for i in range(1, 8)]
r1_dedup['GAD7_total'] = r1_dedup[gad_cols].sum(axis=1)

# Merge
merged = daily_agg.merge(
    demo[['sub_id', 'age1', 'bio_sex']],
    left_index=True, right_on='sub_id', how='inner'
)
merged = merged.merge(
    r1_dedup[['sub_id', 'Extraversion', 'Agreeableness', 'Conscientiousness',
              'Neuroticism', 'Openness', 'GAD7_total']],
    on='sub_id', how='inner'
)
merged = merged.drop_duplicates(subset='sub_id')

# Create binary target
merged['depression_elevated'] = (merged['PHQ9'] >= 5).astype(int)

print(f"Dataset: {len(merged)} participants")
print(f"Class balance: {merged['depression_elevated'].value_counts().to_dict()}")
print()


# ═══════════════════════════════════════════════════════════════════════════════
# 2. FEATURES AND SPLITTING
# ═══════════════════════════════════════════════════════════════════════════════

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

# Stratified train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# Scale features (for logistic regression)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"Features: {len(feature_cols)}")
print(f"Training set: {len(X_train)}")
print(f"Test set: {len(X_test)}")
print()


# ═══════════════════════════════════════════════════════════════════════════════
# 3. HELPER FUNCTION (the refactoring win)
# ═══════════════════════════════════════════════════════════════════════════════

def evaluate_model(model, X_tr, X_te, y_tr, y_te, name="Model"):
    """Fit a model and return a dictionary of classification metrics.

    This function was created by refactoring — originally we had the same
    block of code repeated four times. Now it's one function.
    """
    model.fit(X_tr, y_tr)
    y_pred = model.predict(X_te)

    metrics = {
        'name': name,
        'accuracy': accuracy_score(y_te, y_pred),
        'f1': f1_score(y_te, y_pred),
        'precision': precision_score(y_te, y_pred),
        'recall': recall_score(y_te, y_pred),
    }

    # AUC requires probability predictions (baseline doesn't have predict_proba)
    if hasattr(model, 'predict_proba'):
        y_prob = model.predict_proba(X_te)[:, 1]
        metrics['auc'] = roc_auc_score(y_te, y_prob)
    else:
        metrics['auc'] = None

    return metrics


# ═══════════════════════════════════════════════════════════════════════════════
# 4. BUILD AND EVALUATE MODELS
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("MODEL COMPARISON")
print("=" * 60)

# Baseline: majority class
baseline = DummyClassifier(strategy='most_frequent')
baseline_metrics = evaluate_model(baseline, X_train, X_test, y_train, y_test, "Baseline")
print(f"\n{baseline_metrics['name']}:")
print(f"  Accuracy: {baseline_metrics['accuracy']:.3f}")

# Logistic Regression (uses scaled features)
lr = LogisticRegression(max_iter=1000, random_state=42)
lr_metrics = evaluate_model(lr, X_train_scaled, X_test_scaled, y_train, y_test, "Logistic Regression")
print(f"\n{lr_metrics['name']}:")
print(f"  Accuracy: {lr_metrics['accuracy']:.3f}, F1: {lr_metrics['f1']:.3f}, AUC: {lr_metrics['auc']:.3f}")

# Decision Tree
dt = DecisionTreeClassifier(max_depth=5, random_state=42)
dt_metrics = evaluate_model(dt, X_train, X_test, y_train, y_test, "Decision Tree")
print(f"\n{dt_metrics['name']}:")
print(f"  Accuracy: {dt_metrics['accuracy']:.3f}, F1: {dt_metrics['f1']:.3f}, AUC: {dt_metrics['auc']:.3f}")

# Random Forest
rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
rf_metrics = evaluate_model(rf, X_train, X_test, y_train, y_test, "Random Forest")
print(f"\n{rf_metrics['name']}:")
print(f"  Accuracy: {rf_metrics['accuracy']:.3f}, F1: {rf_metrics['f1']:.3f}, AUC: {rf_metrics['auc']:.3f}")

# Cross-validation for the best models
print("\n\nCross-validation (5-fold):")
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

lr_cv = LogisticRegression(max_iter=1000, random_state=42)
lr_cv_scores = cross_val_score(lr_cv, scaler.fit_transform(X), y, cv=cv, scoring='accuracy')
print(f"  Logistic Regression: {lr_cv_scores.mean():.3f} +/- {lr_cv_scores.std():.3f}")

dt_cv_scores = cross_val_score(DecisionTreeClassifier(max_depth=5, random_state=42),
                                X, y, cv=cv, scoring='accuracy')
print(f"  Decision Tree: {dt_cv_scores.mean():.3f} +/- {dt_cv_scores.std():.3f}")

rf_cv_scores = cross_val_score(RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42),
                                X, y, cv=cv, scoring='accuracy')
print(f"  Random Forest: {rf_cv_scores.mean():.3f} +/- {rf_cv_scores.std():.3f}")

# Collect all results
all_metrics = [baseline_metrics, lr_metrics, dt_metrics, rf_metrics]
results_df = pd.DataFrame(all_metrics)
print("\n" + results_df.to_string(index=False))


# ═══════════════════════════════════════════════════════════════════════════════
# 5. MODEL COMPARISON PLOT
# ═══════════════════════════════════════════════════════════════════════════════

print("\nGenerating model comparison plot...")
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
colours = ['#8C8C8C', '#4A90D9', '#5BA55B', '#E8873D']
model_names = [m['name'] for m in all_metrics]

# Accuracy
axes[0].bar(model_names, [m['accuracy'] for m in all_metrics],
            color=colours, edgecolor='white', linewidth=0.5)
axes[0].set_ylabel('Accuracy', fontsize=12)
axes[0].set_title('Accuracy', fontsize=14, fontweight='bold')
axes[0].tick_params(axis='x', rotation=15)
axes[0].set_ylim(0.4, 0.9)
for i, m in enumerate(all_metrics):
    axes[0].text(i, m['accuracy'] + 0.01, f"{m['accuracy']:.3f}",
                 ha='center', fontsize=10, fontweight='bold')

# F1
f1_vals = [m['f1'] if m['name'] != 'Baseline' else 0 for m in all_metrics]
axes[1].bar(model_names, f1_vals, color=colours, edgecolor='white', linewidth=0.5)
axes[1].set_ylabel('F1 Score', fontsize=12)
axes[1].set_title('F1 Score', fontsize=14, fontweight='bold')
axes[1].tick_params(axis='x', rotation=15)
axes[1].set_ylim(0, 0.95)
for i, (m, v) in enumerate(zip(all_metrics, f1_vals)):
    if v > 0:
        axes[1].text(i, v + 0.01, f"{v:.3f}", ha='center', fontsize=10, fontweight='bold')

# AUC
auc_vals = [m['auc'] if m['auc'] is not None else 0 for m in all_metrics]
axes[2].bar(model_names, auc_vals, color=colours, edgecolor='white', linewidth=0.5)
axes[2].set_ylabel('AUC', fontsize=12)
axes[2].set_title('Area Under ROC Curve', fontsize=14, fontweight='bold')
axes[2].tick_params(axis='x', rotation=15)
axes[2].set_ylim(0, 1.0)
for i, (m, v) in enumerate(zip(all_metrics, auc_vals)):
    if v > 0:
        axes[2].text(i, v + 0.01, f"{v:.3f}", ha='center', fontsize=10, fontweight='bold')

plt.tight_layout()
fig.savefig("images/model_comparison.png", dpi=200, bbox_inches="tight")
plt.close()
print("  Saved: images/model_comparison.png")


# ═══════════════════════════════════════════════════════════════════════════════
# 6. FEATURE IMPORTANCE
# ═══════════════════════════════════════════════════════════════════════════════

print("\nGenerating feature importance plot...")

# Random Forest importances
importances = pd.Series(rf.feature_importances_, index=feature_cols)
importances_sorted = importances.sort_values(ascending=True)

fig, ax = plt.subplots(figsize=(10, 8))
bar_colours = ['#4A90D9' if v >= importances.quantile(0.75) else '#8C8C8C'
               for v in importances_sorted]
importances_sorted.plot(kind='barh', ax=ax, color=bar_colours, edgecolor='white', linewidth=0.5)
ax.set_xlabel('Feature Importance (Gini)', fontsize=12)
ax.set_title('Random Forest Feature Importance: What Predicts Depression?',
             fontsize=14, fontweight='bold')

# Add value labels
for i, (val, name) in enumerate(zip(importances_sorted, importances_sorted.index)):
    ax.text(val + 0.002, i, f"{val:.3f}", va='center', fontsize=9, fontweight='bold')

plt.tight_layout()
fig.savefig("images/feature_importance.png", dpi=200, bbox_inches="tight")
plt.close()
print("  Saved: images/feature_importance.png")

print("\nTop 10 features (Random Forest):")
for feat, imp in importances.sort_values(ascending=False).head(10).items():
    print(f"  {feat:30s} {imp:.3f}")

print("\nLogistic Regression coefficients (absolute, standardised):")
lr_coefs = pd.Series(np.abs(lr.coef_[0]), index=feature_cols)
for feat, coef in lr_coefs.sort_values(ascending=False).head(10).items():
    sign = '+' if lr.coef_[0][feature_cols.index(feat)] > 0 else '-'
    print(f"  {feat:30s} {sign}{coef:.3f}")


# ═══════════════════════════════════════════════════════════════════════════════
# 7. ROC CURVES
# ═══════════════════════════════════════════════════════════════════════════════

print("\nGenerating ROC curves...")

fig, ax = plt.subplots(figsize=(8, 8))

# Logistic Regression
lr_probs = lr.predict_proba(X_test_scaled)[:, 1]
fpr_lr, tpr_lr, _ = roc_curve(y_test, lr_probs)
ax.plot(fpr_lr, tpr_lr, color='#4A90D9', linewidth=2,
        label=f'Logistic Regression (AUC = {lr_metrics["auc"]:.3f})')

# Decision Tree
dt_probs = dt.predict_proba(X_test)[:, 1]
fpr_dt, tpr_dt, _ = roc_curve(y_test, dt_probs)
ax.plot(fpr_dt, tpr_dt, color='#5BA55B', linewidth=2,
        label=f'Decision Tree (AUC = {dt_metrics["auc"]:.3f})')

# Random Forest
rf_probs = rf.predict_proba(X_test)[:, 1]
fpr_rf, tpr_rf, _ = roc_curve(y_test, rf_probs)
ax.plot(fpr_rf, tpr_rf, color='#E8873D', linewidth=2,
        label=f'Random Forest (AUC = {rf_metrics["auc"]:.3f})')

# Random baseline
ax.plot([0, 1], [0, 1], 'k--', linewidth=1, label='Random (AUC = 0.500)')

ax.set_xlabel('False Positive Rate', fontsize=12)
ax.set_ylabel('True Positive Rate', fontsize=12)
ax.set_title('ROC Curves: All Classifiers', fontsize=14, fontweight='bold')
ax.legend(loc='lower right', fontsize=11)
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(-0.02, 1.02)

plt.tight_layout()
fig.savefig("images/roc_curves.png", dpi=200, bbox_inches="tight")
plt.close()
print("  Saved: images/roc_curves.png")


# ═══════════════════════════════════════════════════════════════════════════════
# 8. THRESHOLD ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════

print("\nGenerating threshold analysis...")

# Use Random Forest probabilities (best AUC)
thresholds = np.arange(0.1, 0.91, 0.01)
precisions = []
recalls = []
f1s = []

for t in thresholds:
    y_pred_t = (rf_probs >= t).astype(int)
    if y_pred_t.sum() == 0 or y_pred_t.sum() == len(y_pred_t):
        precisions.append(np.nan)
        recalls.append(np.nan)
        f1s.append(np.nan)
    else:
        precisions.append(precision_score(y_test, y_pred_t))
        recalls.append(recall_score(y_test, y_pred_t))
        f1s.append(f1_score(y_test, y_pred_t))

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(thresholds, precisions, color='#4A90D9', linewidth=2, label='Precision')
ax.plot(thresholds, recalls, color='#A71930', linewidth=2, label='Recall')
ax.plot(thresholds, f1s, color='#5BA55B', linewidth=2, label='F1 Score')
ax.axvline(x=0.5, color='grey', linewidth=1, linestyle='--', alpha=0.7, label='Default (0.5)')
ax.axvline(x=0.3, color='#E8873D', linewidth=1, linestyle='--', alpha=0.7, label='Screening (0.3)')

ax.set_xlabel('Classification Threshold', fontsize=12)
ax.set_ylabel('Score', fontsize=12)
ax.set_title('Threshold Analysis: Random Forest', fontsize=14, fontweight='bold')
ax.legend(fontsize=11, loc='center left')
ax.set_xlim(0.1, 0.9)
ax.set_ylim(0, 1.05)

plt.tight_layout()
fig.savefig("images/threshold_analysis.png", dpi=200, bbox_inches="tight")
plt.close()
print("  Saved: images/threshold_analysis.png")

# Print specific thresholds
print("\nThreshold comparison:")
for t in [0.3, 0.4, 0.5, 0.6, 0.7]:
    y_pred_t = (rf_probs >= t).astype(int)
    p = precision_score(y_test, y_pred_t) if y_pred_t.sum() > 0 else 0
    r = recall_score(y_test, y_pred_t) if y_pred_t.sum() > 0 else 0
    f = f1_score(y_test, y_pred_t) if y_pred_t.sum() > 0 else 0
    print(f"  Threshold {t}: Precision={p:.3f}, Recall={r:.3f}, F1={f:.3f}")


# ═══════════════════════════════════════════════════════════════════════════════
# 9. CONFUSION MATRICES
# ═══════════════════════════════════════════════════════════════════════════════

print("\nGenerating confusion matrices...")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

for ax, threshold, title in zip(axes, [0.3, 0.5],
                                 ['Threshold = 0.3 (Screening)', 'Threshold = 0.5 (Default)']):
    y_pred_t = (rf_probs >= threshold).astype(int)
    cm = confusion_matrix(y_test, y_pred_t)

    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax,
                xticklabels=['Minimal', 'Elevated'],
                yticklabels=['Minimal', 'Elevated'],
                annot_kws={'size': 16, 'fontweight': 'bold'})
    ax.set_xlabel('Predicted', fontsize=12)
    ax.set_ylabel('Actual', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')

    # Add metrics below
    p = precision_score(y_test, y_pred_t)
    r = recall_score(y_test, y_pred_t)
    f = f1_score(y_test, y_pred_t)
    ax.text(0.5, -0.15, f'Precision={p:.2f}  Recall={r:.2f}  F1={f:.2f}',
            transform=ax.transAxes, ha='center', fontsize=11, color='#333')

plt.tight_layout()
fig.savefig("images/confusion_matrices.png", dpi=200, bbox_inches="tight")
plt.close()
print("  Saved: images/confusion_matrices.png")


# ═══════════════════════════════════════════════════════════════════════════════
# 10. FULL CLASSIFICATION REPORT
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("FULL CLASSIFICATION REPORT (Random Forest, threshold=0.5)")
print("=" * 60)
y_pred_final = rf.predict(X_test)
print(classification_report(y_test, y_pred_final, target_names=['Minimal', 'Elevated']))

print("\nAll plots saved to images/")
print("Done.")

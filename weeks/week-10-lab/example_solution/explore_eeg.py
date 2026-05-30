"""
Week 10 Example Solution — Script 1: Explore EEG Data
======================================================

This script loads and explores the pre-extracted EEG motor imagery features.
Run this to understand the data before building any models.

Usage:
    conda activate psyc4411-env
    python example_solution/explore_eeg.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings

warnings.filterwarnings('ignore')
sns.set_theme(style='whitegrid', font_scale=1.1)

# Paths
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
IMG_DIR = Path(__file__).resolve().parent / "images"
IMG_DIR.mkdir(exist_ok=True)


# === LOAD DATA ===
print("=" * 60)
print("Loading EEG Motor Imagery Features")
print("=" * 60)
print()

data = pd.read_csv(DATA_DIR / "eeg_motor_imagery_features.csv")

print(f"Dataset shape: {data.shape[0]:,} trials × {data.shape[1]} columns")
print(f"Participants:  {data['participant_id'].nunique()}")
print(f"Trials per participant: {data.groupby('participant_id').size().describe().to_string()}")
print()


# === CLASS BALANCE ===
print("=" * 60)
print("Class Balance")
print("=" * 60)
print()

balance = data['condition'].value_counts()
print(balance)
print()
print(f"  Left:  {balance.get('left', 0):,}  ({balance.get('left', 0)/len(data)*100:.1f}%)")
print(f"  Right: {balance.get('right', 0):,} ({balance.get('right', 0)/len(data)*100:.1f}%)")
print()


# === FEATURE OVERVIEW ===
feature_cols = [c for c in data.columns
                if c not in ['participant_id', 'trial', 'condition', 'condition_code']]
print("=" * 60)
print("Feature Overview")
print("=" * 60)
print()
print(f"Number of features: {len(feature_cols)}")
print(f"Feature value range: {data[feature_cols].min().min():.6f} to {data[feature_cols].max().max():.6f}")
print()

# Extract channel and band info
channels = sorted(set(col.rsplit('_', 1)[0] for col in feature_cols))
bands = sorted(set(col.rsplit('_', 1)[1] for col in feature_cols))
print(f"Channels ({len(channels)}): {', '.join(channels[:10])}...")
print(f"Bands ({len(bands)}): {', '.join(bands)}")
print()


# === KEY CHANNELS: C3 and C4 ===
print("=" * 60)
print("Motor Cortex Channels: C3 (left) and C4 (right)")
print("=" * 60)
print()

# C3 and C4 are the motor cortex channels most relevant for left/right imagery
motor_features = [c for c in feature_cols if c.startswith(('C3_', 'C4_'))]
print(f"Motor cortex features: {motor_features}")
print()

# Mean power by condition for motor channels
for ch in ['C3', 'C4']:
    print(f"\n{ch} (mean power by condition):")
    for band in ['alpha', 'beta']:
        col = f"{ch}_{band}"
        if col in data.columns:
            left_mean = data[data['condition'] == 'left'][col].mean()
            right_mean = data[data['condition'] == 'right'][col].mean()
            diff = right_mean - left_mean
            print(f"  {band:>5}: Left={left_mean:.6f}, Right={right_mean:.6f}, Diff={diff:+.6f}")


# === MISSING VALUES ===
print()
print("=" * 60)
print("Data Quality")
print("=" * 60)
print()

missing = data[feature_cols].isnull().sum().sum()
print(f"Missing values: {missing}")
print(f"Infinite values: {np.isinf(data[feature_cols].values).sum()}")
print()


# === PLOT 1: Class Balance ===
fig, ax = plt.subplots(figsize=(6, 4))
colours = ['#4A90D9', '#A71930']
data['condition'].value_counts().plot(kind='bar', color=colours, ax=ax, edgecolor='white')
ax.set_title('Class Balance: Left vs Right Motor Imagery', fontsize=14, fontweight='bold')
ax.set_ylabel('Number of trials')
ax.set_xticklabels(['Left hand', 'Right hand'], rotation=0)

# Add count labels
for i, (label, count) in enumerate(data['condition'].value_counts().items()):
    ax.text(i, count + 30, f'{count:,}', ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig(IMG_DIR / "class_balance.png", dpi=150, bbox_inches='tight')
plt.show()
print("Saved: images/class_balance.png")


# === PLOT 2: Feature Distributions — Motor Cortex Alpha/Beta ===
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
motor_cols = ['C3_alpha', 'C4_alpha', 'C3_beta', 'C4_beta']
titles = ['C3 Alpha (left motor cortex)', 'C4 Alpha (right motor cortex)',
          'C3 Beta (left motor cortex)', 'C4 Beta (right motor cortex)']

for ax, col, title in zip(axes.flat, motor_cols, titles):
    if col in data.columns:
        for condition, colour in zip(['left', 'right'], colours):
            subset = data[data['condition'] == condition][col]
            ax.hist(subset, bins=40, alpha=0.6, color=colour, label=f'{condition.title()} hand',
                    edgecolor='white', linewidth=0.5)
        ax.set_title(title, fontsize=11, fontweight='bold')
        ax.set_xlabel('Band power')
        ax.set_ylabel('Count')
        ax.legend(fontsize=9)

plt.suptitle('Motor Cortex Feature Distributions by Condition', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(IMG_DIR / "motor_cortex_distributions.png", dpi=150, bbox_inches='tight')
plt.show()
print("Saved: images/motor_cortex_distributions.png")


# === SUMMARY ===
print()
print("=" * 60)
print("Summary")
print("=" * 60)
print()
print(f"  Trials:       {data.shape[0]:,}")
print(f"  Participants: {data['participant_id'].nunique()}")
print(f"  Features:     {len(feature_cols)}")
print(f"  Classes:      2 (left/right, balanced)")
print(f"  Missing:      {missing}")
print()
print("The distributions for left and right motor imagery overlap heavily.")
print("This confirms the signal is weak — expect ~60% accuracy at best.")
print("Key channels: C3 (left motor cortex) and C4 (right motor cortex).")
print()

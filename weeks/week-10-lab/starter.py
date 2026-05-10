"""
Week 10 — Starter Script: Beat the Baseline
=============================================

This is a starter template for the script workflow.
The imports, data loading, exploration, and preparation are done for you —
your AI coding assistant will help you write the neural network code.

How to use this file:
    1. First, have your AI create a plan.md file (see README.md for details)
    2. Review and revise the plan until you're happy with it
    3. Have the AI edit THIS file (or create a new .py file) with the code
    4. Run from the terminal:
         conda activate psyc4411-env
         python starter.py

Dataset: data/eeg_motor_imagery_features.csv
    4,918 trials from 109 participants, 324 columns.
    Pre-extracted EEG band power features for motor imagery classification
    (left vs right imagined hand movement).
"""

# === IMPORTS ===
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, classification_report

# PyTorch imports — new this week!
import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader

warnings.filterwarnings('ignore')
sns.set_theme(style="whitegrid", font_scale=1.1)


# === LOAD THE DATA ===
data = pd.read_csv("data/eeg_motor_imagery_features.csv")

print(f"Dataset loaded: {data.shape[0]:,} trials, {data.shape[1]} columns")
print(f"Participants: {data['participant_id'].nunique()}")
print()


# === EXPLORE THE DATA ===
# Class balance
print("Class balance:")
print(data['condition'].value_counts())
print(f"  Left:  {(data['condition'] == 'left').sum():,}  ({(data['condition'] == 'left').mean()*100:.1f}%)")
print(f"  Right: {(data['condition'] == 'right').sum():,} ({(data['condition'] == 'right').mean()*100:.1f}%)")
print()

# Feature summary
feature_cols = [c for c in data.columns
                if c not in ['participant_id', 'trial', 'condition', 'condition_code']]
print(f"Number of features: {len(feature_cols)}")
print(f"Feature value range: {data[feature_cols].min().min():.6f} to {data[feature_cols].max().max():.6f}")
print()


# === PREPARE DATA ===
X = data[feature_cols].values
y = data['condition_code'].values

# Stratified 80/20 split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"Train: {len(X_train):,} trials")
print(f"Test:  {len(X_test):,} trials")

# Standardise features (critical for neural networks!)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Use train stats only!

print(f"Features standardised: mean≈{X_train_scaled.mean():.4f}, std≈{X_train_scaled.std():.4f}")
print()


# ═══════════════════════════════════════════════════════════════════
# YOUR CODE STARTS HERE
# ═══════════════════════════════════════════════════════════════════

# Phase 1: Logistic Regression Baseline
# ──────────────────────────────────────
# TODO: Fit LogisticRegression on X_train_scaled, y_train
# TODO: Predict on X_test_scaled
# TODO: Report accuracy and F1


# Phase 2: Build and Train a Neural Network
# ──────────────────────────────────────────
# TODO: Convert X_train_scaled and X_test_scaled to FloatTensors
# TODO: Convert y_train and y_test to LongTensors
# TODO: Wrap the training tensors in a TensorDataset and a DataLoader
#       (batch_size=32, shuffle=True) — this is the inner "batch loop"
#       from the Week 9 lecture flow chart
# TODO: Set torch.manual_seed(42) for reproducibility
# TODO: Define a SimpleNN class (nn.Module) with:
#   - Linear(320, 64), ReLU, Dropout(0.3), Linear(64, 2)
# TODO: Set up CrossEntropyLoss and Adam optimizer (lr=0.001)
# TODO: Training loop for 50 epochs — outer epoch loop + inner batch loop
#       Track BOTH train_losses (mean over batches) AND val_losses
#       (no-grad evaluation on test set each epoch)
# TODO: Plot both loss curves on the same axes, with ln(2) reference line


# Phase 3: Compare and Reflect
# ─────────────────────────────
# TODO: Evaluate MLP on test set (accuracy, F1)
# TODO: Print comparison: LogReg vs MLP
# TODO: Plot confusion matrices side by side
# TODO: Was the neural network worth it?

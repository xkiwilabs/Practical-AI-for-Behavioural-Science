"""
Week 10 Example Solution — Script 2: Train Classifier
=====================================================

This script builds and compares a logistic regression baseline with a
PyTorch neural network (MLP) for EEG motor imagery classification.

Usage:
    conda activate ai-behsci
    python example_solution/train_classifier.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, f1_score, confusion_matrix,
                             classification_report, ConfusionMatrixDisplay)

import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader

warnings.filterwarnings('ignore')
sns.set_theme(style='whitegrid', font_scale=1.1)

# Paths
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
IMG_DIR = Path(__file__).resolve().parent / "images"
IMG_DIR.mkdir(exist_ok=True)


# ═══════════════════════════════════════════════════════════════════
# SECTION 1: Load and Prepare Data
# ═══════════════════════════════════════════════════════════════════
print("=" * 60)
print("Loading and Preparing Data")
print("=" * 60)
print()

data = pd.read_csv(DATA_DIR / "eeg_motor_imagery_features.csv")

feature_cols = [c for c in data.columns
                if c not in ['participant_id', 'trial', 'condition', 'condition_code']]

X = data[feature_cols].values
y = data['condition_code'].values

# Stratified 80/20 split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Train: {len(X_train):,} trials")
print(f"Test:  {len(X_test):,} trials")
print(f"Features: {X_train.shape[1]}")

# Standardise
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"Features standardised: mean={X_train_scaled.mean():.6f}, std={X_train_scaled.std():.6f}")
print()


# ═══════════════════════════════════════════════════════════════════
# SECTION 2: Logistic Regression Baseline
# ═══════════════════════════════════════════════════════════════════
print("=" * 60)
print("Phase 1: Logistic Regression Baseline")
print("=" * 60)
print()

lr_model = LogisticRegression(max_iter=1000, random_state=42)
lr_model.fit(X_train_scaled, y_train)
lr_pred = lr_model.predict(X_test_scaled)

lr_acc = accuracy_score(y_test, lr_pred)
lr_f1 = f1_score(y_test, lr_pred)

print(f"Logistic Regression:")
print(f"  Accuracy: {lr_acc:.3f}")
print(f"  F1 Score: {lr_f1:.3f}")
print()
print("Classification Report:")
print(classification_report(y_test, lr_pred, target_names=['Left', 'Right']))
print()


# ═══════════════════════════════════════════════════════════════════
# SECTION 3: Neural Network — Define and Train
# ═══════════════════════════════════════════════════════════════════
print("=" * 60)
print("Phase 2: PyTorch Neural Network (MLP)")
print("=" * 60)
print()

# Convert to PyTorch tensors and create a DataLoader for the inner batch loop
X_train_tensor = torch.FloatTensor(X_train_scaled)
y_train_tensor = torch.LongTensor(y_train)
X_test_tensor = torch.FloatTensor(X_test_scaled)
y_test_tensor = torch.LongTensor(y_test)

batch_size = 32
train_loader = DataLoader(
    TensorDataset(X_train_tensor, y_train_tensor),
    batch_size=batch_size,
    shuffle=True,
)

print(f"Tensor shapes: X_train={X_train_tensor.shape}, y_train={y_train_tensor.shape}")
print(f"DataLoader:    {len(train_loader)} batches of {batch_size}")


# Define the neural network
class SimpleNN(nn.Module):
    """Simple MLP: 320 → 64 → 2 with ReLU and Dropout."""
    def __init__(self, n_features):
        super().__init__()
        self.layer1 = nn.Linear(n_features, 64)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.3)
        self.output = nn.Linear(64, 2)

    def forward(self, x):
        x = self.dropout(self.relu(self.layer1(x)))
        return self.output(x)


# Set random seed for reproducibility
torch.manual_seed(42)

n_features = X_train_scaled.shape[1]
model = SimpleNN(n_features)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

print(f"\nModel architecture:")
print(model)
print(f"Total parameters: {sum(p.numel() for p in model.parameters()):,}")
print()

# Training loop — nested epoch + batch loops
n_epochs = 50
train_losses = []
val_losses = []

print(f"Training for {n_epochs} epochs (mini-batches of {batch_size})...")
print()

for epoch in range(n_epochs):
    # ----- outer EPOCH loop -----
    model.train()
    running_loss = 0.0
    for X_batch, y_batch in train_loader:
        # ----- inner BATCH loop -----
        optimizer.zero_grad()
        outputs = model(X_batch)
        loss = criterion(outputs, y_batch)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    train_losses.append(running_loss / len(train_loader))

    # After all batches: measure validation loss
    model.eval()
    with torch.no_grad():
        val_outputs = model(X_test_tensor)
        val_loss = criterion(val_outputs, y_test_tensor)
        val_losses.append(val_loss.item())

    if (epoch + 1) % 10 == 0:
        print(f"  Epoch {epoch+1:3d}/{n_epochs}: "
              f"Train loss={train_losses[-1]:.4f}, "
              f"Val loss={val_losses[-1]:.4f}")

print()


# ═══════════════════════════════════════════════════════════════════
# SECTION 4: Evaluate Neural Network
# ═══════════════════════════════════════════════════════════════════
print("=" * 60)
print("Phase 3: Evaluate and Compare")
print("=" * 60)
print()

model.eval()
with torch.no_grad():
    test_outputs = model(X_test_tensor)
    nn_pred = test_outputs.argmax(dim=1).numpy()

nn_acc = accuracy_score(y_test, nn_pred)
nn_f1 = f1_score(y_test, nn_pred)

print(f"Neural Network (MLP):")
print(f"  Accuracy: {nn_acc:.3f}")
print(f"  F1 Score: {nn_f1:.3f}")
print()
print("Classification Report:")
print(classification_report(y_test, nn_pred, target_names=['Left', 'Right']))
print()


# ═══════════════════════════════════════════════════════════════════
# SECTION 5: Model Comparison
# ═══════════════════════════════════════════════════════════════════
print("=" * 60)
print("Model Comparison")
print("=" * 60)
print()
print(f"{'Model':<25} {'Accuracy':>10} {'F1':>10}")
print("-" * 47)
print(f"{'Random guessing':<25} {'0.500':>10} {'—':>10}")
print(f"{'Logistic Regression':<25} {lr_acc:>10.3f} {lr_f1:>10.3f}")
print(f"{'Simple MLP (1 hidden)':<25} {nn_acc:>10.3f} {nn_f1:>10.3f}")
print()

diff = nn_acc - lr_acc
if diff > 0.005:
    print(f"MLP improvement: +{diff:.3f} accuracy ({diff*100:.1f} percentage points)")
elif diff < -0.005:
    print(f"MLP was WORSE by {abs(diff):.3f} accuracy ({abs(diff)*100:.1f} percentage points)")
else:
    print("MLP and LogReg performed about the same.")
print()


# ═══════════════════════════════════════════════════════════════════
# PLOT 1: Training Loss Curve
# ═══════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(train_losses, label='Training loss', color='#4A90D9', linewidth=2)
ax.plot(val_losses, label='Validation loss', color='#A71930', linewidth=2)
ax.axhline(y=np.log(2), color='gray', linestyle='--', linewidth=1,
           label=f'Random guessing (ln(2) = {np.log(2):.3f})')
ax.set_xlabel('Epoch', fontsize=12)
ax.set_ylabel('Loss (CrossEntropy)', fontsize=12)
ax.set_title('Training and Validation Loss Curves', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.set_xlim(0, n_epochs)

plt.tight_layout()
plt.savefig(IMG_DIR / "loss_curves.png", dpi=150, bbox_inches='tight')
plt.show()
print("Saved: images/loss_curves.png")
print()


# ═══════════════════════════════════════════════════════════════════
# PLOT 2: Model Comparison Bar Chart
# ═══════════════════════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

models = ['Logistic\nRegression', 'Simple\nMLP']
colours = ['#4A90D9', '#A71930']

# Accuracy
axes[0].bar(models, [lr_acc, nn_acc], color=colours, edgecolor='white', width=0.6)
axes[0].axhline(y=0.5, color='gray', linestyle='--', linewidth=1, label='Chance (50%)')
axes[0].set_ylabel('Accuracy')
axes[0].set_title('Accuracy', fontsize=12, fontweight='bold')
axes[0].set_ylim(0.4, 0.75)
axes[0].legend(fontsize=9)
for i, v in enumerate([lr_acc, nn_acc]):
    axes[0].text(i, v + 0.008, f'{v:.3f}', ha='center', fontweight='bold', fontsize=11)

# F1
axes[1].bar(models, [lr_f1, nn_f1], color=colours, edgecolor='white', width=0.6)
axes[1].set_ylabel('F1 Score')
axes[1].set_title('F1 Score', fontsize=12, fontweight='bold')
axes[1].set_ylim(0.4, 0.75)
for i, v in enumerate([lr_f1, nn_f1]):
    axes[1].text(i, v + 0.008, f'{v:.3f}', ha='center', fontweight='bold', fontsize=11)

plt.suptitle('Model Comparison: LogReg vs MLP', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(IMG_DIR / "model_comparison.png", dpi=150, bbox_inches='tight')
plt.show()
print("Saved: images/model_comparison.png")
print()


# ═══════════════════════════════════════════════════════════════════
# PLOT 3: Confusion Matrices (side by side)
# ═══════════════════════════════════════════════════════════════════
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

for ax, pred, title in zip(axes,
                           [lr_pred, nn_pred],
                           ['Logistic Regression', 'Simple MLP']):
    cm = confusion_matrix(y_test, pred)
    disp = ConfusionMatrixDisplay(cm, display_labels=['Left', 'Right'])
    disp.plot(ax=ax, cmap='Blues', colorbar=False)
    ax.set_title(f'{title}\nAccuracy: {accuracy_score(y_test, pred):.3f}',
                 fontsize=12, fontweight='bold')

plt.suptitle('Confusion Matrices', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig(IMG_DIR / "confusion_matrices.png", dpi=150, bbox_inches='tight')
plt.show()
print("Saved: images/confusion_matrices.png")
print()


# ═══════════════════════════════════════════════════════════════════
# PLOT 4: Loss Curve Diagnostics (annotated)
# ═══════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(train_losses, label='Training loss', color='#4A90D9', linewidth=2)
ax.plot(val_losses, label='Validation loss', color='#A71930', linewidth=2)
ax.axhline(y=np.log(2), color='gray', linestyle='--', linewidth=1, alpha=0.7,
           label=f'Random guessing ({np.log(2):.3f})')

# Annotate key regions
ax.annotate('Network starts learning\n(loss drops below chance)',
            xy=(10, train_losses[min(10, len(train_losses)-1)]),
            xytext=(25, np.log(2) + 0.01),
            fontsize=10, ha='center',
            arrowprops=dict(arrowstyle='->', color='gray', lw=1.5),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f0f0f0', edgecolor='gray'))

# Find where overfitting starts (validation loss starts increasing)
min_val_idx = np.argmin(val_losses)
if min_val_idx < n_epochs - 1:
    ax.annotate(f'Best validation loss\n(epoch {min_val_idx+1})',
                xy=(min_val_idx, val_losses[min_val_idx]),
                xytext=(min_val_idx + 15, val_losses[min_val_idx] + 0.02),
                fontsize=10, ha='center',
                arrowprops=dict(arrowstyle='->', color='#A71930', lw=1.5),
                bbox=dict(boxstyle='round,pad=0.3', facecolor=(167/255, 25/255, 48/255, 0.1),
                          edgecolor='#A71930'))

ax.set_xlabel('Epoch', fontsize=12)
ax.set_ylabel('Loss (CrossEntropy)', fontsize=12)
ax.set_title('Training Diagnostics: Loss Curve Analysis', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
ax.set_xlim(0, n_epochs)

plt.tight_layout()
plt.savefig(IMG_DIR / "loss_diagnostics.png", dpi=150, bbox_inches='tight')
plt.show()
print("Saved: images/loss_diagnostics.png")
print()


# ═══════════════════════════════════════════════════════════════════
# PLOT 5: Feature Importance (LogReg coefficients)
# ═══════════════════════════════════════════════════════════════════
# Use absolute logistic regression coefficients as a proxy for feature importance
coefs = np.abs(lr_model.coef_[0])
top_k = 15
top_idx = np.argsort(coefs)[-top_k:]
top_features = [feature_cols[i] for i in top_idx]
top_values = coefs[top_idx]

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(range(top_k), top_values, color='#4A90D9', edgecolor='white')

# Highlight motor cortex channels
for i, feat in enumerate(top_features):
    if feat.startswith(('C3_', 'C4_', 'Cz_')):
        bars[i].set_color('#A71930')

ax.set_yticks(range(top_k))
ax.set_yticklabels(top_features)
ax.set_xlabel('Absolute Coefficient', fontsize=12)
ax.set_title('Top 15 Features (Logistic Regression Coefficients)', fontsize=14, fontweight='bold')

# Add legend
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='#A71930', label='Motor cortex (C3/C4/Cz)'),
                   Patch(facecolor='#4A90D9', label='Other channels')]
ax.legend(handles=legend_elements, loc='lower right', fontsize=10)

plt.tight_layout()
plt.savefig(IMG_DIR / "feature_importance.png", dpi=150, bbox_inches='tight')
plt.show()
print("Saved: images/feature_importance.png")
print()


# ═══════════════════════════════════════════════════════════════════
# PLOT 6: "Was It Worth It?" Summary
# ═══════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')

summary_text = f"""
MODEL COMPARISON SUMMARY
{'='*50}

                        LogReg          MLP
  Accuracy:           {lr_acc:.3f}         {nn_acc:.3f}
  F1 Score:           {lr_f1:.3f}         {nn_f1:.3f}
  Lines of code:       ~5             ~30
  Debugging effort:    Minimal        Moderate
  Training time:       <1 sec         ~2 sec

{'='*50}
VERDICT: The neural network did NOT meaningfully beat
logistic regression on this data. The added complexity
(6x more code, new framework, harder debugging) was
NOT justified.

WHY? Pre-extracted tabular features with weak signal.
Neural networks shine when they can learn their own
representations from raw data (images, text, raw EEG).
"""

ax.text(0.5, 0.5, summary_text, transform=ax.transAxes,
        fontsize=12, fontfamily='monospace', verticalalignment='center',
        horizontalalignment='center',
        bbox=dict(boxstyle='round,pad=1', facecolor='#f8f9fa', edgecolor='#dee2e6'))

plt.tight_layout()
plt.savefig(IMG_DIR / "summary.png", dpi=150, bbox_inches='tight')
plt.show()
print("Saved: images/summary.png")
print()


# ═══════════════════════════════════════════════════════════════════
# FINAL SUMMARY
# ═══════════════════════════════════════════════════════════════════
print("=" * 60)
print("FINAL SUMMARY")
print("=" * 60)
print()
print(f"Logistic Regression:  Accuracy={lr_acc:.3f}, F1={lr_f1:.3f}")
print(f"Simple MLP:           Accuracy={nn_acc:.3f}, F1={nn_f1:.3f}")
print()
print(f"Final train loss:     {train_losses[-1]:.4f}")
print(f"Final val loss:       {val_losses[-1]:.4f}")
print(f"Best val loss:        {min(val_losses):.4f} (epoch {np.argmin(val_losses)+1})")
print()
print("Was it worth it? For this data: NO.")
print("Neural networks need raw signal, not pre-extracted features,")
print("to learn representations that outperform linear models.")
print()
print("All plots saved to images/")

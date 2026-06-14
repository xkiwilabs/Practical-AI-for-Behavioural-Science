"""
Week 6 Example Solution — Script 1: Data Exploration
=====================================================

This script loads the Boston College COVID-19 Sleep & Well-Being data,
aggregates daily surveys per participant, scores Big Five personality,
merges everything, and prints summary statistics. Run this first to
understand the data before classification.

Usage:
    conda activate ai-behsci
    cd weeks/week-06-lab/example_solution
    python explore_data.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", font_scale=1.1)

# ── Load the three data files ────────────────────────────────────────────────
data_dir = "../data/boston_college"

print("Loading data files...")
daily = pd.read_csv(f"{data_dir}/daily_survey.csv")
demo = pd.read_csv(f"{data_dir}/demographics.csv")
r1 = pd.read_csv(f"{data_dir}/round1_assessment.csv")

print(f"  Daily survey: {daily.shape[0]:,} entries from {daily.sub_id.nunique():,} participants")
print(f"  Demographics: {demo.shape[0]:,} participants")
print(f"  Round 1:      {r1.shape[0]:,} entries from {r1.sub_id.nunique():,} unique participants")
print()


# ── Aggregate daily survey per participant ────────────────────────────────────
agg_cols = ['PHQ9', 'PANAS_PA', 'PANAS_NA', 'TST', 'SE',
            'sleepdiary_sleeplatency', 'sleepdiary_wakes',
            'exercise', 'alcohol_bev', 'isolation', 'stress',
            'worry_scale', 'panas_sad3', 'panas_happy3', 'people_contact']

daily_with_phq = daily[daily['PHQ9'].notna()]
daily_agg = daily_with_phq.groupby('sub_id')[agg_cols].mean()

print(f"After aggregation: {daily_agg.shape[0]:,} participants with PHQ-9 data")
print()


# ── Score Big Five personality (BFI-2, 30 items) ─────────────────────────────
r1_dedup = r1.drop_duplicates(subset='sub_id', keep='first').copy()
print(f"Round 1 after dedup: {len(r1_dedup)} (removed {len(r1) - len(r1_dedup)} duplicates)")


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

# GAD-7 total
gad_cols = [f'gad_{i}' for i in range(1, 8)]
r1_dedup['GAD7_total'] = r1_dedup[gad_cols].sum(axis=1)

big5 = ['Extraversion', 'Agreeableness', 'Conscientiousness', 'Neuroticism', 'Openness']

print()
print("=== Big Five Personality Statistics ===")
for trait in big5:
    print(f"  {trait}: M={r1_dedup[trait].mean():.2f}, SD={r1_dedup[trait].std():.2f}")
print(f"  GAD-7 total: M={r1_dedup['GAD7_total'].mean():.1f}, SD={r1_dedup['GAD7_total'].std():.1f}")
print()


# ── Merge all three datasets ────────────────────────────────────────────────
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


# ── Create binary target ────────────────────────────────────────────────────
merged['depression_elevated'] = (merged['PHQ9'] >= 5).astype(int)

print("=== Class Balance ===")
print(merged['depression_elevated'].value_counts())
print()
print("Proportions:")
print(merged['depression_elevated'].value_counts(normalize=True).round(3))
print()


# ── Summary statistics ──────────────────────────────────────────────────────
print("=== PHQ-9 Statistics ===")
print(f"  Mean: {merged['PHQ9'].mean():.2f}")
print(f"  SD:   {merged['PHQ9'].std():.2f}")
print(f"  Range: [{merged['PHQ9'].min():.1f}, {merged['PHQ9'].max():.1f}]")
print()

print("=== Demographics ===")
print(f"  Age: M={merged['age1'].mean():.1f}, SD={merged['age1'].std():.1f}")
print(f"  Bio sex: {merged['bio_sex'].value_counts().to_dict()}")
print()


# ── Correlations with PHQ-9 ─────────────────────────────────────────────────
feature_cols = ['PANAS_PA', 'PANAS_NA', 'TST', 'SE',
                'sleepdiary_sleeplatency', 'sleepdiary_wakes',
                'exercise', 'alcohol_bev', 'isolation', 'stress',
                'worry_scale', 'panas_sad3', 'panas_happy3',
                'age1', 'bio_sex',
                'Extraversion', 'Agreeableness', 'Conscientiousness',
                'Neuroticism', 'Openness', 'GAD7_total']

print("=== Correlations with PHQ-9 (continuous) ===")
corrs = merged[['PHQ9'] + feature_cols].corr()['PHQ9'].drop('PHQ9')
corrs_sorted = corrs.abs().sort_values(ascending=False)
for var in corrs_sorted.index:
    print(f"  {var:30s}  r = {corrs[var]:+.3f}")
print()


# ── Class distribution plot ──────────────────────────────────────────────────
print("Generating class distribution plot...")
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# PHQ-9 distribution with threshold
axes[0].hist(merged['PHQ9'], bins=30, color='#4A90D9', edgecolor='white', alpha=0.8)
axes[0].axvline(x=5, color='#A71930', linewidth=2, linestyle='--', label='Threshold (PHQ-9 = 5)')
axes[0].set_xlabel('PHQ-9 Score (averaged across daily entries)', fontsize=12)
axes[0].set_ylabel('Count', fontsize=12)
axes[0].set_title('PHQ-9 Distribution with Classification Threshold', fontsize=14, fontweight='bold')
axes[0].legend(fontsize=11)

# Class balance bar chart
counts = merged['depression_elevated'].value_counts()
bars = axes[1].bar(['Minimal\n(PHQ-9 < 5)', 'Elevated\n(PHQ-9 >= 5)'],
                   [counts[0], counts[1]],
                   color=['#5BA55B', '#A71930'], edgecolor='white', linewidth=0.5)
axes[1].set_ylabel('Number of Participants', fontsize=12)
axes[1].set_title('Class Balance', fontsize=14, fontweight='bold')
for bar, count in zip(bars, [counts[0], counts[1]]):
    pct = count / len(merged) * 100
    axes[1].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
                 f'{count}\n({pct:.1f}%)', ha='center', fontsize=11, fontweight='bold')

plt.tight_layout()
fig.savefig("images/class_distribution.png", dpi=200, bbox_inches="tight")
plt.close()
print("  Saved: images/class_distribution.png")
print()
print("Exploration complete.")

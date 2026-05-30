# Final Plan: What Actually Happened

> This is the updated plan reflecting what we actually built. Compare with the original `plan.md` to see what changed and why.

## What We Set Out to Do

Explore the structure of mental distress using PCA on 42 DASS items, visualise with UMAP, cluster participants by personality and distress profiles, check stability, and write a methods paragraph.

## What Changed

### 1. VCL filter removed more respondents than expected

The age filter barely changed the dataset (39,775 → 39,768), but the VCL careless responder filter removed ~5,200 participants. After both filters: **34,576 respondents**. This is ~13% of the original sample — a substantial number of people claiming to know words that don't exist. This is a good reminder that large online datasets need quality checks.

### 2. PCA found a dominant first component

The first principal component captured **44.78%** of all variance — nearly half the signal in 42 items. This "general distress" factor (all items load positively) is much stronger than the second component (6.74%). The three-component solution explains 55.36%, which matches the three DASS subscales but with an important nuance: the data is more "one big thing plus nuances" than "three equal things."

| Component | Variance | Interpretation |
|-----------|----------|----------------|
| PC1 | 44.78% | General distress — everyone who scores high on anything scores high on everything |
| PC2 | 6.74% | Depression vs Anxiety — separates depressive from anxious symptoms |
| PC3 | 3.85% | Stress vs Anxiety — separates stress from anxiety |

### 3. k=2 was the best cluster solution

| k | Silhouette |
|---|-----------|
| 2 | **0.240** |
| 3 | 0.150 |
| 4 | 0.145 |
| 5 | 0.132 |
| 6 | 0.125 |

The silhouette scores drop sharply after k=2. This suggests the data really has one main division: low distress vs high distress. There's no strong evidence for 3 or 4 distinct "types."

### 4. The two clusters split cleanly on distress severity

| Cluster | N | Depression | Anxiety | Stress | EmotionalStability |
|---------|---|-----------|---------|--------|--------------------|
| 0 (Low distress) | 16,908 (48.9%) | 11.8 | 8.6 | 13.0 | 4.18 |
| 1 (High distress) | 17,668 (51.1%) | 29.7 | 22.8 | 28.7 | 2.32 |

The high-distress cluster has roughly 2.5× the depression scores, nearly 3× the anxiety scores, and 2.2× the stress scores. They also have lower Emotional Stability, Extraversion, and Conscientiousness. This is consistent with a severity dimension rather than distinct "types."

### 5. The clusters are extremely stable

Average agreement across 5 random seeds: **99.9%**. Fewer than 0.35% of participants changed cluster in any run. This is unusually high stability — likely because the two clusters are so well-separated along the distress dimension. With more clusters (k=3 or 4), stability would likely be lower.

### 6. UMAP showed a gradient, not distinct clusters

The UMAP projection showed depression severity as a smooth gradient from low (green) to high (red), without sharp boundaries between groups. This is consistent with the taxometric evidence that distress is dimensional, not categorical.

### 7. Documentation required several corrections

The AI's initial methods paragraph:
- Said "Principal Components Analysis" (correct full name, but inconsistent capitalisation)
- Stated "3 components explaining 56% of variance" — the actual number is 55.36%
- Described the TIPI as a "7-point Likert scale" — the OpenPsychometrics version uses 0–7
- Omitted the careless responder filtering step entirely
- Said "sklearn version 1.3" — needed updating to match the actual installed version

This illustrates why the documentation skill matters: AI drafts are a starting point that must be verified against the actual analysis.

## Key Findings

1. **The dominant structure of distress is one dimension** — PC1 (general distress) captures 45% of all variance. Depression, anxiety, and stress are much more similar than different.

2. **k=2 is the best clustering solution** — the data splits into low and high distress groups. There's no evidence for more nuanced "types" of distress in this dataset.

3. **The two clusters are extremely stable** — 99.9% agreement across random seeds. This is what stability looks like when clusters are real (though "real" here means "a reliable split on a continuous dimension," not "genuine categories").

4. **UMAP shows a gradient, not categories** — consistent with the taxometric literature suggesting distress is dimensional.

5. **Personality differences between clusters are meaningful** — the high-distress cluster scores lower on Emotional Stability (~2.3 vs ~4.2), supporting the well-established link between neuroticism and distress.

## What We'd Do Differently

- Try **hierarchical clustering** to see if the dendrogram reveals meaningful sub-structure within the two main groups
- Run **DBSCAN** to see if there are genuinely separate density regions or just a continuous gradient
- Try **parallel analysis** for a more principled approach to choosing the number of PCA components
- Examine whether the cluster profiles differ across **countries** (the dataset includes respondents from many countries)
- Try clustering on **PCA scores** instead of raw subscales+personality — would the results change?

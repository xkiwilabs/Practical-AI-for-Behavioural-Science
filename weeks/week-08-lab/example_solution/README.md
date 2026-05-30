# Week 8 Example Solution

This folder contains a worked example showing how the Week 8 challenge lab could be completed, including PCA exploration, UMAP visualisation, clustering with stability checks, and a documentation exercise.

> **Note:** This is an *example* solution, not the only correct one. Students' work will look different — different numbers of components, different k values, different cluster interpretations. The point is to demonstrate the process: explore with PCA, visualise with UMAP, cluster thoughtfully, check stability, and document clearly.

## Folder Structure

```
example_solution/
├── README.md                      ← you are here
├── plan.md                        ← initial analysis plan (before coding)
├── plan_final.md                  ← updated plan reflecting what was actually built
├── example_solution.ipynb         ← full notebook workflow (PCA → UMAP → cluster → stability)
├── explore_structure.py           ← script 1: PCA + UMAP exploration
├── cluster_profiles.py            ← script 2: clustering + stability checks
├── slide.html                     ← example presentation slide (reveal.js)
├── css/
│   └── mq-theme.css               ← slide styling
└── images/
    ├── scree_plot.png             ← PCA variance explained
    ├── pca_loadings.png           ← component loadings heatmap
    ├── umap_depression.png        ← UMAP coloured by depression severity
    ├── elbow_silhouette.png       ← k selection diagnostics
    ├── cluster_profiles.png       ← standardised feature means per cluster
    └── stability_check.png        ← agreement across random seeds
```

## Key Results

Using 42 DASS distress items for PCA and 8 features (5 Big Five + 3 DASS subscales) for clustering on 34,576 respondents:

### PCA

| Component | Variance Explained | Cumulative | Interpretation |
|-----------|-------------------|------------|----------------|
| PC1 | 44.78% | 44.78% | General distress — all items load positively |
| PC2 | 6.74% | 51.51% | Depression vs Anxiety contrast |
| PC3 | 3.85% | 55.36% | Stress vs Anxiety contrast |

### Clustering

| k | Silhouette | Notes |
|---|-----------|-------|
| 2 | **0.240** | Best — clean split into low/high distress |
| 3 | 0.150 | |
| 4 | 0.145 | |
| 5 | 0.132 | |

### Cluster Profiles (k=2)

| Cluster | N | Depression | Anxiety | Stress | EmotionalStability |
|---------|---|-----------|---------|--------|--------------------|
| 0 (Low distress) | 16,908 (48.9%) | 11.8 | 8.6 | 13.0 | 4.18 |
| 1 (High distress) | 17,668 (51.1%) | 29.7 | 22.8 | 28.7 | 2.32 |

### Stability

Average agreement across 5 random seeds: **99.9%** — the k=2 solution is very stable.

## Running the Code

```bash
conda activate psyc4411-env
cd weeks/week-08-lab/example_solution

# Script workflow
python explore_structure.py      # PCA + UMAP (~2 min for UMAP)
python cluster_profiles.py       # Clustering + stability

# View the slide
open slide.html    # macOS
```

The notebook can be opened and run cell-by-cell in VS Code or Jupyter.

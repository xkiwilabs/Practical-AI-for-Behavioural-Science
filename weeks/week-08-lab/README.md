# Week 8 Challenge Lab: Find Structure, Don't Fabricate It

> **Group Challenge:** Discover the hidden structure of mental distress using PCA and clustering. Are there meaningful subgroups in how people experience depression, anxiety, and stress — or are you imposing patterns on noise?

This lab works well as group work — meet up (in person or online), work through the challenge together, and present what you find.

---

## The Challenge

Your task is to explore the **structure of mental distress** using the same DASS-42 dataset from Week 4 — but with a completely different question. In Week 4, you asked "can personality predict depression?" Now you'll ask: "are there meaningful patterns hiding in 42 symptoms of distress?"

This challenge has two phases:

**Phase 1 — Dimensionality Reduction:** Run PCA on the 42 DASS items. How many meaningful components are there? What do they represent? Visualise the participants in 2D using UMAP.

**Phase 2 — Clustering:** Cluster participants by their personality and distress profiles. How many groups? Are they psychologically meaningful? Do they survive a different random seed?

You need to:
1. **Run PCA on the 42 DASS items** — how many components? What do they represent?
2. **Visualise with UMAP** — create a 2D map coloured by depression severity
3. **Cluster participants** using at least two values of k — which is better and why?
4. **Profile your clusters** — describe them psychologically (not just with numbers)
5. **Check stability** — do your clusters survive a different random seed? Report silhouette scores
6. **Write a methods paragraph** — use your AI to draft a description suitable for a journal paper, then verify every detail matches what you actually did

---

## Background

In Weeks 2–6, every model you built had a target variable and a clear "right answer." This week, there's no target. No accuracy. No confusion matrix. Instead, you're asking the data to reveal its own structure — and the challenge is figuring out whether what you find is real.

You already know this dataset from Week 4. You know the DASS-42 has 42 items measuring depression, anxiety, and stress. You know the TIPI gives Big Five personality scores. The data preparation is familiar territory. What's new is the question: instead of predicting one variable from others, you're looking for patterns across all variables at once.

**New LLM Skill: Documentation.** In Week 2 you learned prompting, in Week 4 you learned debugging, in Week 6 you learned refactoring. This week's skill is **documentation** — asking your AI to help write clear, accurate descriptions of your analysis. In research, your analysis is only as good as your ability to explain it. The AI's draft is a starting point — you need to verify that every number, method name, and description matches what you actually did. Documentation that doesn't match the analysis is worse than no documentation at all.

---

## Use Whatever AI Tools You Like

VS Code Copilot, ChatGPT, Claude, Gemini — use any combination. Mix and match. There are no restrictions on which AI tools you use in this course.

---

## The Dataset

**OpenPsychometrics DASS-42 + Big Five (TIPI) + Demographics**
- **Source:** [OpenPsychometrics](https://openpsychometrics.org/_rawdata/)
- **Size:** 39,775 respondents, 172 variables
- **Format:** Tab-separated CSV

You may still have this data from Week 4. If not, download it:
```
conda activate ai-behsci
cd weeks/week-08-lab/data
python download_data.py
```

### Key Variables

| Variable Group | Columns | Description |
|---|---|---|
| **DASS-42 items** | `Q1A`–`Q42A` | 42 distress items, coded 1–4 (recode to 0–3) |
| **Depression subscale** | Q3, Q5, Q10, Q13, Q16, Q17, Q21, Q24, Q26, Q31, Q34, Q37, Q38, Q42 | 14 items, sum → 0–42 |
| **Anxiety subscale** | Q2, Q4, Q7, Q9, Q15, Q19, Q20, Q23, Q25, Q28, Q30, Q36, Q40, Q41 | 14 items, sum → 0–42 |
| **Stress subscale** | Q1, Q6, Q8, Q11, Q12, Q14, Q18, Q22, Q27, Q29, Q32, Q33, Q35, Q39 | 14 items, sum → 0–42 |
| **TIPI personality** | `TIPI1`–`TIPI10` | 10 items → 5 Big Five traits |
| **Demographics** | `age`, `gender`, `country` | Age, gender (1–3), country code |
| **Vocabulary check** | `VCL1`–`VCL16` | VCL6, VCL9, VCL12 are fake words (for data quality filtering) |

### Data Preparation Summary
1. Filter ages to 10–100 (remove unrealistic values like birth years)
2. Remove careless responders (anyone who claims to know fake vocabulary words VCL6, VCL9, or VCL12)
3. Recode DASS items from 1–4 to 0–3 (subtract 1)
4. Score DASS subscales (sum 14 items each for Depression, Anxiety, Stress)
5. Score Big Five from TIPI (reverse-score items 2, 4, 6, 8, 10; compute trait means)
6. **Expected result:** ~34,500 respondents after cleaning, 42 DASS items for PCA, 8 features (5 Big Five + 3 DASS subscales) for clustering

---

## Getting Started

1. **Download the data** (if you don't have it from Week 4):
   ```
   conda activate ai-behsci
   cd weeks/week-08-lab/data
   python download_data.py
   ```

2. **Open the starter files:** `starter.ipynb` (notebook) or `starter.py` (script)
   - Cells 1–5 are fully functional — they load, clean, and score the data
   - Cells 6+ are scaffolded — your AI helps you fill them in

3. **Have your AI create a plan first** — before writing any analysis code, ask it to outline the approach

4. **Phase 1: PCA and UMAP** — discover the component structure and visualise it

5. **Phase 2: Clustering** — find groups, profile them, test stability

6. **Write a methods paragraph** — practise documentation with AI assistance

7. **Prepare your presentation slide**

---

## Starter LLM Prompts

**Planning prompt:**
> "I have a pandas DataFrame with ~34,500 rows (after data quality filtering) from the DASS-42 dataset. It contains 42 DASS items (Q1A–Q42A, recoded to 0–3), Big Five personality scores (Extraversion, Agreeableness, Conscientiousness, EmotionalStability, Openness from the TIPI), 3 DASS subscale totals (DASS_Depression, DASS_Anxiety, DASS_Stress), and demographics (age, gender). I want to: (1) run PCA on the 42 raw DASS items to discover the factor structure, (2) visualise participants in 2D using UMAP, coloured by depression severity, (3) cluster participants by their Big Five + DASS profiles using k-means, (4) evaluate the clustering with silhouette scores, (5) check stability with different random seeds. Create a plan — don't write code yet."

**Code prompt (after plan):**
> "Following my analysis plan, write Python code to: (1) standardise the 42 DASS items and fit PCA, (2) create a scree plot showing variance explained per component, (3) display the top 5 loadings for each of the first 3 components, (4) fit UMAP (n_components=2, random_state=42) on the standardised DASS items and create a scatter plot coloured by DASS_Depression, (5) run k-means for k=2,3,4,5 on standardised Big Five + DASS subscales (8 features), (6) plot silhouette scores vs k, (7) profile the best k solution with a bar chart of mean feature values per cluster. Use pandas, sklearn, umap-learn, matplotlib."

**Documentation prompt:**
> "I've run PCA on 42 DASS items from [your N] participants (after filtering for data quality). I found a [your number]-component solution explaining [your %] of total variance. The loadings suggest Component 1 is [your interpretation], Component 2 [your interpretation], and Component 3 [your interpretation]. I then clustered participants using k-means (k=[your k]) on their Big Five personality scores and DASS subscale totals (8 features, standardised). Write a methods paragraph for a psychology journal describing this analysis. Use APA style. Include: sample size, measures, analysis approach, number of components/clusters, and how cluster solutions were evaluated (silhouette scores, stability checks). Be specific about software (Python, scikit-learn)."

---

## Starter Code

- **Notebook:** [starter.ipynb](starter.ipynb) — scaffolded Jupyter notebook
- **Script:** [starter.py](starter.py) — scaffolded Python script

Both contain functional data loading, cleaning, and scoring (cells/sections 1–5). Your AI fills in the analysis sections.

---

## What to Present (1 HTML slide, ~3 min)

1. **PCA results** — how many components? What do they represent? Show the scree plot.
2. **UMAP visualisation** — show the 2D projection. What patterns do you see?
3. **Best cluster solution** — how many clusters? Show the profiles (what does each cluster look like?).
4. **Stability check** — did your clusters survive a different random seed? Report silhouette scores.
5. **Methods paragraph** — show one sentence from your AI-drafted methods paragraph that you had to correct or improve. What did the AI get wrong?

---

## Bonus Challenges

1. **Parallel analysis** — Compare PCA eigenvalues to those from random data (same dimensions). This provides a statistically principled way to determine the number of components. Ask your AI: "How do I run parallel analysis for PCA in Python?"

2. **Varimax rotation** — Apply varimax rotation to the PCA solution. Does it change the interpretation of the components? Ask your AI about rotation methods for PCA.

3. **Hierarchical clustering** — Build a dendrogram and compare to k-means. Do you get the same groups?

4. **DBSCAN** — Try density-based clustering. Does DBSCAN find different clusters than k-means? How many "noise" points does it identify?

5. **Cluster by demographics** — Do cluster memberships differ by age group, gender, or country? Create a cross-tabulation and test with chi-square.

6. **Bootstrap stability** — Resample your data 100 times (with replacement), recluster each time, and measure how often pairs of participants end up in the same cluster. This is a rigorous stability test. Ask your AI about the Jaccard index.

7. **Compare PCA and UMAP** — Show the same participants in PCA space (PC1 vs PC2) and UMAP space. What does UMAP reveal that PCA doesn't? What might it distort?

8. **Try MALD/ELP** — Apply PCA/clustering to a psycholinguistic dataset. Can you cluster words by their processing characteristics? (Download from the Massive Auditory Lexical Decision database.)

---

## Hints

<details>
<summary>1. Scoring DASS subscales</summary>

The raw items (Q1A–Q42A) are coded 1–4. Recode to 0–3 first (subtract 1). Depression items: Q3, Q5, Q10, Q13, Q16, Q17, Q21, Q24, Q26, Q31, Q34, Q37, Q38, Q42. Sum the 14 items for each subscale — scores range 0–42.
</details>

<details>
<summary>2. Standardising for PCA</summary>

PCA is sensitive to scale — variables with larger ranges dominate. Always standardise first:
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(dass_items)
```
</details>

<details>
<summary>3. Choosing the number of components</summary>

Look at the scree plot. The "elbow" is where the curve flattens. Also check cumulative variance explained — you want enough components to capture a useful amount (e.g., > 50%) without keeping noise.
</details>

<details>
<summary>4. UMAP installation</summary>

If UMAP isn't installed: `pip install umap-learn`. Import as `import umap`. Basic usage:
```python
reducer = umap.UMAP(n_components=2, random_state=42)
embedding = reducer.fit_transform(X_scaled)
```
</details>

<details>
<summary>5. Silhouette scores</summary>

Higher is better (range: -1 to 1). Compare across k values:
```python
from sklearn.metrics import silhouette_score
for k in [2, 3, 4, 5]:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(X_scaled)
    print(f"k={k}: silhouette={silhouette_score(X_scaled, labels):.3f}")
```
</details>

<details>
<summary>6. Cluster profiling</summary>

Get the mean of each feature per cluster:
```python
df['cluster'] = labels
profile = df.groupby('cluster')[feature_cols].mean()
profile.plot(kind='bar', figsize=(12, 6))
```
</details>

---

*[Back to course overview](../../README.md)*

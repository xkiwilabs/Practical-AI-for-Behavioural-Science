# Week 6 Challenge Lab: Build a Defensible Classifier

> **Group Challenge:** Classify participants as having elevated or minimal depression using real COVID-era survey data. Compare multiple classifiers, justify your threshold, and consider the ethical implications of your model.

---

## The Challenge

Your task is to build a **classification pipeline** that predicts whether a person has **elevated depression** (PHQ-9 score ≥ 5) or **minimal symptoms** (PHQ-9 < 5) using data from the Boston College COVID-19 Sleep and Well-Being Study. You'll compare four models — a baseline, logistic regression, a decision tree, and a random forest — and justify which model you'd recommend and why.

This isn't just about getting the highest accuracy. You need to:
1. **Report proper classification metrics** — not just accuracy, but precision, recall, F1, and AUC
2. **Justify your decision threshold** — why 0.5? Why not 0.3 or 0.7?
3. **Analyse feature importance** — which features matter most for predicting depression?
4. **Consider one ethical implication** — what could go wrong if this model were deployed?

---

## Background

In Week 5, you learned about classification metrics, decision thresholds, and the difference between types of errors. Now you'll put those concepts into practice. You already know how to build a pipeline (features → split → train → evaluate) from Week 4 — the new challenge is working with **classification models** and **multi-source data** that requires merging.

**New LLM Skill: Refactoring.** In Week 2 you learned prompting, in Week 4 you learned debugging. This week, practise **refactoring** — asking your AI assistant to take working-but-messy code and make it cleaner, more modular, and easier to understand. In research, good documentation and clear comments are as important as the code itself. Someone reading your analysis six months from now (including future you) needs to understand *what* the code does and *why* — not just that it runs. In a research context, it is almost always better to sacrifice a tiny bit of code optimisation for code that is more transparent and easier to follow. Saving a millisecond or two by writing clever, compressed code is not worth it if nobody can understand what's happening.

---

## Use Whatever AI Tools You Like

VS Code Copilot, ChatGPT, Claude, Gemini — use any combination. Mix and match. There are no restrictions on which AI tools you use in this course.

---

## The Dataset

**Boston College COVID-19 Sleep and Well-Being Study**
- **Source:** [OSF](https://osf.io/gpxwa/) — Cunningham, Fields, & Kensinger (2021)
- **Period:** March–June 2020 (early COVID-19 pandemic)
- **Files:** Three CSV files that need to be merged

### File 1: `daily_survey.csv` — Daily diary entries
| Variable | Description |
|----------|------------|
| `sub_id` | Participant identifier |
| `PHQ9` | PHQ-9 depression score (computed, 0–24, 8 items) |
| `PANAS_PA` | Positive affect (PANAS subscale) |
| `PANAS_NA` | Negative affect (PANAS subscale) |
| `TST` | Total sleep time (hours) |
| `SE` | Sleep efficiency (0–1) |
| `sleepdiary_sleeplatency` | Time to fall asleep (minutes) |
| `sleepdiary_wakes` | Number of night-time awakenings |
| `exercise` | Exercised today (0/1) |
| `alcohol_bev` | Alcoholic beverages consumed |
| `isolation` | Isolation/loneliness (1–7, higher = less isolated) |
| `stress` | Stress coping (1–7, higher = better coping) |
| `worry_scale` | COVID worry composite (5–35) |
| `panas_sad3`, `panas_happy3` | Individual mood items |
| `people_contact` | Number of people contacted |

**Important:** Each participant has *multiple* daily entries. You need to **aggregate** (average) these per participant before merging.

### File 2: `demographics.csv` — Participant background
| Variable | Description |
|----------|------------|
| `sub_id` | Participant identifier |
| `age1` | Age (18–90) |
| `bio_sex` | Biological sex (1=Female, 2=Male) |
| `education` | Education level (1–6) |
| `student` | Student status (0/1) |
| `employed` | Employment status (0/1) |

### File 3: `round1_assessment.csv` — Personality and anxiety
| Variable | Description |
|----------|------------|
| `sub_id` | Participant identifier |
| `big5_1` to `big5_30` | Big Five personality items (BFI-2, 1–5 scale) |
| `gad_1` to `gad_7` | GAD-7 anxiety items (0–3 scale) |

**Note:** Round 1 has 75 duplicate `sub_id` entries — drop duplicates (keep first) before merging.

### Data Preparation Summary
1. Aggregate `daily_survey.csv` per participant: `daily.groupby('sub_id')[numeric_cols].mean()`
2. Deduplicate `round1_assessment.csv`: `r1.drop_duplicates(subset='sub_id', keep='first')`
3. Score Big Five traits (6 items each, some reverse-scored) and GAD-7 total
4. Merge all three on `sub_id` (inner join)
5. Create binary target: `depression_elevated = (PHQ9 >= 5).astype(int)`
6. **Expected result:** ~836 participants, 21 features, ~54.5% elevated / ~45.5% minimal

---

## Getting Started

1. **Download the data** (if you haven't already):
   ```
   conda activate ai-behsci
   cd weeks/week-06-lab/data
   python download_data.py
   ```

2. **Open the starter files:** `starter.ipynb` (notebook) or `starter.py` (script)
   - Cells 1–8 are fully functional — they load, aggregate, merge, and create the target
   - Cells 9+ are scaffolded — your AI helps you fill them in

3. **Have your AI create a plan first** — before writing any modelling code, ask it to outline the approach

4. **Build four models:** Baseline → Logistic Regression → Decision Tree → Random Forest

5. **Evaluate with proper metrics:** Accuracy, F1, AUC, precision, recall, confusion matrix

6. **Justify your threshold:** Try at least one threshold other than 0.5

7. **Examine feature importance:** Which features matter most? Does this match psychological intuition?

8. **Consider ethics:** What could go wrong if this model were used to make decisions about people?

9. **Refactor your code:** Ask your AI to improve your code structure, add documentation, and make the logic easier to follow (see refactoring prompts below)

10. **Prepare your presentation slide**

---

## Starter LLM Prompts

**Planning prompt:**
> "I have three CSV files from the Boston College COVID-19 Sleep and Well-Being Study: daily_survey.csv (52,634 daily entries from 1,484 participants), demographics.csv (1,662 participants), and round1_assessment.csv (914 participants, Big Five personality + GAD-7 anxiety). I need to: (1) aggregate daily survey data per participant (mean of numeric columns), (2) score Big Five personality traits from 30 BFI items, (3) compute GAD-7 total, (4) merge all three files on sub_id, (5) create a binary target: elevated depression (PHQ-9 >= 5) vs minimal (< 5). Then build and compare classifiers: baseline, logistic regression, decision tree, and random forest. Create a plan — don't write code yet."

**Code prompt (after plan):**
> "Following my analysis plan, write Python code to: (1) load and aggregate the daily survey per participant, (2) score Big Five traits from BFI-2 items (30 items, 6 per trait, reverse-score items 6,8,10,12,16,18,19,20,22,24,26,28,29,30,2), (3) merge all dataframes, (4) create the binary target, (5) split 80/20 stratified, (6) fit baseline, LogisticRegression, DecisionTreeClassifier(max_depth=5), and RandomForestClassifier(n_estimators=100), (7) report accuracy, F1, AUC, and confusion matrix for each. Use pandas, sklearn, matplotlib."

**Refactoring prompt:**
> "I have this analysis pipeline that works but is messy. Refactor it to: (1) separate data loading/merging from modelling, (2) add assertions to verify data shape after each merge step, (3) create a reusable function called `evaluate_model(model, X_train, X_test, y_train, y_test)` that returns a dictionary of metrics, (4) add clear docstrings to each function, (5) add comments explaining *why* each major step is done (not just *what* it does) — someone reading this code for the first time should understand the reasoning, not just the mechanics. Prioritise readability over cleverness — this is research code, not production software. Keep the logic identical — I want the same outputs but cleaner, better-documented code."

---

## Starter Code

- **Notebook:** [starter.ipynb](starter.ipynb) — scaffolded Jupyter notebook
- **Script:** [starter.py](starter.py) — scaffolded Python script

Both contain functional data loading and merging (cells/sections 1–8). Your AI fills in the modelling sections.

---

## What to Present (1 HTML slide, ~3 min)

1. **Your best model** — which classifier performed best? Report accuracy, F1, and AUC.
2. **Threshold justification** — what threshold did you use and why? What happens if you change it?
3. **Feature importance** — which features mattered most? Show a chart or list the top 5.
4. **Ethical consideration** — one thing that could go wrong if this model were deployed for real.
5. **One refactoring win** — how did refactoring improve your code? This could be better structure, clearer documentation, or code that's easier for someone else to follow.

---

## Bonus Challenges

1. **ROC curves** — Plot ROC curves for all three models (LogReg, DT, RF) on the same figure. Which dominates?

2. **Feature importance comparison** — Compare Random Forest feature importance with logistic regression coefficient magnitudes. Do they agree on what matters?

3. **XGBoost** — Try gradient boosting (`from xgboost import XGBClassifier`). Does it beat the Random Forest? Ask your AI: "How do I install and use XGBoost for classification?"

4. **Class imbalance handling** — Try `class_weight='balanced'` in LogisticRegression and RandomForest. Or try SMOTE (`from imblearn.over_sampling import SMOTE`). Does it change the results?

5. **Daily-level analysis** — Instead of aggregating per participant, try predicting depression at the daily level. How do results differ? What are the statistical issues with this approach?

6. **Subgroup error analysis** — Check model accuracy separately for different age groups or genders. Does the model work equally well for everyone?

7. **Cognitive load alt dataset** — Try your classification pipeline on a completely different dataset. Can you classify high vs low cognitive load from response time data?

8. **Learning curves** — Plot training vs validation accuracy as a function of training set size. Is your model underfitting or overfitting? Ask your AI about `sklearn.model_selection.learning_curve`.

---

## Hints

<details>
<summary>1. Aggregating daily data</summary>

Each participant has multiple daily survey entries. Average them per participant:
```python
agg_cols = ['PHQ9', 'PANAS_PA', 'PANAS_NA', 'TST', 'SE',
            'sleepdiary_sleeplatency', 'sleepdiary_wakes',
            'exercise', 'alcohol_bev', 'isolation', 'stress',
            'worry_scale', 'panas_sad3', 'panas_happy3', 'people_contact']
daily_agg = daily[daily['PHQ9'].notna()].groupby('sub_id')[agg_cols].mean()
```
</details>

<details>
<summary>2. Merging dataframes</summary>

Use inner joins on `sub_id` and check shapes after each merge:
```python
merged = daily_agg.merge(demo[['sub_id', 'age1', 'bio_sex']],
                         left_index=True, right_on='sub_id', how='inner')
print(f"After merge with demographics: {merged.shape}")
```
</details>

<details>
<summary>3. Creating the binary target</summary>

PHQ-9 ≥ 5 indicates at least mild depression:
```python
merged['depression_elevated'] = (merged['PHQ9'] >= 5).astype(int)
print(merged['depression_elevated'].value_counts(normalize=True))
```
</details>

<details>
<summary>4. Stratified splitting</summary>

Keep class proportions equal in train and test:
```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
```
</details>

<details>
<summary>5. Feature importance from trees</summary>

Random forests and decision trees have built-in feature importance:
```python
importances = pd.Series(rf.feature_importances_, index=feature_cols)
importances.sort_values(ascending=True).plot(kind='barh')
```
</details>

<details>
<summary>6. Threshold analysis</summary>

Try different thresholds and see how metrics change:
```python
y_prob = model.predict_proba(X_test)[:, 1]
for threshold in [0.3, 0.4, 0.5, 0.6, 0.7]:
    y_pred = (y_prob >= threshold).astype(int)
    print(f"Threshold {threshold}: F1={f1_score(y_test, y_pred):.3f}")
```
</details>

---

*[Back to course overview](../../README.md)*

# Week 4 Challenge Lab: Predict & Explain — Regression on Real DASS Data

## The Challenge

Build regression models to **predict depression scores** from personality traits and demographics using real survey data from nearly 40,000 people. Compare a baseline model, linear regression, Ridge, and Lasso — report cross-validated MAE and R². Then **explain** what the model tells you: which personality traits matter most for predicting depression, and does this match what you'd expect from psychology?

This is a group challenge. You'll work together during class and prepare a 1-slide, ~3-minute presentation for Week 5.

## Background

In Week 3, you learned the vocabulary of machine learning: features and targets, train/test splits, cross-validation, overfitting, and regularisation. Now you put those ideas to work on a real dataset.

This week's LLM skill focus is **debugging**. When code breaks (and it will — that's normal), you'll practise sharing error messages with your AI assistant and getting useful fixes. The key skill: **ask the AI to explain what went wrong**, not just fix it. Understanding errors makes you faster next time.

## Use Whatever AI Tools You Like

There are no rules about which AI tools you use for this challenge. Use whatever works for you:

- **Inside VS Code:** Copilot Chat (ask questions, get code), Edit mode (highlight code and ask the AI to change it), or Agent mode (let the AI create files, run code, and iterate on its own)
- **Browser chatbots:** ChatGPT, Claude, Gemini — copy and paste code back and forth
- **CLI tools:** If you've installed Claude Code, Codex, or similar command-line tools, feel free to use them
- **Mix and match:** Use a browser chatbot for brainstorming and VS Code for writing code — there's no single "right" setup

## Dataset

The data is in [`data/dass42_data.csv`](data/dass42_data.csv) — **real survey data** from the OpenPsychometrics project. If the file isn't there yet, run the download script first:

```bash
conda activate psyc4411-env
cd weeks/week-04-lab/data
python download_data.py
```

### Overview

| Property | Value |
|----------|-------|
| **Source** | [OpenPsychometrics DASS-42](https://openpsychometrics.org/_rawdata/) |
| **Respondents** | 39,775 |
| **Columns** | 172 (tab-separated) |
| **Format** | Tab-separated CSV (use `sep="\t"` when loading) |

This is much bigger and messier than the synthetic Week 2 dataset. It has real data quality issues — some ages are clearly wrong (e.g., someone entered their birth year instead of their age), and ~54% of respondents are from Malaysia. Working with messy real data is part of the learning experience.

### DASS-42 Items (Q1A – Q42A)

The Depression Anxiety Stress Scales (DASS-42) is a well-validated clinical questionnaire. Each of the 42 items is scored **1–4** in this dataset, but the standard DASS scoring uses **0–3**. You'll need to **subtract 1** from each item before summing.

**Depression subscale (14 items):** Q3, Q5, Q10, Q13, Q16, Q17, Q21, Q24, Q26, Q31, Q34, Q37, Q38, Q42

After recoding (subtract 1) and summing, the Depression score ranges from **0 to 42**. Higher scores = more depressive symptoms.

The Anxiety (14 items) and Stress (14 items) subscales use the remaining items — see the [codebook](data/dass42_codebook.txt) for details.

### Big Five Personality (TIPI1 – TIPI10)

The Ten-Item Personality Inventory (TIPI) measures the Big Five personality traits using just 10 items, rated **1–7**. Items 2, 4, 6, 8, and 10 are **reverse-scored** (reverse = 8 − original).

| Trait | Items | Scoring |
|-------|-------|---------|
| Extraversion | TIPI1, TIPI6 (reverse) | (TIPI1 + TIPI6R) / 2 |
| Agreeableness | TIPI2 (reverse), TIPI7 | (TIPI2R + TIPI7) / 2 |
| Conscientiousness | TIPI3, TIPI8 (reverse) | (TIPI3 + TIPI8R) / 2 |
| Emotional Stability | TIPI4 (reverse), TIPI9 | (TIPI4R + TIPI9) / 2 |
| Openness | TIPI5, TIPI10 (reverse) | (TIPI5 + TIPI10R) / 2 |

### Demographics

| Variable | Description | Values |
|----------|-------------|--------|
| `age` | Age in years | 13–99 (some clearly wrong entries like 1998) |
| `gender` | Self-reported gender | 1=Male, 2=Female, 3=Other, 0=missed |
| `education` | Highest education level | 0=less than high school, 1=high school, 2=university, 3=graduate degree |
| `urban` | Area type | 1=rural, 2=suburban, 3=urban |
| `married` | Marital status | 1=never married, 2=currently married, 3=previously married |
| `familysize` | Number of family members | Integer |
| `hand` | Handedness | 1=right, 2=left, 3=both |
| `religion` | Religious affiliation | 1–12 (various denominations), 0=missed |
| `orientation` | Sexual orientation | 1–5, 0=missed |
| `race` | Racial/ethnic background | 1–13, 0=missed |
| `voted` | Has voted in national election | 1=yes, 2=no |
| `engnat` | English native speaker | 1=yes, 2=no |

### Vocabulary Check (VCL1 – VCL16)

The dataset includes a vocabulary validity check — 16 words where respondents indicated whether they knew the word (1) or not (0). Three of these are **fake words** that don't exist: **VCL6, VCL9, VCL12**. Anyone who claims to know multiple fake words may have been responding carelessly. You can use this to filter low-quality responses.

### Technical/Timing Variables

| Variable | Description |
|----------|-------------|
| `screensize` | Screen resolution |
| `source` | How they found the test (0–2) |
| `introelapse` | Time spent on intro page (seconds) |
| `testelapse` | Time spent on DASS items (seconds) |
| `surveyelapse` | Time spent on demographics (seconds) |
| `Q1E – Q42E` | Response time for each DASS item (milliseconds) |
| `Q1I – Q42I` | Item presentation position |

**Warning about response times:** The item response time variables (Q1E, Q2E, etc.) capture how long someone took on each question — they measure test-taking behaviour, not depression. Including them as features may inflate your R² without adding psychological meaning. This is a deliberate trap to illustrate that "more features" doesn't always mean "better model."

## Getting Started

### Suggested Approach

1. **Load the data** — use `pd.read_csv("data/dass42_data.csv", sep="\t")` and check the shape
2. **Clean the data** — filter out unreasonable ages (e.g., keep 10–100), remove rows with careless responding (VCL fake words)
3. **Ask your AI to plan** — before writing any modelling code, have the AI create a step-by-step analysis plan
4. **Score the DASS Depression subscale** — recode items 1–4 to 0–3 (subtract 1), sum the 14 Depression items
5. **Score the Big Five** — compute the 5 TIPI scales with reverse scoring
6. **Choose features** — start with Big Five, add demographics if you want
7. **Split the data** — 80% train, 20% test (use `random_state=42` so results are reproducible)
8. **Build a baseline** — predict the mean for everyone, calculate MAE and R²
9. **Build and cross-validate models** — LinearRegression, Ridge, Lasso with 5-fold CV
10. **Compare, interpret, and document** — which model wins? What do the coefficients mean?

### Starter LLM Prompts

**Planning prompt (use this first):**

> "I have a pandas DataFrame called `data` loaded from a tab-separated file with 39,775 rows and 172 columns. This is real survey data from the Depression Anxiety Stress Scales (DASS-42). The key variables are: 42 DASS items (Q1A–Q42A, coded 1–4), which need recoding to 0–3 and summing into Depression, Anxiety, and Stress subscales. The target is DASS Depression (14 items, total 0–42). Potential features include: Big Five personality (TIPI1–TIPI10), demographics (age, gender, education, urban, married, familysize, orientation, race), and vocabulary check items (VCL1–VCL16, where VCL6, VCL9, VCL12 are fake words for validity screening). Create a plan for building and comparing regression models (linear regression, Ridge, and Lasso) to predict depression scores from personality and demographics. Include: how to score the DASS subscales, which features to use and why, how to handle data quality (careless responding, bad age entries), how to split the data, how to evaluate the models, and how to compare them. Don't write code yet — just the plan."

**Code prompt (after you've reviewed the plan):**

> "Following my analysis plan, write Python code using scikit-learn to: (1) recode the 14 DASS Depression items from 1–4 to 0–3 and sum them, (2) compute Big Five scores from the TIPI items (reverse-score items 2, 4, 6, 8, 10), (3) select features and handle preprocessing (filter bad age entries, encode categorical demographics), (4) split into 80% train and 20% test, (5) calculate the mean-prediction baseline MAE and R², (6) fit and cross-validate (5-fold) a LinearRegression, Ridge, and Lasso, reporting mean MAE and R² for each, (7) create a bar chart comparing the four models' cross-validated MAE. Use pandas, numpy, matplotlib, and sklearn."

**Debugging prompt (for when things break):**

> "I'm getting this error when running my regression pipeline: [paste full traceback]. I was trying to [describe what you were doing]. My data has these columns: [paste df.columns]. What went wrong and how do I fix it? Explain what caused the error, not just how to fix it."

### Starter Code

Open [`starter.ipynb`](starter.ipynb) for a scaffolded notebook with imports and data loading already set up, or [`starter.py`](starter.py) for a script workflow.

## What to Present

Prepare **1 HTML slide** summarising your group's solution for the start of Week 5 (~3 min per group). Build it using <a href="https://revealjs.com" target="_blank">reveal.js</a> with the help of any AI tool — a browser chatbot (ChatGPT, Gemini, Claude), VS Code with Copilot, or anything else. A <a href="../../resources/presentation-template/">starter template</a> and <a href="../../resources/html-slides-guide.md">step-by-step guide</a> are provided, but you can design it however you like.

**Submitting your slide:** Put your HTML file, `css/` folder (if used), and any images into a folder named `GroupN_Week4` (e.g., `Group3_Week4`). Zip the folder and have **one group member** email it to **michael.j.richardson@mq.edu.au** with subject line `PSYC4411 Challenge Lab - Group N - Week 4`. **Deadline: 12pm (noon) Monday of Week 5.** No PDF needed for challenge lab presentations.

**Tip:** Test before sending — email the zip to yourself first, download it, unzip it, and open the HTML file in your browser. If it displays as you expect, you're good to send.

Your slide should include:

1. **Your best model** — which model performed best? What was the cross-validated MAE and R²?
2. **Feature importance** — which personality traits mattered most for predicting depression? Show the coefficients.
3. **Key interpretation** — in 1–2 sentences, what does the model tell us about personality and depression? Does it match psychological intuition?
4. **Overfitting check** — was there a gap between training and cross-validated performance? What does that tell you?
5. **One debugging story** — what broke, and how did you fix it with your AI assistant?

## Bonus Challenges

Finished early? Try one of these extensions:

1. **Learning curves** — Plot training vs validation error as a function of training set size. Is your model underfitting or overfitting? Ask your AI about `sklearn.model_selection.learning_curve`.

2. **Residual analysis** — Plot predicted vs actual values, and residuals vs predicted. Are there patterns the model misses? Non-linear relationships?

3. **Feature engineering** — Try adding interaction terms (e.g., Extraversion × Emotional Stability) or polynomial features (Age²). Does it improve the model?

4. **Compare DASS subscales** — Run the same pipeline for DASS Anxiety and DASS Stress. Do the same features predict all three, or do they differ?

5. **Lasso regularisation path** — Plot how coefficients change as Lasso's alpha parameter varies. Which features survive the strongest regularisation? Ask your AI about `sklearn.linear_model.lasso_path`.

6. **Response time trap** — If you include item response times (Q1E, Q2E, etc.) as features, you may get a surprisingly high R². But response time captures test-taking behaviour, not depression. Discuss: is this a meaningful prediction, or is the model learning an artefact?

7. **Data quality filtering** — Use the vocabulary check items (VCL6, VCL9, VCL12 are fake words — anyone who claims to know them may be responding carelessly). Filter out participants who checked 2+ fake words. Does the model improve? This teaches a real data science skill: cleaning data before modelling.

8. **Real data: Boston College COVID Sleep & Wellbeing** — Try your regression pipeline on a different real dataset (already downloaded to `data/boston_college/`). This is daily survey data from ~1,484 adults during early COVID-19, with PHQ-9 depression, sleep diary, exercise, and affect data. Can you predict depression from sleep and lifestyle variables?

9. **Synthetic vs real** — Go back to the Week 2 synthetic DASS-21 dataset (`lifestyle_mental_health.csv`, 3,000 rows). Run the same regression pipeline. How do the results compare? Is it easier or harder to predict depression in synthetic vs real data?

## Hints

<details>
<summary>Hint 1: Which features to start with</summary>

Begin with just the Big Five personality scores (computed from the TIPI items). These are the theoretically motivated predictors — Emotional Stability in particular has a strong negative correlation with depression (r ≈ −0.52 in this dataset). Add demographics later and see if they help. **Don't include DASS Anxiety or Stress as features** — that would be circular (they're measured by the same questionnaire).

</details>

<details>
<summary>Hint 2: Scoring the DASS</summary>

The raw items (Q1A–Q42A) are coded 1–4. Recode to 0–3 first (subtract 1). Then sum the 14 Depression items: Q3, Q5, Q10, Q13, Q16, Q17, Q21, Q24, Q26, Q31, Q34, Q37, Q38, Q42. In pandas, this looks like:

```python
dep_items = [f'Q{i}A' for i in [3, 5, 10, 13, 16, 17, 21, 24, 26, 31, 34, 37, 38, 42]]
data['DASS_Depression'] = data[dep_items].sub(1).sum(axis=1)
```

Ask your AI to help if you're unsure about the syntax.

</details>

<details>
<summary>Hint 3: Handling categorical variables</summary>

Gender and education are coded as numbers (1=Male, 2=Female, 3=Other; 0–4 for education). You can use them as-is for a first attempt, but for linear regression, treating ordered numbers as continuous may not capture the right relationships. Ask your AI about `pd.get_dummies()` for one-hot encoding.

</details>

<details>
<summary>Hint 4: Data quality</summary>

Check the age column — some entries are clearly wrong (e.g., age = 1998, which is probably a birth year). Filter these out (e.g., keep ages 10–100). Also consider using the vocabulary check: VCL6, VCL9, VCL12 are fake words. Anyone who claims to know 2 or more fake words may have been responding carelessly — about 2.9% of the sample.

</details>

<details>
<summary>Hint 5: Cross-validation code</summary>

The key function is `sklearn.model_selection.cross_val_score`. Ask your AI: "Show me how to do 5-fold cross-validation with Ridge regression using `cross_val_score`, reporting both MAE and R²." Remember that scikit-learn's MAE scoring returns negative values (it maximises, so it negates the error) — you'll need to negate the result.

</details>

<details>
<summary>Hint 6: Interpreting R²</summary>

In behavioural science, R² values for predicting individual behaviour from survey data are typically 0.10–0.35. An R² around 0.33 using Big Five personality as predictors is actually quite good for this kind of data. If your R² is above 0.50, check whether you accidentally included item response times or other artefactual variables.

</details>

---

*[Back to course overview](../../README.md)*

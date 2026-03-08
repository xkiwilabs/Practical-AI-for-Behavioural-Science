# Analysis Plan: Lifestyle Factors and Depression Visualisation

## Research Question

What lifestyle factors are most strongly associated with depression scores in this dataset, and can we see these relationships clearly in a multi-panel figure?

## Step 1: Explore the Data First

Before deciding what to visualise, we need to understand what's in the dataset:

1. **Summary statistics** — check means, SDs, ranges, and missing values for all variables
2. **Correlation matrix** — compute Pearson correlations between all numeric variables and DASS_Depression. This tells us which variables have the strongest linear associations.
3. **Pairplot** — create a scatter grid of the most promising variables to see the *shape* of each relationship (linear? curved? clustered?)

This exploration will guide our variable selection — we'll focus on the variables that actually show interesting patterns rather than guessing.

## Dataset

- **File:** `data/lifestyle_mental_health.csv`
- **Size:** 3,000 participants x 44 variables
- **Key variable groups:**
  - Demographics: Age, Gender, Occupation, Income_AUD, Relationship_status
  - Lifestyle: Sleep_hrs_night, Exercise_hrs_week, SocialMedia_hrs_week, Screen_time_hrs_day, Caffeine_cups_day, Alcohol_drinks_week, Study_hrs_week
  - Mental health: DASS_Depression, DASS_Anxiety, DASS_Stress (each scored 0-42, from the DASS-21 questionnaire)
  - Wellbeing: Life_satisfaction (1-10), Social_Support_score (1-10)
- **Missing values:** ~2-3% in lifestyle columns (realistic — people skip questions or sensors fail)

## Step 2: Figure Layout

A **2x2 grid** of scatter plots, each showing DASS_Depression on the y-axis against a different lifestyle variable on the x-axis.

### Panel 1 (top-left): Sleep vs Depression
- **Relationship:** More sleep -> lower depression (negative association)
- **Plot type:** Scatter plot with linear trend line
- **Visual features:** Small, semi-transparent points (alpha = 0.3); red trend line

### Panel 2 (top-right): Exercise vs Depression
- **Relationship:** More exercise -> lower depression (negative association)
- **Plot type:** Scatter plot with linear trend line
- **Visual features:** Same styling as Panel 1 for consistency

### Panel 3 (bottom-left): Social Media vs Depression
- **Relationship:** More social media use -> higher depression (positive association)
- **Plot type:** Scatter plot with linear trend line
- **Visual features:** Same styling; this should show an upward trend (opposite direction to sleep and exercise)

### Panel 4 (bottom-right): Study Hours vs Depression
- **Relationship:** More study hours -> higher depression (positive association)
- **Plot type:** Scatter plot with linear trend line
- **Visual features:** This one is interesting — study hours might be a proxy for academic stress

## Styling

- **Figure size:** 12 x 10 inches
- **Overall title:** "Lifestyle Factors and Depression: Exploring Key Relationships"
- **Colour palette:** Use seaborn's default with alpha transparency
- **Clean up:** Use `sns.despine()` for clean borders; `plt.tight_layout()` for spacing
- **Font sizes:** 14pt for subplot titles, 12pt for axis labels

## Libraries

- `pandas` for data loading
- `matplotlib` for figure layout and customisation
- `seaborn` for scatter plots
- `numpy` for trend line calculations

## Output

Save the final figure as `our_visualisation.png` at 300 DPI.

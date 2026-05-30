# Analysis Plan: Exploring the Structure of Mental Distress

## Research Question

Is there meaningful structure in how people experience distress? Specifically: (1) what latent dimensions underlie the 42 DASS symptoms? (2) Are there subgroups of people with distinct personality-distress profiles? (3) Are those subgroups stable?

## Dataset

- **Source:** OpenPsychometrics DASS-42 + Big Five (TIPI) + demographics
- **Size:** 39,775 respondents, 172 variables
- **Same data as Week 4** — different question this time

## Step 1: Data Loading and Cleaning

1. Load `dass42_data.csv` (tab-separated)
2. Filter ages to 10–100 (remove birth years entered as age)
3. Remove careless responders: anyone who endorsed fake vocabulary words (VCL6, VCL9, VCL12)
4. Expected N after cleaning: ~34,500

## Step 2: Score Scales

1. Recode DASS items from 1–4 to 0–3 (subtract 1)
2. Score three DASS subscales (14 items each): Depression, Anxiety, Stress
3. Score Big Five from TIPI (reverse-score items 2, 4, 6, 8, 10; compute trait means)

## Step 3: PCA on 42 DASS Items

1. Standardise all 42 items (z-scores)
2. Fit PCA with all components
3. Create scree plot — look for the "elbow"
4. Examine cumulative variance explained
5. Interpret loadings for the top 3 components — which items load on which component?
6. Expect: 3-component solution matching Depression/Anxiety/Stress structure

## Step 4: UMAP Visualisation

1. Fit UMAP (2 components) on the standardised DASS items
2. Create scatter plot coloured by depression severity
3. Note: distances between clusters are NOT meaningful — only local structure is trustworthy

## Step 5: Clustering

1. Prepare 8 features: 5 Big Five + 3 DASS subscales
2. Standardise (k-means is sensitive to scale)
3. Run k-means for k = 2, 3, 4, 5
4. Evaluate: elbow plot (inertia) + silhouette scores
5. Profile the best k: mean feature values per cluster

## Step 6: Stability Checks

1. Rerun k-means with 5 different random seeds
2. Compare cluster assignments to the reference (seed=42)
3. Report percentage of participants who change cluster
4. If stability is low, try a different k

## Step 7: Documentation

1. Ask AI to draft a methods paragraph describing the analysis
2. Verify every number and method name matches the actual analysis
3. Correct any errors in the AI's draft

## Expected Outcome

The DASS-42 should show a clear 3-component structure (Depression, Anxiety, Stress). Clustering may find 2–3 groups differing primarily in overall distress severity. The large sample (34K+) should produce stable clusters, but the fundamental question is whether these clusters represent genuine "types" or are just arbitrary cuts on a continuous dimension.

# Final Plan: Depression and Lifestyle by Gender (Script Workflow)

> This is the updated plan reflecting what we actually built. Compare with the original `plan.md` to see what changed and why.

## What We Set Out to Do

The original plan was for a 2x2 scatter plot grid (same as the notebook solution) but using a Python script. After reviewing that plan, we decided to make the script version **different** from the notebook version — exploring the same data from a different angle (gender differences) rather than duplicating the same figure.

We also added a critical step that was missing from the original plan: **explore the data first**, before committing to a visualisation design.

## What We Actually Built

### Two scripts instead of one

1. **`explore_data.py`** — Exploration step (run first)
   - Prints summary statistics (mean, SD, min, max) for all variables
   - Reports missing values (~2-3% in lifestyle columns)
   - Computes correlations between lifestyle variables and DASS_Depression (excluding DASS items and subscales to avoid circularity)
   - Creates a correlation heatmap of key variables (`correlation_heatmap.png`)
   - Creates a pairplot of the most promising variables (`pairplot.png`)
   - The output of this script informed our choices in the visualisation script

2. **`visualise_key_variables.py`** — Focused visualisation (run second)
   - A **2x3 figure** exploring how lifestyle factors relate to depression, split by gender
   - **Top row:** Three scatter plots (sleep, exercise, social media vs DASS_Depression), with points and trend lines coloured by gender (Male, Female, Non-binary)
   - **Bottom row:** Three violin plots comparing depression scores for high vs low levels of each lifestyle factor, split by gender
   - Saves `depression_by_gender.png`

### Why two scripts?

Splitting exploration and visualisation into separate scripts is a common pattern in data science:
- **`explore_data.py`** is about understanding — you run it once, look at the outputs, and use what you learn to make decisions
- **`visualise_key_variables.py`** is about communication — it creates the polished figure you'd put on a slide or in a report
- Keeping them separate means you can re-run the visualisation without re-running the exploration, and vice versa

### Why the change from the original plan

1. **Exploration first** — The original plan jumped straight to "what figure should we make?" without first asking "what does the data look like?" The correlation analysis showed us which variables were most worth plotting.
2. **Avoid duplication** — The notebook already has the basic 2x2 scatter plot. The script should show something new.
3. **Gender and Non-binary representation** — The dataset includes Male, Female, and Non-binary categories. Splitting by gender reveals whether lifestyle-depression associations differ across groups.
4. **Violin plots show distributions** — Scatter plots show individual points; violin plots show the shape of the distribution. Using both gives a more complete picture.

## Key Findings

1. **The correlation analysis guided our choices** — Life satisfaction (r = -0.51) had the strongest association with depression, followed by sleep (r = -0.37) and study hours (r = +0.36). Exercise (r = -0.27) and social support (r = -0.28) were moderate. Height, weight, and siblings showed almost no association. Without the exploration step, we might have wasted time plotting irrelevant variables.

2. **Sleep and exercise show similar negative associations with depression across genders** — The trend lines run roughly parallel, suggesting the protective effect of sleep and exercise doesn't differ much by gender in this dataset.

3. **Social media shows a modest positive association with depression** — More social media hours are associated with slightly higher depression scores (r = +0.16). The scatter shows considerable spread, suggesting the relationship is real but other factors matter more.

4. **The violin plots reveal distribution differences** — The low-sleep group has a visibly higher and wider depression distribution than the high-sleep group. This is clearer in the violin plot than in the scatter.

5. **Missing values were handled by dropping affected rows** — About 2-3% of lifestyle values were missing. We used `dropna()` on the variables needed for each plot, which is a straightforward approach for this level of missingness.

## What We Learned About the Script Workflow

- **Exploring the data first** was the most important change from the original plan. It took 5 minutes and saved us from guessing which variables to plot.
- **Two scripts is better than one** for this kind of analysis. The exploration script is messy and informational; the visualisation script is polished and presentational. Different purposes, different code.
- **Planning in a `.md` file** made it easy to iterate on the design before writing code. We changed the figure layout twice in the plan before writing a single line of Python.
- **Running from the terminal** (`python explore_data.py && python visualise_key_variables.py`) was quick — no need to restart kernels or worry about cell execution order.
- **Saving to PNG** was natural in the script workflow. The output files are the deliverables, not the code.

## Tools Used

- pandas, numpy, matplotlib, seaborn
- Ran with: `conda activate psyc4411-env && python explore_data.py && python visualise_key_variables.py`

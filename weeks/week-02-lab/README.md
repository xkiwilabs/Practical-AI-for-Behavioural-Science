# Week 2 Challenge Lab: Visualising Lifestyle and Mental Health

## The Challenge

Create a beautiful, multi-panel visualisation that explores the relationships between lifestyle factors (sleep, exercise, screen time) and depression in a synthetic psychology dataset. Use an LLM coding assistant to help write the Python code. **Success = a figure that could appear in a research presentation.**

This is a group challenge. You'll work together during class and prepare a 1-slide, ~3-minute presentation for Week 3.

> **Note:** This is practice for creating HTML slides and presenting your work. The formal Paper Presentation assessment (20% of your grade) starts in Week 4 and is about a research paper you choose, not a lab challenge. See [assessments/presentation.md](../../assessments/presentation.md) for details.

## Background

This challenge puts the **LLM Problem-Solving Loop** from Week 1 into practice. You'll:
- **Plan** what relationships to explore and how to visualise them
- **Engineer prompts** that give the AI enough context to produce useful code
- **Verify** that the code runs and the output makes sense
- **Refine** your prompts and your figure until it looks great
- **Document** what you did and what you learned

The emphasis is on **prompt engineering** — the more context you give your LLM assistant (what your data looks like, what libraries you're using, what you want to achieve), the better the code it generates. LLMs make mistakes. They'll sometimes produce code that doesn't run, uses the wrong variable names, or creates a plot that doesn't match what you asked for. That's expected. The skill you're building is knowing how to identify the problem and guide the AI to a better solution.

## Dataset

The data is in [`data/fake_depression_dataset.csv`](data/fake_depression_dataset.csv) — a synthetic dataset with 2,000 participants and 12 variables related to lifestyle and mental health. This is simulated data designed for teaching, not real clinical data, but it has realistic patterns built in.

| Variable | Description | Type | Range |
|----------|-------------|------|-------|
| `Age` | Participant's age in years | Continuous | 18–65 |
| `Gender` | Self-reported gender | Categorical | Male, Female |
| `Height_cm` | Height in centimetres | Continuous | ~145–195 |
| `Weight_kg` | Weight in kilograms | Continuous | ~40–110 |
| `TV_hrs_week` | Hours of TV watched per week | Continuous | 0–30 |
| `VideoGames_hrs_week` | Hours of video games per week | Continuous | 0–20 |
| `Siblings` | Number of siblings | Discrete | 0–5 |
| `FB_Friends` | Number of Facebook friends | Discrete | ~100–1000 |
| `SocialMedia_hrs_week` | Hours on social media per week | Continuous | 0–50 |
| `Sleep_hrs_night` | Average hours of sleep per night | Continuous | ~4–9 |
| `Exercise_hrs_week` | Hours of exercise per week | Continuous | 0–7 |
| `Depression` | Depression symptom score | Continuous | ~0–10 |

**Some interesting relationships to explore:**
- Sleep and exercise tend to be associated with lower depression scores
- Screen time (social media, TV, video games) tends to be associated with higher depression scores
- There's a quadratic (U-shaped or inverted-U) relationship between age and depression
- Some variables interact — for example, the relationship between screen time and depression might look different for different age groups
- Not every variable is interesting — finding that out is part of the process

## Getting Started

Open [`starter.ipynb`](starter.ipynb) — the imports and data loading are already done for you.

### Suggested Approach

1. **Explore the data** — Run the cells that show the data's shape, summary statistics, and missing values. Get a feel for what's in the dataset.

2. **PLAN your visualisation** — Choose 3–4 relationships you want to show. Think about what story you want to tell. A multi-panel figure works well here (e.g., a 2×2 grid of scatter plots, each showing a different relationship).

3. **ENGINEER your prompt** — Before you type anything into ChatGPT or Copilot, plan what you're going to ask for. Include:
   - What your data looks like (column names, types)
   - What type of plot you want (scatter, bar, box, etc.)
   - What layout you want (how many panels, grid arrangement)
   - What libraries you're using (`matplotlib` and `seaborn`)
   - Any specific visual features (colours, labels, trend lines)

4. **PROMPT** — Send your carefully engineered prompt to your LLM assistant.

5. **VERIFY** — Paste the code into your notebook and run it. Does it work? Does the output look right? Check the axis labels, the variable names, and whether the patterns make sense.

6. **REFINE** — Adjust colours, labels, layout, and spacing. Fix any errors. If the AI got something wrong, tell it what went wrong and ask it to fix it (with more context this time).

7. **DOCUMENT** — Add markdown cells explaining your figure. Save the final version as a PNG.

### Starter LLM Prompts

Here are four example prompts that demonstrate good prompt engineering — notice how each one gives the AI specific context about the data and tools:

**Prompt 1 — Creating a multi-panel scatter plot:**
> "I have a pandas DataFrame called `data` with columns including `Sleep_hrs_night`, `Exercise_hrs_week`, `SocialMedia_hrs_week`, and `Depression` (all continuous). Using matplotlib and seaborn, create a 2×2 figure with four scatter plots, each showing Depression on the y-axis against a different lifestyle variable on the x-axis. Use `sns.scatterplot` with a small marker size and some transparency. Add a descriptive title to each subplot."

**Prompt 2 — Adding trend lines:**
> "I have a scatter plot created with matplotlib showing Depression vs Sleep_hrs_night. How do I add a linear trend line using numpy's `polyfit`? Show me the code to overlay the trend line on the existing scatter plot in red."

**Prompt 3 — Colouring by a categorical variable:**
> "In my DataFrame `data`, there's a column called `Gender` with values 'Male' and 'Female'. I'm creating a scatter plot of Depression vs Exercise_hrs_week using seaborn. How do I colour the points by Gender and add a legend? Use seaborn's `hue` parameter."

**Prompt 4 — Fixing layout issues:**
> "My matplotlib 2×2 subplot figure has overlapping axis labels and titles. The figure size is (10, 8). How do I fix the spacing? I've tried `plt.tight_layout()` but the titles still overlap with the plot above."

## What to Present

Prepare **1 HTML slide** for the start of Week 3 (~3 minutes per group). Build it using <a href="../../resources/html-slides-guide.md">reveal.js with the help of an LLM coding assistant</a> — a <a href="../../resources/presentation-template/">starter template</a> is provided, but you can design it however you like. Export it as a **PDF** for submission.

Your slide should include:

1. **Your final figure** — the multi-panel visualisation you created
2. **Your approach** — which relationships did you choose and why?
3. **One key finding** — what's the most interesting pattern you found in the data?
4. **One thing about prompting** — what did you learn about communicating with an LLM? What worked well, or what was surprisingly hard?

## Hints

<details>
<summary>Hint 1: Choosing which relationships to visualise</summary>

Start with the variables that are most likely connected to depression: `Sleep_hrs_night`, `Exercise_hrs_week`, and `SocialMedia_hrs_week` are good candidates. For a fourth panel, try `Age` — there's an interesting non-linear pattern there.

Don't feel like you need to include every variable. A focused figure with 4 well-chosen panels tells a better story than 12 cramped panels trying to show everything.

</details>

<details>
<summary>Hint 2: Multi-panel figure layout</summary>

The basic structure for a 2×2 figure in matplotlib is:

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Top-left panel
sns.scatterplot(data=data, x="Sleep_hrs_night", y="Depression", ax=axes[0, 0])
axes[0, 0].set_title("Sleep vs Depression")

# Top-right panel
sns.scatterplot(data=data, x="Exercise_hrs_week", y="Depression", ax=axes[0, 1])
axes[0, 1].set_title("Exercise vs Depression")

# ... and so on for axes[1, 0] and axes[1, 1]

plt.tight_layout()
plt.show()
```

You don't need to memorise this — ask your LLM assistant to generate it. But understanding the structure (a grid of axes, indexed by row and column) helps you debug issues.

</details>

<details>
<summary>Hint 3: Making figures look polished</summary>

A few small touches that make a big difference:

- **Transparency:** Add `alpha=0.4` to your scatter plots when you have many points — it helps show density
- **Colour palette:** Use `palette="Set2"` or `palette="husl"` in seaborn for pleasing colours
- **Figure title:** Add an overall title with `fig.suptitle("Your Title", fontsize=16, fontweight='bold')`
- **Font sizes:** Increase them — `fontsize=12` for axis labels, `fontsize=14` for subplot titles
- **Remove clutter:** Use `sns.despine()` to remove the top and right borders from plots
- **Spacing:** If `plt.tight_layout()` isn't enough, try `plt.subplots_adjust(hspace=0.3, wspace=0.3)`

Ask your LLM assistant: "How can I make this matplotlib figure look more professional and polished?"

</details>

---

*[Back to course overview](../../README.md)*

# Week 2 Challenge Lab: Visualising Lifestyle and Mental Health

> **New to Python packages?** See the [Packages Glossary](../../resources/packages-glossary.md) for a plain-English guide to every package used in this course — what it does, why we chose it, and when you'll use it.

## The Challenge

Create a beautiful, multi-panel visualisation that explores the relationships between lifestyle factors (sleep, exercise, screen time) and depression in a synthetic psychology dataset. Use an LLM coding assistant to help write the Python code. You'll try **two different coding workflows** — Jupyter notebooks and Python scripts — to find which suits you best. **Success = a figure that could appear in a research presentation.**

This is a group challenge. You'll work together during class and prepare a 1-slide, ~3-minute presentation for Week 3.

> **Note:** This is practice for creating HTML slides and presenting your work. The formal Paper Presentation assessment (20% of your grade) starts in Week 4 and is about a research paper you choose, not a lab challenge. See [assessments/presentation.md](../../assessments/presentation.md) for details.

## Background

This challenge puts the **LLM Problem-Solving Loop** from Week 1 into practice:

**Outer loop (your research process):** PLAN → EXECUTE → EVALUATE → DOCUMENT

**Inner loop (working with the AI):** ENGINEER → PROMPT → VERIFY → REFINE

The key lesson from Week 1: **ask the AI to plan first.** Before it writes any code, ask it to outline its approach. A written plan catches misunderstandings early — it's much easier to say "actually, let's use violin plots instead of box plots" when you're looking at a plan than after the AI has written 50 lines of code. Planning saves iteration cycles and produces better results.

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

## Two Ways to Code

In this lab, you'll try two different workflows for writing code with an AI assistant. Neither is "better" — researchers and data scientists use both depending on the task. Trying both now means you can make an informed choice for future weeks.

### Option A: Jupyter Notebook

- **Interactive, cell-by-cell execution** — you run code in small chunks and see results immediately
- Documentation lives in **markdown cells** alongside your code
- **Plan-first approach:** Have the AI write the analysis plan as markdown cells in the notebook. Review the plan. Only then ask for code.
- Good for: exploratory analysis, seeing results immediately, mixing notes and code

### Option B: Python Scripts

- Code lives in **`.py` files**, documentation in **`.md` files**
- You run the whole script from the terminal with `python starter.py`
- **Plan-first approach:** Have the AI create a `plan.md` file. Review and iterate on the plan. Then have the AI create (or edit) a `.py` script. Review the code. Run it.
- Good for: reproducible workflows, cleaner code, version control, larger projects
- Your AI assistant can **create new files**, **edit existing files**, and **add new sections** to files — use this to build up your script and documentation piece by piece

### Which should I use later?

You'll choose one workflow for future labs. Some people prefer the immediacy of notebooks; others prefer the tidiness of scripts. There's no wrong answer — the point of this lab is to try both so you have an informed preference.

## Getting Started

### Part 1: Notebook Workflow (~45 min)

Open [`starter.ipynb`](starter.ipynb) — the imports and data loading are already done for you.

1. **Explore the data** — Run the setup cells to see the data's shape, summary statistics, and missing values. Get a feel for what's in the dataset.

2. **PLAN** — In your AI assistant (Copilot Chat, ChatGPT, Claude, etc.), ask it to create an analysis plan for a multi-panel visualisation. The plan should go in a markdown cell in your notebook — review it before any code is written. Does the approach make sense? Would the panels tell a coherent story? Revise with the AI if needed. This is the **PLAN** step of the outer loop — a good plan means fewer iterations in the inner loop.

3. **ENGINEER your prompt** — Based on your reviewed plan, write a detailed prompt for the code. Include what your data looks like (column names, types), what type of plots you want, the layout, the libraries, and any visual features. The notebook has a weak vs strong prompt comparison to guide you.

4. **EXECUTE** — Send your prompt to the AI and paste the code into your notebook. Run each cell.

5. **VERIFY & REFINE** — Check the output. Are the axes correct? Do the patterns make sense? Does it look professional? Fix issues by sending error messages or feedback back to the AI.

6. **DOCUMENT** — Add markdown cells reflecting on what you found and what you learned.

### Part 2: Script Workflow (~45 min)

For the second half of the lab, try creating a visualisation using Python scripts instead of a notebook. A starter template is provided at [`starter.py`](starter.py) with the imports and data loading already done.

1. **PLAN** — Ask your AI assistant to create a `plan.md` file for a different visualisation (or extension) of the same dataset. The plan should outline: what relationships to explore, what plot types to use, what the final figure layout should look like, and what libraries to use. Review the plan. Iterate — "Actually, let's use violin plots instead of box plots for the gender comparison" — until you're satisfied.

2. **EXECUTE** — Ask the AI to edit `starter.py` (or create a new `.py` script) that implements the plan. The script should load the data, create the visualisation, and save it as a PNG. Your AI assistant can **create new files**, **edit existing ones**, and **build up your project piece by piece** — you don't need to write everything in one go.

3. **RUN** — In the terminal:
   ```
   conda activate psyc4411-env
   python starter.py
   ```

4. **VERIFY & REFINE** — Check the saved PNG. If it needs changes, ask the AI to edit the script and re-run.

5. **DOCUMENT** — Have the AI update `plan.md` with what actually happened — key findings, changes from the original plan, and any surprises. You can also have the AI add new sections to your notebook summarising the script results.

## Starter LLM Prompts

Here are example prompts that demonstrate good prompt engineering. Notice how each one gives the AI specific context about the data and tools.

### Planning Prompts

**For the notebook workflow:**
> "Based on the dataset I've loaded (columns: Age, Gender, Height_cm, Weight_kg, TV_hrs_week, VideoGames_hrs_week, Siblings, FB_Friends, SocialMedia_hrs_week, Sleep_hrs_night, Exercise_hrs_week, Depression — all described in the data dictionary above), write an analysis plan for a 2×2 multi-panel scatter plot figure exploring lifestyle factors and depression. Write the plan as a numbered list in markdown — what goes in each panel, what relationships we're testing, and what visual features to include. Don't write any code yet."

**For the script workflow:**
> "I have a CSV dataset at `data/fake_depression_dataset.csv` with 2000 rows and columns: Age, Gender, Height_cm, Weight_kg, TV_hrs_week, VideoGames_hrs_week, Siblings, FB_Friends, SocialMedia_hrs_week, Sleep_hrs_night, Exercise_hrs_week, Depression. Create a `plan.md` file that outlines a visualisation comparing depression scores across lifestyle factors. Include: which relationships to plot, what plot types to use, what the final figure layout should look like, and what libraries to use (matplotlib, seaborn). Don't write any code yet — just the plan."

### Code Prompts

**Prompt 1 — Creating a multi-panel scatter plot:**
> "I have a pandas DataFrame called `data` with columns including `Sleep_hrs_night`, `Exercise_hrs_week`, `SocialMedia_hrs_week`, and `Depression` (all continuous). Using matplotlib and seaborn, create a 2×2 figure with four scatter plots, each showing Depression on the y-axis against a different lifestyle variable on the x-axis. Use `sns.scatterplot` with a small marker size and some transparency. Add a descriptive title to each subplot."

**Prompt 2 — Adding trend lines:**
> "I have a scatter plot created with matplotlib showing Depression vs Sleep_hrs_night. How do I add a linear trend line using numpy's `polyfit`? Show me the code to overlay the trend line on the existing scatter plot in red."

**Prompt 3 — Colouring by a categorical variable:**
> "In my DataFrame `data`, there's a column called `Gender` with values 'Male' and 'Female'. I'm creating a scatter plot of Depression vs Exercise_hrs_week using seaborn. How do I colour the points by Gender and add a legend? Use seaborn's `hue` parameter."

**Prompt 4 — Fixing layout issues:**
> "My matplotlib 2×2 subplot figure has overlapping axis labels and titles. The figure size is (10, 8). How do I fix the spacing? I've tried `plt.tight_layout()` but the titles still overlap with the plot above."

## What to Present

Prepare **1 HTML slide** for the start of Week 3 (~3 minutes per group). Build it using <a href="https://revealjs.com" target="_blank">reveal.js</a> with the help of any AI tool you like — a browser chatbot (ChatGPT, Gemini, Claude), VS Code with Copilot, or anything else. Most chatbots can generate the HTML file for you directly in the conversation. A <a href="../../resources/presentation-template/">starter template</a> and <a href="../../resources/html-slides-guide.md">step-by-step guide</a> are provided, but you can design it however you like.

**Submitting your slide:** Put your HTML file, `css/` folder (if used), and any images into a folder named `GroupN_Week2` (e.g., `Group3_Week2`). Zip the folder and have **one group member** email it to **michael.j.richardson@mq.edu.au** with subject line `PSYC4411 Challenge Lab - Group N - Week 2`. **Deadline: 12pm (noon) Monday of Week 3.** No PDF needed for challenge lab presentations.

**Tip:** Test before sending — email the zip to yourself first, download it, unzip it, and open the HTML file in your browser. If it displays as you expect, you're good to send.

Your slide should include:

1. **Your final figure** — the multi-panel visualisation you created
2. **Your approach** — which relationships did you choose and why?
3. **One key finding** — what's the most interesting pattern you found in the data?
4. **One thing about prompting** — what did you learn about communicating with an LLM? What worked well, or what was surprisingly hard?
5. **Notebook vs. scripts** — which workflow did you prefer and why? Did the plan-first approach change how you worked with the AI?

## Bonus Challenges

Finished early? Try one of these — they work in either the notebook or the script workflow. Have your AI assistant create new files, edit existing ones, or add new sections to your notebook.

1. **Correlation heatmap:** Ask your AI to create a correlation matrix heatmap showing the relationships between all numeric variables at once. Use `sns.heatmap` with `data.corr()`. Try it as a new cell in your notebook *and* as a standalone script — see which workflow feels more natural.

2. **Group comparison:** Create box plots or violin plots comparing Depression scores across different groups — for example, high vs. low social media users (split at the median), or Male vs. Female participants.

3. **Interactive exploration:** Ask your AI about `seaborn.pairplot` — it creates a grid of scatter plots for every pair of variables. What patterns do you notice that you didn't see in your multi-panel figure?

4. **Annotation:** Add text annotations to your figure highlighting the most interesting findings (e.g., "r = -0.45" next to a strong correlation, or an arrow pointing to an interesting cluster of points).

5. **Multiple output files:** Have the AI create a script that generates several different figures, each saved as a separate PNG. Then have the AI create a summary `.md` file that describes what each figure shows and what patterns were found.

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

<details>
<summary>Hint 4: Running a Python script from the terminal</summary>

If you haven't used the terminal before, here's the step-by-step:

1. Open a terminal in VS Code (Terminal → New Terminal, or `` Ctrl+` ``)
2. Make sure you're in the right folder: `cd weeks/week-02-lab`
3. Activate your environment: `conda activate psyc4411-env`
4. Run the script: `python starter.py`
5. If the script saves a figure, it will appear as a new file in your folder

If you get an error, copy the full error message and send it to your AI assistant — it will help you debug.

</details>

---

*[Back to course overview](../../README.md)*

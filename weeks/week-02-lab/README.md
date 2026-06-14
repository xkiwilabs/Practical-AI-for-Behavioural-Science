# Week 2 Challenge Lab: Visualising Lifestyle and Mental Health

## The Challenge

Create a beautiful, multi-panel visualisation that explores the relationships between lifestyle factors (sleep, exercise, screen time) and depression in a synthetic psychology dataset. Use an LLM coding assistant to help write the Python code. You'll try **two different coding workflows** — Jupyter notebooks and Python scripts — to find which suits you best. **Success = a figure that could appear in a research presentation.**

This is a group challenge. You'll work together and prepare a short 1-slide, ~3-minute presentation to share with the class.

> **Note:** This is good practice for creating HTML slides and presenting your work — a skill you'll reuse throughout the course.

## Background

This challenge puts the **LLM Problem-Solving Loop** from Week 1 into practice:

**Outer loop (your research process):** PLAN → EXECUTE → EVALUATE → DOCUMENT

**Inner loop (working with the AI):** ENGINEER → PLAN → GENERATE → VERIFY → REFINE

The key lesson from Week 1: **planning is a core step, not an afterthought.** In the ENGINEER step, craft your prompt with context and ask for a plan. In the PLAN step, the AI responds with a proposed approach — review it critically before it generates anything. A written plan catches misunderstandings early — it's much easier to say "actually, let's use violin plots instead of box plots" when you're looking at a plan than after the AI has written 50 lines of code. Your first few trips around the inner loop are often about refining the plan itself; only later iterations shift to generating the actual output.

The emphasis is on **prompt engineering** — the more context you give your LLM assistant (what your data looks like, what libraries you're using, what you want to achieve), the better the code it generates. LLMs make mistakes. They'll sometimes produce code that doesn't run, uses the wrong variable names, or creates a plot that doesn't match what you asked for. That's expected. The skill you're building is knowing how to identify the problem and guide the AI to a better solution.

## Use Whatever AI Tools You Like

There are no rules about which AI tools you use for this challenge. Use whatever works for you:

- **Inside VS Code:** GitHub Copilot comes built-in, but you can also install the **Gemini Code Assist**, **Claude Code**, and **Codex** (OpenAI) extensions from the VS Code marketplace. Each gives you Chat, Edit, and Agent modes. Gemini works with any Gmail account, and both Gemini and Codex offer a **free usage tier** — so if you hit the limit on one, just switch to another.
- **Browser chatbots:** ChatGPT, Claude, Gemini — copy and paste code back and forth
- **CLI tools:** If you've installed Claude Code, Codex, or similar command-line tools, feel free to use them
- **Mix and match:** Use a browser chatbot for brainstorming and VS Code for writing code — there's no single "right" setup

That said, **getting comfortable with AI tools inside VS Code will make your life easier** as the semester goes on. When the AI can see your files, run your code, read error messages, and fix problems directly, the feedback loop is much tighter than copying and pasting between a browser and your editor. Over the coming weeks you'll see how **LLM → Code → Solution** — having an AI write and run code to produce a figure, analysis, or document — is more powerful and reproducible than asking an AI to generate those outputs directly.

## Dataset

The data is in [`data/lifestyle_mental_health.csv`](data/lifestyle_mental_health.csv) — a synthetic dataset with 3,000 participants and 44 variables related to lifestyle, demographics, and mental health. This is simulated data designed for teaching, not real clinical data, but it has realistic patterns, correlations, and distributions built in.

The mental health measures use the **DASS-21** (Depression Anxiety Stress Scales) — a real psychometric instrument widely used in Australian psychology research. Each participant answered 21 questions scored 0–3, and these are summed into three subscale scores.

### Demographics

| Variable | Description | Type | Values/Range |
|----------|-------------|------|--------------|
| `Age` | Participant's age in years | Integer | 18–65 |
| `Gender` | Self-reported gender | Categorical | Male, Female, Non-binary |
| `Relationship_status` | Current relationship status | Categorical | Single, In a relationship, Married/De facto |
| `Occupation` | Employment category | Categorical | Student, Employed full-time, Employed part-time, Self-employed, Unemployed, Retired |
| `Siblings` | Number of siblings | Integer | 0–5 |
| `Parents_university` | At least one parent attended university | Categorical | Yes, No |
| `Height_cm` | Height in centimetres | Integer | ~148–198 |
| `Weight_kg` | Weight in kilograms | Integer | ~42–120 |
| `Income_AUD` | Annual household income (AUD) | Integer | ~$2,600–$250,000 |

### Lifestyle

| Variable | Description | Type | Range |
|----------|-------------|------|-------|
| `Sleep_hrs_night` | Average hours of sleep per night | Continuous | ~4–10 |
| `Exercise_hrs_week` | Hours of exercise per week | Continuous | 0–10 |
| `SocialMedia_hrs_week` | Hours on social media per week | Continuous | ~1–50 |
| `TV_hrs_week` | Hours of TV watched per week | Continuous | ~1–30 |
| `VideoGames_hrs_week` | Hours of video games per week | Continuous | ~0–25 |
| `Screen_time_hrs_day` | Total phone/tablet/computer use per day | Continuous | ~1–14 |
| `Alcohol_drinks_week` | Alcoholic drinks per week | Continuous | ~0–20 |
| `Study_hrs_week` | Hours spent studying per week | Continuous | ~0–40 |
| `Caffeine_cups_day` | Cups of coffee/tea per day | Continuous | ~0–8 |
| `Social_Support_score` | Self-rated social support (1 = very low, 10 = very high) | Continuous | 1–10 |

### Mental Health (DASS-21)

| Variable | Description | Type | Range |
|----------|-------------|------|-------|
| `DASS_1` to `DASS_21` | Individual DASS-21 item responses | Ordinal | 0–3 |
| `DASS_Depression` | Depression subscale score (items 3, 5, 10, 13, 16, 17, 21 × 2) | Integer | 0–42 |
| `DASS_Anxiety` | Anxiety subscale score (items 2, 4, 7, 9, 15, 19, 20 × 2) | Integer | 0–42 |
| `DASS_Stress` | Stress subscale score (items 1, 6, 8, 11, 12, 14, 18 × 2) | Integer | 0–42 |

### Wellbeing

| Variable | Description | Type | Range |
|----------|-------------|------|-------|
| `Life_satisfaction` | Self-rated life satisfaction (1 = very low, 10 = very high) | Continuous | 1–10 |

**Some interesting relationships to explore:**
- Sleep and exercise tend to be associated with lower depression scores
- Screen time variables (social media, TV, video games, phone/tablet use) are correlated with each other — they form a cluster
- There's a U-shaped relationship between age and depression (higher for youngest and oldest, lower mid-life)
- Social support seems to protect against depression — and it might change how social media affects people
- Caffeine is linked to sleep, which is linked to depression — a chain of effects
- Not every variable predicts depression equally — some are red herrings. Finding that out is part of the process
- The three DASS subscales (Depression, Anxiety, Stress) are related but not identical — what predicts one doesn't always predict the others
- There are about 2–3% missing values in the lifestyle variables — you'll need to handle these

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
   conda activate ai-behsci
   python starter.py
   ```

4. **VERIFY & REFINE** — Check the saved PNG. If it needs changes, ask the AI to edit the script and re-run.

5. **DOCUMENT** — Have the AI update `plan.md` with what actually happened — key findings, changes from the original plan, and any surprises. You can also have the AI add new sections to your notebook summarising the script results.

## Starter LLM Prompts

Here are example prompts that demonstrate good prompt engineering. Notice how each one gives the AI specific context about the data and tools.

### Planning Prompts

**For the notebook workflow:**
> "Based on the dataset I've loaded (3000 rows, 44 columns including Age, Gender, Occupation, Relationship_status, Sleep_hrs_night, Exercise_hrs_week, SocialMedia_hrs_week, Screen_time_hrs_day, Alcohol_drinks_week, Caffeine_cups_day, Social_Support_score, Income_AUD, DASS_Depression, DASS_Anxiety, DASS_Stress, Life_satisfaction — see the data dictionary above for the full list), write an analysis plan for a multi-panel visualisation exploring lifestyle factors and DASS depression scores. Write the plan as a numbered list in markdown — what goes in each panel, what relationships we're testing, and what visual features to include. Don't write any code yet."

**For the script workflow:**
> "I have a CSV dataset at `data/lifestyle_mental_health.csv` with 3000 rows and 44 columns. The key outcome variables are DASS_Depression, DASS_Anxiety, and DASS_Stress (scored 0–42 each, from the DASS-21 questionnaire). Lifestyle predictors include Sleep_hrs_night, Exercise_hrs_week, SocialMedia_hrs_week, Screen_time_hrs_day, Alcohol_drinks_week, Caffeine_cups_day, Social_Support_score, and Income_AUD. Create a `plan.md` file that outlines a visualisation exploring which lifestyle factors are most strongly related to depression. Include: which relationships to plot, what plot types to use, what the final figure layout should look like, and what libraries to use (matplotlib, seaborn). Don't write any code yet — just the plan."

### Code Prompts

**Prompt 1 — Creating a multi-panel scatter plot:**
> "I have a pandas DataFrame called `data` with columns including `Sleep_hrs_night`, `Exercise_hrs_week`, `SocialMedia_hrs_week`, `Caffeine_cups_day`, and `DASS_Depression` (a depression score from 0–42). Using matplotlib and seaborn, create a 2×2 figure with four scatter plots, each showing DASS_Depression on the y-axis against a different lifestyle variable on the x-axis. Use `sns.scatterplot` with a small marker size and some transparency. Add a descriptive title to each subplot."

**Prompt 2 — Adding trend lines:**
> "I have a scatter plot created with matplotlib showing DASS_Depression vs Sleep_hrs_night. How do I add a linear trend line using numpy's `polyfit`? Show me the code to overlay the trend line on the existing scatter plot in red."

**Prompt 3 — Colouring by a categorical variable:**
> "In my DataFrame `data`, there's a column called `Gender` with values 'Male', 'Female', and 'Non-binary'. I'm creating a scatter plot of DASS_Depression vs Exercise_hrs_week using seaborn. How do I colour the points by Gender and add a legend? Use seaborn's `hue` parameter."

**Prompt 4 — Fixing layout issues:**
> "My matplotlib 2×2 subplot figure has overlapping axis labels and titles. The figure size is (10, 8). How do I fix the spacing? I've tried `plt.tight_layout()` but the titles still overlap with the plot above."

**Prompt 5 — Handling missing values:**
> "My DataFrame `data` has some missing values (NaN) in columns like `Sleep_hrs_night` and `Exercise_hrs_week`. When I try to create a scatter plot, some points are missing. How do I check how many missing values each column has, and should I drop them or fill them in? Show me both options using pandas."

## What to Present

Prepare **1 HTML slide** (~3 minutes per group) to present to the class. Build it using <a href="https://revealjs.com" target="_blank">reveal.js</a> with the help of any AI tool you like — a browser chatbot (ChatGPT, Gemini, Claude), VS Code with Copilot, or anything else. Most chatbots can generate the HTML file for you directly in the conversation. A <a href="../../resources/presentation-template/">starter template</a> and <a href="../../resources/html-slides-guide.md">step-by-step guide</a> are provided, but you can design it however you like.

Your slide should include:

1. **Your final figure** — the multi-panel visualisation you created
2. **Your approach** — which relationships did you choose and why?
3. **One key finding** — what's the most interesting pattern you found in the data?
4. **One thing about prompting** — what did you learn about communicating with an LLM? What worked well, or what was surprisingly hard?
5. **Notebook vs. scripts** — which workflow did you prefer and why? Did the plan-first approach change how you worked with the AI?

## Bonus Challenges

Finished early? Try one of these — they work in either the notebook or the script workflow. Have your AI assistant create new files, edit existing ones, or add new sections to your notebook.

1. **Correlation heatmap:** Ask your AI to create a correlation matrix heatmap of the lifestyle and DASS variables. Use `sns.heatmap` with `data[columns].corr()`. Which lifestyle variables cluster together? Which are most strongly linked to depression?

2. **Group comparison:** Create box plots or violin plots comparing DASS_Depression scores across different groups — by Occupation, Relationship_status, or Gender. Do any groups stand out?

3. **Depression vs. Anxiety vs. Stress:** The DASS-21 measures three things. Create a figure comparing all three subscales — do the same lifestyle factors predict all three, or do they differ?

4. **The caffeine chain:** Caffeine affects sleep, and sleep affects depression. Can you visualise this indirect chain? Try a multi-panel figure that shows caffeine → sleep and sleep → depression side by side.

5. **Age U-shape:** There's a non-linear relationship between age and depression. Can you create a scatter plot with a curved trend line (polynomial fit) that reveals it? Ask your AI about `numpy.polyfit` with degree 2.

6. **Multiple output files:** Have the AI create a script that generates several different figures, each saved as a separate PNG. Then have the AI create a summary `.md` file that describes what each figure shows and what patterns were found.

## Hints

<details>
<summary>Hint 1: Choosing which relationships to visualise</summary>

Start with the variables that are most likely connected to depression: `Sleep_hrs_night`, `Exercise_hrs_week`, `Social_Support_score`, and `SocialMedia_hrs_week` are good candidates. For a fifth or sixth panel, try `Age` (there's an interesting non-linear pattern) or `Alcohol_drinks_week`.

Don't feel like you need to include every variable. A focused figure with 4 well-chosen panels tells a better story than 12 cramped panels trying to show everything.

</details>

<details>
<summary>Hint 2: Multi-panel figure layout</summary>

The basic structure for a 2×2 figure in matplotlib is:

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Top-left panel
sns.scatterplot(data=data, x="Sleep_hrs_night", y="DASS_Depression", ax=axes[0, 0])
axes[0, 0].set_title("Sleep vs DASS Depression")

# Top-right panel
sns.scatterplot(data=data, x="Exercise_hrs_week", y="DASS_Depression", ax=axes[0, 1])
axes[0, 1].set_title("Exercise vs DASS Depression")

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
3. Activate your environment: `conda activate ai-behsci`
4. Run the script: `python starter.py`
5. If the script saves a figure, it will appear as a new file in your folder

If you get an error, copy the full error message and send it to your AI assistant — it will help you debug.

</details>

---

*[Back to course overview](../../README.md)*

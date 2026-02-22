# Prompt Engineering Guide

Your ability to get good results from AI tools depends almost entirely on how you communicate with them. This guide expands on the prompt engineering concepts from the Week 1 companion reading and gives you patterns you can use throughout the course and beyond.

---

## The Core Principle

A vague prompt gets a vague answer. A specific, well-structured prompt gets useful output. The time you invest in writing a good prompt saves you time debugging bad code and going back and forth.

---

## Vague vs Specific: Side-by-Side Examples

### Example 1 — Data visualisation

**Vague:** "Make me a graph"

**Specific:** "Create a scatter plot of Depression score vs Sleep hours from my DataFrame called `data`, with points coloured by Gender, using matplotlib. Add a title, axis labels, and a legend."

### Example 2 — Debugging

**Vague:** "My code doesn't work, fix it"

**Specific:** "I'm getting a `KeyError: 'depression_score'` when I run `data['depression_score'].mean()`. Here are my column names: `Age`, `Gender`, `Depression`, `Sleep_hrs`. I think the column might be called something different. How do I fix this?"

### Example 3 — Understanding a method

**Vague:** "Explain random forests"

**Specific:** "I'm a psychology honours student learning ML for the first time. Explain random forests using a psychology example (like predicting treatment outcomes). Compare it to regular regression, which I'm familiar with. Keep it under 300 words."

### Example 4 — Code generation

**Vague:** "Do a regression"

**Specific:** "I have a pandas DataFrame called `data` with columns `Sleep_hrs_night`, `Exercise_hrs_week`, `SocialMedia_hrs_week` (all continuous predictors), and `Depression` (continuous outcome). Using scikit-learn, fit a linear regression to predict Depression from the three predictors. Show me how to split the data into train/test sets (80/20), fit the model, and print the R-squared score on the test set. Include comments explaining each step."

---

## What Makes a Good Prompt

### 1. Be specific about what you want

Tell the AI exactly what output you expect, including format, variables, and level of detail.

- **Not:** "Analyse my data"
- **Better:** "Calculate the correlation between Sleep_hrs_night and Depression in my DataFrame, print the r-value and p-value, and create a scatter plot with a trend line"

### 2. Give context

The AI doesn't know your data, your tools, or your goals unless you tell it. The more relevant context you provide, the better the output.

**Context to include:**
- What your data looks like (column names, types, ranges, number of rows)
- What libraries/tools you're using
- What you've already tried
- What went wrong (if debugging)
- Your level of expertise ("I'm new to Python" vs "I know pandas but not scikit-learn")

### 3. Ask for explanations

Add "and explain each line of code" or "explain what this does and why" to learn as you go. The AI is a teacher as well as a coder.

### 4. State constraints

"Use only pandas and matplotlib" prevents the AI from suggesting unfamiliar libraries. "Keep the explanation under 200 words" controls verbosity.

### 5. Provide examples

Show what the input looks like and what you want the output to look like. "My data has rows like: `23, Male, 7.5, 3.2, 12, 4.8` and I want a summary table grouped by Gender."

### 6. Iterate

If the first result isn't right, refine your prompt with more detail and try again. Explain what went wrong and what you actually wanted.

---

## Context Engineering

Context engineering goes beyond prompt engineering. It's about providing the AI with the right background information — not just a good question, but the full picture.

### Strategies

- **Paste your column names** — `data.columns.tolist()` → paste the result into your prompt
- **Upload your data dictionary** — many AI tools accept file uploads
- **Share error messages** — copy the full traceback, not just "it didn't work"
- **Reference documentation** — "According to the scikit-learn docs, `RandomForestClassifier` takes a `n_estimators` parameter..."
- **Describe your goal** — "I'm trying to create a figure for my presentation that shows..." gives the AI a purpose, not just a task
- **State your level** — "I'm new to Python and have never used scikit-learn before" helps the AI calibrate its explanations

### Why context matters

The AI responds to exactly what you give it. It doesn't know what you've been working on, what matters to you, or what "good" looks like in your field. A human colleague would ask clarifying questions — the AI usually won't. You need to provide that context upfront.

---

## Prompt Patterns

These are reusable templates you can adapt throughout the course.

### The "I have / I want / Using" pattern

> I have [describe your data or situation].
> I want to [describe the output or goal].
> Using [specify tools, libraries, or constraints].

**Example:** "I have a pandas DataFrame with 2000 rows and columns `Age`, `Sleep_hrs_night`, and `Depression`. I want to create a scatter plot of Age vs Depression with a quadratic trend line. Using matplotlib and numpy."

### The "Step-by-step" pattern

> Walk me through how to [task] step by step. For each step, show the code and explain what it does. Use [libraries] and assume I'm working with [data description].

### The "Debug this" pattern

> I'm running this code: [paste code]. I'm getting this error: [paste error]. My data has these columns: [paste columns]. What's wrong and how do I fix it?

### The "Plan first" pattern

> Before writing any code, plan your approach. What steps will you take? What libraries will you use? What will the output look like? Then show me the code.

This is especially useful for complex tasks — reviewing the plan first catches misunderstandings before the AI writes a whole script in the wrong direction.

### The "Explain like I'm a psych student" pattern

> Explain [concept] in terms a psychology student would understand. Use examples from psychological research. Avoid unnecessary maths. Compare it to methods I might already know, like t-tests and regression.

---

## Common Mistakes

### 1. Being too vague

"Analyse my data" → the AI guesses what you want. Be specific.

### 2. Not providing data context

"Make a plot" without saying what columns exist. The AI will invent column names.

### 3. Accepting the first output without checking

Always verify: Does the code run? Does the output make sense? Are the variable names correct?

### 4. Saying "this doesn't work" without explaining what happened

"This doesn't work" → the AI guesses what went wrong.
"The plot shows all points in blue, but I wanted them coloured by the Gender column (values: Male, Female)" → the AI knows exactly what to fix.

### 5. Asking for too much at once

"Build me a complete ML pipeline with cross-validation, hyperparameter tuning, and a results dashboard" → break it into smaller pieces.

---

## The LLM Problem-Solving Loop

This is the framework you'll use all semester. Prompt engineering is one part of it — the ENGINEER step in the inner loop.

**Outer loop (your research process):**
1. **PLAN** → 2. **EXECUTE** → 3. **EVALUATE** → 4. **DOCUMENT**

**Inner loop (working with the AI):**
1. **ENGINEER** → 2. **PLAN** → 3. **GENERATE** → 4. **VERIFY** → 5. **REFINE**

The ENGINEER step is where prompt engineering lives — crafting a clear, context-rich prompt and asking the AI for a plan. The PLAN step is where the AI responds with a proposed approach and you review it critically before anything is generated. The GENERATE step covers any AI output — code, text, visualisations, analysis — and for complex tasks, sometimes a more detailed sub-plan before the final output. Your first few iterations are often about getting the plan right; only later iterations shift to generating the actual output. The inner loop typically runs 2–5 times per task. That's normal. Each refinement is an opportunity to improve your approach and learn something about how the AI interprets your requests.

See the [Week 1 companion reading](../weeks/week-01-lecture/README.md) for a detailed walkthrough with examples.

---

*[Back to resources](README.md) · [Back to course overview](../README.md)*

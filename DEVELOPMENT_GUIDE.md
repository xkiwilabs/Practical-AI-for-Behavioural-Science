# Development Guide

This document outlines the structure, conventions, and workflow for building out weekly course materials. Refer back to this when creating content for any new week.

---

## Repo Structure

```
Current-Advances-in-Psychological-Methods-and-Analyses-Repo/
├── README.md                      # Course overview + weekly links table
├── DEVELOPMENT_GUIDE.md           # This file — development conventions
├── .gitignore                     # Excludes .pptx, __pycache__, .DS_Store, etc.
├── setup/
│   └── getting-started.md         # Student setup guide (Python, Jupyter, VS Code)
├── _templates/
│   ├── lecture-week.md            # Template for lecture companion readings
│   └── challenge-lab.md           # Template for challenge lab briefs
├── weeks/
│   ├── week-01-lecture/           # Lecture weeks
│   │   ├── README.md              # Companion reading
│   │   ├── readings.md            # Optional/suggested readings
│   │   ├── examples/              # Code examples, notebooks, plots
│   │   └── slides/                # .pptx files (git-ignored, local only)
│   ├── week-02-lab/               # Challenge lab weeks
│   │   ├── README.md              # Challenge brief
│   │   ├── starter.ipynb          # Starter notebook with scaffolding
│   │   └── data/                  # Datasets for the challenge
│   ├── week-11-lecture-lab/       # Hybrid week (both lecture + challenge)
│   ├── week-12-viva-review/       # Study guide + practice questions
│   └── week-13-discussion/        # Discussion prompts + reflection
├── data/                          # Shared datasets (used across weeks)
├── iLearnMaterials/               # HTML files for iLearn LMS (not weekly content)
└── .archive/                      # Archived drafts and earlier versions
```

---

## Branching Strategy

- **`main`** — Student-facing content. Everything here is visible to students.
- **`solutions`** — Solution notebooks for challenges. Merge into main after each challenge presentation week to reveal solutions.

---

## Class Session Timing

Each class session is **2 hours** (Mondays 3–5pm), but content does not fill the full 2 hours. Budget time as follows:

### Lecture Weeks (Weeks 1, 3, 5, 7, 9, 11)

| Activity | Duration | Notes |
|----------|----------|-------|
| Student presentations + Q&A | ~30 min | Pairs present previous lab challenge results |
| Lecture | ~60 min | Core content delivery |
| Buffer / questions / wrap-up | ~30 min | Organic discussion, preview of next lab |

**Exception — Week 1:** No student presentations (it's the first week). Budget ~1.5 hours for the introductory lecture, plus ~30 minutes going over the class structure, assessment, tools, and expectations.

### Lab Weeks (Weeks 2, 4, 6, 8, 10)

| Activity | Duration | Notes |
|----------|----------|-------|
| Challenge briefing | ~15 min | Instructor walks through the brief and dataset |
| Hands-on lab time | ~90 min | Students work on challenge (with LLM assistants) |
| Wrap-up + next steps | ~15 min | What to finish before next week's presentation |

### Implications for Content Scope

- **Companion readings** should cover what can realistically be taught in ~60 minutes of lecture (not 2 hours).
- **Challenge labs** should be achievable in ~90 minutes of focused work, with stretch goals for fast students.
- **Slide decks** should target roughly 40–50 content slides for a 60-minute lecture (some slides are quick, some need discussion).
- **Week 1 slides** can be larger (~60–70 slides) given the extended lecture time.

---

## Building a Lecture Week

Use `_templates/lecture-week.md` as the starting point for `weeks/week-NN-lecture/README.md`.

### Checklist

1. **README.md** — Companion reading covering lecture topics in detail
   - Overview (2-3 sentences: what and why)
   - Key Concepts (explained with psychology-relevant examples)
   - Worked Examples (reference notebooks in `examples/`)
   - Common Misconceptions
   - Connections to Psychology
   - Link to `readings.md`

2. **readings.md** — Suggested and optional readings
   - 1-2 suggested readings (accessible, foundational)
   - 2-4 optional readings (deeper dives, applied examples)
   - Use APA format, include DOI links where available

3. **examples/** — Code examples shown or referenced in lecture
   - Jupyter notebooks (.ipynb) or Python scripts (.py)
   - Each example should be self-contained and runnable
   - Include clear comments explaining each step
   - Name descriptively: `01_train_test_split_demo.ipynb`

4. **slides/** — PowerPoint files (git-ignored)
   - Develop locally, distribute via iLearn
   - Won't appear on GitHub

---

## Building a Challenge Lab Week

Use `_templates/challenge-lab.md` as the starting point for `weeks/week-NN-lab/README.md`.

### Checklist

1. **README.md** — Challenge brief
   - The Challenge (clear goal statement)
   - Background (what lecture concept is being applied)
   - Dataset description (what's in `data/`, what each variable means)
   - Getting Started (suggested steps, useful LLM prompts, starter code reference)
   - What to Present (1 slide, what to include)
   - Hints (collapsible spoiler sections)

2. **starter.ipynb** — Scaffolded Jupyter notebook
   - Import cells with standard libraries
   - Data loading cell
   - Exploratory prompts (e.g., "What does this data look like?")
   - Placeholder cells for each major step
   - Should run without errors up to the point where students take over

3. **data/** — Challenge dataset(s)
   - CSV or JSON format preferred
   - Include a brief data dictionary in the README or as a separate `data_dictionary.md`
   - Keep datasets small enough for GitHub (<50MB)

4. **Solution notebook** (on `solutions` branch only)
   - Complete worked solution
   - Include commentary explaining choices
   - Name: `solution.ipynb`

---

## Conventions

### File Naming
- Folders: `week-NN-type` (e.g., `week-03-lecture`, `week-04-lab`)
- Notebooks: lowercase, hyphens, descriptive (e.g., `01_ridge_lasso_demo.ipynb`)
- Data files: lowercase, underscores (e.g., `personality_survey.csv`)

### Writing Style (for student-facing .md files)
- Write for 4th-year psychology students with no coding/ML background
- Explain jargon the first time it appears
- Use concrete psychology examples (not abstract math)
- Keep companion readings around 1000-2000 words
- Use collapsible sections for hints and optional depth

### Code Style
- Python 3.10+
- Use standard data science stack: pandas, numpy, matplotlib, seaborn, scikit-learn, torch
- Include inline comments for non-obvious steps
- Prefer clarity over cleverness
- All notebooks should run top-to-bottom without errors

### LLM Prompts (in challenge briefs)
- Provide 2-3 starter prompts students can use with their LLM assistant
- Frame prompts as questions, not instructions (teaches good prompting)
- Example: "I have a CSV with columns X, Y, Z. How would I build a simple linear regression to predict Y from X and Z using scikit-learn?"

---

## Weekly Content Summary

| Week | Type | Topic | Key Deliverables |
|------|------|-------|------------------|
| 1 | Lecture | ML in Psychological Science | Companion reading, concept examples |
| 2 | Lab | Setup + LLM Problem-Solving Loop | Starter notebook, figure reproduction challenge |
| 3 | Lecture | Generalisation & Overfitting | Companion reading, train/test demo |
| 4 | Lab | Regression Pipeline | Starter notebook, prediction challenge, dataset |
| 5 | Lecture | Classification & Evaluation | Companion reading, metrics examples |
| 6 | Lab | Trees & Ensembles | Starter notebook, classifier challenge, dataset |
| 7 | Lecture | Clustering & Dim. Reduction | Companion reading, clustering demos |
| 8 | Lab | PCA/UMAP & Clustering | Starter notebook, structure challenge, dataset |
| 9 | Lecture | Neural Networks | Companion reading, MLP examples |
| 10 | Lab | Neural Network Training | Starter notebook, baseline challenge, dataset |
| 11 | Hybrid | Embeddings & LLMs | Companion reading + LLM challenge, dataset |
| 12 | Review | Viva Preparation | Study guide, concept list, practice Qs |
| 13 | Discussion | Ethics & Reflection | Discussion prompts |

# PSYC4411: Current Advances in Psychological Methods and Analyses (2026)

A companion repository for the PSYC4411 course at Macquarie University. This repo contains weekly companion readings, code examples, challenge lab briefs, starter notebooks, and datasets.

**No technical or mathematical background is assumed.** This course teaches you to use modern ML/AI tools — including LLM coding assistants — for psychological and cognitive science research.

---

## About the Instructor

**Michael J. Richardson** is a Professor in the [School of Psychological Sciences](https://www.mq.edu.au/faculty-of-medicine-health-and-human-sciences/school-of-psychological-sciences) within the Faculty of Medicine, Health and Human Sciences at Macquarie University. He completed his undergraduate degree and Master of Science at the [University of Canterbury](https://www.canterbury.ac.nz/) in New Zealand, then his PhD in Experimental Psychology at the [University of Connecticut](https://psych.uconn.edu/) (2005), where he worked with the Center for the Ecological Study of Perception and Action.

Mike's research sits at the intersection of experimental psychology, cognitive science, and computational modelling. He studies how humans perceive, act, coordinate, and make decisions — and how those processes can be understood through the lens of complex dynamical systems. His work spans interpersonal coordination and joint action, perception-action coupling, human-machine interaction, and the application of machine learning and AI to understanding behaviour. His methods toolkit includes nonlinear time-series analysis, dynamical systems modelling, recurrence analysis, deep learning, motion capture, eye-tracking, physiological measurement, and interactive virtual reality.

Before joining Macquarie, Mike held positions at the University of Cincinnati and Colby College. He is the Director of the Centre for Elite Performance, Expertise, and Training (CEPET), a member of the Frontier AI Research Centre at MQ, and serves as Editor of *Ecological Psychology*. He has authored over 200 research outputs — including journal articles, book chapters, and conference proceedings — and his work has been cited over 12,500 times ([Google Scholar](https://scholar.google.com/citations?user=DJPcjuQAAAAJ&hl=en) · [MQ Research Profile](https://researchers.mq.edu.au/en/persons/michael-richardson/)).

In short: he's spent two decades studying how humans move, think, and coordinate, using exactly the kinds of computational and modelling tools this course covers. You're in good hands.

---

## How to Use This Repo

1. **Before each lecture:** Optionally read the companion material for that week
2. **During lab weeks:** Open the challenge brief and starter notebook for your group work
3. **After labs:** Use the examples and readings to deepen your understanding

---

## Weekly Materials

| Week | Date | Type | Topic | Materials |
|------|------|------|-------|-----------|
| 1 | 23 Feb | Lecture | [From Mind to Model: Why ML Belongs in Psychological Science](weeks/week-01-lecture/) | Companion reading, examples |
| 2 | 02 Mar | Lab | [Setup, Plotting, and the LLM Problem-Solving Loop](weeks/week-02-lab/) | Challenge brief, starter notebook |
| 3 | 09 Mar | Lecture | [Models, Not Magic: Generalisation, Overfitting, and How ML Misleads](weeks/week-03-lecture/) | Companion reading, examples |
| 4 | 16 Mar | Lab | [Regression Pipeline, Cross-Validation, and Interpretation](weeks/week-04-lab/) | Challenge brief, starter notebook |
| 5 | 23 Mar | Lecture | [Prediction with Accountability: Classification, Uncertainty, and Evaluation](weeks/week-05-lecture/) | Companion reading, examples |
| 6 | 30 Mar | Lab | [Trees, Ensembles, Feature Importance, and Error Analysis](weeks/week-06-lab/) | Challenge brief, starter notebook |
| — | 06–19 Apr | Break | Mid-Semester Break | — |
| 7 | 20 Apr | Lecture | [Discovering Structure: Clustering and Dimensionality Reduction](weeks/week-07-lecture/) | Companion reading, examples |
| 8 | 27 Apr | Lab | [PCA/UMAP, Clustering, and Stability Checks](weeks/week-08-lab/) | Challenge brief, starter notebook |
| 9 | 04 May | Lecture | [Learning Representations: Neural Networks as Psychological Tools](weeks/week-09-lecture/) | Companion reading, examples |
| 10 | 11 May | Lab | [Simple Neural Network, Training Diagnostics, and Baseline Comparison](weeks/week-10-lab/) | Challenge brief, starter notebook |
| 11 | 18 May | Lecture + Lab | [Meaning in Vectors: Embeddings and LLMs for Research Workflows](weeks/week-11-lecture-lab/) | Companion reading, challenge, examples |
| 12 | 25 May | Review | [Viva Review: Consolidation, Q&A, and Practice Defenses](weeks/week-12-viva-review/) | Study guide, practice questions |
| 13 | 01 Jun | Discussion | [Limits, Ethics, Reproducibility, and Reasoned Conclusions](weeks/week-13-discussion/) | Discussion prompts, reflection |

---

## Setup

See the [Getting Started guide](setup/getting-started.md) for instructions on installing Python, Jupyter, VS Code, and setting up your LLM assistant.

---

## The LLM Problem-Solving Loop

A core workflow you'll develop throughout this course. It has two nested loops — an outer loop for your research process, and an inner loop for working with AI.

**Outer loop (your research process):**

1. **PLAN** — Define what you want to achieve. What question are you answering? What output do you need?
2. **EXECUTE** — Use the inner loop (below) to get AI-generated code and analysis
3. **EVALUATE** — Does the result answer your question? Is it correct? Does it make sense given what you know about the domain?
4. **DOCUMENT** — Record what you did, what worked, and what you learned

**Inner loop (working with the AI):**

1. **ENGINEER** — Craft your prompt: be specific, provide context (your data, libraries, constraints), state your goal clearly
2. **PROMPT** — Send it to the AI
3. **VERIFY** — Read the code the AI gives you. Don't just copy and paste — look at what it's doing. Then run it. Does it execute without errors? Does the output make sense?
4. **REFINE** — If it's not right: add more context, correct misunderstandings, try a different approach. Then go back to step 1.

The inner loop typically runs 2–5 times per task. That's normal — even experienced developers iterate with AI tools. Strategies that help: ask the AI to plan before coding, break problems into smaller pieces, provide rich context (paste in column names, error messages, documentation), and explain *what* went wrong, not just *that* something went wrong.

**Critical rule:** Never trust LLM output without verification. You are the researcher. The AI is a tool.

See the [Week 1 companion reading](weeks/week-01-lecture/) for a detailed walkthrough with examples.

---

## AI Disclosure

I use LLMs and generative AI tools for virtually all aspects of my work — research, writing, coding, data analysis, course development, and scientific exploration. These tools make me more productive, help me think through problems from new angles, and let me spend less time on tedious mechanics and more time on the ideas that matter. I embrace their use, I actively explore how they can enhance research and scientific practice, and I encourage my students to do the same.

Here's the thing: using AI tools well is a skill, not a shortcut. It requires critical thinking, domain knowledge, and the ability to evaluate whether what the AI gives you is actually correct. That's what this course teaches. The use of AI should be praised, encouraged, and talked about openly — not hidden or treated as something to be ashamed of. We're all figuring out how to work with these tools, and the students who lean into that process will be better researchers for it.

In that spirit, I include an AI disclosure statement for nearly everything in this repository, and **I expect you to do the same for all work you submit in this course.** Transparency about AI use is not a confession — it's good scientific practice. Below is a template you can adapt for your own assignments and submissions.

### AI Disclosure Template

> **AI Disclosure Statement**
>
> This work was completed with the assistance of the following AI tools:
>
> - **[Tool name(s)]** (e.g., ChatGPT, Claude, GitHub Copilot, Gemini) — used for [describe what you used it for: generating code, debugging, explaining concepts, drafting text, data exploration, etc.]
>
> All AI-generated content was reviewed, verified, and edited by the author. The research questions, interpretation of results, and critical evaluation of outputs are entirely my own.
>
> **Specific contributions:**
> - [e.g., "Used Claude to generate the initial matplotlib code for the multi-panel figure, then modified the colour scheme and labels manually"]
> - [e.g., "Used ChatGPT to explain the difference between L1 and L2 regularisation, then rewrote the explanation in my own words"]
> - [e.g., "Used GitHub Copilot for code autocompletion while writing the data preprocessing pipeline"]
>
> **What I verified:** [e.g., "Checked all plot outputs against the raw data, confirmed model accuracy metrics by hand, verified that the references cited by the AI actually exist"]

Use this template (or something similar) for every piece of assessed work you submit. Be specific about what you used and what you checked. The goal isn't to limit your AI use — it's to make you a thoughtful, transparent user of these tools.

### Course Materials Disclosure

The content and materials for this course were designed and developed in collaboration with numerous AI tools, including [Claude](https://claude.ai), [ChatGPT](https://chat.openai.com), [GitHub Copilot](https://github.com/features/copilot), and [Gemini](https://gemini.google.com). All materials were reviewed, verified, and curated by the course instructor. This transparent use of AI in course development reflects the same approach we teach students throughout the unit — AI tools are powerful collaborators, but human judgement, verification, and critical evaluation remain essential.

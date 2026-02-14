# Practical AI for Behavioural Science

### PSYC4411: Current Advances in Psychological Methods and Analyses — Macquarie University, Semester 1 2026

A hands-on course introducing machine learning and AI tools to psychological and cognitive science research. No coding or technical background required.

Students learn to frame research questions for supervised and unsupervised learning, evaluate models responsibly, and use LLM-based assistants (ChatGPT, Claude, Gemini, GitHub Copilot) to support coding, analysis, visualisation, and research workflows — all through practical, student-guided experimentation with real and synthetic datasets.

This repository contains weekly companion readings, lecture slides, challenge lab briefs, starter notebooks, and datasets.

**Learning Objectives** — By the end of this course, students will be able to:

1. **Frame research questions** appropriately for supervised and unsupervised machine learning
2. **Build and evaluate** regression, classification, clustering, and simple neural network models
3. **Use LLM coding assistants** effectively to write, debug, refactor, and document code
4. **Interpret model outputs** with appropriate uncertainty and connect findings to psychological constructs
5. **Identify common pitfalls** including overfitting, data leakage, and spurious structure
6. **Communicate findings** clearly, distinguishing prediction from explanation and acknowledging limitations
7. **Evaluate ethical implications** of ML-based categorisation and prediction in psychological research

---

## About the Instructor

**Michael J. Richardson** is a Professor in the [School of Psychological Sciences](https://www.mq.edu.au/faculty-of-medicine-health-and-human-sciences/departments-and-schools/school-of-psychological-sciences) and the [Centre for Elite Performance and Expertise](https://www.mq.edu.au/research/research-centres-groups-and-facilities/healthy-people/centres/centre-for-elite-performance-expertise-and-training) within the Faculty of Medicine, Health and Human Sciences at Macquarie University. He completed his undergraduate degree and Master of Science at the [University of Canterbury](https://www.canterbury.ac.nz/) in New Zealand, then his PhD in Experimental Psychology at the [University of Connecticut](https://psych.uconn.edu/) (2005), at the Center for the Ecological Study of Perception and Action.

Following a one-year postdoc at UConn and [Haskins Laboratories](https://haskinslabs.org/), he joined [Colby College](https://www.colby.edu/) in Maine as an Assistant Professor in 2006. He then moved to the [University of Cincinnati](https://www.uc.edu/) in 2009, progressing from Assistant Professor to Full Professor of Psychology before heading down under to [Macquarie University](https://www.mq.edu.au/) in 2017. He currently teaches in the psychology and cognitive science programs within the School of Psychological Sciences and co-directs the **MInD Lab** (Movement and Interaction Dynamics Lab).

His research sits at the intersection of experimental psychology, cognitive science, and computational modelling. He studies how humans perceive, act, coordinate, and make decisions — and how those processes can be understood through the lens of complex dynamical systems. His work spans interpersonal coordination and joint action, perception-action coupling, human-machine interaction, and, more recently, the application of machine learning and AI to understand and model human behaviour, as well as develop human-aligned AI and multi-agent systems. He has authored over 200 research outputs — including journal articles, book chapters, and conference proceedings ([Google Scholar](https://scholar.google.com/citations?user=DJPcjuQAAAAJ&hl=en) · [MQ Research Profile](https://researchers.mq.edu.au/en/persons/michael-richardson/)) — and has received research funding from the National Science Foundation (NSF), the National Institutes of Health (NIH), the Australian Research Council (ARC), the Australian Defence Force and Defence Science and Technology Group, Google Research, as well as many other industry partners.

---

## Teaching Assistant and Collaborators

**Teaching Assistant:** [Dr Ayeh Alhasan](https://www.researchgate.net/profile/Ayeh-Alhasan)

**Course Development:** This course was developed by [Prof. Michael J. Richardson](https://researchers.mq.edu.au/en/persons/michael-richardson/), [Prof. Rachel W. Kallen](https://researchers.mq.edu.au/en/persons/rachel-kallen), and [Dr Ayeh Alhasan](https://www.researchgate.net/profile/Ayeh-Alhasan), all from the [School of Psychological Sciences](https://www.mq.edu.au/faculty-of-medicine-health-and-human-sciences/departments-and-schools/school-of-psychological-sciences) at Macquarie University.

---

## How to Use This Repo

1. **Before each lecture:** Read the companion reading for that week (the `README.md` in each week's folder — this is the required reading)
2. **During lab weeks:** Open the challenge brief and starter notebook for your group work
3. **After labs:** Use the optional readings in `readings.md` and the examples to deepen your understanding

---

## Weekly Materials

Materials are released on the Monday of each class week. The dates below show when each topic goes live — by the end of semester, all weeks will be available here.

| Week | Date | Type | Topic | Slides |
|------|------|------|-------|--------|
| 1 | 23 Feb | Lecture | [Why ML and AI Belongs in the Cognitive, Psychological and Behavioural Sciences](weeks/week-01-lecture/) | <a href="https://xkiwilabs.github.io/Practical-AI-for-Behavioural-Science/weeks/week-01-lecture/slides/index.html" target="_blank">Slides</a> |
| 2 | 02 Mar | Lab | [Setup, Plotting, and the LLM Problem-Solving Loop](weeks/week-02-lab/) | <a href="https://xkiwilabs.github.io/Practical-AI-for-Behavioural-Science/weeks/week-02-lab/slides/index.html" target="_blank">Slides</a> |
| 3 | 09 Mar | Lecture | [Models, Not Magic: Generalisation, Overfitting, and How ML Misleads](weeks/week-03-lecture/) | <a href="https://xkiwilabs.github.io/Practical-AI-for-Behavioural-Science/weeks/week-03-lecture/slides/index.html" target="_blank">Slides</a> |
| 4 | 16 Mar | Lab | [Regression Pipeline, Cross-Validation, and Interpretation](weeks/week-04-lab/) | <a href="https://xkiwilabs.github.io/Practical-AI-for-Behavioural-Science/weeks/week-04-lab/slides/index.html" target="_blank">Slides</a> |
| 5 | 23 Mar | Lecture | [Prediction with Accountability: Classification, Uncertainty, and Evaluation](weeks/week-05-lecture/) | <a href="https://xkiwilabs.github.io/Practical-AI-for-Behavioural-Science/weeks/week-05-lecture/slides/index.html" target="_blank">Slides</a> |
| 6 | 30 Mar | Lab | [Trees, Ensembles, Feature Importance, and Error Analysis](weeks/week-06-lab/) | <a href="https://xkiwilabs.github.io/Practical-AI-for-Behavioural-Science/weeks/week-06-lab/slides/index.html" target="_blank">Slides</a> |
| — | 06–19 Apr | Break | Mid-Semester Break | — |
| 7 | 20 Apr | Lecture | [Discovering Structure: Clustering and Dimensionality Reduction](weeks/week-07-lecture/) | <a href="https://xkiwilabs.github.io/Practical-AI-for-Behavioural-Science/weeks/week-07-lecture/slides/index.html" target="_blank">Slides</a> |
| 8 | 27 Apr | Lab | [PCA/UMAP, Clustering, and Stability Checks](weeks/week-08-lab/) | <a href="https://xkiwilabs.github.io/Practical-AI-for-Behavioural-Science/weeks/week-08-lab/slides/index.html" target="_blank">Slides</a> |
| 9 | 04 May | Lecture | [Learning Representations: Neural Networks as Psychological Tools](weeks/week-09-lecture/) | <a href="https://xkiwilabs.github.io/Practical-AI-for-Behavioural-Science/weeks/week-09-lecture/slides/index.html" target="_blank">Slides</a> |
| 10 | 11 May | Lab | [Simple Neural Network, Training Diagnostics, and Baseline Comparison](weeks/week-10-lab/) | <a href="https://xkiwilabs.github.io/Practical-AI-for-Behavioural-Science/weeks/week-10-lab/slides/index.html" target="_blank">Slides</a> |
| 11 | 18 May | Lecture + Lab | [Meaning in Vectors: Embeddings and LLMs for Research Workflows](weeks/week-11-lecture-lab/) | <a href="https://xkiwilabs.github.io/Practical-AI-for-Behavioural-Science/weeks/week-11-lecture-lab/slides/index.html" target="_blank">Slides</a> |
| 12 | 25 May | Review | [Viva Review: Consolidation, Q&A, and Practice Defenses](weeks/week-12-viva-review/) | — |
| 13 | 01 Jun | Discussion | [Limits, Ethics, Reproducibility, and Reasoned Conclusions](weeks/week-13-discussion/) | — |

---

## Assessments

| Assessment | Weight | Format | Due |
|------------|--------|--------|-----|
| [Paper Presentation](assessments/presentation.md) | 20% | 3-min talk + 1 HTML slide (PDF submission) | Weeks 4, 6, 8, or 10 |
| [Written Assignment](assessments/written-assignment.md) | 40% | Popular science article + LLM chat history | Sunday 19 Apr, 11:55pm |
| [Viva Exam](assessments/viva-exam.md) | 40% | 15-min oral exam (3 sections) | Weeks 12–13 |

See the [assessments folder](assessments/) for full details, rubrics, and tips.

---

## Resources

Guides and references for tools used in this course — all written for beginners:

- **[AI Tools guide](resources/ai-tools-guide.md)** — Overview of AI tools in 2026: conversational AI, coding assistants, research tools, local models
- **[Prompt Engineering guide](resources/prompt-engineering-guide.md)** — Writing effective prompts: patterns, examples, and common mistakes
- **[VS Code guide](resources/vscode-guide.md)** — Navigate the interface, install extensions, use the terminal
- **[Jupyter Notebooks guide](resources/jupyter-guide.md)** — Cells, kernels, execution order, common mistakes
- **[GitHub guide](resources/github-guide.md)** — Account setup, navigating repos, Student Developer Pack
- **[Markdown guide](resources/markdown-guide.md)** — Formatting syntax for notebooks and READMEs
- **[HTML Slides guide](resources/html-slides-guide.md)** — Creating your presentation slide with reveal.js
- **[Presentation template](resources/presentation-template/)** — Ready-to-use HTML slide template

See the [resources folder](resources/) for the full list.

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

---

## Licence

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Licence](https://creativecommons.org/licenses/by-nc-sa/4.0/).

[![CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

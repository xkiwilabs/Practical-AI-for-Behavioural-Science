# PSYC4411: Current Advances in Psychological Methods and Analyses (2026)

### Machine Learning and AI for Research

This unit introduces modern computational methods now shaping psychological and cognitive science research, with a focus on machine learning and contemporary AI tools, including large language models (LLMs). Students learn how to frame research questions for supervised and unsupervised learning, evaluate models responsibly, and use LLM-based assistants to support coding, analysis, visualisation, and research workflows.

**No technical or mathematical background is assumed.** Emphasis is placed on practical, student-guided experimentation and sound scientific interpretation. Students will learn to use modern LLM tools (e.g., ChatGPT, Claude, Gemini, GitHub Copilot) as coding assistants and problem-solving partners throughout the course.

**Learning Objectives** — By the end of this course, students will be able to:

1. **Frame research questions** appropriately for supervised and unsupervised machine learning
2. **Build and evaluate** regression, classification, clustering, and simple neural network models
3. **Use LLM coding assistants** effectively to write, debug, refactor, and document code
4. **Interpret model outputs** with appropriate uncertainty and connect findings to psychological constructs
5. **Identify common pitfalls** including overfitting, data leakage, and spurious structure
6. **Communicate findings** clearly, distinguishing prediction from explanation and acknowledging limitations
7. **Evaluate ethical implications** of ML-based categorisation and prediction in psychological research

This is a companion repository containing weekly companion readings, code examples, challenge lab briefs, starter notebooks, and datasets.

---

## About the Instructor

I, **Michael J. Richardson**, am a Professor in the [School of Psychological Sciences](https://www.mq.edu.au/faculty-of-medicine-health-and-human-sciences/school-of-psychological-sciences) within the Faculty of Medicine, Health and Human Sciences at Macquarie University. I completed my undergraduate degree and Master of Science at the [University of Canterbury](https://www.canterbury.ac.nz/) in New Zealand, then my PhD in Experimental Psychology at the [University of Connecticut](https://psych.uconn.edu/) (2005), where I worked with the Center for the Ecological Study of Perception and Action.

My research sits at the intersection of experimental psychology, cognitive science, and computational modelling. I study how humans perceive, act, coordinate, and make decisions — and how those processes can be understood through the lens of complex dynamical systems. My work spans interpersonal coordination and joint action, perception-action coupling, human-machine interaction, and the application of machine learning and AI to understanding behaviour. I have authored over 200 research outputs — including journal articles, book chapters, and conference proceedings ([Google Scholar](https://scholar.google.com/citations?user=DJPcjuQAAAAJ&hl=en) · [MQ Research Profile](https://researchers.mq.edu.au/en/persons/michael-richardson/)) — and have received research funding from the National Science Foundation (NSF), the National Institutes of Health (NIH), the Australian Research Council (ARC), the Australian Defence Force and Defence Science and Technology Group, Google Research, as well as many other industry partners.

---

## How to Use This Repo

1. **Before each lecture:** Optionally read the companion material for that week
2. **During lab weeks:** Open the challenge brief and starter notebook for your group work
3. **After labs:** Use the examples and readings to deepen your understanding

---

## Weekly Materials

| Week | Date | Type | Topic | Slides |
|------|------|------|-------|--------|
| 1 | 23 Feb | Lecture | [From Mind to Model: Why ML Belongs in Psychological Science](weeks/week-01-lecture/) | [Slides](weeks/week-01-lecture/slides/index.html) |
| 2 | 02 Mar | Lab | [Setup, Plotting, and the LLM Problem-Solving Loop](weeks/week-02-lab/) | — |
| 3 | 09 Mar | Lecture | [Models, Not Magic: Generalisation, Overfitting, and How ML Misleads](weeks/week-03-lecture/) | Slides |
| 4 | 16 Mar | Lab | [Regression Pipeline, Cross-Validation, and Interpretation](weeks/week-04-lab/) | — |
| 5 | 23 Mar | Lecture | [Prediction with Accountability: Classification, Uncertainty, and Evaluation](weeks/week-05-lecture/) | Slides |
| 6 | 30 Mar | Lab | [Trees, Ensembles, Feature Importance, and Error Analysis](weeks/week-06-lab/) | — |
| — | 06–19 Apr | Break | Mid-Semester Break | — |
| 7 | 20 Apr | Lecture | [Discovering Structure: Clustering and Dimensionality Reduction](weeks/week-07-lecture/) | Slides |
| 8 | 27 Apr | Lab | [PCA/UMAP, Clustering, and Stability Checks](weeks/week-08-lab/) | — |
| 9 | 04 May | Lecture | [Learning Representations: Neural Networks as Psychological Tools](weeks/week-09-lecture/) | Slides |
| 10 | 11 May | Lab | [Simple Neural Network, Training Diagnostics, and Baseline Comparison](weeks/week-10-lab/) | — |
| 11 | 18 May | Lecture + Lab | [Meaning in Vectors: Embeddings and LLMs for Research Workflows](weeks/week-11-lecture-lab/) | Slides |
| 12 | 25 May | Review | [Viva Review: Consolidation, Q&A, and Practice Defenses](weeks/week-12-viva-review/) | — |
| 13 | 01 Jun | Discussion | [Limits, Ethics, Reproducibility, and Reasoned Conclusions](weeks/week-13-discussion/) | — |

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

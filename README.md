# Practical AI for Behavioural Science

### Machine Learning & AI for Psychological and Cognitive Science — Macquarie University

A hands-on course introducing machine learning and AI tools to psychological and cognitive science research. No coding or technical background required.

Students learn to frame research questions for supervised and unsupervised learning, evaluate models responsibly, and use LLM-based assistants (ChatGPT, Claude, Gemini, GitHub Copilot) to support coding, analysis, visualisation, and research workflows, all through practical, student-guided experimentation with real and synthetic datasets.

This repository contains weekly companion readings, lecture slides, challenge lab briefs, starter notebooks, and datasets.

**Learning Objectives:** By the end of this course, students will be able to:

1. **Frame research questions** appropriately for supervised and unsupervised machine learning
2. **Build and evaluate** regression, classification, clustering, and simple neural network models
3. **Use LLM coding assistants** effectively to write, debug, refactor, and document code
4. **Interpret model outputs** with appropriate uncertainty and connect findings to psychological constructs
5. **Identify common pitfalls** including overfitting, data leakage, and spurious structure
6. **Communicate findings** clearly, distinguishing prediction from explanation and acknowledging limitations
7. **Evaluate ethical implications** of ML-based categorisation and prediction in psychological research

---

## About the Instructor

**Michael J. Richardson** is a Professor in the [School of Psychological Sciences](https://www.mq.edu.au/faculty-of-medicine-health-and-human-sciences/departments-and-schools/school-of-psychological-sciences) and the [Centre for Elite Performance and Expertise](https://www.mq.edu.au/research/research-centres-groups-and-facilities/healthy-people/centres/centre-for-elite-performance-expertise-and-training) within the Faculty of Medicine, Health and Human Sciences at Macquarie University. He currently teaches in the psychology and cognitive science programs within the School of Psychological Sciences and co-directs the **MInD Lab** (Movement and Interaction Dynamics Lab).

His research sits at the intersection of cognitive science and computational modelling. He studies how humans perceive, act, coordinate, and make decisions, and how those processes can be understood through the lens of complex dynamical systems. His work spans interpersonal coordination and joint action, perception-action coupling, human-machine interaction, and, more recently, the application of machine learning and AI to understand and model human behaviour, as well as develop human-aligned AI and multi-agent systems ([Google Scholar](https://scholar.google.com/citations?user=DJPcjuQAAAAJ&hl=en) · [MQ Research Profile](https://researchers.mq.edu.au/en/persons/michael-richardson/)).

---

## Course Development

This course was developed by [Prof. Michael J. Richardson](https://researchers.mq.edu.au/en/persons/michael-richardson/), [Prof. Rachel W. Kallen](https://researchers.mq.edu.au/en/persons/rachel-kallen), and [Dr Ayeh Alhasan](https://www.researchgate.net/profile/Ayeh-Alhasan), all from the [School of Psychological Sciences](https://www.mq.edu.au/faculty-of-medicine-health-and-human-sciences/departments-and-schools/school-of-psychological-sciences) at Macquarie University.

---

## How to Use This Repo

1. **Before each lecture:** Read the companion reading for that week (the `README.md` in each week's folder — this is the required reading)
2. **During lab weeks:** Open the challenge brief and starter notebook for your group work
3. **After labs:** Use the optional readings in `readings.md` and the examples to deepen your understanding

---

## Quick Start: Choose Your Setup

### **Option A: Local Installation (Recommended if it worked for you)**

Follow the [setup guide](setup/getting-started.md) to install Python, VS Code, and course packages on your computer. See [Week 2 troubleshooting](#week-2-setup-troubleshooting) below if you run into issues.

### **Option B: GitHub Codespaces (Fast, no installation needed) ⭐**

If you couldn't get Python/VS Code working on your laptop, use **GitHub Codespaces**. VS Code runs in your browser, all dependencies are pre-configured, and you pay nothing.

**Setup in 3 steps:**

1. Go to this repository (you're already here)
2. Click the green **Code** button (top-right) → **Codespaces** → **Create codespace on main**
3. Wait 2–3 minutes. VS Code opens in your browser with everything ready to go. Click the Python kernel dropdown (top-right) and select **AI for Behavioural Science** if prompted.

That's it. You can now:
- Open Jupyter notebooks (`.ipynb` files)
- Write and run Python code
- Save work to GitHub automatically
- **Use GitHub Copilot** (optional, only if you have Student Developer Pack approval — but free alternatives exist if you don't)

**Does Codespaces cost?** No, it's free. Codespaces gives everyone **120 free core-hours per month**, regardless of Student Developer Pack status. This course uses ~2–4 hours/week. You stay well under the limit. [How pricing works →](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces)

**No Student Developer Pack yet?** Don't worry. Codespaces works perfectly without it. You'll just use a free AI tool (like Gemini Code Assist) instead of Copilot. See the [Codespaces guide](resources/codespaces-guide.md#if-you-dont-have-student-developer-pack-yet-or-it-was-rejected) for details.

For full setup details, see the [Codespaces guide](resources/codespaces-guide.md).

---

## Week 2: Setup Troubleshooting

Struggled with local setup in Week 2? You're not alone, and there are solutions:

- **Can't install Miniconda?** → Use Codespaces (Option B above)
- **VS Code won't find Python?** → Use Codespaces, or restart your terminal after installation
- **Jupyter notebooks don't work?** → Use Codespaces (it's pre-configured)
- **Got it working on one laptop but visiting another?** → Use Codespaces

---

## Weekly Materials

The course runs over 13 topics — alternating lecture weeks (with a companion reading and slides) and challenge-lab weeks (with a brief, starter notebook, and dataset).

| Week | Type | Topic | Slides |
|------|------|-------|--------|
| 1 | Lecture | [Why ML and AI Belongs in the Cognitive, Psychological and Behavioural Sciences](weeks/week-01-lecture/) | <a href="https://xkiwilabs.github.io/Practical-AI-for-Behavioural-Science/weeks/week-01-lecture/slides/index.html" target="_blank">Slides</a> |
| 2 | Lab | [Setup, Plotting, and the LLM Problem-Solving Loop](weeks/week-02-lab/) | <a href="https://xkiwilabs.github.io/Practical-AI-for-Behavioural-Science/weeks/week-02-lab/slides/index.html" target="_blank">Slides</a> |
| 3 | Lecture | [Models, Not Magic: Generalisation, Overfitting, and How ML Misleads](weeks/week-03-lecture/) | <a href="https://xkiwilabs.github.io/Practical-AI-for-Behavioural-Science/weeks/week-03-lecture/slides/index.html" target="_blank">Slides</a> |
| 4 | Lab | [Regression Pipeline, Cross-Validation, and Interpretation](weeks/week-04-lab/) | <a href="https://xkiwilabs.github.io/Practical-AI-for-Behavioural-Science/weeks/week-04-lab/slides/index.html" target="_blank">Slides</a> |
| 5 | Lecture | [Prediction with Accountability: Classification, Uncertainty, and Evaluation](weeks/week-05-lecture/) | <a href="https://xkiwilabs.github.io/Practical-AI-for-Behavioural-Science/weeks/week-05-lecture/slides/index.html" target="_blank">Slides</a> |
| 6 | Lab | [Trees, Ensembles, Feature Importance, and Error Analysis](weeks/week-06-lab/) | <a href="https://xkiwilabs.github.io/Practical-AI-for-Behavioural-Science/weeks/week-06-lab/slides/index.html" target="_blank">Slides</a> |
| 7 | Lecture | [Discovering Structure: Clustering and Dimensionality Reduction](weeks/week-07-lecture/) | <a href="https://xkiwilabs.github.io/Practical-AI-for-Behavioural-Science/weeks/week-07-lecture/slides/index.html" target="_blank">Slides</a> |
| 8 | Lab | [PCA/UMAP, Clustering, and Stability Checks](weeks/week-08-lab/) | <a href="https://xkiwilabs.github.io/Practical-AI-for-Behavioural-Science/weeks/week-08-lab/slides/index.html" target="_blank">Slides</a> |
| 9 | Lecture | [Learning Representations: Neural Networks as Psychological Tools](weeks/week-09-lecture/) | <a href="https://xkiwilabs.github.io/Practical-AI-for-Behavioural-Science/weeks/week-09-lecture/slides/index.html" target="_blank">Slides</a> |
| 10 | Lab | [Simple Neural Network, Training Diagnostics, and Baseline Comparison](weeks/week-10-lab/) | <a href="https://xkiwilabs.github.io/Practical-AI-for-Behavioural-Science/weeks/week-10-lab/slides/index.html" target="_blank">Slides</a> |
| 11 | Lecture + Lab | [Meaning in Vectors: Embeddings and LLMs for Research Workflows](weeks/week-11-lecture-lab/) | <a href="https://xkiwilabs.github.io/Practical-AI-for-Behavioural-Science/weeks/week-11-lecture-lab/slides/index.html" target="_blank">Slides</a> |
| 12 | Review | [Course Review: Consolidation, Concept Practice, and Q&A](weeks/week-12-viva-review/) | <a href="https://xkiwilabs.github.io/Practical-AI-for-Behavioural-Science/weeks/week-12-viva-review/slides/index.html" target="_blank">Slides</a> |
| 13 | Lecture + Discussion | [Agents, Ethics, and Looking Back](weeks/week-13-lecture-and-discussion/) | <a href="https://xkiwilabs.github.io/Practical-AI-for-Behavioural-Science/weeks/week-13-lecture-and-discussion/slides/index.html" target="_blank">Slides</a> |

---

## Resources

Guides and references for tools used in this course, all written for beginners:

- **[AI Tools guide](resources/ai-tools-guide.md)** — Overview of AI tools: conversational AI, coding assistants, research tools, local models
- **[Prompt Engineering guide](resources/prompt-engineering-guide.md)** — Writing effective prompts: patterns, examples, and common mistakes
- **[VS Code guide](resources/vscode-guide.md)** — Navigate the interface, install extensions, use the terminal
- **[Jupyter Notebooks guide](resources/jupyter-guide.md)** — Cells, kernels, execution order, common mistakes
- **[GitHub guide](resources/github-guide.md)** — Account setup, navigating repos, Student Developer Pack
- **[Markdown guide](resources/markdown-guide.md)** — Formatting syntax for notebooks and READMEs
- **[HTML Slides guide](resources/html-slides-guide.md)** — Creating slides with reveal.js
- **[Presentation template](resources/presentation-template/)** — Ready-to-use HTML slide template

See the [resources folder](resources/) for the full list.

---

## Setup

See the [Getting Started guide](setup/getting-started.md) for instructions on installing Python, Jupyter, VS Code, and setting up your LLM assistant.

---

## The LLM Problem-Solving Loop

A core workflow you'll develop throughout this course. It has two nested loops: an outer loop for your research process, and an inner loop for working with AI.

**Outer loop (your research process):**

1. **PLAN** — Define what you want to achieve. What question are you answering? What output do you need?
2. **EXECUTE** — Use the inner loop (below) to get AI-generated code and analysis
3. **EVALUATE** — Does the result answer your question? Is it correct? Does it make sense given what you know about the domain?
4. **DOCUMENT** — Record what you did, what worked, and what you learned

**Inner loop (working with the AI):**

1. **ENGINEER** — Craft your prompt: be specific, provide context (your data, libraries, constraints), state your goal clearly, and, crucially, ***ask for a plan***
2. **PLAN** — The AI responds with a proposed approach. Review it critically — right methods, right steps? Redirect *before* anything is generated. If it skipped the plan and jumped to code, ask it to step back
3. **GENERATE** — Once the plan looks right, have the AI carry it out — code, text, visualisations, or a more detailed sub-plan for complex tasks
4. **VERIFY** — Read what the AI gives you. Don't just copy and paste — look at what it's doing. Then run it. Does it execute without errors? Does the output make sense?
5. **REFINE** — If it's not right: add more context, correct misunderstandings, try a different approach. Go back to the appropriate step — sometimes you need to fix the plan, sometimes just the output.

In practice, your first few trips around the loop are often about refining the *plan*; only later iterations shift to generating the actual output. The inner loop typically runs 2–5 times per task. That's normal. Even experienced developers iterate with AI tools. Strategies that help: break problems into smaller pieces, provide rich context (paste in column names, error messages, documentation), explain *what* went wrong not just *that* something went wrong, and refine at the right level (plan vs output).

**Critical rule:** Never trust LLM output without verification. You are the researcher. The AI is a tool.

See the [Week 1 companion reading](weeks/week-01-lecture/) for a detailed walkthrough with examples.

---

## AI Disclosure

I use LLMs and generative AI tools for virtually all aspects of my work: research, writing, coding, data analysis, course development, and scientific exploration. These tools make me more productive, help me think through problems from new angles, and let me spend less time on tedious mechanics and more time on the ideas that matter. I embrace their use, I actively explore how they can enhance research and scientific practice, and I encourage my students to do the same.

Here's the thing: using AI tools well is a skill, not a shortcut. It requires critical thinking, domain knowledge, and the ability to evaluate whether what the AI gives you is actually correct. That's what this course teaches. The use of AI should be praised, encouraged, and talked about openly, not hidden or treated as something to be ashamed of. We're all figuring out how to work with these tools, and the students who lean into that process will be better researchers for it.

In that spirit, I include an AI disclosure statement for nearly everything in this repository, and **I encourage you to do the same for any work you produce or share.** Transparency about AI use is not a confession; it's good scientific practice. Below is a template you can adapt for your own work.

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

Use this template (or something similar) for any work you produce with AI assistance. Be specific about what you used and what you checked. The goal isn't to limit your AI use; it's to make you a thoughtful, transparent user of these tools.

### Course Materials Disclosure

The content and materials for this course were designed and developed in collaboration with numerous AI tools, including [Claude](https://claude.ai), [ChatGPT](https://chat.openai.com), [GitHub Copilot](https://github.com/features/copilot), and [Gemini](https://gemini.google.com). All materials were reviewed, verified, and curated by the course instructor. This transparent use of AI in course development reflects the same approach we teach students throughout the unit: AI tools are powerful collaborators, but human judgement, verification, and critical evaluation remain essential.

It is also worth acknowledging that the large language models used to help create these materials, and all current LLMs, were trained on vast quantities of text scraped from the internet, largely without the explicit consent of the original authors. If you have ever published a paper, written a book, posted on a blog, or contributed to any publicly accessible text online, there is a near-certainty that your words were part of the training data for one or more of these models. This is sometimes described as *model-mediated content appropriation*: LLMs can reproduce, remix, and recombine the ideas and language of millions of authors without attribution. We want to explicitly acknowledge the collective intellectual labour of the scientists, researchers, educators, and writers whose published work forms the foundation on which these AI tools operate. Their contributions are embedded, uncredited, in every output these models produce, including the materials you are reading now.

---

## Licence

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Licence](https://creativecommons.org/licenses/by-nc-sa/4.0/).

[![CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

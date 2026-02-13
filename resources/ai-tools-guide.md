# AI Tools Guide (2026)

A comprehensive overview of the AI tools available to you as a student and researcher. All tools listed here have free tiers or student access. This guide focuses on what each tool is good for and how to get started.

---

## Conversational AI

These are the general-purpose AI assistants you'll use most throughout this course. All have free tiers.

### ChatGPT

- **Website:** <a href="https://chat.openai.com" target="_blank">chat.openai.com</a>
- **What it does:** General-purpose conversational AI. Handles coding, writing, analysis, and research questions.
- **Free tier:** GPT-4o with usage limits; unlimited GPT-4o-mini
- **Best for:** General questions, brainstorming, explaining concepts, drafting text
- **Deep Research:** Available on paid plans — the AI autonomously searches, reads, and synthesises information from many sources
- **Tip:** Use the "Code Interpreter" mode (called "Data Analysis" in ChatGPT) to upload files and have the AI run Python code for you directly

### Claude

- **Website:** <a href="https://claude.ai" target="_blank">claude.ai</a>
- **What it does:** Conversational AI from Anthropic. Strong at long documents, nuanced reasoning, and coding.
- **Free tier:** Claude Sonnet 4.5 with usage limits
- **Best for:** Analysing long papers, nuanced explanations, coding help, careful reasoning
- **Tip:** Claude handles very long inputs well — you can paste entire papers and ask detailed questions about them

### Gemini

- **Website:** <a href="https://gemini.google.com" target="_blank">gemini.google.com</a>
- **What it does:** Google's conversational AI. Natively multimodal (text, images, audio).
- **Free tier:** Gemini 2.5 Flash with generous limits
- **Deep Research:** Available — similar to ChatGPT's deep research, autonomously investigates topics
- **Best for:** Quick questions, image analysis, integration with Google Workspace
- **Tip:** Gemini can search the web in real-time, making it useful for finding recent papers and checking facts

---

## Coding Assistants

These tools help you write, debug, and understand code. They integrate into your code editor.

### GitHub Copilot

- **Website:** <a href="https://github.com/features/copilot" target="_blank">github.com/features/copilot</a>
- **What it does:** AI code completion and chat inside VS Code. Suggests code as you type and answers questions via Copilot Chat.
- **Free for students:** Apply for the <a href="https://education.github.com/pack" target="_blank">GitHub Student Developer Pack</a> to get Copilot Pro free
- **Best for:** Code autocompletion while you work, inline explanations, debugging in VS Code
- **Setup:** Install the "GitHub Copilot" extension in VS Code, then sign in with your GitHub account
- **Tip:** Copilot Chat (the sidebar panel) is great for asking "what does this code do?" or "why am I getting this error?"

### Cursor & Windsurf

- **Cursor:** <a href="https://cursor.com" target="_blank">cursor.com</a> · **Windsurf:** <a href="https://windsurf.com" target="_blank">windsurf.com</a>
- **What they do:** VS Code-based editors rebuilt around AI assistance. Deep integration of AI into every part of the coding workflow.
- **Free tiers:** Both have free tiers with limited completions
- **Best for:** More advanced coding projects, multi-file editing, AI-driven refactoring
- **Note:** These are optional alternatives to VS Code + Copilot. For this course, VS Code + Copilot is the recommended setup.

### CLI Agents

- **Claude Code:** <a href="https://docs.anthropic.com/en/docs/claude-code" target="_blank">docs.anthropic.com/en/docs/claude-code</a> (paid)
- **Codex CLI:** <a href="https://github.com/openai/codex" target="_blank">github.com/openai/codex</a> (paid)
- **Gemini CLI:** <a href="https://github.com/google-gemini/gemini-cli" target="_blank">github.com/google-gemini/gemini-cli</a> (free with Google account)
- **What they do:** AI agents that work in your terminal — they can read your codebase, write files, run tests, and fix bugs autonomously.
- **Note:** These are the cutting edge of AI coding. You don't need them for this course, but they're worth knowing about.

---

## Research Tools

These AI tools are designed specifically for academic research.

### NotebookLM

- **Website:** <a href="https://notebooklm.google.com" target="_blank">notebooklm.google.com</a>
- **What it does:** Upload papers, lecture notes, or textbook chapters. Get AI summaries, interactive mind maps, and even podcast-style audio overviews.
- **Free:** Yes, with a Google account
- **Best for:** Understanding papers, generating summaries, study revision
- **Tip:** Upload the companion reading and lecture slides for each week to create your own study resource

### Semantic Scholar

- **Website:** <a href="https://semanticscholar.org" target="_blank">semanticscholar.org</a>
- **What it does:** AI-powered academic search engine. Helps you find relevant papers and understand citation networks.
- **Free:** Yes
- **Best for:** Finding papers for your presentation and written assignment, exploring who cites whom

### Elicit

- **Website:** <a href="https://elicit.com" target="_blank">elicit.com</a>
- **What it does:** Evidence synthesis from 200M+ academic papers. Ask a research question, get structured answers with citations.
- **Free tier:** Limited searches per month
- **Best for:** Literature reviews, finding papers that support or contradict a claim

### Consensus

- **Website:** <a href="https://consensus.app" target="_blank">consensus.app</a>
- **What it does:** Ask research questions in plain language, get answers backed by peer-reviewed literature.
- **Free tier:** Limited searches per month
- **Best for:** Quick evidence checks — "Does exercise reduce depression?" → answers from published studies

---

## Running AI Locally

For privacy-sensitive work or offline use, you can run AI models on your own computer.

### Why Run Locally?

When you use ChatGPT or Claude, your prompts are sent to external servers. For coursework, that's fine. But in research — especially with sensitive clinical data, patient records, or proprietary datasets — sending data to external services may violate ethics approvals or data governance policies. Running locally means your data never leaves your machine.

### Tools for Local AI

- **Ollama:** <a href="https://ollama.com" target="_blank">ollama.com</a> — Open-source, command-line tool for running models locally. Free.
- **LM Studio:** <a href="https://lmstudio.ai" target="_blank">lmstudio.ai</a> — Graphical interface, beginner-friendly. Free.

### What You Can Run

- **Meta Llama 4** — Available in Scout and Maverick variants
- **Mistral Large 3** — 675B parameters, Apache 2.0 licence
- **Google Gemma 3** — Smaller, efficient, designed for local use

### Hardware Requirements

Modern Apple Silicon Macs (M2 Pro and above) can run useful models comfortably. On the PC side, you need a dedicated GPU with reasonable VRAM. Smaller models (7B–13B parameters) run on most recent laptops; larger models need more capable hardware.

---

## Image, Video, and Audio

- **DALL-E 3** (via ChatGPT) — Image generation from text
- **Midjourney** (<a href="https://midjourney.com" target="_blank">midjourney.com</a>) — High-quality image generation
- **ElevenLabs** (<a href="https://elevenlabs.io" target="_blank">elevenlabs.io</a>) — Text-to-speech and voice cloning
- **Whisper** (via OpenAI or locally) — Speech-to-text transcription

These can be useful for creating experimental stimuli, generating visualisations, transcribing interviews, and making materials accessible.

---

## Which Tool Should I Use?

| I want to... | Try this first |
|--------------|----------------|
| Get help with Python code | GitHub Copilot (in VS Code) or ChatGPT |
| Understand a research paper | Claude (paste the paper) or NotebookLM |
| Find papers for my assignment | Semantic Scholar or Elicit |
| Debug an error in my notebook | Copilot Chat or ChatGPT (paste the error) |
| Quick fact-check a claim | Consensus or Gemini (with web search) |
| Work with sensitive data | Ollama or LM Studio (local models) |
| Create a study summary | NotebookLM (upload your materials) |

---

*[Back to resources](README.md) · [Back to course overview](../README.md)*

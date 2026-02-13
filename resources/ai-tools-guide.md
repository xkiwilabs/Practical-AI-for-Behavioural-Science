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
- **What it does:** AI coding assistant inside VS Code with four modes: inline completions (ghost text as you type), Chat (ask questions and debug), Edit mode (describe changes in plain English), and Agent mode (autonomous multi-step coding). Also includes a model selector to choose between GPT, Claude, and Gemini models.
- **Free for students:** Apply for the <a href="https://education.github.com/pack" target="_blank">GitHub Student Developer Pack</a> to get Copilot Pro free
- **Best for:** Code autocompletion while you work, inline explanations, debugging in VS Code
- **Setup:** Install the "GitHub Copilot" extension in VS Code, then sign in with your GitHub account
- **Full guide:** See the **[Copilot guide](copilot-guide.md)** for a detailed walkthrough of each mode with examples

### Cursor & Windsurf

- **Cursor:** <a href="https://cursor.com" target="_blank">cursor.com</a> · **Windsurf:** <a href="https://windsurf.com" target="_blank">windsurf.com</a>
- **What they do:** VS Code-based editors rebuilt around AI assistance. Deep integration of AI into every part of the coding workflow.
- **Free tiers:** Both have free tiers with limited completions
- **Best for:** More advanced coding projects, multi-file editing, AI-driven refactoring
- **Note:** These are optional alternatives to VS Code + Copilot. For this course, VS Code + Copilot is the recommended setup.

### CLI Agents

CLI stands for **Command-Line Interface** — these are tools you run in the terminal rather than through a graphical window. They can read your entire codebase, write files, run tests, and fix bugs autonomously.

| Tool | Provider | Install | Access |
|------|----------|---------|--------|
| **Gemini CLI** | Google | `npm install -g @google/gemini-cli` | Free with Google account |
| **Claude Code** | Anthropic | Download from <a href="https://claude.ai/download" target="_blank">claude.ai/download</a> | Max, Team, or API subscription |
| **Codex CLI** | OpenAI | `npm install -g @openai/codex` | Plus, Pro, or API subscription |

- **Links:** <a href="https://github.com/google-gemini/gemini-cli" target="_blank">Gemini CLI on GitHub</a> · <a href="https://docs.anthropic.com/en/docs/claude-code" target="_blank">Claude Code docs</a> · <a href="https://github.com/openai/codex" target="_blank">Codex CLI on GitHub</a>
- The `npm` install commands require <a href="https://nodejs.org/" target="_blank">Node.js</a> (which includes npm). Gemini CLI needs Node.js 20+; Codex CLI needs Node.js 18+.
- **Note:** You don't need any of these for this course. They're here for students who are curious or who already have paid subscriptions.

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

These tools can be useful for creating experimental stimuli, generating visualisations, transcribing interviews, and making materials accessible.

### Image Generation

- **Gemini** (<a href="https://gemini.google.com" target="_blank">gemini.google.com</a>) — Generate images directly in the Gemini app by asking it to create an image. Powered by Imagen 3 / Gemini 3 Pro Image. Free tier includes daily image generation. Via the API (Google AI Studio), Gemini 2.5 Flash Image provides up to 500 images per day at no cost.
- **DALL-E 3** (via ChatGPT) — Image generation from text descriptions. Available to free ChatGPT users with daily limits.
- **Midjourney** (<a href="https://midjourney.com" target="_blank">midjourney.com</a>) — High-quality artistic image generation. Paid only, but produces stunning results.

### Video Generation

- **Gemini + Veo** (<a href="https://gemini.google.com" target="_blank">gemini.google.com</a>) — Generate short videos (up to 8 seconds, up to 4K) from text or image prompts using Veo 3.1. Available in the Gemini app and via the API. Includes natively generated audio. Free access with daily limits; expanded access with Google AI Pro/Ultra subscriptions or the free student plan.

### Text-to-Speech

- **Gemini TTS** (<a href="https://ai.google.dev/gemini-api/docs/speech-generation" target="_blank">ai.google.dev</a>) — Gemini 2.5 Flash and Pro TTS models convert text to natural-sounding speech with control over style, accent, pace, and emotion using natural language prompts. Supports 30+ speakers in 80+ languages. Available via Google AI Studio and the Gemini API.
- **ElevenLabs** (<a href="https://elevenlabs.io" target="_blank">elevenlabs.io</a>) — High-quality text-to-speech and voice cloning. Free tier with limited characters per month.
- **NotebookLM Audio Overviews** (<a href="https://notebooklm.google.com" target="_blank">notebooklm.google.com</a>) — Upload papers or notes and get AI-generated podcast-style audio summaries. Free.

### Speech-to-Text

- **Whisper** (via OpenAI or locally) — Speech-to-text transcription. Highly accurate, supports many languages. Can run locally for free or via the OpenAI API.

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
| Generate an image or diagram | Gemini or ChatGPT (DALL-E 3) |
| Create a short video clip | Gemini (Veo 3.1) |
| Convert text to speech | Gemini TTS or ElevenLabs |
| Transcribe an interview | Whisper (locally or via OpenAI API) |

---

*[Back to resources](README.md) · [Back to course overview](../README.md)*

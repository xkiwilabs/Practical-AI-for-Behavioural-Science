# GitHub Copilot Guide

GitHub Copilot is an AI coding assistant that lives inside VS Code. It's free for students (via the GitHub Student Developer Pack) and is the main coding assistant we recommend for this course. This guide walks you through everything it can do.

---

## Getting Access

If you followed the [Getting Started guide](../setup/getting-started.md), you should already have access:

1. Sign up for the [GitHub Student Developer Pack](https://education.github.com/pack) using your `@students.mq.edu.au` email
2. Install the **GitHub Copilot** extension in VS Code
3. Sign in to GitHub from VS Code (Accounts icon → Sign in with GitHub)

Once approved, you'll see a small Copilot icon in the VS Code status bar. Approval can take a few days — everything else in the course works without it.

---

## The Four Ways to Use Copilot

Copilot isn't just one feature — it has four different modes, each useful in different situations. Think of them as four levels of help, from a gentle nudge to a full-on coding partner.

### 1. Inline Completions (Ghost Text)

**What it does:** As you type code, Copilot suggests the rest of the line (or even several lines) in grey "ghost" text.

**How to use it:**
- Start typing code in any Python file or notebook cell
- Wait a moment — a grey suggestion appears
- Press **Tab** to accept the suggestion, or keep typing to ignore it
- Press **Esc** to dismiss a suggestion

**Example:** If you type `import pandas`, Copilot might suggest ` as pd` in grey text. Press Tab and it fills it in.

**Tips:**
- Write a comment describing what you want, then press Enter — Copilot often writes the code for you
- For example, type `# Create a scatter plot of Sleep vs Mood using seaborn` and press Enter — Copilot will suggest the plotting code
- You don't have to accept the whole suggestion. You can press `Ctrl+Right` (Windows) or `Cmd+Right` (Mac) to accept just one word at a time

---

### 2. Chat

**What it does:** A conversation panel where you can ask Copilot questions, get explanations, and request code — like having ChatGPT built into your code editor, with full context of your files.

**How to open it:** Click the **Copilot Chat icon** in the Activity Bar (left sidebar), or press `Cmd+Shift+I` (Mac) / `Ctrl+Shift+I` (Windows).

**What you can ask:**
- "What does this code do?" (select code first, then ask)
- "I'm getting a `KeyError: 'Depression'` — here's my code. What's wrong?"
- "Write a function that calculates the mean and standard deviation of each column"
- "Explain what a pandas DataFrame is in plain language"
- "How do I save a matplotlib figure as a PNG file?"

**Tips:**
- Copilot Chat can see your open files, so it already has context about your code — you don't need to paste everything in
- Select a block of code before asking a question, and Copilot will focus on that code
- Use `@workspace` in your message to let Copilot search across all files in your project (e.g., `@workspace where is the dataset loaded?`)
- You can also type `/explain` to get an explanation of selected code, or `/fix` to ask Copilot to fix an error

---

### 3. Edit Mode

**What it does:** You describe a change in natural language, and Copilot edits your code directly — showing you the changes before you accept them.

**How to use it:**
1. Open the Chat panel
2. Look at the top of the chat — there's a mode selector. Choose **Edit**
3. Type what you want to change (e.g., "Add axis labels to the scatter plot" or "Change the colour palette to 'coolwarm'")
4. Copilot shows the proposed changes as a diff (green = added, red = removed)
5. Review the changes and click **Accept** or **Discard**

**When to use it:** Edit mode is great when you already have working code and want to modify it — adding features, fixing formatting, changing variable names, etc.

---

### 4. Agent Mode

**What it does:** The most powerful mode. Copilot works autonomously across multiple files — planning changes, writing code, running it, checking for errors, and fixing problems automatically. It's like having a coding partner who can do the typing for you.

**How to use it:**
1. Open the Chat panel
2. Switch the mode selector to **Agent**
3. Describe what you want (e.g., "Load the CSV file from the data folder, clean missing values, and create a correlation heatmap")
4. Copilot plans the steps, makes the changes, and shows you what it did
5. Review and accept or reject the changes

**When to use it:** Agent mode is great for bigger tasks — setting up a new analysis, creating multiple plots, or restructuring code. It works best when you give it a clear description of what you want.

**Tips:**
- Agent mode can run your code and see the output — so if something fails, it tries to fix it automatically
- You can guide it with follow-up messages ("Actually, use seaborn instead of matplotlib for the heatmap")
- Always review what Agent mode produces — it's powerful but not perfect

---

## The Model Selector

At the top of the Chat panel, you'll see a **model dropdown** next to the mode selector. This lets you choose which AI model powers Copilot's responses.

Different models have different strengths:

| Model | Good for |
|-------|----------|
| **GPT-4o** | Fast responses, general coding tasks |
| **Claude Sonnet** | Careful reasoning, longer code, nuanced explanations |
| **Gemini** | Fast, good at search and factual questions |
| **o3-mini** / **o4-mini** | Complex reasoning, planning, multi-step problems |

You don't need to think too hard about this — the default model works well for most tasks. But if you're not happy with a response, try switching models and asking again. Different models sometimes give better answers for different kinds of questions.

---

## Copilot for Psychology Students: Practical Examples

Here are some real situations you'll encounter in this course and how Copilot can help:

### "I don't know how to start"

Type a comment in a code cell describing what you want:

```python
# Load the dataset from data/fake_depression_dataset.csv
# Show the first 5 rows and print the column names
```

Then press Enter — Copilot will suggest the code.

### "I got an error and I don't know what it means"

Copy the error message. Open Copilot Chat and say:

> "I'm running this code in a Jupyter notebook and got this error. What's wrong and how do I fix it?"

Then paste the error. Copilot can see your code file for context.

### "I want to make a plot but don't know the syntax"

In Copilot Chat, be specific:

> "Using seaborn and matplotlib, create a box plot comparing Depression scores across Gender categories. Use the DataFrame called `data`. Add a title and axis labels."

### "I need to explain what my code does"

Select your code, then type `/explain` in Copilot Chat. It will give you a plain-language breakdown you can use in your notebook's markdown cells.

### "My setup isn't working"

Paste the error message into Copilot Chat (or ChatGPT/Claude in your browser). AI assistants are great at diagnosing installation errors, package conflicts, and environment problems.

---

## Common Issues

**Copilot isn't suggesting anything:**
- Check the status bar — is the Copilot icon visible? If it has a line through it, Copilot is disabled for this file type.
- Make sure you're signed in to GitHub (Accounts icon in the bottom-left).
- Your Student Developer Pack may still be processing — check your email for approval.

**Suggestions are wrong or unhelpful:**
- Add more context — write a detailed comment above the line explaining what you want.
- Try being more specific about the libraries, variable names, and data structures you're using.
- Switch models in the model dropdown.

**Chat doesn't know about my code:**
- Make sure the relevant file is open in the editor. Copilot Chat uses your open files as context.
- Use `@workspace` to search across all project files.
- Select the specific code you're asking about before typing your question.

**"Copilot is not available for this file type":**
- Copilot works best with code files (`.py`, `.ipynb`). It may not activate for `.md` or `.txt` files.

---

## Alternative AI Coding Tools

GitHub Copilot is our top recommendation because it's free for students, built into VS Code, and works without extra configuration. But if you have access to other AI services, you can also use:

### VS Code Extensions

| Extension | Provider | Access |
|-----------|----------|--------|
| **Gemini Code Assist** | Google | Free with a Google account |

Search for "Gemini Code Assist" in VS Code's Extensions panel and sign in with your Google account. It offers similar features to Copilot (chat, inline completions, code explanations).

### CLI Tools (Command-Line Interface)

A CLI is a tool you run in the terminal instead of through a graphical window. These are more advanced, but worth knowing about — they can read your entire codebase, write files, and run tests autonomously.

| Tool | Provider | Install command | Access |
|------|----------|----------------|--------|
| **Gemini CLI** | Google | `npm install -g @google/gemini-cli` | Free with a Google account |
| **Claude Code** | Anthropic | Download from [claude.ai/download](https://claude.ai/download) | Requires Max/Team/API subscription |
| **Codex CLI** | OpenAI | `npm install -g @openai/codex` | Requires Plus/Pro/API subscription |

> **What is `npm`?** It stands for Node Package Manager — a tool for installing JavaScript/Node.js software. If you want to use these CLI tools, you'd need to install [Node.js](https://nodejs.org/) first (which includes `npm`). This is entirely optional for this course.

You don't need any of these tools for PSYC4411. They're here for students who are curious or who already have paid accounts with these providers. See the [AI Tools guide](ai-tools-guide.md) for a full overview.

---

*[Back to resources](README.md) · [Back to course overview](../README.md)*

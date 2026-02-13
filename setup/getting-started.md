# Getting Started — PSYC4411 Setup Guide

**Please complete these steps before Week 2.** The first part of the Week 2 class will be dedicated to troubleshooting any issues, so don't worry if you get stuck — bring your laptop and we'll sort it out together.

Everything you need for this course is **free**. This guide assumes you've never installed programming tools before, so we'll walk through every step.

Here's what you'll set up:

| Tool | What it does |
|------|-------------|
| **GitHub** | A platform for sharing code and collaborating (also gets you free AI tools) |
| **VS Code** | A text editor designed for writing and running code |
| **Miniconda** | A lightweight installer for Python and package management |
| **Course packages** | Libraries for plotting, statistics, and machine learning |
| **AI assistants** | Tools that help you write code and understand concepts |

---

## Step 1: Create a GitHub Account

GitHub is where developers (and increasingly, researchers) store and share code. You'll need an account to access free student tools, including GitHub Copilot — an AI coding assistant that works inside VS Code.

1. Go to [github.com](https://github.com) and click **Sign up**
2. **Use a personal email address** (Gmail, Outlook, etc.) — not your Macquarie email. Why? Your MQ email will stop working after you graduate, but your GitHub account will be useful for years to come.
3. Choose a username. This will be visible to others, so pick something professional-ish (e.g., `jsmith-psych` rather than `xX_party_animal_Xx`).
4. Complete the sign-up process and verify your email.

### Add Your MQ Email and Get Free Student Tools

5. Once logged in, go to **Settings** → **Emails** → **Add email address** and add your `@students.mq.edu.au` email. Verify it.
6. Go to the [GitHub Student Developer Pack](https://education.github.com/pack) and click **Sign up for Student Developer Pack**
7. Select your `@students.mq.edu.au` email when asked for academic verification
8. You may need to upload proof of enrolment (a screenshot of your student ID or enrolment confirmation works)

The Student Developer Pack gives you **free access to GitHub Copilot Pro** and over 90 other developer tools. Approval can take a few days, so do this early.

---

## Step 2: Install VS Code

VS Code (Visual Studio Code) is a free text editor made by Microsoft. It's where you'll write and run your code, open Jupyter notebooks, and use AI assistants.

### macOS

1. Go to [code.visualstudio.com](https://code.visualstudio.com) and click the download button for Mac
2. Open the downloaded `.zip` file — it will unzip into an application called **Visual Studio Code**
3. Drag **Visual Studio Code** into your **Applications** folder
4. Open it from Applications (you may need to right-click → Open the first time, then click "Open" on the security dialog)

### Windows

1. Go to [code.visualstudio.com](https://code.visualstudio.com) and click the download button for Windows
2. Run the downloaded installer
3. **Important:** When you see the "Select Additional Tasks" screen, make sure to check:
   - ✅ "Add to PATH" (this lets you open VS Code from the command line)
   - ✅ "Register Code as an editor for supported file types"
4. Click Install, then Finish

### First Launch

When you open VS Code for the first time, you'll see a Welcome tab. Feel free to explore it, or close it — we'll set up the important bits in Step 6.

---

## Step 3: Download the Course Repository

All course materials live in a GitHub repository. You need to **clone** (download a linked copy of) this repository to your computer. The key benefit of cloning rather than just downloading a ZIP file: when we add new materials each week, you can **pull** (fetch) the updates with one click.

### Using VS Code

1. Open VS Code
2. Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows) to open the **Command Palette**
3. Type `Git: Clone` and select it
4. Paste this URL and press Enter:
   ```
   https://github.com/xkiwilabs/Current-Advances-in-Psychological-Methods-and-Analyses-Repo.git
   ```
5. Choose where to save it (your Desktop or Documents folder is fine)
6. When VS Code asks "Would you like to open the cloned repository?", click **Open**

You should now see all the course folders in the VS Code sidebar.

> **If VS Code says Git is not installed:**
> - **Mac:** You'll see a pop-up asking to install "Command Line Developer Tools" — click **Install** and wait for it to finish (this can take a few minutes). Then try the clone steps again.
> - **Windows:** Download and install Git from [git-scm.com](https://git-scm.com). Use the default settings (click Next through each screen). Restart VS Code, then try the clone steps again.

### Pulling Updates Later

Throughout the semester, we'll add new weekly materials. To get the latest content:

1. Open the course folder in VS Code
2. Click the **Source Control** icon in the left sidebar (it looks like a branch/fork symbol)
3. Click the **⋯** (three dots) menu at the top of the Source Control panel → **Pull**

Any new or updated files will be downloaded automatically. We'll remind you to pull before each new week.

---

## Step 4: Install Miniconda

Miniconda is a lightweight installer that gives you Python and **conda** — a tool for managing packages and environments. An environment is a self-contained set of packages that keeps your course tools separate from everything else on your computer, so nothing gets mixed up.

> **Already have Anaconda or Miniconda installed?** You can skip this step entirely — go straight to Step 5. Anaconda includes everything Miniconda does (and more).

### macOS

1. Go to the [Miniconda download page](https://docs.anaconda.com/miniconda/) and download the **macOS installer** (choose the `.pkg` file for the easiest install)
2. Open the downloaded `.pkg` file and follow the installer prompts (click Continue, Agree, Install)
3. When the installer finishes, **close and reopen Terminal** — this is important so your terminal knows where to find conda

**Verify it worked:** Open **Terminal** (search for "Terminal" in Spotlight, or find it in Applications → Utilities) and type:

```
conda --version
```

You should see something like `conda 24.x.x`. If you see "command not found", try closing and reopening Terminal. If it still doesn't work, you may need to run `~/miniconda3/bin/conda init` and then restart Terminal.

### Windows

1. Go to the [Miniconda download page](https://docs.anaconda.com/miniconda/) and download the **Windows installer** (the `.exe` file)
2. Run the downloaded installer
3. **Important:** During installation, check the box that says **"Add Miniconda3 to my PATH environment variable"**. The installer warns against this, but for this course it makes everything much easier.
4. Click **Install** and wait for it to finish
5. **Close and reopen PowerShell** after installation

**Verify it worked:** Open **PowerShell** (search for "PowerShell" in the Start menu) and type:

```
conda --version
```

You should see something like `conda 24.x.x`. If you get an error, make sure you checked the "Add to PATH" box during installation — if you missed it, uninstall Miniconda and reinstall with that box checked.

---

## Step 5: Run the Setup Script

This is where the magic happens. We've written a script that automatically:
- Creates a **conda environment** called `psyc4411` — a self-contained set of packages for this course
- Installs all the Python libraries you'll need (pandas for data, matplotlib for plotting, scikit-learn for machine learning, etc.)
- Registers everything with VS Code/Jupyter so it all works together

You should still have the course repository open in VS Code from Step 3. If not, open VS Code and go to **File → Open Folder** and select the course repository folder.

1. Open the **terminal inside VS Code**: go to **View → Terminal** (or press `` Ctrl+` `` — that's the backtick key, usually below Escape)
2. **Windows only:** You may need to allow scripts to run (this is a one-time security setting). Type:
   ```
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
   Press **Y** if asked to confirm.
3. Navigate to the setup folder:
   ```
   cd setup
   ```
4. Run the setup script:
   - **Mac:** `bash setup-mac.sh`
   - **Windows:** `.\setup-windows.ps1`
5. Wait for it to finish. You'll see progress messages and, at the end, "Setup complete!"

### If Something Goes Wrong

- **"conda not found"** — Miniconda isn't installed or isn't in your PATH. Go back to Step 4. Make sure you closed and reopened VS Code after installing Miniconda (the terminal inside VS Code needs to be restarted too).
- **"environment already exists"** — The script will ask if you want to recreate it. Choose "y" to start fresh.
- **Installation hangs for a long time** — Some packages are large. Give it up to 10 minutes on a slow connection. If it's truly stuck, press `Ctrl + C` to cancel and try again.
- **Any other error** — Take a screenshot and bring it to class in Week 2. We'll figure it out together.

---

## Step 6: Install VS Code Extensions

Extensions add extra features to VS Code. You need three (and one optional but highly recommended one):

1. Open VS Code
2. Click the **Extensions** icon in the left sidebar (it looks like four squares, with one slightly detached) — or press `Ctrl+Shift+X` (Windows) / `Cmd+Shift+X` (Mac)
3. Search for and install each of these:

| Extension | Publisher | What it does |
|-----------|-----------|-------------|
| **Python** | Microsoft | Python language support, debugging, linting |
| **Jupyter** | Microsoft | Run Jupyter notebooks inside VS Code |
| **GitHub Copilot** | GitHub | AI code completion + Copilot Chat (requires Student Developer Pack) |

For each one: type the name in the search bar, find the one by the correct publisher, and click **Install**.

**Optional extras:** If you have a Google account, you can also install **Gemini Code Assist** (by Google) for an alternative AI assistant inside VS Code. And if you have a paid ChatGPT or Claude subscription, see the [Copilot guide](../resources/copilot-guide.md#alternative-ai-coding-tools) for other options.

### Sign In to GitHub from VS Code

This step connects VS Code to your GitHub account. It enables Copilot, syncs your settings across devices, and lets you access repositories from within VS Code.

1. Click the **Accounts** icon in the bottom-left corner of VS Code (it looks like a person silhouette)
2. Click **Sign in with GitHub to use GitHub Copilot** (or **Turn on Cloud Changes** — either works to start the sign-in flow)
3. A browser window will open asking you to authorise VS Code to access your GitHub account — click **Authorize**
4. You'll be redirected back to VS Code. You should now see your GitHub username in the bottom-left corner.

Once signed in, three things happen automatically:
- **GitHub Copilot** activates (if your Student Developer Pack has been approved — you'll see a small Copilot icon in the bottom status bar)
- **Settings Sync** turns on, so your VS Code setup (extensions, themes, keybindings) is backed up to your GitHub account and follows you across devices
- **Git integration** connects, so you can push/pull code to GitHub directly from VS Code later in the course

If your Student Developer Pack hasn't been approved yet, Copilot won't activate — that's fine, everything else still works. Come back to check once you get the approval email.

---

## Step 7: Test Your Setup

Let's make sure everything works together. There are two ways to test — a notebook test and a script test.

### Test 1: Notebook (test-setup.ipynb)

1. Open VS Code and open the course repository folder (if it's not already open from Step 3, go to **File → Open Folder** and select `Current-Advances-in-Psychological-Methods-and-Analyses-Repo`)
2. Navigate to `setup/test-setup.ipynb` in the file explorer on the left and click to open it
4. **Select the right kernel:** When the notebook opens, look at the top right corner of the notebook. You should see a kernel selector — click it and choose **PSYC4411** from the list. If you don't see it, try selecting "Python Environments" and look for `psyc4411 (conda)`.
5. Click **Run All** (the double-play button at the top of the notebook) or run each cell one at a time with `Shift + Enter`
6. If you see library version numbers and a scatter plot, followed by "Setup complete!" — you're done with this test!

### Test 2: Python script (test-setup.py)

This test runs as a Python script in the terminal — good practice for running code outside of a notebook.

1. Open a terminal (in VS Code: View → Terminal, or use the macOS Terminal / Windows PowerShell)
2. Activate the course environment:
   ```
   conda activate psyc4411
   ```
   You should see `(psyc4411)` appear at the start of your terminal prompt.
3. Navigate to the setup folder (if you're not already there):
   ```
   cd path/to/Current-Advances-in-Psychological-Methods-and-Analyses-Repo/setup
   ```
4. Run the test script:
   ```
   python test-setup.py
   ```
5. If you see "All checks passed!" — your setup is complete!

**If the PSYC4411 kernel doesn't appear in VS Code:** Close VS Code completely, reopen it, and try again. Sometimes VS Code needs a restart to detect newly created environments.

---

## Step 8: Set Up Your AI Coding Assistants

Throughout this course, you'll use AI assistants to help write code, debug errors, and understand concepts. Think of these as very knowledgeable (but sometimes confidently wrong) study partners. Here's what's available:

### Free for Everyone

These tools have free tiers that are more than enough for this course:

- **ChatGPT** — [chat.openai.com](https://chat.openai.com)
  General-purpose AI assistant. Great for explaining concepts and helping with code. The free tier includes GPT-4o mini. Also has a **Deep Research** mode that can autonomously investigate topics across many sources — like having a research assistant that reads dozens of papers for you.

- **Claude** — [claude.ai](https://claude.ai)
  Another excellent AI assistant with a free tier. Particularly good at careful, detailed explanations and working through long pieces of code.

- **Google Gemini** — [gemini.google.com](https://gemini.google.com)
  Google's AI assistant with a free tier. Also has a **Deep Research** mode for comprehensive literature and topic exploration.

### Enhanced Free Access for Students

These give you more powerful AI access at no cost:

- **GitHub Copilot Pro** (free via Student Developer Pack) — This is the big one for coding. Copilot works directly inside VS Code and gives you four powerful features:
  - **Inline completions** — suggests code as you type (press Tab to accept)
  - **Copilot Chat** — ask questions, debug errors, get explanations (like ChatGPT inside VS Code)
  - **Edit mode** — describe what you want to change in plain English, and Copilot edits your code
  - **Agent mode** — describe a whole task and Copilot plans, writes, and tests the code for you
  - **Model selector** — choose between different AI models (GPT, Claude, Gemini) for different tasks

  If you completed Step 1, you should have access once your Student Developer Pack is approved. See the **[Copilot guide](../resources/copilot-guide.md)** for a full walkthrough of each feature.

- **Google Gemini Pro Student Plan** — Free for 1 year. Includes Gemini Pro, Deep Research, and 2TB of Google storage. Sign up at [gemini.google/students](https://gemini.google/students/) (verified through SheerID with your university email).

### Research-Specific Tools

These tools are built specifically for academic research:

- **NotebookLM** — [notebooklm.google.com](https://notebooklm.google.com)
  Free. Upload papers, lecture notes, or textbook chapters, and get AI-generated summaries, interactive mind maps, and data tables. Excellent for literature reviews and understanding new topics.

- **Elicit** — [elicit.com](https://elicit.com)
  Evidence synthesis from over 200 million academic papers. Ask a research question, get structured summaries of relevant findings.

- **Consensus** — [consensus.app](https://consensus.app)
  Ask research questions in plain language, get answers backed by peer-reviewed literature.

- **Semantic Scholar** — [semanticscholar.org](https://semanticscholar.org)
  AI-powered academic search engine covering over 200 million papers. Great for finding related work and understanding citation networks.

### What About Deep Research?

Both ChatGPT and Gemini now offer **Deep Research** modes that go beyond a quick chat response. When you use Deep Research, the AI will autonomously search, read, and synthesise information across many sources — spending several minutes investigating your question thoroughly. This is incredibly useful for:
- Understanding a new topic from multiple angles
- Literature reviews and finding relevant papers
- Exploring how a method has been used across different research areas

### Our Recommendation

Set up **GitHub Copilot in VS Code** (for in-line code help while you work) plus keep a browser tab open with **ChatGPT or Claude** (for longer explanations, debugging help, and concept questions). Try different tools throughout the semester — each has different strengths, and part of becoming a skilled researcher is learning which tool works best for which task.

---

## Optional: Set Up API Keys for Programmatic Access

The AI assistants above all work through their websites and VS Code extensions — you don't need API keys for normal use in this course. However, if you want to call AI models directly from Python code (e.g., for text analysis, embeddings, or automated tasks in later weeks), you can set up API keys.

**Why you might want this:** In Weeks 9–11, we'll work with embeddings and programmatic AI access. Having API keys ready means you can run code that calls these models directly, rather than copying and pasting between a chat window and your notebook.

### How to set it up

1. **Create a `.secrets` folder** in the root of your course repository:
   ```
   Current-Advances-in-Psychological-Methods-and-Analyses-Repo/
   └── .secrets/
       └── api_keys.json
   ```

2. **Create `api_keys.json`** inside that folder. Copy and paste this template:

   ```json
   {
     "openai": {
       "api_key": "PASTE_YOUR_OPENAI_API_KEY_HERE",
       "note": "Get from https://platform.openai.com/api-keys"
     },
     "anthropic": {
       "api_key": "PASTE_YOUR_ANTHROPIC_API_KEY_HERE",
       "note": "Get from https://console.anthropic.com/settings/keys"
     },
     "google": {
       "api_key": "PASTE_YOUR_GOOGLE_AI_API_KEY_HERE",
       "note": "Get from https://aistudio.google.com/apikey"
     }
   }
   ```

3. **Replace the placeholder values** with your actual API keys. You don't need all three — just add the ones you have. Most providers offer free tiers with limited usage that is more than enough for this course.

4. **Make sure `.secrets/` is in your `.gitignore`** so your keys are never pushed to GitHub. The course repo already includes this — but if you're working in your own repo, add this line to your `.gitignore`:
   ```
   .secrets/
   ```

### Where to get API keys

| Provider | Free tier | Where to get a key |
|----------|-----------|-------------------|
| **OpenAI** | Limited free credits for new accounts | <a href="https://platform.openai.com/api-keys" target="_blank">platform.openai.com/api-keys</a> |
| **Anthropic** | Limited free credits for new accounts | <a href="https://console.anthropic.com/settings/keys" target="_blank">console.anthropic.com/settings/keys</a> |
| **Google AI** | Generous free tier (Gemini API) | <a href="https://aistudio.google.com/apikey" target="_blank">aistudio.google.com/apikey</a> |

### How to use them in Python

```python
import json

# Load your API keys
with open("../../.secrets/api_keys.json") as f:
    keys = json.load(f)

# Example: use the OpenAI key
openai_key = keys["openai"]["api_key"]
```

We'll provide starter code for this when we get to the relevant weeks. You don't need to worry about it now.

> **Important:** Never share your API keys, paste them into chat messages, or commit them to GitHub. Treat them like passwords. The `.secrets/` folder is gitignored specifically to prevent accidental sharing.

---

## Optional: Install Local AI Models

> **Only do this if your computer has 32GB of RAM or more.** If you're not sure, skip this step — the cloud-based AI tools above are more than enough for this course.

Later in the semester, we'll explore running AI models directly on your own computer. This is useful in research when you're working with sensitive data that can't be sent to external servers, or when you want to experiment without usage limits. If you have capable hardware, you can set this up now.

**Two tools to choose from (or install both):**

- **Ollama** — Runs from the terminal. Lightweight, scriptable, great for automation. See the **[Ollama guide](../resources/ollama-guide.md)** for installation and setup.
- **LM Studio** — Has a graphical interface that looks like ChatGPT. Easier if you're not yet comfortable with the terminal. See the **[LM Studio guide](../resources/lm-studio-guide.md)** for installation and setup.

**Who should consider this?**

- **Mac users** with Apple Silicon (M1 Pro/Max or newer) and **32GB+ unified memory** — you're in the sweet spot
- **Desktop/mini PC users** with **64GB+ RAM** — excellent for local models
- **Windows/Linux users** with an **NVIDIA GPU** (12GB+ VRAM) — GPU acceleration helps a lot

If your computer has 16GB of RAM or less, local models won't run well and you'll have a better experience with the cloud tools. No need to install anything — you won't be at any disadvantage in this course.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "conda not found" or "conda is not recognised" | Miniconda isn't installed or isn't in your PATH. Reinstall from [docs.anaconda.com/miniconda](https://docs.anaconda.com/miniconda/). On Windows, make sure to check "Add to PATH". On Mac, close and reopen Terminal after installing. |
| Setup script fails with "permission denied" | **Mac:** Make sure you're using `bash setup-mac.sh` (not `./setup-mac.sh`). **Windows:** Run the ExecutionPolicy command from Step 5. |
| VS Code doesn't show the PSYC4411 kernel | Close and reopen VS Code. If still missing, open a terminal and run: `conda run -n psyc4411 python -m ipykernel install --user --name=psyc4411 --display-name="PSYC4411"` |
| Packages fail to install (network error) | Check your internet connection. If on campus, try switching between WiFi and a personal hotspot. |
| "ModuleNotFoundError" when running the test notebook | You're using the wrong Python environment. Make sure to select the **PSYC4411** kernel in the top-right of the notebook. |
| `conda activate` says "Run 'conda init' first" | Run `conda init` in your terminal, then close and reopen the terminal. This is a one-time setup that teaches your shell how to activate environments. |
| Copilot says I don't have access | Your Student Developer Pack may still be processing. It can take a few days. Everything else will work without Copilot. |

**Tip:** If you hit an error during setup, try pasting the full error message into **Copilot Chat**, **ChatGPT**, or **Claude**. AI assistants are great at diagnosing installation errors, package conflicts, and environment problems. Just say something like: *"I'm trying to set up Python for a university course and I got this error:"* and paste the error.

**Still stuck?** Bring your laptop to the Week 2 class and we'll help you get sorted. You can also post a question in the iLearn discussion forum — chances are someone else hit the same issue.

---

*[Back to course overview](../README.md)*

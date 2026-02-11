# Getting Started — PSYC4411 Setup Guide

**Please complete these steps before Week 2.** The first part of the Week 2 class will be dedicated to troubleshooting any issues, so don't worry if you get stuck — bring your laptop and we'll sort it out together.

Everything you need for this course is **free**. This guide assumes you've never installed programming tools before, so we'll walk through every step.

Here's what you'll set up:

| Tool | What it does |
|------|-------------|
| **GitHub** | A platform for sharing code and collaborating (also gets you free AI tools) |
| **VS Code** | A text editor designed for writing and running code |
| **Python** | The programming language we'll use for data analysis |
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

When you open VS Code for the first time, you'll see a Welcome tab. Feel free to explore it, or close it — we'll set up the important bits in Step 5.

---

## Step 3: Install Python

Python is the programming language used throughout this course. You won't need to memorise Python syntax — you'll use AI assistants to help write code — but Python needs to be installed on your computer so the code can actually run.

### macOS

1. Go to [python.org/downloads](https://www.python.org/downloads/) and click the big yellow **Download Python 3.12.x** button (or whatever the latest 3.12+ version is)
2. Open the downloaded `.pkg` file and follow the installer prompts (click Continue, Agree, Install)
3. When the installer finishes, it may open a Finder window — you can close this

**Verify it worked:** Open **Terminal** (search for "Terminal" in Spotlight, or find it in Applications → Utilities) and type:

```
python3 --version
```

You should see something like `Python 3.12.8`. If you see an error, try closing and reopening Terminal, then try again.

### Windows

1. Go to [python.org/downloads](https://www.python.org/downloads/) and click the big yellow **Download Python 3.12.x** button
2. Run the downloaded installer
3. **This is the most important step:** At the very bottom of the first installer screen, you'll see a checkbox that says **"Add python.exe to PATH"** — **CHECK THIS BOX**. If you miss this, Python won't work from the command line and you'll need to reinstall.
4. Click **Install Now** and wait for it to finish

**Verify it worked:** Open **PowerShell** (search for "PowerShell" in the Start menu) and type:

```
python --version
```

You should see something like `Python 3.12.8`. If you get an error saying `python` is not recognised, you probably missed the "Add to PATH" checkbox — uninstall Python and reinstall, making sure to check that box.

---

## Step 4: Run the Setup Script

This is where the magic happens. We've written a script that automatically:
- Creates a **virtual environment** — think of this as a self-contained folder that keeps your course packages separate from everything else on your computer, so nothing gets mixed up
- Installs all the Python libraries you'll need (pandas for data, matplotlib for plotting, scikit-learn for machine learning, etc.)
- Registers everything with VS Code/Jupyter so it all works together

### macOS

1. Open **Terminal**
2. Navigate to the setup folder. If you saved the course repository to your Desktop, you'd type something like:
   ```
   cd ~/Desktop/Current-Advances-in-Psychological-Methods-and-Analyses-Repo/setup
   ```
   (Adjust the path to wherever you saved the course folder.)
3. Run the setup script:
   ```
   bash setup-mac.sh
   ```
4. Wait for it to finish. You'll see progress messages and, at the end, "Setup complete!"

### Windows

1. Open **PowerShell**
2. You may need to allow scripts to run (this is a one-time Windows security setting). Type:
   ```
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
   Press **Y** if asked to confirm.
3. Navigate to the setup folder. If you saved the course repository to your Desktop, you'd type something like:
   ```
   cd ~\Desktop\Current-Advances-in-Psychological-Methods-and-Analyses-Repo\setup
   ```
4. Run the setup script:
   ```
   .\setup-windows.ps1
   ```
5. Wait for it to finish. You'll see progress messages and, at the end, "Setup complete!"

### If Something Goes Wrong

- **"python not found"** — Python isn't installed or isn't in your PATH. Go back to Step 3.
- **"pip not found"** — This usually means the virtual environment didn't activate. Try closing your terminal, reopening it, and running the script again.
- **Installation hangs for a long time** — Some packages are large. Give it up to 10 minutes on a slow connection. If it's truly stuck, press `Ctrl + C` to cancel and try again.
- **Any other error** — Take a screenshot and bring it to class in Week 2. We'll figure it out together.

---

## Step 5: Install VS Code Extensions

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

**GitHub Copilot** will ask you to sign in with your GitHub account. If your Student Developer Pack hasn't been approved yet, Copilot won't activate — that's fine, come back to it later.

---

## Step 6: Test Your Setup

Let's make sure everything works together.

1. Open VS Code
2. Go to **File → Open Folder** and open the course repository folder (`Current-Advances-in-Psychological-Methods-and-Analyses-Repo`)
3. Navigate to `setup/test-setup.ipynb` in the file explorer on the left and click to open it
4. **Select the right kernel:** When the notebook opens, look at the top right corner of the notebook. You should see a kernel selector — click it and choose **PSYC4411** from the list. If you don't see it, try selecting "Python Environments" and look for `psyc4411-env`.
5. Click **Run All** (the double-play button at the top of the notebook) or run each cell one at a time with `Shift + Enter`
6. If you see library version numbers and a scatter plot, followed by "Setup complete!" — you're done!

**If the kernel doesn't appear:** Close VS Code completely, reopen it, and try again. Sometimes VS Code needs a restart to detect newly created environments.

---

## Step 7: Set Up Your AI Coding Assistants

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

- **GitHub Copilot Pro** (free via Student Developer Pack) — This is the big one for coding. Copilot works directly inside VS Code, suggesting code as you type and letting you ask questions via Copilot Chat. If you completed Step 1, you should have access.

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

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "python not found" or "python3 not found" | Python isn't installed or isn't in your PATH. Reinstall from [python.org](https://python.org) — on Windows, make sure to check "Add to PATH" |
| Setup script fails with "permission denied" | **Mac:** Make sure you're using `bash setup-mac.sh` (not `./setup-mac.sh`). **Windows:** Run the ExecutionPolicy command from Step 4. |
| VS Code doesn't show the PSYC4411 kernel | Close and reopen VS Code. If still missing, open a terminal in VS Code and run: `python -m ipykernel install --user --name=psyc4411 --display-name="PSYC4411"` |
| Packages fail to install (network error) | Check your internet connection. If on campus, try switching between WiFi and a personal hotspot. |
| "ModuleNotFoundError" when running the test notebook | You're using the wrong Python environment. Make sure to select the **PSYC4411** kernel in the top-right of the notebook. |
| Copilot says I don't have access | Your Student Developer Pack may still be processing. It can take a few days. Everything else will work without Copilot. |

**Still stuck?** Bring your laptop to the Week 2 class and we'll help you get sorted. You can also post a question in the iLearn discussion forum — chances are someone else hit the same issue.

---

*[Back to course overview](../README.md)*

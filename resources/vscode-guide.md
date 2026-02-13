# VS Code Guide for Beginners

Visual Studio Code (VS Code) is the code editor we use in this course. It's free, powerful, and where you'll write code, run notebooks, and use AI assistants. This guide covers the essentials.

---

## What Is VS Code?

VS Code is a text editor designed for working with code. Think of it as Microsoft Word, but for code — it understands programming languages, highlights syntax in colour, catches errors, and integrates with tools like Jupyter notebooks and GitHub Copilot.

**Download:** <a href="https://code.visualstudio.com" target="_blank">code.visualstudio.com</a> (free, available for Mac, Windows, and Linux)

---

## The Interface

When you open VS Code, you'll see several areas:

| Area | Where | What it does |
|------|-------|--------------|
| **Activity Bar** | Far left (vertical icons) | Switch between file explorer, search, extensions, etc. |
| **Side Bar** | Left panel | Shows files, search results, or extensions (depending on what you clicked) |
| **Editor** | Centre | Where you view and edit files |
| **Terminal** | Bottom panel | A command-line terminal built into VS Code |
| **Status Bar** | Very bottom | Shows the current Python environment, line number, etc. |

### Opening a folder

Always **open a folder**, not individual files. This gives VS Code the full context of your project.

1. File → Open Folder (or Cmd+O on Mac)
2. Navigate to the course repo folder
3. Click Open

You'll see all the course files in the Side Bar.

---

## Essential Extensions

Extensions add features to VS Code. Install these for this course:

| Extension | What it does | How to install |
|-----------|--------------|----------------|
| **Python** (Microsoft) | Python language support, debugging, linting | Search "Python" in Extensions |
| **Jupyter** (Microsoft) | Run Jupyter notebooks inside VS Code | Search "Jupyter" in Extensions |
| **GitHub Copilot** | AI code completion and chat | Search "GitHub Copilot" in Extensions |

**To install an extension:**
1. Click the Extensions icon in the Activity Bar (or Cmd+Shift+X)
2. Search for the extension name
3. Click **Install**

---

## Using the Terminal

The terminal is a text-based way to interact with your computer. You'll use it to run setup scripts and occasionally to manage Python packages.

**To open the terminal:** View → Terminal (or Ctrl+` — that's the backtick key, usually below Escape)

The terminal opens at the bottom of the VS Code window. You can type commands here just like in the macOS Terminal or Windows PowerShell.

**Common commands you might use:**

```
python --version          # Check which Python version is installed
pip install pandas        # Install a Python package
python my_script.py       # Run a Python file
```

---

## Working with Jupyter Notebooks

Jupyter notebooks (`.ipynb` files) are the main format for lab challenges in this course. VS Code has excellent built-in support.

**To open a notebook:** Click any `.ipynb` file in the Side Bar.

**Key things to know:**

- **Cells:** Notebooks are made up of cells — either code (Python) or Markdown (text). Click a cell to select it.
- **Running a cell:** Click the play button (▶) next to a cell, or press Shift+Enter
- **Kernel:** The "engine" that runs your code. Make sure it's set to the **PSYC4411** kernel (check the top-right corner of the notebook)
- **Adding a cell:** Hover between cells and click the **+ Code** or **+ Markdown** button
- **Restarting the kernel:** If things get stuck, click the "Restart" button in the toolbar — this clears all variables and lets you start fresh

See the [Jupyter Notebooks guide](jupyter-guide.md) for more detail.

---

## Selecting the Right Python Environment

After running the setup script, you'll have a Python environment called `psyc4411-env` with all the course packages installed.

**To select it in VS Code:**

1. Open any `.py` or `.ipynb` file
2. Look at the bottom-right of the Status Bar — it shows the current Python interpreter
3. Click it and select `psyc4411-env` from the list
4. For notebooks, you can also select the kernel from the top-right corner (look for **PSYC4411**)

If `psyc4411-env` doesn't appear, you may need to rerun the setup script — see the [Getting Started guide](../setup/getting-started.md).

---

## Using GitHub Copilot in VS Code

Once you've installed the GitHub Copilot extension and signed in:

### Inline Completions

As you type code, Copilot suggests completions in grey text. Press **Tab** to accept a suggestion, or keep typing to ignore it.

### Copilot Chat

Click the Copilot icon in the Activity Bar (or press Cmd+Shift+I) to open Copilot Chat. You can ask questions like:

- "What does this code do?"
- "I'm getting a KeyError — here's my code. What's wrong?"
- "Write a scatter plot of Depression vs Sleep using seaborn"

Copilot Chat can see your open files, which means it already has context about your code.

---

## Useful Keyboard Shortcuts

| Action | Mac | Windows |
|--------|-----|---------|
| Open Command Palette | Cmd+Shift+P | Ctrl+Shift+P |
| Open terminal | Ctrl+` | Ctrl+` |
| Run cell in notebook | Shift+Enter | Shift+Enter |
| Save file | Cmd+S | Ctrl+S |
| Open file search | Cmd+P | Ctrl+P |
| Toggle sidebar | Cmd+B | Ctrl+B |
| Open extensions | Cmd+Shift+X | Ctrl+Shift+X |

---

## Troubleshooting

**"No Python interpreter selected"** — Click the Python version in the Status Bar and select `psyc4411-env`.

**Terminal says "command not found: python"** — Try `python3` instead of `python`. On some systems, Python 3 is only available as `python3`.

**Copilot not suggesting anything** — Make sure you're signed in (check the Copilot icon in the Status Bar). Also check that your Student Developer Pack has been approved.

**Notebook cells won't run** — Check that the kernel is set to PSYC4411 (top-right of the notebook). If it says "No Kernel", click and select the PSYC4411 kernel.

---

*[Back to resources](README.md) · [Back to course overview](../README.md)*

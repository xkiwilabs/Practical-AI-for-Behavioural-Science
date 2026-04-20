# GitHub Guide for Beginners

GitHub is where the course materials live and where you'll access weekly readings, challenge briefs, starter notebooks, and datasets. This guide covers what you need to know.

---

## What Is GitHub?

GitHub is a website for storing, sharing, and collaborating on code and documents. Think of it as Google Drive for code: files are stored online, anyone with access can view them, and changes are tracked over time.

A **repository** (or "repo") is like a project folder. The PSYC4411 course repo contains all your weekly materials, organised into folders.

You don't need to learn the command-line tool `git` for this course. Everything you need can be done through the GitHub website and VS Code.

---

## Creating Your Account

1. Go to <a href="https://github.com" target="_blank">github.com</a>
2. Click **Sign up**
3. **Use your personal email** (not your MQ email). Your MQ email will expire after graduation, but your GitHub account will stay with you for your career
4. Choose a professional username, something like `jsmith-psych` rather than `party_animal_99`
5. Complete the signup process

---

## GitHub Student Developer Pack

The <a href="https://education.github.com/pack" target="_blank">Student Developer Pack</a> gives you free access to GitHub Copilot Pro and other developer tools.

**How to apply:**

1. Go to <a href="https://education.github.com/pack" target="_blank">education.github.com/pack</a>
2. Click **Sign up for Student Developer Pack**
3. Verify your student status using your **@students.mq.edu.au** email (you can add this as a secondary email to your GitHub account)
4. You may need to upload a photo of your student ID
5. Approval usually takes a few days

Once approved, you'll have free access to GitHub Copilot Pro — the AI coding assistant you'll use throughout this course.

> **MQ student ID rejected?** GitHub sometimes rejects Macquarie University IDs because they don't show an expiry date. If this happens to you, see the **[Student Verification guide](github-student-verification.md)** for how to fix it with a supporting enrolment letter.

---

## Navigating the Course Repository

The course repo is at: **xkiwilabs/Practical-AI-for-Behavioural-Science**

### Key areas

| Folder | What's inside |
|--------|---------------|
| `weeks/week-01-lecture/` | Week 1 companion reading, readings list, slides |
| `weeks/week-02-lab/` | Week 2 challenge brief, starter notebook, dataset |
| `setup/` | Getting started guide, setup scripts |
| `assessments/` | Assessment details: presentation, written assignment, viva |
| `resources/` | This folder — guides and references |

### Reading files on GitHub

- Click any `.md` file to see it rendered with formatting (headings, bold, links, etc.)
- Click any `.ipynb` file to see a preview of the Jupyter notebook
- Click any `.csv` file to see a table preview of the data
- Use the breadcrumb navigation at the top to move between folders

### Downloading files

**Individual files:**
1. Navigate to the file
2. Click the **Download raw file** button (down-arrow icon)

**The entire repo:**
1. Click the green **Code** button on the repo's main page
2. Select **Download ZIP**
3. Extract the ZIP file on your computer

**Using VS Code (recommended):**
1. Open VS Code
2. Open the Command Palette (Cmd+Shift+P on Mac, Ctrl+Shift+P on Windows)
3. Type "Git: Clone" and press Enter
4. Paste the repo URL and choose where to save it

---

## Key Concepts

- **Repository (repo):** A project folder on GitHub containing files, folders, and their history
- **Branch:** A parallel version of the repo. We use `main` for student-facing content. You won't need to create branches.
- **Commit:** A saved snapshot of changes. Each commit has a message describing what changed.
- **README.md:** The main information file in any folder. GitHub automatically displays it when you open a folder.
- **Fork:** Your own copy of someone else's repo. Optional for this course (see below).

---

## Forking (Optional): Save Your Work to Your Own Repository

You **don't need to fork** for this course — you can just download files. But if you want to keep your work backed up on GitHub, forking is the way to do it.

**A fork is:** A complete copy of the course repo under your own GitHub account. You can edit it, push your changes, and it stays separate from the original course repo (so you can't accidentally overwrite the instructor's files, and vice versa).

### When to fork

- You want to save your lab work, presentations, and analysis code to GitHub (cloud backup)
- You plan to revisit this code after the course
- You want a Git-tracked history of your changes
- You're using **Codespaces and want to push your work** somewhere

### How to fork

1. Go to [github.com/xkiwilabs/Practical-AI-for-Behavioural-Science](https://github.com/xkiwilabs/Practical-AI-for-Behavioural-Science)
2. Click the **Fork** button (top-right, next to "Star")
3. GitHub asks where you want to fork it → select your own account
4. You now have your own copy at `github.com/your-username/Practical-AI-for-Behavioural-Science`

### Cloning your fork (in VS Code or Codespaces)

1. Go to your fork (github.com/your-username/...)
2. Click the green **Code** button
3. Copy the HTTPS URL
4. In VS Code/Codespaces: **Command Palette** (Cmd+Shift+P or Ctrl+Shift+P) → **Git: Clone** → paste the URL

Now you have a local copy you can edit and push back to your fork.

### Keeping your fork up to date with course materials

When I add new course materials each week, you want to pull them into your fork:

1. In the terminal, set the upstream (do this once):
   ```
   git remote add upstream https://github.com/xkiwilabs/Practical-AI-for-Behavioural-Science.git
   ```

2. Each week, fetch updates:
   ```
   git fetch upstream
   git merge upstream/main
   ```

3. Push to your fork:
   ```
   git push
   ```

Now your fork has the latest course materials **plus** your own work.

### Example workflow (Codespaces + Forking)

1. **Week 1:** Create fork, clone it to Codespaces
2. **Week 2:** `git pull` to get Week 2 materials, complete lab, save work
3. **Week 3:** `git push origin main` to back up your work, `git fetch upstream && git merge upstream/main` to get Week 3 materials
4. **End of course:** All your weekly work is saved in your fork

---

## Tips

- **Bookmark the course repo** in your browser for quick access
- **Check the repo before each class** for updated materials
- You don't need to learn git commands — browsing and downloading from the website is sufficient
- If you want to learn git (optional but useful), GitHub has an excellent <a href="https://docs.github.com/en/get-started/start-your-journey/hello-world" target="_blank">Hello World tutorial</a>

---

*[Back to resources](README.md) · [Back to course overview](../README.md)*

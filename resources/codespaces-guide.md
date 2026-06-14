# GitHub Codespaces Guide

**TL;DR:** Click Code → Codespaces → Create codespace. Wait 2 minutes. Code in VS Code in your browser. Free, nothing to install.

---

## What Is GitHub Codespaces?

GitHub Codespaces is **VS Code running in your browser on GitHub's servers**. Instead of installing Python, Git, and packages on your laptop, everything runs remotely. You get:

- ✅ **No installation needed** — just click a button
- ✅ **Identical to local VS Code** — same interface, same shortcuts, same extensions
- ✅ **Jupyter notebooks work perfectly** — all built-in
- ✅ **GitHub Copilot ready** — if you have Student Developer Pack
- ✅ **Auto-saves to GitHub** — your work is backed up
- ✅ **Free for this course** — 120 core-hours/month (we use ~2–4 hours/week)

**When to use Codespaces:**
- You couldn't install Python/VS Code on your laptop
- You don't have a powerful laptop
- You're using a school computer or borrowed device
- You're travelling and want to keep coding
- You're just testing before committing to local installation

---

## Getting Started: 3 Steps

### Step 1: Open the Codespaces menu

Go to [github.com/xkiwilabs/Practical-AI-for-Behavioural-Science](https://github.com/xkiwilabs/Practical-AI-for-Behavioural-Science)

Click the green **Code** button (top-right of the page).

![code button location]

### Step 2: Click Codespaces

You'll see three tabs: **Local**, **HTTPS**, **SSH**, and **Codespaces**. Click the **Codespaces** tab.

Then click **Create codespace on main**.

![codespaces tab]

### Step 3: Wait for the environment to build

GitHub is setting up a container with Python, conda, and all your course packages. This takes 2–3 minutes the first time. You'll see progress messages:

```
Building dev container...
Installing packages...
Setting up ai-behsci environment...
Opening in VS Code...
```

**What's happening behind the scenes?** The repo contains a `.devcontainer/devcontainer.json` file that tells GitHub exactly what to install and configure. You don't need to do anything; GitHub detects it automatically and uses it to set up your environment. It's like a recipe that says "install Python 3.12, create the ai-behsci conda environment, add these VS Code extensions," etc. All automatic.

When it's done, **VS Code opens in your browser**. You're ready to go.

---

## Choosing Machine Type (CPU Power)

**TL;DR: Do nothing. GitHub pre-selects 2-core, which is FREE and powerful enough. Don't change it.**

When you click **Create codespace**, GitHub shows a **Machine type** dropdown. Here's what your options are:

| Machine | Cores | Cost | Good for? |
|---------|-------|------|-----------|
| **2-core** (DEFAULT) | 2 CPUs | **FREE** ✅ | ✅ This course. Sufficient for all labs. |
| **4-core** | 4 CPUs | ~$0.18/hour extra | Faster execution (costs money — not recommended) |
| **8-core+** | 8+ CPUs | $$$ | Not needed. Skip. |

### Just leave it on 2-core

**Important:** The default machine type is **2-core**, and it's completely free for this course. You don't need to select anything. Just click "Create codespace" and move on.

If you see the Machine type dropdown, **leave it set to 2-core**. Don't pick 4-core or 8-core unless you want to pay extra.

### Does 2-core have enough power?

Yes. Absolutely. It handles:
- Loading and processing datasets (~3,000 rows)
- Training scikit-learn models (regression, classification, clustering, neural networks)
- Creating plots and visualisations
- Running all course labs without issues

### What if I accidentally pick 4-core and get charged?

Don't panic. Here's how to switch back to free 2-core:

1. Stop your codespace (Code → Codespaces → ⋯ → Stop codespace)
2. Click ⋯ → **Change machine type**
3. Select **2-core**
4. Resume

You'll only be paying for the time you *actually used* the 4-core machine (charged at ~$0.18/hour). But after you switch back to 2-core, future usage is free again.

### GPU?

Codespaces doesn't offer GPU in the free tier. For this course, you don't need it: CPU is plenty for the work we're doing. (GPU matters for massive image/video processing or training giant models, not for psychology datasets.)

---

## What You'll See

When Codespaces opens, you'll see VS Code exactly as it appears on your computer:

| Part | What it is |
|------|-----------|
| **Left sidebar** | File explorer — click to open course materials |
| **Centre** | Editor — where you write code and read notebooks |
| **Bottom panel** | Terminal — run commands (usually not needed) |
| **Top bar** | Tabs for open files, search, extensions, etc. |

**Jupyter kernel:** A dropdown in the top-right corner shows the Python environment. It should say **ai-behsci**. If not, click it and select **ai-behsci** from the list.

---

## Using Notebooks, Code, and the Terminal

Everything works the same as local VS Code:

### Opening and running notebooks

1. Click any `.ipynb` file in the sidebar
2. Make sure the kernel (top-right) is set to **ai-behsci**
3. Click the **play ▶ button** next to a cell to run it

### Running Python scripts

1. Right-click a `.py` file → **Run Python File**
2. Or open the terminal (View → Terminal) and type `python file_name.py`

### Running setup/test scripts

In the terminal:
```
cd setup
python test-setup.py
```

---

## Cost Management: Spending Limits & Usage Tracking

### Set Your Spending Limit to $0 (Recommended)

This prevents accidental charges if you accidentally leave a codespace running.

1. Go to [github.com](https://github.com) → your **profile photo** (top-right) → **Settings**
2. Click **Billing and plans** in the left sidebar
3. Click **Spending limits**
4. Set the limit to **$0**

Now, if you ever approach your 120-hour free limit, GitHub will **warn you** instead of charging your card. You won't be blindsided.

### Track Your Usage

Check how many hours you've used anytime:

1. Go to [github.com](https://github.com) → your **profile photo** → **Settings** → **Billing and plans**
2. Click **Codespaces** in the left sidebar
3. You'll see:
   - **Hours used this month**
   - **List of all your codespaces** (and how long each has run)
   - **Storage used**

**Expected usage for this course:** ~0.5–1 hour per lab week = ~13 hours over the entire semester. Well under 120.

### Close Your Codespace When Done (Saves Hours)

**Important:** Leaving your codespace running (even if you're not actively coding) burns through your free hours.

**When you're done for the day:**

1. Close your browser tab with Codespaces
2. Go back to the repo on GitHub
3. Click Code → **Codespaces**
4. You'll see your codespace listed. Click the **⋯** menu → **Stop codespace**

This **pauses** the codespace. You can resume it anytime, and it picks up where you left off. Stopped codespaces don't burn hours.

**How long before GitHub auto-stops?** GitHub auto-stops idle codespaces after 30 minutes of inactivity. But don't rely on this. Manually stop when you're done.

---

## Key Differences from Local VS Code

### Saving and backups

- **Auto-saves every few seconds** — no need to press Ctrl+S (though you can)
- **Changes are synced to GitHub** — even if your browser closes, work is saved
- **No local files on your computer** — you only have the remote version

### Closing and returning

- **Stop the codespace when you're done** (see section above — saves free hours!)
- **Return to it later** — go back to the repo → Code → Codespaces → select your existing codespace from the list
- **Delete it** — if you're completely done, right-click the codespace under Code → Codespaces and click "Delete"

**Tip:** You only need **one codespace** for this course. Create it once, and reuse it all semester. Just stop it when you're not using it, and resume when you need it again.

---

## Pulling Course Updates Each Week

When I add new materials to the course repository, you can fetch them into your codespace:

1. Open the terminal in your codespace (View → Terminal)
2. Type: `git pull`
3. Any new files download automatically

You don't need to create a new codespace. Just pull the updates into your existing one. This keeps everything synced.

---

## Downloading and Sharing Your Work

All files you create in Codespaces are saved to GitHub automatically. Here's how to download them or view them locally.

### Download files you create

To download any file or folder (like your HTML slides or figures):

1. In the Codespaces file explorer, **right-click the file** (e.g., `my_presentation.html` or `plot.png`)
2. Select **Download**
3. The file appears in your Downloads folder

**Or from GitHub directly:**
1. Go to the repository on GitHub
2. Navigate to your file
3. Click **Download** (the arrow icon at the top-right of the file view)

### View HTML slides in a browser

If you created an HTML presentation (e.g., `presentation.html`):

**Option A: View in Codespaces (built-in preview)**
1. Right-click the `.html` file in the explorer
2. Select **Open with Live Server**
3. A preview window opens to the right. Click the link to pop out in a full browser tab

**Option B: Download and open locally**
1. Right-click the `.html` file → **Download**
2. Open the file from your Downloads folder (double-click it)
3. It opens in your default browser

Both methods work. Option A is faster if you're just checking; Option B is better if you want to save it permanently.

### Figures, plots, and outputs

Anything you generate (PNG, PDF, CSV files, etc.) is saved in Codespaces. Download them the same way as HTML:

1. Right-click the file → **Download**
2. It goes to your Downloads folder

### What about pushing to the course repository?

**You can't push directly to the main course repo.** Only the instructor and official collaborators can do that. This prevents accidental overwrites.

**If you want to save your work permanently:**
- **Option 1:** Keep it in your Codespaces (auto-backed up to GitHub)
- **Option 2:** Create your own fork of the repo and push there (see [GitHub guide](github-guide.md) for forking instructions)
- **Option 3:** Just download the files to your computer

For most students, just downloading files at the end of each lab is easiest.

---

## Using AI Coding Assistants in Codespaces

**Important:** You don't need Student Developer Pack to use Codespaces. But Copilot (GitHub's AI assistant) requires it. If you don't have Student Developer Pack approval yet, see the alternatives below.

### If you have GitHub Student Developer Pack

Copilot is already active in VS Code. You can:

**Open Copilot Chat:**
Press **Ctrl+Shift+I** (Windows) or **Cmd+Shift+I** (Mac). A chat panel opens on the right.

**Ask Copilot for help:**
```
@workspace Write Python code to load the lifestyle_mental_health.csv 
file and create a scatter plot of sleep vs depression
```

Copilot reads your files, understands your data, and generates code. Select and paste it into your notebook or script.

**Inline suggestions:** As you type code, Copilot suggests completions (greyed-out text). Press **Tab** to accept.

**More:** See the [Copilot guide](copilot-guide.md) for detailed prompt engineering tips.

### If you don't have Student Developer Pack yet (or it was rejected)

You can still use free AI assistants in Codespaces. Just install them from the VS Code extensions marketplace:

**1. Gemini Code Assist** (free tier — recommended)
   - In Codespaces, click **Extensions** (Ctrl+Shift+X)
   - Search for **"Gemini Code Assist"** (by Google)
   - Click **Install**
   - Sign in with your **Gmail account** (free — no payment needed)
   - Use it exactly like Copilot: press **Ctrl+Shift+I** for chat, or it suggests code as you type

**2. OpenAI Codex or Claude Code** (check free tier limits)
   - Same process: Extensions → Search → Install → Sign in
   - Some offer free usage limits, others are paid
   - See the [AI Tools guide](ai-tools-guide.md) for which ones have free tiers

**3. Browser-based AI** (no installation needed)
   - Open ChatGPT, Claude, or Gemini in a separate browser tab
   - Code in Codespaces on the left, chat with AI on the right
   - Copy code back and forth

**Does this work in Codespaces?** Yes. Codespaces is VS Code, so all the same extensions work. You install them in your Codespaces environment just as you would locally, and they sync to your account.

**Bottom line:** Codespaces works great without Copilot. You'll just use a different (free) AI tool. The 120 free core-hours per month are still yours.

---

## Troubleshooting

### "Python environment not found"

If you see this error, the conda environment didn't build. Try restarting:

1. Open the terminal (View → Terminal)
2. Type: `conda activate ai-behsci`
3. If that fails, type: `conda env create -f setup/environment.yml`

### Jupyter kernel shows "Python 3.xx" instead of "ai-behsci"

Click the kernel dropdown, then click **Select Another Kernel** → **ai-behsci**.

### Notebook cell won't run / takes forever

- Click the kernel dropdown and select **ai-behsci**
- Try restarting the kernel: press Ctrl+Shift+P, search "Restart Kernel"

### "I ran out of storage" message

Codespaces includes 15GB. If you're getting close, delete old notebooks or data files you don't need. Right-click in the sidebar → Delete.

### Need to pull the latest course materials

Open the terminal and type:
```
git pull
```

This fetches any new files added to the course repo since you created your codespace.

---

## Cost: When Do I Start Paying?

### Free tier (you have this)

- **120 core-hours per month** — 1 codespace running for 120 hours, or 2 codespaces for 60 hours each
- **15GB storage** — enough for all course materials
- **No credit card required** — free tier doesn't upgrade automatically

### Does this course use up my free tier?

**No.** This course needs roughly:
- 13 weeks × 3 hours/week = **39 core-hours**
- Plus ~1GB storage

You stay **well under** 120 hours. Even with other classes, you're unlikely to hit the limit.

### Billing

[GitHub's pricing page](https://github.com/features/codespaces/pricing) explains the full details. Key points:
- **Free tier:** 120 core-hours/month + 15GB storage (no payment)
- **Paid (if you exceed):** $0.18 per core-hour + $0.07 per GB/month extra storage
- **You control it:** Can manually stop codespaces to save hours

**Bottom line:** It's free. Don't worry about cost.

---

## Advanced: Working with Git in Codespaces

If you've forked the course repo or are committing work:

### Push changes to GitHub

```
git add .
git commit -m "Your message here"
git push
```

### Pull updates from the course repo

```
git pull
```

This happens automatically each week when we add new materials.

**More:** See the [GitHub guide](github-guide.md) for details on cloning, forking, and pushing.

---

## When to Go Back to Local Setup

Codespaces is great for "I need this to work right now." But for the long term, consider local setup if:

- You want faster performance (browser adds slight latency)
- You prefer working offline
- You're doing heavy data processing (Codespaces compute is modest)
- You want full control of your environment

**You can switch anytime.** Just follow the [setup guide](../setup/getting-started.md) and install locally. All your work stays on GitHub.

---

## Questions?

See the [troubleshooting](../setup/getting-started.md#troubleshooting) section in the main setup guide, or ask in class.

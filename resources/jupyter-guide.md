# Jupyter Notebooks Guide

Jupyter notebooks are interactive documents that combine code, text, and visualisations. They're the main format for lab challenges in this course. This guide covers what you need to know.

---

## What Is a Jupyter Notebook?

A Jupyter notebook (`.ipynb` file) is a document made up of **cells**. Each cell is either:

- **Code cell** — contains Python code that you can run
- **Markdown cell** — contains formatted text (headings, bold, lists, etc.)

You run cells one at a time, and the output appears directly below the cell. This makes notebooks great for data analysis — you can write code, see the results, and add notes as you go.

The name "Jupyter" comes from the three programming languages it originally supported: **Ju**lia, **Py**thon, and **R**. We'll use Python.

---

## Opening a Notebook

In VS Code, click any `.ipynb` file in the file explorer. The notebook opens in the editor area with cells displayed vertically.

Make sure the kernel is set to **PSYC4411** — check the top-right corner of the notebook. If it shows something else, click it and select PSYC4411 from the list.

---

## Working with Cells

### Running a cell

Click the **play button** (▶) next to a cell, or press **Shift+Enter** (runs the cell and moves to the next one).

When a code cell runs, you'll see a number appear in square brackets to the left, like `[1]`. This tells you the order in which cells were run — more on why this matters below.

### Adding a new cell

Hover between two cells — you'll see **+ Code** and **+ Markdown** buttons appear. Click the one you want.

### Deleting a cell

Select the cell, then press the **trash can** icon in the cell toolbar, or right-click and choose "Delete Cell".

### Moving cells

Click and drag cells up or down to reorder them, or use the up/down arrows in the cell toolbar.

---

## Execution Order Matters

This is the most common source of confusion with notebooks. Cells can be run in any order, and **the order you run them matters**.

Here's an example of how this can go wrong:

```python
# Cell 1
x = 10

# Cell 2
y = x + 5
print(y)  # Output: 15

# Cell 3
x = 100
```

If you run the cells in order (1, 2, 3), cell 2 prints `15`. But if you then run cell 2 again, it prints `105` — because `x` was changed to `100` in cell 3.

### The rule

The notebook's state (which variables exist and what their values are) depends on **which cells you've run and in what order**, not on the order the cells appear in the document.

### How to avoid confusion

- **Run cells from top to bottom** whenever possible
- If things seem wrong, **restart the kernel** (clears all variables) and run all cells from the top
- Look at the numbers in square brackets `[1]`, `[2]`, `[3]` — if they're not sequential, you may have run cells out of order
- The number `[*]` means the cell is currently running

---

## The Kernel

The **kernel** is the "engine" that runs your Python code. Think of it as a separate Python session running in the background.

### Key things about the kernel

- All your variables, imported libraries, and data live in the kernel's memory
- When you restart the kernel, **everything is erased** — all variables, all data, all imports
- After restarting, you need to rerun cells from the top (starting with the import cells)

### When to restart

- When things behave unexpectedly (especially if you ran cells out of order)
- When the notebook feels "stuck" (a cell has been running for too long)
- When you want to verify that your notebook runs cleanly from top to bottom

### How to restart

In VS Code, use the **Restart** button in the notebook toolbar (circular arrow icon). You can choose:

- **Restart** — Clears the kernel but keeps cell outputs visible
- **Restart and Run All** — Clears the kernel and reruns every cell from the top

---

## Saving Your Work

- **Auto-save:** VS Code auto-saves files by default. Your notebook is saved as you work.
- **Manual save:** Cmd+S (Mac) or Ctrl+S (Windows)
- **Cell outputs are saved** with the notebook — so if you save and close, your plots and results are still there when you reopen

---

## Markdown Cells

Markdown cells let you add formatted text to your notebooks. Double-click a markdown cell to edit it, then run it (Shift+Enter) to see the formatted version.

See the [Markdown guide](markdown-guide.md) for formatting syntax.

Common uses in notebooks:
- Section headings (using `#`, `##`, `###`)
- Explanations of what your code does
- Notes about your findings
- Documentation of your analysis decisions

---

## Common Mistakes and Fixes

### "NameError: name 'pd' is not defined"

You tried to use pandas before running the import cell. Run the cell that contains `import pandas as pd` first.

### "FileNotFoundError: No such file or directory"

The file path is wrong. Common causes:
- You're running the notebook from a different folder than expected
- The file name has a typo
- The file hasn't been downloaded yet

### A cell runs forever (shows `[*]` and never finishes)

- Try clicking the **Stop** button (square icon) next to the cell
- If that doesn't work, restart the kernel
- Common cause: an infinite loop in your code

### Plots don't appear

Make sure you have `import matplotlib.pyplot as plt` in your imports, and that you're calling `plt.show()` at the end of your plotting code (though in notebooks, plots usually display automatically).

### "ModuleNotFoundError: No module named 'seaborn'"

The package isn't installed in your current environment. Make sure you're using the PSYC4411 kernel (check the top-right corner of the notebook). If the package is still missing, open the terminal and run:

```
pip install seaborn
```

---

## Tips

- **Run all cells from top to bottom** before submitting or presenting your work — this catches any hidden dependencies on out-of-order execution
- **Add markdown cells** above your code cells explaining what the code does and why — this helps your future self (and your group members)
- **Don't be afraid to restart** the kernel — it's like turning it off and on again. You won't lose your code, just the current variable values.
- **Save often** — especially before running experimental code that might crash the kernel

---

*[Back to resources](README.md) · [Back to course overview](../README.md)*

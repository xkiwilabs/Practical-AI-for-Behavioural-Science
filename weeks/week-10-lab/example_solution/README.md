# Week 10 Example Solution

This is a worked example of how the Week 10 challenge could be completed. There are many valid approaches; this is not the only correct one.

## Folder Contents

| File | Description |
|------|-------------|
| `README.md` | This file |
| `plan.md` | Initial analysis plan (created before coding) |
| `plan_final.md` | What actually happened (updated after coding) |
| `example_solution.ipynb` | Full worked notebook with outputs |
| `explore_eeg.py` | Script 1: Data loading and exploration |
| `train_classifier.py` | Script 2: Full classification pipeline |
| `slide.html` | Example presentation slide (open in browser) |
| `css/mq-theme.css` | Slide styling |
| `images/` | Generated plots (6 PNGs) |

## Key Results

| Model | Accuracy | F1 |
|-------|----------|-----|
| Logistic Regression | 60.2% | 0.583 |
| Simple MLP (1 hidden) | 60.1% | 0.570 |

**Bottom line:** The neural network did not beat logistic regression on this data. This is a common outcome when working with pre-extracted tabular features and a weak signal. The added complexity of PyTorch was not justified for this particular problem.

## How to Run

```bash
conda activate ai-behsci

# Download the data first (if not already done)
cd weeks/week-10-lab/data
python download_data.py
cd ..

# Run the exploration script
python example_solution/explore_eeg.py

# Run the full classification pipeline
python example_solution/train_classifier.py

# View the presentation slide
open example_solution/slide.html
```

## Note

This is an example to show what a completed challenge looks like. Your group's work will differ: different code structure, different debugging stories, different reflections. That's expected and encouraged.

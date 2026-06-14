# Week 10 Challenge Lab: Beat the Baseline — Neural Network Training & Diagnostics

> **Group Challenge:** Build a neural network to classify imagined hand movements from EEG brain signals. Compare it to a logistic regression baseline. Diagnose training issues. And honestly assess: was the added complexity worth it?

---

## The Challenge

Your task is to **read minds**, or at least try. You have EEG recordings from 109 people who imagined moving their left or right hand. A machine extracted features from their brain waves. Your job: build a classifier that can tell left from right.

This challenge has three phases:

**Phase 1 — Baseline:** Build a logistic regression classifier using scikit-learn (you already know how to do this). This is your reference point.

**Phase 2 — Neural Network:** Build and train a simple MLP (multi-layer perceptron) in PyTorch. Track the training loss. Diagnose any problems.

**Phase 3 — Honest Comparison:** Compare your neural network to the baseline. Is it better? Is the added complexity (more code, harder debugging, longer training) justified?

You need to:
1. **Fit a logistic regression baseline** — report accuracy and F1
2. **Build a simple MLP in PyTorch** — 1 hidden layer, 64 units, ReLU, dropout
3. **Train the MLP** and track loss curves — plot training and validation loss per epoch
4. **Diagnose training issues** — is the network learning? Overfitting? Stuck at chance?
5. **Compare fairly** — use the same train/test split for both models
6. **Was it worth it?** — honestly evaluate whether the neural network justified its added complexity

---

## Background

Every model you've built so far (linear regression, logistic regression, decision trees, random forests) worked with hand-crafted features. Neural networks are different: they can learn their own internal representations. But with great flexibility comes great risk: they need more data, overfit more easily, and when they fail, they fail silently (no traceback, just a flat loss curve).

The EEG motor imagery task is a genuine challenge used in brain-computer interface (BCI) research. People with paralysis could use systems like this to control prosthetic limbs or communicate through thought alone. The signal is weak, so don't expect 95% accuracy. In BCI research, 60–70% accuracy on a binary task is a meaningful result.

**New LLM Skill: Complex Debugging.** In Week 2 you learned prompting, in Week 4 debugging, in Week 6 refactoring, in Week 8 documentation. This week's skill is **complex debugging** — diagnosing problems when there's no error message, just a model that silently fails. When your neural network's loss stays flat at 0.693 (the loss for random guessing on two classes), there's no traceback to share with your AI. You need to describe the *symptoms*: what the loss curve looks like, what you expected, what the data looks like. This is the hardest debugging skill yet, and the most valuable for real-world machine learning work.

---

## Use Whatever AI Tools You Like

VS Code Copilot, ChatGPT, Claude, Gemini: use any combination. Mix and match. There are no restrictions on which AI tools you use in this course.

---

## The Dataset

**PhysioNet EEG Motor Movement/Imagery Dataset (pre-extracted features)**
- **Source:** [PhysioNet EEGBCI](https://physionet.org/content/eegmmidb/1.0.0/)
- **Citation:** Schalk et al. (2004)
- **Size:** 4,918 trials from 109 participants, 324 columns
- **Format:** CSV (comma-separated)

Download the data:
```
conda activate ai-behsci
cd weeks/week-10-lab/data
python download_data.py
```

### What's in the data?

Each row is one **trial**: a 2-second window of brain activity while someone imagined moving their left or right hand.

| Column Group | Columns | Description |
|---|---|---|
| **Metadata** | `participant_id`, `trial`, `condition`, `condition_code` | Who, which trial, left/right label (0/1) |
| **EEG features** | 320 columns | 64 channels × 5 frequency bands |

### The 320 features

Each EEG channel has 5 features, representing the average power in each frequency band:

| Band | Frequency | What it reflects |
|---|---|---|
| **Delta** | 1–4 Hz | Deep sleep, unconscious processes |
| **Theta** | 4–8 Hz | Drowsiness, memory encoding |
| **Alpha** | 8–13 Hz | Relaxed wakefulness, sensory processing |
| **Beta** | 13–30 Hz | Active thinking, motor planning |
| **Gamma** | 30–45 Hz | Higher cognitive processes, attention |

Feature column names follow the pattern `ChannelName_band` (e.g., `C3_alpha`, `C4_beta`). The most important channels for motor imagery are **C3** (left motor cortex → right hand) and **C4** (right motor cortex → left hand).

### Key facts
- **4,918 trials** from 109 participants (~45 trials each)
- **Balanced classes:** 2,480 left (50.4%) / 2,438 right (49.6%)
- **Expected baseline accuracy:** ~60% (logistic regression)
- **This is genuinely hard** — chance is 50%, and 60% is a meaningful result in BCI research

---

## Getting Started

1. **Download the data:**
   ```
   conda activate ai-behsci
   cd weeks/week-10-lab/data
   python download_data.py
   ```

2. **Open the starter files:** `starter.ipynb` (notebook) or `starter.py` (script)
   - Cells 1–5 are fully functional; they load, explore, and prepare the data
   - Cells 6+ are scaffolded; your AI helps you fill them in

3. **Have your AI create a plan first** — before writing any PyTorch code

4. **Phase 1:** Logistic regression baseline (sklearn, familiar territory)

5. **Phase 2:** Build and train an MLP in PyTorch (new territory)

6. **Phase 3:** Compare, diagnose, and reflect

7. **Prepare your presentation slide**

---

## Starter LLM Prompts

**Planning prompt:**
> "I have pre-extracted EEG features from 109 participants performing motor imagery (imagining left or right hand movement). The CSV has 4,918 rows and 320 features (64 EEG channels × 5 frequency bands: delta, theta, alpha, beta, gamma). The target is binary: left (0) or right (1) hand imagery. I need to: (1) build a logistic regression baseline with sklearn, (2) build and train a simple MLP neural network in PyTorch with 1 hidden layer, (3) compare their accuracy and F1 scores, (4) diagnose any training issues using loss curves. The baseline accuracy from literature is ~60% for logistic regression. Create a plan; don't write code yet."

**Code prompt (after plan):**
> "Following my plan, write Python code to: (1) load the CSV into pandas, (2) separate features (all columns except participant_id, trial, condition, condition_code) and target (condition_code), (3) standardise features with StandardScaler, (4) stratified 80/20 split, (5) fit LogisticRegression baseline and report accuracy + F1, (6) convert to PyTorch tensors (X as FloatTensor, y as LongTensor) and wrap the training tensors in a TensorDataset + DataLoader with batch_size=32 and shuffle=True, (7) set torch.manual_seed(42) for reproducibility, (8) define a SimpleNN class using nn.Module with: Linear(320, 64), ReLU, Dropout(0.3), Linear(64, 2), (9) train for 50 epochs with CrossEntropyLoss and Adam(lr=0.001), using nested loops — outer epoch loop and inner batch loop — and tracking BOTH training and validation loss per epoch, (10) plot training and validation loss curves on the same axes with a horizontal reference line at ln(2), (11) report final accuracy and F1. Use torch, sklearn, matplotlib, pandas."

**Complex debugging prompt:**
> "My neural network training loss stays flat at 0.693 (ln(2)) after 50 epochs. Validation accuracy is ~50% (chance). Here's my code: [paste full training loop]. Data: X_train shape (3934, 320), y_train shape (3934,), 2 classes (balanced). I standardised features and I'm using CrossEntropyLoss + Adam(lr=0.001). What could be wrong? Check: (1) whether I'm calling optimizer.zero_grad() before loss.backward(), (2) whether features are actually being normalised (not just defined but applied), (3) whether my learning rate is too small, (4) whether my architecture (64 hidden units) is too narrow for 320 features."

---

## Starter Code

- **Notebook:** [starter.ipynb](starter.ipynb) — scaffolded Jupyter notebook
- **Script:** [starter.py](starter.py) — scaffolded Python script

Both contain functional data loading, exploration, and preparation (cells/sections 1–5). Your AI fills in the modelling sections.

---

## What to Present (1 HTML slide, ~3 min)

1. **Baseline performance** — logistic regression accuracy and F1
2. **Neural network performance** — MLP accuracy and F1. Show the training loss curves.
3. **Training diagnostics** — did the network overfit? Did you use dropout or early stopping?
4. **Was it worth it?** — Honest comparison: how much did the neural network improve over the baseline? Was the added complexity (code length, debugging time, training time) justified?
5. **One debugging story** — what went wrong during training and how did you fix it (with your AI's help)?

---

## Bonus Challenges

1. **Learning rate sweep** — Try lr = 0.1, 0.01, 0.001, 0.0001. Plot loss curves for each. What's the best rate?

2. **Architecture search** — Try 1 vs 2 vs 3 hidden layers, and 32 vs 64 vs 128 hidden units. Which works best? Create a comparison table.

3. **Dropout experiment** — Try dropout rates of 0.0, 0.2, 0.3, 0.5. Plot validation loss curves for each. At what point does dropout help vs hurt?

4. **sklearn MLPClassifier** — Compare your PyTorch implementation to sklearn's built-in `MLPClassifier`. Do they give the same results? Which is easier to use?

5. **4-class classification** — Use runs with all 4 conditions (left hand, right hand, both hands, feet). How much harder is 4-class? What happens to accuracy?

6. **Channel selection** — Motor imagery is strongest over motor cortex (channels C3, C4, Cz). Try using only the central channels (~6 channels × 5 bands = 30 features) instead of all 320. Does reducing features help or hurt?

7. **Early stopping** — Implement early stopping: track validation loss and stop training when it hasn't improved for 10 epochs. How many epochs does the model actually need?

---

## Hints

<details>
<summary>1. Normalisation matters more for neural networks</summary>

Neural networks are very sensitive to feature scales. Always standardise (mean=0, std=1) BEFORE converting to tensors. Use the training set statistics only:
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Use train stats!
```
</details>

<details>
<summary>2. Check your label types</summary>

`CrossEntropyLoss` expects integer labels as `LongTensor`. A common error is passing float labels or one-hot encoded labels:
```python
y_tensor = torch.LongTensor(y_train)  # Not FloatTensor!
```
</details>

<details>
<summary>3. Start with the simplest network</summary>

Begin with 1 hidden layer of 64 units. Don't add complexity until you've confirmed the simple version works:
```python
class SimpleNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(320, 64)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.3)
        self.output = nn.Linear(64, 2)
```
</details>

<details>
<summary>4. The training loop pattern (nested loops)</summary>

Every PyTorch training loop is **two nested loops** — an outer EPOCH loop and an inner BATCH loop — exactly the structure from the Week 9 flow chart. Wrap your training tensors in a `DataLoader` first:

```python
from torch.utils.data import TensorDataset, DataLoader

train_loader = DataLoader(
    TensorDataset(X_train_tensor, y_train_tensor),
    batch_size=32,
    shuffle=True,
)
```

Then the training loop. The order of the five steps inside the inner loop matters:

```python
for epoch in range(n_epochs):                       # outer EPOCH loop
    running = 0.0
    for X_batch, y_batch in train_loader:           # inner BATCH loop
        optimizer.zero_grad()                        # 1. reset gradients
        outputs = model(X_batch)                     # 2. forward pass
        loss = criterion(outputs, y_batch)           # 3. compute loss
        loss.backward()                              # 4. backward pass
        optimizer.step()                             # 5. update weights
        running += loss.item()
    train_losses.append(running / len(train_loader))
    # After all batches: also measure validation loss — see example solution.
```

Always track **both** train and validation loss — the gap between them is your overfitting diagnostic.
</details>

<details>
<summary>5. Plot loss curves — your best diagnostic</summary>

Track loss per epoch and plot it. This tells you more than any single metric:
```python
train_losses = []
for epoch in range(n_epochs):
    # ... training code ...
    train_losses.append(loss.item())
plt.plot(train_losses)
plt.xlabel('Epoch'); plt.ylabel('Loss')
```
</details>

<details>
<summary>6. Fair comparison = same split</summary>

Use the EXACT same train/test split for both baseline and neural network. Don't re-split:
```python
# Split once
X_train, X_test, y_train, y_test = train_test_split(...)
# Use same splits for both models
baseline = LogisticRegression().fit(X_train_scaled, y_train)
# ... and for PyTorch model
```
</details>

---

*[Back to course overview](../../README.md)*

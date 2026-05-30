# Week 10 Final Plan — What Actually Happened

## What Changed From the Original Plan

### Data
- **Dataset size:** 4,918 trials from 109 participants — exactly as expected
- **Class balance:** 2,480 left (50.4%) / 2,438 right (49.6%) — perfectly balanced
- **Train/test split:** 3,934 train / 984 test (80/20 stratified)
- **Features:** 320 EEG band power features, all numeric, no missing values

### Model Results

| Model | Accuracy | F1 | Notes |
|-------|----------|-----|-------|
| Random guessing | 50.0% | — | Chance level for balanced binary task |
| Logistic Regression | 60.2% | 0.583 | Strong baseline for BCI data |
| Simple MLP (1 hidden) | 60.1% | 0.570 | Did NOT beat logistic regression |

### Key Findings

1. **The MLP did not beat logistic regression.** This is the most important finding. With pre-extracted tabular features and a weak signal, the added complexity of a neural network provided no advantage.

2. **Loss curve did decrease below 0.693**, confirming the network was learning *something*. With mini-batch training (batch_size=32), training loss reached ~0.55 by epoch 50, while validation loss dropped to a minimum around epoch 13 (~0.65) and then started rising. The model couldn't generalise much better than a linear classifier.

3. **Clear overfitting was visible.** Training loss kept dropping while validation loss began rising after ~15 epochs — textbook overfitting, and a good real-world example for students who just met the concept in lecture. Dropout (0.3) helped but couldn't fully prevent it. In practice we'd stop training at the best-val-loss epoch.

4. **Training was fast** — 50 epochs of mini-batch training took only a few seconds on CPU. No GPU needed for this dataset size.

5. **The best features were alpha and beta band powers in C3/C4 channels** — exactly what neuroscience predicts for motor imagery. C4 alpha was notably higher during right-hand imagery (mean +5.50 µV²/Hz), consistent with contralateral motor cortex desynchronisation.

### Debugging Story

The initial MLP architecture and training loop worked on the first attempt — no errors, no flat loss curves. This made the comparison even more telling: even when everything works perfectly, the neural network still doesn't beat logistic regression on this data.

If we had introduced a bug (e.g., forgetting `optimizer.zero_grad()` or using the wrong tensor type), the loss would have stayed flat at 0.693 — a classic silent failure with no traceback. The debugging prompts in the challenge brief address exactly this scenario.

### What I Would Do Differently

1. **Try a deeper architecture** — 2–3 hidden layers with batch normalisation might extract better non-linear feature interactions
2. **Learning rate scheduling** — start higher (0.01) and decay, or use a learning rate finder
3. **Use raw EEG data** — a 1D CNN could learn features directly from time-series data, bypassing the hand-crafted band power extraction
4. **Cross-validation** — our single 80/20 split is noisy; k-fold would give more reliable estimates
5. **Channel selection** — use only motor cortex channels (C3, C4, Cz) to reduce noise from irrelevant channels
6. **Participant-level split** — our current split leaks information (same participant can appear in both train and test). A proper subject-independent split would give more realistic accuracy (~55%)

### Ethical Considerations

BCI systems classify brain signals to help people with paralysis control devices. Accuracy matters enormously — a 60% accurate BCI is usable but frustrating (4 in 10 commands misinterpreted). Before deployment, such systems need:
- Much higher accuracy (ideally >90%, achieved through personalised calibration)
- Clear user feedback so people know when the system is uncertain
- Robust testing across diverse populations (age, disability type, cultural background)

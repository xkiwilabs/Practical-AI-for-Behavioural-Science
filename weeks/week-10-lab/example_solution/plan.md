# Week 10 Analysis Plan — Beat the Baseline

## Research Question

Can a neural network (MLP) classify left vs right motor imagery from pre-extracted EEG features better than logistic regression? And is the added complexity worth it?

## Dataset

- **Source:** PhysioNet EEG Motor Movement/Imagery Dataset (pre-extracted features)
- **File:** `data/eeg_motor_imagery_features.csv`
- **Size:** 4,918 trials from 109 participants
- **Features:** 320 EEG features (64 channels × 5 frequency bands: delta, theta, alpha, beta, gamma)
- **Target:** `condition_code` — left hand (0) vs right hand (1)
- **Balance:** Nearly 50/50 split

## Plan

### Phase 1: Exploration
1. Load CSV and check shape
2. Confirm class balance (should be ~50/50)
3. Examine feature distributions — are there outliers or extreme values?
4. Check which channels/bands vary most between conditions (expect C3/C4 alpha/beta)
5. Save exploration plots

### Phase 2: Logistic Regression Baseline
1. Separate features (320 columns) and target (condition_code)
2. Stratified 80/20 train/test split (random_state=42)
3. Standardise features using StandardScaler (fit on train only)
4. Fit LogisticRegression(max_iter=1000, random_state=42)
5. Report accuracy and F1 on test set
6. Print classification report
7. Expected: ~60% accuracy (this is typical for BCI motor imagery)

### Phase 3: Neural Network (PyTorch MLP)
1. Convert scaled data to PyTorch tensors (FloatTensor for X, LongTensor for y)
2. Wrap training tensors in a TensorDataset + DataLoader (batch_size=32, shuffle=True)
3. Set `torch.manual_seed(42)` for reproducibility
4. Define SimpleNN:
   - Input: 320 features
   - Hidden: 64 units, ReLU activation, Dropout(0.3)
   - Output: 2 classes
5. Train with CrossEntropyLoss + Adam(lr=0.001) for 50 epochs using nested loops:
   - Outer EPOCH loop, inner BATCH loop
   - Average training loss across batches each epoch
6. Track training loss AND validation loss each epoch
5. Plot loss curves — check for:
   - Decreasing loss = learning
   - Flat at 0.693 = random guessing
   - Train drops but val rises = overfitting

### Phase 4: Comparison
1. Evaluate MLP on test set — accuracy and F1
2. Print side-by-side comparison table
3. Plot confusion matrices for both models
4. Plot model comparison bar chart

### Phase 5: Reflection
- Was the MLP better than LogReg?
- How much harder was it to implement?
- Would I recommend using a neural network for this data?

## Expected Outcomes

- **Baseline (LogReg):** ~60% accuracy
- **Simple MLP:** 58–62% (may not beat LogReg!)
- **Key diagnostic:** Loss curve should decrease below 0.693, but not by much
- **Likely conclusion:** For pre-extracted tabular features with limited signal, a neural network doesn't necessarily outperform logistic regression

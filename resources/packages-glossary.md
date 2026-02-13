# Python Packages Glossary

A quick-reference guide to the Python packages you'll use in PSYC4411.

We've chosen **well-known, well-documented, and widely-used packages** for this course — the same tools used by data scientists and researchers around the world. That means when you ask an AI assistant for help, it will know these packages well and give you reliable answers.

**You're not limited to these.** For any challenge lab, you can ask your AI assistant: *"What other Python packages could I use for this task?"* There are often alternatives, and part of learning to work with AI tools is discovering what's available. These are just the ones we'll teach with and that we know work well together.

---

## Data and Numbers

### pandas

**What it does:** Loads, manipulates, and explores tabular data — think of it as Python's version of a spreadsheet.

**You'll use it to:** Read CSV files into DataFrames (data tables), filter rows, calculate summary statistics, group data by categories, and prepare data for analysis.

**Example:** `data = pd.read_csv("my_dataset.csv")` loads a CSV file into a table you can work with.

**Used in:** Every lab from Week 2 onwards.

---

### NumPy

**What it does:** Fast numerical computing — arrays, mathematical operations, and linear algebra under the hood.

**You'll use it to:** Calculate trend lines, generate random numbers, and do maths on whole columns of data at once. Many other packages (pandas, scikit-learn, PyTorch) are built on top of NumPy.

**Example:** `np.mean(scores)` calculates the average of an array of scores.

**Used in:** Every lab from Week 2 onwards (often behind the scenes).

---

## Visualisation

### matplotlib

**What it does:** The foundational plotting library for Python. Almost every other plotting package is built on top of it.

**You'll use it to:** Create figures, arrange multiple plots in grids, customise colours, labels, and layout, and save figures as PNG files.

**Example:** `fig, axes = plt.subplots(2, 2)` creates a 2×2 grid of panels for a multi-panel figure.

**Used in:** Every lab from Week 2 onwards.

---

### seaborn

**What it does:** Makes statistical plots look great with minimal code. Built on top of matplotlib, but with nicer defaults and easier syntax for common plot types.

**You'll use it to:** Create scatter plots, box plots, violin plots, heatmaps, and pair plots with one or two lines of code. It understands pandas DataFrames directly.

**Example:** `sns.scatterplot(data=df, x="Sleep", y="Depression", hue="Gender")` creates a colour-coded scatter plot in one line.

**Used in:** Every lab from Week 2 onwards.

---

## Machine Learning (Classical)

### scikit-learn

**What it does:** The standard toolkit for "classical" machine learning — everything from linear regression to random forests, clustering, and dimensionality reduction.

**You'll use it to:** Split data into training and test sets, fit models (regression, classification, clustering), evaluate model performance (accuracy, R², confusion matrices), and run cross-validation. It follows a consistent pattern: create a model, fit it to data, make predictions.

**Example:** `model = LinearRegression()` then `model.fit(X_train, y_train)` then `model.predict(X_test)` — the same three steps for almost every model.

**Used in:** Weeks 4–8 (regression, classification, clustering, dimensionality reduction).

---

### SciPy

**What it does:** Scientific computing utilities — statistical tests, hierarchical clustering, signal processing, and optimisation.

**You'll use it to:** Build dendrograms (tree diagrams) for hierarchical clustering and run statistical tests. It fills the gaps between NumPy (pure maths) and scikit-learn (full ML pipelines).

**Example:** `scipy.cluster.hierarchy.dendrogram(linkage_matrix)` draws a tree showing how clusters merge.

**Used in:** Weeks 7–8 (unsupervised learning and clustering).

---

## Deep Learning

### PyTorch

**What it does:** A deep learning framework for building and training neural networks. Used by most AI research labs worldwide.

**You'll use it to:** Build a multilayer perceptron (a type of neural network), define loss functions, run training loops with gradient descent, and understand how neural networks learn from data. Don't worry — we'll walk through every step.

**Example:** You'll define layers (`nn.Linear`), a forward pass, and a training loop that gradually improves the network's predictions.

**Used in:** Weeks 9–10 (neural networks).

---

### Transformers (Hugging Face)

**What it does:** Provides access to thousands of pre-trained AI models — the same technology behind tools like ChatGPT, but available for you to use directly in Python.

**You'll use it to:** Generate text embeddings (numerical representations of meaning), measure semantic similarity between sentences, and cluster text data. This is where the course connects to how modern AI language models actually work.

**Example:** You'll load a pre-trained model, feed it sentences, and get back vectors that capture what those sentences *mean* — similar sentences produce similar vectors.

**Used in:** Week 11 (embeddings, language models, and AI for research).

---

### UMAP

**What it does:** Reduces high-dimensional data to 2D or 3D so you can visualise it. Similar to PCA (which is in scikit-learn) but better at preserving complex, non-linear patterns.

**You'll use it to:** Visualise clusters in data that has many variables — for example, plotting hundreds of text embeddings on a 2D scatter plot where similar texts appear close together.

**Example:** `umap.UMAP(n_components=2).fit_transform(data)` takes your high-dimensional data and produces x, y coordinates you can plot.

**Used in:** Weeks 7–8 (dimensionality reduction) and Week 11 (visualising embeddings).

---

## Jupyter Environment

### Jupyter / IPython

**What it does:** The notebook environment you'll code in — lets you mix code, output, and written notes in a single document.

**You'll use it to:** Run code cell by cell, see results immediately, and document your analysis alongside your code. The setup guide installs everything you need.

**Used in:** Every lab.

---

## At a Glance

| Package | One-line summary | First used |
|---------|-----------------|------------|
| **pandas** | Load and explore data tables | Week 2 |
| **NumPy** | Fast maths on arrays | Week 2 |
| **matplotlib** | Create and customise plots | Week 2 |
| **seaborn** | Beautiful statistical plots | Week 2 |
| **scikit-learn** | Classical ML models and evaluation | Week 4 |
| **SciPy** | Hierarchical clustering, stats tests | Week 7 |
| **PyTorch** | Neural networks and deep learning | Week 9 |
| **Transformers** | Pre-trained language models, embeddings | Week 11 |
| **UMAP** | Visualise high-dimensional data in 2D | Week 7 |

---

*[Back to resources](README.md) · [Back to course overview](../README.md)*

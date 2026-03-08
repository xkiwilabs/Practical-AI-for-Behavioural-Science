# Week 3: Additional Readings and Resources

> **Note:** The required reading for this week is the [companion reading](README.md) (the `README.md` in this folder). The readings below are **optional** — they provide additional depth and are a great place to find papers for your presentation and written assignment.

## Suggested Readings

These are accessible papers that directly address the core topics from this week — generalisation, overfitting, cross-validation, and best practices for prediction studies in psychology.

### 1. Yarkoni, T., & Westfall, J. (2017). Choosing prediction over explanation in psychology: Lessons from machine learning. *Perspectives on Psychological Science, 12*(6), 1100–1122. https://doi.org/10.1177/1745691617693393

*Why read this:* Re-recommended from Week 1 — but this time, read Sections 2–3 carefully. They cover overfitting, cross-validation, and regularisation in the context of psychology, and they're directly relevant to everything in this week's lecture. If you only read one paper this week, make it this one. **Open access** — free PDF available via [PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC6603289/) and [author's website](https://talyarkoni.org/pdf/Yarkoni_PPS_2017.pdf).

### 2. de Rooij, M., & Weeda, W. (2020). Cross-validation: A method every psychologist should know. *Advances in Methods and Practices in Psychological Science, 3*(2), 248–263. https://doi.org/10.1177/2515245919898466

*Why read this:* A tutorial written specifically for psychologists on cross-validation — when to use it, how to implement it, and common pitfalls. Clear, practical, and assumes no ML background. Directly relevant to the cross-validation section of this week's reading. **Open access.**

### 3. Poldrack, R. A., Huckins, G., & Varoquaux, G. (2020). Establishment of best practices for evidence for prediction: A review. *JAMA Psychiatry, 77*(5), 534–540. https://doi.org/10.1001/jamapsychiatry.2019.3671

*Why read this:* A concise review of what makes a good prediction study — and the many ways they go wrong. Covers overfitting, information leakage, and reporting standards. Written by leading methodologists in neuroimaging and psychiatry. Short and high-impact. **Free** via [PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC7250718/).

---

## Optional / Deeper Readings

These go deeper into specific topics from the lecture. Read them if something sparked your curiosity.

### 4. Vabalas, A., Gowen, E., Poliakoff, E., & Casson, A. J. (2019). Machine learning algorithm validation with a limited sample size. *PLOS ONE, 14*(11), e0224365. https://doi.org/10.1371/journal.pone.0224365

*Why read this:* Shows that k-fold cross-validation can produce overly optimistic (biased) estimates when sample sizes are small — a common situation in psychology. Uses an autism classification example. Directly relevant to the question of whether cross-validation "guarantees" good performance (it doesn't). **Open access.**

### 5. Hosseini, M., Powell, M., Collins, J., Callahan-Flintoft, C., Jones, W., Bowman, H., & Wyble, B. (2020). I tried a bunch of things: The dangers of unexpected overfitting in classification of brain data. *Neuroscience & Biobehavioral Reviews, 119*, 456–467. https://doi.org/10.1016/j.neubiorev.2020.09.036

*Why read this:* A cautionary tale — the authors got statistically significant classification results on *random data* by trying different preprocessing pipelines and hyperparameter settings. A vivid demonstration of how overfitting happens in practice, even to careful researchers. Preprint available on [bioRxiv](https://www.biorxiv.org/content/10.1101/078816v2).

### 6. Koul, A., Becchio, C., & Cavallo, A. (2018). Cross-validation approaches for replicability in psychology. *Frontiers in Psychology, 9*, 1117. https://doi.org/10.3389/fpsyg.2018.01117

*Why read this:* Positions cross-validation as a tool against the replication crisis — if your findings don't survive cross-validation, they probably won't replicate either. Practical and clearly written. **Open access.**

### 7. Cearns, M., Hahn, T., & Baune, B. T. (2019). Recommendations and future directions for supervised machine learning in psychiatry. *Translational Psychiatry, 9*(1), 271. https://doi.org/10.1038/s41398-019-0607-2

*Why read this:* Practical guidelines for doing ML well in psychiatry — covers sample size, feature selection, cross-validation, and reporting. A good template for what "responsible ML in clinical research" looks like. **Open access.**

### 8. James, G., Witten, D., Hastie, T., Tibshirani, R., & Taylor, J. (2023). *An introduction to statistical learning: With applications in Python.* Springer. Chapters 2 & 5. **Free PDF:** [statlearning.com](https://www.statlearning.com/)

*Why read this:* Cross-referenced from Week 1. Chapter 2 introduces the statistical learning framework — bias-variance trade-off, training vs test error, and the concepts behind everything in this week's lecture. Chapter 5 covers cross-validation in depth. Clear, applied, and not overly mathematical.

### 9. Jacobucci, R., Grimm, K. J., & Zhang, Z. (2023). *Machine learning for social and behavioral research.* Guilford Press.

*Why read this:* Cross-referenced from Week 1. The chapters on regularisation (Ridge, Lasso) and model evaluation are directly relevant to this week's topics and next week's lab. Written specifically for social and behavioural scientists.

---

*[Back to Week 3](README.md) · [Back to course overview](../../README.md)*

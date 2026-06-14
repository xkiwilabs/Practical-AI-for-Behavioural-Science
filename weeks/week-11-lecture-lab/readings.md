# Week 11 Readings: Deep Learning, LLMs, and Generative AI for Psychological Research

> These readings support the Week 11 lecture. **All readings are optional this week** — the lecture and companion reading are self-contained, and you should be saving energy for the Week 12 course review. The suggested readings are the three I'd reach for first if you want to go deeper; the optional list goes further.

---

## Suggested Readings

### 1. Alammar & Grootendorst (2024) — Hands-on Large Language Models

Alammar, J., & Grootendorst, M. (2024). *Hands-on large language models: Language understanding and generation*. O'Reilly Media.

**Why read this:** The best plain-language introduction to how LLMs work end-to-end. Chapters 1–3 cover tokens, embeddings, and the transformer at exactly the level this week's lecture pitched them. Chapters on semantic search and document clustering are directly useful for research applications.

**Access:** Commercial book. Available via O'Reilly online platform — check Macquarie University library for institutional access. Code repository: [github.com/HandsOnLLM](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models).

---

### 2. Mathis et al. (2018) — DeepLabCut

Mathis, A., Mamidanna, P., Cury, K. M., Abe, T., Murthy, V. N., Mathis, M. W., & Bethge, M. (2018). DeepLabCut: Markerless pose estimation of user-defined body parts with deep learning. *Nature Neuroscience*, *21*(9), 1281–1289. https://doi.org/10.1038/s41593-018-0209-y

**Why read this:** The foundational marker-less pose estimation paper, directly cited in the lecture's CNN-applications section. A worked example of how a CNN trained on a few hundred frames can do what motion-capture labs used to need. If you're considering using pose estimation in your honours project, start here.

**Access:** Paywalled via Nature Neuroscience; Macquarie library has institutional access. Preprint available on [bioRxiv](https://www.biorxiv.org/content/10.1101/476531v1).

---

### 3. Vaswani et al. (2017) — Attention Is All You Need

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems*, *30*, 5998–6008. https://arxiv.org/abs/1706.03762

**Why read this:** The transformer paper — the architecture behind every current LLM. Honours students should at least see what the original paper looks like, even if you don't read it in depth. The architectural diagrams in Section 3 map directly onto the self-attention and transformer-block sections of the lecture.

**Access:** Open access on [arXiv](https://arxiv.org/abs/1706.03762).

---

## Optional / Deeper Readings

### 4. Demszky et al. (2023) — Using Large Language Models in Psychology

Demszky, D., Yang, D., Yeager, D. S., Bryan, C. J., Clapper, M., Chandhok, S., Eichstaedt, J. C., Hecht, C., Jamieson, J., Johnson, M., Jones, M., Krettek-Cobb, D., Lai, L., JonesMitchell, N., Ong, D. C., Dweck, C. S., Gross, J. J., & Pennebaker, J. W. (2023). Using large language models in psychology. *Nature Reviews Psychology*, *2*(11), 688–701. https://doi.org/10.1038/s44159-023-00241-5

**Why read this:** The single most relevant review for psychology students. Surveys how LLMs are being used (and misused) across measurement, experimentation, and practice in psychology. Strong on what's ready now versus what isn't.

**Access:** Paywalled via Nature Reviews Psychology; Macquarie library has access. Author-hosted preprint available on [Dora Demszky's site](https://www.dorademszky.com/publications/25838-using-large-language-models-in-psychology).

---

### 5. Pereira et al. (2022) — SLEAP

Pereira, T. D., Tabris, N., Matsliah, A., Turner, D. M., Li, J., Ravindranath, S., Papadoyannis, E. S., Normand, E., Deutsch, D. S., Wang, Z. Y., McKenzie-Smith, G. C., Mitelut, C. C., Castro, M. D., D'Uva, J., Kislin, M., Sanes, D. H., Kocher, S. D., Wang, S. S.-H., Falkner, A. L., … Murthy, M. (2022). SLEAP: A deep learning system for multi-animal pose tracking. *Nature Methods*, *19*(4), 486–495. https://doi.org/10.1038/s41592-022-01426-1

**Why read this:** A useful contrast to DeepLabCut for multi-animal scenarios. If you might track multiple agents (animals or humans) interacting, SLEAP is often the better fit.

**Access:** Paywalled via Nature Methods; Macquarie library has access.

---

### 6. Cao et al. (2019) — OpenPose

Cao, Z., Hidalgo, G., Simon, T., Wei, S.-E., & Sheikh, Y. (2019). OpenPose: Realtime multi-person 2D pose estimation using part affinity fields. *IEEE Transactions on Pattern Analysis and Machine Intelligence*, *43*(1), 172–186. https://doi.org/10.1109/TPAMI.2019.2929257

**Why read this:** The foundational marker-less pose paper for humans. Worth skimming alongside DeepLabCut to see how the same CNN-feature-extraction idea solves a different problem (multiple people in the same frame).

**Access:** Paywalled via IEEE; Macquarie library has access. Open-access preprint on [arXiv](https://arxiv.org/abs/1812.08008).

---

### 7. Barrett et al. (2019) — Emotional Expressions Reconsidered

Barrett, L. F., Adolphs, R., Marsella, S., Martinez, A. M., & Pollak, S. D. (2019). Emotional expressions reconsidered: Challenges to inferring emotion from human facial movements. *Psychological Science in the Public Interest*, *20*(1), 1–68. https://doi.org/10.1177/1529100619832930

**Why read this:** The critical counterpoint to automated emotion recognition. A long, careful review showing that the inference from facial movement to internal emotional state is much weaker than the popular literature implies. Essential reading if you're considering any project that involves automated emotion classification.

**Access:** Paywalled via SAGE; Macquarie library has access. Author manuscript freely available via [University of Glasgow archive](http://eprints.gla.ac.uk/178385/).

---

### 8. Auletta et al. (2023) — LSTMs for Predicting Joint Action

Auletta, F., Kallen, R. W., di Bernardo, M., & Richardson, M. J. (2023). Predicting and understanding human action decisions during skillful joint-action using supervised machine learning and explainable-AI. *Scientific Reports*, *13*, 4992. https://doi.org/10.1038/s41598-023-31807-1

**Why read this:** A direct example of LSTMs used in cognitive science. The model predicts a player's target choice in a multi-agent herding task *before* the player has consciously decided. Pairs explainable AI (SHAP) with sequence modelling — a nice example of how to use a deep model without losing interpretability.

**Access:** Open access (CC BY 4.0) — free PDF from [Nature](https://www.nature.com/articles/s41598-023-31807-1).

---

### 9. Bender et al. (2021) — On the Dangers of Stochastic Parrots

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency*, 610–623. https://doi.org/10.1145/3442188.3445922

**Why read this:** The most influential sceptical paper on large language models. Critiques the environmental cost, bias amplification, and "fluent nonsense" risks of scaling LLMs. An essential counterweight to LLM hype, and a paper you should be able to discuss in any honours-level conversation about AI.

**Access:** Open access via [ACM](https://dl.acm.org/doi/10.1145/3442188.3445922).

---

### 10. Ouyang et al. (2022) — InstructGPT / RLHF

Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., Schulman, J., Hilton, J., Kelton, F., Miller, L., Simens, M., Askell, A., Welinder, P., Christiano, P., Leike, J., & Lowe, R. (2022). Training language models to follow instructions with human feedback. *Advances in Neural Information Processing Systems*, *35*, 27730–27744. https://arxiv.org/abs/2203.02155

**Why read this:** The RLHF paper — the recipe that made ChatGPT *behave* like an assistant rather than just a text predictor. Read at least the introduction and the methods overview to understand the three-stage training pipeline described in the lecture.

**Access:** Open access on [arXiv](https://arxiv.org/abs/2203.02155).

---

### 11. Bommasani et al. (2021) — On the Opportunities and Risks of Foundation Models

Bommasani, R., Hudson, D. A., Adeli, E., Altman, R., Arora, S., von Arx, S., … Liang, P. (2021). On the opportunities and risks of foundation models. *Stanford Center for Research on Foundation Models technical report*. https://arxiv.org/abs/2108.07258

**Why read this:** A long but comprehensive survey of LLMs as "foundation models" — pre-trained models that get adapted to many downstream tasks. You don't need to read all 200+ pages; the executive summary and any section relevant to your interests is enough.

**Access:** Open access on [arXiv](https://arxiv.org/abs/2108.07258); also available from [Stanford CRFM](https://crfm.stanford.edu/report.html).

---

## Readings by Week Topic

| Week | Topic | Key readings |
|------|-------|-------------|
| 1 | AI + Problem Solving | See Week 1 readings |
| 2 | First ML Lab | See Week 2 challenge brief |
| 3 | Generalisation & Overfitting | See Week 3 readings |
| 4 | Regression Lab | See Week 4 challenge brief |
| 5 | Classification & Trees | See Week 5 readings |
| 6 | Classification Lab | See Week 6 challenge brief |
| 7 | Clustering & Dimensionality Reduction | See Week 7 readings |
| 8 | PCA/Clustering Lab | See Week 8 challenge brief |
| 9 | Neural Networks | See Week 9 readings |
| 10 | Neural Network Lab | See Week 10 challenge brief |
| **11** | **Deep Learning, LLMs, GenAI** | **Alammar & Grootendorst (2024), Mathis et al. (2018), Vaswani et al. (2017)** |

---

*[Back to companion reading](README.md) · [Back to course overview](../../README.md)*

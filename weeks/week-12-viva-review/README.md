# Week 12: Viva Review — Study Guide

This is your study hub for the **viva oral exam** (30% of your final grade). The exam is 15 minutes, individual, and in person — you can't bring notes or slides. The three sections, the timing, and the rubric are all spelled out in [assessments/viva-exam.md](../../assessments/viva-exam.md). This page focuses on **how to prepare**.

You'll find two practice files alongside this README:

- **[`concept-list.md`](concept-list.md)** — your **single study reference** for the viva. It has two parts:
  - **Part 1** lists the **40 testable concepts** for Section 1 (you'll be asked to define **10** at random). Definitions are not shown — practise giving them aloud in 20 seconds each.
  - **Part 2** lists **additional course concepts** with definitions (method names, metrics, and tools used throughout the course — R², UMAP, cosine similarity, MediaPipe, etc.). These are not asked in Section 1, but you should be comfortable using them when you talk about the methods you've learned.
- **[`viva-terms.csv`](viva-terms.csv)** — the same 40 testable terms in CSV form (terms only).
- **[`short-answer-examples.md`](short-answer-examples.md)** / **[`viva-questions.csv`](viva-questions.csv)** — **9 example short-answer questions** released for practice. The markdown shows each question with an example narrative response so you can calibrate length and structure; the CSV is the same questions for tools or apps. Your actual 3 exam questions are drawn from a separate test pool you do not see in advance — but the test questions cover the same kinds of ML reasoning skills as the examples, so practising on the examples genuinely prepares you for the exam.

For Section 1, prepare the whole 40-term pool — you do not see your specific 10 in advance. For Section 2, practise on the 9 examples; the test questions sit in the same space of ML decisions but with different research scenarios (different population, instrument, deployment context). Read Part 2 of the concept reference to refresh the broader course terminology before the exam.

---

## What the viva tests

Three sections in one 15-minute sitting:

| Section | Format | Points | Time per item |
|---|---|---|---|
| 1. Concept definitions | **10 terms** drawn at random from a pool of 40 | 40 | 20 sec to think and answer |
| 2. Short-answer research applications | **3 questions** drawn at random from a test pool; 9 example questions are released in advance for practice | 36 | 30 sec to plan + 60 sec to answer |
| 3. Study-proposal elevator pitch (prepared in advance) | 2-min pitch + 30 sec LLM reflection | 24 | 2:30 total |

The full rubric for each section is in [viva-exam.md](../../assessments/viva-exam.md).

Everything examined comes from **Weeks 1–11**. Week 12 (this week) is consolidation; Week 13 is class discussion. No new examinable content from this week or next.

---

## Section 1: Definitions — how to prepare

You'll get 10 terms from `viva-terms.csv`, one at a time. Twenty seconds per term to think and answer. The marker scores **technical accuracy** (75%) and **conciseness** (25%) — accuracy matters more, but rambling costs you marks even when you're right.

**Practice strategy:**

- Read the term list end-to-end and rate yourself on each (confident / shaky / no idea). Focus your study on the shaky and unknown ones.
- For every term, write a **one-sentence definition** of your own. Don't just memorise — phrase it in your own words, then check against the lectures and companion readings to make sure you've kept the technical meaning.
- Practise **out loud and timed**. Set a 20-second timer, look at a random term, and give the definition. The gap between "I know this" and "I can say it in 20 seconds" is bigger than it feels.
- Group related terms (e.g., regularisation / Ridge / Lasso) — understanding the relationships helps when you blank on one.

**What a good 20-second answer looks like:** one clean sentence that nails the technical content, no preamble, no hedging. "Cross-validation is a model evaluation procedure that splits the data into folds and rotates which fold is held out, giving a more stable estimate of out-of-sample performance than a single split." Done.

**What costs you marks:** "Um, so cross-validation is basically when, you know, you split the data into different parts, kind of like training and testing but multiple times, so you can sort of get a better idea of…" — even if the technical idea is right, this loses on conciseness.

---

## Section 2: Short-answer research applications — how to prepare

You'll get 3 questions in the exam. For each: 30 seconds to plan, then up to 60 seconds to answer. The marker scores **appropriateness and technical accuracy** (60%) and **clarity** (40%).

> **A note on the bar — read this first.** This section is testing your **general understanding** of the methods and materials covered in the course — **not** PhD-level technical depth. The goal is to see that you have engaged with the methods, can pick a reasonable approach for a given research scenario, and can talk through what you would do and what you would be cautious about. A clear, structured one-minute answer that touches the main ideas is plenty. You **do not** need to recite textbook definitions, hit every metric, or be perfect. Reasonable choices, reasonable caveats, in your own words. That's it. This section is designed to be approachable, not to stress you out.

Each question presents a research scenario and asks how you'd approach it with the methods you've learned. The marker is looking for a clear three-part answer:

1. **The method you'd choose** and a one-line justification of *why* this method fits this problem.
2. **How you'd set up the study** — what you'd measure, how you'd split the data, what to be careful about in the design.
3. **How you'd evaluate** — which metrics, what could go wrong, what would make you trust (or not trust) the result.

If you hit those three points in plain language, you're already in strong territory. Anything extra — a thoughtful caveat, a comparison to a simpler model, a fairness concern — is icing.

**Practice strategy:**

- Read through the 9 example questions in [`short-answer-examples.md`](short-answer-examples.md). Group them by method family (regression, classification, dim reduction, neural nets, embeddings/LLMs). You'll see the same skeleton repeating.
- For each question, sketch a 3-bullet plan: *method → design → analysis*. Practise *out loud*, timed, in under a minute.
- For each method family, rehearse the **bad outcomes** — class imbalance for classification, overfitting for neural nets, fake clusters for unsupervised learning, hallucinations for LLMs. The marker rewards critical thinking about what could go wrong.
- Don't try to cram every possible method into one answer. A clean, focused choice is better than a tour of everything you remember.

**What a good 60-second answer sounds like:** "I'd treat this as a binary classification problem. Logistic regression as a baseline, then a random forest. Stratified train/test split because the classes will be imbalanced. I'd evaluate with AUC and recall — recall matters here because false negatives are the costly errors in a screening context. Before trusting the result I'd check class balance, whether the model performs differently across demographic subgroups, and how robust it is to a held-out clinic. The model identifies correlates, not causes, so I wouldn't push for clinical deployment from this alone."

That's roughly the bar — a sensible plan, in your own voice, with one or two caveats. You don't need more than that to score well.

---

## Section 3: Study-proposal pitch — how to prepare

This is the one part you **can prepare in advance**. Two minutes, no notes during delivery, on a study you've designed that uses one or more methods from the course.

Section 3 is the most points-per-minute (24 points in 2 minutes) and the easiest to lift through rehearsal. The full rubric is in [viva-exam.md](../../assessments/viva-exam.md) — but the key knobs are **clarity** (30%), **technical accuracy** (30%), and **innovation** (40%). Innovation is the biggest single component, so don't pick a study you already know exists.

**A strong 2-minute pitch hits:**

1. The phenomenon you're investigating and why it matters (15 sec)
2. The participants and what you'd measure (20 sec)
3. The method(s) and why you chose them (30 sec)
4. What a successful result looks like, and what would worry you (30 sec)
5. A clear close — one sentence on the contribution (10 sec)
6. Buffer (15 sec)

**Use an LLM to develop your idea**, then own it. The 30-second LLM reflection at the end is graded informally — the marker is checking whether you used the LLM critically (verifying, rejecting, refining) versus passively accepting whatever it suggested. *"I used an LLM to brainstorm five candidate designs, then rejected three because they didn't match the methods we'd covered, and used the AI to pressure-test the analysis plan for the remaining two"* lands better than *"I asked it to write me a study"*.

**Rehearse out loud at least three times.** Time it. If you can't deliver it in under 2 minutes when alone in your room, you won't deliver it in under 2 minutes in the exam room.

---

## General study advice

- **Study from your own work.** The companion readings, your lab notebooks, your AI chat histories, and the slide decks are the best material. Quizlet decks made by strangers are not.
- **Practise out loud.** Reading silently is not how the viva is examined. Talking to a wall, a flatmate, or a study partner is the highest-leverage thing you can do.
- **Use an LLM as a study partner — but verify.** Try: *"You are an examiner. Ask me 5 random definition questions from this list. Score each answer for accuracy and conciseness."* This works well. *"Tell me everything I need to know about random forests"* does not — you'll get a wall of text you won't remember.
- **Time yourself.** The pressure in the exam is the timer, not the content.
- **The viva is not designed to trick you.** Every term and every question maps to material you've seen in class. If you've engaged with the labs and readings, you have what you need — preparation is about *retrieval under time pressure*.

---

## Common worries

**"What if I draw a term I don't know?"** Twenty seconds is short. Give your best one-sentence attempt — partial credit is real. Don't freeze; the marker would rather hear "I think it's the procedure where…" than silence.

**"What if my pitch sounds basic?"** Innovation in a 4th-year context isn't a Nature paper — it's a credible psychological question with a sensible match to a method you've actually learned. Don't reach for something you can't defend.

**"What if I forget a method name?"** Describe what it does. "A model that combines many decision trees and averages their predictions" gets you to *random forest* — and the marker awards content over recall of the label.

---

*[Back to assessments overview](../../assessments/README.md) · [Back to course overview](../../README.md)*

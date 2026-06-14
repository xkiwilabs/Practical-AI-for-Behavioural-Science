# Course Review Practice App

A small practice tool that walks you through a **full timed run-through** of the
course review — three sections (concept definitions, short answers, and a study
pitch), each with its own time limit — so you can test yourself under a little
gentle time pressure. Nothing here is scored, and nothing is uploaded anywhere;
it is purely for your own self-quizzing.

## How to run it

1. Open the file **`index.html`** in this folder — just **double-click** it and
   it opens in your web browser. You do **not** need Python, a terminal, or an
   internet connection.
2. Click **Start Practice**.
3. Work through the three sections out loud, keeping to the on-screen timers:
   - **Section 1 — Definitions:** 10 terms drawn at random, **4 minutes** in total
     (about 20–25 seconds each).
   - **Section 2 — Short Answer:** 3 questions. For each you get **15 seconds to
     read**, **30 seconds to plan**, then **1 minute to answer**.
   - **Section 3 — Pitch:** a short **10-second "get ready"**, then your
     **2-minute** study-proposal pitch, then **30 seconds** to reflect on how you
     used an LLM.
4. Each run reshuffles the terms and picks a fresh set of questions, so you can
   practise as many times as you like.

> **Tip:** if recording (below) gives you trouble in Chrome opened by
> double-click, you can instead serve the folder locally — open a terminal in
> this folder and run `python3 -m http.server 8000`, then visit
> **http://127.0.0.1:8000/**. This isn't required for the timed practice, only
> if you want the optional recording to be rock-solid.

## Optional: record yourself

On the start screen you can tick **"Record my voice so I can play it back
afterwards."** Your browser will ask permission to use the microphone — that's
expected. If you allow it, you'll see:

- the **name of the microphone** being used, and
- a **live level bar** — speak and it should move.

A bar on every screen shows your recording volume throughout the run, and at the
end you can play back each section to hear how you sound and how well you kept to
time.

Your recording **stays on your own device** — nothing is uploaded, saved to a
server, or seen by anyone else. When you close the page, it's gone.

## Microphone troubleshooting

If the level bar stays **flat (grey)** while you talk, or your playback is silent,
the app is fine — your browser just isn't receiving any sound. Work through these:

1. **Check the device name shown under the bar.** If it's *not* the mic you
   expect (e.g. it says a USB adapter, a headset that's unplugged, or something
   like *Aggregate Device* / *ZoomAudioDevice*), that's the problem.
2. **Chrome keeps its own default microphone, separate from your Mac's.** Go to
   **`chrome://settings/content/microphone`** and set the **Microphone** dropdown
   to your real mic (e.g. *MacBook Microphone*) or to **Default**. Then reload the
   practice page and tick Record again.
3. **macOS permission and input:** open **System Settings → Privacy & Security →
   Microphone** and make sure your browser is switched **on** (quit and reopen the
   browser after changing this). Then **System Settings → Sound → Input** — pick
   your real mic, and check the **Input volume** slider isn't dragged to the far
   left.
4. **Unplug any USB audio adapters** you're not using — the browser sometimes
   latches onto them even when nothing is connected to their input.

You can confirm it's fixed without doing a whole run: tick Record on the start
screen and watch the bar move when you speak.

## What's in this folder

- `index.html` — the practice app (open this one).
- `practice-data.js` — the terms and example questions the app draws from. These
  are the same terms and example questions in the Week 12 study guide, with **no
  answers**.

## A reminder about Section 2

The practice questions are **9 example research scenarios** spanning the major
method families in the course. The goal is to get comfortable picking a sensible
method and talking through it clearly in about a minute. You are **not** expected
to give PhD-level detail — a clear, reasonable answer in your own words is exactly
what this is for.

*[Back to the Week 12 study guide](../README.md)*

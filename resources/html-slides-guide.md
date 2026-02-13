# HTML Slides Guide

For your paper presentation in this course, you'll create a single HTML slide using <a href="https://revealjs.com" target="_blank">reveal.js</a> — the same framework used for the course lecture slides. This guide covers everything you need, from getting started to exporting your slide as a PDF.

---

## What Are HTML Slides?

Instead of PowerPoint, your presentation slide is a simple HTML file that opens in a web browser. This has several advantages:

- **You build it with an LLM coding assistant** — reinforcing the prompt engineering skills from this course
- **It looks great** — web-based slides can have beautiful typography, animations, and layouts
- **It's a learning experience** — you'll get hands-on practice writing structured content with AI help
- **It's portable** — works on any computer with a web browser, no special software needed

You don't need to know HTML or CSS. Your LLM assistant will write the code for you. Your job is to describe what you want, review what it produces, and refine it.

---

## Getting Started

### Option 1: Use the template (recommended for beginners)

1. Download or copy the [presentation template](presentation-template/)
2. Open the folder in VS Code
3. Open `index.html` — this is your slide
4. Right-click `index.html` in VS Code and select "Open with Live Server" (if you have the Live Server extension) or open it directly in your browser (File → Open File)
5. You should see a working slide with the Macquarie University theme

The template is a starting point — you can change everything about it. Different colours, different layout, different fonts. It's yours to customise however you like.

### Option 2: Start from scratch with your LLM

If you'd prefer to build from scratch, ask your LLM assistant:

> "Create a single reveal.js HTML slide for a 3-minute research presentation. Use the reveal.js CDN (version 5.1.0). The slide should have a title, author name, and space for 4 content areas: research question, methods, key findings, and one limitation. Use a clean, professional design. Include all CSS inline in a `<style>` tag."

---

## The Template Structure

The template has this file structure:

```
presentation-template/
├── index.html              # Your slide — edit this file
└── css/
    └── mq-theme.css        # Macquarie University theme (optional to use)
```

The `index.html` file loads reveal.js from a CDN (no installation needed) and contains your slide content between `<div class="slides">` tags.

---

## Customising Your Slide

Ask your LLM assistant to help you customise the slide. Here are some example prompts:

**Changing content:**
> "Replace the placeholder text in my reveal.js slide with: Title: 'Predicting Depression from Smartphone Data'. Author: 'Jane Smith'. Research question: 'Can passive sensor data predict depressive episodes?'"

**Changing colours:**
> "Change the colour scheme of my reveal.js slide from red to blue. Keep the same layout."

**Adding a figure:**
> "I want to include a small image (results_figure.png) on the right side of my slide, with the text content on the left. Show me how to do this in reveal.js."

**Changing layout:**
> "Reorganise my slide so the 4 content areas (research question, methods, findings, limitation) are in a 2×2 grid instead of a vertical list."

**Adding visual elements:**
> "Add a coloured callout box around the 'Key Finding' section to make it stand out."

---

## Tips for a Good Slide

- **Keep text minimal.** Your slide supports your talk — it doesn't replace it. Use keywords and short phrases, not full sentences.
- **One slide, four key points.** Research question, methods, findings, limitation — each in a clearly labelled section.
- **Large font sizes.** Text should be readable from the back of the room. If you have to squint, the font is too small.
- **Use visual hierarchy.** Make the most important information the largest and most prominent.
- **Include your name and paper reference.** A small citation at the bottom of the slide is fine.

---

## Previewing Your Slide

### In a browser

Double-click the `index.html` file, or right-click → Open With → your browser. The slide will display full-screen.

### With Live Server (VS Code extension)

1. Install the "Live Server" extension in VS Code
2. Right-click `index.html` → "Open with Live Server"
3. The slide opens in your browser and automatically refreshes when you save changes

---

## Exporting to PDF

You need to submit your slide as a PDF. Here's how:

### Method 1: Browser Print (easiest)

1. Open your slide in Chrome or Edge
2. Add `?print-pdf` to the end of the URL (e.g., `file:///path/to/index.html?print-pdf`)
3. Press Cmd+P (Mac) or Ctrl+P (Windows) to open the Print dialog
4. Change "Destination" to **Save as PDF**
5. Set "Layout" to **Landscape**
6. Click **Save**

### Method 2: Screenshot

1. Open your slide in the browser
2. Press F11 for full-screen (or Cmd+Shift+F on Mac)
3. Take a screenshot (Cmd+Shift+3 on Mac, Win+Print Screen on Windows)
4. Paste into a document and save as PDF

### Method 3: Ask your LLM

> "How do I export a reveal.js presentation to PDF? I'm using Chrome on [Mac/Windows]."

---

## Submission

1. Export your slide as a PDF (see above)
2. Name it: `[Lastname]_[Firstname]_Presentation.pdf`
3. Upload to the iLearn submission portal **before** your presentation session

---

## Troubleshooting

**Slide is blank when I open index.html:**
- Check that you haven't accidentally deleted the `<div class="slides">` content
- Make sure the reveal.js CDN links are correct (the template has them pre-configured)
- Try opening in Chrome or Edge instead of Safari

**Fonts or styles look wrong:**
- The template uses Google Fonts loaded from the internet — make sure you're online
- If you changed the CSS, ask your LLM to check for syntax errors

**PDF export doesn't look right:**
- Make sure you added `?print-pdf` to the URL before printing
- Set the page size to landscape and margins to "None" or "Minimum"
- Try the screenshot method as a fallback

---

*[Back to resources](README.md) · [Back to course overview](../README.md)*

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

You can use **any AI tools you like** to create your slide — you are not limited to VS Code. Pick whichever approach feels most comfortable.

### Option 1: Use a browser chatbot (easiest — no setup required)

This is the simplest approach. You don't need VS Code or any special software — just a web browser and a chatbot.

1. Open <a href="https://chat.openai.com" target="_blank">ChatGPT</a>, <a href="https://gemini.google.com" target="_blank">Gemini</a>, or <a href="https://claude.ai" target="_blank">Claude</a> in your browser
2. Ask it to create your slide (see the example prompt below)
3. The chatbot will generate HTML code — copy it all and paste it into a new text file
4. Save the file as an `.html` file (make sure it ends in `.html`, not `.txt`)
5. Double-click the file to open it in your browser — you should see your slide
6. To make changes, go back to your chatbot, paste the code, and ask for what you want changed

> **Example prompt:** "Create a single reveal.js HTML slide for a 3-minute research presentation. Use the reveal.js CDN (version 5.1.0). The slide should have a title, author name, and space for 4 content areas: research question, methods, key findings, and one limitation. Use a clean, professional design. Include all CSS inline in a `<style>` tag so the entire slide is in one HTML file."

### Option 2: Use the course template

1. Download or copy the [presentation template](presentation-template/)
2. Open the folder — `index.html` is your slide file
3. Open the folder in VS Code (or any text editor — even Notepad works)
4. Open your HTML file — this is your slide
5. Open it in your browser to preview (double-click the file, or in VS Code: right-click → "Open with Live Server" if you have the extension)
6. Ask your LLM assistant (Copilot Chat, ChatGPT, Claude, etc.) to help you customise it

The template is a starting point — you can change everything about it. Different colours, different layout, different fonts. It's yours to customise however you like.

### Option 3: Start from scratch in VS Code

If you'd prefer full control, create a new file in VS Code and use your LLM assistant (Copilot Chat or any chatbot) to build the HTML from scratch. The example prompt from Option 1 works here too.

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

**Double-click** your HTML file — it will open in your default browser and display the slide. That's it.

If you're using VS Code and want auto-refresh (the slide updates every time you save), install the "Live Server" extension, then right-click your file → "Open with Live Server".

---

## Exporting to PDF

For the formal Paper Presentation assessment, you need to submit a PDF version of your slide via iLearn (in addition to the emailed zip). Here's how to export:

### Method 1: Browser Print (easiest)

1. Open your slide in Chrome or Edge
2. Add `?print-pdf` to the end of the URL (e.g., `file:///path/to/Jane_Smith.html?print-pdf`)
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

### Step 1: Organise your files into a folder

Create a folder containing everything your slide needs to work:

- Your HTML file
- The `css/` folder (if you used the course template or a separate CSS file)
- Any images you included in your slide

**Folder naming:**

- **Paper presentations (individual):** `Lastname_Firstname_WeekN` (e.g., `Smith_Jane_Week4`)
- **Challenge lab presentations (group):** `GroupN_WeekN` (e.g., `Group3_Week2`)

### Step 2: Zip the folder

Right-click the folder → **Compress** (Mac) or **Send to → Compressed (zipped) folder** (Windows).

**Always zip your folder** — MQ email will reject standalone HTML file attachments.

### Step 3: Email the zip file

Email the zip file to **michael.j.richardson@mq.edu.au**.

**Paper presentations:**
- Subject line: `PSYC4411 Presentation - Lastname Firstname - Week N` (e.g., `PSYC4411 Presentation - Smith Jane - Week 4`)
- **Deadline:** 12pm (noon) on the Monday of your presentation week

**Challenge lab presentations:**
- Subject line: `PSYC4411 Challenge Lab - Group N - Week N` (e.g., `PSYC4411 Challenge Lab - Group 3 - Week 2`)
- Only **one group member** needs to send the email
- **Deadline:** 12pm (noon) on the Monday you present (the week after the challenge lab)

### Step 4: Submit PDF via iLearn (paper presentations only)

For the formal Paper Presentation assessment (Weeks 4, 6, 8, 10), you also need to submit a **PDF** via iLearn:

1. Export your slide as a PDF (see Exporting to PDF above)
2. Name it: `Lastname_Firstname_Presentation.pdf`
3. Upload to the iLearn submission portal **before** your presentation session

Challenge lab presentations do not require a PDF submission — just the emailed zip.

### Testing before you send

**Test before sending:** Email the zip to yourself first. Download it, unzip it, open the folder and double-click your HTML file — it should display in your browser exactly as you expect. If something looks wrong (missing styles, broken images), you're probably missing a file in the folder. Fix it, re-zip, and send.

---

## Troubleshooting

**Slide is blank when I open the HTML file:**
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

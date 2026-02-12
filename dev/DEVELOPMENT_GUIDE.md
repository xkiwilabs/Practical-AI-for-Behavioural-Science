# Development Guide

This document outlines the structure, conventions, and workflow for building out weekly course materials. Refer back to this when creating content for any new week.

---

## Repo Structure

```
Current-Advances-in-Psychological-Methods-and-Analyses-Repo/
├── README.md                      # Course overview + weekly links table
├── .gitignore                     # Excludes .pptx, __pycache__, .DS_Store, etc.
├── setup/
│   └── getting-started.md         # Student setup guide (Python, Jupyter, VS Code)
├── weeks/
│   ├── week-01-lecture/           # Lecture weeks
│   │   ├── README.md              # Companion reading
│   │   ├── readings.md            # Optional/suggested readings
│   │   └── slides/                # reveal.js slide deck
│   │       ├── index.html         # The slide deck (HTML)
│   │       ├── css/mq-theme.css   # Shared MQ theme (copy from Week 1)
│   │       └── figures/           # Placeholder images for manual screenshots
│   ├── week-02-lab/               # Challenge lab weeks
│   │   ├── README.md              # Challenge brief
│   │   ├── starter.ipynb          # Starter notebook with scaffolding
│   │   └── data/                  # Datasets for the challenge
│   ├── week-11-lecture-lab/       # Hybrid week (both lecture + challenge)
│   ├── week-12-viva-review/       # Study guide + practice questions
│   └── week-13-discussion/        # Discussion prompts + reflection
├── data/                          # Shared datasets (used across weeks)
├── iLearnMaterials/               # HTML files for iLearn LMS (not weekly content)
└── dev/                           # Development files (not student-facing)
    ├── DEVELOPMENT_GUIDE.md       # This file — development conventions
    ├── _templates/                # Templates for new weeks
    │   ├── lecture-week.md
    │   └── challenge-lab.md
    └── .archive/                  # Archived drafts and earlier versions
```

---

## Branching Strategy

- **`main`** — Student-facing content. Everything here is visible to students.
- **`solutions`** — Solution notebooks for challenges. Merge into main after each challenge presentation week to reveal solutions.

---

## Class Session Timing

Each class session is **2 hours** (Mondays 3–5pm), but content does not fill the full 2 hours. Budget time as follows:

### Lecture Weeks (Weeks 1, 3, 5, 7, 9, 11)

| Activity | Duration | Notes |
|----------|----------|-------|
| Student presentations + Q&A | ~30 min | Pairs present previous lab challenge results |
| Lecture | ~60 min | Core content delivery |
| Buffer / questions / wrap-up | ~30 min | Organic discussion, preview of next lab |

**Exception — Week 1:** No student presentations (it's the first week). Budget ~1.5 hours for the introductory lecture, plus ~30 minutes going over the class structure, assessment, tools, and expectations.

### Lab Weeks (Weeks 2, 4, 6, 8, 10)

| Activity | Duration | Notes |
|----------|----------|-------|
| Challenge briefing | ~15 min | Instructor walks through the brief and dataset |
| Hands-on lab time | ~90 min | Students work on challenge (with LLM assistants) |
| Wrap-up + next steps | ~15 min | What to finish before next week's presentation |

### Implications for Content Scope

- **Companion readings** should cover what can realistically be taught in ~60 minutes of lecture (not 2 hours).
- **Challenge labs** should be achievable in ~90 minutes of focused work, with stretch goals for fast students.
- **Slide decks** should target roughly 40–50 content slides for a 60-minute lecture (some slides are quick, some need discussion).
- **Week 1 slides** can be larger (~60–70 slides) given the extended lecture time.

---

## Building a Lecture Week

Use `dev/_templates/lecture-week.md` as the starting point for `weeks/week-NN-lecture/README.md`.

### Checklist

1. **README.md** — Companion reading covering lecture topics in detail
   - Overview (2-3 sentences: what and why)
   - Key Concepts (explained with psychology-relevant examples)
   - **"Think about it" discussion prompts** — 3-4 per lecture week (see below)
   - Research examples with DOI-linked references
   - Common Misconceptions
   - Connections to Psychology
   - Link to `readings.md`

2. **readings.md** — Suggested and optional readings
   - 1-2 suggested readings (accessible, foundational)
   - 2-4 optional readings (deeper dives, applied examples)
   - Use APA format, include DOI links
   - Note open access availability (PMC, arXiv, author site)

3. **slides/** — reveal.js HTML slide deck (see "Building Slide Decks" below)
   - `index.html` — all slides in one HTML file
   - `css/mq-theme.css` — MQ-branded theme (copy from Week 1, do not modify)
   - `figures/` — placeholder images for screenshots/photos to be added manually

**Note:** There is no `examples/` or `scripts/` folder for lecture weeks. All diagrams (flow charts, hierarchies, timelines, Venn diagrams, comparisons) are built as HTML/CSS directly in the slides — not generated as PNGs. This keeps diagrams editable, animatable with fragments, and consistent with the theme.

### "Think About It" Discussion Prompts

Each lecture week's companion reading should include **3–4 discussion prompts** embedded at natural pause points. These are designed for the instructor to use during the live lecture as 2–3 minute class discussions.

**Format:** Use a blockquote with bold label:
```markdown
> **Think about it:** Your question here?
```

**Guidelines:**
- Place them *after* the concept they relate to, not before — the student needs the context first
- Focus on genuine tensions, open questions, or human-vs-AI contrasts — not factual recall
- Good prompts don't have a single right answer; they invite debate and multiple perspectives
- Prefer questions that connect the technical content to psychology, cognition, or research practice
- Aim for questions that honours students can engage with using their existing knowledge — they shouldn't need ML expertise to have a thoughtful opinion

**Themes that work well:**
- Differences between human cognition and artificial intelligence (e.g., data efficiency, embodied knowledge, understanding vs. pattern matching)
- Ethical tensions in applying ML to human behaviour
- When is a method useful vs. when is it misleading?
- What does "understanding" mean in the context of prediction?

**Example (from Week 1):**
> **Think about it:** Why do you think a toddler can learn "dog" from a few examples while an ML model needs thousands? What does the human bring to the task that the model doesn't?

---

## Building a Challenge Lab Week

Use `dev/_templates/challenge-lab.md` as the starting point for `weeks/week-NN-lab/README.md`.

### Checklist

1. **README.md** — Challenge brief
   - The Challenge (clear goal statement)
   - Background (what lecture concept is being applied)
   - Dataset description (what's in `data/`, what each variable means)
   - Getting Started (suggested steps, useful LLM prompts, starter code reference)
   - What to Present (1 slide, what to include)
   - Hints (collapsible spoiler sections)

2. **starter.ipynb** — Scaffolded Jupyter notebook
   - Import cells with standard libraries
   - Data loading cell
   - Exploratory prompts (e.g., "What does this data look like?")
   - Placeholder cells for each major step
   - Should run without errors up to the point where students take over

3. **data/** — Challenge dataset(s)
   - CSV or JSON format preferred
   - Include a brief data dictionary in the README or as a separate `data_dictionary.md`
   - Keep datasets small enough for GitHub (<50MB)

4. **Solution notebook** (on `solutions` branch only)
   - Complete worked solution
   - Include commentary explaining choices
   - Name: `solution.ipynb`

---

## Building Slide Decks

Slides are built as **reveal.js HTML decks** — no PowerPoint, no build step, no Python figure scripts. Each lecture week has a self-contained `slides/` folder with an `index.html`, a shared CSS theme, and a `figures/` directory for placeholder images only.

All diagrams (flow charts, hierarchies, timelines, Venn diagrams, comparisons) are built as **HTML/CSS directly in the slides**, not generated as PNG images. This means diagrams can be animated with `fragment` classes, styled consistently with the theme, and edited without re-running scripts.

### Workflow: README → Readings → Slides → Iterate

1. **Write the README.md first.** The companion reading defines the content, structure, research examples, and "Think about it" prompts. The slide deck is a visual presentation of this content — not the other way around.
2. **Write readings.md.** Verify all references via web search, confirm DOIs resolve, check for open access versions. Every paper cited in the slides must also appear in readings.md.
3. **Build the slide deck** from the README. Each major section of the reading maps to a section in the slides. Convert diagrams to HTML/CSS, add fragment animations, and link all cited papers to their DOIs.
4. **Iterate.** Open `index.html` in a browser, step through every slide and fragment, adjust text density, timing, and visuals. Refine both the slides and the README together.

### Slide Deck Structure

Every lecture deck follows this template structure:

```
slides/
├── index.html          # The deck — all slides in one file
├── css/
│   └── mq-theme.css    # MQ-branded theme (copy from Week 1, do not modify)
└── figures/
    └── slide##_fig##_placeholder.png  # Placeholders for manual screenshots/photos
```

**No `scripts/` or `examples/` folders** are needed for lecture weeks. If a future week requires a live code demo, use a Jupyter notebook in the lab week instead.

### index.html Template

The HTML file loads reveal.js and plugins from CDN (no local install needed):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Week N: Title — PSYC4411</title>

  <!-- reveal.js core CSS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/theme/white.css" id="theme">

  <!-- Phosphor Icons -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.1/src/regular/style.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.1/src/bold/style.css">

  <!-- MQ custom theme -->
  <link rel="stylesheet" href="css/mq-theme.css">
</head>
<body>
<div class="reveal">
<div class="slides">

  <!-- SLIDES GO HERE -->

</div></div>

<!-- reveal.js core + plugins -->
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.js"></script>
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/plugin/notes/notes.js"></script>

<script>
  // See Week 1 for the full config including nav bar and clock
  Reveal.initialize({ ... });
</script>
</body>
</html>
```

Copy the full `<script>` block from Week 1's `index.html` — it includes the Reveal config, the custom navigation bar builder, and the live clock.

### Reveal.js Configuration

Key settings (defined in the `Reveal.initialize()` call):

| Setting | Value | Purpose |
|---------|-------|---------|
| `width` / `height` | 1920 / 1080 | 16:9 widescreen design dimensions |
| `margin` | 0 | Full-bleed slides |
| `center` | false | Content starts from the top, not vertically centred |
| `controls` | true | Forward/back arrows visible |
| `controlsLayout` | 'edges' | Arrows at far left/right edges of the slide |
| `slideNumber` | false | Disabled — replaced by custom nav bar |
| `progress` | false | Disabled — replaced by custom nav bar |
| `transition` | 'slide' | Horizontal slide transition |
| `hash` | true | URL updates with slide number for direct linking |

### Custom Features (built in JS, appended after `Reveal.initialize()`)

These are included in the Week 1 script block. Copy them into every deck:

- **Slide navigation bar** — thin bar at the bottom of every slide. Shows progress (red tint for visited slides, solid red for current). On hover, expands to show numbered pills with slide-title tooltips. Click to jump.
- **Live clock** — top-right corner, 12-hour format, updates every 15 seconds. Adapts colour for dark-background slides.

### Slide Types and CSS Classes

The MQ theme (`mq-theme.css`) defines these slide types. Use the appropriate class on the `<section>` element.

| Class | Background | Use |
|-------|-----------|-----|
| `.title-slide` | Dark gradient (via `data-background-gradient`) | First slide only — title, subtitle, instructor info |
| `.section-divider` | MQ red gradient (via `data-background-gradient`) | Section breaks between major topics |
| `.think-slide` | Dark navy gradient (via `data-background-gradient`) | "Think about it" discussion prompts |
| `.end-slide` | Dark gradient (via `data-background-gradient`) | Final "Questions?" slide |
| `.image-full` | White | Centred image with caption |
| *(no class)* | White | Standard content slides |

**Important:** Dark-background slides use `data-background-gradient` on the `<section>` tag, not CSS `background`. This is required for reveal.js to render the gradient full-viewport behind the content.

```html
<!-- Section divider example -->
<section class="section-divider" data-background-gradient="linear-gradient(135deg, #A71930 0%, #8B1428 100%)">
  <div class="section-icon"><i class="ph-bold ph-brain"></i></div>
  <h2>Section Title</h2>
  <p>Subtitle text</p>
</section>

<!-- Think about it example -->
<section class="think-slide" data-background-gradient="linear-gradient(135deg, #1A1A2E 0%, #16213E 100%)">
  <h2><i class="ph-bold ph-lightbulb"></i> Think About It</h2>
  <div class="spacer-lg"></div>
  <p>Your discussion question here?</p>
</section>
```

### Background Gradients Reference

| Slide type | `data-background-gradient` value |
|------------|----------------------------------|
| Title slide | `linear-gradient(135deg, #1A1A2E 0%, #16213E 50%, #8B1428 100%)` |
| Section divider | `linear-gradient(135deg, #A71930 0%, #8B1428 100%)` |
| Think-about-it | `linear-gradient(135deg, #1A1A2E 0%, #16213E 100%)` |
| End slide | `linear-gradient(135deg, #1A1A2E 0%, #16213E 50%, #8B1428 100%)` |

### Layout Classes

| Class | Description |
|-------|-------------|
| `.two-col` | Equal two-column grid (50/50) |
| `.two-col-wide-left` | Two-column grid, left wider (65/35) |
| `.two-col-wide-right` | Two-column grid, right wider (35/65) |
| `.three-col` | Equal three-column grid |
| `.col` | Column container (child of the grid classes above) |

### Content Component Classes

| Class | Description |
|-------|-------------|
| `.highlight-box` | Red-accented callout box (left border) |
| `.info-box` | Blue-accented callout box (left border) |
| `.key-insight` | Gold-accented callout box (left border) |
| `.tag` + `.tag-red` / `.tag-blue` / etc. | Inline coloured pill badges |
| `.prompt-bad` | Red-bordered monospace box for "vague" prompt examples |
| `.prompt-good` | Green-bordered monospace box for "specific" prompt examples |
| `.tool-grid` | 2×2 grid of tool/feature cards |
| `.tool-card` | Individual card within `.tool-grid` |
| `.small` | Smaller, grey text for annotations and attributions |
| `.spacer` | 12px vertical gap |
| `.spacer-lg` | 24px vertical gap |

### HTML Diagram Classes

Prefer HTML/CSS diagrams over static images for flow charts, hierarchies, comparisons, and timelines — they animate with fragments, are easy to edit, and scale cleanly.

| Class | Description |
|-------|-------------|
| `.hierarchy-diagram` / `.hierarchy-layer` | Nested box diagram (e.g., AI → ML → DL → GenAI) |
| `.flow-diagram` / `.flow-step` / `.flow-arrow` | Horizontal step-by-step flow chart |
| `.compare-diagram` / `.compare-side` / `.compare-box` | Side-by-side comparison (e.g., traditional vs ML) |
| `.venn-container` / `.venn-circle` / `.venn-overlap` | Two-circle Venn diagram |
| `.timeline` / `.timeline-event` / `.timeline-dot` / `.timeline-year` / `.timeline-text` | Horizontal timeline with coloured dots |

### Coloured Bullet Classes

Match bullet marker colour to a diagram element:

```html
<li class="fragment bullet-blue">Blue-bulleted text</li>
<li class="fragment bullet-red">Red-bulleted text</li>
```

Available: `.bullet-blue`, `.bullet-orange`, `.bullet-grey`, `.bullet-green`, `.bullet-red`, `.bullet-purple`.

Use `.timeline-bullets` on the `<ul>` for extra vertical spacing between items.

### Flow Diagram Cycle-Back Arrows

For loops (outer loop, inner loop), add a right-angle SVG return arrow beneath the flow diagram. The arrow goes down from the last step, across horizontally, and back up into the first step:

```html
<div class="flow-cycle fragment" style="height: 44px;">
  <svg width="720" height="44" viewBox="0 0 720 44" fill="none" xmlns="http://www.w3.org/2000/svg"
       style="display: block; margin: 0 auto;">
    <!-- Right-angle path: down from last step, across, up into first step -->
    <path d="M660 2 V32 H60 V14" stroke="#8C8C8C" stroke-width="2.5"
          stroke-dasharray="6 4" fill="none" stroke-linejoin="round"/>
    <!-- Upward arrowhead -->
    <polygon points="60,6 53,16 67,16" fill="#8C8C8C"/>
    <!-- Label on horizontal segment -->
    <text x="360" y="28" text-anchor="middle" font-family="Inter, sans-serif"
          font-size="13" font-weight="500" fill="#8C8C8C">label text here</text>
  </svg>
</div>
```

Adjust `width`, `M`/`V`/`H` coordinates, and arrowhead position to match the flow diagram width.

### Fragment Animations

Use `class="fragment"` on any element to reveal it on click/keypress. Use `data-fragment-index="N"` to synchronise multiple elements appearing together (e.g., a timeline dot and its matching bullet point):

```html
<!-- These appear together -->
<div class="timeline-event fragment" data-fragment-index="0"> ... </div>
<li class="fragment bullet-blue" data-fragment-index="0">Matching text</li>
```

### Placeholder Images

The only PNGs in `slides/figures/` should be **placeholders for screenshots and photos** that need to be added manually (e.g., app screenshots, research figure reproductions, photos). All diagrams are HTML/CSS.

- File name: `slide##_fig##_placeholder.png` (e.g., `slide19_fig01_placeholder.png`)
- Use any 800×600 grey rectangle image as the placeholder
- Reference in HTML with a descriptive `alt` tag and a `<p class="small">Replace with: description</p>` caption
- Once real images are available, replace the placeholder file and remove the caption

### Citing References in Slides

Every journal article or book cited in the slides must include a hyperlink:

- **Author names** should be wrapped in an `<a>` tag linking to the paper
- **Journal line** (e.g., "Published in Nature, 2023") should also link to the paper
- Link to the **DOI URL** (e.g., `https://doi.org/10.xxxx/xxxxx`) as the primary link — this is permanent and resolves to the publisher
- If the paper is **open access**, note this (e.g., "Open access") after the journal link
- If the paper is behind a paywall but has an **open preprint** (e.g., arXiv, PsyArXiv, PMC), add a second link to the free version
- Always use `target="_blank"` so links open in a new tab

Example:
```html
<li><a href="https://doi.org/10.1038/s41598-023-31807-1" target="_blank">Auletta et al. (2023)</a> used LSTM networks...</li>
...
<p class="small"><em>Published in <a href="https://doi.org/10.1038/s41598-023-31807-1" target="_blank">Scientific Reports, 2023</a></em> · Open access</p>
```

Before including any reference, verify via web search that the DOI resolves correctly and check whether an open access version exists. See `.claude/CLAUDE.md` for full reference verification rules.

### Icons

Use [Phosphor Icons](https://phosphoricons.com/) (loaded via CDN). Two weights available:

- Regular: `<i class="ph ph-icon-name"></i>`
- Bold: `<i class="ph-bold ph-icon-name"></i>`

Common icons used in slides: `ph-brain`, `ph-lightbulb`, `ph-code`, `ph-flask`, `ph-robot`, `ph-chart-line-up`, `ph-chats-circle`, `ph-toolbox`, `ph-arrows-clockwise`, `ph-rocket-launch`, `ph-warning`, `ph-microphone`, `ph-pencil-line`, `ph-presentation-chart`, `ph-gear`, `ph-hand-waving`.

### Typical Section Structure (per lecture)

Each major topic in the lecture follows this pattern in the HTML:

```
1. Section divider slide (dark red background, icon, title)
2. Definition / overview slide (highlight-box with key definition)
3. 2–4 content slides (bullet points with fragments, examples, diagrams)
4. "Think about it" slide (dark navy background, discussion question)
```

### Slide Count Guidelines

| Week type | Target slides | Notes |
|-----------|--------------|-------|
| Week 1 | ~60 | Extended lecture time (no student presentations) |
| Standard lecture (Weeks 3, 5, 7, 9) | 40–50 | ~60 min lecture time |
| Week 11 (hybrid) | 30–40 | Split between lecture and lab |

These include section dividers, think-about-it slides, and the assessment/homework slides. Some slides advance quickly (section dividers); others need 2–3 minutes of discussion.

### Checklist: New Lecture Week (end-to-end)

**Content first:**
- [ ] Write `README.md` — companion reading with key concepts, research examples, "Think about it" prompts
- [ ] Write `readings.md` — verify all DOIs, check open access, APA 7th format
- [ ] Ensure every paper cited in the README has a DOI hyperlink

**Build the slide deck:**
- [ ] Create `slides/` folder: copy `css/mq-theme.css` unchanged from Week 1
- [ ] Create `index.html` — copy the HTML template and full `<script>` block from Week 1 (config + nav bar + clock)
- [ ] Update `<title>` to "Week N: Title — PSYC4411"
- [ ] Update the title slide (week number, subtitle, keep instructor info)
- [ ] Build section dividers for each major topic from the README
- [ ] Build content slides from the README sections
- [ ] Build all diagrams as HTML/CSS (not PNG images) — flow charts, hierarchies, timelines, Venn diagrams, comparisons
- [ ] Add "Think about it" slides matching the README discussion prompts
- [ ] Add fragment animations to all bullet points and diagram elements
- [ ] Link all cited papers to their DOIs with `target="_blank"`
- [ ] Add placeholder images only for screenshots/photos not yet available
- [ ] Test: open in browser, step through every slide and fragment
- [ ] Check text density: slides should feel full (not cramped, not empty)
- [ ] Australian English throughout (behaviour, generalisation, colour, etc.)
- [ ] No `scripts/` or `examples/` folders needed for lecture weeks

---

## Conventions

### File Naming
- Folders: `week-NN-type` (e.g., `week-03-lecture`, `week-04-lab`)
- Notebooks: lowercase, hyphens, descriptive (e.g., `01_ridge_lasso_demo.ipynb`)
- Data files: lowercase, underscores (e.g., `personality_survey.csv`)

### Writing Style (for student-facing .md files)
- Write for 4th-year psychology students with no coding/ML background
- Explain jargon the first time it appears
- Use concrete psychology examples (not abstract math)
- Keep companion readings around 1000-2000 words
- Use collapsible sections for hints and optional depth

### Code Style
- Python 3.10+
- Use standard data science stack: pandas, numpy, matplotlib, seaborn, scikit-learn, torch
- Include inline comments for non-obvious steps
- Prefer clarity over cleverness
- All notebooks should run top-to-bottom without errors

### LLM Prompts (in challenge briefs)
- Provide 2-3 starter prompts students can use with their LLM assistant
- Frame prompts as questions, not instructions (teaches good prompting)
- Example: "I have a CSV with columns X, Y, Z. How would I build a simple linear regression to predict Y from X and Z using scikit-learn?"

---

## Weekly Content Summary

| Week | Type | Topic | Key Deliverables |
|------|------|-------|------------------|
| 1 | Lecture | ML in Psychological Science | Companion reading, slide deck, readings |
| 2 | Lab | Setup + LLM Problem-Solving Loop | Starter notebook, challenge brief, dataset |
| 3 | Lecture | Generalisation & Overfitting | Companion reading, slide deck, train/test demo |
| 4 | Lab | Regression Pipeline | Starter notebook, challenge brief, dataset |
| 5 | Lecture | Classification & Evaluation | Companion reading, slide deck, metrics examples |
| 6 | Lab | Trees & Ensembles | Starter notebook, challenge brief, dataset |
| 7 | Lecture | Clustering & Dim. Reduction | Companion reading, slide deck, clustering demos |
| 8 | Lab | PCA/UMAP & Clustering | Starter notebook, challenge brief, dataset |
| 9 | Lecture | Neural Networks | Companion reading, slide deck, MLP examples |
| 10 | Lab | Neural Network Training | Starter notebook, challenge brief, dataset |
| 11 | Hybrid | Embeddings & LLMs | Companion reading, slide deck, challenge, dataset |
| 12 | Review | Viva Preparation | Study guide, concept list, practice Qs |
| 13 | Discussion | Ethics & Reflection | Discussion prompts |

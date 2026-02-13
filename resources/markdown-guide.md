# Markdown Guide

Markdown is a lightweight way to format text. You'll use it in Jupyter notebook text cells, GitHub READMEs, and anywhere you need formatted text without a word processor. This guide covers everything you need.

---

## What Is Markdown?

Markdown is a way to write formatted text using plain characters. Instead of clicking a "Bold" button like in Word, you type `**bold text**` and it renders as **bold text**. It's used everywhere in the tech world — GitHub, Jupyter, documentation, chat platforms, and more.

---

## Headings

Use `#` symbols at the start of a line. More `#` = smaller heading.

```markdown
# Heading 1 (largest)
## Heading 2
### Heading 3
#### Heading 4
```

---

## Text Formatting

```markdown
**bold text**
*italic text*
***bold and italic***
~~strikethrough~~
`inline code`
```

Renders as: **bold text**, *italic text*, ***bold and italic***, ~~strikethrough~~, `inline code`

---

## Lists

### Unordered (bullet) lists

```markdown
- First item
- Second item
  - Sub-item (indent with 2 spaces)
  - Another sub-item
- Third item
```

### Ordered (numbered) lists

```markdown
1. First step
2. Second step
3. Third step
```

---

## Links

```markdown
[Link text](https://example.com)
```

Example: `[Macquarie University](https://www.mq.edu.au)` renders as [Macquarie University](https://www.mq.edu.au)

To open links in a new tab (useful in GitHub READMEs), use HTML:

```html
<a href="https://example.com" target="_blank">Link text</a>
```

---

## Images

```markdown
![Alt text](path/to/image.png)
```

The alt text describes the image for accessibility. The path can be a relative file path or a URL.

---

## Code

### Inline code

Use backticks for short code references within text:

```markdown
Use the `print()` function to display output.
```

### Code blocks

Use triple backticks for multi-line code. Add the language name for syntax highlighting:

````markdown
```python
import pandas as pd
data = pd.read_csv("my_data.csv")
print(data.head())
```
````

---

## Tables

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Row 1    | Data     | More     |
| Row 2    | Data     | More     |
```

Renders as:

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Row 1    | Data     | More     |
| Row 2    | Data     | More     |

---

## Blockquotes

```markdown
> This is a blockquote. Use it for callouts or emphasis.
```

Renders as:

> This is a blockquote. Use it for callouts or emphasis.

---

## Horizontal Rules

Use three dashes to create a horizontal line:

```markdown
---
```

---

## Collapsible Sections

For content that should be hidden by default (like hints):

```markdown
<details>
<summary>Click to expand</summary>

Hidden content goes here. You can use **any Markdown formatting** inside.

</details>
```

<details>
<summary>Click to expand</summary>

Hidden content goes here. You can use **any Markdown formatting** inside.

</details>

---

## Cheat Sheet

| What you want | What you type | What you get |
|---------------|---------------|--------------|
| Bold | `**text**` | **text** |
| Italic | `*text*` | *text* |
| Inline code | `` `code` `` | `code` |
| Link | `[text](url)` | [text](url) |
| Image | `![alt](path)` | (image) |
| Heading 1 | `# Title` | Large heading |
| Heading 2 | `## Title` | Medium heading |
| Bullet list | `- item` | Bullet point |
| Numbered list | `1. item` | Numbered item |
| Blockquote | `> text` | Indented quote |
| Horizontal rule | `---` | Line across page |

---

## Where You'll Use Markdown

- **Jupyter notebooks:** Markdown cells for explanations, notes, and documentation
- **GitHub:** README files, issue comments, pull request descriptions
- **This course repo:** All companion readings and challenge briefs are written in Markdown

---

*[Back to resources](README.md) · [Back to course overview](../README.md)*

# LM Studio Guide — A Graphical Interface for Local AI Models

LM Studio is a desktop application that lets you download, manage, and chat with large language models (LLMs) on your own computer. Unlike Ollama (which runs from the terminal), LM Studio gives you a **graphical interface** — it looks and feels like using ChatGPT, but everything runs locally on your machine.

> **This is completely optional.** You do not need local models for this course. The cloud-based tools (Copilot, ChatGPT, Claude, Gemini) are more than enough. Local models are useful later in the course and in research when you're working with sensitive data that can't be sent to external servers, or when you want to experiment without usage limits.

---

## Do I Have Enough Hardware?

Local AI models need a lot of memory (RAM). See the [Ollama guide](ollama-guide.md#do-i-have-enough-hardware) for a detailed breakdown, but here's the quick version:

| Your RAM | What you can run |
|----------|-----------------|
| 8–16 GB | Small models only — limited usefulness |
| **32 GB** | **Medium models — minimum for useful results** |
| 64 GB+ | Large models — good quality and speed |
| 96–128 GB+ | Very large models — excellent quality |

**Best candidates for local models:**
- **Mac users** with Apple Silicon (M1 Pro/Max or newer) and 32GB+ unified memory
- **Mini PCs and desktops** with 96–128GB shared/unified memory (increasingly common and affordable)
- **Windows/Linux users** with NVIDIA GPUs that have 12GB+ VRAM

If your computer has 16GB or less, stick with cloud tools — they'll give you a much better experience.

---

## Installing LM Studio

1. Go to <a href="https://lmstudio.ai" target="_blank">lmstudio.ai</a>
2. Click **Download** and choose your platform (macOS, Windows, or Linux)
3. Install as you would any application:
   - **Mac:** Open the `.dmg` file and drag LM Studio to Applications
   - **Windows:** Run the installer and follow the prompts
4. Open LM Studio

---

## Downloading a Model

When you first open LM Studio, you'll need to download a model:

1. Click the **Discover** tab (magnifying glass icon) in the left sidebar
2. Search for a model — good starting points:
   - `Llama 3.2` — Meta's general-purpose model (various sizes)
   - `Qwen 2.5 Coder` — Excellent for code generation
   - `Phi 4` — Microsoft's efficient small model
   - `DeepSeek R1` — Strong at reasoning and maths
3. Each model shows its file size and the RAM needed to run it. **Pick one that fits your hardware** — LM Studio will highlight compatible models.
4. Click **Download** and wait for it to finish

**Tip:** LM Studio makes it easy to see which models will run well on your hardware. Models that are too large for your system will be flagged with a warning.

---

## Chatting with a Model

1. Click the **Chat** tab in the left sidebar
2. Select a downloaded model from the dropdown at the top
3. Type your message in the text box at the bottom and press Enter
4. The model will respond — just like ChatGPT, but running on your own computer

### Example Conversation

**You:** I have a dataset with columns Sleep_hrs_night and Depression. Write Python code using seaborn to create a scatter plot with a trend line.

**Model:** Here's the code to create a scatter plot with a trend line:

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.regplot(data=data, x="Sleep_hrs_night", y="Depression",
            scatter_kws={"alpha": 0.3}, line_kws={"color": "red"})
plt.title("Sleep vs Depression")
plt.show()
```

---

## Using LM Studio as a Local Server

LM Studio can run a local server that's compatible with the OpenAI API format. This means you can use it with Python code, VS Code extensions, and other tools — just point them at your local server instead of the OpenAI API.

### Start the server

1. Click the **Developer** tab in the left sidebar
2. Select a model from the dropdown
3. Click **Start Server**
4. The server will run at `http://localhost:1234`

### Use it from Python

```python
from openai import OpenAI

# Point the OpenAI client at your local LM Studio server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

response = client.chat.completions.create(
    model="local-model",
    messages=[
        {"role": "user", "content": "Explain linear regression in simple terms."}
    ]
)

print(response.choices[0].message.content)
```

This uses the same `openai` Python package you'd use for the real OpenAI API — just with a different base URL. That means code written for cloud APIs can often be switched to local models by changing one line.

### Use it with VS Code

Extensions like **Continue** (<a href="https://continue.dev" target="_blank">continue.dev</a>) can connect to LM Studio's local server, giving you AI coding assistance inside your editor using your own local models.

---

## LM Studio vs. Ollama — Which Should I Use?

Both are excellent tools for running local models. Here's how they compare:

| Feature | LM Studio | Ollama |
|---------|-----------|--------|
| **Interface** | Graphical (point and click) | Terminal (command line) |
| **Ease of use** | Easier for beginners | Requires comfort with the terminal |
| **Model browsing** | Built-in model discovery with hardware compatibility checks | Browse online, pull from terminal |
| **Chat interface** | Built-in, looks like ChatGPT | Terminal-based chat |
| **Local server** | Built-in, one-click | Built-in, runs automatically |
| **Python integration** | Via local server (OpenAI-compatible) | Via local server or `ollama` Python package |
| **Resource usage** | Heavier (GUI app) | Lighter (no GUI overhead) |
| **Automation** | Less suited for scripting | Great for scripting and automation |

**Our suggestion:** If you've never used the terminal before, start with **LM Studio** — it's more visual and intuitive. If you're comfortable with the terminal (or want to be), **Ollama** is lighter and more scriptable. You can install both and use whichever feels right for the task.

---

## Tips

- **Close other memory-heavy apps** before running models. Every GB of RAM matters.
- **Start with a smaller model** to check that everything works, then try larger ones.
- **First response is slow** — the model needs to load into memory. Subsequent responses are faster.
- **LM Studio remembers your conversations** — you can go back to previous chats, just like ChatGPT.
- **Check for updates regularly** — LM Studio is actively developed and new features are added often.

---

## Further Reading

- <a href="https://lmstudio.ai" target="_blank">LM Studio website</a>
- <a href="https://lmstudio.ai/docs" target="_blank">LM Studio documentation</a>

---

*[Back to resources](README.md) · [Back to course overview](../README.md)*

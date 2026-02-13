# Ollama Guide — Running AI Models on Your Own Computer

Ollama lets you download and run large language models (LLMs) directly on your own machine — no internet connection needed, no data sent to external servers. It's free, open-source, and works both from the terminal and through a built-in desktop chat interface.

> **This is completely optional.** You do not need local models for this course. The cloud-based tools (Copilot, ChatGPT, Claude, Gemini) are more than enough. Local models are useful later in the course and in research when you're working with sensitive data that can't be sent to external servers, or when you want to experiment without usage limits.

---

## Do I Have Enough Hardware?

Local AI models need a lot of memory (RAM). The model has to be loaded entirely into memory to run, so the size of the model you can use depends directly on how much memory your computer has.

**Here's a rough guide:**

| Your RAM | What you can run | Experience |
|----------|-----------------|------------|
| 8–16 GB | Small models only (1B–3B parameters) | Very limited — basic tasks, slow |
| **32 GB** | **Medium models (7B–14B parameters)** | **Minimum for useful results** |
| 64 GB | Large models (32B–70B parameters) | Good quality, comfortable speed |
| 96–128 GB+ | Very large models (70B+ parameters) | Excellent quality, approaching cloud AI |

**Who's most likely to have enough?**

- **Mac users with Apple Silicon** (M1 Pro/Max, M2, M3, M4 and their Pro/Max/Ultra variants) — These chips use **unified memory**, meaning the CPU and GPU share the same pool of RAM. A MacBook Pro with 32GB or 36GB of unified memory can run 7B–14B models well. Machines with 48GB, 64GB, or more can run even larger models comfortably.
- **Mini PCs and desktops with shared memory** — An increasing number of compact desktop computers (from brands like Minisforum, Beelink, and others) now ship with 96GB or 128GB of unified/shared memory. These are excellent for running local models.
- **NVIDIA DGX Spark and GB10-based systems** — The <a href="https://www.nvidia.com/en-us/products/workstations/dgx-spark/" target="_blank">NVIDIA DGX Spark</a> (formerly Project DIGITS) is a compact desktop powered by the GB10 Grace Blackwell Superchip with **128GB of unified memory** — purpose-built for running local AI models. It can handle models up to 200 billion parameters. Derivatives are available from <a href="https://www.dell.com/en-us/shop/desktop-computers/dell-pro-max-with-gb10/spd/dell-pro-max-fcm1253-micro" target="_blank">Dell</a>, <a href="https://ipc.msi.com/product_detail/Industrial-Computer-Box-PC/AI-Supercomputer/EdgeXpert-MS-C931" target="_blank">MSI</a>, Acer, ASUS, HP, and Lenovo. These run Ubuntu Linux and are an increasingly popular option for researchers who need serious local AI capability.
- **Windows/Linux with a dedicated GPU** — If you have an NVIDIA GPU with 8GB+ of VRAM, you can run smaller models on the GPU (which is faster than running on CPU alone). For larger models, you need more VRAM or the model will run on the CPU, which is much slower.
- **Linux (Ubuntu) users** — If you're running Ubuntu or another Linux distribution, you're in great company. Linux is the default operating system for most AI and machine learning infrastructure worldwide, and tools like Ollama, PyTorch, and CUDA run natively and often perform best on Linux. If you're curious about Linux but haven't tried it, it's worth exploring — many AI researchers use Ubuntu as their primary OS.
- **Most regular laptops (8–16GB RAM)** — Honestly, the experience won't be great. You can technically run very small models, but the quality and speed will be disappointing compared to cloud tools. If this is you, stick with the cloud tools — they're better for your setup.

**Not sure how much RAM you have?**
- **Mac:** Apple menu → About This Mac → look for "Memory" or "Unified Memory"
- **Windows:** Settings → System → About → look for "Installed RAM"

---

## Installing Ollama

### macOS

1. Go to <a href="https://ollama.com/download" target="_blank">ollama.com/download</a>
2. Click **Download for macOS**
3. Open the downloaded `.zip` file — it will unzip into an application called **Ollama**
4. Drag **Ollama** into your **Applications** folder
5. Open Ollama from Applications — it will add a small icon to your menu bar (top-right of your screen)

### Windows

1. Go to <a href="https://ollama.com/download" target="_blank">ollama.com/download</a>
2. Click **Download for Windows**
3. Run the downloaded installer and follow the prompts
4. Ollama will run in the background (you'll see a small icon in the system tray)

### Linux (Ubuntu)

Ollama has first-class Linux support — one command does everything:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

This installs Ollama and sets it up as a system service that starts automatically. It works on Ubuntu, Debian, Fedora, and most other distributions. If you have an NVIDIA GPU, the installer will detect it and configure GPU acceleration automatically (as long as NVIDIA drivers and CUDA are installed).

> **Why Linux?** Most AI and ML infrastructure runs on Linux. If you're exploring local models seriously — especially on hardware like the DGX Spark — Ubuntu is the native environment and where you'll get the best performance and compatibility.

### Verify it works

Open a terminal (Terminal on Mac, PowerShell on Windows) and type:

```
ollama --version
```

You should see a version number. If you get "command not found", close and reopen your terminal.

---

## Downloading Your First Model

Ollama doesn't come with any models — you download the ones you want. Here are some good starting points:

```bash
# A small, fast model — good for testing (needs 8GB+ RAM)
ollama pull qwen3:8b

# OpenAI's open-weight model — MoE, surprisingly capable (needs 16GB+ RAM)
ollama pull gpt-oss:20b

# A strong general-purpose model (needs 32GB+ RAM)
ollama pull qwen3:32b

# Multimodal (text + images), very capable (needs 64GB+ RAM)
ollama pull llama4:scout
```

The download will take a few minutes depending on your internet speed. Models are stored on your computer and only need to be downloaded once.

**To see what models you've downloaded:**

```bash
ollama list
```

---

## Using Ollama

### Chat in the terminal

The quickest way to use a model:

```bash
ollama run qwen3:8b
```

This opens a chat session. Type your message and press Enter. Type `/bye` to exit.

**Example:**

```
>>> Explain what a scatter plot is in one paragraph, for someone who has never seen one.

A scatter plot is a type of graph that shows the relationship between two
variables by placing dots on a grid. Each dot represents one observation —
for example, one person in a study. The position of the dot shows that
person's values on the two variables: one variable determines how far left
or right the dot goes, and the other determines how high or low...
```

### Chat with the desktop app

Ollama also comes with a **built-in desktop chat interface** (on macOS and Windows) that looks and feels similar to ChatGPT — but everything runs locally on your machine. It supports:

- **File drag-and-drop** — drop a PDF, text file, or code file into the chat for the model to reason about
- **Image inputs** — with compatible models (like Gemma 3), you can include images in your conversations
- **Adjustable context length** — increase the model's memory for processing larger documents

To use it, just open the Ollama app from your Applications folder (Mac) or Start menu (Windows). If you installed the CLI-only version, you can download the desktop app from <a href="https://ollama.com/download" target="_blank">ollama.com/download</a>.

### Use it with Python

Ollama runs a local server that you can call from Python, just like calling the OpenAI or Anthropic APIs — but everything stays on your machine:

```python
import requests

response = requests.post("http://localhost:11434/api/generate", json={
    "model": "qwen3:8b",
    "prompt": "Explain k-means clustering in simple terms.",
    "stream": False
})

print(response.json()["response"])
```

There's also an official Python library:

```bash
pip install ollama
```

```python
import ollama

response = ollama.chat(model="qwen3:8b", messages=[
    {"role": "user", "content": "Explain k-means clustering in simple terms."}
])

print(response["message"]["content"])
```

### Use it with VS Code

Several VS Code extensions can connect to Ollama, letting you use local models inside your editor:

- **Continue** (<a href="https://continue.dev" target="_blank">continue.dev</a>) — Open-source AI coding assistant that works with Ollama. Provides chat, autocomplete, and inline editing using your local models.
- **GitHub Copilot** — Copilot Chat supports connecting to Ollama as a model provider in some configurations.

---

## Recommended Models

> **This list will go out of date.** New open-source models are released almost every week, and the landscape changes fast. The models below were current as of February 2026. Always check the <a href="https://ollama.com/library" target="_blank">Ollama model library</a> for the latest, or ask your AI assistant: *"What are the best open-source models I can run locally right now?"*

Here are models that work well for coding and data science tasks, organised by how much RAM you need:

### Fits in 8–16 GB RAM

| Model | Download | Good for |
|-------|----------|----------|
| **Qwen 3 (8B)** | `ollama pull qwen3:8b` | Strong general-purpose and coding — great starter model |
| **Qwen 3 (4B)** | `ollama pull qwen3:4b` | Lighter option for 8GB machines |
| **GPT-OSS (20B)** | `ollama pull gpt-oss:20b` | OpenAI's open-weight model. MoE architecture (only 3.6B parameters active per query), so it runs fast and fits in 16GB despite being 20B total |

### Fits in 32 GB RAM

| Model | Download | Good for |
|-------|----------|----------|
| **Qwen 3 (32B)** | `ollama pull qwen3:32b` | Excellent reasoning, coding, and general tasks |
| **Qwen 3 (14B)** | `ollama pull qwen3:14b` | Great balance of quality and speed |
| **Qwen 3 Coder (14B)** | `ollama pull qwen3-coder:14b` | Specialised for code generation and debugging |
| **Qwen 3 (30B MoE)** | `ollama pull qwen3:30b-a3b` | MoE with only 3B active — fast and capable |

### Fits in 64 GB RAM

| Model | Download | Good for |
|-------|----------|----------|
| **Llama 4 Scout** | `ollama pull llama4:scout` | Meta's multimodal model (text + images). 109B MoE with 17B active. Near-cloud quality |
| **DeepSeek R1 (70B)** | `ollama pull deepseek-r1:70b` | Excellent reasoning, maths, and code |
| **GPT-OSS (120B)** | `ollama pull gpt-oss:120b` | OpenAI's larger open model. MoE (5.1B active). Very capable |

### Fits in 128 GB+ RAM

| Model | Download | Good for |
|-------|----------|----------|
| **Qwen 3 (235B MoE)** | `ollama pull qwen3:235b` | Frontier-class quality. 22B active parameters. Rivals cloud APIs |
| **GLM-5** | `ollama pull glm-5` | 744B total, 40B active. MIT licence. Strong reasoning and coding |

### What do "MoE" and "active parameters" mean?

Some models use a **Mixture of Experts (MoE)** architecture. The model has many total parameters but only activates a fraction of them for each query — like having a team of specialists where only the relevant ones work on each question. This means:
- **Faster responses** than a dense model of the same total size
- **Lower RAM needed** than you'd expect from the total parameter count
- **Quality comparable** to dense models many times their active size

For example, `gpt-oss:20b` has 21B total parameters but only 3.6B active — so it runs like a small model but thinks like a much larger one.

**To remove a model you no longer want:**

```bash
ollama rm qwen3:8b
```

---

## Tips

- **Ollama needs to be running** for models to work. On Mac, check for the Ollama icon in your menu bar. On Windows, check the system tray.
- **Models run faster on first use** after the initial load. The first response may take a few seconds as the model loads into memory.
- **Close other memory-heavy apps** (Chrome with many tabs, Photoshop, etc.) before running large models — they need that RAM.
- **The model quality scales with size.** If a 3B model gives poor answers, try a 14B or 32B model before concluding that local models aren't useful.
- **You can run models in the background** and query them from notebooks — we'll do this in later weeks of the course.

---

## Further Reading

- <a href="https://ollama.com" target="_blank">Ollama website</a>
- <a href="https://github.com/ollama/ollama" target="_blank">Ollama on GitHub</a> (documentation and examples)
- <a href="https://ollama.com/library" target="_blank">Model library</a> (browse all available models)

---

*[Back to resources](README.md) · [Back to course overview](../README.md)*

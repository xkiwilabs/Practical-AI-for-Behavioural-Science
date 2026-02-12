"""
Generate figures for Week 1 lecture slides.
Run this script before build_slides.py.

Usage:
    python generate_figures.py

Output:
    images/ai_hierarchy.png
    images/traditional_vs_ml.png
    images/ai_timeline.png
    images/llm_loop.png
    images/prediction_vs_explanation.png
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
import os

# Ensure output directory exists
os.makedirs("images", exist_ok=True)

# Colour palette — MQ-inspired with good contrast on dark/light backgrounds
COLOURS = {
    "ai": "#D4533B",        # Red
    "ml": "#E8873D",        # Orange
    "dl": "#F0C05A",        # Gold
    "genai": "#7BC67E",     # Green
    "bg": "#FFFFFF",        # White background
    "text": "#2D2D2D",      # Near-black text
    "accent": "#A71930",    # MQ Red
    "blue": "#4A90D9",      # Soft blue
    "grey": "#8C8C8C",      # Mid grey
    "light_grey": "#F0F0F0",
}

DPI = 300


def fig_ai_hierarchy():
    """Nested circles showing AI > ML > Deep Learning > GenAI."""
    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    ax.set_xlim(-6, 6)
    ax.set_ylim(-5, 5.5)
    ax.set_aspect("equal")
    ax.axis("off")

    circles = [
        (0, 0, 4.5, COLOURS["ai"], "Artificial Intelligence (AI)", -4.2),
        (0, -0.3, 3.3, COLOURS["ml"], "Machine Learning (ML)", -3.2),
        (0, -0.5, 2.2, COLOURS["dl"], "Deep Learning", -2.2),
        (0, -0.6, 1.2, COLOURS["genai"], "Generative AI", -0.6),
    ]

    for x, y, r, colour, label, label_y in circles:
        circle = plt.Circle((x, y), r, fill=True, facecolor=colour,
                            edgecolor="white", linewidth=3, alpha=0.25)
        ax.add_patch(circle)
        circle_border = plt.Circle((x, y), r, fill=False,
                                   edgecolor=colour, linewidth=2.5, alpha=0.8)
        ax.add_patch(circle_border)
        fontsize = 18 if r > 2 else 16
        fontweight = "bold"
        ax.text(x, label_y, label, ha="center", va="center",
                fontsize=fontsize, fontweight=fontweight, color=COLOURS["text"])

    # Add examples on the right side
    examples = [
        (4.8, 3.5, "Robotics, Expert Systems,\nComputer Vision", COLOURS["ai"]),
        (4.8, 1.0, "Random Forests, SVMs,\nRegression", COLOURS["ml"]),
        (4.8, -1.2, "CNNs, RNNs, LSTMs,\nTransformers", COLOURS["dl"]),
        (4.8, -3.2, "ChatGPT, Claude,\nDALL-E, Gemini", COLOURS["genai"]),
    ]
    for x, y, text, colour in examples:
        ax.annotate(text, xy=(x - 2.5, y), xytext=(x, y),
                    fontsize=11, color=COLOURS["text"], va="center",
                    arrowprops=dict(arrowstyle="->", color=colour, lw=1.5),
                    bbox=dict(boxstyle="round,pad=0.4", facecolor=colour,
                             alpha=0.15, edgecolor=colour))

    fig.tight_layout()
    fig.savefig("images/ai_hierarchy.png", dpi=DPI, bbox_inches="tight",
                facecolor="white", transparent=False)
    plt.close()
    print("  Created: images/ai_hierarchy.png")


def fig_traditional_vs_ml():
    """Side-by-side comparison: Traditional Programming vs Machine Learning."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    for ax in (ax1, ax2):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis("off")

    # Traditional Programming (left)
    ax1.set_title("Traditional Programming", fontsize=18, fontweight="bold",
                  color=COLOURS["blue"], pad=15)

    boxes_left = [
        (2, 6, 6, 1.2, "Rules\n(written by human)", COLOURS["blue"]),
        (2, 4, 6, 1.2, "Data", COLOURS["grey"]),
        (2, 1, 6, 1.2, "Output", COLOURS["genai"]),
    ]
    for x, y, w, h, label, colour in boxes_left:
        rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.2",
                              facecolor=colour, alpha=0.2, edgecolor=colour, lw=2)
        ax1.add_patch(rect)
        ax1.text(x + w / 2, y + h / 2, label, ha="center", va="center",
                fontsize=13, fontweight="bold", color=COLOURS["text"])

    # Arrows
    ax1.annotate("", xy=(5, 4), xytext=(5, 6),
                arrowprops=dict(arrowstyle="-|>", color=COLOURS["text"], lw=2))
    ax1.text(5.5, 5.2, "Computer\nfollows rules", fontsize=10, ha="left",
            va="center", style="italic", color=COLOURS["grey"])
    ax1.annotate("", xy=(5, 1.2), xytext=(5, 4),
                arrowprops=dict(arrowstyle="-|>", color=COLOURS["text"], lw=2))

    # Machine Learning (right)
    ax2.set_title("Machine Learning", fontsize=18, fontweight="bold",
                  color=COLOURS["ai"], pad=15)

    boxes_right = [
        (2, 6, 6, 1.2, "Data\n(lots of examples)", COLOURS["ml"]),
        (2, 4, 6, 1.2, "Desired Output\n(labels / goals)", COLOURS["grey"]),
        (2, 1, 6, 1.2, "Rules\n(learned by computer)", COLOURS["ai"]),
    ]
    for x, y, w, h, label, colour in boxes_right:
        rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.2",
                              facecolor=colour, alpha=0.2, edgecolor=colour, lw=2)
        ax2.add_patch(rect)
        ax2.text(x + w / 2, y + h / 2, label, ha="center", va="center",
                fontsize=13, fontweight="bold", color=COLOURS["text"])

    ax2.annotate("", xy=(5, 4), xytext=(5, 6),
                arrowprops=dict(arrowstyle="-|>", color=COLOURS["text"], lw=2))
    ax2.text(5.5, 5.2, "Computer\nfinds patterns", fontsize=10, ha="left",
            va="center", style="italic", color=COLOURS["grey"])
    ax2.annotate("", xy=(5, 1.2), xytext=(5, 4),
                arrowprops=dict(arrowstyle="-|>", color=COLOURS["text"], lw=2))

    fig.tight_layout(w_pad=3)
    fig.savefig("images/traditional_vs_ml.png", dpi=DPI, bbox_inches="tight",
                facecolor="white", transparent=False)
    plt.close()
    print("  Created: images/traditional_vs_ml.png")


def fig_ai_timeline():
    """Horizontal timeline of key AI milestones."""
    fig, ax = plt.subplots(figsize=(13, 5))
    ax.set_xlim(1945, 2030)
    ax.set_ylim(-3, 4)
    ax.axis("off")

    # Main timeline bar
    ax.plot([1948, 2027], [0, 0], color=COLOURS["grey"], lw=3, solid_capstyle="round")

    events = [
        (1950, 2.5, "1950\nTuring:\n\"Can machines\nthink?\"", COLOURS["blue"]),
        (1958, -2.5, "1958\nPerceptron\n(first neural\nnetwork)", COLOURS["ml"]),
        (1980, 2.5, "1980s\nExpert\nSystems\n(AI Spring)", COLOURS["genai"]),
        (1990, -2.5, "1990s\nAI Winter\n(overpromise,\nunderdeliver)", COLOURS["grey"]),
        (2000, 2.5, "2000s\nBig Data +\nCheap GPUs", COLOURS["ml"]),
        (2012, -2.5, "2012\nDeep Learning\nwins ImageNet", COLOURS["dl"]),
        (2017, 2.5, "2017\nTransformers\n\"Attention Is\nAll You Need\"", COLOURS["ai"]),
        (2022, -2.5, "2022\nChatGPT\nlaunches", COLOURS["ai"]),
        (2025, 2.5, "2025-26\nAgentic AI,\nVibe Coding,\nDeep Research", COLOURS["genai"]),
    ]

    for year, y_text, label, colour in events:
        # Dot on timeline
        ax.plot(year, 0, "o", color=colour, markersize=10, zorder=5)
        # Vertical line
        ax.plot([year, year], [0, y_text * 0.6], color=colour, lw=1.5,
                linestyle="--", alpha=0.5)
        # Label
        ax.text(year, y_text, label, ha="center", va="center",
                fontsize=9, color=COLOURS["text"], fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.3", facecolor=colour,
                         alpha=0.15, edgecolor=colour, lw=1))

    ax.set_title("A Brief History of AI", fontsize=20, fontweight="bold",
                color=COLOURS["text"], pad=20)

    fig.tight_layout()
    fig.savefig("images/ai_timeline.png", dpi=DPI, bbox_inches="tight",
                facecolor="white", transparent=False)
    plt.close()
    print("  Created: images/ai_timeline.png")


def fig_llm_loop():
    """Nested LLM Problem-Solving Loop diagram."""
    fig, ax = plt.subplots(figsize=(11, 7))
    ax.set_xlim(-6, 6)
    ax.set_ylim(-5, 5.5)
    ax.axis("off")

    # Outer loop — research process
    outer_r = 4.2
    outer_steps = [
        (90, "PLAN", "Define your\nresearch question"),
        (0, "EXECUTE", "Use AI to build\ncode & analysis"),
        (270, "EVALUATE", "Does the result\nanswer your question?"),
        (180, "DOCUMENT", "Record what you\ndid and learned"),
    ]

    ax.set_title("The LLM Problem-Solving Loop", fontsize=20,
                fontweight="bold", color=COLOURS["text"], pad=10)

    # Draw outer loop label
    ax.text(0, 5.0, "OUTER LOOP — Your Research Process",
            ha="center", va="center", fontsize=13, fontweight="bold",
            color=COLOURS["blue"],
            bbox=dict(boxstyle="round,pad=0.3", facecolor=COLOURS["blue"],
                     alpha=0.1, edgecolor=COLOURS["blue"]))

    for angle_deg, label, desc in outer_steps:
        angle = np.radians(angle_deg)
        x = outer_r * np.cos(angle)
        y = outer_r * np.sin(angle) - 0.3
        rect = FancyBboxPatch((x - 1.3, y - 0.8), 2.6, 1.6,
                              boxstyle="round,pad=0.2",
                              facecolor=COLOURS["blue"], alpha=0.15,
                              edgecolor=COLOURS["blue"], lw=2)
        ax.add_patch(rect)
        ax.text(x, y + 0.2, label, ha="center", va="center",
                fontsize=14, fontweight="bold", color=COLOURS["blue"])
        ax.text(x, y - 0.4, desc, ha="center", va="center",
                fontsize=8, color=COLOURS["grey"])

    # Outer arrows (curved)
    for i in range(4):
        a1 = np.radians(outer_steps[i][0])
        a2 = np.radians(outer_steps[(i + 1) % 4][0])
        # Midpoint arrow
        mid_angles = np.linspace(a1 - 0.3, a2 + 0.3, 20)
        xs = (outer_r + 0.5) * np.cos(mid_angles)
        ys = (outer_r + 0.5) * np.sin(mid_angles) - 0.3
        ax.annotate("", xy=(xs[-1], ys[-1]), xytext=(xs[-3], ys[-3]),
                    arrowprops=dict(arrowstyle="-|>", color=COLOURS["blue"],
                                   lw=1.5, alpha=0.4))

    # Inner loop — working with AI
    inner_r = 2.0
    inner_steps = [
        (90, "ENGINEER", COLOURS["ai"]),
        (0, "PROMPT", COLOURS["ml"]),
        (270, "VERIFY", COLOURS["dl"]),
        (180, "REFINE", COLOURS["genai"]),
    ]

    ax.text(0, -0.3 + 2.5, "INNER LOOP", ha="center", va="center",
            fontsize=10, fontweight="bold", color=COLOURS["ai"])
    ax.text(0, -0.3 + 2.1, "Working with the AI", ha="center", va="center",
            fontsize=9, color=COLOURS["grey"])

    for angle_deg, label, colour in inner_steps:
        angle = np.radians(angle_deg)
        x = inner_r * np.cos(angle)
        y = inner_r * np.sin(angle) - 0.3
        rect = FancyBboxPatch((x - 0.8, y - 0.4), 1.6, 0.8,
                              boxstyle="round,pad=0.15",
                              facecolor=colour, alpha=0.2,
                              edgecolor=colour, lw=2)
        ax.add_patch(rect)
        ax.text(x, y, label, ha="center", va="center",
                fontsize=12, fontweight="bold", color=COLOURS["text"])

    # Inner arrows
    for i in range(4):
        a1 = np.radians(inner_steps[i][0])
        a2 = np.radians(inner_steps[(i + 1) % 4][0])
        mid_angles = np.linspace(a1 - 0.4, a2 + 0.4, 20)
        xs = (inner_r + 0.3) * np.cos(mid_angles)
        ys = (inner_r + 0.3) * np.sin(mid_angles) - 0.3
        ax.annotate("", xy=(xs[-1], ys[-1]), xytext=(xs[-3], ys[-3]),
                    arrowprops=dict(arrowstyle="-|>", color=COLOURS["ai"],
                                   lw=1.5, alpha=0.5))

    fig.tight_layout()
    fig.savefig("images/llm_loop.png", dpi=DPI, bbox_inches="tight",
                facecolor="white", transparent=False)
    plt.close()
    print("  Created: images/llm_loop.png")


def fig_prediction_vs_explanation():
    """Venn-style diagram showing prediction vs explanation."""
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(-5, 5)
    ax.set_ylim(-3.5, 4)
    ax.axis("off")

    # Two overlapping circles
    c1 = plt.Circle((-1.2, 0), 2.5, facecolor=COLOURS["blue"], alpha=0.15,
                    edgecolor=COLOURS["blue"], lw=2.5)
    c2 = plt.Circle((1.2, 0), 2.5, facecolor=COLOURS["ai"], alpha=0.15,
                    edgecolor=COLOURS["ai"], lw=2.5)
    ax.add_patch(c1)
    ax.add_patch(c2)

    # Labels
    ax.text(-2.5, 2.0, "Explanation", fontsize=18, fontweight="bold",
            ha="center", color=COLOURS["blue"])
    ax.text(-2.5, 1.3, "(Traditional\nPsychology)", fontsize=12,
            ha="center", color=COLOURS["grey"])
    ax.text(-2.5, -0.3, "Why does X\ncause Y?", fontsize=12,
            ha="center", color=COLOURS["text"], style="italic")
    ax.text(-2.5, -1.4, "Controlled\nexperiments", fontsize=11,
            ha="center", color=COLOURS["grey"])

    ax.text(2.5, 2.0, "Prediction", fontsize=18, fontweight="bold",
            ha="center", color=COLOURS["ai"])
    ax.text(2.5, 1.3, "(Machine\nLearning)", fontsize=12,
            ha="center", color=COLOURS["grey"])
    ax.text(2.5, -0.3, "Can we forecast\nY from X?", fontsize=12,
            ha="center", color=COLOURS["text"], style="italic")
    ax.text(2.5, -1.4, "Pattern finding\nin large datasets", fontsize=11,
            ha="center", color=COLOURS["grey"])

    # Overlap
    ax.text(0, 0.5, "Both\nvaluable", fontsize=14, fontweight="bold",
            ha="center", va="center", color=COLOURS["text"])
    ax.text(0, -0.5, "This\ncourse", fontsize=12,
            ha="center", va="center", color=COLOURS["accent"],
            fontweight="bold")

    ax.set_title("Prediction vs. Explanation in Psychology",
                fontsize=18, fontweight="bold", color=COLOURS["text"], pad=15)
    ax.text(0, -3.2, "Yarkoni & Westfall (2017)",
            ha="center", fontsize=10, color=COLOURS["grey"], style="italic")

    fig.tight_layout()
    fig.savefig("images/prediction_vs_explanation.png", dpi=DPI,
                bbox_inches="tight", facecolor="white", transparent=False)
    plt.close()
    print("  Created: images/prediction_vs_explanation.png")


if __name__ == "__main__":
    print("Generating Week 1 lecture figures...")
    fig_ai_hierarchy()
    fig_traditional_vs_ml()
    fig_ai_timeline()
    fig_llm_loop()
    fig_prediction_vs_explanation()
    print("\nAll figures generated in images/")

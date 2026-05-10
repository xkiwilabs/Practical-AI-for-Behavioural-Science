"""Generate corrected figures for Week 9 slides.

Uses matplotlib so axis orientation is guaranteed correct:
- Loss curves descend visually (high loss top-left, low loss bottom-right)
- Gradient descent landscape: minimum at bottom of chart
- NN diagrams: nodes and connections use the same coordinate system
"""

from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch

OUT = Path(__file__).parent

# MQ palette
RED = "#A71930"
BLUE = "#4A90D9"
PURPLE = "#7B68A8"
GREEN = "#5BA55B"
GOLD = "#C8972C"
GREY = "#8C8C8C"
CHARCOAL = "#2D2D2D"
LIGHT_GREY = "#F2F2F2"

plt.rcParams.update({
    "font.family": "Inter, DejaVu Sans, sans-serif",
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.1,
    "savefig.dpi": 200,
})


# ---------------------------------------------------------------------------
# 1. Perceptron diagram
# ---------------------------------------------------------------------------
def perceptron():
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")

    # Layout (axis units)
    inputs = [(1.2, 3.2, "x₁"), (1.2, 2.0, "x₂"), (1.2, 0.8, "x₃")]
    sum_pos = (4.5, 2.0)
    bias_pos = (4.5, 3.5)
    act_pos = (6.5, 2.0)
    out_pos = (8.7, 2.0)

    # Connections (drawn first so circles cover endpoints)
    for (x, y, _) in inputs:
        ax.plot([x, sum_pos[0]], [y, sum_pos[1]], color=BLUE, lw=2, alpha=0.6, zorder=1)
    # bias dashed line
    ax.plot([bias_pos[0], sum_pos[0]], [bias_pos[1], sum_pos[1]],
            color=GREY, lw=1.5, ls=(0, (4, 3)), alpha=0.7, zorder=1)
    # sum -> activation
    ax.plot([sum_pos[0], act_pos[0]], [sum_pos[1], act_pos[1]],
            color=CHARCOAL, lw=2, alpha=0.6, zorder=1)
    # activation -> output
    ax.plot([act_pos[0], out_pos[0]], [act_pos[1], out_pos[1]],
            color=GOLD, lw=2, alpha=0.6, zorder=1)

    # Weight labels
    for i, (x, y, _) in enumerate(inputs, start=1):
        mx, my = (x + sum_pos[0]) / 2, (y + sum_pos[1]) / 2
        ax.text(mx, my + 0.18, f"w{chr(0x2080 + i)}", color=CHARCOAL,
                fontsize=11, fontweight="bold", ha="center")

    # Nodes
    def node(pos, label, fill, r=0.32, fontsize=12, fontcolor="white"):
        c = Circle(pos, r, color=fill, zorder=3, ec="white", lw=1.5)
        ax.add_patch(c)
        ax.text(pos[0], pos[1], label, ha="center", va="center",
                color=fontcolor, fontsize=fontsize, fontweight="bold", zorder=4)

    for x, y, lbl in inputs:
        node((x, y), lbl, BLUE)
    node(sum_pos, "Σ", CHARCOAL, r=0.36, fontsize=18)
    node(bias_pos, "+b", GREY, r=0.26, fontsize=10)
    node(act_pos, "σ", GOLD, r=0.36, fontsize=18)
    node(out_pos, "ŷ", RED, r=0.32, fontsize=14)

    # Layer labels (below)
    for x, label in [(1.2, "Inputs"), (4.5, "Weighted sum"),
                     (6.5, "Activation"), (8.7, "Output")]:
        ax.text(x, 0.05, label, ha="center", color=GREY,
                fontsize=10, fontweight="bold")

    fig.savefig(OUT / "perceptron-diagram.png", transparent=True)
    plt.close(fig)


# ---------------------------------------------------------------------------
# 2. MLP architecture
# ---------------------------------------------------------------------------
def mlp_architecture():
    fig, ax = plt.subplots(figsize=(11, 4.5))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 4.5)
    ax.axis("off")

    # Layer x-positions and node y-positions
    layers = [
        ("Input Layer\n(4 features)", 1.2, BLUE,
            [3.6, 2.7, 1.8, 0.9], ["x₁", "x₂", "x₃", "x₄"]),
        ("Hidden Layer 1\n(5 neurons)", 4.0, PURPLE,
            [3.8, 3.0, 2.2, 1.4, 0.6], [""] * 5),
        ("Hidden Layer 2\n(3 neurons)", 6.8, PURPLE,
            [3.2, 2.2, 1.2], [""] * 3),
        ("Output Layer\n(2 outputs)", 9.6, RED,
            [2.7, 1.7], ["ŷ₁", "ŷ₂"]),
    ]

    # Connections (drawn first)
    edge_colors = [BLUE, PURPLE, RED]
    for i in range(len(layers) - 1):
        _, x1, _, ys1, _ = layers[i]
        _, x2, _, ys2, _ = layers[i + 1]
        for y1 in ys1:
            for y2 in ys2:
                ax.plot([x1, x2], [y1, y2], color=edge_colors[i],
                        lw=1.0, alpha=0.25, zorder=1)

    # Nodes
    for label, x, color, ys, names in layers:
        for y, name in zip(ys, names):
            c = Circle((x, y), 0.27, color=color, zorder=3, ec="white", lw=1.5)
            ax.add_patch(c)
            if name:
                ax.text(x, y, name, ha="center", va="center",
                        color="white", fontsize=10, fontweight="bold", zorder=4)
        ax.text(x, 0.05, label, ha="center", va="bottom",
                color=GREY, fontsize=10, fontweight="bold")

    fig.savefig(OUT / "mlp-diagram.png", transparent=True)
    plt.close(fig)


# ---------------------------------------------------------------------------
# 3. Gradient descent landscape (minimum at BOTTOM of chart)
# ---------------------------------------------------------------------------
def gradient_descent():
    fig, ax = plt.subplots(figsize=(10, 4.5))

    # A loss curve with a clear minimum near x ~ 3.5
    x = np.linspace(0, 10, 400)
    y = 0.05 * (x - 3.5) ** 2 + 0.4 + 0.15 * np.sin(0.9 * x) + 0.05 * np.cos(2.5 * x)

    ax.plot(x, y, color=BLUE, lw=2.5, zorder=2)
    ax.fill_between(x, y, y.max() + 0.5, color=BLUE, alpha=0.08, zorder=1)

    # Descent path: start at high loss on the right, step down toward minimum
    path_x = np.array([8.5, 7.4, 6.2, 5.1, 4.2, 3.7, 3.5])
    path_y = np.interp(path_x, x, y)
    ax.plot(path_x, path_y, color=RED, lw=2, zorder=3)
    for px, py, alpha in zip(path_x, path_y,
                             [1.0, 0.85, 0.75, 0.65, 0.55, 0.45, 1.0]):
        ax.scatter([px], [py], s=80, color=RED, alpha=alpha, zorder=4,
                   ec="white", lw=1.2)

    # Annotations
    ax.scatter([path_x[0]], [path_y[0]], s=180, color=RED, zorder=5,
               ec="white", lw=2)
    ax.annotate("Start here\n(high loss)", xy=(path_x[0], path_y[0]),
                xytext=(path_x[0] + 0.4, path_y[0] + 0.3),
                fontsize=11, fontweight="bold", color=RED)

    min_idx = np.argmin(y)
    ax.scatter([x[min_idx]], [y[min_idx]], s=180, color=GREEN, zorder=5,
               ec="white", lw=2)
    ax.annotate("Goal: minimum loss", xy=(x[min_idx], y[min_idx]),
                xytext=(x[min_idx] + 0.4, y[min_idx] + 0.5),
                fontsize=11, fontweight="bold", color=GREEN,
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.2))

    ax.set_xlabel("Weight values", fontsize=12, fontweight="bold", color=GREY)
    ax.set_ylabel("Loss", fontsize=12, fontweight="bold", color=GREY)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_color(GREY)
        spine.set_alpha(0.4)

    ax.set_facecolor(LIGHT_GREY)
    fig.patch.set_facecolor("white")

    fig.savefig(OUT / "gradient-descent-landscape.png")
    plt.close(fig)


# ---------------------------------------------------------------------------
# 4. Training vs validation loss (training drops, val drops then rises)
# ---------------------------------------------------------------------------
def loss_curves():
    fig, ax = plt.subplots(figsize=(10, 4.5))

    epochs = np.arange(0, 51)
    # Training loss: smooth exponential decay
    train_loss = 0.05 + 0.95 * np.exp(-epochs / 12)
    # Validation: drops with training, then rises after epoch ~18 (overfitting)
    val_loss = 0.05 + 0.95 * np.exp(-epochs / 12) + np.where(
        epochs > 18, 0.012 * (epochs - 18), 0.0
    )
    # Add small noise so it looks like real training
    rng = np.random.default_rng(42)
    train_loss = train_loss + rng.normal(0, 0.01, size=train_loss.shape)
    val_loss = val_loss + rng.normal(0, 0.015, size=val_loss.shape)

    ax.plot(epochs, train_loss, color=BLUE, lw=2.5,
            label="Training loss", zorder=3)
    ax.plot(epochs, val_loss, color=RED, lw=2.5, ls="--",
            label="Validation loss", zorder=3)

    # Mark "overfitting begins here"
    overfit_epoch = 18
    ax.axvline(overfit_epoch, color=GOLD, lw=1.5, ls=":", alpha=0.8, zorder=2)
    ax.annotate("Overfitting\nbegins here",
                xy=(overfit_epoch, val_loss[overfit_epoch]),
                xytext=(overfit_epoch + 3, val_loss[overfit_epoch] + 0.18),
                fontsize=11, fontweight="bold", color=GOLD,
                arrowprops=dict(arrowstyle="->", color=GOLD, lw=1.2))

    ax.set_xlabel("Epoch", fontsize=12, fontweight="bold", color=GREY)
    ax.set_ylabel("Loss", fontsize=12, fontweight="bold", color=GREY)
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 1.1)
    ax.legend(loc="upper right", frameon=False, fontsize=11)
    ax.grid(True, alpha=0.2, ls="--")
    for spine in ax.spines.values():
        spine.set_color(GREY)
        spine.set_alpha(0.4)
    ax.set_facecolor(LIGHT_GREY)
    fig.patch.set_facecolor("white")

    fig.savefig(OUT / "training-validation-loss.png")
    plt.close(fig)


# ---------------------------------------------------------------------------
# 5. Activation functions (sigmoid, ReLU)
# ---------------------------------------------------------------------------
def activation_functions():
    fig, axes = plt.subplots(1, 2, figsize=(11, 4))

    x = np.linspace(-6, 6, 400)
    sigmoid = 1 / (1 + np.exp(-x))
    relu = np.maximum(0, x)

    for ax, y, color, name in [
        (axes[0], sigmoid, BLUE, "Sigmoid"),
        (axes[1], relu, RED, "ReLU"),
    ]:
        ax.plot(x, y, color=color, lw=3)
        ax.axhline(0, color=GREY, lw=1, alpha=0.4)
        ax.axvline(0, color=GREY, lw=1, alpha=0.4)
        ax.set_title(name, fontsize=14, fontweight="bold", color=color)
        ax.set_xlim(-6, 6)
        ax.set_xticks([])
        ax.set_facecolor(LIGHT_GREY)
        for spine in ax.spines.values():
            spine.set_color(GREY)
            spine.set_alpha(0.4)

    axes[0].set_ylim(-0.2, 1.2)
    axes[0].set_yticks([0, 1])
    axes[0].set_ylabel("Output", fontsize=11, color=GREY)
    axes[1].set_ylim(-1, 6)
    axes[1].set_yticks([0])

    fig.patch.set_facecolor("white")
    fig.savefig(OUT / "activation-functions-pair.png")
    plt.close(fig)


# ---------------------------------------------------------------------------
# 6. Learning rate comparison (3 panels)
# ---------------------------------------------------------------------------
def learning_rates():
    fig, axes = plt.subplots(1, 3, figsize=(13, 3.6))

    # Underlying loss curve (parabolic-ish)
    x = np.linspace(-5, 5, 200)
    y_curve = 0.4 + 0.18 * (x - 0.5) ** 2

    titles = ["Too Large", "Just Right", "Too Small"]
    colors = [RED, GREEN, BLUE]
    descriptions = [
        "Bounces around wildly.\nOvershoots the valley.\nMay never converge.",
        "Smooth descent.\nReaches the minimum\nefficiently.",
        "Takes forever.\nMay get stuck in a\nshallow dip.",
    ]

    # Step trajectories (manually placed for clarity)
    paths = [
        np.array([-4.2, 3.5, -3.0, 2.5, -2.0, 1.5, -1.0]),       # too large
        np.array([-4.2, -2.8, -1.6, -0.8, -0.2, 0.3, 0.5]),     # just right
        np.array([-4.2, -3.9, -3.6, -3.3, -3.0, -2.7, -2.4]),    # too small
    ]

    for ax, title, color, desc, path in zip(axes, titles, colors, descriptions, paths):
        ax.plot(x, y_curve, color=GREY, lw=2, alpha=0.4)
        path_y = 0.4 + 0.18 * (path - 0.5) ** 2
        ax.plot(path, path_y, color=color, lw=1.8, ls="--", alpha=0.8)
        ax.scatter(path, path_y, color=color, s=55, zorder=3, ec="white", lw=1)

        ax.set_title(title, color=color, fontsize=13, fontweight="bold")
        ax.set_xlim(-5, 5)
        ax.set_ylim(0, 5.5)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_facecolor(LIGHT_GREY)
        for spine in ax.spines.values():
            spine.set_color(GREY)
            spine.set_alpha(0.4)
        ax.text(0, -1.1, desc, ha="center", va="top", color=GREY,
                fontsize=9.5, transform=ax.transData)

    fig.patch.set_facecolor("white")
    fig.subplots_adjust(bottom=0.28)
    fig.savefig(OUT / "learning-rate-comparison.png")
    plt.close(fig)


# ---------------------------------------------------------------------------
# 7. Dropout illustration
# ---------------------------------------------------------------------------
def dropout():
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 4)
    ax.axis("off")

    inputs_y = [3.2, 2.0, 0.8]
    hidden_y = [3.5, 2.6, 1.4, 0.5]
    hidden_active = [True, False, True, False]
    output_y = [2.0]

    # Connections (only from active hidden)
    for iy in inputs_y:
        for hy, active in zip(hidden_y, hidden_active):
            color = BLUE if active else GREY
            alpha = 0.35 if active else 0.08
            ax.plot([1.5, 3.5], [iy, hy], color=color, lw=1.2,
                    alpha=alpha, zorder=1)
    for hy, active in zip(hidden_y, hidden_active):
        for oy in output_y:
            color = PURPLE if active else GREY
            alpha = 0.45 if active else 0.05
            ax.plot([3.5, 5.5], [hy, oy], color=color, lw=1.2,
                    alpha=alpha, zorder=1)

    # Input nodes
    for iy, lbl in zip(inputs_y, ["x₁", "x₂", "x₃"]):
        c = Circle((1.5, iy), 0.25, color=BLUE, zorder=3, ec="white", lw=1.2)
        ax.add_patch(c)
        ax.text(1.5, iy, lbl, ha="center", va="center", color="white",
                fontsize=10, fontweight="bold", zorder=4)

    # Hidden nodes (active vs dropped)
    for hy, active in zip(hidden_y, hidden_active):
        if active:
            c = Circle((3.5, hy), 0.25, color=PURPLE, zorder=3, ec="white", lw=1.2)
            ax.add_patch(c)
        else:
            c = Circle((3.5, hy), 0.25, color="#D0D0D0", zorder=3, ec="white", lw=1.2,
                       alpha=0.7)
            ax.add_patch(c)
            ax.text(3.5, hy, "×", ha="center", va="center", color=RED,
                    fontsize=22, fontweight="bold", zorder=4)

    # Output
    c = Circle((5.5, 2.0), 0.25, color=RED, zorder=3, ec="white", lw=1.2)
    ax.add_patch(c)
    ax.text(5.5, 2.0, "ŷ", ha="center", va="center", color="white",
            fontsize=12, fontweight="bold", zorder=4)

    fig.savefig(OUT / "dropout-diagram.png", transparent=True)
    plt.close(fig)


# ---------------------------------------------------------------------------
# 8. Training loop flow chart (mirrors the slide 19 pseudocode)
# ---------------------------------------------------------------------------
def training_loop_flow():
    """Training loop as nested loops with right-angle routing.

    Routing:
      - "after all batches": exits RIGHT side of batch frame → 90° down →
        90° left → enters RIGHT side of validation box
      - "next epoch": exits LEFT side of validation box → 90° up →
        90° right → enters LEFT side of batch frame
      - Both labels sit ABOVE their horizontal segments adjacent to
        the validation box.
    """
    fig, ax = plt.subplots(figsize=(14, 7.2))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 8)
    ax.axis("off")

    # ---- Outer EPOCH frame -----------------------------------------------
    outer = FancyBboxPatch((0.4, 0.4), 15.2, 7.2,
                           boxstyle="round,pad=0.05,rounding_size=0.25",
                           linewidth=2.5, edgecolor=PURPLE,
                           facecolor=PURPLE, alpha=0.05)
    ax.add_patch(outer)
    ax.text(0.75, 7.25, "EPOCH LOOP",
            color=PURPLE, fontsize=15, fontweight="bold")
    ax.text(0.75, 6.9, "(repeat 10–100+ times)",
            color=PURPLE, fontsize=11, style="italic", alpha=0.85)

    # ---- Inner BATCH frame ------------------------------------------------
    batch_x, batch_y = 1.8, 4.0
    batch_w, batch_h = 12.4, 2.7
    inner = FancyBboxPatch((batch_x, batch_y), batch_w, batch_h,
                           boxstyle="round,pad=0.05,rounding_size=0.2",
                           linewidth=2.5, edgecolor=BLUE,
                           facecolor=BLUE, alpha=0.06)
    ax.add_patch(inner)
    ax.text(2.15, 6.55, "BATCH LOOP",
            color=BLUE, fontsize=12.5, fontweight="bold")

    # ---- Four pipeline boxes ---------------------------------------------
    steps = [
        ("Forward\npass",   BLUE),
        ("Compute\nloss",   RED),
        ("Backward\npass",  PURPLE),
        ("Update\nweights", GREEN),
    ]
    box_w, box_h = 2.1, 1.0
    y_step = 5.4          # boxes pushed up so there's room for the loop arm
    x_starts = [2.4, 5.5, 8.6, 11.7]

    centers = []
    for (label, color), x in zip(steps, x_starts):
        b = FancyBboxPatch((x, y_step), box_w, box_h,
                           boxstyle="round,pad=0.02,rounding_size=0.12",
                           linewidth=2, edgecolor=color,
                           facecolor=color, alpha=0.20)
        ax.add_patch(b)
        ax.text(x + box_w / 2, y_step + box_h / 2, label,
                ha="center", va="center", fontsize=12.5,
                fontweight="bold", color=color)
        centers.append((x + box_w / 2, y_step + box_h / 2))

    for (x1, y1), (x2, y2) in zip(centers[:-1], centers[1:]):
        ax.annotate("",
                    xy=(x2 - box_w / 2 - 0.05, y2),
                    xytext=(x1 + box_w / 2 + 0.05, y1),
                    arrowprops=dict(arrowstyle="-|>", color=CHARCOAL,
                                    lw=2.0, mutation_scale=18))

    # ---- "next batch" right-angle loop arrow inside the batch frame ------
    # Path: down from bottom-centre of Update → left → up into Forward.
    forward_cx = x_starts[0] + box_w / 2
    update_cx = x_starts[-1] + box_w / 2
    loop_y = 4.3   # horizontal arm well below the boxes, inside batch frame

    # Segment 1: down from bottom of Update weights
    ax.plot([update_cx, update_cx], [y_step, loop_y],
            color=BLUE, lw=2.0, solid_capstyle="butt")
    # Segment 2: left across
    ax.plot([update_cx, forward_cx], [loop_y, loop_y],
            color=BLUE, lw=2.0, solid_capstyle="butt")
    # Segment 3: up into bottom of Forward pass — arrowhead pointing up
    next_batch_arrow = FancyArrowPatch(
        (forward_cx, loop_y), (forward_cx, y_step),
        arrowstyle="-|>", mutation_scale=18,
        color=BLUE, lw=2.0,
    )
    ax.add_patch(next_batch_arrow)

    ax.text((forward_cx + update_cx) / 2, loop_y + 0.18,
            "next batch", color=BLUE, fontsize=12,
            ha="center", va="bottom", fontweight="bold", style="italic")

    # ---- Validation box --------------------------------------------------
    val_w, val_h = 4.2, 1.3
    val_x = 8.0 - val_w / 2
    val_y = 1.2
    val = FancyBboxPatch((val_x, val_y), val_w, val_h,
                         boxstyle="round,pad=0.02,rounding_size=0.15",
                         linewidth=2.5, edgecolor=GOLD,
                         facecolor=GOLD, alpha=0.20)
    ax.add_patch(val)
    ax.text(8.0, val_y + val_h / 2,
            "Evaluate on validation set",
            ha="center", va="center", fontsize=13,
            fontweight="bold", color=GOLD)

    # ----- Geometry for the right-angle routes ----------------------------
    batch_right = batch_x + batch_w           # 14.2
    batch_left = batch_x                      # 1.8
    batch_mid_y = batch_y + batch_h / 2       # 5.35
    val_right = val_x + val_w                 # 10.1
    val_left = val_x                          # 5.9
    val_mid_y = val_y + val_h / 2             # 1.85

    pivot_right_x = 15.0                      # vertical pivot for right route
    pivot_left_x = 1.0                        # vertical pivot for left route

    # ----- "after all batches" path (CHARCOAL): R out → down → L into val
    ax.plot([batch_right, pivot_right_x], [batch_mid_y, batch_mid_y],
            color=CHARCOAL, lw=2.2, solid_capstyle="butt")
    ax.plot([pivot_right_x, pivot_right_x], [batch_mid_y, val_mid_y],
            color=CHARCOAL, lw=2.2, solid_capstyle="butt")
    arrow_in = FancyArrowPatch(
        (pivot_right_x, val_mid_y), (val_right, val_mid_y),
        arrowstyle="-|>", mutation_scale=22,
        color=CHARCOAL, lw=2.2,
    )
    ax.add_patch(arrow_in)
    ax.text((pivot_right_x + val_right) / 2, val_mid_y + 0.18,
            "after all batches",
            color=CHARCOAL, fontsize=12, ha="center", va="bottom",
            fontweight="bold", style="italic")

    # ----- "next epoch" path (PURPLE): L out of val → up → R into batch ---
    ax.plot([val_left, pivot_left_x], [val_mid_y, val_mid_y],
            color=PURPLE, lw=2.2, solid_capstyle="butt")
    ax.plot([pivot_left_x, pivot_left_x], [val_mid_y, batch_mid_y],
            color=PURPLE, lw=2.2, solid_capstyle="butt")
    arrow_out = FancyArrowPatch(
        (pivot_left_x, batch_mid_y), (batch_left, batch_mid_y),
        arrowstyle="-|>", mutation_scale=22,
        color=PURPLE, lw=2.2,
    )
    ax.add_patch(arrow_out)
    ax.text((val_left + pivot_left_x) / 2, val_mid_y + 0.18,
            "next epoch",
            color=PURPLE, fontsize=12, ha="center", va="bottom",
            fontweight="bold", style="italic")

    fig.savefig(OUT / "training-loop-flow.png", transparent=True)
    plt.close(fig)


# ---------------------------------------------------------------------------
# 9. Local vs global minima (companion to gradient descent figure)
# ---------------------------------------------------------------------------
def local_vs_global_minima():
    """Loss landscape with multiple minima: two trajectories, one stuck in
    a local minimum, one reaching the global minimum.
    """
    fig, ax = plt.subplots(figsize=(10, 4.8))

    # Multi-modal loss surface — two valleys at different depths
    x = np.linspace(0, 10, 600)
    y = (0.6 * np.exp(-((x - 2.3) ** 2) / 0.8)
         + 1.2 * np.exp(-((x - 6.8) ** 2) / 1.3)
         + 0.05 * x)
    y = 1.4 - y  # invert so valleys are at the bottom

    ax.plot(x, y, color=BLUE, lw=2.5, zorder=2)
    ax.fill_between(x, y, y.max() + 0.6, color=BLUE, alpha=0.08, zorder=1)

    # ---- Trajectory A: starts on the left ridge, gets stuck in local min
    path_a_x = np.array([0.5, 1.1, 1.6, 2.0, 2.25, 2.32])
    path_a_y = np.interp(path_a_x, x, y)
    ax.plot(path_a_x, path_a_y, color=RED, lw=2.2, zorder=3,
            ls="--", alpha=0.8)
    for px, py in zip(path_a_x, path_a_y):
        ax.scatter([px], [py], s=55, color=RED, zorder=4,
                   ec="white", lw=1.2)
    # Big start marker
    ax.scatter([path_a_x[0]], [path_a_y[0]], s=160, color=RED, zorder=5,
               ec="white", lw=2)
    # Stuck marker
    ax.scatter([path_a_x[-1]], [path_a_y[-1]], s=160, color=RED, zorder=5,
               ec="white", lw=2)

    ax.annotate("Start A", xy=(path_a_x[0], path_a_y[0]),
                xytext=(path_a_x[0] - 0.3, path_a_y[0] + 0.25),
                fontsize=11, fontweight="bold", color=RED)
    ax.annotate("Stuck:\nlocal minimum",
                xy=(path_a_x[-1], path_a_y[-1]),
                xytext=(path_a_x[-1] - 1.6, path_a_y[-1] - 0.55),
                fontsize=11, fontweight="bold", color=RED,
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.2))

    # ---- Trajectory B: starts on the right ridge, reaches global min
    path_b_x = np.array([9.4, 8.8, 8.2, 7.6, 7.1, 6.85])
    path_b_y = np.interp(path_b_x, x, y)
    ax.plot(path_b_x, path_b_y, color=GREEN, lw=2.2, zorder=3,
            ls="--", alpha=0.8)
    for px, py in zip(path_b_x, path_b_y):
        ax.scatter([px], [py], s=55, color=GREEN, zorder=4,
                   ec="white", lw=1.2)
    ax.scatter([path_b_x[0]], [path_b_y[0]], s=160, color=GREEN, zorder=5,
               ec="white", lw=2)
    ax.scatter([path_b_x[-1]], [path_b_y[-1]], s=160, color=GREEN, zorder=5,
               ec="white", lw=2)

    ax.annotate("Start B", xy=(path_b_x[0], path_b_y[0]),
                xytext=(path_b_x[0] - 0.1, path_b_y[0] + 0.25),
                fontsize=11, fontweight="bold", color=GREEN)
    ax.annotate("Reaches\nglobal minimum",
                xy=(path_b_x[-1], path_b_y[-1]),
                xytext=(path_b_x[-1] + 0.4, path_b_y[-1] - 0.45),
                fontsize=11, fontweight="bold", color=GREEN,
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=1.2))

    ax.set_xlabel("Weight values", fontsize=12, fontweight="bold", color=GREY)
    ax.set_ylabel("Loss", fontsize=12, fontweight="bold", color=GREY)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim(y.min() - 0.3, y.max() + 0.5)
    for spine in ax.spines.values():
        spine.set_color(GREY)
        spine.set_alpha(0.4)
    ax.set_facecolor(LIGHT_GREY)
    fig.patch.set_facecolor("white")

    fig.savefig(OUT / "local-vs-global-minima.png")
    plt.close(fig)


if __name__ == "__main__":
    perceptron()
    mlp_architecture()
    gradient_descent()
    loss_curves()
    activation_functions()
    learning_rates()
    dropout()
    training_loop_flow()
    local_vs_global_minima()
    print("All figures generated to:", OUT)

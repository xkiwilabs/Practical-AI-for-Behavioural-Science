"""
PSYC4411 Setup Test — Python Script
====================================
Run this from the terminal to check your environment is set up correctly:

    conda activate psyc4411
    python test-setup.py

This does the same checks as test-setup.ipynb, but runs as a standalone
Python script — good practice for running code outside of a notebook.
"""

import sys

def main():
    print()
    print("=" * 50)
    print("  PSYC4411 Setup Test")
    print("=" * 50)
    print()

    # ── Check Python version ──────────────────────────
    print(f"Python: {sys.version}")
    print()

    # ── Check package imports ─────────────────────────
    all_ok = True

    packages = [
        ("pandas", "pd"),
        ("numpy", "np"),
        ("matplotlib", "matplotlib"),
        ("matplotlib.pyplot", "plt"),
        ("seaborn", "sns"),
        ("sklearn", "sklearn"),
    ]

    print("Checking packages:")
    for module_name, alias in packages:
        try:
            mod = __import__(module_name)
            # For sub-modules like matplotlib.pyplot, get the top-level version
            top_level = module_name.split(".")[0]
            top_mod = __import__(top_level)
            version = getattr(top_mod, "__version__", "unknown")
            # Only print version once per top-level package
            if module_name == top_level:
                print(f"  {module_name:<15} v{version}")
            else:
                print(f"  {module_name:<15} (part of {top_level})")
        except ImportError:
            print(f"  {module_name:<15} MISSING")
            all_ok = False

    print()

    # ── Quick matplotlib test ─────────────────────────
    print("Testing matplotlib (create and close a figure)...")
    try:
        import matplotlib
        matplotlib.use("Agg")  # Non-interactive backend — no window needed
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots()
        ax.scatter([1, 2, 3], [4, 5, 6])
        ax.set_title("Test plot")
        plt.close(fig)
        print("  Matplotlib test passed.")
    except Exception as e:
        print(f"  Matplotlib test FAILED: {e}")
        all_ok = False

    print()

    # ── Result ────────────────────────────────────────
    if all_ok:
        print("=" * 50)
        print("  All checks passed! Your setup is ready")
        print("  for PSYC4411. See you in Week 2!")
        print("=" * 50)
    else:
        print("=" * 50)
        print("  Some checks failed. See messages above.")
        print("  Try re-running the setup script, or bring")
        print("  your laptop to Week 2 for help.")
        print("=" * 50)
        sys.exit(1)

    print()


if __name__ == "__main__":
    main()

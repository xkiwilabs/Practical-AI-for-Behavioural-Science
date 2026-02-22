#!/bin/bash
# ============================================================
# PSYC4411 Setup Script — macOS / Linux
# ============================================================
# This script creates a conda environment with all the Python
# packages you need for the course, and registers it as a
# Jupyter kernel so VS Code can find it.
#
# PREREQUISITES:
#   - Miniconda (or Anaconda) must be installed first.
#     Download from: https://docs.anaconda.com/miniconda/
#
# HOW TO RUN:
#   1. Open Terminal
#   2. Navigate to the setup folder:
#      cd path/to/Practical-AI-for-Behavioural-Science/setup
#   3. Run:  bash setup-mac.sh
# ============================================================

# Don't use set -e — we handle errors explicitly so we can
# print actionable remediation instead of silently stopping.

# ── Track overall success ───────────────────────────────────
SETUP_OK=true

echo ""
echo "=========================================="
echo "  PSYC4411 Environment Setup (macOS)"
echo "=========================================="
echo ""

# ── Step 1: Check that conda is available ─────────────────

echo "Step 1: Checking for conda..."

if ! command -v conda &> /dev/null; then
    echo ""
    echo "ERROR: conda is not installed or not found in your PATH."
    echo ""
    echo "Please install Miniconda first:"
    echo "  https://docs.anaconda.com/miniconda/"
    echo ""
    echo "After installing, close and reopen Terminal, then run this script again."
    exit 1
fi

CONDA_VERSION=$(conda --version 2>&1)
echo "Found: $CONDA_VERSION"

# Detect Anaconda vs Miniconda
CONDA_ROOT=$(conda info --base 2>/dev/null)
if echo "$CONDA_ROOT" | grep -qi "anaconda"; then
    echo "  (Using Anaconda — that works perfectly fine for this course)"
fi
echo ""

# ── Step 2: Create (or recreate) the conda environment ───

ENV_NAME="psyc4411"
SKIP_CREATE=false

# Check if environment already exists
if conda env list 2>/dev/null | grep -q "^${ENV_NAME} "; then
    echo "The '$ENV_NAME' environment already exists."
    echo ""
    read -p "Do you want to remove it and start fresh? (y/n) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Removing existing environment..."
        if ! conda env remove -n "$ENV_NAME" -y --quiet; then
            echo "ERROR: Could not remove the existing environment."
            echo "Try manually: conda env remove -n $ENV_NAME"
            SETUP_OK=false
        fi
        echo ""
    else
        echo "Keeping existing environment. Skipping to kernel registration..."
        echo ""
        SKIP_CREATE=true
    fi
fi

if [ "$SETUP_OK" = true ] && [ "$SKIP_CREATE" = false ]; then
    echo "Step 2: Creating conda environment '$ENV_NAME' from environment.yml..."
    echo "(This installs Python and all course packages — may take a few minutes)"
    echo ""

    if ! conda env create -f environment.yml; then
        # Creation failed — try cleaning the cache and retrying once
        echo ""
        echo "Environment creation failed. Clearing conda package cache and retrying..."
        echo "(This fixes corrupted downloads, which is the most common cause)"
        echo ""

        conda clean --packages --tarballs -y 2>/dev/null

        # Remove the partially-created environment if it exists
        if conda env list 2>/dev/null | grep -q "^${ENV_NAME} "; then
            conda env remove -n "$ENV_NAME" -y --quiet 2>/dev/null
        fi

        echo "Retrying environment creation..."
        if ! conda env create -f environment.yml; then
            echo ""
            echo "ERROR: Environment creation failed again after clearing cache."
            SETUP_OK=false
        fi
    fi

    # Verify the environment actually exists
    if [ "$SETUP_OK" = true ]; then
        if ! conda env list 2>/dev/null | grep -q "^${ENV_NAME} "; then
            echo ""
            echo "ERROR: conda reported success, but the '$ENV_NAME' environment was not found."
            SETUP_OK=false
        else
            echo "Environment '$ENV_NAME' created successfully."
        fi
    fi
    echo ""
fi

# ── Step 3: Register the Jupyter kernel ───────────────────

if [ "$SETUP_OK" = true ]; then
    echo "Step 3: Registering Jupyter kernel (so VS Code can find it)..."
    if ! conda run -n "$ENV_NAME" python -m ipykernel install --user --name="$ENV_NAME" --display-name="PSYC4411"; then
        echo "ERROR: Kernel registration failed."
        SETUP_OK=false
    fi
    echo ""
fi

# ── Step 4: Test that packages import correctly ──────────

if [ "$SETUP_OK" = true ]; then
    echo "Step 4: Testing that all packages load correctly..."
    if ! conda run -n "$ENV_NAME" python -c "
import pandas as pd
import numpy as np
import matplotlib
import seaborn as sns
import sklearn
print('  pandas       v' + pd.__version__)
print('  numpy        v' + np.__version__)
print('  matplotlib   v' + matplotlib.__version__)
print('  seaborn      v' + sns.__version__)
print('  scikit-learn v' + sklearn.__version__)
print()
print('All packages installed successfully!')
"; then
        echo "ERROR: Package import test failed."
        SETUP_OK=false
    fi
    echo ""
fi

# ── Step 5: Print result ─────────────────────────────────

if [ "$SETUP_OK" = true ]; then
    echo "=========================================="
    echo "  Setup complete!"
    echo "=========================================="
    echo ""
    echo "Your conda environment is called '$ENV_NAME'."
    echo ""
    echo "To activate it in the terminal, run:"
    echo "  conda activate $ENV_NAME"
    echo ""
    echo "Next steps:"
    echo "  1. Open VS Code and run test-setup.ipynb (select the PSYC4411 kernel)"
    echo "  2. In the terminal, run:  conda activate $ENV_NAME && python test-setup.py"
    echo ""
else
    echo ""
    echo "=========================================="
    echo "  SETUP FAILED"
    echo "=========================================="
    echo ""
    echo "The setup did not complete successfully."
    echo ""
    echo "Try these steps:"
    echo "  1. Run:  conda clean --packages --tarballs -y"
    echo "  2. Run this setup script again"
    echo ""
    echo "If it still fails:"
    echo "  - Try:  conda clean --all -y  (clears the entire cache)"
    echo "  - Then run this setup script again"
    echo ""
    echo "Still stuck? Bring your laptop to the Week 2 class and"
    echo "we'll sort it out together. You can also paste the error"
    echo "message above into ChatGPT or Claude for help."
    echo ""
    exit 1
fi

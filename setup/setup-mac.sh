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

set -e  # Stop immediately if anything goes wrong

echo ""
echo "=========================================="
echo "  PSYC4411 Environment Setup (macOS)"
echo "=========================================="
echo ""

# ── Step 1: Check that conda is available ─────────────────

echo "Checking for conda..."

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
echo ""

# ── Step 2: Create (or recreate) the conda environment ───

ENV_NAME="psyc4411"

# Check if environment already exists
if conda env list | grep -q "^${ENV_NAME} "; then
    echo "The '$ENV_NAME' environment already exists."
    echo ""
    read -p "Do you want to remove it and start fresh? (y/n) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Removing existing environment..."
        conda env remove -n "$ENV_NAME" -y --quiet
        echo ""
    else
        echo "Keeping existing environment. Skipping to kernel registration..."
        echo ""
        # Jump ahead to kernel registration
        SKIP_CREATE=true
    fi
fi

if [ "${SKIP_CREATE}" != "true" ]; then
    echo "Creating conda environment '$ENV_NAME' from environment.yml..."
    echo "(This installs Python and all course packages — may take a few minutes)"
    echo ""
    conda env create -f environment.yml
    echo ""
fi

# ── Step 3: Register the Jupyter kernel ───────────────────

echo "Registering Jupyter kernel (so VS Code can find it)..."
conda run -n "$ENV_NAME" python -m ipykernel install --user --name="$ENV_NAME" --display-name="PSYC4411"
echo ""

# ── Step 4: Test that packages import correctly ──────────

echo "Testing that all packages load correctly..."
conda run -n "$ENV_NAME" python -c "
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
"

echo ""
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

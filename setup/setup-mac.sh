#!/bin/bash
# ============================================================
# PSYC4411 Setup Script — macOS / Linux
# ============================================================
# This script sets up everything you need for the course.
# It creates a virtual environment (a self-contained folder
# that keeps your course packages separate from everything
# else on your computer) and installs all required libraries.
#
# HOW TO RUN:
#   1. Open Terminal
#   2. Navigate to the setup folder:
#      cd path/to/Current-Advances-in-Psychological-Methods-and-Analyses-Repo/setup
#   3. Run:  bash setup-mac.sh
# ============================================================

set -e  # Stop immediately if anything goes wrong

echo ""
echo "=========================================="
echo "  PSYC4411 Environment Setup (macOS)"
echo "=========================================="
echo ""

# Step 1: Check Python is installed
echo "Checking for Python..."
if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
    PIP_CMD=pip3
elif command -v python &> /dev/null; then
    PYTHON_CMD=python
    PIP_CMD=pip
else
    echo ""
    echo "ERROR: Python is not installed or not found in your PATH."
    echo "Please install Python from https://www.python.org/downloads/"
    echo "Then re-run this script."
    exit 1
fi

PYTHON_VERSION=$($PYTHON_CMD --version 2>&1)
echo "Found: $PYTHON_VERSION"
echo ""

# Step 2: Create virtual environment
echo "Creating virtual environment (psyc4411-env)..."
echo "(This is a self-contained folder for your course packages)"
$PYTHON_CMD -m venv psyc4411-env

# Step 3: Activate virtual environment
echo "Activating virtual environment..."
source psyc4411-env/bin/activate

# Step 4: Upgrade pip
echo "Upgrading pip (the package installer)..."
pip install --upgrade pip --quiet

# Step 5: Install course packages
echo ""
echo "Installing course packages (this may take a few minutes)..."
echo "  - pandas (data analysis)"
echo "  - numpy (numerical computing)"
echo "  - matplotlib (plotting)"
echo "  - seaborn (statistical visualisation)"
echo "  - scikit-learn (machine learning)"
echo "  - jupyter & notebook (interactive notebooks)"
echo "  - ipykernel (Jupyter kernel support)"
echo ""
pip install pandas numpy matplotlib seaborn scikit-learn jupyter notebook ipykernel --quiet

# Step 6: Register the kernel so Jupyter/VS Code can find it
echo "Registering Jupyter kernel..."
python -m ipykernel install --user --name=psyc4411 --display-name="PSYC4411" --quiet 2>/dev/null || \
python -m ipykernel install --user --name=psyc4411 --display-name="PSYC4411"

# Step 7: Test that everything imports correctly
echo ""
echo "Testing that all packages load correctly..."
python -c "
import pandas as pd
import numpy as np
import matplotlib
import seaborn as sns
import sklearn
print('  pandas      ✓  (version ' + pd.__version__ + ')')
print('  numpy       ✓  (version ' + np.__version__ + ')')
print('  matplotlib  ✓  (version ' + matplotlib.__version__ + ')')
print('  seaborn     ✓  (version ' + sns.__version__ + ')')
print('  scikit-learn ✓  (version ' + sklearn.__version__ + ')')
print()
print('All packages installed successfully!')
"

echo ""
echo "=========================================="
echo "  Setup complete!"
echo "=========================================="
echo ""
echo "Your virtual environment is called 'psyc4411-env'."
echo ""
echo "To activate it later, run:"
echo "  source psyc4411-env/bin/activate"
echo ""
echo "Next step: Open VS Code and run test-setup.ipynb"
echo "to make sure everything works."
echo ""

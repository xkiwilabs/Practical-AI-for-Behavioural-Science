# ============================================================
# PSYC4411 Setup Script — Windows (PowerShell)
# ============================================================
# This script sets up everything you need for the course.
# It creates a virtual environment (a self-contained folder
# that keeps your course packages separate from everything
# else on your computer) and installs all required libraries.
#
# HOW TO RUN:
#   1. Open PowerShell (search "PowerShell" in the Start menu)
#   2. You may need to allow scripts to run. Type:
#      Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
#      (Press Y if asked to confirm)
#   3. Navigate to the setup folder:
#      cd path\to\Current-Advances-in-Psychological-Methods-and-Analyses-Repo\setup
#   4. Run:  .\setup-windows.ps1
# ============================================================

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "  PSYC4411 Environment Setup (Windows)"    -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

# Step 1: Check Python is installed
Write-Host "Checking for Python..."
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Found: $pythonVersion"
} catch {
    Write-Host ""
    Write-Host "ERROR: Python is not installed or not found in your PATH." -ForegroundColor Red
    Write-Host "Please install Python from https://www.python.org/downloads/" -ForegroundColor Red
    Write-Host "IMPORTANT: During installation, check the box that says" -ForegroundColor Yellow
    Write-Host "           'Add Python to PATH'" -ForegroundColor Yellow
    Write-Host "Then restart PowerShell and re-run this script."
    exit 1
}
Write-Host ""

# Step 2: Create virtual environment
Write-Host "Creating virtual environment (psyc4411-env)..."
Write-Host "(This is a self-contained folder for your course packages)"
python -m venv psyc4411-env

# Step 3: Activate virtual environment
Write-Host "Activating virtual environment..."
.\psyc4411-env\Scripts\Activate.ps1

# Step 4: Upgrade pip
Write-Host "Upgrading pip (the package installer)..."
pip install --upgrade pip --quiet

# Step 5: Install course packages
Write-Host ""
Write-Host "Installing course packages (this may take a few minutes)..."
Write-Host "  - pandas (data analysis)"
Write-Host "  - numpy (numerical computing)"
Write-Host "  - matplotlib (plotting)"
Write-Host "  - seaborn (statistical visualisation)"
Write-Host "  - scikit-learn (machine learning)"
Write-Host "  - jupyter & notebook (interactive notebooks)"
Write-Host "  - ipykernel (Jupyter kernel support)"
Write-Host ""
pip install pandas numpy matplotlib seaborn scikit-learn jupyter notebook ipykernel --quiet

# Step 6: Register the kernel so Jupyter/VS Code can find it
Write-Host "Registering Jupyter kernel..."
python -m ipykernel install --user --name=psyc4411 --display-name="PSYC4411"

# Step 7: Test that everything imports correctly
Write-Host ""
Write-Host "Testing that all packages load correctly..."
python -c @"
import pandas as pd
import numpy as np
import matplotlib
import seaborn as sns
import sklearn
print('  pandas       (version ' + pd.__version__ + ')')
print('  numpy        (version ' + np.__version__ + ')')
print('  matplotlib   (version ' + matplotlib.__version__ + ')')
print('  seaborn      (version ' + sns.__version__ + ')')
print('  scikit-learn (version ' + sklearn.__version__ + ')')
print()
print('All packages installed successfully!')
"@

Write-Host ""
Write-Host "==========================================" -ForegroundColor Green
Write-Host "  Setup complete!"                          -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Your virtual environment is called 'psyc4411-env'."
Write-Host ""
Write-Host "To activate it later, run:"
Write-Host "  .\psyc4411-env\Scripts\Activate.ps1"
Write-Host ""
Write-Host "Next step: Open VS Code and run test-setup.ipynb"
Write-Host "to make sure everything works."
Write-Host ""

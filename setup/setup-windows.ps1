# ============================================================
# PSYC4411 Setup Script — Windows (PowerShell)
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
#   1. Open PowerShell (search "PowerShell" in the Start menu)
#   2. You may need to allow scripts to run. Type:
#      Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
#      (Press Y if asked to confirm)
#   3. Navigate to the setup folder:
#      cd path\to\Practical-AI-for-Behavioural-Science\setup
#   4. Run:  .\setup-windows.ps1
# ============================================================

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "  PSYC4411 Environment Setup (Windows)"    -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

# ── Step 1: Check that conda is available ─────────────────

Write-Host "Checking for conda..."

try {
    $condaVersion = conda --version 2>&1
    Write-Host "Found: $condaVersion"
} catch {
    Write-Host ""
    Write-Host "ERROR: conda is not installed or not found in your PATH." -ForegroundColor Red
    Write-Host ""
    Write-Host "Please install Miniconda first:" -ForegroundColor Yellow
    Write-Host "  https://docs.anaconda.com/miniconda/" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "During installation, make sure to check:" -ForegroundColor Yellow
    Write-Host "  'Add Miniconda to my PATH environment variable'" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "After installing, close and reopen PowerShell, then run this script again."
    exit 1
}
Write-Host ""

# ── Step 2: Create (or recreate) the conda environment ───

$envName = "psyc4411"

# Check if environment already exists
$envList = conda env list 2>&1
if ($envList -match "^$envName\s") {
    Write-Host "The '$envName' environment already exists."
    Write-Host ""
    $response = Read-Host "Do you want to remove it and start fresh? (y/n)"
    if ($response -match "^[Yy]") {
        Write-Host "Removing existing environment..."
        conda env remove -n $envName -y --quiet
        Write-Host ""
    } else {
        Write-Host "Keeping existing environment. Skipping to kernel registration..."
        Write-Host ""
        $skipCreate = $true
    }
}

if (-not $skipCreate) {
    Write-Host "Creating conda environment '$envName' from environment.yml..."
    Write-Host "(This installs Python and all course packages - may take a few minutes)"
    Write-Host ""
    conda env create -f environment.yml
    Write-Host ""
}

# ── Step 3: Register the Jupyter kernel ───────────────────

Write-Host "Registering Jupyter kernel (so VS Code can find it)..."
conda run -n $envName python -m ipykernel install --user --name=$envName --display-name="PSYC4411"
Write-Host ""

# ── Step 4: Test that packages import correctly ──────────

Write-Host "Testing that all packages load correctly..."
conda run -n $envName python -c @"
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
"@

Write-Host ""
Write-Host "==========================================" -ForegroundColor Green
Write-Host "  Setup complete!"                          -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Your conda environment is called '$envName'."
Write-Host ""
Write-Host "To activate it in the terminal, run:"
Write-Host "  conda activate $envName"
Write-Host ""
Write-Host "Next steps:"
Write-Host "  1. Open VS Code and run test-setup.ipynb (select the PSYC4411 kernel)"
Write-Host "  2. In the terminal, run:  conda activate $envName && python test-setup.py"
Write-Host ""

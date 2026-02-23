# ============================================================
# PSYC4411 Setup Script - Windows (PowerShell)
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

# -- Helper: check exit code after external commands --------
# PowerShell does NOT automatically stop on non-zero exit codes
# from external programs (like conda). This function does.
function Assert-ExitCode {
    param([string]$StepName)
    if ($LASTEXITCODE -ne 0) {
        Write-Host ""
        Write-Host "ERROR: '$StepName' failed (exit code $LASTEXITCODE)." -ForegroundColor Red
        return $false
    }
    return $true
}

# -- Track overall success -----------------------------------
$setupOK = $true

Write-Host ""
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "  PSYC4411 Environment Setup (Windows)"    -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

# -- Step 1: Check that conda is available ------------------

Write-Host "Step 1: Checking for conda..."

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

# Detect Anaconda vs Miniconda
$condaInfo = conda info --json 2>&1 | ConvertFrom-Json
$condaRoot = $condaInfo.root_prefix
if ($condaRoot -match "anaconda") {
    Write-Host "  (Using Anaconda - that works perfectly fine for this course)" -ForegroundColor DarkGray
}
Write-Host ""

# -- Step 2: Create (or recreate) the conda environment -----

$envName = "psyc4411"
$skipCreate = $false

# Check if environment already exists
$envList = conda env list 2>&1
if ($envList -match "(?m)^$envName\s") {
    Write-Host "The '$envName' environment already exists."
    Write-Host ""
    $response = Read-Host "Do you want to remove it and start fresh? (y/n)"
    if ($response -match "^[Yy]") {
        Write-Host "Removing existing environment..."
        conda env remove -n $envName -y --quiet 2>&1 | Out-Null
        if (-not (Assert-ExitCode "conda env remove")) {
            Write-Host "Could not remove the existing environment." -ForegroundColor Red
            Write-Host "Try manually: conda env remove -n $envName" -ForegroundColor Yellow
            $setupOK = $false
        }
        Write-Host ""
    } else {
        Write-Host "Keeping existing environment. Skipping to kernel registration..."
        Write-Host ""
        $skipCreate = $true
    }
}

if ($setupOK -and (-not $skipCreate)) {
    Write-Host "Step 2: Creating conda environment '$envName' from environment.yml..."
    Write-Host "(This installs Python and all course packages - may take a few minutes)"
    Write-Host ""

    conda env create -f environment.yml 2>&1
    $createOK = Assert-ExitCode "conda env create"

    # If creation failed, try cleaning the cache and retrying once
    if (-not $createOK) {
        Write-Host ""
        Write-Host "Environment creation failed. Clearing conda package cache and retrying..." -ForegroundColor Yellow
        Write-Host "(This fixes corrupted downloads, which is the most common cause)" -ForegroundColor DarkGray
        Write-Host ""

        conda clean --packages --tarballs -y 2>&1 | Out-Null

        # Remove the partially-created environment if it exists
        $envListRetry = conda env list 2>&1
        if ($envListRetry -match "(?m)^$envName\s") {
            conda env remove -n $envName -y --quiet 2>&1 | Out-Null
        }

        Write-Host "Retrying environment creation..."
        conda env create -f environment.yml 2>&1
        $createOK = Assert-ExitCode "conda env create (retry)"
    }

    if (-not $createOK) {
        $setupOK = $false
    } else {
        # Verify the environment actually exists
        $envListCheck = conda env list 2>&1
        if ($envListCheck -notmatch "(?m)^$envName\s") {
            Write-Host ""
            Write-Host "ERROR: conda reported success, but the '$envName' environment was not found." -ForegroundColor Red
            $setupOK = $false
        } else {
            Write-Host "Environment '$envName' created successfully." -ForegroundColor Green
        }
    }
    Write-Host ""
}

# -- Step 3: Register the Jupyter kernel --------------------

if ($setupOK) {
    Write-Host "Step 3: Registering Jupyter kernel (so VS Code can find it)..."
    conda run -n $envName python -m ipykernel install --user --name=$envName --display-name="PSYC4411" 2>&1
    if (-not (Assert-ExitCode "kernel registration")) {
        $setupOK = $false
    }
    Write-Host ""
}

# -- Step 4: Test that packages import correctly -----------

if ($setupOK) {
    Write-Host "Step 4: Testing that all packages load correctly..."
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
    if (-not (Assert-ExitCode "package import test")) {
        $setupOK = $false
    }
    Write-Host ""
}

# -- Step 5: Print result ------------------------------------

if ($setupOK) {
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
} else {
    Write-Host ""
    Write-Host "==========================================" -ForegroundColor Red
    Write-Host "  SETUP FAILED"                             -ForegroundColor Red
    Write-Host "==========================================" -ForegroundColor Red
    Write-Host ""
    Write-Host "The setup did not complete successfully." -ForegroundColor Red
    Write-Host ""
    Write-Host "Try these steps:" -ForegroundColor Yellow
    Write-Host "  1. Run:  conda clean --packages --tarballs -y" -ForegroundColor Yellow
    Write-Host "  2. Run this setup script again" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "If it still fails:" -ForegroundColor Yellow
    Write-Host "  - Try:  conda clean --all -y  (clears the entire cache)" -ForegroundColor Yellow
    Write-Host "  - Then run this setup script again" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Still stuck? Bring your laptop to the Week 2 class and" -ForegroundColor Cyan
    Write-Host "we'll sort it out together. You can also paste the error" -ForegroundColor Cyan
    Write-Host "message above into ChatGPT or Claude for help." -ForegroundColor Cyan
    Write-Host ""
    exit 1
}

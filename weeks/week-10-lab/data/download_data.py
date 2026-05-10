"""
Download data for Week 10: Neural Network Training
====================================================

Run this script BEFORE class to download the datasets you'll need.

    conda activate psyc4411-env
    cd weeks/week-10-lab/data
    python download_data.py

This downloads:
  1. EEG Motor Movement/Imagery dataset (main challenge)
     — pre-extracted features from PhysioNet's 109-participant BCI study

Total download size: ~6 MB (pre-extracted features only).
Files are saved to this folder.
If files already exist, they won't be re-downloaded.

NOTE: The raw EEG data (1.5 GB) is NOT downloaded — we provide
pre-extracted features so you can focus on building neural networks,
not EEG preprocessing.
"""

import sys
from pathlib import Path
from urllib.request import urlretrieve
from urllib.error import URLError

HERE = Path(__file__).resolve().parent

# GitHub Releases URL for pre-extracted features
EEG_URL = "https://github.com/xkiwilabs/Practical-AI-for-Behavioural-Science/releases/download/v1.0-data/eeg_motor_imagery_features.csv"
EEG_FILE = HERE / "eeg_motor_imagery_features.csv"


def download_file(url, dest, description):
    """Download a file with progress indication."""
    if dest.exists():
        print(f"  Already exists: {dest.name} — skipping")
        return True

    print(f"  Downloading {description}...")
    try:
        urlretrieve(url, dest)
        size_mb = dest.stat().st_size / (1024 * 1024)
        print(f"  Saved: {dest.name} ({size_mb:.1f} MB)")
        return True
    except URLError as e:
        print(f"  ERROR: Could not download {description}: {e}")
        return False


def download_eeg_features():
    """Download pre-extracted EEG features for the motor imagery challenge."""
    print()
    print("=" * 60)
    print("EEG Motor Imagery — Pre-extracted Features (main challenge)")
    print("=" * 60)
    print()
    print("Source: PhysioNet EEG Motor Movement/Imagery Dataset")
    print("  https://physionet.org/content/eegmmidb/1.0.0/")
    print("109 participants | 64-channel EEG | Motor imagery classification")
    print()

    return download_file(
        EEG_URL,
        EEG_FILE,
        "EEG motor imagery features (6 MB)"
    )


if __name__ == "__main__":
    print("PSYC4411 Week 10 — Data Download")
    print("=================================")
    print()
    print("This script downloads the datasets for Week 10's lab challenge.")
    print("Make sure you have an internet connection.")

    ok = download_eeg_features()

    print()
    print("=" * 60)
    if ok:
        print("Download complete! You're ready for Week 10.")
        print()
        print("Dataset: eeg_motor_imagery_features.csv")
        print("  4,918 trials from 109 participants")
        print("  320 EEG features (64 channels × 5 frequency bands)")
        print("  Binary target: left (0) vs right (1) hand imagery")
    else:
        print("Some downloads failed. Check the errors above.")
        print("You can re-run this script — it will skip files already downloaded.")
        sys.exit(1)

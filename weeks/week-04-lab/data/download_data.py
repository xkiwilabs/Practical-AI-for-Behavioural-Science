"""
Download data for Week 4: Regression Pipeline
==============================================

Run this script BEFORE class to download the datasets you'll need.

    conda activate psyc4411-env
    cd weeks/week-04-lab/data
    python download_data.py

This downloads:
  1. OpenPsychometrics DASS-42 dataset (main challenge) — 39,775 respondents
  2. Boston College COVID Sleep & Wellbeing dataset (bonus challenge)

Total download size: ~25 MB. Files are saved to this folder.
If files already exist, they won't be re-downloaded.
"""

import os
import sys
import zipfile
import json
from pathlib import Path
from urllib.request import urlopen, urlretrieve, Request
from urllib.error import URLError

HERE = Path(__file__).resolve().parent


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


def download_openpsychometrics():
    """Download and extract the OpenPsychometrics DASS-42 dataset."""
    print()
    print("=" * 60)
    print("1. OpenPsychometrics DASS-42 (main challenge)")
    print("=" * 60)
    print()
    print("Source: https://openpsychometrics.org/_rawdata/")
    print("39,775 respondents | DASS-42 + Big Five + demographics")
    print()

    data_file = HERE / "dass42_data.csv"
    codebook_file = HERE / "dass42_codebook.txt"

    if data_file.exists() and codebook_file.exists():
        print("  Both files already exist — skipping download")
        return True

    zip_url = "https://openpsychometrics.org/_rawdata/DASS_data_21.02.19.zip"
    zip_path = HERE / "DASS_data_21.02.19.zip"

    if not download_file(zip_url, zip_path, "DASS-42 dataset (6.8 MB)"):
        return False

    print("  Extracting...")
    try:
        with zipfile.ZipFile(zip_path, "r") as zf:
            # Extract data.csv and codebook.txt, renaming for clarity
            for member in zf.namelist():
                if member.endswith("data.csv"):
                    with zf.open(member) as src, open(data_file, "wb") as dst:
                        dst.write(src.read())
                    print(f"  Extracted: {data_file.name}")
                elif member.endswith("codebook.txt"):
                    with zf.open(member) as src, open(codebook_file, "wb") as dst:
                        dst.write(src.read())
                    print(f"  Extracted: {codebook_file.name}")

        # Clean up zip
        zip_path.unlink()
        print("  Removed ZIP file")
        return True
    except zipfile.BadZipFile:
        print("  ERROR: Downloaded file is not a valid ZIP")
        return False


def download_boston_college():
    """Download the Boston College COVID Sleep & Wellbeing dataset."""
    print()
    print("=" * 60)
    print("2. Boston College COVID Sleep & Wellbeing (bonus challenge)")
    print("=" * 60)
    print()
    print("Source: https://osf.io/gpxwa/")
    print("~1,484 participants | PHQ-9 + sleep + lifestyle + personality")
    print()

    bc_dir = HERE / "boston_college"
    bc_dir.mkdir(exist_ok=True)

    # Files to download from the "Most Recent Data" folder on OSF
    files = {
        "demographics.csv": {
            "url": "https://osf.io/download/cnrsj/",
            "desc": "demographics (223 KB)",
        },
        "daily_survey.csv": {
            "url": "https://osf.io/download/duwv4/",
            "desc": "daily survey — this is the big one (20 MB)",
        },
        "round1_assessment.csv": {
            "url": "https://osf.io/download/kv8yx/",
            "desc": "Round 1 assessment (668 KB)",
        },
        "round2_assessment.csv": {
            "url": "https://osf.io/download/j57pm/",
            "desc": "Round 2 assessment (385 KB)",
        },
    }

    success = True
    for filename, info in files.items():
        dest = bc_dir / filename
        if not download_file(info["url"], dest, info["desc"]):
            success = False

    return success


if __name__ == "__main__":
    print("PSYC4411 Week 4 — Data Download")
    print("================================")
    print()
    print("This script downloads the datasets for Week 4's lab challenge.")
    print("Make sure you have an internet connection.")

    ok1 = download_openpsychometrics()
    ok2 = download_boston_college()

    print()
    print("=" * 60)
    if ok1 and ok2:
        print("All downloads complete!")
        print()
        print("You should now have:")
        print(f"  {HERE / 'dass42_data.csv'}")
        print(f"  {HERE / 'dass42_codebook.txt'}")
        print(f"  {HERE / 'boston_college' / 'demographics.csv'}")
        print(f"  {HERE / 'boston_college' / 'daily_survey.csv'}")
        print(f"  {HERE / 'boston_college' / 'round1_assessment.csv'}")
        print(f"  {HERE / 'boston_college' / 'round2_assessment.csv'}")
        print()
        print("You're ready for Week 4!")
    else:
        print("Some downloads failed. Check the errors above.")
        print("You can re-run this script — it will skip files already downloaded.")
        sys.exit(1)

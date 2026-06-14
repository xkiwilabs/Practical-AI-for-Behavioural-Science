"""
Download data for Week 6: Trees & Ensembles (Classification)
=============================================================

Run this script BEFORE class to download the datasets you'll need.

    conda activate ai-behsci
    cd weeks/week-06-lab/data
    python download_data.py

This downloads:
  1. Boston College COVID Sleep & Wellbeing dataset (main challenge)
     — demographics, daily surveys, and assessment rounds

Total download size: ~22 MB. Files are saved to this folder.
If files already exist, they won't be re-downloaded.
"""

import sys
from pathlib import Path
from urllib.request import urlretrieve
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


def download_boston_college():
    """Download the Boston College COVID Sleep & Wellbeing dataset."""
    print()
    print("=" * 60)
    print("Boston College COVID Sleep & Wellbeing (main challenge)")
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
    print("Week 6 — Data Download")
    print("================================")
    print()
    print("This script downloads the datasets for Week 6's lab challenge.")
    print("Make sure you have an internet connection.")

    ok = download_boston_college()

    print()
    print("=" * 60)
    if ok:
        print("All downloads complete!")
        print()
        print("You should now have:")
        print(f"  {HERE / 'boston_college' / 'demographics.csv'}")
        print(f"  {HERE / 'boston_college' / 'daily_survey.csv'}")
        print(f"  {HERE / 'boston_college' / 'round1_assessment.csv'}")
        print(f"  {HERE / 'boston_college' / 'round2_assessment.csv'}")
        print()
        print("You're ready for Week 6!")
    else:
        print("Some downloads failed. Check the errors above.")
        print("You can re-run this script — it will skip files already downloaded.")
        sys.exit(1)

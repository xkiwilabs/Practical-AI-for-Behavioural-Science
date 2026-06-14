"""
Download data for Week 8: PCA/UMAP & Clustering
=================================================

Run this script BEFORE class to download the datasets you'll need.

    conda activate ai-behsci
    cd weeks/week-08-lab/data
    python download_data.py

This downloads:
  1. OpenPsychometrics DASS-42 dataset (main challenge) — 39,775 respondents

Total download size: ~7 MB. Files are saved to this folder.
If files already exist, they won't be re-downloaded.
"""

import sys
import zipfile
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


def download_openpsychometrics():
    """Download and extract the OpenPsychometrics DASS-42 dataset."""
    print()
    print("=" * 60)
    print("OpenPsychometrics DASS-42 (main challenge)")
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


if __name__ == "__main__":
    print("Week 8 — Data Download")
    print("================================")
    print()
    print("This script downloads the datasets for Week 8's lab challenge.")
    print("Make sure you have an internet connection.")

    ok = download_openpsychometrics()

    print()
    print("=" * 60)
    if ok:
        print("All downloads complete!")
        print()
        print("You should now have:")
        print(f"  {HERE / 'dass42_data.csv'}")
        print(f"  {HERE / 'dass42_codebook.txt'}")
        print()
        print("You're ready for Week 8!")
    else:
        print("Some downloads failed. Check the errors above.")
        print("You can re-run this script — it will skip files already downloaded.")
        sys.exit(1)

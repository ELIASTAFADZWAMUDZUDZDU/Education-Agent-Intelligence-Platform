"""
------------------------------------------------------------
Project : Education Agent Intelligence Platform
Module  : Data Pipeline
Purpose : Merge all raw Excel files into a single dataset
Author  : Elias Tafadzwa Mudzudzu
------------------------------------------------------------
"""

# ==========================
# Imports
# ==========================

from pathlib import Path
import pandas as pd


# ==========================
# Paths
# ==========================

RAW_DATA_DIR = Path("data/raw")
PROCESSED_DATA_DIR = Path("data/processed")
OUTPUT_FILE = PROCESSED_DATA_DIR / "merged_agents.xlsx"


# ==========================
# Create Output Directory
# ==========================

PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)


# ==========================
# Locate Excel Files
# ==========================

excel_files = list(RAW_DATA_DIR.glob("*.xlsx"))

if not excel_files:
    raise FileNotFoundError("No Excel files found in data/raw/")


# ==========================
# Read and Merge Files
# ==========================

dataframes = []

print("=" * 60)
print("Merging Education Agent Data")
print("=" * 60)

for file in excel_files:

    print(f"Reading: {file.name}")

    df = pd.read_excel(file)

    # Track where each record came from
    df["source_file"] = file.name

    dataframes.append(df)

merged_df = pd.concat(dataframes, ignore_index=True)


# ==========================
# Save Merged Dataset
# ==========================

merged_df.to_excel(OUTPUT_FILE, index=False)


# ==========================
# Summary
# ==========================

print("\n" + "=" * 60)
print("Merge Completed Successfully")
print("=" * 60)
print(f"Files Processed : {len(excel_files)}")
print(f"Total Records   : {len(merged_df)}")
print(f"Output File     : {OUTPUT_FILE}")
print("=" * 60)
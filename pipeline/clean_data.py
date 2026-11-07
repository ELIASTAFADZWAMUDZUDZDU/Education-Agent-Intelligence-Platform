"""
------------------------------------------------------------
Project : Education Agent Intelligence Platform
Module  : Data Pipeline
Purpose : Clean merged education agent dataset
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

PROCESSED_DATA_DIR = Path("data/processed")

INPUT_FILE = PROCESSED_DATA_DIR / "merged_agents.xlsx"
OUTPUT_FILE = PROCESSED_DATA_DIR / "cleaned_agents.xlsx"


# ==========================
# Load Dataset
# ==========================

print("=" * 60)
print("Cleaning Education Agent Dataset")
print("=" * 60)

df = pd.read_excel(INPUT_FILE)

print(f"Initial Records : {len(df)}")


# ==========================
# Standardize Column Names
# ==========================

df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
      .str.replace(r"[^\w]", "", regex=True)
)


# ==========================
# Rename Columns
# ==========================

df.rename(columns={
    "contact": "contact_number",
    "location": "office_address"
}, inplace=True)


# ==========================
# Merge Equivalent Columns
# ==========================

# Merge source information columns
if (
    "sources_of_information" in df.columns and
    "source_of_information" in df.columns
):
    df["source_of_information"] = (
        df["source_of_information"]
        .fillna(df["sources_of_information"])
    )

    df.drop(columns=["sources_of_information"], inplace=True)


# Merge specialized countries columns
if (
    "specialized_countries" in df.columns and
    "specialization_countries" in df.columns
):
    df["specialized_countries"] = (
        df["specialized_countries"]
        .fillna(df["specialization_countries"])
    )

    df.drop(columns=["specialization_countries"], inplace=True)


# ==========================
# Standardize Missing Values
# ==========================

missing_values = [
    "",
    " ",
    "N/A",
    "NA",
    "n/a",
    "na",
    "-",
    "--",
    "None",
    "none",
    "NULL",
    "null",
    "Unknown",
    "unknown"
]

df.replace(missing_values, pd.NA, inplace=True)


# ==========================
# Remove Empty Rows
# ==========================

df.dropna(how="all", inplace=True)


# ==========================
# Trim Whitespace
# ==========================

text_columns = df.select_dtypes(include="object").columns

for column in text_columns:
    df[column] = df[column].str.strip()


# ==========================
# Remove Duplicate Rows
# ==========================

df.drop_duplicates(inplace=True)


# ==========================
# Remove Duplicate Columns
# ==========================

df = df.loc[:, ~df.columns.duplicated()]


# ==========================
# Reset Index
# ==========================

df.reset_index(drop=True, inplace=True)


# ==========================
# Save Clean Dataset
# ==========================

df.to_excel(OUTPUT_FILE, index=False)


# ==========================
# Summary
# ==========================

print("\n" + "=" * 60)
print("Cleaning Completed Successfully")
print("=" * 60)
print(f"Final Records : {len(df)}")
print(f"Total Columns : {len(df.columns)}")
print(f"Output File   : {OUTPUT_FILE}")
print("=" * 60)

print("\nFinal Columns:")
print(df.columns.tolist())
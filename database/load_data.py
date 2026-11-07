"""
------------------------------------------------------------
Project : Education Agent Intelligence Platform
Module  : Database
Purpose : Load cleaned education agent data into PostgreSQL
Author  : Elias Tafadzwa Mudzudzu
------------------------------------------------------------
"""

# ==========================
# Imports
# ==========================

from pathlib import Path
import pandas as pd

from database.connection import get_connection


# ==========================
# Paths
# ==========================

INPUT_FILE = Path("data/processed/cleaned_agents.xlsx")


# ==========================
# Helper Function
# ==========================

def clean_value(value):
    """
    Converts invalid values to None for PostgreSQL.
    """

    if pd.isna(value):
        return None

    value = str(value).strip()

    if value.lower() in (
        "",
        "nan",
        "none",
        "null",
        "n/a",
        "na",
        "-",
        "--"
    ):
        return None

    return value


# ==========================
# Load Dataset
# ==========================

print("=" * 60)
print("Loading Education Agent Dataset")
print("=" * 60)

df = pd.read_excel(
    INPUT_FILE,
    keep_default_na=False
)

print(f"Records Found : {len(df)}")


# ==========================
# Database Load
# ==========================

connection = None
cursor = None

try:

    connection = get_connection()
    cursor = connection.cursor()

    # Development Only
    cursor.execute(
        "TRUNCATE TABLE education_agents RESTART IDENTITY;"
    )

    insert_query = """
    INSERT INTO education_agents (

        consultant_name,
        website_url,
        specialized_countries,
        services_offered,
        office_address,
        contact_number,
        country,
        social_media_links,
        source_of_information,
        years_in_operation,
        whatsapp_number,
        source_file

    )

    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    records = [

        (

            clean_value(row["consultant_name"]),
            clean_value(row["website_url"]),
            clean_value(row["specialized_countries"]),
            clean_value(row["services_offered"]),
            clean_value(row["office_address"]),
            clean_value(row["contact_number"]),
            clean_value(row["country"]),
            clean_value(row["social_media_links"]),
            clean_value(row["source_of_information"]),
            clean_value(row["years_in_operation"]),
            clean_value(row["whatsapp_number"]),
            clean_value(row["source_file"])

        )

        for _, row in df.iterrows()

    ]

    cursor.executemany(
        insert_query,
        records
    )

    connection.commit()

    print("\n" + "=" * 60)
    print("Data Loaded Successfully")
    print("=" * 60)
    print(f"Inserted Records : {len(records)}")
    print("=" * 60)

except Exception as e:

    if connection:
        connection.rollback()

    print(f"Error: {e}")

finally:

    if cursor:
        cursor.close()

    if connection:
        connection.close()
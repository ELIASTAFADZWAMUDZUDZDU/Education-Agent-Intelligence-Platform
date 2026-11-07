"""
------------------------------------------------------------
Project : Education Agent Intelligence Platform
Module  : Dashboard
Purpose : Database Query Functions
Author  : Elias Tafadzwa Mudzudzu
------------------------------------------------------------
"""

# ==========================
# Imports
# ==========================
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))


import pandas as pd

from database.connection import get_connection


# ==========================
# Get Entire Dataset
# ==========================

def get_all_agents():
    """
    Returns the complete education agent dataset.
    """

    connection = get_connection()

    query = """
        SELECT *
        FROM education_agents
        ORDER BY consultant_name;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


# ==========================
# Get Countries
# ==========================

def get_countries():

    connection = get_connection()

    query = """
        SELECT DISTINCT country
        FROM education_agents
        WHERE country IS NOT NULL
        ORDER BY country;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df["country"].tolist()


# ==========================
# Get Services
# ==========================

def get_services():

    connection = get_connection()

    query = """
        SELECT DISTINCT services_offered
        FROM education_agents
        WHERE services_offered IS NOT NULL
        ORDER BY services_offered;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df["services_offered"].tolist()


# ==========================
# Get Destination Countries
# ==========================

def get_destinations():

    connection = get_connection()

    query = """
        SELECT DISTINCT specialized_countries
        FROM education_agents
        WHERE specialized_countries IS NOT NULL
        ORDER BY specialized_countries;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df["specialized_countries"].tolist()


# ==========================
# Search Dataset
# ==========================

def search_agents(search_text="", country="All", service="All", destination="All"):
    """
    Returns filtered education agents.
    """

    df = get_all_agents()

    # Search by consultant name
    if search_text:
        df = df[
            df["consultant_name"]
            .str.contains(search_text, case=False, na=False)
        ]

    # Filter by country
    if country != "All":
        df = df[df["country"] == country]

    # Filter by services
    if service != "All":
        df = df[df["services_offered"] == service]

    # Filter by destination
    if destination != "All":
        df = df[
            df["specialized_countries"] == destination
        ]

    return df
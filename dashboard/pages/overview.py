"""
------------------------------------------------------------
Project : Education Agent Intelligence Platform
Module  : Dashboard
Purpose : Overview Page
Author  : Elias Tafadzwa Mudzudzu
------------------------------------------------------------
"""

# ==========================
# Imports
# ==========================

import streamlit as st

from db_queries import get_all_agents


# ==========================
# Overview
# ==========================

def show_overview():

    st.title("🌍 Education Agent Intelligence Platform")

    st.write("""
    Explore verified education consultants and recruitment agencies
    across **Africa** and **Papua New Guinea**.

    Search, filter and explore the database below.
    """)

    st.divider()

    # Load Data
    df = get_all_agents()

    # --------------------------
    # Search
    # --------------------------

    search = st.text_input(
        "🔍 Search Consultant",
        placeholder="Type consultant name..."
    )

    if search:

        df = df[
            df["consultant_name"]
            .str.contains(search, case=False, na=False)
        ]

    # --------------------------
    # Country Filter
    # --------------------------

    countries = ["All"] + sorted(df["country"].dropna().unique())

    selected_country = st.selectbox(
        "Country",
        countries
    )

    if selected_country != "All":

        df = df[
            df["country"] == selected_country
        ]

    st.write(f"**Showing {len(df)} Consultants**")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )
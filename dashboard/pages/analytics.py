"""
------------------------------------------------------------
Project : Education Agent Intelligence Platform
Module  : Dashboard
Purpose : Analytics Dashboard
Author  : Elias Tafadzwa Mudzudzu
------------------------------------------------------------
"""

# ==========================
# Imports
# ==========================

import streamlit as st
import plotly.express as px

from dashboard.db_queries import get_all_agents


# ==========================
# Helper Function
# ==========================

def count_available(series):
    """
    Counts valid (non-empty) values in a column.
    """

    return (
        series.fillna("")
              .astype(str)
              .str.strip()
              .replace(["", "nan", "None", "NULL"], "")
              .ne("")
              .sum()
    )


# ==========================
# Analytics Dashboard
# ==========================

def show_analytics():

    st.title("📊 Analytics Dashboard")

    df = get_all_agents()

    # ==========================
    # KPI Cards
    # ==========================

    total_agents = len(df)

    countries = df["country"].nunique()

    websites = count_available(df["website_url"])

    whatsapp = count_available(df["whatsapp_number"])

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Consultants", total_agents)
    col2.metric("Countries Covered", countries)
    col3.metric("Websites Available", websites)
    col4.metric("WhatsApp Available", whatsapp)

    st.divider()

    # ==========================
    # Consultants by Country
    # ==========================

    left, right = st.columns(2)

    with left:

        country_df = (
            df.groupby("country")
              .size()
              .reset_index(name="Consultants")
              .sort_values(
                  by="Consultants",
                  ascending=False
              )
        )

        fig = px.bar(
            country_df,
            x="country",
            y="Consultants",
            text="Consultants",
            title="Consultants by Country"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ==========================
    # Services Offered
    # ==========================

    with right:

        services_df = (
            df.groupby("services_offered")
              .size()
              .reset_index(name="Total")
        )

        fig = px.pie(
            services_df,
            names="services_offered",
            values="Total",
            title="Services Offered"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    # ==========================
    # Data Quality
    # ==========================

    st.subheader("📋 Data Quality")

    website_missing = total_agents - websites
    whatsapp_missing = total_agents - whatsapp

    quality = {
        "Field": [
            "Website",
            "WhatsApp"
        ],
        "Available": [
            websites,
            whatsapp
        ],
        "Missing": [
            website_missing,
            whatsapp_missing
        ]
    }

    st.dataframe(
        quality,
        use_container_width=True,
        hide_index=True
    )

    # ==========================
    # Debug (Temporary)
    # ==========================

    with st.expander("🔧 Debug WhatsApp Column"):

        st.write("Sample WhatsApp Values")

        st.write(df["whatsapp_number"].head(20))

        st.write("Missing Values")

        st.write(df["whatsapp_number"].isna().sum())

        st.write("Available Values Count")

        st.write(count_available(df["whatsapp_number"]))
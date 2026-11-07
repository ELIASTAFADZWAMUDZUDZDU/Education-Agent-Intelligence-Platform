"""
------------------------------------------------------------
Project : Education Agent Intelligence Platform
Module  : Dashboard
Purpose : Export Page
Author  : Elias Tafadzwa Mudzudzu
------------------------------------------------------------
"""

# ==========================
# Imports
# ==========================

import streamlit as st

from db_queries import get_all_agents
from export_utils import to_excel, to_csv


# ==========================
# Export Page
# ==========================

def show_export():

    st.title("📤 Export Data")

    st.write(
        """
        Download the education agent database in your preferred format.
        """
    )

    st.divider()

    df = get_all_agents()

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(

            label="📥 Download Excel",

            data=to_excel(df),

            file_name="education_agents.xlsx",

            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

        )

    with col2:

        st.download_button(

            label="📄 Download CSV",

            data=to_csv(df),

            file_name="education_agents.csv",

            mime="text/csv"

        )

    st.divider()

    st.subheader("Dataset Preview")

    st.dataframe(
        df.head(20),
        use_container_width=True,
        hide_index=True
    )
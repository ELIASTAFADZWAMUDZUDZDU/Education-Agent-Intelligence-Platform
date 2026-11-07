"""
------------------------------------------------------------
Project : Education Agent Intelligence Platform
Module  : Dashboard
Purpose : AI Search Interface
Author  : Elias Tafadzwa Mudzudzu
------------------------------------------------------------
"""

# ==========================
# Imports
# ==========================

import streamlit as st

from dashboard.ai_engine import ask_ai


# ==========================
# AI Search Page
# ==========================

def show_ai_search():

    st.title("🤖 AI Data Assistant")

    st.write(
        """
        Ask questions about education consultants using
        natural language.
        """
    )

    st.info(
        """
        Try questions like:

        • Show all consultants

        • Show consultants in Kenya

        • Show consultants in Zimbabwe

        • Show consultants with websites

        • Show consultants without websites

        • Show consultants with WhatsApp

        • Show consultants without WhatsApp

        • Show consultants recruiting students to Australia

        • Show consultants recruiting students to Canada

        • Show visa consultants

        • Show scholarship consultants

        • How many consultants are in Kenya?
        """
    )

    query = st.text_input(
        "Ask your question..."
    )

    if st.button("Search"):

        if query.strip() == "":

            st.warning("Please enter a question.")
            return

        result = ask_ai(query)

        st.success(result["message"])

        if not result["data"].empty:

            st.dataframe(
                result["data"],
                use_container_width=True,
                hide_index=True
            )
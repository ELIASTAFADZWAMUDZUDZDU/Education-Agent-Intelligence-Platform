"""
------------------------------------------------------------
Project : Education Agent Intelligence Platform
Module  : Dashboard
Purpose : Main Streamlit Application
Author  : Elias Tafadzwa Mudzudzu
------------------------------------------------------------
"""

# ==========================
# Imports
# ==========================

import streamlit as st

from pages.overview import show_overview
from pages.analytics import show_analytics
from pages.export import show_export
from pages.ai_search import show_ai_search


# ==========================
# Page Configuration
# ==========================

st.set_page_config(
    page_title="Education Agent Intelligence Platform",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================
# Sidebar
# ==========================

st.sidebar.title("🌍 EAIP")

st.sidebar.markdown(
    "Education Agent Intelligence Platform"
)

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    (
        "🌍 Overview",
        "📊 Analytics",
        "📤 Export Data",
        "🤖 AI Assistant"
    )
)


# ==========================
# Navigation
# ==========================

if page == "🌍 Overview":
    show_overview()

elif page == "📊 Analytics":
    show_analytics()

elif page == "📤 Export Data":
    show_export()

elif page == "🤖 AI Assistant":
    show_ai_search()


# ==========================
# Footer
# ==========================

st.sidebar.divider()

st.sidebar.caption(
    "Developed by Elias Tafadzwa Mudzudzu"
)
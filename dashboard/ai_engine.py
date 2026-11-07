"""
------------------------------------------------------------
Project : Education Agent Intelligence Platform
Module  : AI Engine
Purpose : Intelligent Search Engine
Author  : Elias Tafadzwa Mudzudzu
------------------------------------------------------------
"""

# ==========================
# Imports
# ==========================

import re

import pandas as pd


# ==========================
# AI Engine
# ==========================

def _has(question, term):
    """True if `term` appears in `question` as a whole word or phrase.

    Whole-word matching avoids false hits such as "all" inside "call" or
    "uk" inside "ukraine".
    """
    return re.search(rf"\b{re.escape(term)}\b", question) is not None


def ask_ai(question, df=None):
    """
    Processes natural language questions and
    returns matching education consultants.

    `df` is the consultants table. If omitted it is loaded from PostgreSQL;
    passing a DataFrame lets the engine be used and tested without a database.
    """

    if df is None:
        from dashboard.db_queries import get_all_agents
        df = get_all_agents()

    question = question.lower().strip()


    # ==========================================
    # Show All Consultants
    # ==========================================

    if _has(question, "all") or _has(question, "everyone"):

        return {
            "message": f"{len(df)} consultants found.",
            "data": df
        }


    # ==========================================
    # Count Questions ("how many consultants in Kenya?")
    # ==========================================

    countries = (
        df["country"]
        .dropna()
        .unique()
    )

    if _has(question, "how many"):

        for country in countries:

            if _has(question, country.lower()):

                total = int(
                    (df["country"].str.lower() == country.lower()).sum()
                )

                return {
                    "message": f"There are {total} consultant(s) in {country}.",
                    "data": pd.DataFrame()
                }


    # ==========================================
    # Search By Country
    # ==========================================

    for country in countries:

        if _has(question, country.lower()):

            result = df[
                df["country"]
                .str.lower()
                == country.lower()
            ]

            return {
                "message": f"{len(result)} consultant(s) found in {country}.",
                "data": result
            }


    # ==========================================
    # Website Availability
    # ==========================================

    if _has(question, "without website") or _has(question, "without websites"):

        result = df[
            df["website_url"]
            .fillna("")
            .str.strip()
            == ""
        ]

        return {
            "message": f"{len(result)} consultant(s) without websites.",
            "data": result
        }


    if _has(question, "with website") or _has(question, "with websites"):

        result = df[
            df["website_url"]
            .fillna("")
            .str.strip()
            != ""
        ]

        return {
            "message": f"{len(result)} consultant(s) with websites.",
            "data": result
        }


    # ==========================================
    # WhatsApp Availability
    # ==========================================

    if _has(question, "without whatsapp"):

        result = df[
            df["whatsapp_number"]
            .fillna("")
            .str.strip()
            == ""
        ]

        return {
            "message": f"{len(result)} consultant(s) without WhatsApp.",
            "data": result
        }


    if _has(question, "with whatsapp"):

        result = df[
            df["whatsapp_number"]
            .fillna("")
            .str.strip()
            != ""
        ]

        return {
            "message": f"{len(result)} consultant(s) with WhatsApp.",
            "data": result
        }


    # ==========================================
    # Destination Country Search
    # ==========================================

    destinations = [
        "india",
        "canada",
        "australia",
        "uk",
        "usa",
        "germany",
        "france",
        "china",
        "ireland",
        "new zealand"
    ]

    for destination in destinations:

        if _has(question, destination):

            result = df[
                df["specialized_countries"]
                .fillna("")
                .str.contains(
                    destination,
                    case=False
                )
            ]

            return {
                "message": f"{len(result)} consultant(s) recruit students to {destination.title()}.",
                "data": result
            }


    # ==========================================
    # Services Search
    # ==========================================

    services = [
        "visa",
        "admission",
        "scholarship",
        "ielts",
        "coaching",
        "counselling",
        "consultation"
    ]

    for service in services:

        if _has(question, service):

            result = df[
                df["services_offered"]
                .fillna("")
                .str.contains(
                    service,
                    case=False
                )
            ]

            return {
                "message": f"{len(result)} consultant(s) offer {service.title()} services.",
                "data": result
            }


    # ==========================================
    # Fallback Search
    # ==========================================

    result = df[
        df.astype(str)
          .apply(
              lambda row:
              row.str.contains(
                  question,
                  case=False,
                  na=False,
                  regex=False
              ).any(),
              axis=1
          )
    ]

    if len(result):

        return {
            "message": f"{len(result)} matching consultant(s) found.",
            "data": result
        }


    # ==========================================
    # No Results
    # ==========================================

    return {
        "message": "Sorry, I couldn't find any matching consultants.",
        "data": pd.DataFrame()
    }
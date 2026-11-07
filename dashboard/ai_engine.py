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

import pandas as pd

from dashboard.db_queries import get_all_agents


# ==========================
# AI Engine
# ==========================

def ask_ai(question):
    """
    Processes natural language questions and
    returns matching education consultants.
    """

    df = get_all_agents()

    question = question.lower().strip()


    # ==========================================
    # Show All Consultants
    # ==========================================

    if "all" in question:

        return {
            "message": f"{len(df)} consultants found.",
            "data": df
        }


    # ==========================================
    # Search By Country
    # ==========================================

    countries = (
        df["country"]
        .dropna()
        .unique()
    )

    for country in countries:

        if country.lower() in question:

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

    if "without website" in question:

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


    if "with website" in question:

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

    if "without whatsapp" in question:

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


    if "with whatsapp" in question:

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

        if destination in question:

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

        if service in question:

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
    # Count Questions
    # ==========================================

    if "how many" in question:

        for country in countries:

            if country.lower() in question:

                total = len(
                    df[
                        df["country"]
                        .str.lower()
                        == country.lower()
                    ]
                )

                return {
                    "message": f"There are {total} consultant(s) in {country}.",
                    "data": pd.DataFrame()
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
                  na=False
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
"""
------------------------------------------------------------
Project : Education Agent Intelligence Platform
Module  : Dashboard
Purpose : Export Utilities
Author  : Elias Tafadzwa Mudzudzu
------------------------------------------------------------
"""

# ==========================
# Imports
# ==========================

from io import BytesIO

import pandas as pd


# ==========================
# Excel Export
# ==========================

def to_excel(df):

    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:

        df.to_excel(
            writer,
            index=False,
            sheet_name="Education Agents"
        )

    return output.getvalue()


# ==========================
# CSV Export
# ==========================

def to_csv(df):

    return df.to_csv(index=False).encode("utf-8")
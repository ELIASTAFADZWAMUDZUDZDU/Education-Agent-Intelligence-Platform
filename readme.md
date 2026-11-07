# Education Agent Intelligence Platform

A data engineering project that merges and cleans lists of education consultants from many countries, loads them into PostgreSQL, and serves them through a Streamlit dashboard with analytics, Excel export, and a rule-based natural-language search.

It was built during an internship to organise publicly listed education consultant and agency information for study-abroad recruitment.

**Built with:** Python, pandas, PostgreSQL (psycopg2), Streamlit, Plotly, openpyxl.

## About the data

The real dataset is not in this repository. It was compiled for an organisation from publicly listed business information, so only the code is published. To let you run everything, `data/sample/sample_agents.xlsx` contains **18 invented consultants** (fake names, `example.com` websites, placeholder phone numbers).

## How it works

```
data/raw/*.xlsx|csv ──▶ pipeline/merge_data.py ──▶ data/processed/merged_agents.xlsx
                                                          │
                                         pipeline/clean_data.py  (standardise columns, de-duplicate, tidy text)
                                                          ▼
                                         data/processed/cleaned_agents.xlsx
                                                          │
                                         database/load_data.py
                                                          ▼
                                         PostgreSQL table education_agents
                                                          │
                                         dashboard/ (Streamlit)  ──▶ Overview · Analytics · Export · AI Search
```

## Quick start with the sample data

Requires Python 3.10+ and PostgreSQL.

```bash
python -m pip install -r requirements.txt
```

1. Create a database and the table: `psql -d <your_database> -f database/schema.sql`
2. Copy `.env.example` to `.env` and fill in your database details. Never commit `.env`.
3. Load the sample data:

```bash
python -m database.load_data data/sample/sample_agents.xlsx
```

4. Start the dashboard:

```bash
streamlit run dashboard/app.py
```

> `load_data` empties the `education_agents` table before inserting. It is meant for development, so do not point it at a database you want to keep.

### Using your own data

Put raw Excel or CSV files in `data/raw/` (git-ignored), then run:

```bash
python pipeline/merge_data.py
python pipeline/clean_data.py
python -m database.load_data
```

## Dashboard pages

- **Overview:** summary and a searchable table.
- **Analytics:** consultants by country, services breakdown, website and WhatsApp availability, and a data quality report.
- **Export:** download filtered results as Excel.
- **AI Search:** ask questions in plain English.

## The search engine

The "AI Search" page uses a **rule-based** engine in `dashboard/ai_engine.py`. It looks for whole-word keywords such as countries, destinations and services, then filters the table. It is not a language model.

Example questions:

```
Show all consultants
Show consultants in Kenya
How many consultants are in Zimbabwe?
Show consultants without website
Show consultants without WhatsApp
Show consultants recruiting students to Australia
Show visa consultants
```

Anything else falls back to a plain-text search across every column.

## Tests

The tests use the sample data and need no database:

```bash
python -m unittest discover -s tests -v
```

They cover country, count, website, WhatsApp, destination and service questions, whole-word matching (so "call" does not mean "all"), special characters in questions, and the no-result message.

## Project structure

```
dashboard/   Streamlit app, search engine, database queries, export helpers, pages
pipeline/    merge_data.py, clean_data.py
database/    connection.py, load_data.py, schema.sql
data/sample/ invented demo data
tests/       offline tests for the search engine
```

## Limitations

- Keyword rules only: unusual phrasing may not be understood, and the first matching rule wins.
- The search loads the whole table into memory, which is fine for a few hundred rows but not for very large data.
- The cleaning step was written for the spreadsheets this project started with, so new files may need column mapping changes.
- No authentication on the dashboard.

## Possible next steps

Semantic search, a REST API, scheduled data refresh, and cloud deployment.

## Author

Elias Tafadzwa Mudzudzu, Computer Science Engineering student at Kalinga University, interested in data engineering and AI.

## Licence

This project is released under the [MIT Licence](LICENSE).

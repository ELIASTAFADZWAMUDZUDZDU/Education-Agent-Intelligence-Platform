# 🎓 Education Agent Intelligence Platform

An end-to-end **Data Engineering** and **AI-powered Analytics** platform for collecting, cleaning, storing, analyzing, and intelligently searching education consultant data from multiple countries.

The project demonstrates the complete data lifecycle—from raw Excel files to an interactive dashboard with an AI-powered search assistant.

---

## 📌 Project Overview

The **Education Agent Intelligence Platform (EAIP)** was developed to centralize information about education consultants and study abroad agencies operating across different countries.

The platform:

- Collects consultant data from multiple Excel datasets.
- Cleans and standardizes inconsistent information.
- Stores the cleaned data in PostgreSQL.
- Provides interactive analytics through Streamlit.
- Enables natural language search using a rule-based AI engine.

---

## 🚀 Features

- ✅ ETL Pipeline (Extract, Transform, Load)
- ✅ Automatic data merging
- ✅ Data cleaning and standardization
- ✅ PostgreSQL integration
- ✅ Interactive Streamlit dashboard
- ✅ Analytics and KPI reporting
- ✅ Excel export
- ✅ AI-powered natural language search
- ✅ Modular architecture

---

# 🏗️ Project Architecture

```
education-agent-intelligence-platform/

│
├── dashboard/
│   ├── app.py
│   ├── ai_engine.py
│   ├── db_queries.py
│   ├── export_utils.py
│   └── pages/
│       ├── overview.py
│       ├── analytics.py
│       ├── export.py
│       └── ai_search.py
│
├── pipeline/
│   ├── merge_data.py
│   ├── clean_data.py
│   ├── enrich_data.py
│   └── export_excel.py
│
├── database/
│   ├── connection.py
│   ├── load_data.py
│   └── schema.sql
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── exports/
│
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Cleaning & Transformation |
| PostgreSQL | Relational Database |
| psycopg2 | PostgreSQL Connector |
| Streamlit | Interactive Dashboard |
| Plotly | Data Visualization |
| OpenPyXL | Excel Processing |
| python-dotenv | Environment Variables |

---

# 📊 ETL Pipeline

The project follows an **Extract → Transform → Load (ETL)** workflow.

## 1️⃣ Extract

Education consultant data is collected from multiple Excel files.

```
Kenya.xlsx
Nigeria.xlsx
Zimbabwe.xlsx
South Africa.xlsx
...
```

---

## 2️⃣ Transform

The transformation process performs:

- Standardized column names
- Merge duplicate columns
- Remove duplicate records
- Standardize missing values
- Clean text fields
- Prepare data for PostgreSQL

---

## 3️⃣ Load

The cleaned dataset is inserted into PostgreSQL.

```
Raw Excel Files
        │
        ▼
Merged Dataset
        │
        ▼
Clean Dataset
        │
        ▼
PostgreSQL
```

---

# 🗄 Database

The PostgreSQL database stores:

- Consultant Name
- Website URL
- Specialized Countries
- Services Offered
- Office Address
- Contact Number
- WhatsApp Number
- Country
- Social Media Links
- Years in Operation
- Source Information

---

# 📈 Dashboard

The dashboard consists of four pages.

## 🏠 Overview

- Platform summary
- Searchable consultant table
- Quick statistics

---

## 📊 Analytics

- KPI Cards
- Consultants by Country
- Services Breakdown
- Website Availability
- WhatsApp Availability
- Data Quality Report

---

## 📤 Export

Allows users to export filtered consultant data to Excel.

---

## 🤖 AI Search

The AI assistant supports natural language queries such as:

```
Show consultants in Kenya

Show consultants with websites

Show consultants without WhatsApp

Show consultants recruiting students to Australia

Show visa consultants

How many consultants are in Zimbabwe?
```

---

# 🧠 AI Engine

The platform includes a **rule-based Natural Language Processing (NLP)** engine.

### AI Workflow

```
User Question
      │
      ▼
Text Preprocessing
      │
      ▼
Intent Detection
      │
      ▼
Entity Extraction
      │
      ▼
Rule-Based Reasoning
      │
      ▼
Database Query
      │
      ▼
Results
```

### AI Capabilities

- Intent Detection
- Entity Extraction
- Natural Language Search
- Intelligent Filtering
- Database Query Generation
- Human-readable Responses

---

# 🏛 Software Architecture

```
                Streamlit Dashboard
                        │
                        ▼
                 AI Search Interface
                        │
                        ▼
                  AI Engine (NLP)
                        │
                        ▼
                 Database Query Layer
                        │
                        ▼
                  PostgreSQL Database
                        ▲
                        │
                  ETL Data Pipeline
                        ▲
                        │
                  Raw Excel Files
```

---

# ▶️ Getting Started

## Clone the Repository

```bash
git clone https://github.com/yourusername/education-agent-intelligence-platform.git

cd education-agent-intelligence-platform
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```env
DB_HOST=localhost
DB_NAME=education_agents
DB_USER=postgres
DB_PASSWORD=your_password
DB_PORT=5432
```

---

## Create the Database

Run:

```sql
database/schema.sql
```

---

## Run the ETL Pipeline

Merge the datasets:

```bash
python pipeline/merge_data.py
```

Clean the dataset:

```bash
python pipeline/clean_data.py
```

Load into PostgreSQL:

```bash
python -m database.load_data
```

---

## Launch the Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 📌 Future Improvements

- OpenAI / Gemini integration
- Semantic search
- Recommendation engine
- Automated web scraping
- Apache Airflow scheduling
- REST API using FastAPI
- User authentication
- Interactive maps
- Cloud deployment

---

# 🎯 Skills Demonstrated

- Python Programming
- Data Engineering
- ETL Pipeline Development
- PostgreSQL
- Data Cleaning
- Streamlit
- Plotly
- Natural Language Processing (Rule-Based)
- Software Architecture
- Database Design

---

# 👨‍💻 Author

**Elias Tafadzwa Mudzudzu**

Computer Engineering Student

Aspiring AI & Data Engineer

---

# ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.
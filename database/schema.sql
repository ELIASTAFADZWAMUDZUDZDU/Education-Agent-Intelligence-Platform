-- Run once against an empty PostgreSQL database:
--   psql -d <your_database> -f database/schema.sql

CREATE TABLE IF NOT EXISTS education_agents (
    id                    SERIAL PRIMARY KEY,

    consultant_name       TEXT,
    website_url           TEXT,
    specialized_countries TEXT,
    services_offered      TEXT,
    office_address        TEXT,
    contact_number        TEXT,
    country               TEXT,
    social_media_links    TEXT,
    source_of_information TEXT,
    years_in_operation    TEXT,
    whatsapp_number       TEXT,
    source_file           TEXT,

    created_at            TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

# ClaimTrace

A full-stack insurance claims explorer built end to end: raw data cleaning, a PostgreSQL star schema, a Django REST API, and a live dashboard that consumes it.

## What it does

ClaimTrace takes a raw auto insurance claims dataset, cleans it, models it into a proper relational database, and serves it through an API to a filterable dashboard. It's built to show the full pipeline a data or BI role actually touches, not just a single piece of it.

The dashboard lets you filter 1,000 claims by policy state, incident severity, and fraud status, with live summary stats (total claims, fraud rate, average claim amount, and detected data anomalies).

## Tech stack

- **Data cleaning:** Python, pandas, Jupyter
- **Database:** PostgreSQL, modelled as a star schema (fact and dimension tables)
- **API:** Django REST Framework
- **Frontend:** HTML, CSS, vanilla JavaScript (fetch API)

## Data cleaning highlights

Rather than just running the raw CSV through a pipeline, the cleaning process involved specific decisions worth calling out:

- Replaced disguised missing values (`?`) with an explicit `Unknown` category, keeping them visible in analysis instead of silently dropping them.
- Detected and flagged (not deleted) a data entry anomaly where an incident date preceded the policy start date, an impossible real-world scenario.
- Converted string dates to proper date types and engineered a new field (`days_policy_to_incident`), a common signal in fraud analysis.

## Database design

The data is modelled as a star schema:

- `fact_claims`: claim-level measures (claim amounts, premium, fraud flag, anomaly flag)
- `dim_insured`: the policyholder (age, occupation, education, relationship status)
- `dim_incident`: the incident itself (type, severity, location, date)

## Running it locally

1. Clone the repo and create a virtual environment.
2. Install dependencies: `pip install django djangorestframework psycopg2-binary python-decouple`
3. Create a PostgreSQL database named `claimtrace` and load the schema.
4. Create a `.env` file with `SECRET_KEY` and `DB_PASSWORD`.
5. Run `python manage.py runserver`.
6. Open `frontend/index.html` in a browser.

## Why I built this

I wanted a project that demonstrated the whole path from messy raw data to something a non-technical person could actually use, not just a notebook full of charts. Every step, from the schema design to the anomaly detection to the API structure, was a decision I made and can explain, not a template I followed.

---

Built by [Pedro Vasconez](https://github.com/PedroJV)

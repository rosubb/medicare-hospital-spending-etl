# Medicare Hospital Spending ETL Pipeline

## 📌 Project Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline using Medicare hospital spending data.

The goal is to simulate a production-style healthcare data engineering workflow including:
- Structured data ingestion
- Data cleaning and transformation
- Logging and error handling
- Loading into PostgreSQL
- Data validation checks

---

## 📂 Dataset

Source: Medicare Hospital Spending by Claim Type (Public Dataset)

The dataset includes:
- Hospital name
- Claim type
- Spending amount
- Time period (start & end date)
- State and region information

Raw dataset is stored in:
`data/raw/`

A small sample is stored in:
`data/sample/`

---

## 🏗 Architecture

Raw CSV  
⬇  
Extract Layer (Python)  
⬇  
Transform Layer (Data Cleaning + Type Casting)  
⬇  
Load Layer (PostgreSQL)  
⬇  
Validation Queries  

---

## 🛠 Tech Stack

- Python
- Pandas
- PostgreSQL
- SQL
- Logging
- Git & GitHub

---

## 📁 Project Structure
## 📊 Example Output

After running the pipeline, the processed dataset contains:

- Standardized column names
- Removed duplicates
- Null value handling
- Derived metrics (e.g., cost_per_discharge)

Example columns:

hospital_name  
claim_type  
total_payments  
discharges  
cost_per_discharge

## 🧪 Data Validation

Basic validation checks include:

- No duplicate rows
- No completely empty rows
- Missing values handled
- Numeric columns properly cast

  ## 🔮 Future Improvements

- Add automated unit tests
- Dockerize the pipeline
- Schedule ETL with Airflow
- Add CI/CD with GitHub Actions
- Deploy to cloud (AWS / GCP)

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


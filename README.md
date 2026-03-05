# Grocery Sales ETL Pipeline (Databricks + PySpark)

## Project Overview

This project implements an **end-to-end ETL data pipeline** for grocery store sales data using **Databricks, PySpark, and Delta Lake**.  
The pipeline processes raw retail datasets and transforms them into analytics-ready datasets using the **Medallion Architecture (Bronze → Silver → Gold)**.

The final output enables **sales forecasting and retail analytics** by generating aggregated sales features such as weekly sales trends, promotion impact, and holiday demand patterns.

---

## Dataset

Dataset Source:  
Kaggle – *Store Sales Time Series Forecasting*

The dataset contains historical grocery sales data from **Corporación Favorita**, a large grocery retailer in Ecuador.

Datasets used:

- `train.csv` → Historical sales data
- `stores.csv` → Store metadata
- `transactions.csv` → Daily store transactions
- `holidays_events.csv` → Holiday information
- `oil.csv` → Oil price data

These datasets simulate a **real-world retail analytics environment**.

---

## Project Architecture

The pipeline follows the **Medallion Architecture**:

Raw Data (Kaggle Dataset)
↓
AWS S3 Data Lake
↓
Databricks PySpark ETL Pipeline
↓
Bronze Layer (Raw Tables)
↓
Silver Layer (Cleaned & Integrated Data)
↓
Gold Layer (Analytics & Forecasting Features)


---

## Medallion Architecture Layers

### Bronze Layer (Raw Data)

Purpose:
- Store raw data exactly as received
- Preserve data lineage

Tables:

- `raw.sales_transactions`
- `raw.stores`
- `raw.transactions`
- `raw.holidays`
- `raw.oil_prices`

Operations:
- Raw CSV ingestion
- Schema validation
- Metadata tracking

---

### Silver Layer (Cleaned Data)

Purpose:
- Clean and standardize datasets
- Integrate multiple data sources

Transformations:

- Remove duplicate records
- Convert data types
- Handle missing values
- Join sales data with store metadata
- Join transaction data with sales records
- Extract date-based features

Output Table:

- `processed.sales_cleaned`

---

### Gold Layer (Analytics Data)

Purpose:
- Generate business-ready datasets for analytics and forecasting.

Features generated:

- Weekly sales aggregation
- Promotion impact metrics
- Holiday sales indicators
- Store performance metrics
- Product category trends

Output Table:

- `analytics.sales_forecast_features`

---

## Project Folder Structure

grocery-sales-etl
│
├── ingestion
│ └── bronze_ingestion.py
│
├── transformations
│ └── silver_transformation.py
│
├── analytics
│ └── gold_features.py
│
├── utils
│ └── data_validation.py
│
├── configs
│
├── workflows
│
├── main_pipeline.py
│
├── requirements.txt
│
└── README.md



---

## Pipeline Execution Flow

bronze_ingestion.py
↓
silver_transformation.py
↓
gold_features.py
↓
main_pipeline.py



The `main_pipeline.py` script orchestrates the entire ETL pipeline.

---

## Technologies Used

- **Python**
- **PySpark**
- **Databricks**
- **Delta Lake**
- **AWS S3**
- **Git & GitHub**

---

## Installation

Clone the repository:

```bash
git clone https://github.com/SuhasSC/grocery-sales-etl-P2_Databricks.git
cd grocery-sales-etl

Install dependencies:
pip install -r requirements.txt

Running the Pipeline

Run the pipeline locally:
python main_pipeline.py


Pipeline stages executed:

1. Raw data ingestion (Bronze)

2. Data cleaning and integration (Silver)

3. Feature engineering and aggregation (Gold)

Business Insights Generated

The pipeline enables several retail analytics insights:

Sales Trends

Identify weekly and seasonal demand patterns.

Store Performance

Determine top-performing stores based on revenue.

Product Category Analysis

Identify high-demand product families.

Promotion Effectiveness

Measure sales increase during promotional campaigns.

Holiday Impact

Analyze how holidays affect product demand.

Customer Traffic Analysis

Evaluate relationship between store transactions and sales.


Future Enhancements

Integrate real-time data ingestion

Build machine learning forecasting models

Create interactive dashboards (Power BI / Tableau)

Implement data quality monitoring

License

This project is developed for educational and research purposes


---

✅ This README includes:

- Project context  
- Architecture  
- ETL pipeline explanation  
- Business insights  
- Setup instructions  
- Professional formatting

It will make your **GitHub project look like a real Data Engineering portfolio project**.

---

If you want, I can also give you **one more very important thing for your project**:

A **perfect architecture diagram image you can directly paste into the README and PPT** (looks much more professional than text diagrams).
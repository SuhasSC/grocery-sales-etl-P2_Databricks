from ingestion.bronze_ingestion import run_bronze_ingestion
from transformations.silver_transformation import run_silver_transformation
from analytics.gold_features import run_gold_features

def run_pipeline():

    print("Starting ETL pipeline")

    run_bronze_ingestion()
    run_silver_transformation()
    run_gold_features()

    print("Pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()
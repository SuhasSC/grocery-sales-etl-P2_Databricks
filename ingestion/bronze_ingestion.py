from pyspark.sql import SparkSession

def run_bronze_ingestion():

    spark = SparkSession.builder \
        .appName("Bronze Ingestion") \
        .getOrCreate()

    sales_path = "data/train.csv"
    stores_path = "data/stores.csv"
    transactions_path = "data/transactions.csv"
    holidays_path = "data/holidays_events.csv"
    oil_path = "data/oil.csv"

    sales_df = spark.read.option("header", True).csv(sales_path)
    stores_df = spark.read.option("header", True).csv(stores_path)
    transactions_df = spark.read.option("header", True).csv(transactions_path)
    holidays_df = spark.read.option("header", True).csv(holidays_path)
    oil_df = spark.read.option("header", True).csv(oil_path)

    sales_df.write.mode("overwrite").parquet("bronze/sales")
    stores_df.write.mode("overwrite").parquet("bronze/stores")
    transactions_df.write.mode("overwrite").parquet("bronze/transactions")
    holidays_df.write.mode("overwrite").parquet("bronze/holidays")
    oil_df.write.mode("overwrite").parquet("bronze/oil")

    print("Bronze ingestion completed")

if __name__ == "__main__":
    run_bronze_ingestion()
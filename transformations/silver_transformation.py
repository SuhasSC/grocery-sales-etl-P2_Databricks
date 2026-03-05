from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date

def run_silver_transformation():

    spark = SparkSession.builder \
        .appName("Silver Transformation") \
        .getOrCreate()

    sales = spark.read.parquet("bronze/sales")
    stores = spark.read.parquet("bronze/stores")
    transactions = spark.read.parquet("bronze/transactions")

    sales_clean = sales \
        .withColumn("date", to_date(col("date"))) \
        .withColumn("sales", col("sales").cast("double")) \
        .dropDuplicates()

    sales_store = sales_clean.join(stores, "store_nbr", "left")

    sales_final = sales_store.join(
        transactions,
        ["date", "store_nbr"],
        "left"
    )

    sales_final.write.mode("overwrite").parquet("silver/sales_clean")

    print("Silver transformation completed")

if __name__ == "__main__":
    run_silver_transformation()
from pyspark.sql import SparkSession
from pyspark.sql.functions import weekofyear, month, dayofweek, sum

def run_gold_features():

    spark = SparkSession.builder \
        .appName("Gold Features") \
        .getOrCreate()

    sales = spark.read.parquet("silver/sales_clean")

    sales_features = sales \
        .withColumn("week_number", weekofyear("date")) \
        .withColumn("month", month("date")) \
        .withColumn("day_of_week", dayofweek("date"))

    weekly_sales = sales_features.groupBy(
        "store_nbr",
        "family",
        "week_number"
    ).agg(
        sum("sales").alias("weekly_sales")
    )

    weekly_sales.write.mode("overwrite").parquet("gold/weekly_sales")

    print("Gold feature engineering completed")

if __name__ == "__main__":
    run_gold_features()
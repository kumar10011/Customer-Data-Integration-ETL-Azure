from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_timestamp

spark = SparkSession.builder.appName("CustomerGold").getOrCreate()

try:
    dbutils.widgets.text("input_path", "")
    dbutils.widgets.text("output_path", "")
    input_path = dbutils.widgets.get("input_path")
    output_path = dbutils.widgets.get("output_path")
except NameError:
    input_path = "output/customers_cleaned"
    output_path = "output/customers_gold"

df = spark.read.option("header", True).option("inferSchema", True).csv(input_path)

# Keep reporting-ready columns.
gold_df = (
    df.select(
        "customer_id",
        "customer_name",
        "email",
        "phone",
        "city",
        "country",
        "processed_timestamp"
    )
    .withColumn("gold_processed_timestamp", current_timestamp())
)

gold_df.write.mode("overwrite").option("header", True).csv(output_path)

spark.stop()

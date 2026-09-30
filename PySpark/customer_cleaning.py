from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, trim, lower, initcap, regexp_replace, coalesce, lit,
    current_timestamp, row_number
)
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("CustomerCleaning").getOrCreate()

# In Databricks, these values can be passed from ADF using widgets.
try:
    dbutils.widgets.text("input_path", "")
    dbutils.widgets.text("output_path", "")
    input_path = dbutils.widgets.get("input_path")
    output_path = dbutils.widgets.get("output_path")
except NameError:
    input_path = "SampleData/customers.csv"
    output_path = "output/customers_cleaned"

df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(input_path)
)

# Standardize column names
df = df.toDF(*[c.strip().lower().replace(" ", "_") for c in df.columns])

# Basic cleansing
df = (
    df
    .withColumn("customer_name", initcap(trim(col("customer_name"))))
    .withColumn("email", lower(trim(col("email"))))
    .withColumn("phone", regexp_replace(trim(col("phone")), r"[^0-9+]", ""))
    .withColumn("city", initcap(trim(col("city"))))
    .withColumn("country", initcap(trim(col("country"))))
)

# Handle missing values
df = (
    df
    .withColumn("email", coalesce(col("email"), lit("unknown@example.com")))
    .withColumn("phone", coalesce(col("phone"), lit("Not Available")))
    .withColumn("city", coalesce(col("city"), lit("Unknown")))
    .withColumn("country", coalesce(col("country"), lit("Unknown")))
)

# Remove invalid CustomerID records
df = df.filter(col("customer_id").isNotNull())

# Deduplicate by CustomerID.
# If multiple records exist, keep one deterministic record.
window_spec = Window.partitionBy("customer_id").orderBy(col("customer_name").asc())

df = (
    df
    .withColumn("_rn", row_number().over(window_spec))
    .filter(col("_rn") == 1)
    .drop("_rn")
    .withColumn("processed_timestamp", current_timestamp())
)

# Write curated output
(
    df.write
    .mode("overwrite")
    .option("header", True)
    .csv(output_path)
)

spark.stop()

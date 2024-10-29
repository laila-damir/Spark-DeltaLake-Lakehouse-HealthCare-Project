from pyspark.sql import SparkSession

# Create Spark session with Delta support
spark = SparkSession.builder \
    .appName("Healthcare Data ETL") \
    .config("spark.jars.packages", "io.delta:delta-core_2.12:1.0.0") \
    .config("spark.sql.extensions", "org.apache.spark.sql.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# Load the CSV data
data_path = "/home/jovyan/BigData/healthcare_dataset.csv"
df = spark.read.option("header", "true").csv(data_path)
df.show()
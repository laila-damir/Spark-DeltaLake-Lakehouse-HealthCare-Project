from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, date_format
from pyspark.sql.types import DoubleType

# Initialize Spark session (if not already done)
spark = SparkSession.builder.appName("HealthCareAnalysis").getOrCreate()

# Your initial DataFrame transformation
transformed_df = (
    df.dropna(subset=["Name", "Date of Admission", "Billing Amount"])  # Drop rows with nulls in these columns
    .withColumnRenamed("Billing Amount", "billing_amount")  # Rename for consistency
    .withColumnRenamed("Blood Type", "blood_type")  # Rename to remove space
    .withColumnRenamed("Medical Condition", "medical_condition")  # Rename to remove space
    .withColumnRenamed("Date of Admission", "date_of_admission")  # Rename to remove space
    .withColumnRenamed("Doctor", "doctor")  # Rename to remove space
    .withColumnRenamed("Hospital", "hospital")  # Rename to remove space
    .withColumnRenamed("Insurance Provider", "insurance_provider")  # Rename to remove space
    .withColumnRenamed("Room Number", "room_number")  # Rename to remove space
    .withColumnRenamed("Admission Type", "admission_type")  # Rename to remove space
    .withColumnRenamed("Discharge Date", "discharge_date")  # Rename to remove space
    .withColumnRenamed("Medication", "medication")  # Rename to remove space
    .withColumnRenamed("Test Results", "test_results")  # Rename to remove space
    .withColumn("date_of_admission", to_date(col("date_of_admission"), "yyyy-MM-dd"))  # Correct date format
    .withColumn("billing_amount", col("billing_amount").cast(DoubleType()))  # Cast to DoubleType
    .withColumn("discharge_date", to_date(col("discharge_date"), "yyyy-MM-dd"))  # Cast to DateType
    .select(
        col("Name"),
        col("Age"),  # Include Age column
        col("Gender"),  # Include Gender column
        col("date_of_admission"),
        col("billing_amount"),
        col("blood_type"),
        col("medical_condition"),
        col("doctor"),
        col("hospital"),
        col("insurance_provider"),
        col("room_number"),
        col("admission_type"),
        col("discharge_date"),
        col("medication"),
        col("test_results")
    )
)

# Register the DataFrame as a temporary view

delta_table_path = "/home/jovyan/BigData/delta_healthcare_data"
transformed_df.createOrReplaceTempView("healthcare_data")
transformed_df.write.csv(delta_table_path, header=True, mode="overwrite")

spark.sql(f"CREATE TABLE IF NOT EXISTS healthcare_data USING DELTA LOCATION '{delta_table_path}'")
spark.sql("SELECT * FROM healthcare_data").show()

# Check the schema of the DataFrame
transformed_df.printSchema()

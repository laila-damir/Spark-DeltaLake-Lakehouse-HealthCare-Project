query_admissions_per_month = """
SELECT
    DATE_FORMAT(`date_of_admission`, 'MMMM yyyy') AS Admission_Month,
    COUNT(1) AS Total_Admissions
FROM
    healthcare_data
WHERE
    `date_of_admission` IS NOT NULL
GROUP BY
    Admission_Month
ORDER BY
    Admission_Month
"""


# Execute the query
df_admissions_per_month = spark.sql(query_admissions_per_month).toPandas()

# Display the result
print(df_admissions_per_month.columns)

# Assuming `transformed_df` is your transformed DataFrame and it is already a Spark DataFrame

# Create a temporary view of the transformed DataFrame
transformed_df.createOrReplaceTempView("healthcare_data")

# Query 1: Count of patients by doctor
query_patients_by_doctor = """
SELECT
    doctor AS Doctor,
    COUNT(*) AS Total_Patients
FROM
    healthcare_data
GROUP BY
    doctor
ORDER BY
    Total_Patients DESC
"""

# Query 2: Total billing amount by doctor
query_billing_by_doctor = """
SELECT
    doctor AS Doctor,
    SUM(billing_amount) AS Total_Billing
FROM
    healthcare_data
GROUP BY
    doctor
ORDER BY
    Total_Billing DESC
"""

# Execute the queries and convert to Pandas DataFrames
df_patients_by_doctor = spark.sql(query_patients_by_doctor).toPandas()
df_billing_by_doctor = spark.sql(query_billing_by_doctor).toPandas()

# Print column names to verify
print(df_patients_by_doctor.columns)
print(df_billing_by_doctor.columns)


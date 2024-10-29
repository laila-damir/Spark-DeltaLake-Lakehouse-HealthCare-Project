-- Query 1: Total Count of Admissions by Day, Month, and Quarter
SELECT
    date_format(date_of_admission, 'yyyy-MM-dd') AS day,
    date_format(date_of_admission, 'yyyy-MM') AS month,
    quarter(date_of_admission) AS quarter,
    COUNT(*) AS total_admissions
FROM
    healthcare_data
GROUP BY
    day, month, quarter
ORDER BY
    day, month, quarter;

-- Query 2: Average Billing Amount per Hospital by Day, Month, and Quarter
SELECT
    date_format(date_of_admission, 'yyyy-MM-dd') AS day,
    date_format(date_of_admission, 'yyyy-MM') AS month,
    quarter(date_of_admission) AS quarter,
    hospital,
    AVG(billing_amount) AS avg_billing_amount
FROM
    healthcare_data
GROUP BY
    day, month, quarter, hospital
ORDER BY
    day, month, quarter, hospital;

-- Query 3: Average Billing Amount per Day per Hospital and Doctor
SELECT
    date_format(date_of_admission, 'yyyy-MM-dd') AS day,
    hospital,
    doctor,
    AVG(billing_amount) AS avg_billing_amount
FROM
    healthcare_data
GROUP BY
    day, hospital, doctor
ORDER BY
    day, hospital, doctor;

-- Query 4: Total Admissions per Doctor by Month
SELECT
    date_format(date_of_admission, 'yyyy-MM') AS month,
    doctor,
    COUNT(*) AS total_admissions
FROM
    healthcare_data
GROUP BY
    month, doctor
ORDER BY
    month, doctor;

-- Query 5: Total Admissions per Gender by Day and Average Billing Amount
SELECT
    date_format(date_of_admission, 'yyyy-MM-dd') AS day,
    gender,
    COUNT(*) AS total_admissions,
    AVG(billing_amount) AS avg_billing_amount
FROM
    healthcare_data
GROUP BY
    day, gender
ORDER BY
    day, gender;

-- Query 6: List of Hospitals with Day and Average Billing Amount per Day
SELECT
    date_format(date_of_admission, 'yyyy-MM-dd') AS day,
    hospital,
    AVG(billing_amount) AS avg_billing_amount
FROM
    healthcare_data
GROUP BY
    day, hospital
ORDER BY
    day, hospital;

-- Query 7: Monthly Total and Average Billing Amount by Insurance Provider
SELECT
    date_format(date_of_admission, 'yyyy-MM') AS month,
    insurance_provider,
    SUM(billing_amount) AS total_billing_amount,
    AVG(billing_amount) AS avg_billing_amount
FROM
    healthcare_data
GROUP BY
    month, insurance_provider
ORDER BY
    month, insurance_provider;

-- Query 8: Average Billing Amount by Age Group and Hospital
SELECT
    age DIV 10 * 10 AS age_group,
    hospital,
    AVG(billing_amount) AS avg_billing_amount
FROM
    healthcare_data
GROUP BY
    age_group, hospital
ORDER BY
    age_group, hospital;

-- Query 9: Quarterly Total Billing Amount by Blood Type
SELECT
    quarter(date_of_admission) AS quarter,
    blood_type,
    SUM(billing_amount) AS total_billing_amount
FROM
    healthcare_data
GROUP BY
    quarter, blood_type
ORDER BY
    quarter, blood_type;

-- Query 10: Top 5 Doctors by Total Billing Amount
SELECT
    doctor,
    SUM(billing_amount) AS total_billing_amount
FROM
    healthcare_data
GROUP BY
    doctor
ORDER BY
    total_billing_amount DESC
LIMIT 5;

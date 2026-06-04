CREATE DATABASE IF NOT EXISTS hospital_db;

USE hospital_db;

CREATE TABLE IF NOT EXISTS covid_cleaned (
    available_extra_rooms_in_hospital INT,
    department STRING,
    ward_facility_code STRING,
    doctor_name STRING,
    staff_available INT,
    patient_id STRING,
    age INT,
    gender STRING,
    type_of_admission STRING,
    severity_of_illness STRING,
    health_conditions STRING,
    visitors_with_patient INT,
    insurance STRING,
    admission_deposit DOUBLE,
    stay_in_days DOUBLE
)
STORED AS PARQUET;

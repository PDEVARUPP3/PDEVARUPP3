-- Query to calculate average length of stay by procedure type

-- Create a temporary table to store discharge dates and admission dates
CREATE TEMPORARY TABLE TempStayDates AS
SELECT
    patient_id,
    procedure_type,
    DATEDIFF(discharge_date, admission_date) AS length_of_stay
FROM
    admissions
WHERE
    discharge_date IS NOT NULL; -- Ensure patient has been discharged

-- Query to calculate average length of stay for each procedure type
SELECT
    procedure_type,
    AVG(length_of_stay) AS avg_length_of_stay
FROM
    TempStayDates
GROUP BY
    procedure_type;
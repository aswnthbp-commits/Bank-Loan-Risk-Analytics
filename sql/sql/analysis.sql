-- ===========================================
-- BANK LOAN RISK ANALYTICS
-- ===========================================

SELECT COUNT(*) AS Total_Applications
FROM bank_loan_data;

SELECT Loan_Status,
COUNT(*) AS Total
FROM bank_loan_data
GROUP BY Loan_Status;

SELECT Gender,
COUNT(*) AS Total
FROM bank_loan_data
GROUP BY Gender;

SELECT Education,
COUNT(*) AS Total
FROM bank_loan_data
GROUP BY Education;

SELECT Property_Area,
COUNT(*) AS Total
FROM bank_loan_data
GROUP BY Property_Area;

SELECT Credit_History,
COUNT(*) AS Total
FROM bank_loan_data
GROUP BY Credit_History;

SELECT
AVG(ApplicantIncome) AS Average_Applicant_Income
FROM bank_loan_data;

SELECT
AVG(LoanAmount) AS Average_Loan_Amount
FROM bank_loan_data;

SELECT
Property_Area,
AVG(LoanAmount) AS Avg_Loan
FROM bank_loan_data
GROUP BY Property_Area
ORDER BY Avg_Loan DESC;

SELECT
Education,
Loan_Status,
COUNT(*) AS Total
FROM bank_loan_data
GROUP BY Education, Loan_Status;

SELECT
Gender,
Loan_Status,
COUNT(*) AS Total
FROM bank_loan_data
GROUP BY Gender, Loan_Status;

SELECT
Married,
Loan_Status,
COUNT(*) AS Total
FROM bank_loan_data
GROUP BY Married, Loan_Status;

SELECT
Property_Area,
Loan_Status,
COUNT(*) AS Total
FROM bank_loan_data
GROUP BY Property_Area, Loan_Status;

SELECT
Credit_History,
Loan_Status,
COUNT(*) AS Total
FROM bank_loan_data
GROUP BY Credit_History, Loan_Status;

SELECT
MAX(ApplicantIncome) AS Highest_Income,
MIN(ApplicantIncome) AS Lowest_Income
FROM bank_loan_data;

SELECT
MAX(LoanAmount) AS Highest_Loan,
MIN(LoanAmount) AS Lowest_Loan
FROM bank_loan_data;
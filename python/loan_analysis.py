import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ==========================================
# BANK LOAN RISK ANALYTICS
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "bank_loan_data.csv"

OUTPUT_DIR = BASE_DIR / "screenshots"

OUTPUT_DIR.mkdir(exist_ok=True)

# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv(DATA_PATH)

print("=" * 60)
print("BANK LOAN RISK ANALYTICS")
print("=" * 60)

print("\nDataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nFirst Five Rows")
print(df.head())

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

# ==========================================
# DATA CLEANING
# ==========================================

object_columns = [
    "Gender",
    "Married",
    "Dependents",
    "Education",
    "Self_Employed",
    "Property_Area",
    "Loan_Status"
]

numeric_columns = [
    "ApplicantIncome",
    "CoapplicantIncome",
    "LoanAmount",
    "Loan_Amount_Term",
    "Credit_History"
]

for col in object_columns:

    mode = df[col].mode()

    if len(mode) > 0:
        df[col] = df[col].fillna(mode[0])

for col in numeric_columns:

    df[col] = pd.to_numeric(df[col], errors="coerce")

    df[col] = df[col].fillna(df[col].median())

# ==========================================
# CHART FUNCTION
# ==========================================

def save_bar(column, title, filename):

    plt.figure(figsize=(8,5))

    df[column].value_counts().plot(kind="bar")

    plt.title(title)

    plt.xlabel(column)

    plt.ylabel("Count")

    plt.tight_layout()

    plt.savefig(OUTPUT_DIR / filename)

    plt.close()
    # ==========================================
# LOAN STATUS DISTRIBUTION
# ==========================================

save_bar(
    "Loan_Status",
    "Loan Approval Distribution",
    "loan_status.png"
)

# ==========================================
# GENDER DISTRIBUTION
# ==========================================

save_bar(
    "Gender",
    "Gender Distribution",
    "gender_distribution.png"
)

# ==========================================
# EDUCATION DISTRIBUTION
# ==========================================

save_bar(
    "Education",
    "Education Distribution",
    "education_distribution.png"
)

# ==========================================
# PROPERTY AREA
# ==========================================

save_bar(
    "Property_Area",
    "Property Area Distribution",
    "property_area.png"
)

# ==========================================
# CREDIT HISTORY
# ==========================================

save_bar(
    "Credit_History",
    "Credit History Distribution",
    "credit_history.png"
)

# ==========================================
# APPLICANT INCOME
# ==========================================

plt.figure(figsize=(8,5))

plt.hist(
    df["ApplicantIncome"],
    bins=20
)

plt.title("Applicant Income Distribution")

plt.xlabel("Applicant Income")

plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "applicant_income.png"
)

plt.close()

# ==========================================
# LOAN AMOUNT
# ==========================================

plt.figure(figsize=(8,5))

plt.hist(
    df["LoanAmount"],
    bins=20
)

plt.title("Loan Amount Distribution")

plt.xlabel("Loan Amount")

plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "loan_amount.png"
)

plt.close()

# ==========================================
# LOAN TERM
# ==========================================

plt.figure(figsize=(8,5))

df["Loan_Amount_Term"].value_counts().sort_index().plot(
    kind="bar"
)

plt.title("Loan Amount Term")

plt.xlabel("Loan Term")

plt.ylabel("Applicants")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "loan_term.png"
)

plt.close()

# ==========================================
# MARRIED VS LOAN STATUS
# ==========================================

cross = pd.crosstab(
    df["Married"],
    df["Loan_Status"]
)

cross.plot(
    kind="bar",
    figsize=(8,5)
)

plt.title("Married vs Loan Status")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "married_vs_loan.png"
)

plt.close()
# ==========================================
# EDUCATION VS LOAN STATUS
# ==========================================

education_status = pd.crosstab(
    df["Education"],
    df["Loan_Status"]
)

education_status.plot(
    kind="bar",
    figsize=(8,5)
)

plt.title("Education vs Loan Status")

plt.xlabel("Education")

plt.ylabel("Applicants")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "education_vs_loan.png"
)

plt.close()

# ==========================================
# PROPERTY AREA VS LOAN STATUS
# ==========================================

property_status = pd.crosstab(
    df["Property_Area"],
    df["Loan_Status"]
)

property_status.plot(
    kind="bar",
    figsize=(8,5)
)

plt.title("Property Area vs Loan Status")

plt.xlabel("Property Area")

plt.ylabel("Applicants")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "property_vs_loan.png"
)

plt.close()

# ==========================================
# BUSINESS SUMMARY
# ==========================================

approved = (df["Loan_Status"] == "Y").sum()
rejected = (df["Loan_Status"] == "N").sum()

print("\n" + "=" * 60)
print("BANK LOAN RISK ANALYTICS SUMMARY")
print("=" * 60)

print(f"Total Applications       : {len(df)}")
print(f"Approved Loans          : {approved}")
print(f"Rejected Loans          : {rejected}")
print(f"Approval Rate           : {approved / len(df) * 100:.2f}%")
print(f"Average Applicant Income: {df['ApplicantIncome'].mean():.2f}")
print(f"Average Loan Amount     : {df['LoanAmount'].mean():.2f}")

print("\nLoan Status")
print(df["Loan_Status"].value_counts())

print("\nGender Distribution")
print(df["Gender"].value_counts())

print("\nEducation Distribution")
print(df["Education"].value_counts())

print("\nProperty Area")
print(df["Property_Area"].value_counts())

print("\nCredit History")
print(df["Credit_History"].value_counts())

print("\nSUCCESS ✓")
print("Charts generated successfully.")
print("Saved inside screenshots folder.")
print("=" * 60)
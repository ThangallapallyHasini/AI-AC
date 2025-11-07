# clean_employee_data.py
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 1) Load dataset
df = pd.read_csv("employees.csv")

print("Original Dataset:\n", df.head(), "\n")

# 2) Handle missing values
# - salary: fill with mean (numeric). convert strings like "NaN" automatically when reading.
df['salary'] = pd.to_numeric(df['salary'], errors='coerce')   # assure numeric
salary_mean = df['salary'].mean()
df['salary'] = df['salary'].fillna(salary_mean)

# - department: fill with 'Unknown'
df['department'] = df['department'].fillna('Unknown')

# - joining_date: fill with mode (most frequent non-null string)
if df['joining_date'].isna().all():
    df['joining_date'] = pd.NaT
else:
    mode_dates = df['joining_date'].mode()
    if len(mode_dates) > 0:
        df['joining_date'] = df['joining_date'].fillna(mode_dates[0])
    else:
        df['joining_date'] = df['joining_date'].fillna('1970-01-01')

# 3) Convert joining_date to datetime (try multiple formats)
df['joining_date'] = pd.to_datetime(df['joining_date'], errors='coerce', dayfirst=True)

# If any joining_date couldn't be parsed (NaT), fill with median/earliest non-null date
if df['joining_date'].isna().any():
    non_null = df['joining_date'].dropna()
    if not non_null.empty:
        median_date = non_null.min()
        df['joining_date'] = df['joining_date'].fillna(median_date)
    else:
        df['joining_date'] = df['joining_date'].fillna(pd.to_datetime('1970-01-01'))

# 4) Standardize department names
def standardize_department(dept):
    if pd.isna(dept):
        return "Unknown"
    s = str(dept).strip().lower()
    if s in ("hr", "human resources", "human-resource", "humanresources"):
        return "HR"
    if s in ("it", "information technology", "information_technology"):
        return "IT"
    if s in ("finance", "fin", "finaNCE".lower()):
        return "Finance"
    if s in ("marketing", "market", "mktg"):
        return "Marketing"
    if s in ("unknown", ""):
        return "Unknown"
    return s.capitalize()

df['department'] = df['department'].apply(standardize_department)

# 5) Encode categorical variables (department, job_role)
label_encoders = {}
for col in ['department', 'job_role']:
    le = LabelEncoder()
    # Fill na for encoding safely
    df[col] = df[col].fillna('Unknown')
    df[col + '_encoded'] = le.fit_transform(df[col].astype(str))
    label_encoders[col] = le

# 6) Save cleaned file and print results
df.to_csv("cleaned_employees.csv", index=False)
print("Cleaned Dataset:\n", df)
print("\n✅ Cleaned data saved as 'cleaned_employees.csv'")

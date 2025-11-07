import pandas as pd

# Step 1: Load the dataset
data = pd.read_csv("healthcare_records.csv")

print("Original Dataset:")
print(data.head(), "\n")

# Step 2: Fill missing numeric values with column mean
numeric_cols = ['blood_pressure', 'heart_rate']
for col in numeric_cols:
    data[col].fillna(data[col].mean(), inplace=True)

# Step 3: Convert height from centimeters to meters
data['height_m'] = data['height_cm'] / 100

# Step 4: Standardize categorical labels for 'gender'
data['gender'] = data['gender'].str.strip().str.lower()  # remove spaces, make lowercase
data['gender'] = data['gender'].replace({
    'm': 'Male',
    'male': 'Male',
    'f': 'Female',
    'female': 'Female'
})

# Step 5: Drop irrelevant columns (patient_id, height_cm)
data = data.drop(columns=['patient_id', 'height_cm'])

# Step 6: Show the cleaned dataset
print("Cleaned Dataset:")
print(data.head(), "\n")

# Step 7: Save the cleaned data
data.to_csv("cleaned_healthcare_records.csv", index=False)

print("✅ Data cleaning completed successfully!")
print("Cleaned file saved as 'cleaned_healthcare_records.csv'")

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Step 1: Load the dataset
data = pd.read_csv("sales_transactions.csv")

print("Original Dataset:")
print(data.head(), "\n")

# Step 2: Convert 'transaction_date' to datetime format
data['transaction_date'] = pd.to_datetime(data['transaction_date'], errors='coerce')

# Step 3: Drop rows with invalid or missing dates
data = data.dropna(subset=['transaction_date'])

# Step 4: Create a new 'Month-Year' column
data['Month-Year'] = data['transaction_date'].dt.strftime('%b-%Y')

# Step 5: Remove rows with zero or negative transaction amounts
data = data[data['transaction_amount'] > 0]

# Step 6: Normalize 'transaction_amount' using Min-Max Scaling
scaler = MinMaxScaler()
data['normalized_amount'] = scaler.fit_transform(data[['transaction_amount']])

# Step 7: Display the cleaned and normalized DataFrame
print("Preprocessed Dataset:")
print(data.head(), "\n")

# Step 8: Save the cleaned data to a new CSV file
data.to_csv("preprocessed_sales_transactions.csv", index=False)

print("✅ Preprocessing completed successfully!")
print("Cleaned file saved as 'preprocessed_sales_transactions.csv'")

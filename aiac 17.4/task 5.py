# Step 1: Install dependencies (only once)
# pip install pandas scikit-learn

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# -----------------------------
# Step 2: Example Financial Dataset
# -----------------------------
data = {
    'date': pd.date_range(start='2025-01-01', periods=15, freq='D'),
    'company_name': ['AlphaCorp', 'BetaInc', 'AlphaCorp', 'BetaInc', 'AlphaCorp',
                     'BetaInc', 'AlphaCorp', 'BetaInc', 'AlphaCorp', 'BetaInc',
                     'AlphaCorp', 'BetaInc', 'AlphaCorp', 'BetaInc', 'AlphaCorp'],
    'sector': ['Tech', 'Finance', 'Tech', 'Finance', 'Tech',
               'Finance', 'Tech', 'Finance', 'Tech', 'Finance',
               'Tech', 'Finance', 'Tech', 'Finance', 'Tech'],
    'stock_price': [120, 85, None, 90, 122, 89, 125, None, 128, 95, 130, 97, 132, 99, None],
    'volume': [15000, None, 16000, 15500, None, 15000, 17000, 16500, None, 16000, 17500, 17000, 18000, None, 19000]
}

df = pd.DataFrame(data)

# -----------------------------
# Step 3: Handle Missing Values
# -----------------------------
# Fill missing stock prices with forward fill (then backward fill as backup)
df['stock_price'] = df['stock_price'].fillna(method='ffill').fillna(method='bfill')

# Fill missing volume with mean
df['volume'] = df['volume'].fillna(df['volume'].mean())

# -----------------------------
# Step 4: Create New Features (Moving Averages)
# -----------------------------
# Sort by date to ensure correct order
df = df.sort_values(by='date')

# Calculate moving averages by company (7-day and 30-day)
df['ma_7'] = df.groupby('company_name')['stock_price'].transform(lambda x: x.rolling(window=7, min_periods=1).mean())
df['ma_30'] = df.groupby('company_name')['stock_price'].transform(lambda x: x.rolling(window=30, min_periods=1).mean())

# -----------------------------
# Step 5: Normalize Continuous Variables
# -----------------------------
scaler = StandardScaler()
df[['stock_price_scaled', 'volume_scaled', 'ma_7_scaled', 'ma_30_scaled']] = scaler.fit_transform(
    df[['stock_price', 'volume', 'ma_7', 'ma_30']]
)

# -----------------------------
# Step 6: Encode Categorical Columns
# -----------------------------
encoder_sector = LabelEncoder()
encoder_company = LabelEncoder()

df['sector_encoded'] = encoder_sector.fit_transform(df['sector'])
df['company_encoded'] = encoder_company.fit_transform(df['company_name'])

# -----------------------------
# Step 7: Final Processed DataFrame
# -----------------------------
print("\n✅ Feature-Engineered Financial Dataset:\n")
print(df.head(10))

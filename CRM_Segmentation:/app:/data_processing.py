import pandas as pd

# Load the dataset
#data = pd.read_csv('../data/customers_extended.csv')
data = pd.read_csv('data:/customers_extended.csv')

# Basic cleaning
data.dropna(inplace=True)  # Remove missing values

# Convert Income to numeric
data['Income'] = data['Income'].replace({'₹': '', ',': ''}, regex=True).astype(float)

# Display the first few rows of the dataset
print(data.head())

# Save cleaned data
#data.to_csv('../data/cleaned_customers_extended.csv', index=False)
data.to_csv('data:/cleaned_customers_extended.csv', index=False)

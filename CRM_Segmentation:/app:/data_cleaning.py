import pandas as pd

# Load the dataset
#data = pd.read_csv('../data/customers.csv')
data = pd.read_csv('data:/customers_extended.csv')


# Basic cleaning
data.dropna(inplace=True)  # Remove missing values
data['Income'] = data['Income'].replace({'₹': '', ',': ''}, regex=True).astype(float)  # Clean income field

# Save cleaned data
#data.to_csv('../data/cleaned_customers.csv', index=False)
data.to_csv('data:/cleaned_customers.csv', index=False)
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load cleaned data
#data = pd.read_csv('../data/cleaned_customers_extended.csv')
data = pd.read_csv('data:/cleaned_customers_extended.csv')


# Select features for clustering (you can modify this based on your analysis)
features = data[['Age', 'Income']]  # Select relevant numeric features

# Fit KMeans
kmeans = KMeans(n_clusters=5)  # Choose number of clusters
data['segment'] = kmeans.fit_predict(features)

# Save segmented data
#data.to_csv('../data/segmented_customers_extended.csv', index=False)
data.to_csv('data:/segmented_customers_extended.csv', index=False)

# Optional: Visualize clusters
plt.scatter(data['Age'], data['Income'], c=data['segment'], cmap='viridis')
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Customer Segments')
plt.show()

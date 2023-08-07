import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load the dataset
data = pd.read_csv('customer_data.csv')

# Extract the relevant columns for clustering (you can select appropriate columns based on your data)
selected_columns = ['PurchaseHistory', 'BrowsingBehavior', 'Demographics']
X = data[selected_columns]

# Data preprocessing - Standardize the features to have mean=0 and variance=1
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine the optimal number of clusters using the elbow method
import matplotlib.pyplot as plt

inertia = []
for num_clusters in range(1, 11):
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

# Plot the elbow curve
plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Elbow Method to Determine Optimal Number of Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()

# Based on the elbow curve, select the optimal number of clusters (K) and run K-means again
optimal_num_clusters = 3  # You can change this value based on the elbow curve
kmeans = KMeans(n_clusters=optimal_num_clusters, random_state=42)
kmeans.fit(X_scaled)

# Add the cluster labels back to the original dataset
data['Cluster'] = kmeans.labels_

# Explore the characteristics of each cluster
cluster_characteristics = data.groupby('Cluster').mean()

# Now, you can use the cluster_characteristics to tailor marketing campaigns and promotions for each segment.
print(cluster_characteristics)

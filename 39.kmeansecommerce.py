import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(data):
    # Select relevant features for clustering
    features = ['TotalAmountSpent', 'NumberOfItemsPurchased']
    X = data[features]

    # Scale the features to have zero mean and unit variance
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled

def apply_kmeans(X_scaled, num_clusters):
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    labels = kmeans.fit_predict(X_scaled)
    return labels

def visualize_clusters(X_scaled, labels, num_clusters):
    # Perform PCA for dimensionality reduction for visualization
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    # Create a DataFrame for visualization
    df = pd.DataFrame(data=X_pca, columns=['PC1', 'PC2'])
    df['Cluster'] = labels

    # Plot the clusters using scatter plot
    plt.figure(figsize=(10, 6))
    for cluster in range(num_clusters):
        cluster_data = df[df['Cluster'] == cluster]
        plt.scatter(cluster_data['PC1'], cluster_data['PC2'], label=f'Cluster {cluster}')

    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.title('Customer Segmentation using K-Means')
    plt.legend()
    plt.show()

def main():
    file_path = 'path/to/your/transaction_data.csv'
    num_clusters = 5  # You can adjust the number of clusters based on the business needs

    # Load and preprocess the data
    data = load_data(file_path)
    X_scaled = preprocess_data(data)

    # Apply K-Means clustering
    labels = apply_kmeans(X_scaled, num_clusters)

    # Visualize the clusters
    visualize_clusters(X_scaled, labels, num_clusters)

if __name__ == "__main__":
    main()

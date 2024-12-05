# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import os
from sklearn.metrics import silhouette_score
import sys
sys.path.append(os.path.abspath(r'C:\Users\swath\OneDrive\Github\Imperial Brands'))
import Features as Fts
import Cleaning as cln

# Load the dataset
file_data = r"C:\Users\swath\OneDrive\Github\Imperial Brands\output\merged_file.csv"
data = pd.read_csv(file_data)
output_directory = r'C:\Users\swath\OneDrive\Github\Imperial Brands\output'

# Call feature function
customer_data = Fts.engineer_customer_data(data, output_directory)

# Call Preprocress function from cleaning.py
cln.preprocess_data


def perform_customer_clustering(data, n_clusters=3):
    """
    This function performs customer segmentation using KMeans clustering.
    It standardizes the features, applies the Elbow method to find the optimal number of clusters,
    computes the silhouette score, and visualizes the results.
    
    Parameters:
    - data: DataFrame containing the customer data with columns 'Frequency', 'Monetary', 'age', 'income', 'satisfaction_score'
    - n_clusters: Number of clusters for KMeans (default is 4, but can be changed)
    
    Returns:
    - customer_data: DataFrame with added 'Cluster' and 'Segment_Label' columns
    - cluster_analysis: DataFrame with mean feature values for each cluster
    - silhouette_avg: Silhouette score for the clustering
    """
    # Select relevant features for clustering
    features = data[['Frequency', 'Monetary', 'age', 'income', 'satisfaction_score']]

    # Standardize the features to ensure they have a mean of 0 and a standard deviation of 1
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    # Calculate the inertia for different values of K (Elbow Method)
    inertia = []
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(scaled_features)
        inertia.append(kmeans.inertia_)

    # Plot the elbow curve
    plt.plot(range(1, 11), inertia, marker='o')
    plt.title('Elbow Method For Optimal K')
    plt.xlabel('Number of clusters (K)')
    plt.ylabel('Inertia')
    plt.show()

    # Apply KMeans clustering with the specified number of clusters (n_clusters)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    data['Cluster'] = kmeans.fit_predict(scaled_features)

    # Calculate silhouette score to validate clustering
    silhouette_avg = silhouette_score(scaled_features, data['Cluster'])
    print(f'Silhouette Score: {silhouette_avg}')

    # Inspect the resulting clusters
    # print(data[['id', 'Frequency', 'Monetary', 'Cluster']].head())

    # Group by clusters and calculate mean of features to understand the segments
    cluster_analysis = data.groupby('Cluster')[['Frequency', 'Monetary', 'age', 'income', 'satisfaction_score']].mean()
    print(cluster_analysis)

    # Assign meaningful labels to the clusters
    cluster_labels = {
        0: 'Low Frequency, Low Spend, High Satisfaction',
        1: 'Moderate Frequency, Higher Spend, High Satisfaction',
        2: 'High Frequency, Higher Spend, Moderate Satisfaction'

    }
    data['Segment_Label'] = data['Cluster'].map(cluster_labels)

    # Create a scatter plot to visualize the clusters
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=data['Frequency'], y=data['Monetary'], hue=data['Segment_Label'], palette='Set2', s=100, alpha=0.7)
    plt.title('Customer Segments Based on Frequency and Monetary')
    plt.xlabel('Frequency')
    plt.ylabel('Monetary')
    plt.legend(title='Cluster')
    plt.show()

    # Return the customer data with added segments, and cluster analysis
    return data, cluster_analysis, silhouette_avg

customer_data, cluster_analysis, silhouette_avg = perform_customer_clustering(customer_data)
perform_customer_clustering(data, n_clusters=3)

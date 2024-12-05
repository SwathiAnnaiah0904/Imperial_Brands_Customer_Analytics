import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
import os
import sys
sys.path.append(os.path.abspath(r'C:\Users\swath\OneDrive\Github\Imperial Brands'))
import Cleaning as cln

# Load your dataset
file_data = r"C:\Users\swath\OneDrive\Github\Imperial Brands\output\Engineered_customer_file.csv"
df = pd.read_csv(file_data)

# Call preprocess function from Cleaning.py
cln.preprocess_data(df)

def perform_clustering_analysis(df, features, n_clusters=2, cluster_range=(2, 11)):
    """
    This function performs the entire clustering analysis including feature scaling, KMeans clustering, 
    silhouette score calculation, and cluster summary visualization.

    Parameters:
    - df: DataFrame with the data.
    - features: List of column names to be used as features for clustering.
    - n_clusters: Initial number of clusters for KMeans (default is 2).
    - cluster_range: Range of cluster numbers for silhouette score analysis (default is 2 to 10).
    """
    # Step 1: Feature scaling
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df[features])

    # Step 2: KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['cluster'] = kmeans.fit_predict(scaled_features)

    # Step 3: Find optimal number of clusters using Silhouette Method
    sil_scores = []
    for k in range(cluster_range[0], cluster_range[1]):  # Try a range of k from cluster_range[0] to cluster_range[1]
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(scaled_features)
        sil_scores.append(silhouette_score(scaled_features, kmeans.labels_))

    # Step 4: Calculate and print silhouette score for current clustering
    silhouette_avg = silhouette_score(scaled_features, df['cluster'])
    print(f'Silhouette Score: {silhouette_avg}')

    # Step 5: Plot Silhouette Scores for different k values
    plt.figure(figsize=(10, 6))
    plt.plot(range(cluster_range[0], cluster_range[1]), sil_scores, marker='o')
    plt.title('Silhouette Score for Different k')
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Silhouette Score')
    plt.show()

    # Step 6: Analyze the clusters
    cluster_summary = df.groupby('cluster').agg({
        'income': 'mean',
        'Monetary': 'mean',
        'gender_male': 'mean',
        'gender_female': 'mean'
    })

    cluster_summary_demo = df.groupby('cluster').agg({
        'age': 'mean',
        'satisfaction_score': 'mean',
        'Frequency': 'mean',
        'gender_male': 'mean',
        'gender_female': 'mean'
    })
    print(cluster_summary_demo)

    # Step 7: Plot Cluster Summary with table
    def plot_cluster_summary_with_table(cluster_summary):
        """
        This function visualizes the cluster summary by creating a bar plot for each feature in the summary.
        It also displays the mean values for each feature in a table below the plot.
        
        Parameters:
        - cluster_summary: DataFrame with the mean of features for each cluster.
        """
        plt.figure(figsize=(14, 8))
        ax = cluster_summary.plot(kind='bar', figsize=(14, 8), colormap='Set2')
        plt.title('Cluster Summary: Mean Values for Each Feature', fontsize=16)
        plt.xlabel('Cluster', fontsize=14)
        plt.ylabel('Mean Value', fontsize=14)
        plt.xticks(rotation=0)

        table_data = cluster_summary.round(2)
        table = plt.table(cellText=table_data.values,
                         colLabels=table_data.columns,
                         cellLoc='center', loc='bottom', colColours=['#f5f5f5']*len(table_data.columns))
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1, 1.5)

        plt.tight_layout()
        plt.show()

    plot_cluster_summary_with_table(cluster_summary)
    plot_cluster_summary_with_table(cluster_summary_demo)


features = ['age', 'income', 'satisfaction_score', 'Frequency', 'Monetary', 'gender_male', 'gender_female']
perform_clustering_analysis(df, features)




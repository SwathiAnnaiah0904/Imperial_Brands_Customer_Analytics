import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import sys
import os
import Cleaning as cln
sys.path.append(os.path.abspath(r'C:\Users\swath\OneDrive\Github\Imperial Brands'))
import Plotting  as pltg
import frequency_monetary_cluster as fmc
import demo_cluster as dc



file_data = r"C:\Users\swath\OneDrive\Github\Imperial Brands\output\Engineered_customer_file.csv"
df = pd.read_csv(file_data)
cln.preprocess_data(df) 


# Call Plot functions from Plotting.py file
pltg.plot_promotion_usage_vs_frequency(df)
pltg.plot_loyalty_status_vs_frequency(df)
pltg.plot_age_based_segmentation_and_satisfaction(df)
pltg.plot_income_based_segmentation_and_satisfaction(df)

# Call frequency_monetary_cluster.py file 
fmc.perform_customer_clustering

# Call demo_cluster.py file 
dc.perform_clustering_analysis









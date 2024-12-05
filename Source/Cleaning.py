import pandas as pd
import os
from sklearn.preprocessing import OneHotEncoder

# Specify the path to the CSV file
file_orders = 'C:/Users/swath/OneDrive/Github/Imperial Brands/Data/orders.csv'
file_customers = 'C:/Users/swath/OneDrive/Github/Imperial Brands/Data/customers.csv'

# Read the CSV file into a pandas DataFrame
df_orders = pd.read_csv(file_orders)
df_customers = pd.read_csv(file_customers)

# Cleaning orders data 
df_orders['Order Date'] = pd.to_datetime(df_orders['Order Date']) #changed date type to date column 
df_orders['id'] = df_orders['id'].astype(int)
df_orders['Value'] = df_orders['Value'].replace({'$': '', '€': '', '£': '', 'GBP': ''}, regex=True)  #Unified Value column for numeric col type
df_orders['Value'] = pd.to_numeric(df_orders['Value'], errors='coerce')

# Merging Orders and customer data into one dataframe
df = pd.merge(df_orders, df_customers, on='id', how='inner')
df['income'] = df['income'].astype(float) 

# Create the directory if it doesn't exist to export the dataframe
directory = r'C:\Users\swath\OneDrive\Github\Imperial Brands\output'
if not os.path.exists(directory):
    os.makedirs(directory)
df.to_csv(os.path.join(directory, 'merged_file.csv'), index=False)

def preprocess_data(df):
    """
    This function performs data preprocessing including:
    - Age-based segmentation
    - Income-based segmentation
    - One-Hot Encoding for gender and region

    Parameters:
    - df: The input DataFrame containing the data to preprocess.

    Returns:
    - df: The DataFrame with the added columns for age group, income group, and one-hot encoded gender and region.
    """
    # Age-based segmentation
    age_bins = [13, 18, 25, 35, 45, 55, 65]
    age_labels = ['13-18','18-25', '26-35', '36-45', '46-55', '55+']
    df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, right=False)

    # Income-based segmentation
    income_bins = [0, 20000, 40000, 60000]
    income_labels = ['low(0-20000)', 'medium(20001-40000)', 'high(40001+)']
    df['income_group'] = pd.cut(df['income'], bins=income_bins, labels=income_labels)

    # One-Hot Encoding for gender and region
    encoder = OneHotEncoder(sparse_output=False)
    
    # Gender encoding
    gender_encoded = encoder.fit_transform(df[['gender']])
    df['gender_male'] = gender_encoded[:, 0]
    df['gender_female'] = gender_encoded[:, 1]
    
    # Region encoding
    region_encoded = encoder.fit_transform(df[['region']])
    region_labels = encoder.categories_[0]  # Get the category labels for the region
    for i, label in enumerate(region_labels):
        df[f'region_{label}'] = region_encoded[:, i]
    
    return df


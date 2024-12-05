import pandas as pd
import os

def engineer_customer_data(data, output_directory):
    """
    This function processes the given customer transaction data to generate frequency and monetary features
    and outputs the engineered customer data as a CSV file.

    Parameters:
    - data: DataFrame with transaction data containing at least 'id', 'Order Date', and 'Value' columns.
    - output_directory: Directory where the resulting CSV file will be saved.

    Returns:
    - customer_data: A DataFrame with engineered features: 'Frequency' and 'Monetary'.
    """
    # Frequency: Number of purchases per customer
    data['Order Date'] = pd.to_datetime(data['Order Date'])
    frequency = data.groupby('id')['Order Date'].count().reset_index()
    frequency.columns = ['id', 'Frequency']

    # Monetary: Total value spent by each customer
    monetary = data.groupby('id')['Value'].sum().reset_index()
    monetary.columns = ['id', 'Monetary']

    # Merge these features back into the main dataframe
    customer_data = data[['id', 'age', 'gender', 'income', 'education', 'region', 'loyalty_status', 'promotion_usage', 'satisfaction_score']].drop_duplicates()
    customer_data = pd.merge(customer_data, frequency, on='id', how='left')
    customer_data = pd.merge(customer_data, monetary, on='id', how='left')

    customer_data.fillna(0, inplace=True)

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    customer_data.to_csv(os.path.join(output_directory, 'Engineered_customer_file.csv'), index=False)
    
    return customer_data


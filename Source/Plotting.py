import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import Cleaning as cln
from sklearn.preprocessing import OneHotEncoder

file_data = r"C:\Users\swath\OneDrive\Github\Imperial Brands\output\Engineered_customer_file.csv"
df = pd.read_csv(file_data)

# Call preprocess function from Cleaning.py
cln.preprocess_data(df) 


def plot_promotion_usage_vs_frequency(df):
    """
    This function plots the average monetary value against frequency for two categories:
    promotion usage = 0 and promotion usage = 1.
    It groups the data by promotion_usage and frequency, calculating the mean of 'Monetary' for each group,
    and then plots separate lines for promotion usage = 0 and promotion usage = 1.

    Parameters:
    df (DataFrame): The input dataframe that contains 'promotion_usage', 'Frequency', and 'Monetary' columns.
    """
    # Step 1: Group the data by Promotion Usage and Frequency, calculating the mean Monetary for each group
    df_grouped = df.groupby(['promotion_usage', 'Frequency']).agg({'Monetary': 'mean'}).reset_index()

    # Step 2: Create a line plot for both promotion_usage = 0 and promotion_usage = 1
    plt.figure(figsize=(12, 6))

    # Plot for promotion_usage = 0
    sns.lineplot(x='Frequency', y='Monetary', data=df_grouped[df_grouped['promotion_usage'] == 0], 
                 label='Promotion Usage = 0', color='blue', marker='o')

    # Plot for promotion_usage = 1
    sns.lineplot(x='Frequency', y='Monetary', data=df_grouped[df_grouped['promotion_usage'] == 1], 
                 label='Promotion Usage = 1', color='red', marker='o')

    # Adding title and labels
    plt.title('Promotion Usage vs Frequency of Purchases')
    plt.xlabel('Frequency of Purchases')
    plt.ylabel('Average Monetary Value')
    plt.legend(title="Promotion Usage")
    plt.grid(True)
    plt.show()



def plot_loyalty_status_vs_frequency(df):
    """
    This function plots the average monetary value against frequency for each loyalty status.
    It groups the data by loyalty_status and frequency, calculating the mean of 'Monetary' for each group,
    and then plots separate lines for each loyalty status.

    Parameters:
    df (DataFrame): The input dataframe that contains 'loyalty_status', 'Frequency', and 'Monetary' columns.
    """
    # Step 1: Group the data by Loyalty Status and Frequency, calculating the mean Monetary for each group 
    df_grouped = df.groupby(['loyalty_status', 'Frequency']).agg({'Monetary': 'mean'}).reset_index()

    # Step 2: Create a line plot for each loyalty status (Gold, Silver, Regular)
    plt.figure(figsize=(12, 6))

    # Plot for loyalty_status = 'Gold'
    sns.lineplot(x='Frequency', y='Monetary', data=df_grouped[df_grouped['loyalty_status'] == 'Gold'], label='Gold', color='gold', marker='o')

    # Plot for loyalty_status = 'Silver'
    sns.lineplot(x='Frequency', y='Monetary', data=df_grouped[df_grouped['loyalty_status'] == 'Silver'], label='Silver', color='silver', marker='o')

    # Plot for loyalty_status = 'Regular'
    sns.lineplot(x='Frequency', y='Monetary', data=df_grouped[df_grouped['loyalty_status'] == 'Regular'], label='Regular', color='blue', marker='o')

    # Adding title and labels
    plt.title('Loyalty Status vs Frequency of Purchases')
    plt.xlabel('Frequency of Purchases')
    plt.ylabel('Average Monetary Value')
    plt.legend(title="Loyalty Status")
    plt.grid(True)
    plt.show()


def plot_age_based_segmentation_and_satisfaction(df):
    """
    This function creates two plots:
    1. A count plot showing the distribution of customers across different age groups.
    2. A boxplot showing the distribution of satisfaction scores across different age groups.

    Parameters:
    df (DataFrame): The input dataframe that contains 'age_group' and 'satisfaction_score' columns.
    """
    # Step 1: Plot for Age-based Segmentation
    plt.figure(figsize=(10, 6))
    sns.countplot(x='age_group', data=df, palette='viridis')
    plt.title('Customer Distribution by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Number of Customers')
    plt.show()

    # Step 3: Boxplot to compare satisfaction score across Age Groups
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='age_group', y='satisfaction_score', data=df, palette='Set2')
    plt.title('Satisfaction Score Distribution by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Satisfaction Score')
    plt.show()



def plot_income_based_segmentation_and_satisfaction(df):
    """
    This function creates two plots:
    1. A count plot showing the distribution of customers across different income groups.
    2. A boxplot showing the distribution of satisfaction scores across different income groups.

    Parameters:
    df (DataFrame): The input dataframe that contains 'income_group' and 'satisfaction_score' columns.
    """
    # Step 2: Plot for Income-based Segmentation
    plt.figure(figsize=(10, 6))
    sns.countplot(x='income_group', data=df, palette='coolwarm')
    plt.title('Customer Distribution by Income Group')
    plt.xlabel('Income Group')
    plt.ylabel('Number of Customers')
    plt.show()

    # Step 4: Boxplot to compare satisfaction score across Income Groups
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='income_group', y='satisfaction_score', data=df, palette='Set1')
    plt.title('Satisfaction Score Distribution by Income Group')
    plt.xlabel('Income Group')
    plt.ylabel('Satisfaction Score')
    plt.show()




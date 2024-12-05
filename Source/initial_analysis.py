import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_data = r"C:\Users\swath\OneDrive\Github\Imperial Brands\output\merged_file.csv"
df = pd.read_csv(file_data)

# Function for Monthly Revenue Trend
def plot_monthly_revenue(df):
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Month'] = df['Order Date'].dt.to_period('M')
    monthly_value = df.groupby('Month')['Value'].sum()
    
    print("\nMonthly Revenue Trend:")
    print(monthly_value)

    # Plotting Monthly Revenue Trend
    plt.figure(figsize=(10, 6))
    monthly_value.plot(kind='line', marker='o', color='orange')
    plt.title('Monthly Revenue Trend')
    plt.xlabel('Month')
    plt.ylabel('Total Order Value')
    plt.xticks(rotation=45)
    plt.show()

# Function for Loyalty Status and Order Value
def plot_loyalty_status_vs_order_value(df):
    loyalty_value = df.groupby('loyalty_status')['Value'].mean()
    
    print("\nAverage Order Value by Loyalty Status:")
    print(loyalty_value)

    # Plotting Loyalty Status vs Order Value with values on top of bars
    plt.figure(figsize=(8, 6))
    ax = sns.barplot(x=loyalty_value.index, y=loyalty_value.values, palette='Blues')
    plt.title('Average Order Value by Loyalty Status')
    plt.xlabel('Loyalty Status')
    plt.ylabel('Average Order Value')

    # Adding the values on top of the bars
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.2f}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', 
                    fontsize=12, color='black', 
                    xytext=(0, 5), textcoords='offset points')
    plt.show()

# Function for Promotion Usage vs Order Value
def plot_promotion_usage_vs_order_value(df):
    promotion_value = df.groupby('promotion_usage')['Value'].mean()
    
    print("\nAverage Order Value by Promotion Usage:")
    print(promotion_value)

    # Plotting Promotion Usage vs Order Value with values on top of bars
    plt.figure(figsize=(8, 6))
    ax = sns.barplot(x=promotion_value.index, y=promotion_value.values, palette='Greens')
    plt.title('Average Order Value by Promotion Usage')
    plt.xlabel('Promotion Usage')
    plt.ylabel('Average Order Value')

    # Adding the values on top of the bars
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.2f}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', 
                    fontsize=12, color='black', 
                    xytext=(0, 5), textcoords='offset points')
    plt.show()

# Function for Satisfaction Scores and Customer Retention
def plot_satisfaction_score_vs_order_value(df):
    satisfaction_value = df.groupby('satisfaction_score')['Value'].mean()
    
    print("\nAverage Order Value by Satisfaction Score:")
    print(satisfaction_value)

    # Plotting Satisfaction Scores vs Order Value with values on top of the points
    plt.figure(figsize=(8, 6))
    ax = sns.lineplot(x=satisfaction_value.index, y=satisfaction_value.values, marker='o', color='purple')
    plt.title('Average Order Value by Satisfaction Score')
    plt.xlabel('Satisfaction Score')
    plt.ylabel('Average Order Value')

    # Adding the values on top of the points
    for x, y in zip(satisfaction_value.index, satisfaction_value.values):
        ax.text(x, y, f'{y:.2f}', ha='center', va='bottom', fontsize=12, color='black')
    plt.show()



# Function for Region vs Order Value
def plot_region_vs_order_value(df):
    # Grouping by region and calculating the average order value
    region_value = df.groupby('region')['Value'].mean()
    
    print("\nAverage Order Value by Region:")
    print(region_value)

    # Plotting Region vs Order Value with values on top of bars
    plt.figure(figsize=(8, 6))
    ax = sns.barplot(x=region_value.index, y=region_value.values, palette='Set2')
    plt.title('Average Order Value by Region')
    plt.xlabel('Region')
    plt.ylabel('Average Order Value')

    # Adding the values on top of the bars
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.2f}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', 
                    fontsize=12, color='black', 
                    xytext=(0, 5), textcoords='offset points')
    plt.show()


# Function for Region vs Order Count
def plot_region_vs_order_count(df):
    # Grouping by region and counting the number of orders
    region_order_count = df.groupby('region').size()
    
    print("\nOrder Count by Region:")
    print(region_order_count)

    # Plotting Region vs Order Count with values on top of bars
    plt.figure(figsize=(8, 6))
    ax = sns.barplot(x=region_order_count.index, y=region_order_count.values, palette='Set2')
    plt.title('Order Count by Region')
    plt.xlabel('Region')
    plt.ylabel('Order Count')

    # Adding the values on top of the bars
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.0f}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', 
                    fontsize=12, color='black', 
                    xytext=(0, 5), textcoords='offset points')
    plt.show()



# Function for Loyalty Status vs Order Count
def plot_loyalty_status_vs_order_count(df):
    # Grouping by loyalty_status and counting the number of orders
    loyalty_order_count = df.groupby('loyalty_status').size()
    
    print("\nOrder Count by Loyalty Status:")
    print(loyalty_order_count)

    # Plotting Loyalty Status vs Order Count with values on top of bars
    plt.figure(figsize=(8, 6))
    ax = sns.barplot(x=loyalty_order_count.index, y=loyalty_order_count.values, palette='Set3')
    plt.title('Order Count by Loyalty Status')
    plt.xlabel('Loyalty Status')
    plt.ylabel('Order Count')

    # Adding the values on top of the bars
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.0f}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', 
                    fontsize=12, color='black', 
                    xytext=(0, 5), textcoords='offset points')
    plt.show()




# Function for Education vs Loyalty Status Count
def plot_education_vs_loyalty_status_count(df):
    # Grouping by education and loyalty_status, then counting the number of orders
    education_loyalty_count = df.groupby(['education', 'loyalty_status']).size().unstack(fill_value=0)
    
    print("\nOrder Count by Education Level and Loyalty Status:")
    print(education_loyalty_count)

    # Plotting Education vs Loyalty Status Count with values on top of bars
    education_loyalty_count.plot(kind='bar', stacked=False, figsize=(10, 6), cmap='Set2')

    # Adding the values on top of the bars
    for p in plt.gca().patches:
        height = p.get_height()
        if height > 0:
            plt.gca().annotate(f'{height:.0f}', 
                               (p.get_x() + p.get_width() / 2., p.get_height()), 
                               ha='center', va='center', 
                               fontsize=12, color='black', 
                               xytext=(0, 5), textcoords='offset points')
    
    plt.title('Order Count by Education Level and Loyalty Status')
    plt.xlabel('Education Level')
    plt.ylabel('Order Count')
    plt.xticks(rotation=45)
    plt.show()


# Function for Region vs Loyalty Status Count
def plot_region_vs_loyalty_status_count(df):
    # Grouping by region and loyalty_status, then counting the number of orders
    region_loyalty_count = df.groupby(['region', 'loyalty_status']).size().unstack(fill_value=0)
    
    print("\nOrder Count by Region and Loyalty Status:")
    print(region_loyalty_count)

    # Plotting Region vs Loyalty Status Count with values on top of bars
    region_loyalty_count.plot(kind='bar', stacked=False, figsize=(10, 6), cmap='Set2')

    # Adding the values on top of the bars
    for p in plt.gca().patches:
        height = p.get_height()
        if height > 0:
            plt.gca().annotate(f'{height:.0f}', 
                               (p.get_x() + p.get_width() / 2., p.get_height()), 
                               ha='center', va='center', 
                               fontsize=12, color='black', 
                               xytext=(0, 5), textcoords='offset points')
    
    plt.title('Order Count by Region and Loyalty Status')
    plt.xlabel('Region')
    plt.ylabel('Order Count')
    plt.xticks(rotation=45)
    plt.show()





# Call Plot functions from Initial Analysis.py file
plot_monthly_revenue(df)
plot_loyalty_status_vs_order_value(df)
plot_promotion_usage_vs_order_value(df)
plot_region_vs_order_value(df)
plot_satisfaction_score_vs_order_value(df)
plot_region_vs_order_count(df)
plot_region_vs_loyalty_status_count(df)
plot_education_vs_loyalty_status_count(df)
plot_loyalty_status_vs_order_count(df)
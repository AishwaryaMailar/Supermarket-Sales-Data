# -*- coding: utf-8 -*-
"""14. Supermarket Sales Data  Data science project final.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11fGM5TQEUuZyhXKEV19CYXS6ULUgngq-
"""

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
uploaded=files.upload()

df=pd.read_csv('/content/sales.csv')
df

df.head()

df.columns

df.info()

df['Order_Date'] = pd.to_datetime(df['Order_Date'], dayfirst=True)
df['Order_Date'].head()

df.describe()

# Create a new column for Profit
df['Profit'] = df['Price'] - df['Cost_Price'] ## Calculates profit for each product by subtracting Cost Price from Selling Price.
df['Profit']

Hi# 1. Distribution of Price
plt.figure(figsize=(8,5))
sns.histplot(df['Price'], bins=50, kde=True)
plt.title('Distribution of Product Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

"""## Observation from above output is :
 - Most products are very cheap (below ₹50).
 - Few expensive products exist, but they are rare.
 - Sales mostly come from low-cost items in high quantity.
 - Right-skewed distribution → More low-priced items, fewer high-priced ones.
"""

print(df['Branch'].unique())

#compares the number of sales across different supermarket branches.
# 2. Sales by Branch
plt.figure(figsize=(6,4))
sns.countplot(x='Branch', data=df, hue='Branch', palette="viridis")
plt.title("Sales Count by Branch")
plt.xlabel("Branch")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

"""## Observations from the above  Output
- Austin, Texas has the highest sales (close to 100,000 sales).
- San Francisco, California ranks second (around 60,000 sales).
- Buffalo, New York and Houston, Texas have moderate sales.
- Sparks, Nevada has the lowest sales, meaning it is the least active branch.
"""

print(df['Category'].unique())

## 3. Sales by Category
plt.figure(figsize=(10,6))
sns.barplot(x='Category', y='Price', hue='Category', data=df, estimator=np.sum, palette='coolwarm') ## coolwarm means blue to red
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)
plt.show()

"""## Observation from above output is
- Electronics & Home & Kitchen have the highest sales.
- Arts & Crafts, Luggage, and Boys' Fashion have the lowest sales.
- The color gradient helps identify trends visually.
"""

# 4. Profit by Category
plt.figure(figsize=(20,10))

# Recalculate the 'Profit' column within the DataFrame
df['Profit'] = df['Price'] - df['Cost_Price']

sns.barplot(x='Category', y='Profit', hue='Category', data=df, estimator=np.sum, palette='coolwarm',legend=True)
plt.xticks(rotation=45)
plt.title("Total Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")
plt.show()

"""## Analysis of the Output

- Electronics and Home & Kitchen categories have the highest total profit.

- Arts & Crafts, Luggage, and Boys' Fashion show lower profits.

"""

# 5. Payment Method Distribution
plt.figure(figsize=(6,4))
sns.countplot(x='Payment_Type', data=df, hue='Payment_Type', palette='pastel', legend=True)
plt.title("Payment Method Distribution")
plt.xlabel("Payment Method")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

"""##  Observations from above output is:
- Cash is the most used payment method.
- ATM cards are the second most popular.
- Mobile payments, gift cards, and checks are used very little.
- Most transactions are done in cash, showing a strong preference for it.
- The legend helps differentiate payment methods.
"""

# 6. Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df[['Price', 'Cost_Price', 'Profit']].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Feature Correlation Heatmap")
plt.show()

"""## Observations from the  above Output:
- Strong correlation (1.00) between Price and Cost_Price, meaning they move together.
- Profit has a high correlation (0.93) with Price, indicating higher prices lead to higher profit.
- Profit and Cost_Price have a slightly lower correlation (0.90) but are still strongly related.
- Conclusion: Price and Cost_Price are almost identical, and both strongly impact Profit

## df['Order_Date'].dt.to_period('M'):

##Converts the Order_Date column (which is in datetime format) into a monthly period (e.g., Jan 2021, Feb 2021, etc.).
## 'M' means it groups data by month instead of individual dates.
## .groupby(...)[‘Profit’].sum():

## Groups the data by month-year and calculates the total profit for each month.
## .plot(marker='o'):

## Plots the total profit over time as a line graph.
## The marker='o' adds circular markers on each data point for better visibility.
"""

# 7. Profit Over Time
plt.figure(figsize=(12,6))
# Convert 'Order_Date' to datetime if it's not already
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df.groupby(df['Order_Date'].dt.to_period('M'))['Profit'].sum().plot(marker='o')
plt.title("Total Profit Over Time")
plt.xlabel("Month-Year")
plt.ylabel("Total Profit")
plt.grid(True)
plt.show()

import pandas as pd
import plotly.express as px

# Sample data (replace with your actual DataFrame)
df['Order_Date'] = pd.to_datetime(df['Order_Date'])  # Ensure Order_Date is in datetime format

# Aggregate profit by month
df_monthly = df.groupby(df['Order_Date'].dt.to_period('M'))['Profit'].sum().reset_index()
df_monthly['Order_Date'] = df_monthly['Order_Date'].astype(str)  # Convert period to string for Plotly

# Create interactive line chart
fig = px.line(df_monthly, x='Order_Date', y='Profit', markers=True,
              title="Total Profit Over Time",
              labels={'Order_Date': 'Month-Year', 'Profit': 'Total Profit'})

fig.update_traces(hoverinfo="x+y", mode='lines+markers')  # Show values on hover

# Show figure
fig.show()

"""## Observations from the Output:
1. Profit Fluctuations:

   --Profit drops sharply in February.

     -- Highest profit is in July, followed by October.

2. Volatility:

  -- The profit trend is not stable, showing ups and downs across months.

  -- Some months (e.g., March, July, October) have higher spikes, possibly due to seasonal demand.

3. General Trend:

     -- No clear upward or downward trend—profit is fluctuating.

    -- Further analysis is needed to understand the reasons (e.g., sales, discounts, market conditions).

"""

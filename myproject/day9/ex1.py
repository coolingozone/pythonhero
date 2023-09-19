# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset into a Pandas DataFrame
data = pd.read_csv('retail_sales_data.csv')  # Replace 'retail_sales_data.csv' with your dataset file

# Check for missing values, duplicates, and data types
print(data.info())
print(data.isnull().sum())
print(data.duplicated().sum())
# Calculate summary statistics
summary_stats = data.describe()

# Visualize the distribution of sales and profit
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(data['Sales'], bins=20, color='skyblue')
plt.title('Sales Distribution')
plt.xlabel('Sales')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(data['Profit'], bins=20, color='lightgreen')
plt.title('Profit Distribution')
plt.xlabel('Profit')
plt.ylabel('Frequency')

plt.show()
# Explore the relationship between sales and profit using a scatter plot
plt.scatter(data['Sales'], data['Profit'], alpha=0.5)
plt.title('Sales vs. Profit')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.show()
# Convert the date column to datetime format (if it's not already)
data['Date'] = pd.to_datetime(data['Date'])

# Create a time series plot
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Sales'], label='Sales', color='blue')
plt.title('Monthly Sales Trend')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.legend()
plt.show()
# Identify the top customers based on total purchase amount
top_customers = data.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(10)

# Visualize the top customers
plt.figure(figsize=(10, 5))
top_customers.plot(kind='bar', color='purple')
plt.title('Top 10 Customers by Total Purchase Amount')
plt.xlabel('Customer Name')
plt.ylabel('Total Purchase Amount')
plt.xticks(rotation=45)
plt.show()
# Identify the best-selling products and product categories
best_selling_products = data.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

# Visualize the best-selling products
plt.figure(figsize=(10, 5))
best_selling_products.plot(kind='bar', color='orange')
plt.title('Top 10 Best-Selling Products')
plt.xlabel('Product Name')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()





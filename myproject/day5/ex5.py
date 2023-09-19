# Import Pandas library
import pandas as pd

# Load the data into a DataFrame
df = pd.read_csv('sales_data.csv')

# Display the first 5 rows
print(df.head())

# Calculate total revenue
total_revenue = df['Revenue'].sum()
print("Total Revenue:", total_revenue)

# Find the product with the highest revenue
highest_revenue_product = df[df['Revenue'] == df['Revenue'].max()]['Product'].values[0]
print("Product with Highest Revenue:", highest_revenue_product)

# Calculate average units sold per sale
average_units_sold = df['Units Sold'].mean()
print("Average Units Sold per Sale:", average_units_sold)

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('sale_data.csv')
high_units_sold = df[df['Units Sold'] > 80]
print("\nRows with Units Sold >80:")
print(high_units_sold)

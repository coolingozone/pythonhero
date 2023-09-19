
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('sale_data.csv')
selected_columns = df[['Date', 'Revenue']]
print("\nSelected Columns:")
print(selected_columns)

import pandas as pd
import pandas as pd
import random
from faker import Faker
import csv

# Initialize Faker for generating random product names
fake = Faker()

# Generate sample data
data = []
for _ in range(100):  # Generating data for 100 sales records, you can adjust this number
    date = fake.date_between(start_date='-1y', end_date='today')  # Random date within the last year
    product = fake.word()  # Random product name
    units_sold = random.randint(1, 100)  # Random units sold between 1 and 100
    revenue = round(random.uniform(10, 2000), 2)  # Random revenue between $10 and $2000
    data.append([date, product, units_sold, revenue])

# Create a Pandas DataFrame
df = pd.DataFrame(data, columns=['Date', 'Product', 'Units Sold', 'Revenue'])

# Save the DataFrame as a CSV file
df.to_csv('sale_data.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)

print("CSV file 'sale_data.csv' has been generated.")

import pandas as pd
import random
from faker import Faker

# Initialize Faker for generating fake data
fake = Faker()

# Create an empty DataFrame
data = pd.DataFrame(columns=['Date', 'Customer Name', 'Product Name', 'Sales', 'Profit', 'Region'])

# Generate random sales data for one year
start_date = '2022-01-01'
end_date = '2022-12-31'
date_range = pd.date_range(start_date, end_date)

for _ in range(1000):  # Generate data for 1000 transactions (you can adjust this number)
    date = random.choice(date_range)
    customer_name = fake.name()
    product_name = fake.word()
    sales = round(random.uniform(10, 500), 2)
    profit = round(random.uniform(1, 100), 2)
    region = fake.state()
    
    data = data.append({
        'Date': date,
        'Customer Name': customer_name,
        'Product Name': product_name,
        'Sales': sales,
        'Profit': profit,
        'Region': region
    }, ignore_index=True)

# Save the DataFrame to a CSV file
data.to_csv('retail_sales_data.csv', index=False)

print("Retail sales data saved to 'retail_sales_data.csv'")

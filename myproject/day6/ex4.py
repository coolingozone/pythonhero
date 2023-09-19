import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales_revenue = [15000, 18000, 20000, 22000, 25000, 28000, 30000, 31000, 29000, 27000, 24000, 22000]

plt.bar(months, sales_revenue)
plt.title('Monthly Sales Revenue in 2021')
plt.xlabel('Month')
plt.ylabel('Sales Revenue ($)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

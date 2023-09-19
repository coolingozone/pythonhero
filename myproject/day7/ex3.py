import matplotlib.pyplot as plt
import seaborn as sns

data = [25, 28, 30, 32, 35, 38, 40, 45, 50, 55]

# Create a histogram
plt.hist(data, bins=5, color='skyblue')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

# Create a box plot
sns.boxplot(data=data, color='salmon')
plt.xlabel('Data')
plt.title('Box Plot')
plt.show()

import matplotlib.pyplot as plt

years = [2018, 2019, 2020, 2021, 2022]
population = [50000, 52000, 55000, 60000, 65000]

plt.plot(years, population, marker='o', linestyle='-')
plt.title('Population Growth Over Time')
plt.xlabel('Year')
plt.ylabel('Population')
plt.grid(True)
plt.show()

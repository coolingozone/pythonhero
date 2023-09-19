import numpy as np

data = np.array([25, 28, 30, 32, 35, 38, 40, 45, 50, 55])

mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)

print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)

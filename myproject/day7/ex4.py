import numpy as np
import matplotlib.pyplot as plt

# Generate random samples from a normal distribution
mu, sigma = 0, 1  # Mean and standard deviation
samples = np.random.normal(mu, sigma, 1000)

# Create a histogram to visualize the distribution
plt.hist(samples, bins=30, density=True, alpha=0.5)
plt.xlabel('Value')
plt.ylabel('Probability')
plt.title('Normal Distribution')
plt.show()

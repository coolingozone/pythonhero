import matplotlib.pyplot as plt
import numpy as np

hours_studied = [2, 3, 5, 1, 4, 6, 2, 5, 7, 8]
test_scores = [65, 70, 80, 55, 75, 90, 60, 85, 95, 100]

# Map color to test scores
colors = np.array(test_scores)

plt.scatter(hours_studied, test_scores, c=colors, cmap='viridis')
plt.title('Relationship between Hours Studied and Test Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Test Scores')
plt.colorbar(label='Test Scores')
plt.grid(True)
plt.show()

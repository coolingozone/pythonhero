# Import necessary libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the California Housing Prices dataset
data = fetch_california_housing(as_frame=True)
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Price'] = data.target

# Split the dataset into features (X) and the target variable (y)
X = df.drop('Price', axis=1)
y = df['Price']

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Linear Regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the evaluation metrics
print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Example: Estimate the price of a house with the following features
new_house_features = pd.DataFrame({'MedInc': [4.0], 'HouseAge': [35.0], 'AveRooms': [5.0], 'AveBedrms': [1.0], 'Population': [800], 'AveOccup': [3.0], 'Latitude': [34.1], 'Longitude': [-118.2]})
predicted_price = model.predict(new_house_features)
print("Estimated Price for New House:", predicted_price[0])

# Scatter plot for actual vs. predicted prices
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual Prices vs. Predicted Prices")
plt.grid(True)
plt.show()



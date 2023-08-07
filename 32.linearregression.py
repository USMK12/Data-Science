import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
data = pd.read_csv('house_data.csv')

# Explore the dataset and understand its structure
print(data.head())  # Display the first few rows of the dataset

# Bivariate analysis - Plotting the relationship between house size and price
plt.scatter(data['HouseSize'], data['Price'])
plt.xlabel('House Size')
plt.ylabel('Price')
plt.title('House Size vs. Price')
plt.show()

# Select the feature and target variable for the model
selected_feature = 'HouseSize'
X = data[[selected_feature]]
y = data['Price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error (MSE): {mse}')
print(f'R-squared (R2): {r2}')

# Visualize the linear regression line on the scatter plot
plt.scatter(data['HouseSize'], data['Price'])
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.xlabel('House Size')
plt.ylabel('Price')
plt.title('House Size vs. Price with Linear Regression')
plt.show()

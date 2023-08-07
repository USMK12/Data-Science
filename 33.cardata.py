import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
data = pd.read_csv('car_data.csv')

# Explore the dataset and understand its structure
print(data.head())  # Display the first few rows of the dataset

# Select the features and the target variable for the model
selected_features = ['EngineSize', 'Horsepower', 'FuelEfficiency']  # You can choose other relevant features
X = data[selected_features]
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

# Get the coefficients of the model to understand the influence of each feature on car prices
coefficients = dict(zip(selected_features, model.coef_))
print("Coefficients:")
for feature, coefficient in coefficients.items():
    print(f"{feature}: {coefficient}")

# Visualize the predicted prices vs. actual prices on a scatter plot
plt.scatter(y_test, y_pred)
plt.plot(y_test, y_test, color='red', linestyle='--')
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual Prices vs. Predicted Prices')
plt.show()

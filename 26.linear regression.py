import numpy as np
from sklearn.linear_model import LinearRegression

def get_input_features():
    # Get input features from the user
    area = float(input("Enter the area of the house (in square feet): "))
    num_bedrooms = int(input("Enter the number of bedrooms: "))
    # Add other features as needed

    return np.array([area, num_bedrooms]).reshape(1, -1)

def main():
    # Sample labeled dataset (replace this with your actual dataset)
    data = np.array([[1000, 2, 300000],
                     [1500, 3, 450000],
                     [1200, 2, 350000],
                     [1800, 4, 500000]])

    X = data[:, :-1]  # Features (area and number of bedrooms)
    y = data[:, -1]   # Prices

    # Create linear regression model
    model = LinearRegression()

    # Fit the model on the data
    model.fit(X, y)

    # Get input features for the new house
    new_house_features = get_input_features()

    # Predict the price for the new house
    predicted_price = model.predict(new_house_features)

    print(f"Predicted price for the new house: ${predicted_price[0]:.2f}")

if __name__ == "__main__":
    main()
';

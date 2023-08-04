import numpy as np
from sklearn.linear_model import LogisticRegression

def get_input_features():
    # Get input features from the user
    usage_minutes = float(input("Enter the usage minutes: "))
    contract_duration = float(input("Enter the contract duration (in months): "))
    # Add other features as needed

    return np.array([usage_minutes, contract_duration]).reshape(1, -1)

def main():
    # Sample labeled dataset (replace this with your actual dataset)
    data = np.array([[500, 12, 0],
                     [300, 6, 1],
                     [800, 24, 0],
                     [400, 18, 1]])

    X = data[:, :-1]  # Features (usage minutes and contract duration)
    y = data[:, -1]   # Churn status (0 for not churned, 1 for churned)

    # Create logistic regression model
    model = LogisticRegression()

    # Fit the model on the data
    model.fit(X, y)

    # Get input features for the new customer
    new_customer_features = get_input_features()

    # Predict whether the new customer will churn or not
    predicted_churn_status = model.predict(new_customer_features)

    if predicted_churn_status[0] == 1:
        print("The new customer is predicted to churn.")
    else:
        print("The new customer is predicted not to churn.")

if __name__ == "__main__":
    main()

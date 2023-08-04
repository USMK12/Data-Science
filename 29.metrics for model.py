import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression  # Replace this with your trained model

def load_dataset():
    # Sample dataset (replace this with your actual dataset)
    data = np.array([[1, 0, 1],
                     [0, 1, 0],
                     [1, 1, 1],
                     [0, 0, 0],
                     [1, 0, 0]])

    X = data[:, :-1]  # Features
    y = data[:, -1]   # Target variable

    return X, y

def get_input_features():
    # Get input features from the user
    num_features = int(input("Enter the number of features: "))
    features = []
    for i in range(num_features):
        feature = input(f"Enter feature name {i + 1}: ")
        features.append(feature)
    return features

def get_target_variable():
    # Get the target variable from the user
    target_variable = input("Enter the target variable name: ")
    return target_variable

def evaluate_model(y_true, y_pred):
    # Calculate evaluation metrics
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)

    return accuracy, precision, recall, f1

def main():
    # Load dataset
    X, y = load_dataset()

    # Get input features and target variable from the user
    input_features = get_input_features()
    target_variable = get_target_variable()

    # Use the specified features for evaluation
    feature_indices = [input_features.index(feature) for feature in input_features]
    X_eval = X[:, feature_indices]

    # Split the dataset into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X_eval, y, test_size=0.2, random_state=42)

    # Sample model (replace this with your trained model)
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model's performance
    accuracy, precision, recall, f1 = evaluate_model(y_test, y_pred)

    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1-score: {f1:.2f}")

if __name__ == "__main__":
    main()

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# Sample data (replace this with your actual dataset)
# Assuming your dataset has features (X) and labels (y)
X = np.array([[1, 2], [2, 3], [3, 4], [5, 1], [6, 2], [7, 3]])
y = np.array([0, 0, 0, 1, 1, 1])

def main():
    # Get input features from the user
    feature1 = float(input("Enter feature 1: "))
    feature2 = float(input("Enter feature 2: "))

    # Combine features into a single array
    new_patient_features = np.array([[feature1, feature2]])

    # Get the value of k from the user
    k = int(input("Enter the value of k: "))

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Standardize the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    new_patient_features = scaler.transform(new_patient_features)

    # Create a KNN classifier and fit it to the training data
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)

    # Predict whether the patient has the medical condition or not
    prediction = knn.predict(new_patient_features)

    # Convert the prediction to human-readable format
    result = "positive" if prediction[0] == 1 else "negative"

    print(f"The prediction for the new patient is: {result}")

if __name__ == "__main__":
    main()

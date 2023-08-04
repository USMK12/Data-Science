import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def load_dataset():
    iris = load_iris()
    X, y = iris.data, iris.target
    return X, y

def main():
    # Load the Iris dataset
    X, y = load_dataset()

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the Decision Tree classifier
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    # Get user inputs for sepal and petal dimensions
    sepal_length = float(input("Enter sepal length: "))
    sepal_width = float(input("Enter sepal width: "))
    petal_length = float(input("Enter petal length: "))
    petal_width = float(input("Enter petal width: "))

    # Create an array with the user inputs
    new_flower = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Make predictions for the new flower
    predicted_species = clf.predict(new_flower)

    # Map the integer predictions back to species names
    iris_species = ['setosa', 'versicolor', 'virginica']
    predicted_species_name = iris_species[predicted_species[0]]

    print(f"The predicted species for the new flower is: {predicted_species_name}")

if __name__ == "__main__":
    main()



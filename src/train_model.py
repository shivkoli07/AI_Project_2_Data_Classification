from sklearn.neighbors import KNeighborsClassifier
import joblib
import os


def train_model(X_train, y_train):
    """
    Train the KNN classification model.
    """

    # Create KNN model
    model = KNeighborsClassifier(n_neighbors=3)

    # Train model
    model.fit(X_train, y_train)

    print("\n===== Model Training Completed =====")
    print("KNN Model trained successfully!")

    # Create models folder if it doesn't exist
    os.makedirs("models", exist_ok=True)

    # Save trained model
    joblib.dump(model, "models/knn_model.pkl")

    print("Model saved as models/knn_model.pkl")

    return model
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
import matplotlib.pyplot as plt
import os


def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model.
    """

    # Predict test data
    y_pred = model.predict(X_test)

    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average="weighted")

    print("\n===== Model Evaluation =====")
    print(f"Accuracy : {accuracy:.2f}")
    print(f"F1 Score : {f1:.2f}")

    # Create outputs folder if it doesn't exist
    os.makedirs("outputs", exist_ok=True)

    # Save Accuracy Report
    with open("outputs/accuracy_report.txt", "w") as file:
        file.write("Model Evaluation Report\n")
        file.write("=========================\n")
        file.write(f"Accuracy : {accuracy:.2f}\n")
        file.write(f"F1 Score : {f1:.2f}\n")

    # Plot Confusion Matrix
    plt.figure(figsize=(6,5))
    plt.imshow(conf_matrix, cmap="Blues")
    plt.title("Confusion Matrix")
    plt.colorbar()

    classes = ["Setosa", "Versicolor", "Virginica"]

    plt.xticks(range(len(classes)), classes, rotation=45)
    plt.yticks(range(len(classes)), classes)

    # Add numbers inside matrix
    for i in range(len(classes)):
        for j in range(len(classes)):
            plt.text(j, i, conf_matrix[i, j],
                     ha="center",
                     va="center",
                     color="black")

    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    plt.tight_layout()

    plt.savefig("outputs/confusion_matrix.png")
    plt.close()

    print("Confusion Matrix saved successfully!")

    return y_pred
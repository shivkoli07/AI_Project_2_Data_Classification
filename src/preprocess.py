from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def preprocess_data(df):
    """
    Preprocess the dataset:
    1. Separate features and target
    2. Split into training and testing sets
    3. Scale the features
    """

    # Features (Input)
    X = df.drop("species", axis=1)

    # Target (Output)
    y = df["species"]

    # Split dataset (80% Train, 20% Test)
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Feature Scaling
    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    print("\n===== Data Preprocessing Completed =====")
    print(f"Training Samples : {len(X_train)}")
    print(f"Testing Samples  : {len(X_test)}")

    return X_train, X_test, y_train, y_test, scaler
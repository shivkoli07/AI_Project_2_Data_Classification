from src.load_data import load_dataset
from src.preprocess import preprocess_data
from src.train_model import train_model
from src.evaluate_model import evaluate_model
from src.predict import predict_species

# Dataset path
dataset_path = "dataset/iris.csv"

# Load dataset
df = load_dataset(dataset_path)

# Preprocess dataset
X_train, X_test, y_train, y_test, scaler = preprocess_data(df)

# Train model
model = train_model(X_train, y_train)

# Evaluate model
y_pred = evaluate_model(model, X_test, y_test)

# Predict new flower
predict_species(model, scaler)
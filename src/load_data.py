import pandas as pd


def load_dataset(file_path):
    """
    Load the dataset from a CSV file.
    """
    df = pd.read_csv(file_path)

    print("\n===== Dataset Loaded Successfully =====\n")
    print("First 5 Rows:")
    print(df.head())

    print("\nDataset Information:")
    print(df.info())

    print("\nDataset Shape:", df.shape)

    print("\nColumn Names:")
    print(df.columns.tolist())

    return df
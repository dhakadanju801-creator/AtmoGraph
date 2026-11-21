import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "supply_chain_disruption_recovery.csv"


def load_data():

    df = pd.read_csv(DATA_PATH)

    print("AtmoGraph Dataset Loaded Successfully!")

    print("\nDataset Shape:")
    print(df.shape)

    print("\nDataset Columns:")
    print(df.columns.tolist())

    print("\nFirst Five Records:")
    print(df.head())

    return df


if __name__ == "__main__":
    df = load_data()
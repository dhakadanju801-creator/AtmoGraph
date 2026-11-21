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

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nStatistical Analysis:")
    print(df.describe())

    print("\nDisruption Types:")
    print(df["disruption_type"].value_counts())

    print("\nIndustry Distribution:")
    print(df["industry"].value_counts())

    print("\nAverage Recovery Days:")
    print(df["full_recovery_days"].mean())

    return df


if __name__ == "__main__":

    df = load_data()
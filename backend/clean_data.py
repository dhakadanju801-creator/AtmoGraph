import pandas as pd
from pathlib import Path

# Load Dataset
BASE_DIR = Path(__file__).resolve().parents[1]

DATA_PATH = BASE_DIR / "data" / "supply_chain_disruption_recovery.csv"

df = pd.read_csv(DATA_PATH)

print("Dataset Loaded:", df.shape)

# 1. Remove extra spaces
categorical_cols = [
    "disruption_type",
    "industry",
    "supplier_region",
    "supplier_size",
    "response_type"
]

for col in categorical_cols:
    df[col] = df[col].str.strip()

print("\n1. Categorical Cleaning Completed")

# 2. Check negative values
numerical_cols = df.select_dtypes(include="number").columns

print("\n2. Negative Values Check")

for col in numerical_cols:
    print(col, ":", (df[col] < 0).sum())

# 3. Production Impact Validation
invalid_impact = (
    (df["production_impact_pct"] < 0) |
    (df["production_impact_pct"] > 100)
)

print("\n3. Invalid Production Impact:", invalid_impact.sum())

# 4. Recovery Timeline Validation
invalid_recovery = (
    df["partial_recovery_days"] >
    df["full_recovery_days"]
)

print("\n4. Invalid Recovery Records:", invalid_recovery.sum())

# 5. Check final data
print("\n5. Final Dataset Shape:", df.shape)

print("\nDATA VALIDATION COMPLETED!")
# 6. Save Cleaned Dataset

OUTPUT_DIR = BASE_DIR / "data" / "processed"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_PATH = OUTPUT_DIR / "cleaned_supply_chain.csv"

df.to_csv(OUTPUT_PATH, index=False)

print("\nCleaned Dataset Saved Successfully!")
print("File Location:", OUTPUT_PATH)
print("Final Shape:", df.shape)
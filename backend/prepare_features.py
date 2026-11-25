import pandas as pd

# Load dataset
df = pd.read_csv("data/processed/cleaned_supply_chain.csv")

# Select input features
features = [
    'disruption_type',
    'industry',
    'supplier_tier',
    'supplier_region',
    'supplier_size',
    'has_backup_supplier',
    'disruption_severity',
    'production_impact_pct',
    'revenue_loss_usd',
    'response_type',
    'response_time_days'
]

# Input and target
X = df[features]
y = df['full_recovery_days']

print("Feature preparation successful!")
print("Features shape:", X.shape)
print("Target shape:", y.shape)

print("\nFeature preview:")
print(X.head())

print("\nTarget preview:")
print(y.head())
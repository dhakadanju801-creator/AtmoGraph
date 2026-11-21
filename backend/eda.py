import pandas as pd
import matplotlib

# No separate window
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# 1. Project Path
BASE_DIR = Path(__file__).resolve().parents[1]

DATA_PATH = BASE_DIR / "data" / "processed" / "cleaned_supply_chain.csv"

# Save graphs in outputs folder
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# 2. Load Dataset
df = pd.read_csv(DATA_PATH)

print("\nEDA Started Successfully!")
print("Dataset Shape:", df.shape)

sns.set_theme(style="whitegrid")


# 3. Function for Count Graphs
def create_countplot(column, title, filename):

    plt.figure(figsize=(10, 6))

    order = df[column].value_counts().index

    sns.countplot(
        data=df,
        x=column,
        order=order,
        hue=column,
        palette="viridis",
        legend=False
    )

    plt.title(title, fontsize=16, fontweight="bold")
    plt.xlabel(column.replace("_", " ").title())
    plt.ylabel("Number of Disruptions")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(OUTPUT_DIR / filename, dpi=300)
    plt.close()

    print(title, "Graph Generated!")


# 4. Disruption Type Analysis
create_countplot(
    "disruption_type",
    "Supply Chain Disruption Types",
    "disruption_types.png"
)


# 5. Industry Analysis
create_countplot(
    "industry",
    "Industry-wise Disruptions",
    "industry_analysis.png"
)


# 6. Supplier Region Analysis
create_countplot(
    "supplier_region",
    "Region-wise Supplier Disruptions",
    "supplier_region.png"
)


# 7. Supplier Size Analysis
create_countplot(
    "supplier_size",
    "Supplier Size Analysis",
    "supplier_size.png"
)


# 8. Response Type Analysis
create_countplot(
    "response_type",
    "Supply Chain Response Analysis",
    "response_analysis.png"
)


# 9. Revenue Loss Distribution
plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x="revenue_loss_usd",
    bins=30,
    kde=True,
    color="teal"
)

plt.title("Revenue Loss Distribution", fontsize=16)
plt.xlabel("Revenue Loss (USD)")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "revenue_loss.png", dpi=300)
plt.close()

print("Revenue Loss Graph Generated!")


# 10. Recovery Time Analysis
plt.figure(figsize=(10, 6))

recovery_data = df[
    [
        "response_time_days",
        "partial_recovery_days",
        "full_recovery_days"
    ]
]

sns.boxplot(data=recovery_data, palette="Set2")

plt.title("Supply Chain Recovery Time Analysis", fontsize=16)
plt.ylabel("Recovery Time (Days)")

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "recovery_time.png", dpi=300)
plt.close()

print("Recovery Time Graph Generated!")


# 11. Correlation Heatmap
plt.figure(figsize=(12, 8))

numeric_df = df.select_dtypes(include="number")

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Feature Correlation Heatmap", fontsize=16)

plt.tight_layout()
plt.savefig(OUTPUT_DIR / "correlation_heatmap.png", dpi=300)
plt.close()

print("Correlation Heatmap Generated!")


# 12. Final Result
print("\nAll EDA Graphs Generated Successfully!")
print("Graph Location:", OUTPUT_DIR)
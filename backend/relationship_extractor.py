import pandas as pd

# Load extracted entities
df = pd.read_csv("data/processed/news_entities.csv")

# Separate organizations and locations
organizations = df[df["Type"] == "ORG"]["Entity"].tolist()
locations = df[df["Type"] == "GPE"]["Entity"].tolist()

# Create relationships
relationships = []

for org in organizations:
    for location in locations:
        relationships.append({
            "Source": org,
            "Relationship": "ASSOCIATED_WITH",
            "Target": location
        })

# Save relationships
result = pd.DataFrame(relationships)

result.to_csv(
    "data/processed/news_relationships.csv",
    index=False
)

print("Relationship extraction completed!")
print(result)
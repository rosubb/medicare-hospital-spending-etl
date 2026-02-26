import pandas as pd
from pathlib import Path

raw_path = Path("data/raw/rows.csv")
sample_path = Path("data/sample/rows_sample.csv")

# Create sample folder if not exists
sample_path.parent.mkdir(parents=True, exist_ok=True)

# Read raw data
df = pd.read_csv(raw_path)

# Save first 200 rows as sample
df.head(200).to_csv(sample_path, index=False)

print("Sample created successfully.")

import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/sample/rows_sample.csv")
OUT_PATH = Path("data/processed/cleaned_data.csv")

def extract(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()
    df = df.fillna(0)
    return df

def load(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)

def main():
    print("Running ETL...")
    df = extract(RAW_PATH)
    df_clean = transform(df)
    load(df_clean, OUT_PATH)
    print(f"Saved to {OUT_PATH}")

if __name__ == "__main__":
    main()
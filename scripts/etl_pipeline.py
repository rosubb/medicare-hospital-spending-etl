import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/sample/rows_sample.csv")
OUT_PATH = Path("data/processed/cleaned_data.csv")

def extract(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)

def transform(df: pd.DataFrame) -> pd.DataFrame:
    # standardize column names
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # drop exact duplicates
    df = df.drop_duplicates()

    # remove rows that are completely empty
    df = df.dropna(how="all")

    # try converting numeric-looking columns
    for col in df.columns:
        if df[col].dtype == "object":
            # attempt numeric conversion where possible
            df[col] = pd.to_numeric(df[col], errors="ignore")

    # fill missing values (simple rule: numeric -> 0, text -> "Unknown")
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(0)
        else:
            df[col] = df[col].fillna("Unknown")

    # example derived metric (only if columns exist)
    if "total_payments" in df.columns and "discharges" in df.columns:
        denom = df["discharges"].replace(0, pd.NA)
        df["cost_per_discharge"] = df["total_payments"] / denom

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
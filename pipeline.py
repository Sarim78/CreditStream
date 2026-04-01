import pandas as pd
from sqlalchemy import create_engine
import os

# Setting Up the Environment
Input_FILE = "data/loan_portfolio.csv"
output_DIR = "output"
Database_Name = "creditstream.db"
Table_Name = "loans"

# This function will extract data from the specified file path and return a DataFrame
def extract_data(filepath):
    print(f"[EXTRACT] Reading data from {filepath}...")
    df = pd.read_csv(filepath)
    print(f"[EXTRACT] Loaded {len(df):,} rows and {len(df.columns)} columns.")
    
    return df 

# This function will perform data cleaning and transformation to prepare the data for analysis or loading into a database
def transform_data(df):
    print("[TRANSFORM] Starting transformation...")

    df = df.drop_duplicates()

    critical_cols = ["loan_id", "credit_score", "ead", "defaulted"]
    df = df.dropna(subset=critical_cols)

    df["origination_date"] = pd.to_datetime(df["origination_date"], errors="coerce")
    df["maturity_date"]    = pd.to_datetime(df["maturity_date"], errors="coerce")

    numeric_cols = df.select_dtypes(include="number").columns
    df[numeric_cols] = df[numeric_cols].fillna(0)

    str_cols = df.select_dtypes(include="object").columns
    df[str_cols] = df[str_cols].apply(lambda col: col.str.strip())

    def assign_risk(score):
        if score >= 750:
            return "Low"
        elif score >= 650:
            return "Medium"
        else:
            return "High"
        
    df["risk_tier"] = df["credit_score"].apply(assign_risk)
    df["el_ratio"] = (df["el"] / df["ead"].replace(0, pd.NA)).fillna(0).round(4)

    df["is_defaulted"] = df["defaulted"].astype(int)
 
    print(f"[TRANSFORM] Done. {len(df):,} clean rows ready to load.")

    return df

# This function will load the transformed DataFrame into a SQLite database, creating the database file if it doesn't exist and replacing the table if it does
def load_data(df, output_dir, database_name, table_name):
    print("[LOAD] Loading data into SQLite...")
 
    os.makedirs(output_dir, exist_ok=True)
 
    db_path = os.path.join(output_dir, database_name)
    engine  = create_engine(f"sqlite:///{db_path}")
 
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)
 
    print(f"[LOAD] {len(df):,} rows loaded into '{table_name}' table.")
    print(f"[LOAD] Database saved at: {db_path}")

# this function will print a summary of the processed data, including key statistics and breakdowns by risk tier and sector
def summarize_data(df):
    print("\n── PIPELINE SUMMARY ──────────────────────────")
    print(f"  Total loans      : {len(df):,}")
    print(f"  Default rate     : {df['is_defaulted'].mean() * 100:.1f}%")
    print(f"  Avg credit score : {df['credit_score'].mean():.0f}")
    print(f"  Avg EL ratio     : {df['el_ratio'].mean():.4f}")
    print(f"  Risk breakdown   :")
    print(df["risk_tier"].value_counts().to_string())
    print(f"\nSector breakdown:")
    print(df["sector"].value_counts().to_string())
    print("──────────────────────────────────────────────\n")

# Run The Pipeline
def main():
    raw_df = extract_data(Input_FILE)
    clean_df = transform_data(raw_df)
    load_data(clean_df, output_DIR, Database_Name, Table_Name)
    summarize_data(clean_df)

    print("[DONE] CreditStream pipeline completed successfully.")

if __name__ == "__main__":
    main()
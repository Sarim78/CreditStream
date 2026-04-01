import pandas as pd
from sqlalchemy import create_engine
import os

# Setting Up the Environment
Input_FILE = "data/loan_data.csv"
output_DIR = "output"
Database_Name = "creditstream.db"
Table_Name = "loans"

# This function will extract data from the specified file path and return a DataFrame
def extract_data(filepath):
    print(f"[EXTRACT] Reading data from {filepath}...")
    df = pd.read_csv(filepath)
    print(f"[EXTRACT] Loaded {len(df):,} rows and {len(df.columns)} columns.")
    
    return df 

def transform(df):
    pass

def load(df, output_dir, database_name, table_name):
    pass

def summary(df):
    pass

# Run The Pipeline
def main():
    pass

if __name__ == "__main__":
    main()
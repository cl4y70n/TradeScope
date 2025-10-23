import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / 'data'

def load_sales_csv(path: str = None) -> pd.DataFrame:
    path = path or DATA_DIR / 'vendas_exemplo.csv'
    df = pd.read_csv(path, parse_dates=['date'])
    # normalization
    df['product'] = df['product'].astype(str)
    df['category'] = df['category'].astype(str)
    df['region'] = df['region'].astype(str)
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce').fillna(0).astype(int)
    df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce').fillna(0.0)
    df['total_price'] = df['quantity'] * df['unit_price']
    return df

# ==========================================
# AI-POWERED FX RISK INTELLIGENCE PLATFORM
# Week 1 - Session 1
# Historical FX Data Collection
# ==========================================

import pandas as pd
import yfinance as yf
from pathlib import Path

# STEP 1: Define project directory 

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
RAW_DATA_DIR.mkdir(parents = True, exist_ok = True)

# STEP 2: Define currency pairs 

currency_pairs = {"GBP_USD": "GBPUSB=X", "EUR_USD": "EURUSD=X", "USD_JPY":"JPY=X"}

# STEP 3: Download historical FX data

for pair, ticker in currency_pairs.items():
    print(f"\nDownloading {pair}...")
    data = yf.download(ticker, period = "5y", interval = "1d", auto_adjust = False, progress = False)

# STEP 4: Check whether data was returned

    if data.empty:
        print(f"No data found for {pair}.")
        continue

# Handle Yahoo Finance MultiIndex Columns

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

 # STEP 5: Save dowloaded data

    df = data.reset_index()

    output_file = RAW_DATA_DIR / f"{pair}_raw.csv"

    df.to_csv(output_file, index = False)

# STEP 6: Display downloaded information

    print(f"Saved successfully: {output_file.name}")
    print(f"Observations: {len(df)}")
    print(f"First date: {df['Date'].min()}")
    print(f"Last date: {df['Date'].max()}")

print("\nAll currency pairs downloaded successfully.")



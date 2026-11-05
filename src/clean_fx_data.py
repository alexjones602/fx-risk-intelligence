# ==========================================
# AI-POWERED FX RISK INTELLIGENCE PLATFORM
# Week 1 - Session 2
# Data Cleaning and Preparation
# ==========================================

import pandas as pd 
import numpy as np 
from pathlib import Path

# STEP 1: Loading datasets into Pandas

# Main project directory
PROJECT_ROOT = Path(__file__).resolve().parents[1]
# Data directories 
RAW_DATA = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA = PROJECT_ROOT / "data" / "processed"
# Processed folder
PROCESSED_DATA.mkdir(parents=True, exist_ok=True)

# Loading FX datasets
gbp_usd = pd.read_csv(RAW_DATA / "GBP_USD_raw.csv")
eur_usd = pd.read_csv(RAW_DATA / "EUR_USD_raw.csv")
usd_jpy = pd.read_csv(RAW_DATA / "USD_JPY_raw.csv")

# Fix GBP/USD Yahoo Finance export format
gbp_usd = gbp_usd.iloc[2:].copy()
gbp_usd = gbp_usd.rename(columns={"Price": "Date"})

# STEP 2: Inspecting and understanding the datasets

# Examining columns and data types
print(gbp_usd.columns)
print(eur_usd.columns)
print(usd_jpy.columns)

print("\nGBP/USD DATA TYPES")
print(gbp_usd.dtypes)
print("\nEUR/USD DATA TYPES")
print(eur_usd.dtypes)
print("\nUSD/JPY DATA TYPES")
print(usd_jpy.dtypes)

# STEP 3: Standardising data types across datasets

# Converting dates to datetime format

for df in [gbp_usd, eur_usd, usd_jpy]:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Define numerical price columns

price_columns = ["Open", "High", "Low", "Close", "Volume"]

# Converting price columns to numeric format

for df in[gbp_usd, eur_usd, usd_jpy]:
    for column in price_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

# Display updated data types

print("\nGBP/USD DATA TYPES")
print(gbp_usd.dtypes)
print("\nEUR/USD DATA TYPES")
print(eur_usd.dtypes)
print("\nUSD/JPY DATA TYPES")
print(usd_jpy.dtypes)

# STEP 4: Investigating data quality

# Checking for missing values

datasets = {"GBP/USD": gbp_usd, "EUR/USD": eur_usd, "USD/JPY": usd_jpy}

for name, df in datasets.items():
    print(f"\n{name}")
    print(df.isnull().sum())
    print("Total missing values:", df.isnull().sum().sum())

# Checking for duplicates

for name, df in datasets.items():
    duplicate_count = df["Date"].duplicated().sum()
    print(f"\n{name}")
    print("Duplicate dates:", duplicate_count)

# Checking for invalid prices

for name, df in datasets.items():
    print(f"\n{name}")
    for column in ["Open", "High", "Low", "Close"]:
        invalid = (df[column] <= 0).sum()
        print(f"{column} Invalid values:", {invalid})

# OHLC validation

for name, df in datasets.items():

    invalid_ohlc = (
        (df["High"] < df["Low"]) |
        (df["High"] < df["Open"]) |
        (df["High"] < df["Close"]) |
        (df["Low"] > df["Open"]) |
        (df["Low"] > df["Close"])
    )

    print(name, "Invalid OHLC observations:", invalid_ohlc.sum())

# Investigating OHLC validation failures

for name, df in datasets.items():

    # Identify individual validation failures

    high_below_low = df["High"] < df["Low"]

    high_below_open = df["High"] < df["Open"]

    high_below_close = df["High"] < df["Close"]

    low_above_open = df["Low"] > df["Open"]

    low_above_close = df["Low"] > df["Close"]

    # Combine all validation failures

    invalid_ohlc = (
        high_below_low |
        high_below_open |
        high_below_close |
        low_above_open |
        low_above_close
    )

    print(f"\n{name}")

    print("High below Low:", high_below_low.sum())

    print("High below Open:", high_below_open.sum())

    print("High below Close:", high_below_close.sum())

    print("Low above Open:", low_above_open.sum())

    print("Low above Close:", low_above_close.sum())

    print("\nFirst 10 invalid observations:")

    print(
        df.loc[
            invalid_ohlc,
            ["Date", "Open", "High", "Low", "Close"]
        ].head(10).to_string(index=False)
    )

# Quantify OHLC inconsistencies

for name, df in datasets.items():

    invalid = (
        (df["High"] < df["Open"]) |
        (df["High"] < df["Close"]) |
        (df["Low"] > df["Open"]) |
        (df["Low"] > df["Close"]) |
        (df["High"] < df["Low"])
    )

    print(f"\n{name}")
    print("Total observations:", len(df))
    print("Invalid observations:", invalid.sum())
    print("Percentage invalid:", round(invalid.mean() * 100, 2), "%")

    print("\nFirst 20 flagged observations:")

    print(
        df.loc[
            invalid,
            ["Date", "Open", "High", "Low", "Close"]
        ].head(20).to_string(index=False)
    )

# Measure OHLC discrepancies across all three currency pairs

for name, df in datasets.items():

    print(f"\n{'='*50}")
    print(f"INVESTIGATING {name}")
    print(f"{'='*50}")

    invalid = (
        (df["High"] < df["Open"]) |
        (df["High"] < df["Close"]) |
        (df["Low"] > df["Open"]) |
        (df["Low"] > df["Close"]) |
        (df["High"] < df["Low"])
    )

    flagged = df.loc[invalid].copy()

    print("Invalid observations:", len(flagged))

    print("\nLargest High discrepancies:")

    flagged["High_Breach"] = (
        flagged[["Open", "Close"]].max(axis=1)
        - flagged["High"]
    ).clip(lower=0)

    print(
        flagged.nlargest(5, "High_Breach")[
            ["Date", "Open", "High", "Low",
             "Close", "High_Breach"]
        ].to_string(index=False)
    )

    print("\nLargest Low discrepancies:")

    flagged["Low_Breach"] = (
        flagged["Low"]
        - flagged[["Open", "Close"]].min(axis=1)
    ).clip(lower=0)

    print(
        flagged.nlargest(5, "Low_Breach")[
            ["Date", "Open", "High", "Low",
             "Close", "Low_Breach"]
        ].to_string(index=False)
    )

#Investigate OHLC anomalies by year

for name, df in datasets.items():

    invalid = (
        (df["High"] < df["Open"]) |
        (df["High"] < df["Close"]) |
        (df["Low"] > df["Open"]) |
        (df["Low"] > df["Close"])
    )

    print(f"\n{name} ANOMALIES BY YEAR")

    print(
        df.loc[invalid]
        .groupby(df.loc[invalid, "Date"].dt.year)
        .size()
    )

# Categorise OHLC anomalies by severity

for name, df in datasets.items():

    high_breach = pd.concat([
        (df["Open"] - df["High"]).clip(lower=0),
        (df["Close"] - df["High"]).clip(lower=0)
    ], axis=1).max(axis=1)

    low_breach = pd.concat([
        (df["Low"] - df["Open"]).clip(lower=0),
        (df["Low"] - df["Close"]).clip(lower=0)
    ], axis=1).max(axis=1)

    max_breach = pd.concat(
        [high_breach, low_breach], axis=1
    ).max(axis=1)

    invalid = max_breach > 0

    print(f"\n{name} ANOMALY SEVERITY")

    print("Total anomalies:", invalid.sum())

    print("Maximum discrepancy:", max_breach.max())

    print("Average discrepancy:", max_breach[invalid].mean())

    print("\nSeverity distribution:")

    print(pd.cut(
        max_breach[invalid],
        bins=[0, 0.0001, 0.001, float("inf")],
        labels=["Minor", "Moderate", "Major"]
    ).value_counts())

# Inspecting original raw csv data

raw_files = {
    "GBP/USD": "GBP_USD_raw.csv",
    "EUR/USD": "EUR_USD_raw.csv",
    "USD/JPY": "USD_JPY_raw.csv"
}

dates_to_check = {
    "GBP/USD": "2022-06-17",
    "EUR/USD": "2022-12-26",
    "USD/JPY": "2022-08-29"
}

for name, filename in raw_files.items():

    file_path = RAW_DATA / filename

    print(f"\n========== {name} RAW DATA ==========")

    with open(file_path, "r", encoding="utf-8-sig") as file:

        lines = file.readlines()

    target_date = dates_to_check[name]

    for line in lines:

        if target_date in line:

            print(line.strip())

# Data quality flag 

for name, df in datasets.items():

    df["OHLC_Invalid"] = (
        (df["High"] < df["Open"]) |
        (df["High"] < df["Close"]) |
        (df["Low"] > df["Open"]) |
        (df["Low"] > df["Close"]) |
        (df["High"] < df["Low"])
    )

    print(f"\n{name}")
    print("Invalid OHLC records:", df["OHLC_Invalid"].sum())
    print("Valid OHLC records:", (~df["OHLC_Invalid"]).sum())

# Validating closing prices

for name, df in datasets.items():

    invalid_close = (
        df["Close"].isna() |
        (df["Close"] <= 0)
    )

    print(f"\n{name}")
    print("Missing closing prices:", df["Close"].isna().sum())
    print("Zero or negative closing prices:", 
          (df["Close"] <= 0).sum())
    print("Valid closing prices:", (~invalid_close).sum())

# Data coverage

for name, df in datasets.items():

    print(f"\n========== {name} ==========")

    print("First date:", df["Date"].min())
    print("Last date:", df["Date"].max())

    print("Number of observations:", len(df))

    print("Duplicate dates:", df["Date"].duplicated().sum())

    print("Dates in chronological order:",
          df["Date"].is_monotonic_increasing)

# STEP 5: Merging FX datasets

# Prepare datasets for merging

gbp_usd_clean = gbp_usd[
    ["Date", "Close", "OHLC_Invalid"]
].copy()

eur_usd_clean = eur_usd[
    ["Date", "Close", "OHLC_Invalid"]
].copy()

usd_jpy_clean = usd_jpy[
    ["Date", "Close", "OHLC_Invalid"]
].copy()

# Rename columns to identify each currency pair

gbp_usd_clean = gbp_usd_clean.rename(
    columns={
        "Close": "GBPUSD_Close",
        "OHLC_Invalid": "GBPUSD_OHLC_Invalid"
    }
)

eur_usd_clean = eur_usd_clean.rename(
    columns={
        "Close": "EURUSD_Close",
        "OHLC_Invalid": "EURUSD_OHLC_Invalid"
    }
)

usd_jpy_clean = usd_jpy_clean.rename(
    columns={
        "Close": "USDJPY_Close",
        "OHLC_Invalid": "USDJPY_OHLC_Invalid"
    }
)

# Merge the three currency-pair datasets

fx_data = gbp_usd_clean.merge(
    eur_usd_clean,
    on="Date",
    how="inner"
)

fx_data = fx_data.merge(
    usd_jpy_clean,
    on="Date",
    how="inner"
)

# Computing the merged dataset 

print("Shape:", fx_data.shape)

print("\nColumn names:")
print(fx_data.columns.tolist())

print("\nFirst 5 observations:")
print(fx_data.head())

print("\nLast 5 observations:")
print(fx_data.tail())

# STEP 6: Saving the merged dataset

OUTPUT_DIR = Path("data/processed")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

output_file = OUTPUT_DIR / "cleaned_fx_data.csv"

fx_data.to_csv(output_file, index=False)

print("\nFX dataset successfully saved to:", output_file)

# STEP 7: Verify saved dataset

verified_fx_data = pd.read_csv(
    output_file,
    parse_dates=["Date"]
)

print("\n========== SAVED DATASET VERIFICATION ==========")

print("Shape:", verified_fx_data.shape)

print("Missing values:")
print(verified_fx_data.isna().sum())

print("Duplicate dates:", verified_fx_data["Date"].duplicated().sum())

print("\nFirst 5 rows:")
print(verified_fx_data.head())
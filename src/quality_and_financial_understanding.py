# ==========================================
# AI-POWERED FX RISK INTELLIGENCE PLATFORM
# Week 1 - Session 3
# Data Quality and Financial Understanding
# ==========================================

# PART 1: Review of existing, processed dataset

from zipfile import Path
from pathlib import Path as FilePath

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load cleaned FX data
df = pd.read_csv("data/processed/cleaned_fx_data.csv")

# Covert date column to datetime format
df['Date'] = pd.to_datetime(df["Date"], format = "%Y-%m-%d")

# Set date column as index
df = df.set_index("Date")

# Display first five rows
df.head()

# Understanding structure
print(df.shape)
print(df.info())
print(df.describe())
print(df.dtypes)

# STEP 2: Data quality validation

# Missing observations check
df.isnull().sum()
missing_percentage = (df.isnull().sum() / len(df)) * 100
print(missing_percentage)

# Check for duplicates
print("Duplicated dates:", df.index.duplicated().sum())
df[df.index.duplicated(keep = False)]

# Check for positive exchange rates
price_columns = ["GBPUSD_Close", "EURUSD_Close", "USDJPY_Close"]
for col in price_columns:
    print(col, "Non-positive values:", (df[col] <= 0).sum())

# Check for date alignment 
print(df.index.min())
print(df.index.max())
print("Unique dates:", df.index.nunique())
print("Date index sorted:", df.index.is_monotonic_increasing)
date_gaps = df.index.to_series().diff().dt.days[1:]
print(date_gaps.value_counts().head(10))

# Investigating unusual price movements (greater than 2% daily)
returns = df[price_columns].pct_change() * 100
print(returns.describe())
unusual_movements = returns[(returns.abs() > 2).any(axis=1)]
print(unusual_movements)

# Check OHLC quality flags
flag_columns = ["GBPUSD_OHLC_Invalid", "EURUSD_OHLC_Invalid", "USDJPY_OHLC_Invalid"]
for col in flag_columns:
    print(col,df[col].value_counts())
for col in flag_columns:
    percentage = df[col].mean() * 100
    print(f"{col} percentage of invalid OHLC: {percentage:.2f}%")

# PART 3: Calculating FX returns

# Percentage returns
returns_pct = df[price_columns].pct_change() * 100
returns_pct = returns_pct.dropna()
returns_pct.head()
print(returns_pct.describe())

# Logarithmic returns
returns_log = np.log(df[price_columns] / df[price_columns].shift(1))
returns_log = returns_log.dropna()
returns_log.head()
print(returns_log.describe())

# PART 4: Basic financial analysis

# Average daily returns
print(returns_pct.mean())

# Daily volatility
daily_volatility = returns_pct.std()
print(daily_volatility)

# Annualised volatility (assuming 252 trading days)
annualised_volatility = (returns_pct.std() * np.sqrt(252))
print(annualised_volatility)

# Comparison of currency pairs
summary = pd.DataFrame({"Average Daily Return (%)": returns_pct.mean(), "Daily Volatility (%)": daily_volatility, "Annualised Volatility (%)": annualised_volatility})
print(summary)

# Visualise returns and volatility
returns_pct.plot(figsize = (10, 6), title = "Daily Percentage Returns")
plt.ylabel("Daily Returns (%)")
plt.xlabel("Date")
plt.axhline(0, color = "black", linewidth = 0.8, linestyle = "--")
plt.show()

# Correlation matrix of returns
correlation = returns_pct.corr()
print(correlation)

# Visualise correlation matrix
plt.figure(figsize = (8, 6))
plt.imshow(correlation, vmin = -1, vmax = 1, cmap = "coolwarm")
plt.colorbar(label = "Correlation")
plt.xticks(range(len(correlation.columns)), correlation.columns, rotation = 45)
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title("FX Returns Correlation Matrix")
plt.tight_layout()
plt.show()

# PART 5: Summary and report of findings

# Dataset overview
observations = len(df)
columns = len(df.columns)

start_date = df.index.min().strftime("%d/%m/%Y")
end_date = df.index.max().strftime("%d/%m/%Y")

# Data quality results

missing_values = df.isnull().sum()

duplicate_dates = df.index.duplicated().sum()

non_positive = (df[price_columns] <= 0).sum()

dates_sorted = df.index.is_monotonic_increasing
unique_dates = df.index.nunique()

unusual_counts = (returns_pct.abs() > 2).sum()

unusual_rows = ((returns_pct.abs() > 2).any(axis=1).sum())

ohlc_results = {}
for col in flag_columns:
    flags = (df[col].astype("string").str.strip().str.lower())

    invalid_count = flags.isin(["true", "1", "yes"]).sum()

    missing_flags = flags.isna().sum()

    invalid_percentage = (invalid_count / len(df) * 100)

    ohlc_results[col] = {"Invalid observations": int(invalid_count),"Invalid percentage": invalid_percentage,"Missing flags": int(missing_flags)}

# Financial analysis results

financial_summary = pd.DataFrame({"Average Daily Return (%)": returns_pct.mean(),"Daily Volatility (%)": daily_volatility,"Annualised Volatility (%)": annualised_volatility})
financial_summary = financial_summary.round(4)

correlation = returns_pct.corr()

most_volatile = annualised_volatility.idxmax()
least_volatile = annualised_volatility.idxmin()

highest_return = returns_pct.mean().idxmax()
lowest_return = returns_pct.mean().idxmin()

correlation_pairs = correlation.where(np.triu(np.ones(correlation.shape),k=1).astype(bool)).stack()
strongest_pair = (correlation_pairs.abs().idxmax())

strongest_correlation = (correlation_pairs.loc[strongest_pair])

# Markdown table function
def markdown_table(dataframe):

    headers = list(dataframe.columns)

    lines = ["| " + " | ".join(headers) + " |","| " + " | ".join(["---"] * len(headers)) + " |"]

    for index, row in dataframe.iterrows():

        values = [str(index)] + [str(value) for value in row.values]

        lines.append("| " + " | ".join(values) + " |")

    return "\n".join(lines)

quality_summary = pd.DataFrame({"Result": [f"{missing_values.sum()} missing values",f"{duplicate_dates} duplicate dates",f"{non_positive.sum()} non-positive prices",f"{unique_dates} unique dates",str(dates_sorted),f"{unusual_rows} observations"]}, index=["Missing values","Duplicate dates","Non-positive prices","Unique dates","Dates sorted correctly","Movements above 2%"])
ohlc_summary = pd.DataFrame(ohlc_results).T.round(3)
unusual_summary = pd.DataFrame({"Movements above 2%": unusual_counts})

# STEP 6: Write up of report

report = f"""
# AI-Powered FX Risk Intelligence Platform

## Week 1 – Session 3: Data Quality and Financial Understanding

## 1. Executive Summary

This session focused on validating the historical FX dataset
and developing an understanding of financial returns,
volatility and correlation.

The analysis covered GBP/USD, EUR/USD and USD/JPY.

Data validation checks were conducted to assess the
reliability and consistency of the dataset.

Simple percentage returns and logarithmic returns were
calculated, followed by initial financial analysis.

The objective was to establish a reliable dataset and
understand the financial characteristics of the three
currency pairs before progressing to risk modelling.

## 2. Dataset Overview

| Measure | Result |
|---|---|
| Data source | Yahoo Finance |
| Frequency | Daily |
| Currency pairs | GBP/USD, EUR/USD, USD/JPY |
| Start date | {start_date} |
| End date | {end_date} |
| Observations | {observations:,} |
| Columns | {columns} |

## 3. Data Quality Assessment

### 3.1 Validation Summary

{markdown_table(quality_summary)}

### 3.2 OHLC Validation

{markdown_table(ohlc_summary)}

OHLC validation flags identify observations where the
original Open, High, Low and Close prices failed the
implemented validation rules.

A flagged observation does not automatically mean
that its closing price is invalid.

### 3.3 Unusual Price Movements

The analysis identified daily percentage movements
greater than 2%.

{markdown_table(unusual_summary)}

Movements were identified using a 2% investigation
threshold.

These observations should be investigated rather than
automatically removed, as they may represent genuine
financial market events.

### 3.4 Data Quality Conclusion

The validation checks provide an assessment of the
completeness, consistency and reliability of the
processed FX dataset.

The results should be reviewed alongside the original
source files, particularly when assessing date alignment
and the effects of the inner join.

## 4. Financial Analysis

### 4.1 Simple Percentage Returns

Daily percentage returns were calculated using the
percentage change in consecutive closing exchange rates.

These returns measure the relative daily movement
in each currency pair.

### 4.2 Logarithmic Returns

Logarithmic returns were also calculated to provide
an alternative measure of daily FX movements.

They are widely used in financial modelling because
they are additive across consecutive periods.

### 4.3 Average Returns and Volatility

{markdown_table(financial_summary)}

Annualised volatility was calculated using a
252 trading-day convention.

### 4.4 Key Financial Findings

- Highest annualised volatility: {most_volatile}
- Lowest annualised volatility: {least_volatile}
- Highest average daily return: {highest_return}
- Lowest average daily return: {lowest_return}

### 4.5 Correlation Analysis

{markdown_table(correlation.round(4))}

The strongest absolute pairwise correlation was between
{strongest_pair[0]} and {strongest_pair[1]},
with a correlation coefficient of
{strongest_correlation:.4f}.

Correlation measures the strength and direction of
the relationship between daily currency returns.

## 5. Interpretation and Financial Understanding

The analysis demonstrates the distinction between
exchange rates and financial returns.

Exchange rates represent the relative value of one
currency against another, whereas returns measure
the percentage change in that value over time.

Volatility measures the variability of returns and
provides an indication of historical market risk.

Correlation helps identify relationships between
currency pairs and is relevant when assessing
portfolio risk.

These measures form the foundation for subsequent
financial risk modelling.

## 6. Limitations and Considerations

- The dataset uses daily closing prices rather than
  intraday observations.
- An inner join retains only dates shared by all
  three currency datasets.
- Historical volatility does not guarantee future
  volatility.
- Currency correlations can change over time.
- Unusual price movements require investigation
  before being classified as data errors.
- OHLC quality flags identify potential data issues
  but do not independently establish closing-price validity.

## 7. Conclusion and Next Steps

Session 3 established the foundations for financial
analysis using the processed FX dataset.

Data quality checks were completed, simple and
logarithmic returns were calculated, and initial
volatility and correlation measures were produced.

---

Report generated using Python and pandas.
"""

# STEP 7: Save report
project_folder = FilePath(__file__).resolve().parent.parent
docs_folder = project_folder / "docs"

docs_folder.mkdir(exist_ok=True)

report_path = docs_folder / "W1S3_findings.md"

report_path.write_text(report, encoding="utf-8")

print(f"Report successfully saved to: {report_path}")
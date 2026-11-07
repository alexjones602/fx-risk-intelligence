
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
| Start date | 03/11/2021 |
| End date | 03/11/2026 |
| Observations | 1,300 |
| Columns | 6 |

## 3. Data Quality Assessment

### 3.1 Validation Summary

| Result |
| --- |
| Missing values | 0 missing values |
| Duplicate dates | 0 duplicate dates |
| Non-positive prices | 0 non-positive prices |
| Unique dates | 1300 unique dates |
| Dates sorted correctly | True |
| Movements above 2% | 15 observations |

### 3.2 OHLC Validation

| Invalid observations | Invalid percentage | Missing flags |
| --- | --- | --- |
| GBPUSD_OHLC_Invalid | 28.0 | 2.154 | 0.0 |
| EURUSD_OHLC_Invalid | 35.0 | 2.692 | 0.0 |
| USDJPY_OHLC_Invalid | 71.0 | 5.462 | 0.0 |

OHLC validation flags identify observations where the
original Open, High, Low and Close prices failed the
implemented validation rules.

A flagged observation does not automatically mean
that its closing price is invalid.

### 3.3 Unusual Price Movements

The analysis identified daily percentage movements
greater than 2%.

| Movements above 2% |
| --- |
| GBPUSD_Close | 4 |
| EURUSD_Close | 1 |
| USDJPY_Close | 12 |

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

| Average Daily Return (%) | Daily Volatility (%) | Annualised Volatility (%) |
| --- | --- | --- |
| GBPUSD_Close | 0.0003 | 0.5273 | 8.3701 |
| EURUSD_Close | -0.0015 | 0.4735 | 7.5172 |
| USDJPY_Close | 0.0272 | 0.6198 | 9.8384 |

Annualised volatility was calculated using a
252 trading-day convention.

### 4.4 Key Financial Findings

- Highest annualised volatility: USDJPY_Close
- Lowest annualised volatility: EURUSD_Close
- Highest average daily return: USDJPY_Close
- Lowest average daily return: EURUSD_Close

### 4.5 Correlation Analysis

| GBPUSD_Close | EURUSD_Close | USDJPY_Close |
| --- | --- | --- |
| GBPUSD_Close | 1.0 | 0.7847 | -0.466 |
| EURUSD_Close | 0.7847 | 1.0 | -0.4916 |
| USDJPY_Close | -0.466 | -0.4916 | 1.0 |

The strongest absolute pairwise correlation was between
GBPUSD_Close and EURUSD_Close,
with a correlation coefficient of
0.7847.

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

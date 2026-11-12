
# AI-Powered FX Risk Intelligence Platform

## Week 2 - Session 2: Volatility Clustering and ARCH

## 1. Objective

The objective of this session was to investigate volatility clustering across GBP/USD, EUR/USD and USD/JPY exchange rates and determine whether historical market movements influence subsequent volatility.

The analysis used daily logarithmic returns, squared returns, rolling volatility, autocorrelation plots and ARCH-LM statistical tests.

## 2. Daily Return Analysis

A total of 1,299 daily return observations were analysed for each currency pair.

The calculated standard deviations were:

GBP/USD: 0.005275 (0.5275%)

EUR/USD: 0.004733 (0.4733%)

USD/JPY: 0.006206 (0.6206%)

USD/JPY demonstrated the highest overall return volatility, followed by GBP/USD and EUR/USD. Average daily returns were relatively close to zero across all three pairs, indicating that the analysis is primarily concerned with fluctuations around the average return rather than a consistent directional movement.

The largest positive daily return was recorded for GBP/USD at 3.03%, while the largest negative return was -4.23%. This demonstrates that significant market movements can occur in both directions.

## 3. Volatility Clustering and Autocorrelation

Squared daily returns were calculated to investigate whether large market movements tend to be followed by further large movements.

The analysis used autocorrelation function (ACF) plots across 30 lags to examine relationships between squared returns over time.

The purpose of this analysis was to identify whether volatility demonstrated persistence, rather than occurring randomly. The squared-return approach is particularly useful because it captures the magnitude of market movements independently of their direction.

## 4. ARCH-LM Test Results

The ARCH-LM test was conducted using 5, 10 and 20 lags to determine whether previous market shocks contain information about subsequent volatility.

At a 5% significance level, all three currency pairs demonstrated statistically significant ARCH effects.

The initial five-lag results were:

GBP/USD: LM statistic = 133.40, p-value = 4.51 × 10⁻²⁷.

EUR/USD: LM statistic = 46.40, p-value = 7.54 × 10⁻⁹.

USD/JPY: LM statistic = 19.91, p-value = 0.00130.

All p-values were below 0.05, meaning the null hypothesis of no ARCH effects was rejected for every currency pair.

Further testing across 10 and 20 lags produced similarly significant results. This indicates that volatility dependence is not limited to the most recent trading days.

GBP/USD produced the strongest ARCH-LM statistics, suggesting the strongest evidence of dependence in squared returns. EUR/USD also demonstrated substantial ARCH effects, while USD/JPY showed statistically significant but comparatively weaker evidence.

## 5. Implications for FX Risk Management

The findings suggest that FX volatility is not constant over time. Previous market shocks contain useful information about subsequent volatility, meaning periods of elevated market risk may persist.

This is important for the development of the FX Risk Intelligence Platform because relying on constant historical variance could underestimate risk during periods of heightened market activity.

The results support using conditional volatility models to produce more responsive risk estimates and improve volatility forecasting.
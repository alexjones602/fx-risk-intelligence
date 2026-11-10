
# AI-Powered FX Risk Intelligence Platform

## Week 2 - Session 1: Stationarity and Autocorrelation

## 1. Session Objective

The objective of this session was to investigate the statistical characteristics of the GBP/USD, EUR/USD and USD/JPY daily FX return series before progressing to econometric volatility modelling.

The analysis focused on testing stationarity using the Augmented Dickey-Fuller (ADF) and KPSS tests, alongside investigating autocorrelation across the first 20 lags.

The purpose was to establish whether the FX returns demonstrate sufficiently stable statistical properties and whether historical returns exhibit meaningful linear relationships over time.

## 2. Data Preparation

The analysis used the cleaned FX dataset developed during Week 1.

The dataset contained 1,300 observations for each currency pair, covering 3 November 2021 to 3 November 2026.

Daily percentage returns were calculated using the percentage change between consecutive exchange rate observations.

The resulting return series were:

- GBP/USD
- EUR/USD
- USD/JPY

The first observation was excluded from return calculations because no previous exchange rate was available.

## 3. Augmented Dickey-Fuller (ADF) Results

The ADF test was conducted on all three daily return series to investigate the presence of a unit root.

The null hypothesis assumed that each series was non-stationary.

A p-value below the 0.05 significance threshold provided evidence to reject the null hypothesis and support stationarity.

| Currency Pair | ADF Statistic | P-value | Conclusion |
|---|---:|---:|---|
| GBP/USD | -16.3955 | 2.67 × 10^-29 | Stationary |
| EUR/USD | -12.9042 | 4.19 × 10^-24 | Stationary |
| USD/JPY | -36.1463 | 0.0000* | Stationary |

*The USD/JPY p-value was displayed as zero by Python due to numerical rounding.*

All three ADF statistics were substantially more negative than their respective 5% critical values.

**Interpretation:**

The results provide very strong evidence against the null hypothesis of a unit root.

Therefore, all three daily FX return series demonstrate evidence of stationarity.

USD/JPY produced the most negative ADF statistic, followed by GBP/USD and EUR/USD.

## 4. Kwiatkowski-Phillips-Schmidt-Shin (KPSS) Results

The KPSS test was conducted as a complementary stationarity assessment.

Unlike ADF, the KPSS null hypothesis assumes that the series is stationary.

| Currency Pair | KPSS Statistic | P-value | Conclusion |
|---|---:|---:|---|
| GBP/USD | 0.1587 | 0.1000 | Stationary evidence |
| EUR/USD | 0.1390 | 0.1000 | Stationary evidence |
| USD/JPY | 0.1743 | 0.1000 | Stationary evidence |

All three KPSS statistics were below the 5% critical value of 0.463.

The reported p-values were 0.10, meaning there was insufficient evidence to reject the null hypothesis of stationarity.

Python also generated interpolation warnings because the calculated statistics fell below the lower end of the KPSS lookup table. The actual p-values are greater than the displayed 0.10.

**Interpretation:**

The KPSS results support the conclusions obtained from the ADF tests.

Both tests therefore provide consistent evidence that GBP/USD, EUR/USD and USD/JPY daily returns are stationary.

## 5. Comparison of ADF and KPSS Results

The two stationarity tests produced consistent results across all three currency pairs.

The ADF tests rejected the null hypothesis of a unit root, while the KPSS tests failed to reject the null hypothesis of stationarity.

This provides stronger combined evidence that the three daily FX return series are stationary.

No conflicting stationarity results were identified.

## 6. Autocorrelation Analysis

Autocorrelation was calculated across the first 20 lags for each currency pair.

The purpose was to investigate whether historical daily returns demonstrated linear relationships with subsequent returns.

The lag 1 results were:

| Currency Pair | Lag 1 Autocorrelation |
|---|---:|
| GBP/USD | 0.0023 |
| EUR/USD | 0.0094 |
| USD/JPY | -0.0041 |

All three coefficients were extremely close to zero.

**Interpretation:**

There is very little evidence of a linear relationship between consecutive daily FX returns.

This suggests that previous trading day's returns provide limited information about the direction of the following day's return.

Higher-lag analysis also produced relatively small autocorrelation coefficients.

Notable observations included:

- GBP/USD: Lag 6 (-0.0672) and lag 18 (0.0653) showed relatively stronger relationships.
- EUR/USD: Lag 6 (-0.0619) and lag 8 (0.0652) showed relatively stronger relationships.
- USD/JPY: Autocorrelation remained relatively small across all 20 lags.

These higher-lag relationships are modest and should not automatically be interpreted as statistically significant without further testing.

Overall, the three return series demonstrate relatively weak linear autocorrelation.

## 7. ACF Chart Analysis

The Autocorrelation Function (ACF) charts were generated for all three currency pairs across 20 lags.

The charts provided a visual representation of the autocorrelation coefficients and their approximate 95% confidence intervals.

The general pattern was consistent with the calculated autocorrelation results.

Most autocorrelation coefficients were relatively close to zero, suggesting limited linear serial dependence.

Some higher-lag observations appeared to extend beyond the confidence intervals, particularly for GBP/USD and EUR/USD.

However, these isolated observations do not establish persistent autocorrelation across the series.

Further investigation using the Ljung-Box test would help establish whether autocorrelation is jointly significant across multiple lags.

## 8. Overall Findings

The session produced three important findings.

**1. All three FX return series demonstrate stationarity.**

The ADF and KPSS tests provided consistent evidence that GBP/USD, EUR/USD and USD/JPY daily percentage returns are stationary.

**2. Linear autocorrelation is generally weak.**

Lag 1 autocorrelation was extremely close to zero across all three currency pairs.

Higher-lag coefficients were also relatively small, suggesting limited linear dependence in the direction of daily returns.

**3. Further investigation of volatility behaviour is required.**

Although returns demonstrate limited linear autocorrelation, this does not establish that their volatility is constant.

Financial markets frequently exhibit volatility clustering, where periods of large price movements are followed by further large movements.

Investigating squared returns and conducting ARCH-effect testing will therefore be important in the next stage.

## 9. Implications for GARCH Modelling

The results provide a positive foundation for progressing towards ARCH and GARCH modelling.

The stationarity findings support the use of daily FX returns as the underlying series for subsequent volatility analysis.

The limited autocorrelation in original returns also suggests that there may be relatively little linear dependence in daily return movements.

However, this does not mean that the magnitude of returns is independent over time.

The next stage will investigate whether squared returns demonstrate significant autocorrelation, indicating volatility clustering.

This distinction is particularly important because GARCH models are designed to estimate changing conditional variance rather than simply predict the direction of future exchange rate movements.

## 10. Conclusion

Week 2 Session 1 successfully established the statistical foundations for further econometric analysis of the three FX currency pairs.

Both ADF and KPSS tests demonstrated consistent evidence of stationarity across GBP/USD, EUR/USD and USD/JPY daily returns.

Autocorrelation analysis also identified generally weak linear relationships between historical and subsequent returns.

The findings support progressing to the investigation of volatility clustering and ARCH effects.

The next stage will focus on establishing whether historical market shocks influence subsequent volatility and whether this behaviour can be captured through ARCH and GARCH modelling.

**Overall conclusion:** The three FX return series demonstrate suitable stationarity characteristics for further econometric investigation. The next priority is to establish whether their conditional volatility exhibits persistent patterns that can be modelled and forecast.

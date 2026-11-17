# AI-Powered FX Risk Intelligence Platform

## Week 3 - Session 1: Feature Engineering and Predictive Targets

## 1. Objective

The aim of this session was to prepare the historical FX dataset for machine learning.

This involved creating predictive features from historical exchange rate data and defining a target variable that measures future five-day volatility.

The work focused on GBP/USD, EUR/USD and USD/JPY.

## 2. Feature Engineering

Predictive features were created to help machine learning models identify patterns in exchange rate movements and volatility.

The following seven features were calculated for each currency pair:

| Feature | Description |
|---|---|
| Return_1D | Percentage change in exchange rate over one trading day. |
| Return_5D | Percentage change over the previous five trading days. |
| Volatility_5D | Standard deviation of daily returns over five days. |
| Volatility_20D | Standard deviation of daily returns over 20 days. |
| Volatility_60D | Standard deviation of daily returns over 60 days. |
| Momentum_5D | Exchange rate movement over the previous five days. |
| Momentum_20D | Exchange rate movement over the previous 20 days. |

### Key calculations

- Daily returns were calculated using `pct_change()`.
- Rolling volatility was calculated using `.rolling(window=n).std()`.
- Momentum was calculated by comparing the current exchange rate with its value five or 20 trading days earlier.

These features provide the model with information about recent price movements, longer-term trends and changes in market volatility.

## 3. Defining the Five-Day Volatility Target

A forward-looking target was created for each currency pair:

- GBPUSD_Target_Volatility_5D
- EURUSD_Target_Volatility_5D
- USDJPY_Target_Volatility_5D

The target measures the standard deviation of the next five daily returns.

For example, when making a prediction at time T, the target represents volatility over trading days T+1 to T+5.

This is important because the model must learn to predict future volatility using information available at the time of prediction.

The target is not annualised.

## 4. Data Quality and Validation

Several checks were carried out to ensure the machine learning dataset was suitable for modelling.

The checks included:

- Identifying missing values.
- Checking for duplicate dates and observations.
- Confirming dates were in chronological order.
- Checking exchange rates were positive.
- Checking for negative volatility values.
- Confirming that the predictive features and target variables were correctly created.

Missing observations were expected at the beginning of the dataset because rolling calculations require a minimum number of historical observations. Additional observations were unavailable at the end because future five-day targets could not be calculated.

## 5. Final Machine Learning Dataset

The original dataset contained 1,300 observations.

After feature engineering and removal of incomplete observations, the final dataset contained:

| Measure | Result |
|---|---:|
| Original observations | 1,300 |
| Final observations | 1,235 |
| Observations removed | 65 |
| Total columns | 25 |
| Predictive features | 21 |
| Target variables | 3 |
| Date column | 1 |

The final dataset contains seven predictive features and one target variable for each of the three currency pairs, alongside the Date column.

## 6. Saving the Dataset

The final machine learning dataset was saved to:

`data/processed/ml_features.csv`

The session documentation was saved to:

`docs/session_01_feature_engineering.md`

This means the processed dataset can now be reused in future modelling sessions without repeating the feature engineering calculations.

## 7. Important Modelling Considerations

A few points need to be considered before training the models.

**Feature duplication**

Return_5D and Momentum_5D contain mathematically equivalent information. This creates unnecessary duplication in the feature set.

**Avoiding data leakage**

Target variables must never be included as predictive features. Only information available at the prediction date should be used to train the model.

**Chronological splitting**

The dataset must be divided into training, validation and test sets in date order rather than randomly.

A five-observation gap between the datasets is also intended to reduce overlap between the five-day forward-looking target windows.

**Separate currency models**

GBP/USD, EUR/USD and USD/JPY each have their own volatility target. Models should therefore be trained and evaluated separately for each currency pair, unless a deliberately designed pooled modelling approach is used.

## 8. Session Outcome

The session successfully transformed the cleaned historical FX dataset into a machine-learning dataset.

The main achievements were:

- Created 21 predictive features across three currency pairs.
- Defined three five-day forward-looking volatility targets.
- Completed data quality checks.
- Removed incomplete observations.
- Produced a final dataset containing 1,235 observations and 25 columns.
- Saved the processed dataset for use in subsequent modelling sessions.
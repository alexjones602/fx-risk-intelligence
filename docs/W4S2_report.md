# AI-Powered FX Risk Intelligence Platform

## Week 4 - Session 2: Out-Of-Sample testing and Walk Forward validation

## 1. Executive Summary

This session evaluated the out-of-sample forecasting performance of the Random Forest and XGBoost regression models developed during Week 3 of the AI-Powered FX Risk Intelligence Platform.

The objective was to determine whether the models could consistently forecast five-day future volatility across GBP/USD, EUR/USD and USD/JPY using previously unseen market observations.

An expanding-window walk-forward validation approach was implemented across three testing periods. Each model was repeatedly trained using historical observations and evaluated against a subsequent unseen testing window.

The validation produced 2,214 individual predictions across 18 model, currency and fold combinations.

The results indicate that:

- Both models successfully generated varying predictions across all three validation periods.
- Random Forest generally achieved lower MAE and RMSE than XGBoost.
- GBP/USD produced the most consistent forecasting errors across the validation periods.
- USD/JPY presented the greatest forecasting difficulty, particularly during the third validation period.
- All R² scores were negative, indicating that neither model consistently outperformed a simple benchmark based on the mean of the actual values in each testing period.
- Forecasting performance deteriorated substantially during the third validation period, suggesting potential sensitivity to changing market conditions.

Overall, the models provide a useful starting point for FX volatility forecasting, but further investigation and optimisation are required before either model can be considered reliable for practical forecasting applications.

## 2. Validation Methodology

An expanding-window walk-forward validation approach was selected to evaluate model performance over time.

Unlike random train-test splitting, this approach preserves the chronological order of financial observations. This is particularly important when forecasting financial time series, where future observations must not influence model training.

The dataset contained 1,235 observations, covering the period from January 2022 onwards.

The validation configuration was:

| Parameter | Configuration |
|---|---|
| Total observations | 1,235 |
| Initial training proportion | 70% |
| Initial training observations | 864 |
| Testing window proportion | 10% |
| Observations per testing window | 123 |
| Number of testing periods | 3 |
| Gap between training and testing | 5 observations |
| Forecasting models | Random Forest and XGBoost |
| Currency pairs | GBP/USD, EUR/USD and USD/JPY |

A five-observation gap was introduced between the training and testing datasets to reduce the risk of information leakage associated with overlapping five-day target periods.

### 2.1 Walk-Forward Validation Periods

Three sequential validation periods were constructed.

| Validation Period | Training Observations | Testing Observations | Testing Period |
|---|---:|---:|---|
| Fold 1 | 859 | 123 | 23 May 2025 – 11 November 2025 |
| Fold 2 | 982 | 123 | 12 November 2025 – 5 May 2026 |
| Fold 3 | 1,105 | 123 | 6 May 2026 – 23 October 2026 |

The training dataset expanded after each validation period, allowing the models to incorporate additional historical information before forecasting the next testing window.

This structure provides an indication of how model performance changes as additional historical observations become available.

### 2.2 Forecasting Models

Two machine learning regression models were evaluated.

**Random Forest Regressor**

The Random Forest model was configured using:

- 200 decision trees.
- Maximum tree depth of 6.
- Minimum samples per split of 10.
- Minimum samples per leaf of 5.
- Random state of 42.

The depth and minimum sample restrictions were intended to limit model complexity and reduce overfitting.

**XGBoost Regressor**

The XGBoost model was configured using:

- 200 boosting estimators.
- Maximum tree depth of 3.
- Learning rate of 0.03.
- Subsample of 0.8.
- Column subsampling of 0.8.
- Squared error regression objective.

XGBoost uses sequential boosting to improve predictions by learning from the errors of previous trees.

Both models were trained independently for each currency pair and validation period.

## 3. Model Evaluation Metrics

Three principal evaluation metrics were used to assess forecasting accuracy.

**Mean Absolute Error (MAE)**

MAE measures the average absolute difference between actual and predicted volatility.

A lower MAE indicates that the model's forecasts are, on average, closer to the actual observed values.

**Root Mean Squared Error (RMSE)**

RMSE measures the square root of the average squared forecasting errors.

Unlike MAE, RMSE places greater emphasis on larger forecasting errors. This makes it particularly useful when evaluating volatility forecasts, as large errors during periods of elevated market volatility can be especially important.

**R² (Coefficient of Determination)**

R² measures how much variation in the actual target values is explained by the model.

An R² value of 1 indicates a perfect fit, while a value of 0 indicates performance equivalent to predicting the mean of the testing-period target values.

A negative R² indicates that the model performs worse than this mean-based benchmark.

For this analysis, negative R² values are particularly important because they indicate that the models are not yet providing sufficiently strong predictive explanations of future volatility.

## 4. Results and Performance Analysis

The walk-forward validation produced the following results.

### 4.1 GBP/USD Forecasting Performance

| Model | Fold | MAE | RMSE | R² |
|---|---:|---:|---:|---:|
| Random Forest | 1 | 0.001360 | 0.001658 | -0.4986 |
| Random Forest | 2 | 0.001266 | 0.001612 | -0.0925 |
| Random Forest | 3 | 0.001449 | 0.001661 | -0.6112 |
| XGBoost | 1 | 0.001466 | 0.001807 | -0.7815 |
| XGBoost | 2 | 0.001237 | 0.001593 | -0.0670 |
| XGBoost | 3 | 0.001357 | 0.001591 | -0.4789 |

**Findings**

GBP/USD demonstrated the most consistent forecasting errors across the three validation periods.

Random Forest achieved lower MAE and RMSE during Fold 1, while XGBoost performed slightly better during Folds 2 and 3.

The lowest MAE was achieved by Random Forest during Fold 2, at 0.001266.

XGBoost also produced its strongest R² result during Fold 2, with a value of -0.0670. Although this remains negative, it represents a closer result to the mean-based benchmark than the other GBP/USD evaluations.

The relatively stable RMSE values suggest that forecasting errors did not increase substantially between the three periods.

However, all six R² results were negative, indicating that neither model consistently explained the variation in future GBP/USD volatility.

**Conclusion:** GBP/USD represents the strongest forecasting candidate of the three currency pairs, although further improvements are required to achieve positive out-of-sample R².

### 4.2 EUR/USD Forecasting Performance

| Model | Fold | MAE | RMSE | R² |
|---|---:|---:|---:|---:|
| Random Forest | 1 | 0.001649 | 0.002108 | -0.1511 |
| Random Forest | 2 | 0.001687 | 0.001904 | -0.2021 |
| Random Forest | 3 | 0.001492 | 0.001715 | -2.8033 |
| XGBoost | 1 | 0.001698 | 0.002255 | -0.3177 |
| XGBoost | 2 | 0.001741 | 0.001966 | -0.2825 |
| XGBoost | 3 | 0.001607 | 0.001815 | -3.2590 |

**Findings**

Random Forest consistently achieved lower MAE and RMSE than XGBoost across all three validation periods.

The lowest MAE was achieved by Random Forest during Fold 3, at 0.001492.

Interestingly, the third validation period produced the lowest absolute forecasting errors for both models. However, the R² results deteriorated considerably.

Random Forest recorded an R² of -2.8033, while XGBoost recorded -3.2590.

This demonstrates that lower absolute errors do not necessarily translate into better explanatory performance. The R² metric is influenced by the amount of variation in the actual target values during the testing period.

The substantial deterioration in R² suggests that the models struggled to explain the variation in future EUR/USD volatility during Fold 3.

**Conclusion:** Random Forest was the stronger EUR/USD model across all three periods. However, the significant deterioration in R² during Fold 3 highlights a potential weakness in adapting to changing volatility patterns.

### 4.3 USD/JPY Forecasting Performance

| Model | Fold | MAE | RMSE | R² |
|---|---:|---:|---:|---:|
| Random Forest | 1 | 0.001948 | 0.002582 | -0.2646 |
| Random Forest | 2 | 0.002219 | 0.002666 | -0.4145 |
| Random Forest | 3 | 0.004585 | 0.005015 | -2.9291 |
| XGBoost | 1 | 0.002001 | 0.002680 | -0.3627 |
| XGBoost | 2 | 0.002351 | 0.002800 | -0.5607 |
| XGBoost | 3 | 0.004672 | 0.005130 | -3.1112 |

**Findings**

USD/JPY produced the weakest overall forecasting performance.

Random Forest achieved lower MAE and RMSE than XGBoost across all three validation periods.

However, both models experienced a substantial deterioration during Fold 3.

Random Forest MAE increased from 0.002219 in Fold 2 to 0.004585 in Fold 3. XGBoost MAE increased from 0.002351 to 0.004672.

The deterioration was also reflected in RMSE, which increased to 0.005015 for Random Forest and 0.005130 for XGBoost.

Both models recorded substantially negative R² values during Fold 3, indicating particularly weak performance relative to the mean-based benchmark.

This suggests that the models struggled to capture the volatility behaviour of USD/JPY during the most recent testing period.

Potential explanations include changes in market volatility, unusual price movements, changing relationships between explanatory variables and future volatility, or a market regime not adequately represented in the training data.

These explanations require further investigation rather than being assumed from the metrics alone.

**Conclusion:** Random Forest performed marginally better than XGBoost, but neither model demonstrated sufficiently reliable USD/JPY forecasting performance. This currency pair should be prioritised for further investigation.

## 5. Comparison Between Random Forest and XGBoost

Comparing the two models across all three currency pairs reveals a relatively consistent pattern.

| Currency Pair | Stronger Model Based on MAE/RMSE | Key Observation |
|---|---|---|
| GBP/USD | Mixed | XGBoost performed slightly better in Folds 2 and 3; Random Forest performed better in Fold 1 |
| EUR/USD | Random Forest | Lower MAE and RMSE in all three folds |
| USD/JPY | Random Forest | Lower MAE and RMSE in all three folds |

Random Forest demonstrated the strongest overall consistency.

It outperformed XGBoost on both MAE and RMSE in 12 out of the 18 individual comparisons.

XGBoost performed better in six comparisons, all relating to GBP/USD.

This suggests that Random Forest may be better suited to the current feature set and model configuration, particularly when forecasting EUR/USD and USD/JPY volatility.

However, the differences between the models were relatively small in several testing periods.

It would therefore be premature to conclude that Random Forest is universally superior.

The consistently negative R² values also demonstrate that neither model has yet achieved sufficiently strong out-of-sample explanatory performance.

## 6. Analysis of Performance Across Market Periods

One of the most important findings from the walk-forward validation is the deterioration in forecasting performance during Fold 3.

The testing period covered May to October 2026.

The results were particularly concerning for EUR/USD and USD/JPY, where both models recorded substantially more negative R² values.

For USD/JPY, the increase in MAE and RMSE indicates a significant deterioration in absolute forecasting accuracy.

For EUR/USD, the absolute errors actually decreased, but R² became substantially more negative. This suggests that the models struggled to explain the variation in the actual target values during this period.

GBP/USD displayed comparatively stable MAE and RMSE values, although its R² scores also remained negative.

These findings highlight the importance of evaluating forecasting models across multiple market conditions rather than relying on a single train-test split.

A model that performs adequately during one period may struggle when the underlying financial market behaviour changes.

The results therefore suggest that the current models may have limitations in adapting to changing market regimes.

## 7. Prediction Quality and Validation Integrity

The validation process generated 2,214 predictions in total.

This represents:

- 3 currency pairs.
- 2 forecasting models.
- 3 validation periods.
- 123 predictions per combination.

Every currency, model and fold combination contained 123 predictions.

The prediction counts therefore confirm that all 18 validation combinations were successfully evaluated.

The `Unique_Predictions` diagnostic also demonstrated that the models were generating varying forecasts rather than returning a single constant prediction.

Most combinations produced 123 unique predictions. EUR/USD XGBoost during Fold 2 produced 122 unique predictions.

This confirms that the models were responding to differences in the input features, although prediction variation alone does not establish forecasting accuracy.

The validation structure also preserved chronological ordering and used a five-observation gap between training and testing.

One further consideration is that the five-day target periods associated with observations within and across testing folds may overlap. This does not invalidate the current evaluation, but should be considered when interpreting aggregate performance and when designing a more advanced validation framework.

## 8. Key Limitations Identified

Several limitations were identified through the results.

**1. Negative out-of-sample R²**

All 18 model evaluations produced negative R² values.

This indicates that neither model consistently outperformed the mean-based benchmark within the individual testing periods.

Further feature engineering and model optimisation are required.

**2. Sensitivity to changing market conditions**

The deterioration in Fold 3, particularly for USD/JPY, suggests that the models may not generalise effectively across changing market environments.

**3. Currency-specific forecasting performance**

The models do not perform equally well across all currency pairs.

USD/JPY appears particularly difficult to forecast, suggesting that currency-specific characteristics may require additional consideration.

**4. Limited model configurations**

Only one configuration of Random Forest and one configuration of XGBoost were evaluated.

The results may therefore improve through systematic hyperparameter optimisation.

**5. Benchmark comparison**

Although R² provides a mean-based benchmark, additional comparisons against simple forecasting approaches are required to establish whether the machine learning models provide practical predictive value.

# AI-Powered FX Risk Intelligence Platform

## Week 3 - Session 2: Random Forest Modelling

## 1. Session Objective

The objective of this session was to develop and evaluate my first machine-learning model for the FX Risk Intelligence Platform.

I used a Random Forest Regressor to predict future five-day volatility (`Target_Volatility_5D`) using the features created during the previous feature engineering session.

The main aims were to:
- Understand how a Random Forest model works.
- Prepare the dataset for machine learning.
- Train the model using historical FX data.
- Evaluate its predictive performance.
- Identify which features have the greatest influence on predictions.

## 2. Dataset Preparation

The engineered dataset was divided into three separate datasets:

| Dataset | Observations |
|---|---:|
| Training | 859 |
| Validation | 180 |
| Testing | 186 |
| **Total** | **1,225** |

The data was split chronologically rather than randomly. This is important when working with financial time-series data because the model should learn from historical observations and make predictions about later periods.

Five observations were left between the dataset sections to help reduce the risk of overlapping future volatility targets.

The target variable was `Target_Volatility_5D`, while the remaining selected numerical features were used as predictors.

## 3. Random Forest Model Development

I created a Random Forest Regressor using Python's Scikit-learn library.

A Random Forest works by building multiple decision trees and combining their predictions to produce a final result. This helps capture relationships between different financial variables.

The model was configured using the following parameters:

| Parameter | Setting |
|---|---:|
| Number of trees | 200 |
| Maximum tree depth | 10 |
| Minimum samples to split | 5 |
| Minimum samples per leaf | 2 |
| Random state | 42 |

The model was trained using the training dataset and then used to generate predictions against the validation dataset.

## 4. Model Evaluation

To assess performance, I used three evaluation metrics:

- **MAE (Mean Absolute Error):** Measures the average absolute difference between actual and predicted volatility. Lower values indicate better accuracy.
- **RMSE (Root Mean Squared Error):** Measures prediction error while placing greater weight on larger errors. Lower values are better.
- **R² (R-squared):** Measures how well the model explains variation in the target variable. A value closer to 1 is generally better.

### Validation Results

I compared the Random Forest against a baseline model that simply predicts the average volatility from the training data.

| Metric | Random Forest | Baseline |
|---|---:|---:|
| MAE | 0.001357 | 0.001578 |
| RMSE | 0.001677 | 0.001842 |
| R² | -0.6321 | -0.9709 |

The Random Forest performed better than the baseline across all three metrics.

In particular:
- MAE improved by approximately 14%.
- RMSE improved by approximately 9%.
- R² improved from -0.9709 to -0.6321.

This indicates that the Random Forest was able to identify some useful patterns in the historical FX data.

However, the negative R² score shows that the model still struggles to explain changes in future volatility. Although it outperformed the baseline, its predictive performance remains limited.

### Final Test Results

After evaluating the model, I used the separate test dataset to assess how well it performed on unseen observations.

| Metric | Test Result |
|---|---:|
| MAE | 0.001768 |
| RMSE | 0.002040 |
| R² | -0.648819 |

The test results were weaker than the validation results, with both MAE and RMSE increasing.

This suggests that the model found it more difficult to predict volatility in the later dataset. It also indicates that the model may not generalise consistently to new market conditions.

## 5. Feature Importance

I examined the model's feature importance scores to identify which variables contributed most to its predictions.

The five most important features were:

| Feature | Importance |
|---|---:|
| GBPUSD_Volatility_20D | 0.338400 |
| EURUSD_Volatility_60D | 0.085136 |
| GBPUSD_Volatility_60D | 0.067192 |
| USDJPY_Volatility_60D | 0.060687 |
| EURUSD_Volatility_20D | 0.059736 |

The most significant finding was that `GBPUSD_Volatility_20D` accounted for approximately 33.84% of the model's feature importance.

This suggests that recent GBP/USD volatility was particularly influential when estimating future volatility.

The results also show that longer-term volatility measures across EUR/USD and USD/JPY contributed to the model's predictions.

Feature importance indicates which variables the model relied on most heavily. It does not necessarily mean that these variables directly cause future volatility.

## 6. Prediction Analysis

I also compared the model's predicted volatility against the actual values in the test dataset.

The initial predictions showed that the model sometimes overestimated future volatility.

| Date | Actual Volatility | Predicted Volatility |
|---|---:|---:|
| 10/02/2026 | 0.002023 | 0.003728 |
| 11/02/2026 | 0.002406 | 0.003988 |
| 12/02/2026 | 0.002987 | 0.004099 |
| 13/02/2026 | 0.002851 | 0.004017 |
| 16/02/2026 | 0.004200 | 0.004117 |

The model initially predicted higher volatility than actually occurred. However, by 16 February, its prediction was much closer to the actual value.

This highlights that although the model can identify general volatility patterns, its predictions are not consistently accurate.

## 7. Saving Model Outputs

At the end of the session, I successfully saved the model and its supporting outputs.

The main files generated were:

- `random_forest_model.pkl` – saved trained Random Forest model.
- `validation_predictions.csv` – validation actual and predicted values.
- `test_predictions.csv` – test actual and predicted values.
- `feature_importance.csv` – feature importance scores.

These outputs will allow me to compare the Random Forest against other machine-learning models in future sessions.
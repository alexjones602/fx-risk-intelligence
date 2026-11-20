# AI-Powered FX Risk Intelligence Platform

## Week 3 - Session 3: XGBoost and Model comparisons

## 1. Session Objective

The objective of this session was to develop, train and evaluate an XGBoost regression model to forecast future foreign exchange market volatility.

Following the previous session on Random Forest modelling, this session introduced XGBoost as a second machine-learning approach.

The main objectives were:

- Understand how XGBoost works.
- Prepare the FX dataset for model training.
- Train an XGBoost regression model.
- Generate five-day volatility predictions.
- Evaluate model performance using MAE, RMSE and R-squared.
- Compare XGBoost against Random Forest.
- Analyse feature importance.
- Save the trained model and associated outputs.

## 2. Dataset Preparation

The dataset contained historical foreign exchange information for three currency pairs:

- GBP/USD
- EUR/USD
- USD/JPY

The existing feature-engineering process provided several explanatory variables for each currency pair.

These included:

- Daily returns (1-day and 5-day).
- Historical volatility (5-day, 20-day and 60-day).
- Momentum (5-day and 20-day).

The prediction target was:

`GBPUSD_Target_Volatility_5D`

This represented future five-day GBP/USD volatility.

The three target variables were excluded from the explanatory feature dataset to prevent target information from being included as model inputs.

After removing observations with missing target values, the modelling dataset contained:

- 1,235 observations.
- 21 explanatory features.
- One target variable.

## 3. Training, Validation and Testing

The dataset was divided chronologically rather than randomly.

This was important because financial time-series data must preserve the sequence of historical observations.

The dataset was divided into:

- Training: 70%
- Validation: 15%
- Testing: 15%

A five-observation gap was introduced between the datasets to reduce overlap caused by the five-day forward-looking volatility target.

The training dataset was used to fit the model, the validation dataset was used during model evaluation, and the testing dataset was reserved for measuring final predictive performance.

## 4. XGBoost Model Development

XGBoost (Extreme Gradient Boosting) is an ensemble machine-learning algorithm that builds multiple decision trees sequentially.

Each new tree attempts to improve upon the errors made by previous trees.

This allows the algorithm to identify complex relationships and non-linear patterns within financial datasets.

The model was developed using Python's `XGBRegressor` implementation.

The following parameters were configured:

| Parameter | Value | Purpose |
|---|---|---|
| n_estimators | 600 | Number of boosting trees |
| learning_rate | 0.03 | Controls the contribution of each tree |
| max_depth | 3 | Limits tree complexity |
| subsample | 0.8 | Uses 80% of observations per tree |
| colsample_bytree | 0.8 | Uses 80% of features per tree |
| min_child_weight | 5 | Controls minimum child-node weight |
| reg_lambda | 5 | Applies L2 regularisation |
| objective | reg:squarederror | Regression objective |
| eval_metric | rmse | Root Mean Squared Error |
| random_state | 42 | Ensures reproducibility |

The relatively low learning rate and restricted tree depth were intended to help control model complexity and reduce overfitting.

The model was successfully trained using the training dataset, with the validation dataset supplied during training.

## 5. Model Predictions and Evaluation

Following training, the XGBoost model generated predictions using the unseen testing dataset.

Three evaluation metrics were calculated.

### Mean Absolute Error (MAE)

Measures the average absolute difference between predicted and actual volatility values.

Lower values indicate more accurate predictions.

### Root Mean Squared Error (RMSE)

Measures prediction errors while placing greater emphasis on larger errors.

Lower values indicate better performance.

### R-squared (R²)

Measures how much variation in the target variable is explained by the model.

A negative R² indicates that the model performs worse than a baseline that predicts the mean of the actual target values on the test dataset.

The XGBoost results were:

| Evaluation Metric | XGBoost Result |
|---|---:|
| MAE | 0.001620 |
| RMSE | 0.001929 |
| R² | -0.451846 |

The MAE and RMSE values indicate the average scale of prediction errors was relatively small.

However, the negative R² is an important limitation.

Despite producing reasonably small absolute errors, the model did not explain the variation in future volatility sufficiently well to outperform the mean-prediction baseline.

This suggests that further model development and feature refinement will be necessary.

## 6. Random Forest and XGBoost Comparison

The next stage compared XGBoost against the Random Forest model developed in the previous session.

The comparison produced the following results:

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Random Forest | 0.001801 | 0.002072 | -0.675897 |
| XGBoost | 0.001620 | 0.001929 | -0.451846 |

XGBoost performed better across all three evaluation metrics.

Key observations:

- XGBoost achieved a lower MAE than Random Forest.
- XGBoost also produced a lower RMSE.
- XGBoost achieved a less negative R².
- Both models produced negative R² values, indicating that neither currently provides satisfactory predictive performance against the mean baseline.

Overall, XGBoost demonstrated an improvement over Random Forest, although further optimisation is required before either model can be considered reliable for forecasting future FX volatility.

## 7. Feature Importance Analysis

An important part of the session involved identifying which explanatory variables contributed most to the XGBoost model's predictions.

The model's built-in feature importance scores were extracted and ranked in descending order.

The five most influential features were:

| Feature | Importance |
|---|---:|
| GBPUSD_Volatility_20D | 0.168101 |
| GBPUSD_Momentum_5D | 0.099589 |
| GBPUSD_Volatility_60D | 0.082600 |
| GBPUSD_Return_5D | 0.076748 |
| EURUSD_Volatility_60D | 0.066629 |

The results suggest that historical GBP/USD volatility over 20 days was the most influential variable in predicting future five-day volatility.

GBP/USD momentum over five days was the second most important feature, indicating that recent market movements also contributed to the model's predictions.

Interestingly, EUR/USD and USD/JPY variables also appeared among the influential features.

This suggests that movements in other major currency pairs may contain useful information when forecasting GBP/USD volatility.

However, feature importance measures the model's reliance on individual variables. It does not establish causation or guarantee that a feature will remain important in future market conditions.
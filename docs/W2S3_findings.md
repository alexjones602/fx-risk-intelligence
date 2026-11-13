
# AI-Powered FX Risk Intelligence Platform

## Week 2 - Session 3: GARCH(1,1) Modelling and Forecasting

## 1. Objective

The objective of this session was to develop and estimate GARCH(1,1) models for GBP/USD, EUR/USD and USD/JPY to investigate volatility persistence and forecast future FX market volatility.

Building on the previous session's investigation into volatility clustering and ARCH effects, this exercise used GARCH modelling to quantify the relationship between historical market shocks and subsequent volatility.

The analysis also evaluated the forecasting performance of each model using an out-of-sample testing approach.

## 2. GARCH model estimation results

Separate GARCH(1,1) models were estimated for all three currency pairs using historical daily logarithmic returns.

The models produced the following parameter estimates:
Parameter	GBP/USD	EUR/USD	USD/JPY
Omega	0.00313	0.00187	0.01346
Alpha	0.04891	0.03737	0.06312
Beta	0.93916	0.95422	0.90326
Persistence	0.98807	0.99159	0.96638
Long-run volatility (%)	0.51229	0.47144	0.63274

Interpretation of results
Volatility persistence:

All three currency pairs demonstrate high volatility persistence, with alpha and beta coefficients combining to produce values close to 1.

EUR/USD recorded the highest persistence at 0.99159, followed by GBP/USD at 0.98807 and USD/JPY at 0.96638.

This suggests that volatility shocks in all three currency markets can have a lasting impact, with EUR/USD demonstrating the strongest persistence.

Sensitivity to market shocks (Alpha):

USD/JPY recorded the highest alpha coefficient of 0.06312, compared with 0.04891 for GBP/USD and 0.03737 for EUR/USD.

This suggests that USD/JPY volatility responds more strongly to new market shocks.

EUR/USD has the lowest alpha coefficient, suggesting a relatively smaller immediate response to unexpected market movements.

Volatility persistence (Beta):

EUR/USD recorded the highest beta coefficient at 0.95422, indicating that previous volatility has a particularly strong influence on its subsequent conditional variance.

This suggests that volatility in EUR/USD tends to decay more gradually following periods of market disruption.

Long-run volatility:

USD/JPY recorded the highest estimated long-run daily volatility at 0.63274%, compared with 0.51229% for GBP/USD and 0.47144% for EUR/USD.

This indicates that USD/JPY has the highest estimated long-run volatility of the three currency pairs under the fitted models.

## 3. Five-day volatility forecasting

The fitted GARCH models were used to generate five-day ahead conditional volatility forecasts for all three currency pairs.

The forecasts were calculated by extracting the predicted conditional variance and converting it into standard deviation.

The resulting forecasts were visualised together to compare the expected volatility patterns across the three FX markets.

The five-day forecast outputs were successfully generated for GBP/USD, EUR/USD and USD/JPY.

The forecasts provide an indication of how current market volatility is expected to evolve over the next five trading days.

An important characteristic of the GARCH model is that forecasts generally move towards their estimated long-run volatility level as the forecast horizon increases.

This reflects the model's assumption that volatility shocks gradually lose their influence over time.

## 4. Out-of-sample forecasting evaluation

To assess forecasting performance, the historical dataset was divided into an 80% training sample and a 20% testing sample.

The evaluation produced the following results:
Currency pair	Testing observations	MSE	QLIKE
GBP/USD	260	0.066180	1.460641
EUR/USD	260	0.043597	1.442046
USD/JPY	260	0.364251	2.008001

All three models successfully generated 260 matched out-of-sample forecasts.
Interpretation of results:

GBP/USD:

GBP/USD produced an MSE of 0.066180 and a QLIKE score of 1.460641.

This indicates a moderate forecasting error relative to the other currency pairs. Its QLIKE score was slightly higher than EUR/USD, suggesting that its volatility forecasts were marginally less accurate under this evaluation metric.

EUR/USD:

EUR/USD achieved the lowest MSE of 0.043597 and the lowest QLIKE score of 1.442046.

This suggests that EUR/USD produced the strongest forecasting performance of the three currency pairs.

Its relatively low forecasting errors indicate that the GARCH model was better able to estimate changes in its conditional variance over the testing period.

USD/JPY:

USD/JPY recorded the highest MSE of 0.364251 and QLIKE of 2.008001.

This indicates weaker forecasting performance compared with GBP/USD and EUR/USD.

The larger forecasting errors suggest that USD/JPY volatility was more difficult for the GARCH model to predict accurately.

This may reflect its higher estimated long-run volatility and greater sensitivity to new market shocks.

Overall forecasting comparison:

EUR/USD demonstrated the strongest forecasting performance across both evaluation metrics, while USD/JPY demonstrated the weakest.

This suggests that although GARCH(1,1) can be applied consistently across different currency pairs, its forecasting effectiveness varies between FX markets.

## 5. Key findings

The analysis produced five main findings:

1. High volatility persistence: All three currency pairs demonstrated volatility persistence, with alpha plus beta values close to one.

2. Different responses to market shocks: USD/JPY had the highest alpha coefficient, suggesting greater sensitivity to new market information.

3. Different long-run volatility levels: USD/JPY recorded the highest estimated long-run volatility, while EUR/USD recorded the lowest.

4. Differences in forecasting accuracy: EUR/USD achieved the lowest MSE and QLIKE scores, indicating the strongest out-of-sample forecasting performance.

5. Model limitations: The results demonstrate that a standard GARCH(1,1) model does not perform equally well across all currency pairs. Alternative specifications may improve forecasting accuracy, particularly for USD/JPY.

## 6. Limitations and further investigation

Although the GARCH(1,1) models produced useful volatility estimates, several limitations should be considered.
- The models assume normally distributed standardised returns, which may underestimate the probability of extreme market movements.
- GARCH(1,1) does not explicitly account for asymmetric volatility responses to positive and negative shocks.
- Historical volatility patterns may not fully capture unexpected economic or geopolitical events.
- Squared daily returns are used as a proxy for realised variance rather than a direct measurement of underlying volatility.
Potential improvements include testing a Student's t-distribution, investigating EGARCH models and comparing forecasting performance across alternative volatility specifications.

## 7. Conclusion

This session successfully developed and evaluated three independent GARCH(1,1) models for GBP/USD, EUR/USD and USD/JPY.

The results demonstrated that volatility persistence is an important characteristic across all three FX markets, although their sensitivity to market shocks and long-run volatility levels differ.

EUR/USD produced the strongest out-of-sample forecasting performance, while USD/JPY presented the greatest forecasting challenge.

The analysis demonstrates how GARCH modelling can be used to estimate changing market risk and generate forward-looking volatility forecasts.

Importantly, the outputs provide a foundation for the next stage of the AI-Powered FX Risk Intelligence Platform, where volatility forecasts can be incorporated into Value at Risk (VaR) and Expected Shortfall calculations.
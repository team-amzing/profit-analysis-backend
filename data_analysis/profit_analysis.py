"""
Using the predictions created in price_prediction.py the profit margin is analysed
for each prediction.
"""

from data_analysis.price_prediction import model_arima


def sell_function(data_points, n_days, stock, daily_costs):
    # Predict 5 days using 2000 data points
    prediction_df = model_arima(data_points, n_days)

    # Calculates the profit for each day predicted taking into account running costs.
    # And compares it with the highest profit so far.
    count = 1
    best_profit = 0
    price = prediction_df.iloc[0]["predicted_value"]
    pot_profit = stock * price
    profit_array = [pot_profit]
    while count < n_days:
        price = prediction_df.iloc[count]["predicted_value"]
        profit = stock * price - daily_costs * count
        profit_array.append(profit)
        if pot_profit < profit:
            best_profit = count
            pot_profit = profit
        count += 1
    if best_profit == 0:
        result = "Sell today"
    elif best_profit == 1:
        result = "Sell tomorrow"
    else:
        result = "Sell in " + str(best_profit) + " days"
    return result, profit_array


def calculate_profit_margin(n_days, n_predictions, stock, daily_costs):
    """Calculate the predicted profit margin for a given set of
    predictions."""

    predictions = model_arima(n_days, n_predictions)
    # Use pandas apply method to add a new column to the data frame populated
    # based on existing rows in the table
    predictions["profit_margin"] = predictions.apply(
        lambda row: row.predicted_value * stock - daily_costs, axis=1
    )
    return predictions

"""
Using the predictions created in price_prediction.py the profit margin is analysed
for each prediction.

def sell_today(value, predictions):
    """Returns a boolean value for to indicate whether to sell today."""
    return value > max(predictions.predicted_value)
"""
# set variables
No_units = 750000
Running_cost = 30000

def sell_today(today_value, tomorrow_value, No_units, Running_cost):
    """Returns a boolean value for to indicate whether to sell today, after considering todays and tomorrows profit."""
    today_profit = today_value*No_units
    tomorrows_profit = (tomorrow_value*No_units) - Running_cost
    if today_profit >= tomorrows_profit
        return today_profit > tomorrows_profit
    else:
        return today_profit < tomorrows_profit

def get_predictions(model, n_days, n_predictions, current_value, No_units, Running_cost):
    """Returns the predictions from a given model and a comparison between the best predicted value and
    the current value."""
    predictions = model(n_days, n_predictions, current_value)
    return sell_today(current_value, predictions[0], No_units, Running_cost), predictions


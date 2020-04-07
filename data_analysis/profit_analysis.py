"""
Using the predictions created in price_prediction.py the profit margin is analysed
for each prediction.
"""


def sell_today(value, predictions, no_units, daily_cost):
    """Returns a boolean value for to indicate whether to sell today."""
    profit_today = value * no_units
    profit_tomorrow = (predictions.predicted_value[0] * no_units) - daily_cost

    return profit_today > profit_tomorrow


def get_predictions(model, n_days, n_predictions, current_value, no_units, daily_cost):
    """Returns the predictions from a given model and a comparison between the best predicted value and
    the current value."""
    predictions = model(n_days, n_predictions, current_value)
    return sell_today(current_value, predictions, no_units, daily_cost), predictions


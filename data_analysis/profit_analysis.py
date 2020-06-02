"""
Using the predictions created in price_prediction.py the profit margin is analysed
for each prediction.
"""


def sell_today(value_today, value_tomorrow, no_units, daily_cost):
    """Returns a boolean value for to indicate whether to sell today."""
    profit_today = value_today * no_units
    profit_tomorrow = (value_tomorrow * no_units) - daily_cost
    return profit_today > profit_tomorrow


def get_predictions(model, n_days, n_predictions, current_value, no_units, daily_cost, covid_today):
    """Returns the predictions from a given model and a comparison between the best predicted value and
    the current value."""
    predictions = model(n_days, n_predictions, current_value)
    next_value = predictions.predicted_value[0]
    todays_error = 10 * covid_today
    predictions['error'] = predictions['error'] * todays_error
    return sell_today(current_value, next_value, no_units, daily_cost), predictions


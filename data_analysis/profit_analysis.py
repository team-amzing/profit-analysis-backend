"""
Using the predictions created in price_prediction.py the profit margin is analysed
for each prediction.
"""


def sell_today(value_today, value_tomorrow, no_units, daily_cost, error_tomorrow_upper,
               error_tomorrow_lower):
    """Returns a boolean value for to indicate whether to sell today."""
    confidence = 0.8 # 80%
    profit_today = value_today * no_units
     
    max_cost_tomorrow = error_tomorrow_upper
    min_cost_tomorrow = error_tomorrow_lower
    difference = max_cost_tomorrow - min_cost_tomorrow
    count = 0
     
    for ii in range(int(min_cost_tomorrow), int(max_cost_tomorrow + 1)):
        profit_tomorrow = cost(no_units, (min_cost_tomorrow + ii), daily_cost)
        if profit_tomorrow > profit_today:
            count += 1
    confidence_value = count/difference
    return confidence_value < confidence


def get_predictions(model, n_days, n_predictions, current_value, no_units, daily_cost, covid_today):
    """Returns the predictions from a given model and a comparison between the best predicted value and
    the current value."""
    predictions = model(n_days, n_predictions, current_value)
    next_value = predictions.predicted_value[0]
    todays_error = covid_today
    predictions['error_lower'] = predictions['error_lower'] * todays_error
    error_tomorrow_upper = predictions['error_upper'].iloc[0]
    error_tomorrow_lower = predictions['error_lower'].iloc[0]
    return sell_today(current_value, next_value, no_units, daily_cost, error_tomorrow_upper,
                      error_tomorrow_lower), predictions


def cost(no_units, value, daily_cost):
    profit = (value * no_units) - daily_cost
    return profit


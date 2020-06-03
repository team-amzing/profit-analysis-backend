"""
Using the predictions created in price_prediction.py the profit margin is analysed
for each prediction.
"""


def sell_today(value_today, value_tomorrow, no_units, daily_cost, error_tomorrow):
    """Returns a boolean value for to indicate whether to sell today."""
    confidence = 0.8 # 80%
    profit_today = value_today * no_units
    max_cost_tomorrow = int(value_tomorrow + error_tomorrow)
    min_cost_tomorrow = int(value_tomorrow - error_tomorrow)
    difference = max_cost_tomorrow - min_cost_tomorrow
    count = 0
    for ii in range(min_cost_tomorrow, max_cost_tomorrow + 1):
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
    todays_error = 10 * covid_today
    predictions['error'] = predictions['error'] * todays_error
    error_tomorrow = predictions['error'].iloc[0]
    return sell_today(current_value, next_value, no_units, daily_cost, error_tomorrow), predictions

def cost(no_units, value, daily_cost):
    profit = (value * no_units) - daily_cost
    return profit
    

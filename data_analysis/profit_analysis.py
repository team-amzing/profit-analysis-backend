"""
Using the predictions created in price_prediction.py the profit margin is analysed
for each prediction.
"""
import numpy as np

def sell_today(value_today, value_tomorrow, no_units, daily_cost, error_tomorrow):
    """Returns a boolean value for to indicate whether to sell today with a confidence of 80%."""
    confidence = 0.8 # 80%
    profit_today = value_today * no_units
    max_cost_tomorrow = round((value_tomorrow + error_tomorrow), 3)
    min_cost_tomorrow = round((value_tomorrow - error_tomorrow), 3)
    difference = max_cost_tomorrow - min_cost_tomorrow
    count = 0
    value_array = values_array(min_cost_tomorrow, max_cost_tomorrow)
    for ii in range(0, len(value_array)):
        profit_tomorrow = (value_array[ii] * no_units) - daily_cost
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

def values_array(min_cost, max_cost):
    """creates an array of numbers between max and min price to count."""
    value_array = np.arange(min_cost, (max_cost+0.001), 0.001)
    return value_array   

"""
Using the predictions created in price_prediction.py the profit margin is analysed
for each prediction.
"""

from data_analysis.price_prediction import model_arima
from get_data.get_data import get_current_value


def sell_today(n_days, n_predictions):
    """Compares the current price to predicted prices and returns a boolean value
    to sell or not sell today."""
    predictions = model_arima(n_days, n_predictions)
    current_value = [float(get_current_value())]
    values = current_value + [value for value in predictions.predicted_value]

    # If today's price is the maximum value then return 1 to sell today
    if values[0] == max(values):
        return 1, predictions
    # If today's price is not the maximum value the return 0 to not sell today
    if values[0] != max(values):
        return 0, predictions

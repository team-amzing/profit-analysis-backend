"""
Using the predictions created in price_prediction.py the profit margin is analysed
for each prediction.
"""

from data_analysis.price_prediction import model_arima
from get_data.get_data import get_current_value


def sell_today(n_days, value, predictions):
    """Returns a boolean value for to indicate whether to sell today."""
    return value < max(predictions.predicted_value)


def get_predictions(model, n_days, n_predictions, url):
    """Returns the predictions from a given model and a comparison between the best predicted value and
    the current value."""
    predictions = model(n_days, n_predictions)
    current_value = get_current_value(url)
    return sell_today(n_days, current_value, predictions), predictions

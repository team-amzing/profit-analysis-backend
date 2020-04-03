"""
Using the predictions created in price_prediction.py the profit margin is analysed
for each prediction.
"""


def sell_today(value, predictions):
    """Returns a boolean value for to indicate whether to sell today."""
    return value > max(predictions.predicted_value)


def get_predictions(model, n_days, n_predictions, current_value):
    """Returns the predictions from a given model and a comparison between the best predicted value and
    the current value."""
    predictions = model(n_days, n_predictions, current_value)
    return sell_today(current_value, predictions), predictions

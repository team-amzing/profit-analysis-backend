"""
Using the data imported from quandl in get_data the price is predicted
with errors for the next five days, in increments of days.
"""

from datetime import datetime
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA

from get_data.get_data import call_api, get_current_value


def model_arima(n_days, n_predictions):
    """Returns an array of predicted prices for given number of days using
    Quandl API data."""

    data = call_api(n_days)
    df = pd.DataFrame(data)
    model = ARIMA(df[["Value"]], order=(1, 1, 1))
    fitted = model.fit(disp=0)

    # Forecast, standard error, confidence region for a confidence of 95%
    forecast, error, conf = fitted.forecast(n_predictions, alpha=0.05)
    return pd.DataFrame(
        data={
            "date": df.Date[:n_predictions],
            "predicted_value": forecast,
            "error": error,
        }
    )

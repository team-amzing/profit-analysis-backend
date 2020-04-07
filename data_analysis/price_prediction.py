"""
Using the data imported from quandl in get_data the price is predicted
with errors for the next five days, in increments of days.
"""

from datetime import datetime, timedelta
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA

from get_data.get_data import call_api


def model_arima(n_days, n_predictions, current_value):
    """Returns an array of predicted prices for given number of days using
    Quandl API data."""

    data = call_api(n_days)
    df = pd.DataFrame(data)

    # If last date in data frame is not current date append
    # data frame with current date and price
    current_time = datetime.now()
    if current_time.date() > df.Date.iloc[-1].date():
        df = df.append(
            {"Date": current_time, "Value": current_value}, ignore_index=True
            )
    model = ARIMA(df[["Value"]], order=(1, 1, 1))
    fitted = model.fit(disp=0)

    # Forecast, standard error, confidence region for a confidence of 95%
    forecast, error, conf = fitted.forecast(n_predictions, alpha=0.05)

    dates = [current_time.date() + timedelta(days=day) for day in range(1, n_predictions + 1)]

    return pd.DataFrame(
        data={
            "date": dates,
            "predicted_value": forecast,
            "error": error,
        }
    )

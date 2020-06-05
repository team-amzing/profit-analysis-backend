"""
Using the data imported from quandl in get_data the price is predicted
with errors for the next five days, in increments of days.
"""
 
from datetime import datetime, date, time, timedelta
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
from get_data.import_data import call_macro
import numpy as np
from fbprophet import Prophet
from pandas import read_csv
import matplotlib.pyplot as plt
file = open('./get_data/macrotrends_data.csv', 'r')
 
def model_prophet(n_days, n_predictions, current_value):
    """Returns an array of predicted prices for given number of days using
    Quandl API data."""
    data = call_macro(0,file)
    df = pd.DataFrame(data)
    d = {'ds':df.date, 'y':df.value}
    df_pred = pd.DataFrame(data=d)

    holidaysUS = pd.DataFrame(pd.DataFrame({
    'holiday': 'USHoliday',
    'ds': pd.to_datetime(['2020-01-01', '2020-01-20', '2020-02-17',
                          '2020-04-10', '2020-05-25', '2020-09-07',
                          '2020-10-12', '2020-11-11', '2020-11-26',
                          '2020-11-27', '2020-12-24', '2020-12-25',
                          '2020-12-31', '2021-01-01']),
                          'lower_window': 0,
                          'upper_window': 1,}))

    model = Prophet(holidays=holidaysUS, daily_seasonality=False).fit(df_pred)
    
    future = model.make_future_dataframe(periods=365)
    forecast = model.predict(future)

    #Less than or equal to current day + n_predictions
    tomorrows_date = (datetime.now() + timedelta(days=1))
    max_dates = (tomorrows_date + timedelta(days=30))
    forecast = forecast[(forecast['ds'] > tomorrows_date) & (forecast['ds'] <= max_dates)]
    next_20_values = forecast
    for date in next_20_values['ds']:
        week_no = date.weekday()
        if(week_no >= 5):
            i = next_20_values[(next_20_values.ds == date)].index
            next_20_values = next_20_values.drop(i)

    #error = next_20_values.yhat_upper.head(n_predictions) - next_20_values.yhat_lower.head(n_predictions)
    #N_predictions(R) = Returned
    n_predictionsR = next_20_values.head(n_predictions)
    dates = n_predictionsR.ds.tolist()
    values = n_predictionsR.yhat.tolist()
    error_upper = n_predictionsR.yhat_upper.tolist()
    error_lower = n_predictionsR.yhat_lower.tolist()

    return pd.DataFrame(
        data={
            "date": dates,
            "predicted_value": values,
            "error_upper": error_upper,
            "error_lower": error_lower,
        }
    )

def model_arima(n_days, n_predictions, current_value):
    """Returns an array of predicted prices for given number of days using
    Quandl API data."""

    data = call_macro(n_days, file)
    df = pd.DataFrame(data)

    current_time = datetime.now()
    model = ARIMA(df["value"], order=(1, 1, 1))
    fitted = model.fit(disp=0)

    # Forecast, standard error, confidence region for a confidence of 95%
    forecast, error, conf = fitted.forecast(n_predictions, alpha=0.05)
    
    dates = [current_time + timedelta(days=day) for day in range(1, n_predictions + 1)]
    
    return pd.DataFrame(
        data={
            "date": dates,
            "predicted_value": forecast,
            "error": error,
        }
    )
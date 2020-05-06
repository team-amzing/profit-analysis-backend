"""
Using the data imported from quandl in get_data the price is predicted
with errors for the next five days, in increments of days.
"""

from datetime import datetime, timedelta
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
#import sys
#import os
#sys.path.append(os.path.abspath('../get_data'))
from get_data.importData import call_macro
#from get_data.get_data import call_api

file = open('./get_data/macrotrends_data.csv', 'r')

def model_arima(n_days, n_predictions, current_value):
    """Returns an array of predicted prices for given number of days using
    Quandl API data."""

    data = call_macro(n_days, file)
    #data = call_api(n_days)
    df = pd.DataFrame(data)

    # If last date in data frame is not current date append
    # data frame with current date and price
    current_time = datetime.now()
    #current_time_string = current_time.strftime('%d/%m/%Y')
    #current_time_formatted = datetime.strptime(current_time_string, '%d/%m/%Y')
    #last_date_on_csv_formatted = datetime.strptime(df['date'].iloc[-1], '%d/%m/%Y')
    #if current_time_formatted > last_date_on_csv_formatted:
    #    df = df.append(
    #        {"date": current_time, "value": current_value}, ignore_index=True
    #        )
    #print ("This is what the fuck df is: ", df[['date', 'value']])
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

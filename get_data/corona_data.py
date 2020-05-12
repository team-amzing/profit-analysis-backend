from datetime import date
import pandas as pd
import requests
import os
from get_data.import_data import call_macro
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(THIS_FOLDER, 'macrotrends_data.csv')


# Date from the day before the outbreak in italy
def get_days():
    outbreak_date = date(2020, 2, 21)
    today = date.today()
    return (today - outbreak_date).days


def corona_data(days):
  """Collect prices and normalise to see the overall effect on the stock"""
  histprices = call_macro(days, file)
  df = pd.DataFrame(histprices)
  dfs = [df.set_index("date")]
  outbreak_value = df.iloc[0]["value"]
  histprice_normalised = pd.concat(dfs, axis=1)
  histprice_normalised = (histprice_normalised / histprice_normalised.iloc[0])
  return histprice_normalised, outbreak_value

from datetime import date
import pandas as pd
import requests

from get_data.get_data import call_api

# Date from the day before the outbreak in italy
def get_days():
    outbreakDate = date(2020, 2, 21)
    today = date.today()
    return (today - outbreakDate).days


def coronaData(days):
  """Collect prices and normalise to see the overall effect on the stock"""
  histprices = call_api(days)
  df = pd.DataFrame(histprices)
  dfs = [df.set_index("Date")]
  histpriceNormalised = pd.concat(dfs, axis=1)
  return histpriceNormalised / histpriceNormalised.iloc[0], histpriceNormalised.iloc[0]


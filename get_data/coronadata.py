from datetime import date
import pandas as pd
import requests

from get_data.get_data import call_api

# Date from the day before the outbreak in italy
outbreakDate = date(2020, 2, 21)
today = date.today()
days = (today - outbreakDate).days

# Collect prices and normalise to see the overall effect on the stock
def coronaData(days):
  histprices = call_api(days)
  df = pd.DataFrame(histprices)
  dfs = [df.set_index("Date")]
  histpriceNormalised = pd.concat(dfs, axis=1)
  return histpriceNormalised = histpriceNormalised / histpriceNormalised.iloc[0]


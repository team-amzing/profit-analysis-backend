from datetime import date
import pandas as pd
import requests
import os
from importData import call_macro
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(THIS_FOLDER, 'macrotrends_data.csv')


# Date from the day before the outbreak in italy
def get_days():
    outbreakDate = date(2020, 2, 21)
    today = date.today()
    return (today - outbreakDate).days


def coronaData(days):
  """Collect prices and normalise to see the overall effect on the stock"""
  histprices = call_macro(days, file)
  df = pd.DataFrame(histprices)
  dfs = [df.set_index("Date")]
  histpriceNormalised = pd.concat(dfs, axis=1)

  histpriceNormalised = (histpriceNormalised / histpriceNormalised.iloc[0])
  print (histpriceNormalised)
  return histpriceNormalised

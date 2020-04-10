from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
import csv
import requests
from get_data import get_current_value
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(THIS_FOLDER, 'macrotrends_data.csv')
URL = "https://markets.businessinsider.com/commodities/oil-price?type=wti"

def addTodaysDateToMacrotrends(file):
    df = pd.read_csv(file)
    today = date.today()
    colNames = df.columns
    #dd/mm/YY
    todays_date = today.strftime("%d/%m/%Y")
    todays_price = get_current_value(URL)
    newData = [[todays_date, todays_price]]
    df_new = pd.DataFrame(data=newData, columns=colNames)

    #concatenate old and new csv
    df_complete = pd.concat([df, df_new], axis = 0)
    df_complete.to_csv(file, index=False)

def call_macro(n_days, file):
    """Calls the API using the given API key, and returns the last n_days worth
    of WTI oil price data."""
    df = pd.read_csv(file)
    return df.iloc[-n_days:]

# def get_current_value():
#     """Webscraper to return the current market value for WTI oil."""

#     page = requests.get(
#         "https://markets.businessinsider.com/commodities/oil-price?type=wti"
#     )
#     soup = BeautifulSoup(page.text, "html.parser")
#     current_prices = soup.find(class_="push-data")
#     return float(str(current_prices.next))

#addTodaysDateToMacrotrends(file)

#print (call_macro(5, file))

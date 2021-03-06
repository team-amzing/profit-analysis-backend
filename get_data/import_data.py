from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
from datetime import datetime
import csv
import requests
from get_data.get_data import get_current_value
URL = "https://markets.businessinsider.com/commodities/oil-price?type=wti"

def addTodaysDateToMacrotrends(file):
    df = pd.read_csv(file)
    today = date.today()
    colNames = df.columns
    time = datetime.now()
    #dd/mm/YY
    todays_date = today.strftime("%d/%m/%Y")
    current_time = time.strftime("%H:%M:%S")
    current_time_to_int = int(current_time[:2])
    lastRowOnCSV = (df.tail(1)['date']).to_string(index=False).strip()
    #Failsafe 1: Only update the data after closing time (6pm)
    if current_time_to_int >= 18:
        #Failsafe 2: Only update the data if the data does not already exist on the csv.
        if todays_date != lastRowOnCSV:
            todays_price = get_current_value(URL)
            newData = [[todays_date, todays_price]]
            df_new = pd.DataFrame(data=newData, columns=colNames)
            #concatenate old and new csv
            df_complete = pd.concat([df, df_new], axis = 0)
            df_complete.to_csv(file, index=False)
            print ("New data has been added to macrotrends_data.csv.")
        else:
            print ("Todays data has already been added. Data will not be updated.")
    else:
        print ("The current time is before the closing time, data will not be added.")

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

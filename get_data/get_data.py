"""
WIT oil price data is acquired from the Quandl API for use by the data_analysis module.
"""

import requests
import quandl

from bs4 import BeautifulSoup

# API key for Michael's account
API_KEY = "NszGhwY_Qh8Ubj1BWhVt"

# TODO: Create team API key and move API_KEY to constants file


def call_api(n_days):
    """Calls the API using the given API key, and returns the last n_days worth
    of WTI oil price data."""

    # Declare Quandl API key
    quandl.ApiConfig.api_key = API_KEY

    # Get data from the quandl api, then only return the number of days asked for
    data = quandl.get("EIA/PET_RWTC_D", returns="numpy")
    return data[-n_days:]


def get_current_value():
    """Webscraper to return the current market value for WTI oil."""

    page = requests.get(
        "https://markets.businessinsider.com/commodities/oil-price?type=wti"
    )
    soup = BeautifulSoup(page.text, "html.parser")
    current_prices = soup.find(class_="push-data")
    return float(str(current_prices.next))

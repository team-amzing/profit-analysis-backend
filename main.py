"""Script to run the ARIMA analysis and calculate a given number of predictions
and the profit margin for that day, exported as a .npy file."""
import sys
import os
from numpy import save
from datetime import date
from data_analysis.price_prediction import model_arima
from data_analysis.profit_analysis import get_predictions
from get_data.get_data import get_current_value
from get_data.import_data import addTodaysDateToMacrotrends

#This is the csv file that the oil data will be stored in
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(THIS_FOLDER, 'get_data/macrotrends_data.csv')

#Add todays oil price data to the csv
addTodaysDateToMacrotrends(file)

from datetime import date

from data_analysis.price_prediction import model_arima
from data_analysis.profit_analysis import get_predictions
from get_data.get_data import get_current_value
from get_data.graphs_for_server import plot_to_file

# Model choice for analysis
MODEL = model_arima

# Constants for model parameters
TRAINING_DAYS = 2000
PREDICTED_DAYS = 9

# Constants for vessel information
UNITS = 750000
COST = 30000

# URL for scraping the current value
URL = "https://markets.businessinsider.com/commodities/oil-price?type=wti"

# Current value of oil
VALUE = get_current_value(URL)

date_today = date.today()

sell_today, predictions = get_predictions(MODEL, TRAINING_DAYS, PREDICTED_DAYS, VALUE, UNITS, COST)

# Generate a plot and table for the server
plot_to_file("projection", predictions, sell_today, VALUE, PREDICTED_DAYS)

html_string = f"""
    <h1>WTI Oil Price Prediction for {date_today}</h1>
    <h2>Oil price today: {VALUE}</h2>
    {predictions.to_html()}
    <h2>Should you sell today? {sell_today}</h2>
    <img src="projection.svg" height="500" width ="265" alt="Projection plot missing" >
"""

with open("index.html", "w") as file:
    file.write(html_string)

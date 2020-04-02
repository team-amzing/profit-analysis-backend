"""Script to run the ARIMA analysis and calculate a given number of predictions
and the profit margin for that day, exported as a .npy file."""

from numpy import save

from data_analysis.price_prediction import model_arima
from data_analysis.profit_analysis import get_predictions


# Model choice for analysis
MODEL = model_arima

# Constants for model parameters
TRAINING_DAYS = 2000
PREDICTED_DAYS = 7

# URL for scraping the current value
URL = "https://markets.businessinsider.com/commodities/oil-price?type=wti"

sell_today, predictions = get_predictions(MODEL, TRAINING_DAYS, PREDICTED_DAYS, URL)

# Save boolean value to numpy file
save("sell_today.npy", sell_today)

# Save data frame as pickle file
predictions.to_pickle("./predictions.pkl")

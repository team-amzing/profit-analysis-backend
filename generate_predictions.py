"""Script to run the ARIMA analysis and calculate a given number of predictions
and the profit margin for that day, exported as a .npy file."""

from numpy import save

from data_analysis.profit_analysis import calculate_profit_margin


# Constants for information on the Tanker
OIL_STOCK = 750000
TANKER_DAILY_COSTS = 30000

# Constants for ARIMA parameters
TRAINING_DAYS = 2000
PREDICTED_DAYS = 7

predictions = calculate_profit_margin(
    TRAINING_DAYS, PREDICTED_DAYS, OIL_STOCK, TANKER_DAILY_COSTS
)

# Save data frame as pickle file
predictions.to_pickle("./predictions.pkl")

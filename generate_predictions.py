"""Script to run the ARIMA analysis and calculate a given number of predictions
and the profit margin for that day, exported as a .npy file."""

from numpy import save

from data_analysis.profit_analysis import sell_today

# Constants for ARIMA parameters
TRAINING_DAYS = 2000
PREDICTED_DAYS = 7

sell_today, predictions = sell_today(TRAINING_DAYS, PREDICTED_DAYS)

# Save boolean value to numpy file
save("sell_today.npy", sell_today)

# Save data frame as pickle file
predictions.to_pickle("./predictions.pkl")

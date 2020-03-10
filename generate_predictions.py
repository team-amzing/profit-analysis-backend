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
predictions_array = predictions.to_numpy()

# Save numpy array to file
save("predictions.npy", predictions_array)

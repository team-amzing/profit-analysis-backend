import matplotlib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def plot_to_file(filename, predictions, sell_today, todays_price, n_predictions):
    """
    Reads a pandas dataframe with all dates as datetime objects(!), and returns an .png
    that contains the predicted values for the next few days, along with the profit
    one can expect if one waited until that day (as costs go up daily).
    filename does not need to contain the .png file extension.
    """
    # Read in files
    SERVER_URL = "http://35.204.193.240/"

    # Window setup
    tomorrows_price = predictions["predicted_value"][1]
    difference = str(tomorrows_price - todays_price)

    # Calculate axis labels
    date_strings = [[]] * n_predictions
    gross_labels = []
    profit_labels = []
    colours = (
        []
    )  # Uses red and green to indicate if a day is predicted to be a profit or loss
    for index in range(n_predictions):
        date_strings[index] = (
            pd.to_datetime(predictions["date"].values[index]).strftime("%m-%d")
            #predictions["date"][index].strftime("%m-%d")
        )  # Took %Y, year, out
        gross_labels.append(f'{predictions["predicted_value"].values[index]:.2f}')

    font = {"family": "serif", "weight": "normal", "size": 12}

    matplotlib.rc("font", **font)

    ## Formatting

    pix_per_inch = 96  # Number of pixels per inch to create the figure size
    fig = plt.figure(
        figsize=(380 / pix_per_inch, 200 / pix_per_inch)
    )  # This takes inches as arguements
    ax1 = fig.add_subplot(111)  # This just allows more freedom using ax. not plt.
    plt.subplots_adjust(
        left=0.22, bottom=0.3
    )  # Add extra room to ensure graph fits fine
    ax1.set_xticks(np.arange(0, n_predictions))
    ax1.set_xticklabels(date_strings, rotation=45, ha="right", rotation_mode="anchor")
    plt.suptitle("Next week's outlook")
    ax1.set_ylabel("USD", rotation=90, ha="right", rotation_mode="anchor")
    plt.grid()
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    # Annotate each point with the profit you'd make right now compared to waiting for this day
    x = np.arange(0, n_predictions)
    y = predictions["predicted_value"].values

    ## Adding values
    ax1.plot(x, y, color="black", linewidth=3)
    plt.savefig(f"{filename}.png", format="png")

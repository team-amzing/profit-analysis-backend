import numpy as np
from scipy.optimize import least_squares

from get_data.coronadata import get_days, corona_data

# Get data
days = get_days()
data, outbreak_value = corona_data(days)
outbreak_value = float(outbreak_value)
data_value = list(data["Value"])


def generate_data(t, A, sigma, omega, noise=0, n_outliers=0, random_state=0):
    """ Generates data for the regression """
    y = A * np.exp(-sigma * t) * np.sin(omega * t)
    rnd = np.random.RandomState(random_state)
    error = noise * rnd.randn(t.size)
    outliers = rnd.randint(0, t.size, n_outliers)
    error[outliers] *= 35
    return y + error


def fun(x, t, y):
    """ function for computing residuals for least square minimiation"""
    return x[0] * np.exp(-x[1] * t) * np.sin(x[2] * t) - y


def covid_pred(days, data_value, outbreakValue):
    """ Creates a nonlinear regression and outputs a prediction for the next day """
    x_train = np.linspace(0, days, days)
    x_reg = np.linspace(0, days + 1, 300)
    x0 = np.ones(3)  # inital estimate
    res = least_squares(
        fun, x0, loss="soft_l1", f_scale=0.1, args=(x_train, data_value)
    )
    y_reg = generate_data(x_reg, *res.x)  # prediction
    return y_reg[-1] * outbreak_value

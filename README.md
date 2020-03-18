# profit-analysis-backend
This repo contains the data analysis for WIT intermediate oil prices using the ARIMA time series analysis model. It generates compressed files containing the predicted data and assessed boolean value for whether to sell today.

## Installation
Once you have cloned down this repository using `git clone` cd into the app directory eg.

```
cd profit-analysis-backend
```

The project uses pipenv to manage project and development packages. To install these requirements run

```
pipenv install --dev
```

To initialise the virtual environment run

```
pipenv shell
```

To exit the virtual environment use `exit` and to see where you virtual environment is located run
`pipenv --venv` which may be useful when setting up your project interpreter in your IDE.

This project used the black auto formatter which can be run on git commit along with flake8 if you install pre-commit. To do this run the following in your terminal from within your virtual environment.

```
pre-commit install
```

Now pre-commit hooks should run on `git commit`.

## Running the analysis
This app downloads time series data from the Quandl API and performs ARIMA analysis upon this data. Run the following code in your terminal to run the analysis from a Linux/Mac distribution. This will generate a pickle file that contains the predictions for the given days and a numpy file that contains a boolean for if to sell today

```bash
python -m generate_predictions
```

If you are using Windows you will need to run

```bash
python -m generate_predictions.py
```

# profit-analysis-backend
This repo contains the data analysis for WIT intermediate oil prices(USD) using the ARIMA time series analysis model. It generates compressed files containing the predicted data and assessed boolean value for whether to sell today.

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
This app downloads time series data from the Quandl API and performs ARIMA analysis upon this data. Run the following code in your terminal to run the analysis. This will generate a pickle file that contains the predictions for the given days and a numpy file that contains a boolean for if to sell today

```bash
python main.py
```

## Docker
The above steps can be carried out with the docker-compose setup, which will also run a local server. This local server can be found at "localhost" once the containers are running.

The docker-compose setup consists of a Python and an NGINX container with a mounted volume `code`. To build the image and run the image, run the following:

```bash
docker-compose up --build
```

Once your container is built, you will be able to run it more quickly using:

```bash
docker-compose up
```

You can use `Ctrl C` to cancel out of the containers. Use `docker ps` to see which containers are running and to go into a container use the following command:

```bash
docker exec -it <container-name> bash
```

Be sure to have run `docker-compose up` before running this command as you will not be able to enter a container if it not active.

#!/bin/bash
pipenv install
p=$(pipenv --venv)
source "$p/bin/activate"
python -m generate_predictions

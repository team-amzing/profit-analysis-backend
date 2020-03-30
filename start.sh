#!/bin/bash

#loop forever
while [ "0" = "0" ] ; do
  python /code/generate_predictions.py
  sleep 3600

done


#!/bin/bash

nginx

#loop forever
while [ "0" = "0" ] ; do

    cp /code/predictions.pkl /usr/share/nginx/html/
    cp /code/sell_today.npy /usr/share/nginx/html/
    sleep 60

done

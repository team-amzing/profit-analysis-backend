#!/bin/bash

nginx

#loop forever
while [ "0" = "0" ] ; do
    RESULT=$(cat /code/sell_today.txt)

    echo "Should you sell today? $RESULT" > /usr/share/nginx/html/index.html
    sleep 60

done

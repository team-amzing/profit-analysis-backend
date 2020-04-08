#!/bin/bash

nginx

#loop forever
while [ "0" = "0" ] ; do
    rm /usr/share/nginx/html/index.html
    cp /code/index.html /usr/share/nginx/html/.
    sleep 60

done

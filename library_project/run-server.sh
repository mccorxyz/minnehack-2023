#!/bin/bash

#python3 manage.py migrate
#python3 manage.py makemigrations
#python3 manage.py runserver 0.0.0.0:80
python3 manage.py runserver_plus 0.0.0.0:443 --cert-file /etc/l#python3 manage.py runserver_plus 0.0.0.0:443etsencrypt/live/cknutson.org/cert.pem --key-file /etc/letsencrypt/live/cknutson.org/key.pem

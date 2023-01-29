#!/bin/bash

docker run -d --name=bookend -v bookendDB:/app --rm -p 8080:80 rogueraptor7/bookend:latest
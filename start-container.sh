#!/bin/bash

docker run -d --name=bookend --privileged -v bookendDB:/app --rm -p 80:80 rogueraptor7/bookend:latest
#!/bin/bash

docker run -d --name=bookend --privileged -v "${PWD}"/library_project/db.sqlite3:/app/db.sqlite3:rw --rm -p 80:80 rogueraptor7/bookend:latest
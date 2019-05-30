#!/bin/sh

gunicorn --reload --bind 127.0.0.1:8800 --access-logfile - githook:app

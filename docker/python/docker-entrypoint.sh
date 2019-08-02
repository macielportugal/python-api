#!/bin/sh
cd /srv/http/app
export APP_CONFIG_FILE=config/development.py
export FLASK_DEBUG=1
export FLASK_APP=routes.py
flask run --host=0.0.0.0
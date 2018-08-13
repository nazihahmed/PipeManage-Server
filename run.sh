#!/bin/bash
. venv/bin/activate
python3 -m pip install -r requirements.txt
python3 app.py | tee dev_app.log

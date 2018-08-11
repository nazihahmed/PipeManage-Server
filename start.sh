#!/bin/bash
pushd /opt/intel
    . venv/bin/activate
    python3 app.py > /home/pi/Desktop/app.log 2>&1
popd

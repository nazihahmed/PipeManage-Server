#!/bin/bash
bash kill.sh
pushd /opt/intel
    . venv/bin/activate
    python3 app.py &> python_app.log &
popd

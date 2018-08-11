#!/bin/bash
pushd /opt/intel
    . venv/bin/activate
    python3 app.py > /opt/intel/app.log 2>&1
popd

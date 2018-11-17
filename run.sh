#!/bin/bash
. venv/bin/activate
python3 -m pip install -r requirements.txt
pushd /opt/intel/intel-manage-secrets
  bash ./generateCerts.sh
popd
python3 app.py | tee dev_app.log

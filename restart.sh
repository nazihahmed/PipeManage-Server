#!/bin/bash
sudo kill $(ps aux | grep 'bin/[p]ython3 app.py' | awk '{print $2}')
bash /opt/intel/start.sh &

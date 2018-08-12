#!/bin/bash
ps aux | grep 'bin/[p]ython3 app.py' | awk '{print $2}'

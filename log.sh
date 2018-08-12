tailf /proc/$(ps aux | grep 'bin/[p]ython3 app.py' | awk '{print $2}')/fd/1

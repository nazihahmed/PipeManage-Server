# PipeManage Server

## Requirements
  - [Python 3.7.0](https://www.python.org/downloads/release/python-370/)

## How to run
1. run the init bash script
```bash
bash init.sh
```
2. run the app
```bash
python3 app.py
```
4. navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## How to add new packages
- make sure to have a venv with all the packages from `requirements.txt`
- install the new package using pip
```bash
pip install <package>
```
- freeze pip and save all the packages to `requirements.txt` using:
```bash
pip freeze > requirements.txt
```
- checkout the changes with `git diff` and make sure that it's correct

## Find out Raspberry pi IP address
```
hostname -I
```

## Reference
![Raspberry pi 3 B+ pinout](https://www.jameco.com/Jameco/workshop/circuitnotes/raspberry_pi_circuit_note_fig2a.jpg)
![Liquid sensor pinout](http://www.icstation.com/images/uploads/liquid%20level%20sensor_12292_2.jpg)

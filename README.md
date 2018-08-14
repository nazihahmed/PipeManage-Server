# Intel Pipe-manage project

## Requirements
  - [Python 3.7.0](https://www.python.org/downloads/release/python-370/)

## How to run
1. create a venv (virtual environment) and activate it
```bash
python3 -m venv venv
. venv/bin/activate
```
2. install required packages
```bash
python3 -m pip install -r requirements.txt
```
3. run the app
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
![Liquid sensor pinout](https://uc0c5413aef038413ae99ebeba93.previews.dropboxusercontent.com/p/thumb/AAKT3Mn19kXgB1k_sNhzt80qTz7Zwusfla6IWcnbN4B19vDaDqUJZIF8t1PXKuH9OqTNvbuXcyOGztvz3Gp0pgwyoZX1_-0put0OtyhHtvwwjLBtE9BDVeM1hZzU8rfYj2hEtG3EofKiOn7smP5BOh_8FRyK_VQRg7n3su-m9zztcHlEW4qPWkKvA9j6lWBYdOYP8Y7nxQjyUeOTfYgE8i6qbQMUEmydUzNm6cS6gwph6A/p.png?size_mode=5)

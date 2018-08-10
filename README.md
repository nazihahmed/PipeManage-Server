# Intel Pipe-manage project

## requirements
  - [Python 3.7.0](https://www.python.org/downloads/release/python-370/)

## How to run
1. create a venv (virtual environment) and activate it
  - `python3 -m venv venv`
  - `. venv/bin/activate`
2. install required packages
  - `python3 -m pip install -r requirements.txt`
3. run the app
  - `python3 app.py`
4. navigate to `http://127.0.0.1:5000/`

## How to add new packages
- make sure to have a venv with all the packages from `requirements.txt`
- install the new package using pip
  - `pip install <package>`
- freeze pip and save all the packages to `requirements.txt` using:
  - `pip freeze >> requirements.txt`
- checkout the changes with `git diff` and make sure that it's correct

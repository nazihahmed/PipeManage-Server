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
pip freeze >> requirements.txt
```
- checkout the changes with `git diff` and make sure that it's correct

## Find out Raspberry pi IP address
```
hostname -I
```

## Reference
![Raspberry pi 3 B+ pinout](https://www.jameco.com/Jameco/workshop/circuitnotes/raspberry_pi_circuit_note_fig2a.jpg)
![Liquid sensor pinout](https://previews.dropbox.com/p/thumb/AAJrzSNGy4Bn2uSou0sZH6CbO84m9r0OT-Pu3EBKrFHlFZWEh0u4-nET_qdq1ouBbqmmayg7nY1TWIgUN-OOysQHMdQBQ8sYsXyQEGh1uFKI0Ai6EVwA0fOu5q2osg0ofsLGe41obpLvVZSpnd8z-s2JPrKfvwiyXwxixL2a1UY--JaS8wZvCjgM1xRFshybxTo5MEgcZiZbeQYP4LCROc-kSUsBQe6LgBXgRuGJhG8D5A/p.png?size=800x600&size_mode=3)

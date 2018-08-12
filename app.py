from flask import Flask, render_template
import datetime
import RPi.GPIO as GPIO
from flask_socketio import SocketIO
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
#
# app.config['SECRET_KEY'] = 'secret!'
# # socketio = SocketIO(app)
# GPIO.setmode(GPIO.BCM)
#
#
# # 6 sensors as input
#
# inputPins = {
#    15 : {'name' : 'sensor 1'},
#    17 : {'name' : 'sensor 2'},
#    18 : {'name' : 'sensor 3'},
#    27 : {'name' : 'sensor 4'},
#    23 : {'name' : 'sensor 5'},
#    22 : {'name' : 'sensor 6'},
# }
#
# # 6 relays as output
#
# outputPins = {
#    24 : {'name' : 'relay 1'},
#    10 : {'name' : 'relay 2'},
#    9  : {'name' : 'relay 3'},
#    25 : {'name' : 'relay 4'},
#    11 : {'name' : 'relay 5'},
#    8  : {'name' : 'relay 6'},
# }
#
# for pin in outputPins:
#    GPIO.setup(pin, GPIO.OUT)
#    GPIO.output(pin, GPIO.LOW)
#
# for pin in inputPins:
#    GPIO.setup(pin, GPIO.IN)
#
# def updateInputStatus():
#     for pin in inputPins:
#        inputPins[pin]['state'] = GPIO.input(pin)
#
# @app.route('/')
# def index():
#
#     return render_template('index.html')
#
# # @socketio.on('message')
# # def handle_message(message):
# #     print('received message: ' + message)
# #
# # @socketio.on('json')
# # def handle_json(json):
# #     print('received json1: ' + str(json))
# #
# # @socketio.on('my event')
# # def handle_my_custom_event(json):
# #     print('received json: ' + str(json))
#
# @app.route('/main')
# def hello2():
#    now = datetime.datetime.now()
#    timeString = now.strftime("%Y-%m-%d %H:%M")
#    templateData = {
#       'title' : 'HELLO!',
#       'time': timeString
#       }
#    return render_template('main.html', **templateData)
#
# @app.route("/pin/<pin>")
# def readPin(pin):
#    try:
#       GPIO.setup(int(pin), GPIO.IN)
#       if GPIO.input(int(pin)) == True:
#          response = "Pin number " + pin + " is high!"
#       else:
#          response = "Pin number " + pin + " is low!"
#    except:
#       response = "There was an error reading pin " + pin + "."
#
#    templateData = {
#       'title' : 'Status of Pin' + pin,
#       'response' : response
#       }
#
#    return render_template('pin.html', **templateData)
#
# @app.route('/hello/<name>')
# def hello(name):
#     return render_template('page.html', name=name)
#
# @app.route("/control")
# def control():
#    # For each pin, read the pin state and store it in the pins dictionary:
#
#    # Put the pin dictionary into the template data dictionary:
#    templateData = {
#       'pins' : pins
#       }
#    # Pass the template data into the template main.html and return it to the user
#    return render_template('control.html', **templateData)
#
# @app.route("/update")
# def update():
#    subprocess.call("./update.sh")
#    return render_template('indel.html')
#
# # The function below is executed when someone requests a URL with the pin number and action in it:
# @app.route("/<changePin>/<action>")
# def action(changePin, action):
#    # Convert the pin from the URL into an integer:
#    changePin = int(changePin)
#    # Get the device name for the pin being changed:
#    deviceName = pins[changePin]['name']
#    # If the action part of the URL is "on," execute the code indented below:
#    if action == "on":
#       # Set the pin high:
#       GPIO.output(changePin, GPIO.HIGH)
#       # Save the status message to be passed into the template:
#       message = "Turned " + deviceName + " on."
#    if action == "off":
#       GPIO.output(changePin, GPIO.LOW)
#       message = "Turned " + deviceName + " off."
#    if action == "toggle":
#       # Read the pin and set it to whatever it isn't (that is, toggle it):
#       GPIO.output(changePin, not GPIO.input(changePin))
#       message = "Toggled " + deviceName + "."
#
#    # For each pin, read the pin state and store it in the pins dictionary:
#    for pin in pins:
#       pins[pin]['state'] = GPIO.input(pin)
#
#    # Along with the pin dictionary, put the message into the template data dictionary:
#    templateData = {
#       'message' : message,
#       'pins' : pins
#    }
#
#    return render_template('control.html', **templateData)
#

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

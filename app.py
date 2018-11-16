from flask import Flask, render_template, jsonify, request
# import eventlet
import time
import RPi.GPIO as GPIO
import boto3
import os
import json
import logging
import atexit
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient

certs = {
    'keyPath': 'certs/deviceCert.key',
    'certPath': 'certs/deviceCert.crt',
    'caPath': 'certs/root.pem',
    'host': 'a2s7dpv6qj1qss.iot.us-west-2.amazonaws.com'
};

client = boto3.client(
    'dynamodb',
    aws_access_key_id='AKIAIMECMFPF5LJCOCSQ',
    aws_secret_access_key='TEwasPgZoUuKC5Yp3YfFdCLwVVxgvJ2UjMAtnIwT',
    region_name='us-west-2'
)

now = int(str(time.time())[0:14].replace('.','')) # datetime.datetime.now()

print("current timestamp",now, flush=True)

# configuration
DEBUG = True

# logger = logging.getLogger("AWSIoTPythonSDK.core")
# logger.setLevel(logging.DEBUG)
# streamHandler = logging.StreamHandler()
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# streamHandler.setFormatter(formatter)
# logger.addHandler(streamHandler)

fileDir = os.path.dirname(os.path.realpath('__file__'))
thingFileName = os.path.join(fileDir, 'certs/thingName.txt')
thingFile = open(thingFileName, 'r+')
thingName = ''
if os.stat(thingFileName).st_size == 0:
    response = client.scan(
        ExpressionAttributeValues={
            ':now': {
                'N': str(now - 10*60*1000),
            },
            ':later': {
                'N': str(now),
            }
        },
        ExpressionAttributeNames={
            '#t': 'timestamp'
        },
        FilterExpression='#t BETWEEN :now AND :later',
        TableName='autoDeviceRegistration'
    )

    sortedResponse = response['Items']
    sortedResponse.sort(key=lambda x:int(x['timestamp']['N']))
    # get latest item
    thing = sortedResponse[-1];
    thingName = thing['thingName']['S'];
    thingFile.write(thingName)
    thingFile.close()
else:
    thingName = thingFile.read()

print("we have thingName", flush=True)
print(thingName, flush=True)


myShadowClient = AWSIoTMQTTShadowClient(thingName)

# Configurations
myShadowClient.configureEndpoint(certs['host'], 8883)
myShadowClient.configureCredentials(certs['caPath'], certs['keyPath'], certs['certPath'])
myShadowClient.configureConnectDisconnectTimeout(10)  # 10 sec
myShadowClient.configureAutoReconnectBackoffTime(1, 32, 20)
myShadowClient.configureMQTTOperationTimeout(5)  # 5 sec

# try:
myShadowClient.connect()
# except:
#     print("coldn't connect to shadow, trying again in 5 seconds")
#     time.sleep(5)
#     myShadowClient.connect()


def customTopicCallback(client, userdata, message):
    print("Received a delta: ", flush=True)
    # print(message.payload, flush=True)
    data = json.loads(message.payload)
    if "state" in data:
        updateOutputsStatus(data["state"])
    # print("from topic: ", flush=True)
    # print(message.topic, flush=True)
    # print("--------------\n\n", flush=True)

def updateDesiredState(desired):
    state = {
        'state': {
                'desired':desired
                }
    }
    myDeviceShadow.shadowUpdate(json.dumps(state), customCallback, 5)

def updateReportedState(reported):
    state = {
        'state': {
                'reported':reported
                }
    }
    myDeviceShadow.shadowUpdate(json.dumps(state), customCallback, 5)

def customCallback(response,status,token):
    pass
    # print("\ngot response", flush=True)
    # print("""response,'\n-------------\n',"""status,'\n-------------\n',token, flush=True)
    # print("--------------\n\n", flush=True)

# Create a device shadow instance using persistent subscription
myDeviceShadow = myShadowClient.createShadowHandlerWithName(thingName, True)
shadowGetToken = myDeviceShadow.shadowGet(customCallback, 5)
myMQTTClient = myShadowClient.getMQTTConnection()
myMQTTClient.subscribe("$aws/things/" + thingName + "/shadow/update/delta", 1, customTopicCallback)
# myDeviceShadow.shadowUpdate(myJSONPayload, customCallback, 5)
# myDeviceShadow.shadowDelete(customCallback, 5)
# myDeviceShadow.shadowRegisterDeltaCallback(customCallback)
# myDeviceShadow.shadowUnregisterDeltaCallback()

def exit_handler():
    GPIO.cleanup()

atexit.register(exit_handler)

GPIO.setmode(GPIO.BCM)

# 6 sensors as input

inputPins = {
   4  : {'name' : 'sensor 1'},
   17 : {'name' : 'sensor 2'},
   18 : {'name' : 'sensor 3'},
   27 : {'name' : 'sensor 4'},
   23 : {'name' : 'sensor 5'},
   22 : {'name' : 'sensor 6'},
}

# 6 relays as output

outputPins = {
   16 : {'name' : 'relay 1', 'auto': 0},
   12 : {'name' : 'relay 2', 'auto': 0},
   19 : {'name' : 'relay 3', 'auto': 0},
   13 : {'name' : 'relay 4', 'auto': 0},
   6  : {'name' : 'relay 5', 'auto': 0},
   5  : {'name' : 'relay 6', 'auto': 0},
}

for pin in outputPins:
    print("setting up out pin",pin, flush=True)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

for pin in inputPins:
    print("setting up in pin",pin, flush=True)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def getInputPin(outputPin):
    inputPin = None
    for input, state in inputPins.tems():
        if state['name'][-1:] == outputPins[outputPin]['name'][-1:]:
            inputPin = input
            break
    return inputPin

def updateIOStatus():
    for pin in inputPins:
        inputPins[pin]['state'] = GPIO.input(pin)
    for out in outputPins:
        outputPins[out]['state'] = 1 if GPIO.input(out) == 0 else 0

def updateReportedIO():
    updated = {**inputPins, **outputPins}
    updateReportedState(updated)

def toggleAutomaticOutput(output, status):
    updateIOStatus()
    if status == True:
        outputPins[output]['auto'] = 1
    else:
        outputPins[output]['auto'] = 0

def updateOutputsStatus(outputs):
    print("updating outputs")
    for outputStr in outputs:
        output = int(outputStr)
        print("check output",outputs[outputStr], flush=True)
        if output in outputPins:
            if 'auto' in outputs[outputStr]:
                if outputs[outputStr]['auto'] == 0:
                    print("PIN", output, "AUTO OFF")
                    toggleAutomaticOutput(output, False)
                    # GPIO.output(output, GPIO.LOW)
                elif outputs[outputStr]['auto'] == 1:
                    print("PIN", output, "AUTO ON")
                    toggleAutomaticOutput(output, True)
                    # GPIO.output(output, GPIO.HIGH)
            if outputPins[output]['auto'] != 1:
                if outputs[outputStr]['state'] == 0:
                    print("PIN", output, "LOW")
                    GPIO.output(output, GPIO.HIGH)
                elif outputs[outputStr]['state'] == 1:
                    print("PIN", output, "HIGH")
                    GPIO.output(output, GPIO.LOW)
            cleanDesired = {}
            cleanDesired[output] = None
            updateDesiredState(cleanDesired)
    updateReportedIO()

def initPins():
    updateReportedIO()
    updateReportedState(outputPins)

initPins()

while True:
    updateIOStatus()
    for pin, state in outputPins.items():
        if state['auto'] == 1:
            inputPin = inputPins[getInputPin(pin)]
            if inputPin['state'] == 0 and state['state'] == 0:
                GPIO.output(pin, GPIO.HIGH)
            elif inputPin['state'] == 1:
                GPIO.output(pin, GPIO.LOW)
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        raise
    except:
        print("exiting")

# Webcam Bot
#
# Captures an image and sends the image as a base64 encoded string

import cv2, base64
import paho.mqtt.client as paho
import numpy as np
import toby

cap = cv2.VideoCapture(0)

webcam = toby.Bot("webcam", "webcam")

def on_disconnect():
    print "disconnected"

def on_connect():
    print "connected"
    webcam.follow(["webcam"], "followed")

def on_message(message):
    print message

    if ('message' in message.get_payload() and message.get_payload()['message'] == "cap"):
        ret, frame = cap.read()
        frame = cv2.resize(frame, (0,0), fx=0.4, fy=0.4)
        cnt = cv2.imencode('.png',frame)[1]
        b64 = base64.encodestring(cnt)
        png = str(b64).strip()
        webcam.send(toby.Message("", {"png": png}, ["png"], ''))

webcam.set_on_connect(on_connect)
webcam.set_on_disconnect(on_disconnect)
webcam.set_on_message(on_message)
webcam.start()

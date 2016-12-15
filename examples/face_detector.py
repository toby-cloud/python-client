# Face detector bot
#
# Detects all faces from images tagged with "png".
# It expects the message payload to have a "png" field with a
# Base64 encoded image
#

import time, cv2, base64
import paho.mqtt.client as paho
import numpy as np

import toby

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_detector = toby.Bot("face", "face")

def on_disconnect():
    print "disconnected"

def on_connect():
    print "connected"
    face_detector.follow(["png"], "followed")

def on_message(message):

    if 'png' in message.get_payload():
        print "received png"
        imgData = base64.b64decode(message.get_payload()["png"]);
        nparr = np.fromstring(imgData, np.uint8)
        frame = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=10,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        print str(len(faces)) + " faces detected"
        face_detector.send(toby.Message("", {"message": str(len(faces)) + " faces detected"}, ["face", "png"], ''))

        for (x,y,w,h) in faces:
            #cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),10) # frame faces
            frame[y:y+h, x:x+w] = np.flipud(frame[y:y+h, x:x+w]) # flip faces

        frame = cv2.resize(frame, (0,0), fx=.5, fy=.5) # reduce to half for faster encoding and sending
        cnt = cv2.imencode('.png',frame)[1]
        b64 = base64.encodestring(cnt)
        png = str(b64).strip()
        face_detector.send(toby.Message("", {"png": png}, ["face", "png"], ''))



face_detector.set_on_connect(on_connect)
face_detector.set_on_disconnect(on_disconnect)
face_detector.set_on_message(on_message)
face_detector.start()

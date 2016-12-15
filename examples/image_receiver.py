import time, cv2, base64
import paho.mqtt.client as paho
import numpy as np

import toby

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

webcam = toby.Bot("receive", "receive")

def on_disconnect():
    print "disconnected"

def on_connect():
    print "connected"
    webcam.follow(["png"], "followed")

def on_message(message):
    #print message

    if 'png' in message.get_payload():
        print "received png"
        imgData = base64.b64decode(message.payload["png"]);
        nparr = np.fromstring(imgData, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)
        frame = cv2.resize(img_np, (0,0), fx=.2, fy=.2)
        cv2.imwrite("toby-received-image.jpg", img_np)
        cv2.namedWindow("image", cv2.WINDOW_NORMAL)
        cv2.imshow("image", frame);
        cv2.waitKey(3)
        cv2.destroyAllWindows()

webcam.set_on_connect(on_connect)
webcam.set_on_disconnect(on_disconnect)
webcam.set_on_message(on_message)
webcam.start()

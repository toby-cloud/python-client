
import os, urlparse, time
import paho.mqtt.client as paho

class Toby:

    def __init__(self, botId, secret):
        self.botId = botId
        self.secret = secret
        self.sessionId = ""
        self.client = False
        self.on_message = False
        self.on_connect = False

    def set_on_connect (self, callback):
        self.on_connect = callback

    def set_on_message(self, callback):
        self.on_message = callback

    def follow(self, hashtag_string):
        if (not self.client):
            print "can't follow tags, no client"
            quit()
        self.client.publish("server/" + self.botId + "/subscribe", hashtag_string)

    def send(self, message):
        if (not self.client):
            print "can't send. no client"
            quit()
        self.client.publish("server/" + self.botId, message)

    def start(self):

        if (not self.on_message or not self.on_connect):
            print "set on_connect and on_message callbacks before starting"
            quit()

        def on_mqtt_connect(client, obj, rc):
            self.client = client
            self.client.subscribe("client/" + self.botId + "/#");
            self.on_connect();

        def on_mqtt_message(client, obj, msg):
            topic = str(msg.topic)
            message = str(msg.payload)
            topic_list = topic.split("/")

            self.on_message(message)


        def on_mqtt_publish(client, obj, mid):
            return

        def on_mqtt_subscribe(client, obj, mid, granted_qos):
            return

        mqttc = paho.Client()

        mqttc.on_message = on_mqtt_message
        mqttc.on_connect = on_mqtt_connect
        mqttc.on_publish = on_mqtt_publish
        mqttc.on_subscribe = on_mqtt_subscribe

        # Connect
        mqttc.username_pw_set(self.botId, self.secret)
        mqttc.connect("toby.cloud", 444)

        # Continue the network loop, exit when an error occurs
        rc = 0
        while rc == 0:
            rc = mqttc.loop()
        print("rc: " + str(rc))

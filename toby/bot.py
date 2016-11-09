import os, urlparse, time, json
import paho.mqtt.client as mqtt
from .message import Message
from .errors import ConnectionError
from .errors import CallbackError


class Bot:
    def __init__(self, id, sk):
        self.botId = id
        self.botSk = sk
        self.client = False
        self.on_message = False
        self.on_connect = False
        self.connected = False

    def set_on_connect(self, callback):
        """ set the bot's on connect callback
        """
        self.on_connect = callback

    def set_on_disconnect(self, callback):
        """ set the bot's on disconnect callback
        """
        self.on_disconnect = callback

    def set_on_message(self, callback):
        """ set the bot's on message callback
        """
        self.on_message = callback

    def start(self):
        """ attempt to establish MQTT connection with Toby server
        """
        if not self.on_connect or not self.on_disconnect or not self.on_message:
            raise CallbackError('set callbacks before starting')

        # Called when the client connects to broker
        def on_connect(client, userdata, flags, rc):
            self.connected = True
            self.client.subscribe('client/' + self.botId + '/#')
            self.on_connect()

        # Called when a PUBLISH message is received from the server.
        def on_message(client, userdata, msg):
            self.on_message(str(msg.payload))

        # Called when the client disconnects from the broker
        def on_disconnect(client, userdata, rc):
            self.connected = False
            self.on_disconnect()
            self.client.disconnect()

        self.client = mqtt.Client(client_id=self.botId)
        self.client.username_pw_set(self.botId, password=self.botSk)
        self.client.on_connect = on_connect
        self.client.on_disconnect = on_disconnect
        self.client.on_message = on_message
        self.client.connect('toby.cloud', 444, 60)

        try:
            # Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
            self.client.loop_forever()
        except KeyboardInterrupt:
            pass

    def end(self):
        """ break the connection with the Toby server
        """
        if not self.client or not self.connected:
            raise ConnectionError('Bot#end requires active connection')
        self.client.disconnect()

    def send(self, message):
        """ send a message
        """
        if not self.client or not self.connected:
            raise ConnectionError('Bot#follow requires active connection')
        if not isinstance(message, type(Message())):
            raise TypeError('Bot#send requires a message')
        if not message.is_empty():
            self.client.publish('server/' + self.botId + '/send', str(message))

    def follow(self, tags=[], ackTag=''):
        """ add bot subscriptions
        """
        if not self.client or not self.connected:
            raise ConnectionError('Bot#follow requires active connection')
        if not type(tags) is list:
            raise ValueError('Bot#follow requires a list')
        request = {'tags': tags, 'ackTag': ackTag or ''}
        self.client.publish('server/' + self.botId + '/follow', json.dumps(request))

    def unfollow(self, tags=[], ack_tag=''):
        """ remove bot subscriptions
        """
        if not self.client or not self.connected:
            raise ConnectionError('Bot#unfollow requires active connection')
        if not type(tags) is list:
            raise ValueError('Bot#unfollow requires a list')
        request = {'tags': tags, 'ackTag': ack_tag or ''}
        self.client.publish('server/' + self.botId + '/unfollow', json.dumps(request))

    def info(self, ackTag=''):
        """ get bot info
        """
        if not self.client or not self.connected:
            raise ConnectionError('Bot#info requires active connection')
        request = {'ackTag': ackTag or ''}
        self.client.publish('server/' + self.botId + '/info', json.dumps(request))

    def create_bot(self, id, sk, ack_tag):
        """ create a bot (users only)
        """
        if not self.client or not self.connected:
            raise ConnectionError('Bot#create_bot requires active connection')
        request = {'id': id, 'secret': sk, 'ackTag': ack_tag}
        self.client.publish('server/' + self.botId + '/create-bot', json.dumps(request))

    def create_socket(self, persist, ack_tag):
        """ create a socket (bots only)
        """
        if not self.client or not self.connected:
            raise ConnectionError('Bot#create_socket requires active connection')
        request = {'persist': persist, 'ackTag': ack_tag}
        self.client.publish('server/' + self.botId + '/create-socket', json.dumps(request))

    def remove_bot(self, target_id, ack_tag):
        """ remove a bot (users only)
        """
        if not self.client or not self.connected:
            raise ConnectionError('Bot#remove_bot requires active connection')
        request = {'botId': target_id, 'ackTag': ack_tag}
        self.client.publish('server/' + self.botId + '/remove-bot', json.dumps(request))

    def remove_socket(self, target_id, ack_tag):
        """ remove a socket (bots only)
        """
        if not self.client or not self.connected:
            raise ConnectionError('Bot#remove_socket requires active connection')
        request = {'botId': target_id, 'ackTag': ack_tag}
        self.client.publish('server/' + self.botId + '/remove-socket', json.dumps(request))

    def hooks_on(self, sk, ack_tag):
        """ turn bot hooks on
        """
        if not self.client or not self.connected:
            raise ConnectionError('Bot#hooks_on requires active connection')
        request = {'hookSecret': sk, 'ackTag': ack_tag}
        self.client.publish('server/' + self.botId + '/hooks-on', json.dumps(request))

    def hooks_off(self, ack_tag):
        """ turn bot hooks off
        """
        if not self.client or not self.connected:
            raise ConnectionError('Bot#hooks_off requires active connection')
        request = {'ackTag': ack_tag}
        self.client.publish('server/' + self.botId + '/hooks-off', json.dumps(request))

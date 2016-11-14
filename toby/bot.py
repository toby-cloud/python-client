import os, urlparse, time, json
import paho.mqtt.client as mqtt
from .message import Message
from .errors import ConnectionError
from .errors import CallbackError


class Bot:
    def __init__(self, id, sk):
        self.id = id
        self.sk = sk
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

    def __generate_mqtt_callbacks(self):
        """ generate the mqtt callbacks
        """
        if not self.on_connect or not self.on_disconnect or not self.on_message:
            raise CallbackError('bot callbacks not set')

        # Called when the client connects to broker
        def mqtt_on_connect(client, userdata, flags, rc):
            self.connected = True
            self.client.subscribe('client/' + self.id)
            self.on_connect()

        # Called when a PUBLISH message is received from the server.
        def mqtt_on_message(client, userdata, msg):
            m = Message()
            m.from_json_string(str(msg.payload))
            self.on_message(m)

        # Called when the client disconnects from the broker
        def mqtt_on_disconnect(client, userdata, rc):
            self.connected = False
            self.on_disconnect()
            self.client.disconnect()

        return [mqtt_on_connect, mqtt_on_disconnect, mqtt_on_message]

    def start(self):
        """ attempt to establish MQTT connection with Toby server
        """
        try:
            on_connect, on_disconnect, on_message = self.__generate_mqtt_callbacks()
        except CallbackError:
            raise CallbackError('set bot callbacks before starting')

        self.client = mqtt.Client(client_id=self.id)
        self.client.username_pw_set(self.id, password=self.sk)
        self.client.on_connect = on_connect
        self.client.on_disconnect = on_disconnect
        self.client.on_message = on_message
        self.client.connect('localhost', 1883, 60)

        try:
            self.client.loop_forever() # blocking call; dispatches callbacks; handles reconnecting
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
            req = {"payload": message.get_payload(), "tags": message.get_tags(), "ack": message.get_ack()}
            self.client.publish('server/' + self.id + '/send', json.dumps(req))

    def follow(self, tags=[], ack=''):
        """ add bot subscriptions
        """
        if not self.client or not self.connected:
            raise ConnectionError('Bot#follow requires active connection')
        if not type(tags) is list:
            raise ValueError('Bot#follow requires a list')
        request = {'tags': tags, 'ack': ack or ''}
        self.client.publish('server/' + self.id + '/follow', json.dumps(request))

    def unfollow(self, tags=[], ack=''):
        """ remove bot subscriptions
        """
        if not self.client or not self.connected:
            raise ConnectionError('Bot#unfollow requires active connection')
        if not type(tags) is list:
            raise ValueError('Bot#unfollow requires a list')
        request = {'tags': tags, 'ack': ack or ''}
        self.client.publish('server/' + self.id + '/unfollow', json.dumps(request))

    def info(self, ack=''):
        """ get bot info
        """
        if not self.client or not self.connected:
            raise ConnectionError('Bot#info requires active connection')
        request = {'ack': ack or ''}
        self.client.publish('server/' + self.id + '/info', json.dumps(request))

    def create_bot(self, id, sk, ack):
        """ create a bot (users only)
        """
        if not self.client or not self.connected:
            raise ConnectionError('Bot#create_bot requires active connection')
        request = {'id': id, 'sk': sk, 'ack': ack or ''}
        self.client.publish('server/' + self.id + '/create-bot', json.dumps(request))

    def create_socket(self, persist, ack):
        """ create a socket (bots only)
        """
        if not self.client or not self.connected:
            raise ConnectionError('Bot#create_socket requires active connection')
        if not ack:
            raise BotError('Bot#create_socket requires an ack tag')
        request = {'persist': persist, 'ack': ack}
        self.client.publish('server/' + self.id + '/create-socket', json.dumps(request))

    def remove_bot(self, target_id, ack):
        """ remove a bot (users only)
        """
        if not self.client or not self.connected:
            raise ConnectionError('Bot#remove_bot requires active connection')
        request = {'id': target_id, 'ack': ack or ''}
        self.client.publish('server/' + self.id + '/remove-bot', json.dumps(request))

    def remove_socket(self, target_id, ack):
        """ remove a socket (bots only)
        """
        if not self.client or not self.connected:
            raise ConnectionError('Bot#remove_socket requires active connection')
        request = {'id': target_id, 'ack': ack or ''}
        self.client.publish('server/' + self.id + '/remove-socket', json.dumps(request))

    def hooks_on(self, sk, ack):
        """ turn bot hooks on
        """
        if not self.client or not self.connected:
            raise ConnectionError('Bot#hooks_on requires active connection')
        request = {'sk': sk, 'ack': ack or ''}
        self.client.publish('server/' + self.id + '/hooks-on', json.dumps(request))

    def hooks_off(self, ack):
        """ turn bot hooks off
        """
        if not self.client or not self.connected:
            raise ConnectionError('Bot#hooks_off requires active connection')
        request = {'ack': ack or ''}
        self.client.publish('server/' + self.id + '/hooks-off', json.dumps(request))

import json

class Message:

    def __init__(self, sender="", payload={}, tags=[], ack=""):
        # default constructor
        self.sender = sender
        self.payload = payload
        self.tags = tags
        self.ack = ack

    def __str__(self):
        # convert to string
        m = {'from': self.sender, 'payload': self.payload, 'tags': self.tags, 'ack': self.ack}
        return json.dumps(m)

    def from_json_string(self, s):
        # create message from json string
        m = json.loads(s)
        try:
            self.__init__(m['from'], m['payload'], m['tags'], m['ack'])
        except KeyError:
            print(s)
            print("MALFORMED MESSAGE WARNING: creating empty message")
            self.__init__()

    def is_empty(self):
        # returns true if all fields are empty
        return str(self) == str(Message())

    def get_sender(self):
        return self.sender

    def get_payload(self):
        return self.payload

    def get_tags(self):
        return self.tags

    def get_ack(self):
        return self.ack

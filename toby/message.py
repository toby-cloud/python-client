import json

class Message:

    def __init__(self, payload="", type="", tags=[], ackTag=""):
        # default constructor
        self.payload = payload
        self.type = type
        self.tags = tags
        self.ackTag = ackTag

    def __str__(self):
        # convert to string

        # NOTE the Toby API will be changing soon
        m = {'message':self.payload, 'messageType': self.type, 'tags': self.tags, 'ackTag': self.ackTag}
        return json.dumps(m)

    def from_json_string(self, s):
        #
        m = json.loads(s)
        try:
            self.__init__(m['message'], m['messageType'], m['tags'], m['ackTag'])
        except KeyError:
            print("MALFORMED MESSAGE WARNING: creating empty message")
            self.__init__()

    def is_empty(self):
        # returns true if all fields are empty
        return str(self) == str(Message())

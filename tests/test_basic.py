import unittest
import json
import toby

# example on_connect callback
def on_connect():
    return True

# example on_message callback
def on_message(message):
    return message

class TestBotErrors(unittest.TestCase):

    def test_start_missing_callbacks(self):
        bot = toby.Bot("", "")
        with self.assertRaises(toby.CallbackError):
            bot.start()
        bot.set_on_message = on_message
        with self.assertRaises(toby.CallbackError):
            bot.start()

    def test_not_connected_send(self):
        bot = toby.Bot("", "")
        bot.set_on_connect = on_connect
        bot.set_on_message = on_message
        with self.assertRaises(toby.ConnectionError):
            bot.send("")

    def test_not_connected_follow(self):
        bot = toby.Bot("", "")
        bot.set_on_connect = on_connect
        bot.set_on_message = on_message
        with self.assertRaises(toby.ConnectionError):
            bot.follow("")


class TestMessage(unittest.TestCase):

    def test_empty(self):
        message = toby.Message()
        self.assertTrue(json.loads(str(message)) == json.loads('{"message":"","messageType":"","tags":[],"ackTag":""}'))

    def test_to_string_all_fields(self):
        message = toby.Message('hello', 'TEXT', ['tag1', 'tag2'], 'ack')
        self.assertTrue(json.loads(str(message)) == json.loads('{"message":"hello","messageType":"TEXT","tags":["tag1","tag2"],"ackTag":"ack"}'))

    def test_from_string(self):
        s = '{"message":"hello","messageType":"TEXT","tags":["tag1","tag2"],"ackTag":"ack"}'
        message = toby.Message('hello', 'TEXT', ['tag1', 'tag2'], 'ack')
        smessage = toby.Message()
        smessage.from_json_string(s)
        self.assertTrue(str(smessage) == str(message))

    def test_from_string_malformed(self):
        s = '{"mese":"he","mesype":"TET","tgs":["tag1","tag2"],"ag":"ack"}'
        message = toby.Message()
        message.from_json_string(s)
        self.assertTrue(message.is_empty())

    def test_empty_constructor_is_empty(self):
        self.assertTrue(toby.Message().is_empty())

    def test_from_string_is_empty(self):
        m = toby.Message()
        m.from_json_string('{"random":"values","that":"should not", "be": "loaded"}')
        self.assertTrue(m.is_empty())

if __name__ == '__main__':
    unittest.main()

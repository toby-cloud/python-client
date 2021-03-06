import unittest
import json
import toby

# example on_connect callback
def on_connect():
    return True

# example on_message callback
def on_message(message):
    return message

class TestBotCallbackErrors(unittest.TestCase):

    def test_start_missing_callbacks(self):
        bot = toby.Bot("", "")
        with self.assertRaises(toby.CallbackError):
            bot.start()
        bot.set_on_message = on_message
        with self.assertRaises(toby.CallbackError):
            bot.start()


class TestNotConnectedErrors(unittest.TestCase):

    def test_not_connected_end(self):
        bot = toby.Bot("", "")
        bot.set_on_connect = on_connect
        bot.set_on_message = on_message
        with self.assertRaises(toby.ConnectionError):
            bot.end()

    def test_not_connected_send(self):
        bot = toby.Bot("", "")
        bot.set_on_connect = on_connect
        bot.set_on_message = on_message
        with self.assertRaises(toby.ConnectionError):
            bot.send(toby.Message("asdf"))

    def test_not_connected_info(self):
        bot = toby.Bot("", "")
        bot.set_on_connect = on_connect
        bot.set_on_message = on_message
        with self.assertRaises(toby.ConnectionError):
            bot.info('ack')

    def test_not_connected_follow(self):
        bot = toby.Bot("", "")
        bot.set_on_connect = on_connect
        bot.set_on_message = on_message
        with self.assertRaises(toby.ConnectionError):
            bot.follow([])

    def test_not_connected_unfollow(self):
        bot = toby.Bot("", "")
        bot.set_on_connect = on_connect
        bot.set_on_message = on_message
        with self.assertRaises(toby.ConnectionError):
            bot.unfollow([])

    def test_not_connected_create_bot(self):
        bot = toby.Bot("", "")
        bot.set_on_connect = on_connect
        bot.set_on_message = on_message
        with self.assertRaises(toby.ConnectionError):
            bot.create_bot('botid', 'botsk', 'ack')

    def test_not_connected_create_socket(self):
        bot = toby.Bot("", "")
        bot.set_on_connect = on_connect
        bot.set_on_message = on_message
        with self.assertRaises(toby.ConnectionError):
            bot.create_socket(False, 'ack')

    def test_not_connected_remove_bot(self):
        bot = toby.Bot("", "")
        bot.set_on_connect = on_connect
        bot.set_on_message = on_message
        with self.assertRaises(toby.ConnectionError):
            bot.remove_bot('targetid', 'ack')

    def test_not_connected_remove_socket(self):
        bot = toby.Bot("", "")
        bot.set_on_connect = on_connect
        bot.set_on_message = on_message
        with self.assertRaises(toby.ConnectionError):
            bot.remove_socket('targetid', 'ack')

    def test_not_connected_hooks_on(self):
        bot = toby.Bot("", "")
        bot.set_on_connect = on_connect
        bot.set_on_message = on_message
        with self.assertRaises(toby.ConnectionError):
            bot.hooks_on('sk', 'ack')

    def test_not_connected_hooks_off(self):
        bot = toby.Bot("", "")
        bot.set_on_connect = on_connect
        bot.set_on_message = on_message
        with self.assertRaises(toby.ConnectionError):
            bot.hooks_off('ack')

class TestMessage(unittest.TestCase):

    def test_empty(self):
        message = toby.Message()
        self.assertTrue(json.loads(str(message)) == json.loads('{"from":"","payload":{},"tags":[],"ack":""}'))

    def test_to_string_all_fields(self):
        message = toby.Message('sender', {"hello":"world"}, ['tag1', 'tag2'], 'ack')
        self.assertTrue(json.loads(str(message)) == json.loads('{"from":"sender","payload":{"hello":"world"},"tags":["tag1","tag2"],"ack":"ack"}'))

    def test_from_string(self):
        s = '{"from":"sender","payload":{"hello":"world"},"tags":["tag1","tag2"],"ack":"ack"}'
        message = toby.Message('sender', {"hello":"world"}, ['tag1', 'tag2'], 'ack')
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

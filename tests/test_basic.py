import unittest
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

if __name__ == '__main__':
    unittest.main()

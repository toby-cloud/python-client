import unittest
<<<<<<< HEAD
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
=======

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
>>>>>>> 3979969cc0a0848763f59ca31a6fb41cbf2d6248

if __name__ == '__main__':
    unittest.main()


from toby_class import Toby

toby = Toby("", "")

def on_connect():
    toby.follow("#python");

def on_message(message):
    print "MESSAGE: " + message
    toby.send("got your message #bot1")

toby.set_on_connect(on_connect)
toby.set_on_message(on_message)
toby.start()

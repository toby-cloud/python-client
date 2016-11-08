
from toby import Bot

bot = Bot("python", "python")

def on_connect():
    #toby.follow("#python");
    print "connected"

def on_message(message):
    #print "MESSAGE: " + message
    #toby.send("got your message #bot1")
    print message

bot.set_on_connect(on_connect)
bot.set_on_message(on_message)
#bot.start()
#bot.send('something')

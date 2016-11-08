
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
<<<<<<< HEAD
#bot.start()
#bot.send('something')
=======
bot.start()
>>>>>>> 3979969cc0a0848763f59ca31a6fb41cbf2d6248

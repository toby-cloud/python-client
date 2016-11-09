
import toby

<<<<<<< HEAD
bot = toby.Bot("gabe2", "gabe2")

def on_connect():
    print "connected"
    bot.info("python")
    #bot.send(toby.Message("hey", "TEXT", ['asf'], 'python'))

def on_disconnect():
    print "disconnected"

=======
bot = toby.Bot("python", "python")

def on_connect():
    print "connected"
    bot.unfollow(["python"])
    bot.send(toby.Message("hey", "TEXT", ['asf'], 'python'))
>>>>>>> c9ef4b01bf15a764d8d5f16a2cc0693273cfdaf4

def on_message(message):
    #print "MESSAGE: " + message
    #toby.send("got your message #bot1")
    print message

bot.set_on_connect(on_connect)
bot.set_on_disconnect(on_disconnect)
bot.set_on_message(on_message)
bot.start()
#bot.send('something')

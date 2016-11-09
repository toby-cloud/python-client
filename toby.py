
import toby

bot = toby.Bot("gabe2", "gabe2")

def on_connect():
    print "connected"
    bot.info("python")
    #bot.send(toby.Message("hey", "TEXT", ['asf'], 'python'))

def on_disconnect():
    print "disconnected"


def on_message(message):
    #print "MESSAGE: " + message
    #toby.send("got your message #bot1")
    print message

bot.set_on_connect(on_connect)
bot.set_on_disconnect(on_disconnect)
bot.set_on_message(on_message)
bot.start()
#bot.send('something')

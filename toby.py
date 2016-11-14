
import toby

bot = toby.Bot("gbot2", "gbot2")


def on_disconnect():
    print "disconnected"

def on_connect():
    print "connected"
    bot.info("info")
    #bot.create_bot("gbot2", "gbot2", "create")
    #bot.create_socket(False, "socket")
    #bot.send(toby.Message("", {"hello":"world"}, ["vLX2WD3k", "gbot"], 'python'))
    #bot.follow(["gbot2"])
    #bot.unfollow(["gbot"])

def on_message(message):
    #print "MESSAGE: " + message
    #toby.send("got your message #bot1")
    print message

bot.set_on_connect(on_connect)
bot.set_on_disconnect(on_disconnect)
bot.set_on_message(on_message)
bot.start()

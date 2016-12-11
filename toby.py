
import toby

bot = toby.Bot("python", "python")

def on_disconnect():
    print "disconnected"

def on_connect():
    print "connected"
    bot.info("info")
    #bot.create_bot("", "", "create-bot")
    #bot.create_socket(False, "create-socket")
    #bot.send(toby.Message("", {"hello":"world"}, ["toby"], "python"))
    #bot.follow(["python"])
    #bot.unfollow(["python"])

def on_message(message):
    #print "MESSAGE: " + message
    #toby.send("got your message #bot1")
    print message

bot.set_on_connect(on_connect)
bot.set_on_disconnect(on_disconnect)
bot.set_on_message(on_message)
bot.start()

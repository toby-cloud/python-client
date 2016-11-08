
import toby

bot = toby.Bot("python", "python")

def on_connect():
    print "connected"
    bot.unfollow(["python"])
    bot.send(toby.Message("hey", "TEXT", ['asf'], 'python'))

def on_message(message):
    #print "MESSAGE: " + message
    #toby.send("got your message #bot1")
    print message

bot.set_on_connect(on_connect)
bot.set_on_message(on_message)
bot.start()
#bot.send('something')

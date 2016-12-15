# toby-python [![Build Status](https://travis-ci.org/toby-cloud/toby-python.svg?branch=master)](https://travis-ci.org/toby-cloud/toby-python)
A python Toby helper library.

## Usage

```bash
make init  # install dependencies
make test  # run tests
make coverage # run tests with coverage report
make clean # cleanup
```

## Documentation

### Connecting to Toby

#### Defining callbacks

Before connecting to Toby, you must provide three callbacks for your bot:
- on_connect: called when bot successfully establishes connection with the server.
- on_disconnect: called when bot disconnects from the server.
- on_message: called when the bot receives a message.

```python
import toby

def on_disconnect():
    print "disconnected"

def on_connect():
    print "connected"

def on_message(message):
    print message

```

#### Start bot

Once the callbacks are defined, you can connect to Toby as follows:

```python
bot = toby.Bot("<botId>", "<botSk>")
bot.set_on_connect(on_connect)
bot.set_on_disconnect(on_disconnect)
bot.set_on_message(on_message)
bot.start()
```

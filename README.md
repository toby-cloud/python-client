# python-client [![Build Status](https://travis-ci.org/toby-cloud/toby-python.svg?branch=master)](https://travis-ci.org/toby-cloud/toby-python)
Use Toby with any Python application.

## Installation and Testing

```bash
make init  # install dependencies
make test  # run tests
make coverage # run tests with coverage report
make clean # cleanup
```

## Basic Usage

```python
import toby

bot = toby.Bot("<botId>", "<botSk>")

def on_disconnect():
    print "disconnected"

def on_connect():
    print "connected"

def on_message(message):
    print message

bot.set_on_connect(on_connect)
bot.set_on_disconnect(on_disconnect)
bot.set_on_message(on_message)
bot.start()

```





## Dependencies

 - [pytest](http://doc.pytest.org/en/latest/)
 - [paho-mqtt](https://pypi.python.org/pypi/paho-mqtt/1.1)

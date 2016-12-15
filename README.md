# toby-python [![Build Status](https:#travis-ci.org/toby-cloud/toby-python.svg?branch=master)](https:#travis-ci.org/toby-cloud/toby-python)
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

### Send

To send a message, provide a JSON payload, a list of tags, and an ack tag.

```python
bot.send(toby.Message("", {"message":"hello world"}, ["tag"], 'ack'))
```

### Information

Get information about the bot.

```python
bot.info('info')
```

### Follow

Subscribe to tags (standard bots only).

```python
bot.follow(["tag1", "tag2"], "followed")); # tags, ack
```

### Unfollow

Unsubscribe from tags (standard bots only).

```python
bot.unfollow(["tag1", "tag2"]), "unfollowed"); # tags, ack
```

### Create Bot

Create a standard bot (users only).

```python
bot.create_bot("id", "sk", "created"); # botId, botSk, ack
```

### Create Socket

Create a socket bot (standard bots only).

```python
bot.create_socket(false, "created"); # persist, ack
```

### Remove Bot

Remove a standard bot (users only).

```python
bot.remove_bot("target_id", "removed"); # bot ID, ack
```

### Remove Socket

Remove a socket bot (standard bots only).

```python
bot.remove_socket("target_id", "removed"); # socket ID, ack
```

### Turn Hooks On

Enable web hooks (standard bots only);

```python
bot.hooks_on("hook_sk", "hooks_on"); # hook password, ack
```

### Turn Hooks Off

Disable web hooks (standard bots only);

```python
bot.hooks_off("hooks_off"); # hook password, ack
```

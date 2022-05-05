# 🤖 Mechagodzilla 🦖

## About

A discord bot built with [discord.py](https://discordpy.readthedocs.io)

## Features

### ❕Commands

- 🗨️ **Talks**: `hi`, `dm`!
- 💭 **Quotes**: `quote`!
- **Full list** of commands: [here](https://github.com/allanjsouza/mechagodzilla/blob/master/docs/COMMANDS.md).

### 🔔 Events

- React when mentioned

## Installation

These are the requirements for the bot.

- [Python 3.8.10](https://www.python.org/downloads) (Required packages listed in requirements.txt)

Setup your `.env` configuration file:

```sh
$ cp .env.example .env
```

Add yout own Discord `AUTH_TOKEN` (mandatory) and optionally setup your `COMMAND_PREFIX`. Then you should be able to start the bot by running:

```sh
python app
```

### Development

To start developing install `dev` dependencies:

```sh
# `make install` can also get the job done
pip install -e .['dev']
```

**Tests**

```sh
# Run tests
pytest tests/

# Run tests & coverage
pytest tests/ -v --cov=app # `make test`

# Coverage report
coverage html
```

## License

Released under the [MIT](https://github.com/allanjsouza/mechagodzilla/blob/master/LICENSE) license.

<h1><img src="https://user-images.githubusercontent.com/5806540/166961075-66690c37-eb4e-409d-9a5e-2b5799747ef4.png" alt="dev-bot"/> dev-bot</h1>

[![CI](https://github.com/allanjsouza/dev-bot/actions/workflows/ci.yml/badge.svg)](https://github.com/allanjsouza/dev-bot/actions/workflows/ci.yml)
[![Coverage Status](https://coveralls.io/repos/github/allanjsouza/dev-bot/badge.svg?branch=main)](https://coveralls.io/github/allanjsouza/dev-bot?branch=main)

## About

A discord bot built with [discord.py](https://discordpy.readthedocs.io)

## Features

### ❕Commands

- 🗨️ **Talks**: `hi`, `dm`!
- 💭 **Quotes**: `quote`!
- **Full list** of commands: [here](https://github.com/allanjsouza/dev-bot/blob/master/docs/COMMANDS.md).

### 🔔 Events

- React when mentioned

## Installation

These are the requirements for the bot.

- [Python 3.8.10](https://www.python.org/downloads) (Required packages listed in requirements.txt)

Setup your `.env` configuration file:

```sh
$ cp example.env .env
```

Add yout own Discord `AUTH_TOKEN` (mandatory) and optionally setup your `COMMAND_PREFIX`. Then you should be able to start the bot by running:

```sh
# Start the bot
python app/bot.py
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
pytest tests/ -v # or `make test`

# Run tests & coverage
pytest tests/ -v --cov=app

# Coverage report
coverage html

# Tip: use `make coverage` to run tests, coverage and browse the coverage report
```

## License

Released under the [MIT](https://github.com/allanjsouza/dev-bot/blob/master/LICENSE) license.

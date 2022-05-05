import os
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()

CMD_PREFIX = os.getenv("COMMAND_PREFIX") or "!"
DISCORD_TOKEN = os.getenv("AUTH_TOKEN")
EXT_DIRS = ["app.commands", "app.events", "app.tasks"]


def load_extensions(bot):
    for ext_path in EXT_DIRS:
        dir_path = ext_path.replace(".", "/")
        if not os.path.isdir(dir_path):
            continue

        for file in os.listdir(dir_path):
            if file.endswith(".py"):
                extension = f"{ext_path}.{file[:-3]}"
                bot.load_extension(extension)


load_extensions(__bot := commands.Bot(CMD_PREFIX))


def run():
    __bot.run(DISCORD_TOKEN)

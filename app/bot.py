import os
from discord.ext import commands

from app.config import Config

CMD_PREFIX = Config.COMMAND_PREFIX
DISCORD_TOKEN = Config.AUTH_TOKEN
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

if __name__ == "__main__":
    __bot.run(DISCORD_TOKEN)

from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument

from app.bot import CMD_PREFIX
from app.utils.logging import logger

HELP_MSG = f"Send `{CMD_PREFIX}help` to get instructions about available commands"


class Management(commands.Cog):
    """General bot management event listener"""

    def __init__(self, bot):
        self._bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(f"Logged in as {self._bot.user}")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self._bot.user:
            return

        if self._bot.user in message.mentions:
            await message.add_reaction("🦖")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            await ctx.send(f"Unknown command. {HELP_MSG}")
        elif isinstance(error, MissingRequiredArgument):
            await ctx.send(f"Missing argument(s). {HELP_MSG}")
        else:
            logger.error(str(error))
            await ctx.send(f"Sorry but something went wrong 🛠️")


def setup(bot):
    bot.add_cog(Management(bot))

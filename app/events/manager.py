from app.bot import CMD_PREFIX
from utils.logging import logger
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound


class Manager(commands.Cog):
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
            help = f"{CMD_PREFIX}help"
            await ctx.send(f"Unknown command. Send `{help}` to get instructions about available commands")


def setup(bot):
    bot.add_cog(Manager(bot))

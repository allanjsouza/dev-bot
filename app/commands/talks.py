import discord
from discord.ext import commands


class Talks(commands.Cog):
    """Talking commands"""

    def __init__(self, bot):
        self._bot = bot

    @commands.command(name="hi", help="Get a greeting message from bot")
    async def hello(self, ctx):
        await self.greet(ctx, ctx.author)

    @commands.command(name="dm",
                      help="Asks bot to send you a direct greeting message")
    async def direct_message(self, ctx):
        try:
            await self.greet(ctx.author, ctx.author)
        except discord.errors.Forbidden:
            await ctx.send("Unable to send you direct messages!")
            await ctx.send("Go to \"User Settings > Privacy & Safety\" and enable \"Allow direct messages from server members\"")

    async def greet(self, ctx, fellow):
        await ctx.send(f"Hello, {fellow.name}! 🦖")


def setup(bot):
    bot.add_cog(Talks(bot))

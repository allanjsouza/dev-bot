import discord
from discord.ext import commands

from app.services import quotes


class Quotes(commands.Cog):
    """Quoting commands"""

    def __init__(self, bot):
        self._bot = bot

    @commands.command(name="quote",
                      help=f"Get a random quote from {quotes.get_service_name()}")
    async def quote(self, ctx):
        try:
            quote = quotes.get_random_quote()
            embed = discord.Embed(
                description=f"_\"{quote.text}\"_\n- **{quote.author}**",
                color=0x00FF00
            )
            embed.set_footer(
                text=f"Random quote from {quotes.get_service_name()}")

            await ctx.send(embed=embed)

        except Exception as error:
            await ctx.send("Sorry, something went wrong")
            print(error)


def setup(bot):
    bot.add_cog(Quotes(bot))

from discord import Embed
from discord.ext import commands

from app.models.shouldideploy import ShouldideployMessage
from app.services import shouldideploy


class Fun(commands.Cog):
    """Fun commands"""

    def __init__(self, bot):
        self._bot = bot

    @commands.command(
        name="shouldideploy", help=f"Check if it is a good time to deploy"
    )
    async def shouldideploy(self, ctx):
        shouldideploy_msg = shouldideploy.check_shouldideploy()
        embed = Embed(
            title="Should I deploy today?",
            url=shouldideploy.get_service_url(),
            description=shouldideploy_msg.text,
            color=shouldideploy_msg.color,
        )
        embed.set_thumbnail(url=shouldideploy_msg.thumb_url)
        embed.set_footer(
            text=shouldideploy_msg.footer, icon_url=shouldideploy_msg.footer_icon
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Fun(bot))

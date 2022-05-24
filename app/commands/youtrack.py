from discord import Embed
from discord.ext import commands
from app.services.youtrack import handle_data
from app.services.youtrack import http


class YouTrack(commands.Cog):
    """YouTrack commands"""

    def __init__(self, bot):
        self._bot = bot

    @commands.command(name="issues", help="Get issues youtrack")
    async def hello(self, ctx):
        await self.greet(ctx, ctx.author)

    async def greet(self, ctx, fellow):
        test = http.url("7-12")

        story_points = handle_data.get_story_point(http.get(test))

        issues_count = handle_data.issues_count(http.get(test))

        critical_level = handle_data.critical_level(http.get(test))

        embed = Embed()

        embed.color = 0x00FF00

        embed.add_field(name="**Bugs By Priority** :ocean:",
                        value=critical_level)

        embed.add_field(name="**Bugs in Week** :cloud_rain:",
                        value=issues_count)

        embed.add_field(name="**Story Point** :sunny:", value=story_points)

        embed.set_footer(text="YouTrack Issues")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(YouTrack(bot))

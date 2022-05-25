from discord import Embed
from discord.ext import commands
from numpy import True_
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
        async with ctx.typing():
            test = http.url("7-12")

            story_points = handle_data.get_story_point(http.get(test))

            issues_count = handle_data.issues_count(http.get(test))

            critical_level = handle_data.critical_level(http.get(test))

            timer_solver_bugs = handle_data.solve_time_bugs(http.get(test))

            embed = Embed()

            embed.color = 0x00FF00

            embed.add_field(name="**Story Point** :sunny:",
                            value=f"Total: {story_points}",
                            inline=False)

            embed.add_field(name="**Bugs In Week** :cloud_rain:",
                            value=f"Total: {issues_count}",
                            inline=False)

            embed.add_field(name="**Bugs Production By Priority** :ocean:",
                            value=critical_level,
                            inline=False)

            embed.add_field(name="**Average Time Solve Bugs in Production** :timer:",
                            value=timer_solver_bugs,
                            inline=False)

            embed.set_footer(text="YouTrack Issues")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(YouTrack(bot))

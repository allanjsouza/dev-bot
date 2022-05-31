from discord import Embed
from discord.ext import commands

from app.config import Config
from app.services.youtrack import call_api, handle_data

SOLVE_WEEK = Config.SOLVE_WEEK
SOLVE_BUGS_PROJECT = Config.SOLVE_BUGS_PROJECT
SOLVE_BUGS_PROD = Config.SOLVE_BUGS_PROD


class YouTrack(commands.Cog):
    """YouTrack commands"""

    def __init__(self, bot):
        self._bot = bot

    @commands.command(name="issues", help="Get issues youtrack")
    async def hello(self, ctx):
        await self.greet(ctx, ctx.author)

    async def greet(self, ctx, fellow):
        async with ctx.typing():
            solve_week = call_api.url(SOLVE_WEEK)

            solve_bugs_project = call_api.url(SOLVE_BUGS_PROJECT)

            solve_bugs_prod = call_api.url(SOLVE_BUGS_PROD)

            story_points = handle_data.get_story_point(call_api.get(solve_week))

            bugs_count_in_week = handle_data.issues_count(call_api.get(solve_bugs_prod))

            critical_level = handle_data.critical_level(
                call_api.get(solve_bugs_project)
            )

            timer_solver_bugs = handle_data.solve_time_bugs(
                call_api.get(solve_bugs_prod)
            )

            embed = Embed()

            embed.color = 0x00FF00

            embed.add_field(
                name="**Story point this week** :sunny:",
                value=f"**Total:** {story_points}",
                inline=False,
            )

            if bugs_count_in_week != 0:
                embed.add_field(
                    name="**Bugs in week** :cloud_rain:",
                    value=bugs_count_in_week,
                    inline=False,
                )
            else:
                embed.add_field(
                    name="**Don't have bugs in week** :tada:",
                    value=":rocket:",
                    inline=False,
                )

            if timer_solver_bugs != 0 and critical_level != 0:
                embed.add_field(
                    name="**Production bugs by priority this week** :ocean:",
                    value=critical_level,
                    inline=False,
                )

                embed.add_field(
                    name="**Average time solve bugs in production this week** :timer:",
                    value=timer_solver_bugs,
                    inline=False,
                )
            else:
                embed.add_field(
                    name="**Don't have bugs in production** :tada:",
                    value=":t_rex:",
                    inline=False,
                )

            embed.set_footer(text="YouTrack Issues")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(YouTrack(bot))

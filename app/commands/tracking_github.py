from app.services.scm import scm
from discord import Embed
from discord.ext import commands


class GitHubTracking(commands.Cog):
    def __init__(self, bot):
        self._bot = bot
        self._provider = scm.get_provider()

    @commands.command(name="tracking", help="GitHub Tracking Pull Requests")
    async def quote(self, ctx, repo):
        async with ctx.typing():
            (days, hours, mins, total) = self._provider.get_all_pull_requests(repo)
            pullRequestWeek =  self._provider.get_open_pr_this_week(repo)

            embed = Embed()
            embed.color = 0x00FF00
            embed.add_field(
                inline=False,
                name="Tracking Time",
                value=f"Days: {days}\nHours: {hours}\nMinutes: {mins}\nTotal Issues: {total}"
            )

            embed.add_field(
                inline=False,
                name="Pull Request",
                value=f"Open's in week: {pullRequestWeek}"
            )

            await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(GitHubTracking(bot))

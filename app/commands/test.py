from app.services.scm import scm
from discord.ext import commands


class Testing(commands.Cog):
    """Quoting commands"""

    def __init__(self, bot):
        self._bot = bot
        self._provider = scm.get_provider()

    @commands.command(name="ok", help="Testing to test?")
    async def quote(self, ctx, repo):
        async with ctx.typing():
            (a, b, c, d) = self._provider.get_all_pull_requests(repo)
            await ctx.send(f"A: {a}\nB: {b}\nC: {c}\nD: {d}")

        async with ctx.typing():
            result =  self._provider.get_open_pr_this_week(repo)
            await ctx.send(result)


def setup(bot):
    bot.add_cog(Testing(bot))

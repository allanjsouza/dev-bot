from discord.ext import commands

from app.helpers.pull_request import generate_embed_from
from app.models.pull_request import PullRequest
from app.services.scm import scm
from app.services.scm.errors import RepoNotFoundError


def is_draft(pull_request: PullRequest) -> bool:
    return pull_request.draft


class Scm(commands.Cog):
    """Source code management commands"""

    def __init__(self, bot):
        self._bot = bot
        self._provider = scm.get_provider()

    @commands.command(
        name="pulls", help="Get the opened pull requests on specified repo"
    )
    async def pulls(self, ctx, repo):
        try:
            open_pulls = self._provider.get_open_pull_requests(repo)
            if not open_pulls:
                await ctx.send(f"There is no open pull request on repo `{repo}`")
            for pull in open_pulls:
                embed = generate_embed_from(pull)
                await ctx.send(embed=embed)
        except RepoNotFoundError:
            await ctx.send(f"Sorry but I could not find repo `{repo}`")


def setup(bot):
    bot.add_cog(Scm(bot))

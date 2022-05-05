import discord
from discord.ext import commands

reaction_role_mapping = {
    "🦖": "member",
    "🧑‍💻": "tech",
    "🤙": "oncall"
}


class Reactions(commands.Cog):
    """Reactions event listener"""

    def __init__(self, bot):
        self._bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        try:
            role_name = reaction_role_mapping.get(reaction.emoji, None)
            if role_name and (role := self.get_role(role_name, user.guild)):
                await user.add_roles(role)
        except discord.errors.Forbidden:
            await reaction.message.channel.send(f"Unable to add roles to {user.name}")

    def get_role(self, role_name, guild):
        for role in guild.roles:
            if role.name == role_name:
                return role

        return None


def setup(bot):
    bot.add_cog(Reactions(bot))

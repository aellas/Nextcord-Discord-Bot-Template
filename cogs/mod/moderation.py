import nextcord
from nextcord.ext import commands, application_checks

class ClearCog(commands.Cog):
    def __init__(self, bot: commands.bot):
     self.bot = bot
     
    @nextcord.slash_command(name="clear", description="Purge messages")
    @application_checks.has_permissions(manage_messages=True)
    async def clear(self, interaction: nextcord.Interaction, amount: int):
        await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(f"Cleared {amount} messages")
        
    @nextcord.slash_command(name="ban", description="Ban user")
    @application_checks.has_permissions(ban_members=True)
    async def ban(self, interaction: nextcord.Interaction, user: nextcord.User, reason: str):
        await user.ban(reason=reason)
        await interaction.response.send_message(f"Banned {user}")
        
    @nextcord.slash_command(name="kick", description="Kick user")
    @application_checks.has_permissions(kick_members=True)
    async def kick(self, interaction: nextcord.Interaction, user: nextcord.User, reason: str):
        await user.kick(reason=reason)
        await interaction.response.send_message(f"Kicked {user}")
        
def setup(bot):
    bot.add_cog(ClearCog(bot))
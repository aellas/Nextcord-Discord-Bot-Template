import nextcord
from nextcord.ext import commands

class PingCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Simple ping pong command, just for fun
    @nextcord.slash_command(name="ping", description="pong")
    async def ping(self, interaction: nextcord.Interaction):
        # If you use [slash command] /ping (in discord), the bot will respond with pong
        await interaction.response.send_message("Pong!")
        
def setup(bot):
    bot.add_cog(PingCog(bot))
        
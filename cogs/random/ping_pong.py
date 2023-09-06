# Import necessary components from nextcord
import nextcord
from nextcord.ext import commands

# Define a custom Cog class that extends commands.Cog
class PingCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Define a slash command named "ping" with the description "pong"
    @nextcord.slash_command(name="ping", description="pong")
    async def ping(self, interaction: nextcord.Interaction):
        # When the command is invoked, the bot responds with "Pong!"
        await interaction.response.send_message("Pong!")
        
# Define a setup function to add the Cog to the bot
def setup(bot):
    bot.add_cog(PingCog(bot))

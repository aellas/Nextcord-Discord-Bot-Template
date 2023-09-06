# Import necessary components from nextcord
import nextcord
from nextcord.ext import commands

# Define a custom Cog class that extends commands.Cog
class ExampleSlashCommandCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Define a slash command using the @nextcord.slash_command decorator
    @nextcord.slash_command(name="test", description="test")
    async def test(self, interaction: nextcord.Interaction):
        # Respond to the slash command with a message
        await interaction.response.send_message("test")

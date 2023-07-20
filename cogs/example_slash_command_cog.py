import nextcord
from nextcord.ext import commands

class ExampleSlashCommandCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @nextcord.slash_command(name="test", description="test")
    async def test(self, interaction: nextcord.Interaction):
        await interaction.response.send_message("test")
        
    """
    This will enable to use the slash commands globally (servers that the bot is in)
    You can also limit the slash command to only be used in a specific server using guilds=
    see below how to add that function
    
    TESTING_GUILD_ID = YOURGUILDID
    @nextcord.slash_command(name="test", description="test", guilds=[TESTING_GUILD_ID])
    
    To get your GUILD_ID:
    Right click your server name and click 'Copy Server ID'
    """
 
        
def setup(bot):
    bot.add_cog(ExampleSlashCommandCog(bot))
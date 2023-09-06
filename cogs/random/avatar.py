# Import necessary components from nextcord
import nextcord
from nextcord.ext import commands

# Define a custom Cog class that extends commands.Cog
class AvatarCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    # Define a slash command named "avatar" with the description "Get the avatar of a user"
    @nextcord.slash_command(name="avatar", description="Get the avatar of a user")
    async def avatar(self, interaction: nextcord.Interaction, user: nextcord.User):
        # When the "avatar" command is invoked, the bot sends the URL of the user's avatar
        await interaction.response.send_message(user.avatar.url)
        
# Define a setup function to add the Cog to the bot
def setup(bot):
    bot.add_cog(AvatarCog(bot))

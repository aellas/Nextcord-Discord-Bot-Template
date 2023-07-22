import nextcord
from nextcord.ext import commands

class AvatarCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @nextcord.slash_command(name="avatar", description="Get the avatar of a user")
    async def avatar(self, interaction: nextcord.Interaction, user: nextcord.User):
        await interaction.response.send_message(user.avatar.url)
          

        
def setup(bot):
    bot.add_cog(AvatarCog(bot))
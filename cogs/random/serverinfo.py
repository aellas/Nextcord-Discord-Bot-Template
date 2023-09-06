# Import necessary components from nextcord
import nextcord
from nextcord.ext import commands

# Define a custom Cog class that extends commands.Cog
class ServerInfoCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Define a slash command to get basic server information
    @nextcord.slash_command(name="server_info", description="Get server info")
    async def basic_serverinfo(self, interaction: nextcord.Interaction):
        # Create an embed to display server information
        embed = nextcord.Embed(color=nextcord.Color.blurple())
        embed.set_author(name=interaction.guild.name, icon_url=interaction.guild.icon.url)
        embed.add_field(name="Owner", value=interaction.guild.owner, inline=True)
        embed.add_field(name="Member Count", value=interaction.guild.member_count, inline=True)
        embed.add_field(name="Role Count", value=len(interaction.guild.roles), inline=True)
        embed.add_field(name="Server Level", value=interaction.guild.premium_tier, inline=True)
        embed.add_field(name="Boost Count", value=f"{interaction.guild.premium_subscription_count}/14", inline=True)
        embed.add_field(name="Channel Count", value=len(interaction.guild.channels), inline=True)
        embed.add_field(name="Description", value=interaction.guild.description, inline=False)
        embed.set_footer(text=interaction.guild.id, icon_url="https://cryptologos.cc/logos/space-id-id-logo.png")

        embed.set_thumbnail(url=interaction.guild.icon.url)
        
        # Send the embed as a response to the interaction
        await interaction.response.send_message(embed=embed)

# Define a setup function to add the Cog to the bot
def setup(bot):
    bot.add_cog(ServerInfoCog(bot))

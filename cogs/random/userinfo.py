# Import necessary components from nextcord
import nextcord
from nextcord.ext import commands
from nextcord.utils import format_dt

# Define a custom Cog class that extends commands.Cog
class UserinfoCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Define a slash command to get basic user information
    @nextcord.slash_command(name="basic_userinfo", description="Get basic information on a user")
    async def basicuserinfo(self, interaction: nextcord.Interaction, user: nextcord.User):
        await interaction.response.send_message(f"Name: {user.name}\nID: {user.id}\nAccount created at: {user.created_at}")
        
    # Define a slash command to get advanced user information
    @nextcord.slash_command(name="advanced_userinfo", description="More advanced userinfo command")
    async def advanceduserinfo(self, interaction: nextcord.Interaction, user: nextcord.User):
        # Various information about the user
        bot = str(user.bot).replace("False", "User").replace("True", "Bot")
        created = format_dt(user.created_at, "R")
        joined = format_dt(interaction.user.joined_at, "R")
        roles = [role.mention for role in user.roles if role.name != "@everyone"]
        role = str(roles).replace("[", "").replace("]", "").replace("'", "").replace(",", " ")
        status = str(user.status).replace("dnd", "<:dnd_badge:1132382322218508349> DND").replace("online", "<:online_badge:1132382196590714880> Online").replace("idle", "<:idle_badge:1132382200155881603> Idle").replace("offline", "<:offline_badge:1132382195097550868> Offline")

        # User badges based on public_flags
        badges = ""
        if user.public_flags.staff:
            badges += "<:discord_staff:1132379154654957669> "
        if user.public_flags.partner:
            badges += "<:partner:1132378094855004160> "
        if user.public_flags.hypesquad:
            badges += "<:hypesquad:1132378611635191828> "
        # Add more badge checks as needed

        # Create an embed to display user information
        embed = nextcord.Embed(color=nextcord.Color.blurple())
        embed.set_author(name=user.name, icon_url="https://cdn3.emoji.gg/emojis/2986-discord-username.png")
        embed.set_thumbnail(url=user.avatar)
        embed.set_footer(text=user.id, icon_url="https://cryptologos.cc/logos/space-id-id-logo.png")
        embed.add_field(name="User Mention", value=user.mention, inline=True)
        embed.add_field(name="User or Bot?", value=bot, inline=True)
        embed.add_field(name="Account Created", value=created, inline=True)
        embed.add_field(name="User Status", value=status, inline=True)
        embed.add_field(name="Server Position", value=f"{interaction.guild.members.index(user)}/{len(interaction.guild.members)}", inline=True)
        embed.add_field(name="Joined Server", value=joined, inline=True)
        embed.add_field(name="User Badges", value=badges, inline=True)
        embed.add_field(name="User Roles", value=role, inline=False)

        # Send the embed as a response to the interaction
        await interaction.response.send_message(embed=embed)

# Define a setup function to add the Cog to the bot
def setup(bot):
    bot.add_cog(UserinfoCog(bot))

import nextcord
from nextcord.ext import commands, application_checks

# Define a class called ClearCog that inherits from commands.Cog
class ClearCog(commands.Cog):
    # Initialize the ClearCog class with a reference to the bot
    def __init__(self, bot: commands.bot):
        self.bot = bot

    # Define a slash command named "clear" with a description
    # This command purges a specified number of messages
    @nextcord.slash_command(name="clear", description="Purge messages")
    # Check if the user has the permission to manage messages
    @application_checks.has_permissions(manage_messages=True)
    # Define a coroutine function for the "clear" command
    async def clear(self, interaction: nextcord.Interaction, amount: int):
        # Purge (delete) the specified number of messages in the channel
        await interaction.channel.purge(limit=amount)
        # Send a response message indicating the number of messages cleared
        await interaction.response.send_message(f"Cleared {amount} messages")

    # Define a slash command named "ban" with a description
    # This command bans a user with an optional reason
    @nextcord.slash_command(name="ban", description="Ban user")
    # Check if the user has the permission to ban members
    @application_checks.has_permissions(ban_members=True)
    # Define a coroutine function for the "ban" command
    async def ban(self, interaction: nextcord.Interaction, user: nextcord.User, reason: str):
        # Ban the specified user with an optional reason
        await user.ban(reason=reason)
        # Send a response message indicating the user has been banned
        await interaction.response.send_message(f"Banned {user}")

    # Define a slash command named "kick" with a description
    # This command kicks a user with an optional reason
    @nextcord.slash_command(name="kick", description="Kick user")
    # Check if the user has the permission to kick members
    @application_checks.has_permissions(kick_members=True)
    # Define a coroutine function for the "kick" command
    async def kick(self, interaction: nextcord.Interaction, user: nextcord.User, reason: str):
        # Kick the specified user with an optional reason
        await user.kick(reason=reason)
        # Send a response message indicating the user has been kicked
        await interaction.response.send_message(f"Kicked {user}")

# Define a function called setup that takes the bot as an argument
def setup(bot):
    # Add the ClearCog class as a cog to the bot
    bot.add_cog(ClearCog(bot))

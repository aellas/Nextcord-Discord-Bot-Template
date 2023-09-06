# Import necessary components from nextcord.ext
from nextcord.ext import commands

# Define a custom Cog class that extends commands.Cog
class ExampleCogListenerCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Define an event listener using the @commands.Cog.listener() decorator
    @commands.Cog.listener()
    async def on_message(self, message):
        
        # Check if the message author is the bot itself, and if so, do nothing
        if message.author == self.bot.user:
            return
        
        # Check if the message content is "example_cog_listener"
        if message.content == "example_cog_listener":
            # Send a response message to the same channel
            await message.channel.send("example_cog_listener")

# Define a setup function that adds the Cog to the bot
def setup(bot):
    bot.add_cog(ExampleCogListenerCog(bot))

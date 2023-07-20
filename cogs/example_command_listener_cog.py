from nextcord.ext import commands

class ExampleCogListenerCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        
        # If the listener detectes a message, but the author is bot, do nothing.
        if message.author == self.bot.user:
            return
        
        # if the listener detects the string "example_cog_listener", return the message
        if message.content == "example_cog_listener":
            await message.channel.send("example_cog_listener")
        
def setup(bot):
    bot.add_cog(ExampleCogListenerCog(bot))
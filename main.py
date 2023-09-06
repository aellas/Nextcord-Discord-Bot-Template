# Import necessary libraries
import json
import logging
import nextcord
from nextcord.ext import commands

# Function to load the bot's configuration from a JSON file
def load_configuration():
    try:
        with open("json/configuration.json", "r") as config_file:
            data = json.load(config_file)
            token = data["token"]
            prefix = data["prefix"]
        return token, prefix
    except FileNotFoundError:
        logging.error("Configuration file not found.")
        return None
    except json.JSONDecodeError:
        logging.error("Error decoding configuration file.")
        return None

# Function to set up logging for the bot
def setup_logging():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s  %(message)s")
    file_handler = logging.FileHandler("bot.log")
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logging.getLogger("").addHandler(file_handler)

# Function to load bot extensions (cogs)
def load_extensions(client, extensions):
    for extension in extensions:
        try:
            client.load_extension(extension)
            logging.info(f"Loaded {extension}")
        except commands.ExtensionError as e:
            logging.error(f"Failed to load {extension}: {e}")

# Load the bot's configuration (token and prefix) from the JSON file
token, prefix = load_configuration()

# Check if the configuration was successfully loaded
if token and prefix:
    # Set up Discord bot intents
    intents = nextcord.Intents.default()
    intents.members = True
    intents.presences = True
    intents.message_content = True
    
    # Create a Discord bot instance with the specified command prefix and intents
    client = commands.Bot(command_prefix=prefix, help_command=None, intents=intents)

    # Event handler for when the bot is ready
    @client.event
    async def on_ready():
        await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing, name='nextcord template'))

    if __name__ == "__main__":
        # Set up logging for the bot
        setup_logging()
        
        # List of bot extensions (cogs) to load
        extensions = [
            'cogs.random.ping_pong',
            'cogs.random.avatar',
            'cogs.random.userinfo',
            'cogs.mod.moderation',
            'cogs.random.serverinfo',
        ]
        
        # Load the specified extensions (cogs)
        load_extensions(client, extensions)
        
        # Start the bot using the provided token
        client.run(token)
        logging.info("Bot started")
else:
    logging.error("Failed to load configuration.")
